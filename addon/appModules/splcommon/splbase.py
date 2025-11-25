# SPL Studio base services
# An app module and global plugin package for NVDA
# Copyright 2018-2026 Joseph Lee, released under GPL.

# Base services for Studio app module and support modules
# These include Studio API handler, layer commands manager, and base track item class.

import ctypes
from functools import wraps
from abc import abstractmethod
import enum
import ui
import api
import windowUtils
import scriptHandler
import globalVars
from winUser import sendMessage
from logHandler import log
from NVDAObjects.IAccessible import sysListView32
import addonHandler
# From NVDA 2026.1 onwards, winBindings package should be used to look for Windows API dll's.
try:
	from winBindings.user32 import dll as user32
except ModuleNotFoundError:
	from winUser import user32

addonHandler.initTranslation()

# The API handler requires Studio components to define their own API's.
# This is the case for local (original) and Remote Studio.
class StudioAPIAvailability(enum.IntEnum):
	NOAPI = 0  # No API, screen traversal is required
	LOCALAPI = 1  # Local (original) Studio
	REMOTEAPI = 2  # Remote Studio


# Record window handles for local and Remote Studio for use from API handlers.
_SPLWindowHandles: dict[str, int | None] = {}

# Various SPL IPC tags.
SPLSelectTrack = 121

# Check if Studio itself is running.
# This is to make sure custom commands for SPL Assistant commands
# and other app module gestures display appropriate error messages.
# Some checks will need to omit message output.
def studioIsRunning(justChecking: bool = False, splComponent: str = "splstudio") -> bool:
	global _SPLWindowHandles
	# Keep the boolean flag handy because of message output.
	hwnd = _SPLWindowHandles.get(splComponent)
	isStudioAlive = (hwnd is not None and hwnd == user32.FindWindowW(splComponent, None)) or (
		hwnd is None and user32.FindWindowW(splComponent, None) not in (
			0,  # NVDA 2025.3 and earlier (returns 0 if handle is not found)
			None  # NVDA 2026.1 and later (returns None if handle is not found)
		)
	)
	if not isStudioAlive:
		log.debug(f"SPL: Studio ({splComponent}) is not alive")
		if not justChecking:
			# Translators: A message informing users that Studio is not running so certain commands will not work.
			ui.message(_("Studio main window not found"))
	return isStudioAlive


# Set Studio window handle to the given value so the handle itself can remain private.
def setStudioWindowHandle(hwnd: int | None, splComponent: str = "splstudio") -> None:
	global _SPLWindowHandles
	if hwnd:
		_SPLWindowHandles[splComponent] = hwnd
	else:
		del _SPLWindowHandles[splComponent]


# Use SPL Studio API to obtain needed values.
# A thin wrapper around user32.SendMessage function with Studio handle and WM_USER supplied.
# #45: returns whatever result SendMessage function says.
# If NVDA is in debug mode, print arg, command and other values if accompanied by "--spl-apidebug" option.
# Strengthen this by checking for the handle once more.
# #92: SendMessage function returns something from anything (including from dead window handles),
# so really make sure Studio window handle is alive.
def studioAPI(arg: int, command: int, splComponent: str = "splstudio") -> int | None:
	global _SPLWindowHandles
	if not studioIsRunning(justChecking=True, splComponent=splComponent):
		return None
	# Global plugin can also call this function with no Studio window handle value defined.
	# The global plugin can call API for any SPL component that supports API calls.
	hwnd = _SPLWindowHandles.get(splComponent)
	if hwnd is None:
		hwnd = user32.FindWindowW(splComponent, None)
		_SPLWindowHandles[splComponent] = hwnd
	if (studioAPIDebug := "--spl-apidebug" in globalVars.unknownAppArgs):
		log.debug(f"SPL: Studio API wParem is {arg}, lParem is {command}")
	val = sendMessage(hwnd, 1024, arg, command)
	# 64-bit NVDA: Studio API results max out at 32 bits.
	# Is the most significant bit set to 1 (signed integer but NVDA says unsigned)?
	# This results in 32-bit overflow or erroneous messages when a negative integer is expected.
	if val >= 0x80000000:
		# Convert the value into a signed 32-bit integer.
		val = ctypes.c_int32(val).value
	if studioAPIDebug:
		log.debug(f"SPL: Studio API result is {val}")
	# SendMessage function might be stuck while Studio exits, resulting in NULL window handle.
	if not user32.FindWindowW(splComponent, None):
		val = None
		log.debug("Studio window is gone, Studio API result is None")
	return val


# Select a track upon request.
def selectTrack(trackIndex: int) -> None:
	studioAPI(-1, SPLSelectTrack)
	log.debug(f"SPL: selecting track index {trackIndex}")
	studioAPI(trackIndex, SPLSelectTrack)


