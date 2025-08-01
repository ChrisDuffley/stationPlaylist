# StationPlaylist (formerly StationPlaylist Studio)
# An app module and global plugin package for NVDA
# Copyright 2011, 2013-2025 Geoff Shang, Joseph Lee and others, released under GPL.
# The primary function of this appModule is to provide meaningful feedback to users of SplStudio
# by allowing speaking of items which cannot be easily found.
# Version 0.01 - 7 April 2011:
# Initial release: Jamie's focus hack plus auto-announcement of status items.
# Additional work done by Joseph Lee and other contributors.
# Renamed to StationPlaylist in 2019 in order to describe the scope of this add-on.
# For SPL Studio Controller, focus movement and other utilities,
# see the global plugin version of this app module.

# Minimum version: SPL 6.0, NVDA 2024.1.

from typing import Any
import os
import time
import threading
import collections
import controlTypes
import appModuleHandler
import api
import config
import globalVars
import scriptHandler
import eventHandler
import review
import ui
import nvwave
import speech
import braille
import touchHandler
import gui
import wx
import winKernel
from winUser import user32, OBJID_CLIENT
from logHandler import log
from NVDAObjects import NVDAObject, NVDAObjectTextInfo
from NVDAObjects.IAccessible import IAccessible, getNVDAObjectFromEvent, sysListView32
from NVDAObjects.behaviors import Dialog
import textInfos
import tones
import versionInfo
from ..splcommon import splbase, splconsts, splactions, splconfig
from . import splconfui
from . import splmisc
import addonHandler
from ..skipTranslation import translate

addonHandler.initTranslation()


# Make sure the broadcaster is running a compatible version.
SPLMinVersion = "6.0"

# Threads pool.
micAlarmT: threading.Timer | None = None
micAlarmT2 = None
libScanT: threading.Thread | None = None

# Various SPL IPC tags.
SPLPlaylistHourDuration = 27
SPLLibraryScanCount = 32
SPLMetadataStreaming = 36
SPLStatusInfo = 39
SPLCurTrackPlaybackTime = 105
SPLTrackCount = 124

# Braille and play a sound in response to an alarm or an event.
def messageSound(wavFile: str, message: str) -> None:
	nvwave.playWaveFile(wavFile)
	braille.handler.message(message)


# A special version for microphone alarm (continuous or not).
def _micAlarmAnnouncer() -> None:
	if splconfig.SPLConfig["General"]["AlarmAnnounce"] in ("beep", "both"):
		nvwave.playWaveFile(os.path.join(os.path.dirname(__file__), "SPL_MicAlarm.wav"))
	if splconfig.SPLConfig["General"]["AlarmAnnounce"] in ("message", "both"):
		# Translators: Presented when microphone has been active for a while.
		ui.message(_("Microphone active"))


