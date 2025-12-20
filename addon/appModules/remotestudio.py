# StationPlaylist Remote Studio
# An app module and global plugin package for NVDA
# Copyright 2025-2026 Joseph Lee, released under GPL.

# Basic support for StationPlaylist Remote Studio.
# Borrows heavily from Studio as the user interface is quite similar with changes specific to Remote Studio.

from typing import Any
import collections
import time
import threading
import ui
import tones
import api
import controlTypes
import queueHandler
# From NVDA 2026.1 onwards, winBindings package should be used to look for Windows API dll's.
try:
	from winBindings.user32 import dll as user32
except ModuleNotFoundError:
	from winUser import user32
from logHandler import log
from NVDAObjects import NVDAObject
from . import splstudio
from .splcommon import splconfig, splbase, splcarts

# Various SPL IPC tags.
SPLStatusInfo = 39
SPLTrackPlaybackStatus = 104
SPLCurTrackPlaybackTime = 105

# Return a tuple of column headers.
# This is just a thinly disguised indexOf function from Studio's track item class.
def indexOf(rsVersion: str) -> tuple[str, ...]:
	# Remote Studio 6.20 defines Studio 6.11 column headers.
	# Therefore, the version parameter is not needed.
	return tuple(["Status"] + splconfig.SPLDefaults["ColumnAnnouncement"]["ColumnOrder"])


class RemoteStudioPlaylistViewerItem(splstudio.StudioPlaylistViewerItem):
	"""Track items found in Remote Studio.
	Columns are based on Studio 6.11 and earlier.
	"""

	@property
	def screenColumnOrder(self):
		# Return the actual default column order based on Studio release.
		return indexOf(self.appModule.productVersion)[1:]

	def indexOf(self, columnHeader: str) -> int | None:
		try:
			return indexOf(self.appModule.productVersion).index(columnHeader)
		except ValueError:
			return None

	# Update column headers shown on screen (which does nothing in Remote Studio).
	def updateColumnHeader(self, header: str) -> str:
		return header