# Switch focus to SPL Studio window from anywhere.
def focusToSPLWindow(studioWindowChecked: bool = False) -> None:
	# Don't do anything if we're already focus on SPL Studio.
	# Only check if the caller did not check focused object first.
	if not studioWindowChecked and "splstudio" in api.getForegroundObject().appModule.appName:
		return
	try:
		studioWindow = windowUtils.findDescendantWindow(
			api.getDesktopObject().windowHandle, visible=True, className="TStudioForm"
		)
		user32.SetForegroundWindow(studioWindow)
	except LookupError:
		# Translators: presented when SPL Studio window is minimized.
		ui.message(_("SPL Studio is minimized to system tray."))


# The finally function for status announcement scripts in this module (source: Tyler Spivey's code).
def finally_(func, final):
	"""Calls final after func, even if it fails."""

	def wrap(f):
		@wraps(f)
		def new(*args, **kwargs):
			try:
				func(*args, **kwargs)
			finally:
				final()

		return new

	return wrap(final)


# SPL Playlist item (SPL add-on base object)
# #65: this base class represents trakc items
# across StationPlaylist suites such as Studio, Creator and Track Tool.
class SPLTrackItem(sysListView32.ListItem):
	"""An abstract class representing track items across SPL suite of applications
	including Studio, Creator, Track Tool, and Remote VT.
	This base class provides common properties, scripts, and methods such as Columns Explorer and others.
	Subclasses should provide custom routines for various attributes, including global ones to suit their needs.

	Each subclass, housed in app modules, is named after the app module name where tracks are encountered,
	such as SPLStudioTrackItem for Studio.
	Subclasses of module-specific subclasses are named after SPL version, for example
	SPL510TrackItem for studio 5.10 if version-specific handling is required.
	Classes representing different parts of an app are given descriptive names such as
	StudioPlaylistViewerItem for tracks found in Studio's Playlist Viewer (main window).
	"""

	# #103: provide an abstract index of function.
	@abstractmethod
	def indexOf(self, columnHeader: str) -> int | None:
		return None

	@scriptHandler.script(
		description=_(
			# Translators: input help mode message for column explorer commands.
			"Pressing once announces data for a track column, "
			"pressing twice will present column data in a browse mode window"
		),
		# Script decorator can take in a list of gestures, thus take advantage of it.
		gestures=[f"kb:control+nvda+{i}" for i in range(10)],
		category=_("StationPlaylist"),
		speakOnDemand=True,
	)
	def script_columnExplorer(self, gesture):
		# Due to the below formula, columns explorer will be restricted to number commands.
		columnPos = int(gesture.displayName.split("+")[-1])
		if columnPos == 0:
			columnPos = 10
		# #115: do not proceed if parent list reports less than 10 columns.
		if columnPos > self.parent.columnCount:
			log.debug(f"SPL: column {columnPos} is out of range for this item")
			# Translators: Presented when column is out of range.
			ui.message(_("Column {columnPosition} not found").format(columnPosition=columnPos))
			return
		columnPos -= 1
		header = None
		# Search for the correct column (child object) based on the header from explore columns list.
		# Because of this, track items must expose individual columns as child objects.
		if hasattr(self, "exploreColumns"):
			# Sometimes, odd Unicode characters such as up arrow (↑) are present.
			# This is seen when items are sorted by columns in ascending and descending order.
			columnHeaders = [child.columnHeaderText.strip("↑↓") for child in self.children]
			header = self.exploreColumns[columnPos]
			# Consult more concrete track item classes about column header changes shown on screen.
			if hasattr(self, "updateColumnHeader"):
				header = self.updateColumnHeader(header)
			if header not in columnHeaders:
				# Translators: Presented when a specific column header is not found.
				ui.message(_("{headerText} not found").format(headerText=header))
				return
			columnPos = columnHeaders.index(header)
		column = self.getChild(columnPos)
		columnContent = column.name
		if header is None:
			header = column.columnHeaderText
		# Empty string (or None) is column content, so make no distinction.
		# However, if column content is None (seen when NVDA restarts while focused on a track item),
		# None will become an empty string ("").
		if columnContent is None:
			columnContent = ""
		columnData = f"{header}: {columnContent}"
		# #61: pressed once will announce column data, twice will present it in a browse mode window.
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(columnData)
		else:
			# Translators: Title of the column data window.
			ui.browseableMessage(columnData, title=_("Track data"), closeButton=True)

	@scriptHandler.script(
		# Translators: input help mode message for columns viewer command.
		description=_("Presents data for all columns in the currently selected track"),
		gesture="kb:control+NVDA+-",
	)
	def script_trackColumnsViewer(self, gesture):
		# Fetch column headers and texts from child columns,
		# meaning columns viewer will reflect visual display order.
		columnContents = [
			"{}: {}".format(
				column.columnHeaderText, column.name if column.name is not None else ""
			) for column in self.children
		]
		# Translators: Title of the column data window.
		ui.browseableMessage("\n".join(columnContents), title=_("Track data"), closeButton=True)

	# A friendly way to report track position via location text.
	def _get_locationText(self):
		# Translators: location text for a playlist item (example: item 1 of 10).
		return _("Item {current} of {total}").format(
			current=self.IAccessibleChildID, total=self.parent.rowCount
		)