# Manage microphone alarm announcement.
def micAlarmManager(micAlarmWav: str, micAlarmMessage: str) -> None:
	messageSound(micAlarmWav, micAlarmMessage)
	# Play an alarm sound (courtesy of Jerry Mader from Mader Radio).
	global micAlarmT2
	# Use a timer to play a tone when microphone was active for more than the specified amount.
	# Mechanics come from Clock add-on.
	if splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarmInterval"]:
		micAlarmT2 = wx.PyTimer(_micAlarmAnnouncer)
		wx.CallAfter(micAlarmT2.Start, splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarmInterval"] * 1000)


# Category sounds dictionary (key = category, value = tone pitch).
_SPLCategoryTones = {
	"Break Note": 415,
	"Timed Break Note": 208,
	"<Manual Intro>": 600,
}


# Show additional controls in browseable message window.
browseableMessageButtons = {"closeButton": True} if versionInfo.version_year >= 2025 else {}


# SPL Playlist item (SPL add-on base object) is defined in splcommon.splbase module.
# Classes pertaining to Studio app module will be defined here.
class SPLStudioTrackItem(splbase.SPLTrackItem):
	"""A representative class of Studio track items outside of Playlist Viewer."""

	pass


class StudioPlaylistViewerItem(splbase.SPLTrackItem):
	"""A class representing items found in Playlist Viewer (main window).
	It provides utility scripts when Playlist Viewer entries are focused,
	such as location text and enhanced column navigation."""

	def _get_name(self):
		# Build name pieces, as SysListView32.ListItem class nullifies description.
		# 19.06: have the column inclusion and order keys handy in order to avoid attribute lookup.
		columnsToInclude = splconfig.SPLConfig["ColumnAnnouncement"]["IncludedColumns"]
		columnOrder = splconfig.SPLConfig["ColumnAnnouncement"]["ColumnOrder"]
		# Catch an unusual case where screen order is off yet column order is same as screen order
		# and NVDA is told to announce all columns.
		if not splconfig.SPLConfig["ColumnAnnouncement"]["UseScreenColumnOrder"] and (
			columnOrder != splconfig.SPLDefaults["ColumnAnnouncement"]["ColumnOrder"]
			or len(columnsToInclude) != 17
		):
			trackNamePieces = []
			# Table column header report options (1 = report rows and columns, 3 = report columns).
			includeColumnHeaders = config.conf["documentFormatting"]["reportTableHeaders"] in (1, 3)
			# Include status (actual item name as reported by MSAA) if present
			# (accessibility mode is enabled in Studio options).
			if self.firstChild.name:
				trackNamePieces.append(self.firstChild.name)
			for header in columnOrder:
				if header in columnsToInclude:
					index = self.indexOf(header)
					if index is None:
						continue
					content = self._getColumnContentRaw(index)
					if content:
						trackNamePieces.append(
							"{}: {}".format(header, content) if includeColumnHeaders else content
						)
			trackName = "; ".join(trackNamePieces)
		else:
			trackName = super(StudioPlaylistViewerItem, self).name
		return trackName

	def event_stateChange(self):
		# Why is it that NVDA keeps announcing "not selected" when track items are scrolled?
		if controlTypes.State.SELECTED not in self.states:
			pass

	@scriptHandler.script(gesture="kb:space")
	def script_select(self, gesture):
		gesture.send()
		speech.speakMessage(self.firstChild.name)
		braille.handler.handleUpdate(self)

	# Read selected columns.
	# But first, find where the requested column lives.
	# #142: do not ignore Status column (0) just because it is the name of the track as reported by MSAA.
	def indexOf(self, columnHeader: str) -> int | None:
		try:
			columnHeaders = ["Status"] + splconfig.SPLDefaults["ColumnAnnouncement"]["ColumnOrder"]
			return columnHeaders.index(columnHeader)
		except ValueError:
			return None

	def reportFocus(self):
		if splconfig.SPLConfig["General"]["CategorySounds"]:
			category = self._getColumnContentRaw(self.indexOf("Category"))
			if category in _SPLCategoryTones:
				tones.beep(_SPLCategoryTones[category], 50)
		# Comments please.
		if splconfig.SPLConfig["General"]["TrackCommentAnnounce"] != "off":
			self.announceTrackComment(0)
		if self._savedColumnNumber is None:
			super(IAccessible, self).reportFocus()
		else:
			# Don't forget that column position starts at 1, not 0 (therefore subtract 1).
			colNumber = self._savedColumnNumber - 1
			if (
				(verticalColumnAnnounce := splconfig.SPLConfig["General"]["VerticalColumnAnnounce"]) is not None
			):
				# Get the raw view of column array (pass in "18" columns directly).
				colNumber = list(self.parent._getColumnOrderArrayRaw(18)).index(
					self.indexOf(verticalColumnAnnounce)
				)
			# Add track check status to column data if needed by using a customized move to column number method.
			cell = self.getChild(colNumber)
			if colNumber > 0 and self.firstChild.name:
				cell.name = "{0} {1}".format(self.firstChild.name, cell.name)
			self._moveToColumn(cell)
		# Let the app module keep a reference to this track.
		self.appModule._focusedTrack = self
		# #142: just like fake table row behavior class, nullify saved column number.
		self.__class__._savedColumnNumber = None

	# Use Studio API to obtain track position and item count.
	def _get_locationText(self):
		# Translators: location text for a playlist item (example: item 1 of 10).
		return _("Item {current} of {total}").format(
			current=self.IAccessibleChildID, total=splbase.studioAPI(0, SPLTrackCount)
		)

	# #12: select and set focus to this track.
	def doAction(self, index=None):
		self.setFocus()
		self.setFocus()
		splbase.selectTrack(self.IAccessibleChildID - 1)

	# Obtain column contents for all columns for this track.
	# A convenience method that calls column content getter for a list of columns.
	# Readable flag will transform None into an empty string, suitable for output.
	# #61: readable flag will become a string parameter to be used in columns viewer.
	def _getColumnContents(
		self, columns: list[int] | None = None, readable: bool = False
	) -> list[str | None]:
		if columns is None:
			columns = list(range(18))
		columnContents = [self._getColumnContentRaw(col) for col in columns]
		if readable:
			# #148: Use enumerate function to obtain both column content and position in one go
			# rather than using a range based on list length.
			for pos, content in enumerate(columnContents):
				if content is None:
					columnContents[pos] = ""
		return columnContents

	# Track movement scripts.
	# Detects top/bottom of a playlist if told to do so.

	@scriptHandler.script(gesture="kb:downArrow")
	def script_nextTrack(self, gesture):
		gesture.send()
		if (
			self.IAccessibleChildID == self.parent.childCount - 1
			and splconfig.SPLConfig["General"]["TopBottomAnnounce"]
		):
			tones.beep(2000, 100)

	@scriptHandler.script(gesture="kb:upArrow")
	def script_prevTrack(self, gesture):
		gesture.send()
		if self.IAccessibleChildID == 1 and splconfig.SPLConfig["General"]["TopBottomAnnounce"]:
			tones.beep(2000, 100)

	# Vertical column navigation.
	# The following move to row method was customized for Studio track item.

	def _moveToRow(self, row):
		if not row:
			return self._moveToColumn(None) if splconfig.SPLConfig["General"]["TopBottomAnnounce"] else None
		nav = api.getNavigatorObject()
		if nav != self and nav.parent == self:
			self.__class__._savedColumnNumber = nav.columnNumber
		# Do action method will set focus to and select the row in question.
		row.doAction()

	# Overlay class version of Columns Explorer.

	@property
	def exploreColumns(self) -> list[str]:
		return splconfig.SPLConfig["ExploreColumns"]["Studio"]

	# Toggle screen column order.
	# Limited to playlist viewer as this is where the toggle should be performed.

	@scriptHandler.script(
		# Translators: Input help message for screen column order toggle command in SPL Studio.
		description=_("Toggles track column announcement order between screen layout and custom order"),
		gesture="kb:NVDA+V",
	)
	def script_toggleScreenColumnOrder(self, gesture):
		if not splconfig.SPLConfig["ColumnAnnouncement"]["UseScreenColumnOrder"]:
			splconfig.SPLConfig["ColumnAnnouncement"]["UseScreenColumnOrder"] = True
			# Translators: presented when NVDA will present track columns in screen order.
			ui.message(_("Use screen order when announcing track columns"))
		else:
			splconfig.SPLConfig["ColumnAnnouncement"]["UseScreenColumnOrder"] = False
			# Translators: presented when NVDA will present track columns in custom order set by a user.
			ui.message(_("Use custom order when announcing track columns"))
		braille.handler.handleUpdate(self)

	# Track comments.

	# Track comment announcer.
	# Levels indicate what should be done.
	# 0 indicates reportFocus, subsequent levels indicate script repeat count+1.
	def announceTrackComment(self, level: int) -> None:
		filename = self._getColumnContentRaw(self.indexOf("Filename"))
		if filename is not None and filename in splconfig.trackComments:
			if level == 0:
				if splconfig.SPLConfig["General"]["TrackCommentAnnounce"] in ("message", "both"):
					# Message comes from NVDA Core.
					ui.message(translate("has comment"))
				if splconfig.SPLConfig["General"]["TrackCommentAnnounce"] in ("beep", "both"):
					tones.beep(1024, 100)
			elif level == 1:
				ui.message(splconfig.trackComments[filename])
			elif level == 2:
				api.copyToClip(splconfig.trackComments[filename])
				# Translators: Presented when track comment has been copied to clipboard.
				ui.message(_("Track comment copied to clipboard"))
			else:
				self._trackCommentsEntry(filename, splconfig.trackComments[filename])
		else:
			if level in (1, 2):
				ui.message(translate("No comments"))
			elif level >= 3:
				# Timed break notes shows an odd value for filename (seconds in integers followed by a colon),
				# potentially confusing users.)
				if filename and not filename.endswith(":"):
					self._trackCommentsEntry(filename, "")
				else:
					# Translators: Presented when focused on a track other than an actual track (such as hour marker).
					ui.message(_("Comments cannot be added to this kind of track"))

	# A proxy function to call the track comments entry dialog.
	def _trackCommentsEntry(self, filename: str, comment: str) -> None:
		dlg = wx.TextEntryDialog(
			gui.mainFrame,
			_("Track comment"),
			# Translators: The title of the track comments dialog.
			_("Track comment"),
			value=comment,
		)

		def callback(result):
			if result == wx.ID_OK:
				newComment = dlg.GetValue()
				# No need to deal with track comments if Studio is gone and/or value is empty.
				# Optimization: same values are not allowed.
				if (
					newComment is None
					or newComment == comment
					or not splbase.studioIsRunning(justChecking=True)
				):
					return
				elif newComment == "":
					# #156: guard against nonexistent filenames.
					try:
						del splconfig.trackComments[filename]
					except KeyError:
						pass
				else:
					splconfig.trackComments[filename] = dlg.GetValue()

		gui.runScriptModalDialog(dlg, callback)

	@scriptHandler.script(
		description=_(
			# Translators: Input help message for track comment announcemnet command in SPL Studio.
			"Announces track comment if any. Press twice to copy this information to the clipboard, "
			"and press three times to open a dialog to add, change or remove track comments"
		),
		gesture="kb:Alt+NVDA+C",
		category=_("StationPlaylist"),
		speakOnDemand=True,
	)
	def script_announceTrackComment(self, gesture):
		scriptRepeatCount = scriptHandler.getLastScriptRepeatCount()
		# Do not allow many track comment dialog instances from appearing.
		# Security: do not allow comments to be copied or changed in secure mode.
		if globalVars.appArgs.secure:
			scriptRepeatCount = 0
		if scriptRepeatCount <= 2:
			self.announceTrackComment(scriptRepeatCount + 1)


SPLAssistantHelp = {
	# Translators: The text of the help command in SPL Assistant layer.
	"off": _("""After entering SPL Assistant, press:
A: Automation.
C: Announce name of the currently playing track.
D: Remaining time for the playlist.
Control+D: Control keys toggle (Studio 6.10 and later).
E: Overall metadata streaming status.
Shift+1 through shift+4, shift+0: Metadata streaming status for DSP encoder and four additional URL's.
H: Duration of trakcs in this hour slot.
Shift+H: Duration of remaining trakcs in this hour slot.
I: Listener count.
K: Move to place marker track.
Control+K: Set place marker track.
L: Line-in status.
M: Microphone status.
N: Next track.
O: Playlist hour over/under by.
P: Playback status.
Shift+P: Pitch for the current track.
R: Record to file.
Shift+R: Monitor library scan.
S: Scheduled time for the track.
Shift+S: Time until the selected track will play.
T: Cart edit/insert mode.
U: Studio up time.
W: Weather and temperature.
Y: Playlist modification.
F8: Take playlist snapshots such as track count, longest track and so on.
Shift+F8: Obtain playlist transcripts in a variety of formats.
F9: Mark current track as start of track time analysis.
F10: Perform track time analysis.
F12: Switch to an instant switch profile."""),
	# Translators: The text of the help command in SPL Assistant layer when JFW layer is active.
	"jfw": _("""After entering SPL Assistant, press:
A: Automation.
C: Toggle cart explorer.
Shift+C: Announce name of the currently playing track.
Control+D: Control keys toggle (Studio 6.10 and later).
E: Overall metadata streaming status.
Shift+1 through shift+4, shift+0: Metadata streaming status for DSP encoder and four additional URL's.
Shift+E: Record to file.
F: Track finder.
H: Duration of trakcs in this hour slot.
Shift+H: Duration of remaining trakcs in this hour slot.
K: Move to place marker track.
Control+K: Set place marker track.
L: Listener count.
Shift+L: Line-in status.
M: Microphone status.
N: Next track.
O: Playlist hour over/under by.
P: Playback status.
Shift+P: Pitch for the current track.
R: Remaining time for the playlist.
Shift+R: Monitor library scan.
S: Scheduled time for the track.
Shift+S: Time until the selected track will play.
T: Cart edit/insert mode.
U: Studio up time.
W: Weather and temperature.
Y: Playlist modification.
F8: Take playlist snapshots such as track count, longest track and so on.
Shift+F8: Obtain playlist transcripts in a variety of formats.
F9: Mark current track as start of track time analysis.
F10: Perform track time analysis.
F12: Switch to an instant switch profile."""),
}


# Provide a way to fetch dialog description in reverse order.
# This is used in Studio's About dialog as children are in reverse tab order somehow.
class ReversedDialog(Dialog):
	"""Overrides the description property to obtain dialog text except in reverse order.
	This is employed in Studio's help/About dialog.
	"""

	@classmethod
	def getDialogText(cls, obj, allowFocusedDescendants=True):
		"""This classmethod walks through the children of the given object, and collects up and
		returns any text that seems to be  part of a dialog's message text.
		@param obj: the object who's children you want to collect the text from
		@type obj: L{IAccessible}
		@param allowFocusedDescendants: if false no text will be returned at all
		if one of the descendants is focused.
		@type allowFocusedDescendants: boolean
		"""
		children = obj.children
		textList = []
		childCount = len(children)
		# For these dialogs, children are arranged in reverse tab order (very strange indeed).
		for index in range(childCount - 1, -1, -1):
			child = children[index]
			childStates = child.states
			childRole = child.role
			# We don't want to handle invisible or unavailable objects
			if controlTypes.State.INVISIBLE in childStates or controlTypes.State.UNAVAILABLE in childStates:
				continue
			# For particular objects, we want to descend in to them and get their children's message text
			if childRole in (
				controlTypes.Role.PROPERTYPAGE,
				controlTypes.Role.PANE,
				controlTypes.Role.PANEL,
				controlTypes.Role.WINDOW,
				controlTypes.Role.GROUPING,
				controlTypes.Role.PARAGRAPH,
				controlTypes.Role.SECTION,
				controlTypes.Role.TEXTFRAME,
				controlTypes.Role.UNKNOWN,
			):
				# Grab text from descendants, but not for a child which inherits from Dialog and has focusable descendants
				# Stops double reporting when focus is in a property page in a dialog
				childText = cls.getDialogText(child, not isinstance(child, Dialog))
				if childText:
					textList.append(childText)
				elif childText is None:
					return None
				continue
			# If the child is focused  we should just stop and return None
			if not allowFocusedDescendants and controlTypes.State.FOCUSED in child.states:
				return None
			# We only want text from certain controls.
			if not (
				# Static text, labels and links
				childRole in (controlTypes.Role.STATICTEXT, controlTypes.Role.LABEL, controlTypes.Role.LINK)
				# Read-only, non-multiline edit fields
				or (
					childRole == controlTypes.Role.EDITABLETEXT
					and controlTypes.State.READONLY in childStates
					and controlTypes.State.MULTILINE not in childStates
				)
			):
				continue
			# We should ignore a text object directly after a grouping object,
			# as it's probably the grouping's description
			if index > 0 and children[index - 1].role == controlTypes.Role.GROUPING:
				continue
			# Like the last one, but a graphic might be before the grouping's description
			if (
				index > 1
				and children[index - 1].role == controlTypes.Role.GRAPHIC
				and children[index - 2].role == controlTypes.Role.GROUPING
			):
				continue
			childName = child.name
			if (
				childName
				and index < (childCount - 1)
				and children[index + 1].role
				not in (
					controlTypes.Role.GRAPHIC,
					controlTypes.Role.STATICTEXT,
					controlTypes.Role.SEPARATOR,
					controlTypes.Role.WINDOW,
					controlTypes.Role.PANE,
					controlTypes.Role.BUTTON,
				)
				and children[index + 1].name == childName
			):
				# This is almost certainly the label for the next object, so skip it.
				continue
			isNameIncluded = child.TextInfo is NVDAObjectTextInfo or childRole in (
				controlTypes.Role.LABEL,
				controlTypes.Role.STATICTEXT,
			)
			childText = child.makeTextInfo(textInfos.POSITION_ALL).text
			if not childText or childText.isspace() and child.TextInfo is not NVDAObjectTextInfo:
				childText = child.basicText
				isNameIncluded = True
			if not isNameIncluded:
				# The label isn't in the text, so explicitly include it first.
				if childName:
					textList.append(childName)
			if childText:
				textList.append(childText)
		return "\n".join(textList)


# Temporary Cue time pickers does not expose the correct tree.
# Thankfully, when up or down arrows are pressed, display text changes.
class SPLTimePicker(IAccessible):
	@scriptHandler.script(gestures=["kb:upArrow", "kb:downArrow"])
	def script_changeTimePickerValue(self, gesture):
		# Slightly modified "read current line" script without complexities of tree interceptor and caret.
		gesture.send()
		info = api.getFocusObject().makeTextInfo(textInfos.POSITION_FIRST)
		info.expand(textInfos.UNIT_LINE)
		speech.speakTextInfo(info, unit=textInfos.UNIT_LINE, reason=controlTypes.OutputReason.CARET)


class AppModule(appModuleHandler.AppModule):
	# Translators: Script category for StationPlaylist add-on commands in input gestures dialog.
	scriptCategory = _("StationPlaylist")
	_focusedTrack = None
	# Monitor Studio API routines.
	_SPLStudioMonitor = None

	# Prepare the settings dialog among other things.
	def __init__(self, *args, **kwargs):
		# #110: assertion thrown when attempting to locate Studio window handle
		# because the locator thread is queued from main thread when NVDA is gone.
		# This is seen when restarting NVDA while studio add-on settings screen was active.
		if wx.GetApp() is None:
			return
		super().__init__(*args, **kwargs)
		if self.productVersion < SPLMinVersion:
			wx.CallAfter(gui.messageBox,
			# Translators: error dialog shown when a broadcaster is running an unsupported STduio release.
			_("You are using an unsupported version of {appName}. "
			"This add-on requires {appName} {version} or later").format(
				appName=self.productName, version=SPLMinVersion
			),
			# Translators: the title of the app version error dialog.
			_("Unsupported {appName} release").format(appName=self.productName),
			)
			raise RuntimeError("Unsupported version of Studio is running, exiting app module")
		# Announce app version if minimal startup flag is not set.
		try:
			if not globalVars.appArgs.minimal:
				# No translation.
				ui.message("{} {}".format(self.productName, self.productVersion))
		except Exception:
			pass
		# #40: react to profile switches.
		# #94: also listen to profile reset action.
		splactions.SPLActionProfileSwitched.register(self.actionProfileSwitched)
		splactions.SPLActionSettingsReset.register(self.actionSettingsReset)
		# To avoid a resource leak, metadata actions must be registered here,
		# not when splmisc module is being imported.
		splactions.SPLActionProfileSwitched.register(splmisc.metadata_actionProfileSwitched)
		splactions.SPLActionSettingsReset.register(splmisc.metadata_actionSettingsReset)
		# Load config database if not done already.
		splconfig.openConfig(self.appName)
		splconfig.initStudioExtraSteps()
		# Announce status changes while using other programs.
		eventHandler.requestEvents(
			eventName="nameChange", processId=self.processID, windowClassName="TStatusBar"
		)
		eventHandler.requestEvents(
			eventName="nameChange", processId=self.processID, windowClassName="TStaticText"
		)
		# Also for requests window.
		eventHandler.requestEvents(eventName="show", processId=self.processID, windowClassName="TRequests")
		try:
			self.prefsMenu = gui.mainFrame.sysTrayIcon.preferencesMenu
			self.SPLSettings = self.prefsMenu.Append(
				wx.ID_ANY,
				# Translators: the label for a menu item in NVDA Preferences menu
				# to open SPL Studio add-on settings.
				_("SPL Studio Settings..."),
				# Translators: tooltip for SPL Studio settings dialog.
				_("SPL settings"),
			)
			gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, splconfui.onConfigDialog, self.SPLSettings)
		except AttributeError:
			self.prefsMenu = None
		# #82: notify others when Studio window gets focused the first time
		# in order to synchronize announcement order.
		self._initStudioWindowFocused = threading.Event()
		# Let me know the Studio window handle.
		# Do not allow this thread to run forever (seen when evaluation times out and the app module starts).
		self.noMoreHandle = threading.Event()
		# If this is started right away, foreground and focus objects will be NULL according to NVDA
		# if NVDA restarts while Studio is running.
		t = threading.Thread(target=self._locateSPLHwnd)
		wx.CallAfter(t.start)
		# Display startup dialogs if any (but not when minimal startup flag is set).
		# Sometimes, wxPython 4 says wx.App isn't ready.
		try:
			wx.CallAfter(splconfig.showStartupDialogs)
		except Exception:
			pass

	# Locate the handle for main window for caching purposes.
	def _locateSPLHwnd(self) -> None:
		while not (hwnd := user32.FindWindowW("SPLStudio", None)):
			time.sleep(1)
			# If the demo copy expires and the app module begins, this loop will spin forever.
			# Make sure this loop catches this case.
			if self.noMoreHandle.is_set():
				self.noMoreHandle.clear()
				return
		# Only this thread will have privilege of notifying Studio handle's existence.
		with threading.Lock():
			splbase.setStudioWindowHandle(hwnd)
			log.debug(f"SPL: Studio handle is {hwnd}")
		# #41: start background monitor unless Studio is exiting.
		try:
			self._SPLStudioMonitor = wx.PyTimer(self.studioAPIMonitor)
			wx.CallAfter(self._SPLStudioMonitor.Start, 1000)
		except Exception:
			pass
		# Remind me to broadcast metadata information.
		# Also when delayed action is needed
		# because metadata action handler couldn't locate Studio handle itself.
		# Pass in Studio init event so the below function can ask the event to wait.
		splmisc.startupMetadataReminder(self._initStudioWindowFocused)

	# Studio API heartbeat.
	# Although useful for library scan detection, it can be extended to cover other features.

	def studioAPIMonitor(self) -> None:
		# Only proceed if Studio handle is valid (Studio is fully operational).
		if not splbase.studioIsRunning(justChecking=True):
			if self._SPLStudioMonitor is not None:
				self._SPLStudioMonitor.Stop()
				self._SPLStudioMonitor = None
				return
		# #41: background library scan detection.
		# Thankfully, current lib scan reporter function will not proceed
		# when library scan is happening via Insert Tracks dialog.
		# #92: if Studio dies, zero will be returned, so check for window handle once more.
		# #155: library scan count must be an integer.
		libScanCount: int | None = splbase.studioAPI(1, SPLLibraryScanCount)
		if libScanCount and libScanCount >= 0:
			if not splbase.studioIsRunning(justChecking=True):
				return
			if not self.libraryScanning:
				self.script_libraryScanMonitor(None)
		# #86: certain internal markers require presence of a playlist,
		# otherwise unexpected things may happen.
		trackCount = splbase.studioAPI(0, SPLTrackCount)
		if not trackCount:
			if self._focusedTrack is not None:
				self._focusedTrack = None
			if self._analysisMarker is not None:
				self._analysisMarker = None
		# #145: playlist analysis marker value must be below track count.
		# #155: and track count must be an integer.
		if (
			self._analysisMarker is not None
			and trackCount is not None
			and not 0 <= self._analysisMarker < trackCount
		):
			self._analysisMarker = None

	# Let the global plugin know if SPLController passthrough is allowed.
	def SPLConPassthrough(self) -> bool:
		return splconfig.SPLConfig["Advanced"]["SPLConPassthrough"]

	# The only job of the below event is to notify others that Studio window has appeared for the first time.
	# This is used to coordinate various status announcements.

	def event_foreground(self, obj: NVDAObject, nextHandler: collections.abc.Callable[[], None]):
		if not self._initStudioWindowFocused.is_set() and obj.windowClassName == "TStudioForm":
			self._initStudioWindowFocused.set()
		nextHandler()

	def event_NVDAObject_init(self, obj: NVDAObject):
		# Employ structural pattern matching to handle different window class names.
		match obj.windowClassName:
			case "TListView":
				# From 0.01: previously focused item fires focus event when it shouldn't.
				if (
					obj.role in (controlTypes.Role.CHECKBOX, controlTypes.Role.LISTITEM)
					and controlTypes.State.FOCUSED not in obj.states
				):
					obj.shouldAllowIAccessibleFocusEvent = False
			case "TRadioGroup":
				# Radio button group names are not recognized as grouping, so work around this.
				obj.role = controlTypes.Role.GROUPING
			case "TEdit" | "TComboBox":
				# In certain edit fields and combo boxes, the field name is written to the screen,
				# and there's no way to fetch the object for this text.
				# Thus use review position text (first item in screen position function return tuple).
				if not obj.name:
					fieldName = review.getScreenPosition(obj)[0]
					fieldName.expand(textInfos.UNIT_LINE)
					if obj.windowClassName == "TComboBox":
						obj.name = fieldName.text.replace(obj.windowText, "")
					else:
						obj.name = fieldName.text
			case "TStatusBar":
				# Status bar labels are not found in Studio 6 but is written to the screen.
				if obj.name is None:
					obj.name = obj.displayText
			case _:
				pass

	# Some controls which needs special routines.
	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: list[NVDAObject]) -> None:
		role = obj.role
		try:
			windowStyle = obj.windowStyle
		except AttributeError:
			windowStyle = 0
		# Use structural pattern matching to detect overlay classes.
		match obj.windowClassName:
			case "TTntListView.UnicodeClass":
				if role == controlTypes.Role.LISTITEM:
					trackItemWindowStyle = 1443991617
					if abs(windowStyle - trackItemWindowStyle) % 0x100000 == 0:
						clsList.insert(0, StudioPlaylistViewerItem)
					else:
						clsList.insert(0, SPLStudioTrackItem)
				# #69: allow actual list views to be treated as SysListView32.List
				# so column count and other data can be retrieved easily.
				elif role == controlTypes.Role.LIST:
					clsList.insert(0, sysListView32.List)
			# Recognize known dialogs.
			case "TDemoRegForm" | "TOpenPlaylist":
				clsList.insert(0, Dialog)
			# For Studio's About dialog to reverse dialog content traversal.
			case "TAboutForm":
				clsList.insert(0, ReversedDialog)
			# Temporary cue time picker and friends.
			case "TDateTimePicker":
				clsList.insert(0, SPLTimePicker)
			case _:
				pass

	# Keep an eye on library scans in insert tracks window.
	libraryScanning = False
	scanCount = 0
	# Prevent NVDA from announcing scheduled time multiple times.
	scheduledTimeCache = ""
	# Prevent NVDA from announcing match results in Insert Tracks/search.
	matchedResultsCache = ""

	# Automatically announce mic, line in, etc changes
	# These items are static text items whose name changes.
	# Note: There are two status bars, hence the need to exclude Up time so it doesn't announce every minute.
	# Unfortunately, Window handles and WindowControlIDs seem to change, so can't be used.
	# Only announce changes if told to do so via the following function.
	def _TStatusBarChanged(self, obj: NVDAObject) -> bool:
		name = obj.name
		if name.startswith("  Up time:"):
			return False
		elif name.startswith("Scheduled for"):
			if self.scheduledTimeCache == name:
				return False
			self.scheduledTimeCache = name
			return splconfig.SPLConfig["SayStatus"]["SayScheduledFor"]
		elif "Listener" in name:
			return splconfig.SPLConfig["SayStatus"]["SayListenerCount"]
		elif name.startswith("Cart") and obj.IAccessibleChildID == 3:
			return splconfig.SPLConfig["SayStatus"]["SayPlayingCartName"]
		# In insert tracks dialog, name change event is fired continuously until actual result is known.
		# To prevent an event flood risk, say "no" if the same result text was cached.
		elif "match" in name and api.getForegroundObject().windowClassName == "TTrackInsertForm":
			return self.matchedResultsCache != name
		return True

	# Now the actual event.
	def event_nameChange(self, obj: NVDAObject, nextHandler: collections.abc.Callable[[], None]):
		# Do not let NVDA get name for None object when SPL window is maximized.
		if not obj.name:
			return
		# Only announce changes in status bar objects when told to do so.
		if obj.windowClassName == "TStatusBar" and self._TStatusBarChanged(obj):
			# Special handling for Play Status
			if obj.IAccessibleChildID == 1:
				if "Play status" in obj.name:
					# Strip off "  Play status: " for brevity only in main playlist window.
					ui.message(obj.name.split(":")[1][1:])
				elif "Loading" in obj.name:
					if splconfig.SPLConfig["General"]["LibraryScanAnnounce"] not in ("off", "ending"):
						# If library scan is in progress, announce its progress when told to do so.
						self.scanCount += 1
						if self.scanCount % 100 == 0:
							self._libraryScanAnnouncer(
								obj.name[1 : obj.name.find("]")],
								splconfig.SPLConfig["General"]["LibraryScanAnnounce"],
							)
					if not self.libraryScanning:
						self.libraryScanning = True
				elif "match" in obj.name:
					# Announce search/match results from insert tracks dialog
					# while there is no library rescan in progress.
					# Only announce match count as the whole thing is very verbose,
					# and results text would have been checked by status bar checker anyway.
					if not self.libraryScanning:
						self.matchedResultsCache = obj.name
						ui.message(" ".join(obj.name.split()[:2]))
					else:
						if (
							splconfig.SPLConfig["General"]["LibraryScanAnnounce"] != "off"
							and self.libraryScanning
						):
							if splconfig.SPLConfig["General"]["BeepAnnounce"]:
								tones.beep(370, 100)
							else:
								# Translators: Presented when library scan is complete.
								ui.message(
									_("Scan complete with {scanCount} items").format(
										scanCount=obj.name.split()[3]
									)
								)
						if self.libraryScanning:
							self.libraryScanning = False
						self.scanCount = 0
			else:
				# Because cart edit text shows cart insert status, exclude this from toggle state announcement.
				if obj.name.endswith((" On", " Off")) and not obj.name.startswith("Cart "):
					self._toggleMessage(obj.name)
				else:
					ui.message(obj.name)
				if self.cartExplorer or splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarm"]:
					# Activate mic alarm or announce when cart explorer is active.
					self.doExtraAction(obj.name)
		# Monitor the end of track and song intro time and announce it.
		elif obj.windowClassName == "TStaticText":
			if obj.simplePrevious is not None:
				if obj.simplePrevious.name == "Track Starts" and obj.parent.parent.firstChild.name == "Remaining":
					# End of track text.
					if (
						splconfig.SPLConfig["General"]["BrailleTimer"] in ("outro", "both")
						and api.getForegroundObject().processID == self.processID
					):
						braille.handler.message(obj.name)
					if (
						obj.name
						== "00:{0:02d}".format(splconfig.SPLConfig["IntroOutroAlarms"]["EndOfTrackTime"])
						and splconfig.SPLConfig["IntroOutroAlarms"]["SayEndOfTrack"]
					):
						self.alarmAnnounce(obj.name, 440, 200)
				elif obj.simplePrevious.name == "Track Starts" and obj.parent.parent.firstChild.name == "Song Ramp":
					# Song intro content.
					if (
						splconfig.SPLConfig["General"]["BrailleTimer"] in ("intro", "both")
						and api.getForegroundObject().processID == self.processID
					):
						braille.handler.message(obj.name)
					if (
						obj.name
						== "00:{0:02d}".format(splconfig.SPLConfig["IntroOutroAlarms"]["SongRampTime"])
						and splconfig.SPLConfig["IntroOutroAlarms"]["SaySongRamp"]
					):
						self.alarmAnnounce(obj.name, 512, 400, intro=True)
		nextHandler()

	# Handle toggle messages.
	def _toggleMessage(self, msg: str) -> None:
		if splconfig.SPLConfig["General"]["MessageVerbosity"] != "beginner":
			msg = msg.split()[-1]
		if splconfig.SPLConfig["General"]["BeepAnnounce"]:
			# User wishes to hear beeps instead of words. The beeps are power on and off sounds from PAC Mate Omni.
			if msg.endswith("Off"):
				if splconfig.SPLConfig["General"]["MessageVerbosity"] == "beginner":
					wavFile = os.path.join(os.path.dirname(__file__), "SPL_off.wav")
					try:
						messageSound(wavFile, msg)
					except Exception:
						pass
				else:
					tones.beep(500, 100)
					braille.handler.message(msg)
			elif msg.endswith("On"):
				if splconfig.SPLConfig["General"]["MessageVerbosity"] == "beginner":
					wavFile = os.path.join(os.path.dirname(__file__), "SPL_on.wav")
					try:
						messageSound(wavFile, msg)
					except Exception:
						pass
				else:
					tones.beep(1000, 100)
					braille.handler.message(msg)
		else:
			ui.message(msg)

	# Perform extra action in specific situations (mic alarm, for example).
	def doExtraAction(self, status: str) -> None:
		# Be sure to only deal with cart mode changes if Cart Explorer is on.
		# Optimization: Return early if the below condition is true.
		if self.cartExplorer and status.startswith("Cart") and status.endswith((" On", " Off")):
			# The best way to detect Cart Edit off is consulting file modification time.
			# Automatically reload cart information if this is the case.
			if status in ("Cart Edit Off", "Cart Insert On"):
				self.carts = splmisc.cartExplorerRefresh(api.getForegroundObject().name, self.carts)
			# Translators: Presented when cart modes are toggled while cart explorer is on.
			ui.message(_("Cart explorer is active"))
			return
		# Microphone alarm and alarm interval if defined.
		global micAlarmT, micAlarmT2
		micAlarm = splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarm"]
		# #38: only enter microphone alarm area if alarm should be turned on.
		if not micAlarm:
			if micAlarmT is not None:
				micAlarmT.cancel()
			micAlarmT = None
			if micAlarmT2 is not None:
				micAlarmT2.Stop()
			micAlarmT2 = None
		else:
			# Play an alarm sound (courtesy of Jerry Mader from Mader Radio).
			micAlarmWav = os.path.join(os.path.dirname(__file__), "SPL_MicAlarm.wav")
			# Translators: Presented when microphone was on for more than a specified time in microphone alarm dialog.
			micAlarmMessage = _("Warning: Microphone active")
			# Use a timer to play a tone when microphone was active for more than the specified amount.
			if status == "Microphone On":
				micAlarmT = threading.Timer(micAlarm, micAlarmManager, args=[micAlarmWav, micAlarmMessage])
				try:
					micAlarmT.start()
				except RuntimeError:
					micAlarmT = threading.Timer(micAlarm, messageSound, args=[micAlarmWav, micAlarmMessage])
					micAlarmT.start()
			elif status == "Microphone Off":
				if micAlarmT is not None:
					micAlarmT.cancel()
				micAlarmT = None
				if micAlarmT2 is not None:
					micAlarmT2.Stop()
				micAlarmT2 = None

	# Respond to profile switches if asked.
	def actionProfileSwitched(self) -> None:
		# #38: obtain microphone alarm status
		# (only if Studio is still alive and Studio API says something).
		status = splbase.studioAPI(2, SPLStatusInfo)
		if splbase.studioIsRunning(justChecking=True) and status is not None:
			self.doExtraAction(splconsts.studioStatusMessages[2][status])

	def actionSettingsReset(self, factoryDefaults: bool = False) -> None:
		global micAlarmT, micAlarmT2
		# Regardless of factory defaults flag, turn off microphone alarm timers.
		if micAlarmT is not None:
			micAlarmT.cancel()
		micAlarmT = None
		if micAlarmT2 is not None:
			micAlarmT2.Stop()
		micAlarmT2 = None
		status = splbase.studioAPI(2, SPLStatusInfo)
		if splbase.studioIsRunning(justChecking=True) and status is not None:
			self.doExtraAction(splconsts.studioStatusMessages[2][status])

	# Alarm announcement: Alarm notification via beeps, speech or both.
	def alarmAnnounce(self, timeText: str, tone: float, duration: int, intro: bool = False) -> None:
		if splconfig.SPLConfig["General"]["AlarmAnnounce"] in ("beep", "both"):
			tones.beep(tone, duration)
		if splconfig.SPLConfig["General"]["AlarmAnnounce"] in ("message", "both"):
			alarmTime = int(timeText.split(":")[1])
			if intro:
				# Translators: Presented when end of introduction is approaching
				# (example output: 5 sec left in track introduction).
				ui.message(
					_("Warning: {seconds} sec left in track introduction").format(seconds=str(alarmTime))
				)
			else:
				# Translators: Presented when end of track is approaching.
				ui.message(_("Warning: {seconds} sec remaining").format(seconds=str(alarmTime)))

	# Add or remove SPL-specific touch commands.
	# Code comes from Enhanced Touch Gestures add-on from the same author.
	# This may change if NVDA core decides to abandon touch mode concept.

	def event_appModule_gainFocus(self):
		if touchHandler.handler:
			if "SPL" not in touchHandler.availableTouchModes:
				touchHandler.availableTouchModes.append("SPL")
				# Add the human-readable representation also.
				# Translators: the label for a dedicated touch mode for SPL Studio.
				touchHandler.touchModeLabels["spl"] = _("SPL mode")

	def event_appModule_loseFocus(self):
		if touchHandler.handler:
			# Switch to object mode.
			touchHandler.handler._curTouchMode = touchHandler.availableTouchModes[1]
			if "SPL" in touchHandler.availableTouchModes:
				# If we have too many touch modes, pop all except the original entries.
				for mode in touchHandler.availableTouchModes:
					if mode == "SPL":
						touchHandler.availableTouchModes.pop()
			try:
				del touchHandler.touchModeLabels["spl"]
			except KeyError:
				pass

	# React to show events from certain windows.

	def event_show(self, obj: NVDAObject, nextHandler: collections.abc.Callable[[], None]):
		if obj.windowClassName == "TRequests" and splconfig.SPLConfig["General"]["RequestsAlert"]:
			nvwave.playWaveFile(os.path.join(os.path.dirname(__file__), "SPL_Requests.wav"))
		nextHandler()

	# Save configuration and perform other tasks when terminating.
	def terminate(self):
		super().terminate()
		# Unregister profile switch and reset handlers.
		splactions.SPLActionProfileSwitched.unregister(self.actionProfileSwitched)
		splactions.SPLActionSettingsReset.unregister(self.actionSettingsReset)
		# Don't forget about metadata connection announcement handlers.
		splactions.SPLActionProfileSwitched.unregister(splmisc.metadata_actionProfileSwitched)
		splactions.SPLActionSettingsReset.unregister(splmisc.metadata_actionSettingsReset)
		# Perform app module termination work via action handlers.
		# Among other tasks, close any opened SPL add-on dialogs.
		splactions.SPLActionAppTerminating.notify()
		# #39: terminate microphone alarm/interval threads, otherwise errors are seen.
		global micAlarmT, micAlarmT2
		if micAlarmT is not None:
			micAlarmT.cancel()
		micAlarmT = None
		if micAlarmT2 is not None:
			micAlarmT2.Stop()
		micAlarmT2 = None
		splconfig.terminateStudioExtraSteps()
		splconfig.closeConfig(self.appName)
		# Delete focused track reference.
		self._focusedTrack = None
		# #86: track time analysis marker should be gone, too.
		self._analysisMarker = None
		# #41: We're done monitoring Studio API.
		if self._SPLStudioMonitor is not None:
			self._SPLStudioMonitor.Stop()
			self._SPLStudioMonitor = None
		try:
			self.prefsMenu.Remove(self.SPLSettings)
		except (RuntimeError, AttributeError):
			pass
		# Tell the handle finder thread it's time to leave this world.
		self.noMoreHandle.set()
		# Manually clear the following dictionaries.
		self.carts.clear()
		self._cachedStatusObjs.clear()
		# Don't forget to reset timestamps for cart files.
		splmisc.cartEditTimestamps = []
		# Just to make sure:
		splbase.setStudioWindowHandle(None)

	# A few time related scripts (elapsed time, remaining time, etc.).

	# Specific to time scripts using Studio API.
	# Split this into two functions: the announcer (below) and formatter.
	# The ms (millisecond) argument will be used when announcing playlist remainder.
	# Include hours by default unless told not to do so.
	# #155: time can be None, in which case it will do nothing.
	def announceTime(
		self, t: int | None, offset: int | None = None, ms: bool = True, includeHours: bool | None = None
	) -> None:
		if t is None:
			return
		if t <= 0:
			ui.message("00:00")
		else:
			ui.message(self._ms2time(t, offset=offset, ms=ms, includeHours=includeHours))

	# Formatter: given time in milliseconds, convert it to human-readable format.
	# There will be times when one will deal with time in seconds.
	# For some cases, do not include hour slot when trying to conform to what Studio displays.)
	def _ms2time(
		self, t: int, offset: int | None = None, ms: bool = True, includeHours: bool | None = None
	) -> str:
		if t <= 0:
			return "00:00"
		else:
			if ms:
				# Be sure to convert time into integer indirectly via floor division.
				t = (t // 1000) if not offset else (t // 1000) + offset
			mm, ss = divmod(t, 60)
			if mm > 59 and (
				includeHours or (includeHours is None and splconfig.SPLConfig["General"]["TimeHourAnnounce"])
			):
				hh, mm = divmod(mm, 60)
				return f"{hh:02d}:{mm:02d}:{ss:02d}"
			else:
				return f"{mm:02d}:{ss:02d}"

	@scriptHandler.script(
		# Message comes from Foobar 2000 app module, part of NVDA Core.
		description=translate("Reports the remaining time of the currently playing track, if any"),
		gestures=["kb:control+alt+t", "ts(SPL):2finger_flickDown"],
		speakOnDemand=True,
	)
	def script_sayRemainingTime(self, gesture):
		if splbase.studioIsRunning():
			self.announceTime(splbase.studioAPI(3, SPLCurTrackPlaybackTime), offset=1)

	@scriptHandler.script(
		# Message comes from Foobar 2000 app module, part of NVDA Core.
		description=translate("Reports the elapsed time of the currently playing track, if any"),
		gesture="kb:alt+shift+t",
		speakOnDemand=True,
	)
	def script_sayElapsedTime(self, gesture):
		if splbase.studioIsRunning():
			self.announceTime(splbase.studioAPI(0, SPLCurTrackPlaybackTime))

	@scriptHandler.script(
		description=_(
			# Translators: Input help mode message for a command in StationPlaylist add-on.
			"Announces broadcaster time. "
			"If pressed twice, reports minutes and seconds left to top of the hour."
		),
		gestures=["kb:shift+nvda+f12", "ts(SPL):2finger_flickUp"],
		speakOnDemand=True,
	)
	def script_sayBroadcasterTime(self, gesture):
		if not splbase.studioIsRunning():
			return
		# Says things such as "25 minutes to 2" and "5 past 11".
		# #29: Also announces top of hour timer (mm:ss), the clock next to broadcaster time.
		# Parse the local time and say it similar to how Studio presents broadcaster time.
		localtime = time.localtime()
		# For both broadcaster time and top of hour, minute is needed.
		m = localtime[4]
		if scriptHandler.getLastScriptRepeatCount() == 0:
			h = localtime[3]
			if h not in (0, 12):
				h %= 12
			if m == 0:
				if h == 0:
					h += 12
				# Messages in this method should not be translated.
				ui.message("{hour} o'clock".format(hour=h))
			elif 1 <= m <= 30:
				if h == 0:
					h += 12
				ui.message("{minute} min past {hour}".format(minute=m, hour=h))
			else:
				if h == 12:
					h = 1
				m = 60 - m
				ui.message("{minute} min to {hour}".format(minute=m, hour=h + 1))
		else:
			self.announceTime(3600 - (m * 60 + localtime[5]), ms=False)

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Announces time including seconds."),
		speakOnDemand=True,
	)
	def script_sayCompleteTime(self, gesture):
		if not splbase.studioIsRunning():
			return
		# Says complete time in hours, minutes and seconds via kernel32's routines.
		ui.message(winKernel.GetTimeFormatEx(winKernel.LOCALE_NAME_USER_DEFAULT, 0, None, None))

	# Show the Alarms panel in add-on settings screen.

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Opens SPL Studio alarms settings."),
		gestures=["kb:alt+nvda+1", "ts(SPL):2finger_flickRight"],
	)
	def script_openAlarmsSettings(self, gesture):
		wx.CallAfter(splconfui.openAddonSettingsPanel, splconfui.AlarmsPanel)

	# SPL Config management among others.

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Opens SPL Studio add-on configuration dialog."),
		gestures=["kb:alt+NVDA+0", "ts(SPL):2finger_flickLeft"],
	)
	def script_openConfigDialog(self, gesture):
		# Rather than calling the config dialog open event,
		# call the open dialog function directly to avoid indirection.
		wx.CallAfter(splconfui.openAddonSettingsPanel, None)

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Opens SPL add-on broadcast profiles dialog."),
		gesture="kb:alt+NVDA+p",
	)
	def script_openBroadcastProfilesDialog(self, gesture):
		wx.CallAfter(splconfui.onBroadcastProfilesDialog, None)

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Opens SPL Studio add-on welcome dialog."),
		gesture="kb:alt+NVDA+f1",
	)
	def script_openWelcomeDialog(self, gesture):
		gui.mainFrame.prePopup()
		d = splconfig.WelcomeDialog(gui.mainFrame)
		d.Raise()
		d.Show()
		gui.mainFrame.postPopup()

	# Other commands (track finder and others)

	# Braille timer.
	# Announce end of track and other info via braille.

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Toggles between various braille timer settings."),
		gesture="kb:control+shift+x",
	)
	def script_setBrailleTimer(self, gesture):
		brailleTimer = splconfig.SPLConfig["General"]["BrailleTimer"]
		if brailleTimer == "off":
			brailleTimer = "outro"
		elif brailleTimer == "outro":
			brailleTimer = "intro"
		elif brailleTimer == "intro":
			brailleTimer = "both"
		else:
			brailleTimer = "off"
		splconfig.SPLConfig["General"]["BrailleTimer"] = brailleTimer
		splconfig.message("BrailleTimer", brailleTimer)

	# The track finder utility for find track script and other functions
	# Perform a linear search to locate the track name and/or description which matches the entered value.
	# Also, find column content for a specific column if requested.
	# The below routines are also used in place marker track locator.

	# Search history
	# Accept both None and str because it will be filtered to remove None anyway.
	findText: list[str] | None = None

	def trackFinder(
		self, text: str, obj: NVDAObject, directionForward: bool = True, column: list[int] | None = None
	) -> None:
		speech.cancelSpeech()
		# #32: Update search text even if the track with the search term in columns does not exist.
		# #27: especially if the search history is empty.
		# Thankfully, track finder dialog will populate the first item,
		# but it is better to check a second time for debugging purposes.
		if self.findText is None:
			self.findText = []
		if text not in self.findText:
			self.findText.insert(0, text)
		if obj is not None and not column:
			column = [obj.indexOf("Artist"), obj.indexOf("Title")]
		track = self._trackLocator(text, obj=obj, directionForward=directionForward, columns=column)
		if track:
			# We need to fire set focus event twice and exit this routine.
			# (done via doAction method).
			track.doAction()
		else:
			wx.CallAfter(
				gui.messageBox,
				# Translators: Standard dialog message when an item one wishes to search is not found
				# (copy this from main nvda.po).
				_('text "%s" not found') % text,
				translate("0 matches"),
				wx.OK | wx.ICON_INFORMATION,
			)

	# Split from track finder in 2015.
	# Return a track with the given search criteria.
	# Column is a list of columns to be searched.
	def _trackLocator(
		self,
		text: str,
		obj: NVDAObject | None = None,
		directionForward: bool = True,
		columns: list[int] | None = None,
	) -> NVDAObject | None:
		# It doesn't make sense to search for tracks if text and/or columns are not specified.
		# It is also an optimization because the below loop will not be run if any of the following are true.
		if not text or not columns:
			return None
		nextTrack = "next" if directionForward else "previous"
		while obj is not None:
			for column in columns:
				columnText = obj._getColumnContentRaw(column)
				if columnText and text in columnText:
					return obj
			obj = getattr(obj, nextTrack)
		return None

	# Find a specific track based on a searched text.
	# But first, check if track finder can be invoked.
	# Attempt level specifies which track finder to open (0 = Track Finder, 1 = Column Search, 2 = Time range).
	def _trackFinderCheck(self, attemptLevel: int) -> bool:
		if not splbase.studioIsRunning():
			return False
		playlistErrors = self.canPerformPlaylistCommands(announceErrors=False)
		if playlistErrors == self.SPLPlaylistNotFocused:
			# Different responses based on structural pattern matching results.
			match attemptLevel:
				case 0:
					# Translators: Presented when a user attempts to find tracks but is not at the track list.
					ui.message(_("Track finder is available only in track list."))
				case 1:
					# Translators: Presented when a user attempts to find tracks but is not at the track list.
					ui.message(_("Column search is available only in track list."))
				case 2:
					# Translators: Presented when a user attempts to find tracks but is not at the track list.
					ui.message(_("Time range finder is available only in track list."))
				case _:
					pass
			return False
		# Make sure a playlist is loaded.
		elif playlistErrors == self.SPLPlaylistNotLoaded:
			# Translators: Presented when a user wishes to find a track but didn't add any tracks.
			ui.message(_("You need to add at least one track to find tracks."))
			return False
		return True

	def trackFinderGUI(self, directionForward: bool = True, columnSearch: bool = False) -> None:
		try:
			if not columnSearch:
				# Translators: Title for track finder dialog.
				title = _("Find track")
			else:
				# Translators: Title for column search dialog.
				title = _("Column search")
			startObj = api.getFocusObject()
			if (
				api.getForegroundObject().windowClassName == "TStudioForm"
				and startObj.role == controlTypes.Role.LIST
			):
				startObj = startObj.firstChild
			d = splmisc.SPLFindDialog(
				gui.mainFrame,
				startObj,
				self.findText[0] if self.findText and len(self.findText) else "",
				title,
				directionForward=directionForward,
				columnSearch=columnSearch,
			)
			gui.mainFrame.prePopup()
			d.Raise()
			d.Show()
			gui.mainFrame.postPopup()
		except RuntimeError:
			wx.CallAfter(splmisc.finderError)

	# Perform actions as directed by below scripts
	# (open track finder dialog variants, search forward or backward, full find or find next/previous).
	def findTrackDispatch(
		self, directionForward: bool = True, columnSearch: bool = False, incrementalFind: bool = False
	) -> None:
		if self._trackFinderCheck(1 if columnSearch else 0):
			# Although counterintuitive, filtering must take place to avoid finding nothing or everything.
			# With incremental find set, passing in None or an empty string to track finder
			# results in "finding" the next or previous track.
			if self.findText is not None:
				# Avoid type error when opening track finder dialog.
				self.findText = list(filter(lambda x: x not in (None, ""), self.findText))
				# Nullify find text list if it is empty for compatibility with code checking for None.
				# This is more so for incremental find next/previous.
				if not len(self.findText):
					self.findText = None
			if self.findText is None or not incrementalFind:
				self.trackFinderGUI(directionForward=directionForward, columnSearch=columnSearch)
			else:
				startObj = api.getFocusObject()
				if (
					api.getForegroundObject().windowClassName == "TStudioForm"
					and startObj.role == controlTypes.Role.LIST
				):
					startObj = startObj.firstChild if directionForward else startObj.lastChild
				startObj = startObj.next if directionForward else startObj.previous
				self.trackFinder(self.findText[0], startObj, directionForward=directionForward)

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Finds a track in the track list."),
		gesture="kb:control+nvda+f",
	)
	def script_findTrack(self, gesture):
		self.findTrackDispatch()

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Finds text in columns.")
	)
	def script_columnSearch(self, gesture):
		self.findTrackDispatch(columnSearch=True)

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Finds the next occurrence of the track with the name in the track list."),
		gesture="kb:nvda+f3",
	)
	def script_findTrackNext(self, gesture):
		self.findTrackDispatch(incrementalFind=True)

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Finds previous occurrence of the track with the name in the track list."),
		gesture="kb:shift+nvda+f3",
	)
	def script_findTrackPrevious(self, gesture):
		self.findTrackDispatch(directionForward=False, incrementalFind=True)

	# Time range finder.
	# Locate a track with duration falling between min and max.

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Locates track with duration within a time range")
	)
	def script_timeRangeFinder(self, gesture):
		if self._trackFinderCheck(2):
			try:
				d = splmisc.SPLTimeRangeDialog(gui.mainFrame, api.getFocusObject())
				gui.mainFrame.prePopup()
				d.Raise()
				d.Show()
				gui.mainFrame.postPopup()
			except RuntimeError:
				wx.CallAfter(splmisc.finderError)

	# Cart explorer
	cartExplorer = False
	# The carts dictionary (key = cart gesture, item = cart name).
	carts: dict[str, Any] = {}

	# Assigning and building carts.

	def cartsBuilder(self, build: bool = True) -> None:
		# A function to build and return cart commands.
		if build:
			for cart in splconsts.cartKeys:
				self.bindGesture(f"kb:{cart}", "cartExplorer")
				self.bindGesture(f"kb:shift+{cart}", "cartExplorer")
				self.bindGesture(f"kb:control+{cart}", "cartExplorer")
				self.bindGesture(f"kb:alt+{cart}", "cartExplorer")
		else:
			self.clearGestureBindings()
			self.bindGestures(self.__gestures)

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Toggles cart explorer to learn cart assignments."),
		gesture="kb:alt+nvda+3",
	)
	def script_toggleCartExplorer(self, gesture):
		if not splbase.studioIsRunning():
			return
		if not self.cartExplorer:
			# Prevent cart explorer from being engaged outside of playlist viewer.
			fg = api.getForegroundObject()
			if fg.windowClassName != "TStudioForm":
				# Translators: Presented when cart explorer cannot be entered.
				ui.message(_("You are not in playlist viewer, cannot enter cart explorer"))
				return
			# Studio 6 demo uses "Demo" as default user name, therefore remove user name.
			studioTitle = fg.name
			if "Demo - Demo" in studioTitle:
				studioTitle = "StationPlaylist Studio Demo"
			self.carts = splmisc.cartExplorerInit(studioTitle)
			if self.carts["faultyCarts"]:
				# Translators: presented when cart explorer could not be switched on.
				ui.message(_("Some or all carts could not be assigned, cannot enter cart explorer"))
				return
			else:
				self.cartExplorer = True
				self.cartsBuilder()
				# Translators: Presented when cart explorer is on.
				ui.message(_("Entering cart explorer"))
		else:
			self.cartExplorer = False
			self.cartsBuilder(build=False)
			self.carts.clear()
			splmisc.cartEditTimestamps = []
			# Translators: Presented when cart explorer is off.
			ui.message(_("Exiting cart explorer"))

	def script_cartExplorer(self, gesture):
		if api.getForegroundObject().windowClassName != "TStudioForm":
			gesture.send()
			return
		if scriptHandler.getLastScriptRepeatCount() >= 1:
			gesture.send()
		else:
			if gesture.displayName in self.carts:
				ui.message(self.carts[gesture.displayName])
			elif self.carts["standardLicense"] and (
				len(gesture.displayName) == 1 or gesture.displayName[-2] == "+"
			):
				# Translators: Presented when cart command is unavailable.
				ui.message(_("Cart command unavailable"))
			else:
				# Translators: Presented when there is no cart assigned to a cart command.
				ui.message(_("Cart unassigned"))

	# Library scan announcement
	# Announces progress of a library scan
	# (launched from insert tracks dialog by pressing Control+Shift+R
	# or from rescan option from Options dialog).

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Toggles library scan progress settings."),
		gesture="kb:shift+nvda+r",
	)
	def script_setLibraryScanProgress(self, gesture):
		libraryScanAnnounce = splconfig.SPLConfig["General"]["LibraryScanAnnounce"]
		if libraryScanAnnounce == "off":
			libraryScanAnnounce = "ending"
		elif libraryScanAnnounce == "ending":
			libraryScanAnnounce = "progress"
		elif libraryScanAnnounce == "progress":
			libraryScanAnnounce = "numbers"
		else:
			libraryScanAnnounce = "off"
		splconfig.SPLConfig["General"]["LibraryScanAnnounce"] = libraryScanAnnounce
		splconfig.message("LibraryScanAnnounce", libraryScanAnnounce)

	@scriptHandler.script(gesture="kb:control+shift+r")
	def script_startScanFromInsertTracks(self, gesture):
		gesture.send()
		fg = api.getForegroundObject()
		if fg.windowClassName == "TTrackInsertForm":
			# Translators: Presented when library scan has started.
			ui.message(_("Scan start")) if not splconfig.SPLConfig["General"]["BeepAnnounce"] else tones.beep(
				740, 100
			)
			self.libraryScanning = True

	# Report library scan (number of items scanned) in the background.
	def monitorLibraryScan(self) -> None:
		global libScanT
		if (
			libScanT
			and libScanT.is_alive()
			and api.getForegroundObject().windowClassName == "TTrackInsertForm"
		):
			return
		# #155: ideally library scan count would be an integer.
		libScanCount: int | None = splbase.studioAPI(1, SPLLibraryScanCount)
		if libScanCount is not None and libScanCount < 0:
			self.libraryScanning = False
			return
		time.sleep(0.1)
		# Is library scan count still an integer?
		libScanCount = splbase.studioAPI(1, SPLLibraryScanCount)
		if libScanCount is None:
			self.libraryScanning = False
			return
		# Library scan may have finished while this thread was sleeping.
		if libScanCount < 0:
			self.libraryScanning = False
			# Translators: Presented when library scanning is finished.
			ui.message(_("{itemCount} items in the library").format(
				itemCount=splbase.studioAPI(0, SPLLibraryScanCount)
			))
		else:
			libScanT = threading.Thread(target=self.libraryScanReporter)
			libScanT.daemon = True
			libScanT.start()

	def libraryScanReporter(self) -> None:
		scanIter = 0
		scanCount: int | None = splbase.studioAPI(1, SPLLibraryScanCount)
		while scanCount is not None and scanCount >= 0:
			if not self.libraryScanning or not splbase.studioIsRunning(justChecking=True):
				return
			time.sleep(1)
			# Do not continue if we're back on insert tracks form or library scan is finished.
			if api.getForegroundObject().windowClassName == "TTrackInsertForm" or not self.libraryScanning:
				return
			# Scan count may have changed during sleep.
			scanCount = splbase.studioAPI(1, SPLLibraryScanCount)
			# Return early if scan count is None (Studio dies).
			# This also means library scan progress will not be announced (makes sense since Studio is gone).
			if scanCount is None:
				self.libraryScanning = False
				return
			if scanCount < 0:
				break
			scanIter += 1
			if scanIter % 5 == 0 and splconfig.SPLConfig["General"]["LibraryScanAnnounce"] not in (
				"off",
				"ending",
			):
				# Queue the announcement to main thread because of braille handler thread.
				wx.CallAfter(
					self._libraryScanAnnouncer,
					scanCount,
					splconfig.SPLConfig["General"]["LibraryScanAnnounce"],
				)
		self.libraryScanning = False
		# What if config database died?
		if splconfig.SPLConfig and splconfig.SPLConfig["General"]["LibraryScanAnnounce"] != "off":
			if splconfig.SPLConfig["General"]["BeepAnnounce"]:
				tones.beep(370, 100)
			else:
				# Translators: Presented after library scan is done.
				ui.message(
					_("Scan complete with {itemCount} items").format(
						itemCount=splbase.studioAPI(0, SPLLibraryScanCount)
					)
				)

	# Take care of library scanning announcement.
	def _libraryScanAnnouncer(self, count: int, announcementType: str) -> None:
		if announcementType == "progress":
			# Translators: Presented when library scan is in progress.
			tones.beep(550, 100) if splconfig.SPLConfig["General"]["BeepAnnounce"] else ui.message(
				_("Scanning")
			)
		elif announcementType == "numbers":
			if splconfig.SPLConfig["General"]["BeepAnnounce"]:
				tones.beep(550, 100)
				# No need to provide translatable string - just use index.
				ui.message("{0}".format(count))
			else:
				# Translators: Presented when library scan is in progress.
				ui.message(_("{itemCount} items scanned").format(itemCount=count))

	# Place markers.
	placeMarker: str | None = None

	# Is the place marker set on this track?
	# Track argument is None (only useful for debugging purposes).
	def isPlaceMarkerTrack(self, track: NVDAObject | None = None) -> bool:
		if track is None:
			track = api.getFocusObject()
		# No, only list items can become place marker tracks.
		if track.role != controlTypes.Role.LISTITEM:
			raise ValueError("Only list items can be marked as a place marker track")
		if self.placeMarker == track._getColumnContentRaw(track.indexOf("Filename")):
			return True
		return False

	# Used in delete track workaround routine.
	def preTrackRemoval(self) -> None:
		try:
			if self.isPlaceMarkerTrack(track=api.getFocusObject()):
				self.placeMarker = None
		except ValueError:
			pass

	# Metadata streaming manager
	# Obtains information on metadata streaming for each URL,
	# notifying the broadcaster if told to do so upon startup.
	# Also allows broadcasters to toggle metadata streaming.

	# The script version to open the manage metadata URL's dialog.
	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Opens a dialog to quickly enable or disable metadata streaming.")
	)
	def script_manageMetadataStreams(self, gesture):
		# Do not even think about opening this dialog if handle to Studio isn't found (not fully running).
		if not splbase.studioIsRunning(justChecking=True):
			# Translators: Presented when streaming dialog cannot be shown.
			ui.message(_("Cannot open metadata streaming dialog"))
			return
		try:
			# #44: do not rely on Studio API function object as its workings (including arguments) may change.
			# Use a flag to tell the streaming dialog that this is
			# invoked from somewhere other than add-on settings dialog.
			d = splconfui.MetadataStreamingDialog(gui.mainFrame)
			gui.mainFrame.prePopup()
			d.Raise()
			d.Show()
			gui.mainFrame.postPopup()
		except RuntimeError:
			# #125: call centralized error handler.
			wx.CallAfter(splconfui.configDialogOpenError)

	# Playlist Analyzer
	# These include track time analysis, playlist snapshots, and some form of playlist transcripts and others.
	# Although not directly related to this, track finder and its friends,
	# as well as remaining playlist duration command also fall under playlist analyzer.
	# A playlist must be loaded and visible in order for these to work,
	# or for some, most recent focused track must be known.

	# Possible playlist errors.
	SPLPlaylistNoErrors = 0
	SPLPlaylistNotFocused = 1
	SPLPlaylistNotLoaded = 2
	SPLPlaylistLastFocusUnknown = 3

	def canPerformPlaylistCommands(
		self, playlistViewerRequired: bool = True, mustSelectTrack: bool = False, announceErrors: bool = True
	) -> int:
		# #81: most commands do require that playlist viewer must be
		# the foreground window (focused), hence the keyword argument.
		# Also let NVDA announce generic error messages listed below if told to do so,
		# and for some cases, not at all because the caller will announce them.
		playlistViewerFocused = api.getForegroundObject().windowClassName == "TStudioForm"
		if playlistViewerRequired and not playlistViewerFocused:
			if announceErrors:
				# Translators: an error message presented when performing some playlist commands
				# while focused on places other than Playlist Viewer.
				ui.message(_("Please return to playlist viewer before invoking this command."))
			return self.SPLPlaylistNotFocused
		if not splbase.studioAPI(0, SPLTrackCount):
			if announceErrors:
				# Translators: an error message presented when performing some playlist commands
				# while no playlist has been loaded.
				ui.message(_("No playlist has been loaded."))
			return self.SPLPlaylistNotLoaded
		if mustSelectTrack and self._focusedTrack is None:
			if announceErrors:
				# Translators: an error message presented when performing some playlist commands
				# while no tracks are selected/focused.
				ui.message(_("Please select a track from playlist viewer before invoking this command."))
			return self.SPLPlaylistLastFocusUnknown
		return self.SPLPlaylistNoErrors

	# Track time analysis/Playlist snapshots
	# Return total length of the selected tracks upon request.
	# Analysis command (SPL Assistant) will be assignable.
	# Also gather various data about the playlist.
	_analysisMarker: int | None = None

	# Trakc time analysis and playlist snapshots, and to some extent, some parts of playlist transcripts
	# require main playlist viewer to be the foreground window.
	# Track time analysis does require knowing the start and ending track, while others do not.
	def _trackAnalysisAllowed(self, mustSelectTrack: bool = True) -> bool:
		if not splbase.studioIsRunning():
			return False
		# #81: just return the result of consulting playlist dispatch along with error messages if any.
		match self.canPerformPlaylistCommands(mustSelectTrack=mustSelectTrack, announceErrors=False):
			case self.SPLPlaylistNotFocused:
				# Translators: Presented when playlist analyzer cannot be performed
				# because user is not focused on playlist viewer.
				ui.message(_("Not in playlist viewer, cannot perform playlist analysis."))
				return False
			case self.SPLPlaylistNotLoaded:
				# Translators: reported when no playlist has been loaded when trying to perform playlist analysis.
				ui.message(_("No playlist to analyze."))
				return False
			case self.SPLPlaylistLastFocusUnknown:
				# Translators: Presented when playlist analysis cannot be activated.
				ui.message(_("No tracks are selected, cannot perform playlist analysis."))
				return False
			case _:
				return True

	# Return total duration of a range of tracks.
	# This is used in track time analysis when multiple tracks are selected.
	# This is also called from playlist duration scripts.
	def playlistDuration(self, start: NVDAObject | None = None, end: NVDAObject | None = None) -> int:
		if start is None:
			start = api.getFocusObject()
		duration = start.indexOf("Duration")
		totalDuration = 0
		obj = start
		while obj not in (None, end):
			# Technically segue.
			segue = obj._getColumnContentRaw(duration)
			# NVDA returns an empty string instead of None in order to
			# avoid errors with 64-bit SysListView32 controls.
			# For compatibility, check both None and an empty string.
			if segue not in (None, "", "00:00"):
				hms = segue.split(":")
				totalDuration += (int(hms[-2]) * 60) + int(hms[-1])
				if len(hms) == 3:
					totalDuration += int(hms[0]) * 3600
			obj = obj.next
		return totalDuration

	# Playlist snapshots
	# Data to be gathered comes from a set of flags.
	# By default, playlist duration (including shortest and average),
	# category summary and other statistics will be gathered.
	def playlistSnapshots(
		self, obj: NVDAObject, end: NVDAObject | None, snapshotFlags: list[str] | None = None
	) -> dict[str, Any]:
		# #55: is this a complete snapshot?
		completePlaylistSnapshot = obj.IAccessibleChildID == 1 and end is None
		# Track count and total duration are always included.
		# #155: annotate snapshot map to avoid type annotation issues when assigning key/value pairs.
		snapshot: dict[str, Any] = {}
		if snapshotFlags is None:
			snapshotFlags = [
				flag
				for flag in splconfig.SPLConfig["PlaylistSnapshots"]
				if splconfig.SPLConfig["PlaylistSnapshots"][flag]
			]
		duration = obj.indexOf("Duration")
		title = obj.indexOf("Title")
		# A tuple list of duration in seconds (integer) and track titles.
		# Used to obtain total duration, average, shortest, and longest tracks.
		trackLengths = []
		totalDuration = 0
		artist = obj.indexOf("Artist")
		artists = []
		category = obj.indexOf("Category")
		categories = []
		genre = obj.indexOf("Genre")
		genres = []
		# A specific version of the playlist duration loop is needed in order to gather statistics.
		while obj not in (None, end):
			segue = obj._getColumnContentRaw(duration)
			trackTitle = obj._getColumnContentRaw(title)
			categories.append(obj._getColumnContentRaw(category))
			# Don't record artist and genre information for an hour marker (reported by a broadcaster).
			if categories[-1] != "Hour Marker":
				artists.append(obj._getColumnContentRaw(artist))
				genres.append(obj._getColumnContentRaw(genre))
			# Convert segue to an integer for ease of min/max comparison.
			# NVDA returns an empty string instead of None in order to
			# avoid errors with 64-bit SysListView32 controls.
			# For compatibility, check both None and an empty string.
			if segue not in (None, ""):
				hms = segue.split(":")
				segue = (int(hms[-2]) * 60) + int(hms[-1])
				if len(hms) == 3:
					segue += int(hms[0]) * 3600
				totalDuration += segue
				trackLengths.append((segue, trackTitle))
			obj = obj.next
		# #55: use total track count if it is an entire playlist, if not, resort to categories count.
		if completePlaylistSnapshot:
			snapshot["PlaylistItemCount"] = splbase.studioAPI(0, SPLTrackCount)
		else:
			snapshot["PlaylistItemCount"] = len(categories)
		snapshot["PlaylistTrackCount"] = len(artists)
		snapshot["PlaylistDurationTotal"] = self._ms2time(totalDuration, ms=False)
		# Shortest and longest tracks.
		if "DurationMinMax" in snapshotFlags:
			trackDurations = [track[0] for track in trackLengths]
			# #159: do not record shortest/longest tracks if the playlist consists of hour markers.
			if len(trackDurations) > 0:
				shortest = min(trackDurations)
				shortestIndex = trackDurations.index(shortest)
				snapshot["PlaylistDurationMin"] = "{} ({})".format(
					trackLengths[shortestIndex][1], self._ms2time(trackLengths[shortestIndex][0], ms=False)
				)
				longest = max(trackDurations)
				longestIndex = trackDurations.index(longest)
				snapshot["PlaylistDurationMax"] = "{} ({})".format(
					trackLengths[longestIndex][1], self._ms2time(trackLengths[longestIndex][0], ms=False)
				)
		if "DurationAverage" in snapshotFlags:
			# #57: zero division error may occur if the playlist consists of hour markers only.
			try:
				# Track count is an integer, so use floor division.
				snapshot["PlaylistDurationAverage"] = self._ms2time(
					totalDuration // snapshot["PlaylistTrackCount"], ms=False
				)
			except ZeroDivisionError:
				snapshot["PlaylistDurationAverage"] = "00:00"
		if "CategoryCount" in snapshotFlags:
			snapshot["PlaylistCategoryCount"] = collections.Counter(categories)
		if "ArtistCount" in snapshotFlags:
			snapshot["PlaylistArtistCount"] = collections.Counter(artists)
		if "GenreCount" in snapshotFlags:
			snapshot["PlaylistGenreCount"] = collections.Counter(genres)
		return snapshot

	# Output formatter for playlist snapshots.
	# Pressing once will speak and/or braille it, pressing twice or more will output this info to an HTML file.

	def playlistSnapshotOutput(self, snapshot: dict[str, Any], scriptCount: int) -> None:
		statusInfo = [
			# Translators: one of the results for playlist snapshots feature
			# for announcing total number of items in a playlist.
			_("Items: {playlistItemCount}").format(playlistItemCount=snapshot["PlaylistItemCount"])
		]
		statusInfo.append(
			# Translators: one of the results for playlist snapshots feature
			# for announcing total number of tracks in a playlist.
			_("Tracks: {playlistTrackCount}").format(playlistTrackCount=snapshot["PlaylistTrackCount"])
		)
		statusInfo.append(
			# Translators: one of the results for playlist snapshots feature
			# for announcing total duration of a playlist.
			_("Duration: {playlistTotalDuration}").format(
				playlistTotalDuration=snapshot["PlaylistDurationTotal"]
			)
		)
		if "PlaylistDurationMin" in snapshot:
			statusInfo.append(
				# Translators: one of the results for playlist snapshots feature
				# for announcing shortest track name and duration of a playlist.
				_("Shortest: {playlistShortestTrack}").format(
					playlistShortestTrack=snapshot["PlaylistDurationMin"]
				)
			)
			statusInfo.append(
				# Translators: one of the results for playlist snapshots feature
				# for announcing longest track name and duration of a playlist.
				_("Longest: {playlistLongestTrack}").format(
					playlistLongestTrack=snapshot["PlaylistDurationMax"]
				)
			)
		if "PlaylistDurationAverage" in snapshot:
			statusInfo.append(
				# Translators: one of the results for playlist snapshots feature
				# for announcing average duration for tracks in a playlist.
				_("Average: {playlistAverageDuration}").format(
					playlistAverageDuration=snapshot["PlaylistDurationAverage"]
				)
			)
		# For top artists and genres, report statistics if there is an actual common entries counter.
		if "PlaylistArtistCount" in snapshot:
			artistCount = splconfig.SPLConfig["PlaylistSnapshots"]["ArtistCountLimit"]
			artists = snapshot["PlaylistArtistCount"].most_common(None if not artistCount else artistCount)
			if scriptCount == 0:
				try:
					statusInfo.append(
						# Translators: one of the results for playlist snapshots feature
						# for announcing top artist in a playlist.
						_("Top artist: {} ({})").format(artists[0][0], artists[0][1])
					)
				except IndexError:
					statusInfo.append(
						# Translators: one of the results for playlist snapshots feature
						# when there is no top artist.
						_("Top artist: none")
					)
			elif scriptCount == 1:
				if len(artists) == 0:
					statusInfo.append(
						# Translators: one of the results for playlist snapshots feature
						# when there is no top artist (formatted for browse mode).
						_("Top artists: none")
					)
				else:
					artistList = []
					# Translators: one of the results for playlist snapshots feature,
					# a heading for a group of items.
					header = _("Top artists:")
					for item in artists:
						artist, count = item
						if artist is None:
							# Translators: one of the results for playlist snapshots feature
							# when there is no artist information.
							info = _("No artist information ({artistCount})").format(artistCount=count)
						else:
							# Translators: one of the results for playlist snapshots feature
							# for artist count information.
							info = _("{artistName} ({artistCount})").format(
								artistName=artist, artistCount=count
							)
						artistList.append("<li>{}</li>".format(info))
					statusInfo.append("".join([header, "<ol>", "\n".join(artistList), "</ol>"]))
		if "PlaylistCategoryCount" in snapshot:
			categoryCount = splconfig.SPLConfig["PlaylistSnapshots"]["CategoryCountLimit"]
			categories = snapshot["PlaylistCategoryCount"].most_common(
				None if not categoryCount else categoryCount
			)
			if scriptCount == 0:
				statusInfo.append(
					# Translators: one of the results for playlist snapshots feature
					# for announcing top track category in a playlist.
					_("Top category: {} ({})").format(categories[0][0], categories[0][1])
				)
			elif scriptCount == 1:
				categoryList = []
				# Translators: one of the results for playlist snapshots feature,
				# a heading for a group of items.
				header = _("Categories:")
				for item in categories:
					category, count = item
					category = category.replace("<", "")
					category = category.replace(">", "")
					# Translators: one of the results for playlist snapshots feature
					# for category count information.
					info = _("{categoryName} ({categoryCount})").format(
						categoryName=category, categoryCount=count
					)
					categoryList.append("<li>{}</li>".format(info))
				statusInfo.append("".join([header, "<ol>", "\n".join(categoryList), "</ol>"]))
		if "PlaylistGenreCount" in snapshot:
			genreCount = splconfig.SPLConfig["PlaylistSnapshots"]["GenreCountLimit"]
			genres = snapshot["PlaylistGenreCount"].most_common(None if not genreCount else genreCount)
			if scriptCount == 0:
				try:
					statusInfo.append(
						# Translators: one of the results for playlist snapshots feature
						# for announcing top genre in a playlist.
						_("Top genre: {} ({})").format(genres[0][0], genres[0][1])
					)
				except IndexError:
					statusInfo.append(
						# Translators: one of the results for playlist snapshots feature
						# when there is no top genre.
						_("Top genre: none")
					)
			elif scriptCount == 1:
				if len(genres) == 0:
					statusInfo.append(
						# Translators: one of the results for playlist snapshots feature
						# when there is no top genre (formatted for browse mode).
						_("Top genres: none")
					)
				else:
					genreList = []
					# Translators: one of the results for playlist snapshots feature,
					# a heading for a group of items.
					header = _("Top genres:")
					for item in genres:
						genre, count = item
						if genre is None:
							# Translators: one of the results for playlist snapshots feature
							# when there is no genre information for an item.
							info = _("No genre information ({genreCount})").format(genreCount=count)
						else:
							# Translators: one of the results for playlist snapshots feature
							# for genre count information.
							info = _("{genreName} ({genreCount})").format(genreName=genre, genreCount=count)
						genreList.append("<li>{}</li>".format(info))
					statusInfo.append("".join([header, "<ol>", "\n".join(genreList), "</ol>"]))
		if scriptCount == 0:
			ui.message(", ".join(statusInfo))
		else:
			# Translators: The title of a window for displaying playlist snapshots information.
			ui.browseableMessage(
				"<p>".join(statusInfo),
				title=_("Playlist snapshots"),
				isHtml=True,
				**browseableMessageButtons,
			)

	# Some handlers for native commands.

	@scriptHandler.script(gestures=["kb:Shift+delete", "kb:Shift+numpadDelete"])
	def script_deleteTrack(self, gesture):
		self.preTrackRemoval()
		gesture.send()

	# When Escape is pressed, activate background library scan if conditions are right.
	@scriptHandler.script(gesture="kb:escape")
	def script_escape(self, gesture):
		gesture.send()
		if self.libraryScanning:
			if not libScanT or (libScanT and not libScanT.is_alive()):
				self.monitorLibraryScan()

	# SPL Assistant: reports status on playback, operation, etc.
	# Used layer command approach to save gesture assignments.
	# Most were borrowed from JFW and Window-Eyes layer scripts (Window-Eyes command layout removed in 2020).

	# Set up the layer script environment.
	def getScript(self, gesture):
		if not self.SPLAssistant:
			return appModuleHandler.AppModule.getScript(self, gesture)
		script = appModuleHandler.AppModule.getScript(self, gesture)
		if not script:
			script = self.script_error
		return splbase.finally_(script, self.script_finish)

	@scriptHandler.script(speakOnDemand=True)
	def script_finish(self):
		self.SPLAssistant = False
		self.clearGestureBindings()
		self.bindGestures(self.__gestures)
		if self.cartExplorer:
			self.cartsBuilder()

	def script_error(self, gesture):
		tones.beep(120, 100)
		self.script_finish()

	# SPL Assistant flag.
	SPLAssistant = False

	# The SPL Assistant layer driver.

	@scriptHandler.script(
		description=_(
			# Translators: Input help mode message for a layer command in StationPlaylist add-on.
			"The SPL Assistant layer command. "
			"See the add-on guide for more information on available commands.",
		),
		speakOnDemand=True,
	)
	def script_SPLAssistantToggle(self, gesture):
		if scriptHandler.getLastScriptRepeatCount() > 0:
			gesture.send()
			self.script_finish()
			return
		# Don't bother if Studio main window handle isn't found (Studio is not fully running).
		if not splbase.studioIsRunning(justChecking=True):
			# Translators: Presented when SPL Assistant cannot be invoked.
			ui.message(_("Failed to locate Studio main window, cannot enter SPL Assistant"))
			return
		if self.SPLAssistant:
			self.script_error(gesture)
			return
		# To prevent entering wrong gesture while the layer is active.
		self.clearGestureBindings()
		# Choose the required compatibility layer.
		CompatibilityLayer = splconfig.SPLConfig["Advanced"]["CompatibilityLayer"]
		self.bindGestures(self.__SPLAssistantGestures[CompatibilityLayer])
		for i in range(5):
			self.bindGesture(f"kb:shift+{i}", "metadataEnabled")
		self.SPLAssistant = True
		tones.beep(512, 50)
		if CompatibilityLayer == "jfw":
			ui.message("JAWS")

	# Status table keys
	SPLPlayStatus = 0
	SPLSystemStatus = 1
	SPLNextTrackTitle = 3
	SPLNextPlayer = 4
	SPLCurrentTrackTitle = 5
	SPLCurrentPlayer = 6
	SPLTemperature = 7

	# Table of child constants based on versions
	# These are scattered throughout the screen, so one can use foreground.getChild(index) to fetch them
	# (getChild tip from Jamie Teh (NV Access/Mozilla)).
	# Because 6.x an possible future releases may use different screen layouts,
	# look up the needed constant from the table below
	# (row = info needed, column = version).
	# As of 2025, the below table is based on Studio 6.0.
	# #119: a list indicates iterative descent to locate the actual objects.
	statusObjs = {
		"6": {
			SPLPlayStatus: [-1, -3],  # Play status, mic, control keys (Studio 6.10 and later), etc.
			SPLSystemStatus: [-1, -2],  # The second status bar containing system status such as up time.
			SPLNextTrackTitle: [-1, 1, 2, 0],  # Name and duration of the next track if any.
			SPLNextPlayer: [-1, 1, 2, 1],  # Name and duration of the next track if any.
			SPLCurrentTrackTitle: [-1, 1, 9],  # Name of the currently playing track.
			SPLCurrentPlayer: [-1, 1, 9, 0],  # Name of the currently playing track.
			SPLTemperature: [-1, 1, 3, 0],  # Temperature for the current city.
		},
	}

	_cachedStatusObjs: dict[int, Any] = {}

	# Called in the layer commands requiring screen traversal.
	def status(self, infoIndex: int) -> NVDAObject:
		# Look up the cached objects first for faster response.
		if (
			infoIndex not in self._cachedStatusObjs
			# When Studio window size changes, location of some elements becomes undefined.
			or not any(self._cachedStatusObjs[infoIndex].location)
		):
			fg = api.getForegroundObject()
			if fg is not None and fg.windowClassName != "TStudioForm":
				# Allow gesture-based functions to look up status information even if Studio window isn't focused
				# (several SPL Controller commands will use this route).
				fg = getNVDAObjectFromEvent(user32.FindWindowW("TStudioForm", None), OBJID_CLIENT, 0)
			studioVersion = self.productVersion.split(".")[0]
			statusIndex = self.statusObjs[studioVersion][infoIndex]
			# Sometimes (especially when first loaded), OBJID_CLIENT fails,
			# so resort to retrieving focused object instead.
			if fg is not None and fg.childCount > 1:
				obj = fg
				# In most cases, first-level child object holds status information.
				if isinstance(statusIndex, int):
					obj = fg.getChild(statusIndex)
				# #119: for some status items, an object one level below info index must be fetched,
				# evidenced by different window handles.
				# For situations like this (a list of navigational child indecies), an iterative descent will be used.
				else:
					for child in statusIndex:
						obj = obj.getChild(child)
				self._cachedStatusObjs[infoIndex] = obj
			else:
				return api.getFocusObject()
		return self._cachedStatusObjs[infoIndex]

	def sayStatus(self, index: int) -> None:
		# No, status index must be an integer.
		studioStatus = splbase.studioAPI(index, SPLStatusInfo)
		if studioStatus is None:
			return
		status = splconsts.studioStatusMessages[index][studioStatus]
		if splconfig.SPLConfig["General"]["MessageVerbosity"] == "advanced":
			status = status.split()[-1]
		ui.message(status)

	# The layer commands themselves.

	def script_sayPlayStatus(self, gesture):
		self.sayStatus(0)

	def script_sayAutomationStatus(self, gesture):
		self.sayStatus(1)

	def script_sayMicStatus(self, gesture):
		self.sayStatus(2)

	def script_sayLineInStatus(self, gesture):
		self.sayStatus(3)

	def script_sayRecToFileStatus(self, gesture):
		self.sayStatus(4)

	def script_sayCartEditStatus(self, gesture):
		# Because cart edit status also shows cart insert status, verbosity control will not apply.
		cartEdit = splbase.studioAPI(5, SPLStatusInfo)
		cartInsert = splbase.studioAPI(6, SPLStatusInfo)
		if cartEdit:
			ui.message("Cart Edit On")
		elif not cartEdit and cartInsert:
			ui.message("Cart Insert On")
		else:
			ui.message("Cart Edit Off")

	def script_sayControlKeysStatus(self, gesture):
		# Properly shown in Studio 6.10 and later.
		if self.productVersion < "6.10":
			self.script_error(None)
			return
		obj = self.status(self.SPLPlayStatus).lastChild
		ui.message(obj.name)

	def script_sayHourTrackDuration(self, gesture):
		self.announceTime(splbase.studioAPI(0, SPLPlaylistHourDuration))

	def script_sayHourRemaining(self, gesture):
		self.announceTime(splbase.studioAPI(1, SPLPlaylistHourDuration))

	def script_sayPlaylistRemainingDuration(self, gesture):
		if self.canPerformPlaylistCommands() == self.SPLPlaylistNoErrors:
			obj = api.getFocusObject()
			if obj.role == controlTypes.Role.LIST:
				obj = obj.firstChild
			self.announceTime(self.playlistDuration(start=obj), ms=False)

	def script_sayHourOvertime(self, gesture):
		playlistOvertime = splbase.studioAPI(2, SPLPlaylistHourDuration)
		# Highly unlikely but None check is done to satisfy type checkers.
		if playlistOvertime is not None:
			overtimePrefix = "+" if playlistOvertime >= 0 else "-"
			ui.message("{}{}".format(
				overtimePrefix, self._ms2time(abs(playlistOvertime), includeHours=False)
			))

	def script_sayPlaylistModified(self, gesture):
		obj = self.status(self.SPLSystemStatus).getChild(5)
		# Translators: presented when playlist modification message isn't shown.
		ui.message(obj.name if obj.name else _("Playlist modification not available"))

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Announces title of the next track if any"),
		speakOnDemand=True,
	)
	def script_sayNextTrackTitle(self, gesture):
		if not splbase.studioIsRunning():
			self.script_finish()
			return
		try:
			if not splbase.studioAPI(0, SPLStatusInfo):
				# Message comes from Foobar 2000 app module, part of NVDA Core.
				nextTrack = translate("No track playing")
			else:
				obj = self.status(self.SPLNextTrackTitle)
				# Translators: Presented when there is no information for the next track.
				nextTrack = _("No next track scheduled") if obj.name is None else obj.name
			# #34: normally, player position (name of the internal player in Studio) would not be announced,
			# but might be useful for some broadcasters with mixers.
			if splconfig.SPLConfig["SayStatus"]["SayStudioPlayerPosition"]:
				player = self.status(self.SPLNextPlayer).name
				ui.message(", ".join([player, nextTrack]))
			else:
				ui.message(nextTrack)
		except RuntimeError:
			# Translators: Presented when next track information is unavailable.
			ui.message(_("Cannot find next track information"))
		finally:
			self.script_finish()

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Announces title of the currently playing track"),
		speakOnDemand=True,
	)
	def script_sayCurrentTrackTitle(self, gesture):
		if not splbase.studioIsRunning():
			self.script_finish()
			return
		try:
			if not splbase.studioAPI(0, SPLStatusInfo):
				# Message comes from Foobar 2000 app module, part of NVDA Core.
				currentTrack = translate("No track playing")
			else:
				obj = self.status(self.SPLCurrentTrackTitle)
				currentTrack = obj.name
				# Studio 6 does not define accessibility label for this item, so display text must be used.
				currentTrack = obj.displayText.partition(obj.firstChild.name)[-1]
			# #34: see the note on next track script above.
			if splconfig.SPLConfig["SayStatus"]["SayStudioPlayerPosition"]:
				player = self.status(self.SPLCurrentPlayer).name
				ui.message(", ".join([player, currentTrack]))
			else:
				ui.message(currentTrack)
		except RuntimeError:
			# Translators: Presented when current track information is unavailable.
			ui.message(_("Cannot find current track information"))
		finally:
			self.script_finish()

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Announces temperature and weather information"),
		speakOnDemand=True,
	)
	def script_sayTemperature(self, gesture):
		if not splbase.studioIsRunning():
			self.script_finish()
			return
		# Temperature object position is different between Studio 6.0x and 6.1x.
		# Therefore, manually change index traversal route whenever this script is run.
		if self.productVersion.startswith("6.1"):
			self.statusObjs["6"][self.SPLTemperature] = [-1, 1, 3, 1]
		try:
			obj = self.status(self.SPLTemperature)
			# Translators: Presented when there is no weather or temperature information.
			ui.message(obj.name if obj.name else _("Weather and temperature not configured"))
		except RuntimeError:
			# Translators: Presented when temperature information cannot be found.
			ui.message(_("Weather information not found"))
		finally:
			self.script_finish()

	def script_sayUpTime(self, gesture):
		obj = self.status(self.SPLSystemStatus).firstChild
		ui.message(obj.name)

	def script_sayScheduledTime(self, gesture):
		# Scheduled is the time originally specified in Studio,
		# scheduled to play is broadcast time based on current time.
		# Sometimes, hour markers return seconds.999 due to rounding error, hence this must be taken care of here.
		# #155: Studio API can return None if Studio dies.
		trackStarts = splbase.studioAPI(3, SPLPlaylistHourDuration)
		if trackStarts is None:
			return
		trackStarts = divmod(trackStarts, 1000)
		# For this method, all three components of time display (hour, minute, second) must be present.
		# In case it is midnight (0.0 but sometimes shown as 86399.999 due to rounding error), just say "midnight".
		if trackStarts in ((86399, 999), (0, 0)):
			ui.message("00:00:00")
		else:
			self.announceTime(trackStarts[0] + 1 if trackStarts[1] == 999 else trackStarts[0], ms=False)

	def script_sayScheduledToPlay(self, gesture):
		# This script announces length of time remaining until the selected track will play.
		# Hour announcement should not be used to match what's displayed on screen.
		self.announceTime(splbase.studioAPI(4, SPLPlaylistHourDuration), includeHours=False)

	def script_sayListenerCount(self, gesture):
		obj = self.status(self.SPLSystemStatus).getChild(3)
		# Translators: Presented when there is no listener count information.
		ui.message(obj.name if obj.name else _("Listener count not found"))

	def script_sayTrackPitch(self, gesture):
		obj = self.status(self.SPLSystemStatus).getChild(4)
		ui.message(obj.name)

	# Few toggle/misc scripts that may be excluded from the layer later.

	def script_libraryScanMonitor(self, gesture):
		if not self.libraryScanning:
			# #155: if library scan count is None, then final scan count would also be None.
			libScanCount = splbase.studioAPI(1, SPLLibraryScanCount)
			# Do nothing if library scan count is indeed None.
			if libScanCount is None:
				return
			if libScanCount < 0:
				ui.message(_("{itemCount} items in the library").format(
					itemCount=splbase.studioAPI(0, SPLLibraryScanCount)
				))
				return
			self.libraryScanning = True
			if not splconfig.SPLConfig["General"]["BeepAnnounce"]:
				# Translators: Presented when attempting to start library scan.
				ui.message(_("Monitoring library scan"))
			else:
				tones.beep(740, 100)
			self.monitorLibraryScan()
		else:
			# Translators: Presented when library scan is already in progress.
			ui.message(_("Scanning is in progress"))

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Marks focused track as start marker for various playlist analysis commands")
	)
	def script_markTrackForAnalysis(self, gesture):
		self.script_finish()
		if self._trackAnalysisAllowed():
			focus = api.getFocusObject()
			if scriptHandler.getLastScriptRepeatCount() == 0:
				self._analysisMarker = focus.IAccessibleChildID - 1
				# Translators: Presented when track time analysis is turned on.
				ui.message(_("Playlist analysis activated"))
			else:
				self._analysisMarker = None
				# Translators: Presented when track time analysis is turned off.
				ui.message(_("Playlist analysis deactivated"))

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Announces total length of tracks between analysis start marker and the current track"),
		speakOnDemand=True,
	)
	def script_trackTimeAnalysis(self, gesture):
		self.script_finish()
		if self._trackAnalysisAllowed():
			if self._analysisMarker is None:
				# Translators: Presented when track time analysis cannot be used because start marker is not set.
				ui.message(_("No track selected as start of analysis marker, cannot perform time analysis"))
				return
			focus = api.getFocusObject()
			trackPos = focus.IAccessibleChildID - 1
			analysisBegin = min(self._analysisMarker, trackPos)
			analysisEnd = max(self._analysisMarker, trackPos)
			analysisRange = analysisEnd - analysisBegin + 1
			totalLength = self.playlistDuration(
				start=focus.parent.getChild(analysisBegin), end=focus.parent.getChild(analysisEnd + 1)
			)
			# Playlist duration method returns raw seconds, so do not force milliseconds,
			# and in case of multiple tracks, multiply this by 1000.
			if analysisRange == 1:
				self.announceTime(totalLength, ms=False)
			else:
				ui.message(
					# Translators: Presented when time analysis is done for a number of tracks
					# (example output: Tracks: 3, totaling 5:00).
					_("Tracks: {numberOfSelectedTracks}, totaling {totalTime}").format(
						numberOfSelectedTracks=analysisRange, totalTime=self._ms2time(totalLength * 1000)
					)
				)

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Presents playlist snapshot information such as number of tracks and top artists"),
		speakOnDemand=True,
	)
	def script_takePlaylistSnapshots(self, gesture):
		if not splbase.studioIsRunning():
			self.script_finish()
			return
		if not self._trackAnalysisAllowed(mustSelectTrack=False):
			self.script_finish()
			return
		obj = api.getFocusObject()
		if obj.role == controlTypes.Role.LIST:
			obj = obj.firstChild
		scriptCount = scriptHandler.getLastScriptRepeatCount()
		# Display the decorated HTML window on the first press if told to do so.
		if splconfig.SPLConfig["PlaylistSnapshots"]["ShowResultsWindowOnFirstPress"]:
			scriptCount += 1
		# Never allow this to be invoked more than twice, as it causes
		# performance degredation and multiple HTML windows are opened.
		if scriptCount >= 2:
			self.script_finish()
			return
		# #55: partial playlist snapshots require start and end range.
		# Analysis marker is an integer, so locate the correct track.
		start = obj.parent.firstChild if self._analysisMarker is None else None
		end = None
		if self._analysisMarker is not None:
			trackPos = obj.IAccessibleChildID - 1
			analysisBegin = min(self._analysisMarker, trackPos)
			analysisEnd = max(self._analysisMarker, trackPos)
			start = obj.parent.getChild(analysisBegin)
			end = obj.parent.getChild(analysisEnd).next
		# Speak and braille on the first press, display a decorated HTML message for subsequent presses.
		self.playlistSnapshotOutput(self.playlistSnapshots(start, end), scriptCount)
		self.script_finish()

	def script_playlistTranscripts(self, gesture):
		if not splbase.studioIsRunning():
			self.script_finish()
			return
		if not self._trackAnalysisAllowed(mustSelectTrack=False):
			self.script_finish()
			return
		obj = api.getFocusObject()
		if obj.role == controlTypes.Role.LIST:
			obj = obj.firstChild
		try:
			d = splmisc.SPLPlaylistTranscriptsDialog(gui.mainFrame, obj)
			gui.mainFrame.prePopup()
			d.Raise()
			d.Show()
			gui.mainFrame.postPopup()
		except RuntimeError:
			wx.CallAfter(splmisc.plTranscriptsDialogError)
		self.script_finish()

	def script_switchProfiles(self, gesture):
		# #118: do not allow profile switching while add-on settings screen is shown.
		splconfui.instantProfileSwitchConfigUICheck()

	def script_setPlaceMarker(self, gesture):
		obj = api.getFocusObject()
		try:
			index = obj.indexOf("Filename")
		except AttributeError:
			# Translators: Presented when place marker cannot be set.
			ui.message(_("No tracks found, cannot set place marker"))
			return
		filename = obj._getColumnContentRaw(index)
		if filename:
			self.placeMarker = filename
			# Translators: Presented when place marker track is set.
			ui.message(_("place marker set"))
		else:
			# Translators: Presented when attempting to place a place marker on an unsupported track.
			ui.message(_("This track cannot be used as a place marker track"))

	def script_findPlaceMarker(self, gesture):
		# Place marker command will be restricted to playlist viewer in order to prevent focus bouncing.
		if self.canPerformPlaylistCommands() == self.SPLPlaylistNoErrors:
			# Guard against place marker filename becoming nothing.
			# #155: an extra check to make sure it is indeed a string.
			if self.placeMarker is not None and self.placeMarker != "":
				obj = api.getFocusObject().parent.firstChild
				track = self._trackLocator(self.placeMarker, obj=obj, columns=[obj.indexOf("Filename")])
				# Only do the following if a track is found.
				if track:
					track.doAction()
				else:
					# Bogus place marker, so nullify it.
					self.placeMarker = None
					ui.message(_("No place marker found"))
			else:
				# Nullify place marker if it holds incorrect data.
				self.placeMarker = None
				# Translators: Presented when no place marker is found.
				ui.message(_("No place marker found"))

	def script_metadataStreamingAnnouncer(self, gesture):
		ui.message(splmisc.metadataStatus())

	# Gesture(s) for the following script cannot be changed by users.
	def script_metadataEnabled(self, gesture):
		# 0 is DSP encoder status, others are servers.
		metadataStreams = ("DSP encoder", "URL 1", "URL 2", "URL 3", "URL 4")
		url = int(gesture.displayName[-1])
		if splbase.studioAPI(url, SPLMetadataStreaming):
			ui.message(
				# Translators: Status message for metadata streaming.
				_("Metadata streaming on {URLPosition} enabled").format(URLPosition=metadataStreams[url])
			)
		else:
			ui.message(
				# Translators: Status message for metadata streaming.
				_("Metadata streaming on {URLPosition} disabled").format(URLPosition=metadataStreams[url])
			)

	def script_layerHelp(self, gesture):
		layerHelpTitle = {
			# Translators: The title for SPL Assistant help screen.
			"off": _("SPL Assistant help"),
			# Translators: The title for SPL Assistant help screen.
			"jfw": _("SPL Assistant help for JAWS layout"),
		}
		compatibility = splconfig.SPLConfig["Advanced"]["CompatibilityLayer"]
		ui.browseableMessage(
			SPLAssistantHelp[compatibility],
			title=layerHelpTitle[compatibility],
			**browseableMessageButtons
		)

	__SPLAssistantGestures = {
		"off": {
			"kb:p": "sayPlayStatus",
			"kb:a": "sayAutomationStatus",
			"kb:m": "sayMicStatus",
			"kb:l": "sayLineInStatus",
			"kb:r": "sayRecToFileStatus",
			"kb:t": "sayCartEditStatus",
			"kb:control+d": "sayControlKeysStatus",
			"kb:h": "sayHourTrackDuration",
			"kb:shift+h": "sayHourRemaining",
			"kb:d": "sayPlaylistRemainingDuration",
			"kb:o": "sayHourOvertime",
			"kb:y": "sayPlaylistModified",
			"kb:u": "sayUpTime",
			"kb:n": "sayNextTrackTitle",
			"kb:c": "sayCurrentTrackTitle",
			"kb:w": "sayTemperature",
			"kb:i": "sayListenerCount",
			"kb:s": "sayScheduledTime",
			"kb:shift+s": "sayScheduledToPlay",
			"kb:shift+p": "sayTrackPitch",
			"kb:shift+r": "libraryScanMonitor",
			"kb:f8": "takePlaylistSnapshots",
			"kb:shift+f8": "playlistTranscripts",
			"kb:f9": "markTrackForAnalysis",
			"kb:f10": "trackTimeAnalysis",
			"kb:f12": "switchProfiles",
			"kb:f": "findTrack",
			"kb:Control+k": "setPlaceMarker",
			"kb:k": "findPlaceMarker",
			"kb:e": "metadataStreamingAnnouncer",
			"kb:f1": "layerHelp",
		},
		"jfw": {
			"kb:p": "sayPlayStatus",
			"kb:a": "sayAutomationStatus",
			"kb:m": "sayMicStatus",
			"kb:shift+l": "sayLineInStatus",
			"kb:shift+e": "sayRecToFileStatus",
			"kb:t": "sayCartEditStatus",
			"kb:control+d": "sayControlKeysStatus",
			"kb:h": "sayHourTrackDuration",
			"kb:shift+h": "sayHourRemaining",
			"kb:r": "sayPlaylistRemainingDuration",
			"kb:o": "sayHourOvertime",
			"kb:y": "sayPlaylistModified",
			"kb:u": "sayUpTime",
			"kb:n": "sayNextTrackTitle",
			"kb:shift+c": "sayCurrentTrackTitle",
			"kb:c": "toggleCartExplorer",
			"kb:w": "sayTemperature",
			"kb:l": "sayListenerCount",
			"kb:s": "sayScheduledTime",
			"kb:shift+s": "sayScheduledToPlay",
			"kb:shift+p": "sayTrackPitch",
			"kb:shift+r": "libraryScanMonitor",
			"kb:f8": "takePlaylistSnapshots",
			"kb:shift+f8": "playlistTranscripts",
			"kb:f9": "markTrackForAnalysis",
			"kb:f10": "trackTimeAnalysis",
			"kb:f12": "switchProfiles",
			"kb:f": "findTrack",
			"kb:Control+k": "setPlaceMarker",
			"kb:k": "findPlaceMarker",
			"kb:e": "metadataStreamingAnnouncer",
			"kb:f1": "layerHelp",
		}
	}