class AppModule(splstudio.AppModule):
	# Remote Studio API is available for some features.
	_SPLAPILevel = splbase.StudioAPIAvailability.REMOTEAPI

	def terminate(self):
		super().terminate()
		# Clear app module flags and attributes.
		self._pastStatusBarContent = None
		# Clear Remote Studio settings file timestamp (mostly for cart explorer).
		splcarts.cartEditRemoteTimestamps = None

	# Locate the handle for Remote Studio for caching purposes.
	def _locateSPLHwnd(self) -> None:
		while not (hwnd := user32.FindWindowW("RemoteStudio", None)):
			time.sleep(1)
			# If the demo copy expires and the app module begins, this loop will spin forever.
			# Make sure this loop catches this case.
			if self.noMoreHandle.is_set():
				self.noMoreHandle.clear()
				return
		# Only this thread will have privilege of notifying Studio handle's existence.
		with threading.Lock():
			splbase.setStudioWindowHandle(hwnd, splComponent="remotestudio")
			log.debug(f"SPL: Remote Studio handle is {hwnd}")

	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: list[NVDAObject]) -> None:
		if (
			obj.windowClassName == "TTntListView.UnicodeClass"
			and obj.role == controlTypes.Role.LISTITEM
			and obj.parent.simpleParent.windowClassName == "TStudioForm"
		):
			clsList.insert(0, RemoteStudioPlaylistViewerItem)
			return
		super().chooseNVDAObjectOverlayClasses(obj, clsList)

	# Status bar is one long text separated by vertical bars (|).
	# Record status bar contents when Remote Studio is connected to a local Studio instance.
	_pastStatusBarContent: str | None = None

	def event_foreground(self, obj: NVDAObject, nextHandler: collections.abc.Callable[[], None]):
		if obj.windowClassName == "TStudioForm":
			# Tell NVDA to announce just the changed bits of the status bar.
			# Record the current status bar text if the app module doesn't know about it.
			if not self._pastStatusBarContent:
				self._pastStatusBarContent = self.status(self.SPLRemoteStatus).displayText
			# Refresh carts if cart explorer is active and Remote Studio settings have changed.
			if self.cartExplorer:
				self.carts = splcarts.cartExplorerRefresh(obj.name, self.carts, remoteStudio=True)
				if "refresh" in self.carts and self.carts["refresh"]:
					del self.carts["refresh"]
					queueHandler.queueFunction(
						queueHandler.eventQueue, ui.message, _("Cart explorer is active")
					)
		nextHandler()

	def event_nameChange(self, obj: NVDAObject, nextHandler: collections.abc.Callable[[], None]):
		if obj.windowClassName == "TStatusBar":
			# Only announce the changed parts of the status bar except when connecting the first time.
			if "|" in obj.name:
				if self._pastStatusBarContent:
					statusBarText = obj.name.split("  |  ")
					oldStatusBarText = self._pastStatusBarContent.split("  |  ")
					changedStatusBarContent = []
					for newStatus, oldStatus in zip(statusBarText, oldStatusBarText):
						if newStatus != oldStatus:
							changedStatusBarContent.append(newStatus)
					for content in changedStatusBarContent:
						queueHandler.queueFunction(queueHandler.eventQueue, self.doRemoteStudioExtraAction, content)
				self._pastStatusBarContent = obj.name
			elif "match" in obj.name:
				# Announce search/match results from insert tracks dialog.
				# Only announce match count as the whole thing is very verbose.
				if splconfig.SPLConfig["General"]["BeepAnnounce"]:
					tones.beep(370, 40)
				ui.message(" ".join(obj.name.split()[:2]))
			else:
				# Announce connection status in Remote Studio.
				ui.message(obj.name)
			return nextHandler()
		# Track remaining/elapsed time changes are handled from the local Studio app module.
		super().event_nameChange(obj, nextHandler)

	def doRemoteStudioExtraAction(self, content: str) -> None:
		# Do play a beep when asked.
		if content.endswith((" On", " Off")):
			self._toggleMessage(content)
		else:
			ui.message(content)
		if splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarm"]:
			# Activate mic alarm or announce when cart explorer is active.
			self.doExtraAction(content)

	# Announce elapsed and remaining times differently across local and Remote Studio
	# (API can be used in local and remote Studio).
	# Remote Studio: only track elapsed/remaining time will be announced.
	def announceTrackTime(self, trackTime: str) -> None:
		# Track time parameter can be either "remaining" or "elapsed".
		match trackTime:
			case "remaining":
				remainingTime = splbase.studioAPI(3, SPLCurTrackPlaybackTime, splComponent="remotestudio")
				self.announceTime(remainingTime)
			case "elapsed":
				elapsedTime = splbase.studioAPI(0, SPLCurTrackPlaybackTime, splComponent="remotestudio")
				self.announceTime(elapsedTime)
			case _:
				raise ValueError(f"Unrecognized track time announcement command: {trackTime}")

	# Cart explorer (Remote Studio)
	cartExplorer = False
	# The carts dictionary (key = cart gesture, item = cart name).
	carts: dict[str, Any] = {}

	# Toggle cart explorer (private method)
	# Remote Studio: no need to check Studio title.
	def _toggleCartExplorer(self) -> None:
		if not self.cartExplorer:
			# Prevent cart explorer from being engaged outside of playlist viewer.
			fg = api.getForegroundObject()
			if fg.windowClassName != "TStudioForm":
				ui.message(_("You are not in playlist viewer, cannot enter cart explorer"))
				return
			self.carts = splcarts.cartExplorerInit(fg.name, remoteStudio=True)
			if self.carts["faultyCarts"]:
				ui.message(_("Some or all carts could not be assigned, cannot enter cart explorer"))
				return
			else:
				self.cartExplorer = True
				self.cartsBuilder()
				ui.message(_("Entering cart explorer"))
		else:
			self.cartExplorer = False
			self.cartsBuilder(build=False)
			self.carts.clear()
			splcarts.cartEditRemoteTimestamps = None
			ui.message(_("Exiting cart explorer"))

	# Assigning and building carts.

	def cartsBuilder(self, build: bool = True) -> None:
		# A function to build and return cart commands.
		# Remote Studio offers twelve carts (function keys only).
		if build:
			for cart in splcarts.cartKeys[:12]:
				self.bindGesture(f"kb:{cart}", "cartExplorer")
		else:
			self.clearGestureBindings()
			self.bindGestures(self.__gestures)

	# Check to make sure a playlist is indeed loaded by checking track count.
	def playlistLoaded(self) -> bool:
		focus = api.getFocusObject()
		if isinstance(focus, RemoteStudioPlaylistViewerItem):
			return True
		return bool(getattr(focus, "rowCount", 0))

	# Status table keys
	# Unlike local Studio, Remote Studio API is limited, so screen traversal must be done for some elements.
	# This is applicable to SPL Assistant commands and other scripts.
	SPLRemoteStatus = 0
	SPLNextTrackTitle = 1
	SPLNextPlayer = 2
	SPLCurrentTrackTitle = 3
	SPLCurrentPlayer = 4
	SPLTrackStarts = 5
	SPLTemperature = 6

	# Table of child constants based on versions
	# Same as local Studio: scattered around the screen, so use foreground.getChild(index) to fetch them
	# As of 2025, the below table is based on local Studio 6.10 interface.
	statusObjs = {
		"6": {
			SPLRemoteStatus: [2, 0],  # Remote Studio status bar
			SPLNextTrackTitle: [2, 2, 2, 0],
			SPLNextPlayer: [2, 2, 2, 1],
			SPLCurrentTrackTitle: [2, 2, 9],
			SPLCurrentPlayer: [2, 2, 9, 0],
			SPLTrackStarts: [2, 2, -3],
			SPLTemperature: [2, 2, 3, 1],  # Temperature for the current city.
		},
	}

	_cachedStatusObjs: dict[int, Any] = {}

	# Remote Studio status bar messages (distinct from local Studio).
	# For playback, Remote Studio can also say "Paused".
	_studioStatusMessages = (
		["Stopped", "Playing", "Paused"],
		["Automation Off", "Automation On"],
		["Mic Off", "Mic On"],
		["Line Off", "Line On"],
	)

	# Report status bar contents such as microphone status.
	# Remote Studio: not all status flags are supported.
	def sayStatus(self, index: int) -> None:
		# No, status index must be an integer (compatibility with local Studio).
		studioStatus = splbase.studioAPI(index, SPLStatusInfo, splComponent="remotestudio")
		if studioStatus is None:
			return
		# Special handling for playback (playing/stopped/paused)
		if index == 0 and studioStatus == 1:  # Playing/paused
			# Set status to 2 (paused) if the remote track is paused.
			if splbase.studioAPI(0, SPLTrackPlaybackStatus, splComponent="remotestudio") == 3:
				studioStatus = 2
		status = self._studioStatusMessages[index][studioStatus]
		if splconfig.SPLConfig["General"]["MessageVerbosity"] == "advanced":
			status = status.split()[-1]
		ui.message(status)
