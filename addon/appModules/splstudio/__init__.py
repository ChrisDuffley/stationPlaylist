# StationPlaylist Studio
# An app module and global plugin package for NVDA
# Copyright 2011, 2013-2016, Geoff Shang, Joseph Lee and others, released under GPL.
# The primary function of this appModule is to provide meaningful feedback to users of SplStudio
# by allowing speaking of items which cannot be easily found.
# Version 0.01 - 7 April 2011:
# Initial release: Jamie's focus hack plus auto-announcement of status items.
# Additional work done by Joseph Lee and other contributors.
# For SPL Studio Controller, focus movement, SAM Encoder support and other utilities, see the global plugin version of this app module.

# Minimum version: SPL 5.00, NvDA 2015.3.

from functools import wraps
import os
import time
import threading
import controlTypes
import appModuleHandler
import api
import review
import eventHandler
import scriptHandler
import queueHandler
import ui
import nvwave
import speech
import braille
import touchHandler
import gui
import wx
from winUser import user32, sendMessage, OBJID_CLIENT
from NVDAObjects import NVDAObject, NVDAObjectTextInfo
from NVDAObjects.IAccessible import IAccessible, getNVDAObjectFromEvent
from NVDAObjects.behaviors import Dialog
import textInfos
import tones
import splconfig
import splconfui
import splmisc
import splupdate
import addonHandler
addonHandler.initTranslation()


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

# Make sure the broadcaster is running a compatible version.
SPLMinVersion = "5.10"

# Cache the handle to main Studio window.
_SPLWin = None

# Threads pool.
micAlarmT = None
micAlarmT2 = None
libScanT = None

# Blacklisted versions of Studio where library scanning functionality is broken.
noLibScanMonitor = []

# Braille and play a sound in response to an alarm or an event.
def messageSound(wavFile, message):
	nvwave.playWaveFile(wavFile)
	braille.handler.message(message)

# A special version for microphone alarm (continuous or not).
def _micAlarmAnnouncer():
		if splconfig.SPLConfig["General"]["AlarmAnnounce"] in ("beep", "both"):
			nvwave.playWaveFile(os.path.join(os.path.dirname(__file__), "SPL_MicAlarm.wav"))
		if splconfig.SPLConfig["General"]["AlarmAnnounce"] in ("message", "both"):
			# Translators: Presented when microphone has been active for a while.
			ui.message(_("Microphone active"))

# Manage microphone alarm announcement.
def micAlarmManager(micAlarmWav, micAlarmMessage):
	messageSound(micAlarmWav, micAlarmMessage)
	# Play an alarm sound (courtesy of Jerry Mader from Mader Radio).
	global micAlarmT2
	# Use a timer to play a tone when microphone was active for more than the specified amount.
	# Mechanics come from Clock add-on.
	if splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarmInterval"]:
		micAlarmT2 = wx.PyTimer(_micAlarmAnnouncer)
		micAlarmT2.Start(splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarmInterval"] * 1000)

# Call SPL API to obtain needed values.
# A thin wrapper around user32.SendMessage and calling a callback if defined.
# Offset is used in some time commands.
def statusAPI(arg, command, func=None, ret=False, offset=None):
	if _SPLWin is None: return
	val = sendMessage(_SPLWin, 1024, arg, command)
	if ret:
		return val
	if func:
		func(val) if not offset else func(val, offset)

# Select a track upon request.
def selectTrack(trackIndex):
	statusAPI(-1, 121)
	statusAPI(trackIndex, 121)

# Category sounds dictionary (key = category, value = tone pitch).
_SPLCategoryTones = {
	"Break Note":415,
	"Timed Break Note":208,
	"<Manual Intro>":600,
}

# Routines for track items themselves (prepare for future work).
class SPLTrackItem(IAccessible):
	"""A base class for providing utility scripts when track entries are focused, such as track dial."""

	def initOverlayClass(self):
		#if splconfig.SPLConfig["General"]["TrackDial"]:
			#self.bindGesture("kb:rightArrow", "nextColumn")
			#self.bindGesture("kb:leftArrow", "prevColumn")
		# LTS: Take a greater role in assigning enhanced Columns Explorer command at the expense of limiting where this can be invoked.
		# 8.0: Just assign number row.
		for i in xrange(10):
			self.bindGesture("kb:control+nvda+%s"%(i), "columnExplorer")

	# Locate the real column index for a column header.
	# This is response to a situation where columns were rearranged yet testing shows in-memory arrangement remains the same.
	# Subclasses must provide this function.
	def _origIndexOf(self, columnHeader):
		return splconfig._SPLDefaults7["General"]["ExploreColumns"].index(columnHeader)

	# Read selected columns.
	# But first, find where the requested column lives.
	# 8.0: Make this a public function.
	def indexOf(self, columnHeader):
		# Handle both 5.0x and 5.10 column headers.
		try:
			return self._origIndexOf(columnHeader)
		except ValueError:
			return None

	def reportFocus(self):
		# 7.0: Cache column header data structures if meeting track items for the first time.
		# It is better to do it while reporting focus, otherwise Python throws recursion limit exceeded error when initOverlayClass does this.
		if self.appModule._columnHeaders is None:
			self.appModule._columnHeaders = self.parent.children[-1]
		# 7.0: Also cache column header names to improve performance (may need to check for header repositioning later).
		if self.appModule._columnHeaderNames is None:
			self.appModule._columnHeaderNames = [header.name for header in self.appModule._columnHeaders.children]
		if splconfig.SPLConfig["General"]["CategorySounds"]:
			category = self._getColumnContent(self.indexOf("Category"))
			if category in _SPLCategoryTones:
				tones.beep(_SPLCategoryTones[category], 50)
		# LTS: Comments please.
		if splconfig.SPLConfig["General"]["TrackCommentAnnounce"] != "off":
			self.announceTrackComment(0)
		# 6.3: Catch an unusual case where screen order is off yet column order is same as screen order and NvDA is told to announce all columns.
		# 17.1: Even if vertical column commands are performed, build description pieces for consistency.
		if splconfig._shouldBuildDescriptionPieces():
			descriptionPieces = []
			for header in splconfig.SPLConfig["ColumnAnnouncement"]["ColumnOrder"]:
				if header in splconfig.SPLConfig["ColumnAnnouncement"]["IncludedColumns"]:
					index = self.indexOf(header)
					if index is None: continue # Header not found, mostly encountered in Studio 5.0x.
					content = self._getColumnContent(index)
					if content:
						descriptionPieces.append("%s: %s"%(header, content))
			self.description = ", ".join(descriptionPieces)
		if self.appModule._announceColumnOnly is None:
			super(IAccessible, self).reportFocus()
		else:
			self.appModule._announceColumnOnly = None
			verticalColumnAnnounce = splconfig.SPLConfig["General"]["VerticalColumnAnnounce"]
			if verticalColumnAnnounce == "Status" or (verticalColumnAnnounce is None and self.appModule.SPLColNumber == 0):
				self._leftmostcol()
			else:
				self.announceColumnContent(self.appModule.SPLColNumber if verticalColumnAnnounce is None else self.indexOf(verticalColumnAnnounce), header=verticalColumnAnnounce, reportStatus=self.name is not None)
		# 7.0: Let the app module keep a reference to this track.
		self.appModule._focusedTrack = self

	# Track Dial: using arrow keys to move through columns.
	# This is similar to enhanced arrow keys in other screen readers.

	def script_toggleTrackDial(self, gesture):
		#if not splconfig.SPLConfig["General"]["TrackDial"]:
			#splconfig.SPLConfig["General"]["TrackDial"] = True
			#self.bindGesture("kb:rightArrow", "nextColumn")
			#self.bindGesture("kb:leftArrow", "prevColumn")
			# Translators: Reported when track dial is on.
			#dialText = _("Track Dial on")
			#if self.appModule.SPLColNumber > 0:
				# Translators: Announced when located on a column other than the leftmost column while using track dial.
				#dialText+= _(", located at column {columnHeader}").format(columnHeader = self.appModule.SPLColNumber+1)
			#dialTone = 780
		#else:
			#splconfig.SPLConfig["General"]["TrackDial"] = False
			#try:
				#self.removeGestureBinding("kb:rightArrow")
				#self.removeGestureBinding("kb:leftArrow")
			#except KeyError:
				#pass
			# Translators: Reported when track dial is off.
			#dialText = _("Track Dial off")
			#dialTone = 390
		#if not splconfig.SPLConfig["General"]["BeepAnnounce"]:
			#ui.message(dialText)
		#else:
			#tones.beep(dialTone, 100)
			#braille.handler.message(dialText)
			#if splconfig.SPLConfig["General"]["TrackDial"] and self.appModule.SPLColNumber > 0:
				# Translators: Spoken when enabling track dial while status message is set to beeps.
				#speech.speakMessage(_("Column {columnNumber}").format(columnNumber = self.appModule.SPLColNumber+1))
		ui.message("Track Dial is deprecated in 2017, please unassign Track Dial toggle command via Input Gestures dialog")
	# Translators: Input help mode message for SPL track item.
	script_toggleTrackDial.__doc__=_("Toggles track dial on and off.")
	script_toggleTrackDial.category = _("StationPlaylist Studio")

	# Some helper functions to handle corner cases.
	# Each track item provides its own version.
	def _leftmostcol(self):
		if self.appModule._columnHeaders is None:
			self.appModule._columnHeaders = self.parent.children[-1]
		leftmost = self.appModule._columnHeaders.firstChild.name
		if not self.name or self.name == "":
			# Translators: Announced when leftmost column has no text while track dial is active.
			ui.message(_("{leftmostColumn} not found").format(leftmostColumn = leftmost))
		else:
			# Translators: Standard message for announcing column content.
			ui.message(_("{leftmostColumn}: {leftmostContent}").format(leftmostColumn = leftmost, leftmostContent = self.name))

	# Locate column content.
	# This is merely the proxy of the module level function defined in the misc module.
	def _getColumnContent(self, col):
		return splmisc._getColumnContent(self, col)

	# Announce column content if any.
	# 7.0: Add an optional header in order to announce correct header information in columns explorer.
	# 17.1: Allow checked status in 5.1x and later to be announced if this is such a case (vertical column navigation).)
	def announceColumnContent(self, colNumber, header=None, reportStatus=False):
		columnHeader = header if header is not None else self.appModule._columnHeaderNames[colNumber]
		columnContent = self._getColumnContent(self.indexOf(columnHeader))
		status = self.name + " " if reportStatus else ""
		if columnContent:
			# Translators: Standard message for announcing column content.
			ui.message(unicode(_("{checkStatus}{header}: {content}")).format(checkStatus = status, header = columnHeader, content = columnContent))
		else:
			# Translators: Spoken when column content is blank.
			speech.speakMessage(_("{checkStatus}{header}: blank").format(checkStatus = status, header = columnHeader))
			# Translators: Brailled to indicate empty column content.
			braille.handler.message(_("{checkStatus}{header}: ()").format(checkStatus = status, header = columnHeader))

	# Now the scripts.

	def script_nextColumn(self, gesture):
		if (self.appModule.SPLColNumber+1) == self.appModule._columnHeaders.childCount:
			tones.beep(2000, 100)
		else:
			self.appModule.SPLColNumber +=1
		self.announceColumnContent(self.appModule.SPLColNumber)

	def script_prevColumn(self, gesture):
		if self.appModule.SPLColNumber <= 0:
			tones.beep(2000, 100)
		else:
			self.appModule.SPLColNumber -=1
		if self.appModule.SPLColNumber == 0:
			self._leftmostcol()
		else:
			self.announceColumnContent(self.appModule.SPLColNumber)

	def script_firstColumn(self, gesture):
		self.appModule.SPLColNumber = 0
		self._leftmostcol()

	def script_lastColumn(self, gesture):
		self.appModule.SPLColNumber = self.appModule._columnHeaders.childCount-1
		self.announceColumnContent(self.appModule.SPLColNumber)

	# Track movement scripts.
	# Detects top/bottom of a playlist if told to do so.

	def script_nextTrack(self, gesture):
		gesture.send()
		if self.IAccessibleChildID == self.parent.childCount-1 and splconfig.SPLConfig["General"]["TopBottomAnnounce"]:
			tones.beep(2000, 100)

	def script_prevTrack(self, gesture):
		gesture.send()
		if self.IAccessibleChildID == 1 and splconfig.SPLConfig["General"]["TopBottomAnnounce"]:
			tones.beep(2000, 100)

	# Vertical column navigation.

	def script_nextRowColumn(self, gesture):
		newTrack = self.next
		if newTrack is None and splconfig.SPLConfig["General"]["TopBottomAnnounce"]:
			tones.beep(2000, 100)
		else:
			self.appModule._announceColumnOnly = True
			newTrack.setFocus(), newTrack.setFocus()
			selectTrack(newTrack.IAccessibleChildID-1)

	def script_prevRowColumn(self, gesture):
		newTrack = self.previous
		if newTrack is None and splconfig.SPLConfig["General"]["TopBottomAnnounce"]:
			tones.beep(2000, 100)
		else:
			self.appModule._announceColumnOnly = True
			newTrack.setFocus(), newTrack.setFocus()
			selectTrack(newTrack.IAccessibleChildID-1)

			# Overlay class version of Columns Explorer.

	def script_columnExplorer(self, gesture):
		# LTS: Just in case Control+NVDA+number row command is pressed...
		# Due to the below formula, columns explorer will be restricted to number commands.
		columnPos = int(gesture.displayName.split("+")[-1])-1
		header = splconfig.SPLConfig["General"]["ExploreColumns"][columnPos]
		column = self.indexOf(header)
		if column is not None:
			self.announceColumnContent(column, header=header)
		else:
			# Translators: Presented when a specific column header is not found.
			ui.message(_("{headerText} not found").format(headerText = header))

# Track comments.

	# Track comment announcer.
	# Levels indicate what should be done.
	# 0 indicates reportFocus, subsequent levels indicate script repeat count+1.
	def announceTrackComment(self, level):
		filename = self._getColumnContent(self.indexOf("Filename"))
		if filename is not None and filename in splconfig.trackComments:
			if level == 0:
				if splconfig.SPLConfig["General"]["TrackCommentAnnounce"] in ("message", "both"):
					ui.message(_("Has comment"))
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
				# Translators: Presented when there is no track comment for the focused track.
				ui.message(_("No comment"))
			elif level >= 3:
				if filename is not None:
					self._trackCommentsEntry(filename, "")
				else:
					# Translators: Presented when focused on a track other than an actual track (such as hour marker).
					ui.message(_("Comments cannot be added to this kind of track"))

	# A proxy function to call the track comments entry dialog.
	def _trackCommentsEntry(self, filename, comment):
		dlg = wx.TextEntryDialog(gui.mainFrame,
		_("Track comment"),
		# Translators: The title of the track comments dialog.
		_("Track comment"), defaultValue=comment)
		def callback(result):
			if result == wx.ID_OK:
				if dlg.GetValue() is None: return
				elif dlg.GetValue() == "": del splconfig.trackComments[filename]
				else: splconfig.trackComments[filename] = dlg.GetValue()
		gui.runScriptModalDialog(dlg, callback)

	def script_announceTrackComment(self, gesture):
		self.announceTrackComment(scriptHandler.getLastScriptRepeatCount()+1)
	# Translators: Input help message for track comment announcemnet command in SPL Studio.
	script_announceTrackComment.__doc__ = _("Announces track comment if any. Press twice to copy this information to the clipboard, and press three times to open a dialog to add, change or remove track comments")

	__gestures={
		"kb:control+alt+rightArrow":"nextColumn",
		"kb:control+alt+leftArrow":"prevColumn",
		"kb:control+alt+downArrow":"nextRowColumn",
		"kb:control+alt+upArrow":"prevRowColumn",
		"kb:control+alt+home":"firstColumn",
		"kb:control+alt+end":"lastColumn",
		"kb:downArrow":"nextTrack",
		"kb:upArrow":"prevTrack",
		"kb:Alt+NVDA+C":"announceTrackComment"
	}

class SPL510TrackItem(SPLTrackItem):
	"""Track item for Studio 5.10 and later."""

	def event_stateChange(self):
		# Why is it that NVDA keeps announcing "not selected" when track items are scrolled?
		if controlTypes.STATE_SELECTED not in self.states:
			pass

	def script_select(self, gesture):
		gesture.send()
		speech.speakMessage(self.name)
		braille.handler.handleUpdate(self)

	# Studio 5.10 version of original index finder.
	def _origIndexOf(self, columnHeader):
		return splconfig._SPLDefaults7["ColumnAnnouncement"]["ColumnOrder"].index(columnHeader)+1

	# Handle track dial for SPL 5.10.
	def _leftmostcol(self):
		if not self.name:
			# Translators: Presented when no track status is found in Studio 5.10.
			ui.message(_("Status not found"))
		else:
			# Translators: Status information for a checked track in Studio 5.10.
			ui.message(_("Status: {name}").format(name = self.name))

	__gestures={"kb:space":"select"}

SPLAssistantHelp={
	# Translators: The text of the help command in SPL Assistant layer.
	"off":_("""After entering SPL Assistant, press:
A: Automation.
C: Announce name of the currently playing track.
D: Remaining time for the playlist.
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
1 through 0 (6 for Studio 5.01 and earlier): Announce columns via Columns Explorer (0 is tenth column slot).
F9: Mark current track as start of track time analysis.
F10: Perform track time analysis.
F12: Switch to an instant switch profile.
Shift+F1: Open online user guide."""),
# Translators: The text of the help command in SPL Assistant layer when JFW layer is active.
	"jfw":_("""After entering SPL Assistant, press:
A: Automation.
C: Toggle cart explorer.
Shift+C: Announce name of the currently playing track.
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
1 through 0 (6 for Studio 5.01 and earlier): Announce columns via Columns Explorer (0 is tenth column slot).
F9: Mark current track as start of track time analysis.
F10: Perform track time analysis.
F12: Switch to an instant switch profile.
Shift+F1: Open online user guide."""),
# Translators: The text of the help command in SPL Assistant layer when Window-Eyes layer is active.
	"wineyes":_("""After entering SPL Assistant, press:
A: Automation.
C: Toggle cart explorer.
Shift+C: Announce name of the currently playing track.
D: Remaining time for the playlist.
E: Elapsed time.
F: Track finder.
R: Remaining time for the currently playing track.
G: Overall metadata streaming status.
Shift+1 through shift+4, shift+0: Metadata streaming status for DSP encoder and four additional URL's.
H: Duration of trakcs in this hour slot.
Shift+H: Duration of remaining trakcs in this hour slot.
K: Move to place marker track.
Control+K: Set place marker track.
L: Listener count.
Shift+L: Line-in status.
M: Microphone status.
N: Next track.
P: Playback status.
Shift+P: Pitch for the current track.
Shift+E: Record to file.
Shift+R: Monitor library scan.
S: Scheduled time for the track.
Shift+S: Time until the selected track will play.
T: Cart edit/insert mode.
U: Studio up time.
W: Weather and temperature.
Y: Playlist modification.
1 through 0 (6 for Studio 5.01 and earlier): Announce columns via Columns Explorer (0 is tenth column slot).
F9: Mark current track as start of track time analysis.
F10: Perform track time analysis.
F12: Switch to an instant switch profile.
Shift+F1: Open online user guide.""")}

# Provide a way to fetch dialog description in reverse order.
# This is used in Studio's About dialog as children are in reverse tab order somehow.
class ReversedDialog(Dialog):
	"""Overrides the description property to obtain dialog text except in reverse order.
	This is employed in Studio's help/About dialog.
	"""

	@classmethod
	def getDialogText(cls,obj,allowFocusedDescendants=True):
		"""This classmethod walks through the children of the given object, and collects up and returns any text that seems to be  part of a dialog's message text.
		@param obj: the object who's children you want to collect the text from
		@type obj: L{IAccessible}
		@param allowFocusedDescendants: if false no text will be returned at all if one of the descendants is focused.
		@type allowFocusedDescendants: boolean
		"""
		children=obj.children
		textList=[]
		childCount=len(children)
		# For these dialogs, children are arranged in reverse tab order (very strange indeed).
		for index in xrange(childCount-1, -1, -1):
			child=children[index]
			childStates=child.states
			childRole=child.role
			#We don't want to handle invisible or unavailable objects
			if controlTypes.STATE_INVISIBLE in childStates or controlTypes.STATE_UNAVAILABLE in childStates:
				continue
			#For particular objects, we want to descend in to them and get their children's message text
			if childRole in (controlTypes.ROLE_PROPERTYPAGE,controlTypes.ROLE_PANE,controlTypes.ROLE_PANEL,controlTypes.ROLE_WINDOW,controlTypes.ROLE_GROUPING,controlTypes.ROLE_PARAGRAPH,controlTypes.ROLE_SECTION,controlTypes.ROLE_TEXTFRAME,controlTypes.ROLE_UNKNOWN):
				#Grab text from descendants, but not for a child which inherits from Dialog and has focusable descendants
				#Stops double reporting when focus is in a property page in a dialog
				childText=cls.getDialogText(child,not isinstance(child,Dialog))
				if childText:
					textList.append(childText)
				elif childText is None:
					return None
				continue
			#If the child is focused  we should just stop and return None
			if not allowFocusedDescendants and controlTypes.STATE_FOCUSED in child.states:
				return None
			# We only want text from certain controls.
			if not (
				 # Static text, labels and links
				 childRole in (controlTypes.ROLE_STATICTEXT,controlTypes.ROLE_LABEL,controlTypes.ROLE_LINK)
				# Read-only, non-multiline edit fields
				or (childRole==controlTypes.ROLE_EDITABLETEXT and controlTypes.STATE_READONLY in childStates and controlTypes.STATE_MULTILINE not in childStates)
			):
				continue
			#We should ignore a text object directly after a grouping object, as it's probably the grouping's description
			if index>0 and children[index-1].role==controlTypes.ROLE_GROUPING:
				continue
			#Like the last one, but a graphic might be before the grouping's description
			if index>1 and children[index-1].role==controlTypes.ROLE_GRAPHIC and children[index-2].role==controlTypes.ROLE_GROUPING:
				continue
			childName=child.name
			if childName and index<(childCount-1) and children[index+1].role not in (controlTypes.ROLE_GRAPHIC,controlTypes.ROLE_STATICTEXT,controlTypes.ROLE_SEPARATOR,controlTypes.ROLE_WINDOW,controlTypes.ROLE_PANE,controlTypes.ROLE_BUTTON) and children[index+1].name==childName:
				# This is almost certainly the label for the next object, so skip it.
				continue
			isNameIncluded=child.TextInfo is NVDAObjectTextInfo or childRole in (controlTypes.ROLE_LABEL,controlTypes.ROLE_STATICTEXT)
			childText=child.makeTextInfo(textInfos.POSITION_ALL).text
			if not childText or childText.isspace() and child.TextInfo is not NVDAObjectTextInfo:
				childText=child.basicText
				isNameIncluded=True
			if not isNameIncluded:
				# The label isn't in the text, so explicitly include it first.
				if childName:
					textList.append(childName)
			if childText:
				textList.append(childText)
		return "\n".join(textList)


class AppModule(appModuleHandler.AppModule):

	# Translators: Script category for Station Playlist commands in input gestures dialog.
	scriptCategory = _("StationPlaylist Studio")
	SPLCurVersion = appModuleHandler.AppModule.productVersion
	_columnHeaders = None
	_columnHeaderNames = None
	_focusedTrack = None
	_announceColumnOnly = None # Used only if vertical column navigation commands are used.

	# Prepare the settings dialog among other things.
	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		if self.SPLCurVersion < SPLMinVersion:
			raise RuntimeError("Unsupported version of Studio is running, exiting app module")
		# Translators: The sign-on message for Studio app module.
		try:
			ui.message(_("Using SPL Studio version {SPLVersion}").format(SPLVersion = self.SPLCurVersion))
		except IOError, AttributeError:
			pass
		splconfig.initConfig()
		# Announce status changes while using other programs.
		# This requires NVDA core support and will be available in 6.0 and later (cannot be ported to earlier versions).
		# For now, handle all background events, but in the end, make this configurable.
		if hasattr(eventHandler, "requestEvents"):
			eventHandler.requestEvents(eventName="nameChange", processId=self.processID, windowClassName="TStatusBar")
			eventHandler.requestEvents(eventName="nameChange", processId=self.processID, windowClassName="TStaticText")
			self.backgroundStatusMonitor = True
		else:
			self.backgroundStatusMonitor = False
		self.prefsMenu = gui.mainFrame.sysTrayIcon.preferencesMenu
		self.SPLSettings = self.prefsMenu.Append(wx.ID_ANY, _("SPL Studio Settings..."), _("SPL settings"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, splconfui.onConfigDialog, self.SPLSettings)
		# Let me know the Studio window handle.
		# 6.1: Do not allow this thread to run forever (seen when evaluation times out and the app module starts).
		self.noMoreHandle = threading.Event()
		threading.Thread(target=self._locateSPLHwnd).start()
		# Check for add-on update if told to do so.
		# LTS: Only do this if channel hasn't changed.
		if splconfig.SPLConfig["Update"]["AutoUpdateCheck"] or splupdate._updateNow:
			# 7.0: Have a timer call the update function indirectly.
			queueHandler.queueFunction(queueHandler.eventQueue, splconfig.updateInit)
		# Display startup dialogs if any.
		wx.CallAfter(splconfig.showStartupDialogs)

	# Locate the handle for main window for caching purposes.
	def _locateSPLHwnd(self):
		hwnd = user32.FindWindowA("SPLStudio", None)
		while not hwnd:
			time.sleep(1)
			# If the demo copy expires and the app module begins, this loop will spin forever.
			# Make sure this loop catches this case.
			if self.noMoreHandle.isSet():
				self.noMoreHandle.clear()
				self.noMoreHandle = None
				return
			hwnd = user32.FindWindowA("SPLStudio", None)
		# Only this thread will have privilege of notifying handle's existence.
		with threading.Lock() as hwndNotifier:
			global _SPLWin
			_SPLWin = hwnd
		# Remind me to broadcast metadata information.
		if splconfig.SPLConfig["General"]["MetadataReminder"] == "startup":
			self._metadataAnnouncer(reminder=True)

	# Let the global plugin know if SPLController passthrough is allowed.
	def SPLConPassthrough(self):
		return splconfig.SPLConfig["Advanced"]["SPLConPassthrough"]

	def event_NVDAObject_init(self, obj):
		# From 0.01: previously focused item fires focus event when it shouldn't.
		if obj.windowClassName == "TListView" and obj.role in (controlTypes.ROLE_CHECKBOX, controlTypes.ROLE_LISTITEM) and controlTypes.STATE_FOCUSED not in obj.states:
			obj.shouldAllowIAccessibleFocusEvent = False
		# Radio button group names are not recognized as grouping, so work around this.
		elif obj.windowClassName == "TRadioGroup":
			obj.role = controlTypes.ROLE_GROUPING
		# In certain edit fields and combo boxes, the field name is written to the screen, and there's no way to fetch the object for this text. Thus use review position text.
		elif obj.windowClassName in ("TEdit", "TComboBox") and not obj.name:
			fieldName, fieldObj  = review.getScreenPosition(obj)
			fieldName.expand(textInfos.UNIT_LINE)
			if obj.windowClassName == "TComboBox":
				obj.name = fieldName.text.replace(obj.windowText, "")
			else:
				obj.name = fieldName.text

	# Some controls which needs special routines.
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		role = obj.role
		windowStyle = obj.windowStyle
		if obj.windowClassName == "TTntListView.UnicodeClass" and role == controlTypes.ROLE_LISTITEM and abs(windowStyle - 1443991625)%0x100000 == 0:
			clsList.insert(0, SPL510TrackItem)
		# 7.2: Recognize known dialogs.
		elif obj.windowClassName in ("TDemoRegForm", "TOpenPlaylist"):
			clsList.insert(0, Dialog)
		# For About dialog in Studio 5.1x and later.
		elif obj.windowClassName == "TAboutForm" and self.SPLCurVersion >= "5.1":
			clsList.insert(0, ReversedDialog)

	# Keep an eye on library scans in insert tracks window.
	libraryScanning = False
	scanCount = 0
	# For 5.0X and earlier: prevent NVDA from announcing scheduled time multiple times.
	scheduledTimeCache = ""
	# Track Dial (A.K.A. enhanced arrow keys)
	SPLColNumber = 0

	# Automatically announce mic, line in, etc changes
	# These items are static text items whose name changes.
	# Note: There are two status bars, hence the need to exclude Up time so it doesn't announce every minute.
	# Unfortunately, Window handles and WindowControlIDs seem to change, so can't be used.
	# Only announce changes if told to do so via the following function.
	def _TStatusBarChanged(self, obj):
		name = obj.name
		if name.startswith("  Up time:"):
			return False
		elif name.startswith("Scheduled for"):
			if self.scheduledTimeCache == name: return False
			self.scheduledTimeCache = name
			return splconfig.SPLConfig["SayStatus"]["SayScheduledFor"]
		elif "Listener" in name:
			return splconfig.SPLConfig["SayStatus"]["SayListenerCount"]
		elif name.startswith("Cart") and obj.IAccessibleChildID == 3:
			return splconfig.SPLConfig["SayStatus"]["SayPlayingCartName"]
		return True

	# Now the actual event.
	def event_nameChange(self, obj, nextHandler):
		# Do not let NvDA get name for None object when SPL window is maximized.
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
						self.scanCount+=1
						if self.scanCount%100 == 0:
							self._libraryScanAnnouncer(obj.name[1:obj.name.find("]")], splconfig.SPLConfig["General"]["LibraryScanAnnounce"])
					if not self.libraryScanning:
						if self.productVersion not in noLibScanMonitor:
							if not self.backgroundStatusMonitor: self.libraryScanning = True
				elif "match" in obj.name:
					if splconfig.SPLConfig["General"]["LibraryScanAnnounce"] != "off" and self.libraryScanning:
						if splconfig.SPLConfig["General"]["BeepAnnounce"]: tones.beep(370, 100)
						else:
							# Translators: Presented when library scan is complete.
							ui.message(_("Scan complete with {scanCount} items").format(scanCount = obj.name.split()[3]))
					if self.libraryScanning: self.libraryScanning = False
					self.scanCount = 0
			else:
				if obj.name.endswith((" On", " Off")):
					self._toggleMessage(obj.name)
				else:
					ui.message(obj.name)
				if self.cartExplorer or int(splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarm"]):
					# Activate mic alarm or announce when cart explorer is active.
					self.doExtraAction(obj.name)
		# Monitor the end of track and song intro time and announce it.
		elif obj.windowClassName == "TStaticText": # For future extensions.
			if obj.simplePrevious is not None:
				if obj.simplePrevious.name == "Remaining Time":
					# End of track for SPL 5.x.
					if splconfig.SPLConfig["General"]["BrailleTimer"] in ("outro", "both") and api.getForegroundObject().processID == self.processID:
						braille.handler.message(obj.name)
					if (obj.name == "00:{0:02d}".format(splconfig.SPLConfig["IntroOutroAlarms"]["EndOfTrackTime"])
					and splconfig.SPLConfig["IntroOutroAlarms"]["SayEndOfTrack"]):
						self.alarmAnnounce(obj.name, 440, 200)
				elif obj.simplePrevious.name == "Remaining Song Ramp":
					# Song intro for SPL 5.x.
					if splconfig.SPLConfig["General"]["BrailleTimer"] in ("intro", "both") and api.getForegroundObject().processID == self.processID:
						braille.handler.message(obj.name)
					if (obj.name == "00:{0:02d}".format(splconfig.SPLConfig["IntroOutroAlarms"]["SongRampTime"])
					and splconfig.SPLConfig["IntroOutroAlarms"]["SaySongRamp"]):
						self.alarmAnnounce(obj.name, 512, 400, intro=True)
				# Hack: auto scroll in Studio itself might be broken (according to Brian Hartgen), so force NVDA to announce currently playing track automatically if told to do so.
				try:
					if obj == self.status(self.SPLCurrentTrackTitle).firstChild.firstChild:
						if ((splconfig.SPLConfig["SayStatus"]["SayPlayingTrackName"] == "auto" and self.SPLCurVersion < "5.11")
						or (splconfig.SPLConfig["SayStatus"]["SayPlayingTrackName"] == "background" and api.getForegroundObject().windowClassName != "TStudioForm")):
							ui.message(obj.name)
				except AttributeError:
					pass
		nextHandler()

	# JL's additions

	# Handle toggle messages.
	def _toggleMessage(self, msg):
		if splconfig.SPLConfig["General"]["MessageVerbosity"] != "beginner":
			msg = msg.split()[-1]
		if splconfig.SPLConfig["General"]["BeepAnnounce"]:
			# User wishes to hear beeps instead of words. The beeps are power on and off sounds from PAC Mate Omni.
			if msg.endswith("Off"):
				if splconfig.SPLConfig["General"]["MessageVerbosity"] == "beginner":
					wavFile = os.path.join(os.path.dirname(__file__), "SPL_off.wav")
					try:
						messageSound(wavFile, msg)
					except:
						pass
				else:
					tones.beep(500, 100)
					braille.handler.message(msg)
			elif msg.endswith("On"):
				if splconfig.SPLConfig["General"]["MessageVerbosity"] == "beginner":
					wavFile = os.path.join(os.path.dirname(__file__), "SPL_on.wav")
					try:
						messageSound(wavFile, msg)
					except:
						pass
				else:
					tones.beep(1000, 100)
					braille.handler.message(msg)
		else:
			ui.message(msg)

	# Perform extra action in specific situations (mic alarm, for example).
	def doExtraAction(self, status):
		micAlarm = splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarm"]
		if self.cartExplorer:
			if status == "Cart Edit On":
				# Translators: Presented when cart edit mode is toggled on while cart explorer is on.
				ui.message(_("Cart explorer is active"))
			elif status == "Cart Edit Off":
				# Translators: Presented when cart edit mode is toggled off while cart explorer is on.
				ui.message(_("Please reenter cart explorer to view updated cart assignments"))
		if micAlarm:
			# Play an alarm sound (courtesy of Jerry Mader from Mader Radio).
			global micAlarmT, micAlarmT2
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
				if micAlarmT is not None: micAlarmT.cancel()
				micAlarmT = None
				if micAlarmT2 is not None: micAlarmT2.Stop()
				micAlarmT2 = None

	# Alarm announcement: Alarm notification via beeps, speech or both.
	def alarmAnnounce(self, timeText, tone, duration, intro=False):
		if splconfig.SPLConfig["General"]["AlarmAnnounce"] in ("beep", "both"):
			tones.beep(tone, duration)
		if splconfig.SPLConfig["General"]["AlarmAnnounce"] in ("message", "both"):
			alarmTime = int(timeText.split(":")[1])
			if intro:
				# Translators: Presented when end of introduction is approaching (example output: 5 sec left in track introduction).
				ui.message(_("Warning: {seconds} sec left in track introduction").format(seconds = str(alarmTime)))
			else:
				# Translators: Presented when end of track is approaching.
				ui.message(_("Warning: {seconds} sec remaining").format(seconds = str(alarmTime)))


	# Hacks for gain focus events.
	def event_gainFocus(self, obj, nextHandler):
		if self.deletedFocusObj or (obj.windowClassName == "TListView" and obj.role == 0):
			self.deletedFocusObj = False
			return
		nextHandler()

	# Add or remove SPL-specific touch commands.
	# Code comes from Enhanced Touch Gestures add-on from the same author.
	# This may change if NVDA core decides to abandon touch mode concept.

	def event_appModule_gainFocus(self):
		if touchHandler.handler:
			if "SPL" not in touchHandler.availableTouchModes:
				touchHandler.availableTouchModes.append("SPL")
				# Add the human-readable representation also.
				touchHandler.touchModeLabels["spl"] = _("SPL mode")

	def event_appModule_loseFocus(self):
		if touchHandler.handler:
			# Switch to object mode.
			touchHandler.handler._curTouchMode = touchHandler.availableTouchModes[1]
			if "SPL" in touchHandler.availableTouchModes:
				# If we have too many touch modes, pop all except the original entries.
				for mode in touchHandler.availableTouchModes:
					if mode == "SPL": touchHandler.availableTouchModes.pop()
			try:
				del touchHandler.touchModeLabels["spl"]
			except KeyError:
				pass


	# Save configuration when terminating.
	def terminate(self):
		super(AppModule, self).terminate()
		# 6.3: Memory leak results if encoder flag sets and other encoder support maps aren't cleaned up.
		# This also could have allowed a hacker to modify the flags set (highly unlikely) so NvDA could get confused next time Studio loads.
		import sys
		if "globalPlugins.SPLStudioUtils.encoders" in sys.modules:
			import globalPlugins.SPLStudioUtils.encoders
			globalPlugins.SPLStudioUtils.encoders.cleanup()
		splconfig.saveConfig()
		# Delete focused track reference.
		self._focusedTrack = None
		try:
			self.prefsMenu.RemoveItem(self.SPLSettings)
		except AttributeError, wx.PyDeadObjectError:
			pass
		# Tell the handle finder thread it's time to leave this world.
		self.noMoreHandle.set()
		# Manually clear the following dictionaries.
		self.carts.clear()
		self._cachedStatusObjs.clear()
		# Just to make sure:
		global _SPLWin
		if _SPLWin: _SPLWin = None


	# Script sections (for ease of maintenance):
	# Time-related: elapsed time, end of track alarm, etc.
	# Misc scripts: track finder and others.
	# SPL Assistant layer: status commands.

	# A few time related scripts (elapsed time, remaining time, etc.).

	# Specific to time scripts using Studio API.
	# 6.0: Split this into two functions: the announcer (below) and formatter.
	# 7.0: The ms (millisecond) argument will be used when announcing playlist remainder.
	# 16.12: Include hours by default unless told not to do so.
	def announceTime(self, t, offset = None, ms=True, includeHours=None):
		if t <= 0:
			ui.message("00:00")
		else:
			ui.message(self._ms2time(t, offset = offset, ms=ms, includeHours=includeHours))

	# Formatter: given time in milliseconds, convert it to human-readable format.
	# 7.0: There will be times when one will deal with time in seconds.
	# 16.12: For some cases, do not include hour slot when trying to conform to what Studio displays.)
	def _ms2time(self, t, offset = None, ms=True, includeHours=None):
		if t <= 0:
			return "00:00"
		else:
			if ms:
				t = (t/1000) if not offset else (t/1000)+offset
			mm, ss = divmod(t, 60)
			if mm > 59 and (includeHours or (includeHours is None and splconfig.SPLConfig["General"]["TimeHourAnnounce"])):
				hh, mm = divmod(mm, 60)
				# Hour value is also filled with leading zero's.
				# 6.1: Optimize the string builder so it can return just one string.
				t0 = str(hh).zfill(2)
				t1 = str(mm).zfill(2)
				t2 = str(ss).zfill(2)
				return ":".join([t0, t1, t2])
			else:
				t1 = str(mm).zfill(2)
				t2 = str(ss).zfill(2)
				return ":".join([t1, t2])

	# Scripts which rely on API.
	def script_sayRemainingTime(self, gesture):
		statusAPI(3, 105, self.announceTime, offset=1)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayRemainingTime.__doc__=_("Announces the remaining track time.")

	def script_sayElapsedTime(self, gesture):
		statusAPI(0, 105, self.announceTime)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayElapsedTime.__doc__=_("Announces the elapsed time for the currently playing track.")

	def script_sayBroadcasterTime(self, gesture):
		# Says things such as "25 minutes to 2" and "5 past 11".
		# Parse the local time and say it similar to how Studio presents broadcaster time.
		h, m = time.localtime()[3], time.localtime()[4]
		if h not in (0, 12):
			h %= 12
		if m == 0:
			if h == 0: h+=12
			# Messages in this method should not be translated.
			broadcasterTime = "{hour} o'clock".format(hour = h)
		elif 1 <= m <= 30:
			if h == 0: h+=12
			broadcasterTime = "{minute} min past {hour}".format(minute = m, hour = h)
		else:
			if h == 12: h = 1
			m = 60-m
			broadcasterTime = "{minute} min to {hour}".format(minute = m, hour = h+1)
		ui.message(broadcasterTime)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayBroadcasterTime.__doc__=_("Announces broadcaster time.")

	def script_sayCompleteTime(self, gesture):
		import winKernel
		# Says complete time in hours, minutes and seconds via kernel32's routines.
		ui.message(winKernel.GetTimeFormat(winKernel.LOCALE_USER_DEFAULT, 0, None, None))
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayCompleteTime.__doc__=_("Announces time including seconds.")

	# Invoke the common alarm dialog.
	# The below invocation function is also used for error handling purposes.
	# Levels indicate which dialog to show (0 = all, 1 = outro, 2 = intro, 3 = microphone).

	def alarmDialog(self, level):
		if splconfui._configDialogOpened:
			# Translators: Presented when the add-on config dialog is opened.
			wx.CallAfter(gui.messageBox, _("The add-on settings dialog is opened. Please close the settings dialog first."), _("Error"), wx.OK|wx.ICON_ERROR)
			return
		try:
			d = splconfig.SPLAlarmDialog(gui.mainFrame, level)
			gui.mainFrame.prePopup()
			d.Raise()
			d.Show()
			gui.mainFrame.postPopup()
			splconfig._alarmDialogOpened = True
		except RuntimeError:
			wx.CallAfter(splconfig._alarmError)

	# Set the end of track alarm time between 1 and 59 seconds.

	def script_setEndOfTrackTime(self, gesture):
		self.alarmDialog(1)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_setEndOfTrackTime.__doc__=_("sets end of track alarm (default is 5 seconds).")

	# Set song ramp (introduction) time between 1 and 9 seconds.

	def script_setSongRampTime(self, gesture):
		self.alarmDialog(2)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_setSongRampTime.__doc__=_("sets song intro alarm (default is 5 seconds).")

	# Tell NVDA to play a sound when mic was active for a long time, as well as contorl the alarm interval.
	# 8.0: This dialog will let users configure mic alarm interval as well.

	def script_setMicAlarm(self, gesture):
		self.alarmDialog(3)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_setMicAlarm.__doc__=_("Sets microphone alarm (default is 5 seconds).")

	# SPL Config management among others.

	def script_openConfigDialog(self, gesture):
		wx.CallAfter(splconfui.onConfigDialog, None)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_openConfigDialog.__doc__=_("Opens SPL Studio add-on configuration dialog.")

	def script_openWelcomeDialog(self, gesture):
		gui.mainFrame.prePopup()
		splconfig.WelcomeDialog(gui.mainFrame).Show()
		gui.mainFrame.postPopup()
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_openWelcomeDialog.__doc__=_("Opens SPL Studio add-on welcome dialog.")

	# Other commands (track finder and others)

	# Toggle whether beeps should be heard instead of toggle announcements.
	# Deprecated in 8.0, may come back later.

	#def script_toggleBeepAnnounce(self, gesture):
		#splconfig.SPLConfig["General"]["BeepAnnounce"] = not splconfig.SPLConfig["General"]["BeepAnnounce"]
		#splconfig.message("BeepAnnounce", splconfig.SPLConfig["General"]["BeepAnnounce"])
	#script_toggleBeepAnnounce.__doc__=_("Toggles status announcements between words and beeps.")

	# Braille timer.
	# Announce end of track and other info via braille.

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
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_setBrailleTimer.__doc__=_("Toggles between various braille timer settings.")

	# The track finder utility for find track script and other functions
	# Perform a linear search to locate the track name and/or description which matches the entered value.
	# Also, find column content for a specific column if requested.
	# 6.0: Split this routine into two functions, with the while loop moving to a function of its own.
	# This new function will be used by track finder and place marker locator.
	findText = ""

	def trackFinder(self, text, obj, directionForward=True, column=None):
		speech.cancelSpeech()
		if column is None:
			column = [obj.indexOf("Artist"), obj.indexOf("Title")]
		track = self._trackLocator(text, obj=obj, directionForward=directionForward, columns=column)
		if track:
			if self.findText != text: self.findText = text
			# We need to fire set focus event twice and exit this routine (return if 5.0x).
			# 16.10.1/15.2 LTS: Just select this track in order to prevent a dispute between NVDA and SPL in regards to focused track.
			# 16.11: Call setFocus if it is post-5.01, as SPL API can be used to select the desired track.
			selectTrack(track.IAccessibleChildID-1)
			track.setFocus(), track.setFocus()
		else:
			wx.CallAfter(gui.messageBox,
			# Translators: Standard dialog message when an item one wishes to search is not found (copy this from main nvda.po).
			_("Search string not found."),
			# Translators: Standard error title for find error (copy this from main nvda.po).
			_("Find error"),wx.OK|wx.ICON_ERROR)

	# Split from track finder in 2015.
	# Return a track with the given search criteria.
	# Column is a list of columns to be searched (if none, it'll be artist and title).
	def _trackLocator(self, text, obj=api.getFocusObject(), directionForward=True, columns=None):
		nextTrack = "next" if directionForward else "previous"
		while obj is not None:
			# Do not use column content attribute, because sometimes NVDA will say it isn't a track item when in fact it is.
			# If this happens, use the module level version of column content getter.
			# Optimization: search column texts.
			for column in columns:
				columnText = splmisc._getColumnContent(obj, column)
				if columnText and text in columnText:
					return obj
			obj = getattr(obj, nextTrack)
		return None

		# Find a specific track based on a searched text.
	# But first, check if track finder can be invoked.
	# Attempt level specifies which track finder to open (0 = Track Finder, 1 = Column Search, 2 = Time range).
	def _trackFinderCheck(self, attemptLevel):
		if api.getForegroundObject().windowClassName != "TStudioForm":
			if attemptLevel == 0:
				# Translators: Presented when a user attempts to find tracks but is not at the track list.
				ui.message(_("Track finder is available only in track list."))
			elif attemptLevel == 1:
				# Translators: Presented when a user attempts to find tracks but is not at the track list.
				ui.message(_("Column search is available only in track list."))
			elif attemptLevel == 2:
				# Translators: Presented when a user attempts to find tracks but is not at the track list.
				ui.message(_("Time range finder is available only in track list."))
			return False
		elif api.getForegroundObject().windowClassName == "TStudioForm" and api.getFocusObject().role == controlTypes.ROLE_LIST:
			# Translators: Presented when a user wishes to find a track but didn't add any tracks.
			ui.message(_("You need to add at least one track to find tracks."))
			return False
		return True

	def trackFinderGUI(self, columnSearch=False):
		try:
			# Translators: Title for track finder dialog.
			if not columnSearch: title = _("Find track")
			# Translators: Title for column search dialog.
			else: title = _("Column search")
			d = splmisc.SPLFindDialog(gui.mainFrame, api.getFocusObject(), self.findText, title, columnSearch = columnSearch)
			gui.mainFrame.prePopup()
			d.Raise()
			d.Show()
			gui.mainFrame.postPopup()
			splmisc._findDialogOpened = True
		except RuntimeError:
			wx.CallAfter(splmisc._finderError)

	def script_findTrack(self, gesture):
		if self._trackFinderCheck(0): self.trackFinderGUI()
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_findTrack.__doc__=_("Finds a track in the track list.")

	def script_columnSearch(self, gesture):
		if self._trackFinderCheck(1): self.trackFinderGUI(columnSearch=True)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_columnSearch.__doc__=_("Finds text in columns.")

	# Find next and previous scripts.

	def script_findTrackNext(self, gesture):
		if self._trackFinderCheck(0):
			if self.findText == "": self.trackFinderGUI()
			else: self.trackFinder(self.findText, obj=api.getFocusObject().next)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_findTrackNext.__doc__=_("Finds the next occurrence of the track with the name in the track list.")

	def script_findTrackPrevious(self, gesture):
		if self._trackFinderCheck(0):
			if self.findText == "": self.trackFinderGUI()
			else: self.trackFinder(self.findText, obj=api.getFocusObject().previous, directionForward=False)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_findTrackPrevious.__doc__=_("Finds previous occurrence of the track with the name in the track list.")

	# Time range finder.
	# Locate a track with duration falling between min and max.

	def script_timeRangeFinder(self, gesture):
		if self._trackFinderCheck(2):
			try:
				d = splmisc.SPLTimeRangeDialog(gui.mainFrame, api.getFocusObject(), statusAPI)
				gui.mainFrame.prePopup()
				d.Raise()
				d.Show()
				gui.mainFrame.postPopup()
				splmisc._findDialogOpened = True
			except RuntimeError:
				wx.CallAfter(splmisc._finderError)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_timeRangeFinder.__doc__=_("Locates track with duration within a time range")

	# Cart explorer
	cartExplorer = False
	carts = {} # The carts dictionary (key = cart gesture, item = cart name).

	# Assigning carts.

	def buildFNCarts(self):
		# Used xrange, as it is much faster; change this to range if NvDA core decides to use Python 3.
		for i in xrange(12):
			self.bindGesture("kb:f%s"%(i+1), "cartExplorer")
			self.bindGesture("kb:shift+f%s"%(i+1), "cartExplorer")
			self.bindGesture("kb:control+f%s"%(i+1), "cartExplorer")
			self.bindGesture("kb:alt+f%s"%(i+1), "cartExplorer")

	def buildNumberCarts(self):
		for i in xrange(10):
			self.bindGesture("kb:%s"%(i), "cartExplorer")
			self.bindGesture("kb:shift+%s"%(i), "cartExplorer")
			self.bindGesture("kb:control+%s"%(i), "cartExplorer")
			self.bindGesture("kb:alt+%s"%(i), "cartExplorer")
		# Take care of dash and equals.
		self.bindGesture("kb:-", "cartExplorer"), self.bindGesture("kb:=", "cartExplorer")
		self.bindGesture("kb:shift+-", "cartExplorer"), self.bindGesture("kb:shift+=", "cartExplorer")
		self.bindGesture("kb:control+-", "cartExplorer"), self.bindGesture("kb:control+=", "cartExplorer")
		self.bindGesture("kb:alt+-", "cartExplorer"), self.bindGesture("kb:alt+=", "cartExplorer")

	def cartsBuilder(self, build=True):
		# A function to build and return cart commands.
		if build:
			self.buildFNCarts()
			self.buildNumberCarts()
		else:
			self.clearGestureBindings()
			self.bindGestures(self.__gestures)

	def script_toggleCartExplorer(self, gesture):
		if not self.cartExplorer:
			# Prevent cart explorer from being engaged outside of playlist viewer.
			# Todo for 6.0: Let users set cart banks.
			fg = api.getForegroundObject()
			if fg.windowClassName != "TStudioForm":
				# Translators: Presented when cart explorer cannot be entered.
				ui.message(_("You are not in playlist viewer, cannot enter cart explorer"))
				return
			self.carts = splmisc.cartExplorerInit(fg.name)
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
			# Translators: Presented when cart explorer is off.
			ui.message(_("Exiting cart explorer"))
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_toggleCartExplorer.__doc__=_("Toggles cart explorer to learn cart assignments.")

	def script_cartExplorer(self, gesture):
		if api.getForegroundObject().windowClassName != "TStudioForm":
			gesture.send()
			return
		if scriptHandler.getLastScriptRepeatCount() >= 1: gesture.send()
		else:
			if gesture.displayName in self.carts: ui.message(self.carts[gesture.displayName])
			elif self.carts["standardLicense"] and (len(gesture.displayName) == 1 or gesture.displayName[-2] == "+"):
				# Translators: Presented when cart command is unavailable.
				ui.message(_("Cart command unavailable"))
			else:
				# Translators: Presented when there is no cart assigned to a cart command.
				ui.message(_("Cart unassigned"))

	# Library scan announcement
	# Announces progress of a library scan (launched from insert tracks dialog by pressing Control+Shift+R or from rescan option from Options dialog).

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
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_setLibraryScanProgress.__doc__=_("Toggles library scan progress settings.")

	def script_startScanFromInsertTracks(self, gesture):
		gesture.send()
		fg = api.getForegroundObject()
		if fg.windowClassName == "TTrackInsertForm":
			# Translators: Presented when library scan has started.
			ui.message(_("Scan start"))
			if self.productVersion not in noLibScanMonitor: self.libraryScanning = True

	# Report library scan (number of items scanned) in the background.
	def monitorLibraryScan(self):
		global libScanT
		if libScanT and libScanT.isAlive() and api.getForegroundObject().windowClassName == "TTrackInsertForm":
			return
		countA = statusAPI(1, 32, ret=True)
		if countA == 0:
			self.libraryScanning = False
			return
		time.sleep(0.1)
		if api.getForegroundObject().windowClassName == "TTrackInsertForm" and self.productVersion in noLibScanMonitor:
			self.libraryScanning = False
			return
		# Sometimes, a second call is needed to obtain the real scan count in Studio 5.10 and later.
		countB = statusAPI(1, 32, ret=True)
		if countA == countB:
			self.libraryScanning = False
			countB = statusAPI(0, 32, ret=True)
			# Translators: Presented when library scanning is finished.
			ui.message(_("{itemCount} items in the library").format(itemCount = countB))
		else:
			libScanT = threading.Thread(target=self.libraryScanReporter, args=(_SPLWin, countA, countB, 1))
			libScanT.daemon = True
			libScanT.start()

	def libraryScanReporter(self, _SPLWin, countA, countB, parem):
		scanIter = 0
		while countA != countB:
			if not self.libraryScanning: return
			countA = countB
			time.sleep(1)
			# Do not continue if we're back on insert tracks form or library scan is finished.
			if api.getForegroundObject().windowClassName == "TTrackInsertForm" or not self.libraryScanning:
				return
			countB, scanIter = statusAPI(parem, 32, ret=True), scanIter+1
			if countB < 0:
				break
			if scanIter%5 == 0 and splconfig.SPLConfig["General"]["LibraryScanAnnounce"] not in ("off", "ending"):
				self._libraryScanAnnouncer(countB, splconfig.SPLConfig["General"]["LibraryScanAnnounce"])
		self.libraryScanning = False
		if self.backgroundStatusMonitor: return
		if splconfig.SPLConfig["General"]["LibraryScanAnnounce"] != "off":
			if splconfig.SPLConfig["General"]["BeepAnnounce"]:
				tones.beep(370, 100)
			else:
				# Translators: Presented after library scan is done.
				ui.message(_("Scan complete with {itemCount} items").format(itemCount = countB))

	# Take care of library scanning announcement.
	def _libraryScanAnnouncer(self, count, announcementType):
		if announcementType == "progress":
			# Translators: Presented when library scan is in progress.
			tones.beep(550, 100) if splconfig.SPLConfig["General"]["BeepAnnounce"] else ui.message(_("Scanning"))
		elif announcementType == "numbers":
			if splconfig.SPLConfig["General"]["BeepAnnounce"]:
				tones.beep(550, 100)
				# No need to provide translatable string - just use index.
				ui.message("{0}".format(count))
			else: ui.message(_("{itemCount} items scanned").format(itemCount = count))

	# Place markers.
	placeMarker = None

	# Is the place marker set on this track?
	# Track argument is None (only useful for debugging purposes).
	def isPlaceMarkerTrack(self, track=None):
		if track is None: track = api.getFocusObject()
		index = track.indexOf("Filename")
		filename = track._getColumnContent(index)
		if self.placeMarker == (index, filename):
			return True
		return False

	# Used in delete track workaround routine.
	def preTrackRemoval(self):
		if self.isPlaceMarkerTrack(track=api.getFocusObject()):
			self.placeMarker = None

	# Metadata streaming manager
	# Obtains information on metadata streaming for each URL, notifying the broadcaster if told to do so upon startup.
	# Also allows broadcasters to toggle metadata streaming.

	# First, the reminder function.
	# 7.0: Calls the module-level version.
	def _metadataAnnouncer(self, reminder=False):
		splmisc._metadataAnnouncer(reminder=reminder, handle=_SPLWin)

	# The script version to open the manage metadata URL's dialog.
	def script_manageMetadataStreams(self, gesture):
		# Do not even think about opening this dialog if handle to Studio isn't found.
		if _SPLWin is None:
			# Translators: Presented when stremaing dialog cannot be shown.
			ui.message(_("Cannot open metadata streaming dialog"))
			return
		if splconfui._configDialogOpened or splconfui._metadataDialogOpened:
			# Translators: Presented when the add-on config dialog is opened.
			wx.CallAfter(gui.messageBox, _("The add-on settings dialog or the metadata streaming dialog is opened. Please close the opened dialog first."), _("Error"), wx.OK|wx.ICON_ERROR)
			return
		try:
			# Passing in the function object is enough to change the dialog UI.
			d = splconfui.MetadataStreamingDialog(gui.mainFrame, func=statusAPI)
			gui.mainFrame.prePopup()
			d.Raise()
			d.Show()
			gui.mainFrame.postPopup()
			splconfui._metadataDialogOpened = True
		except RuntimeError:
			wx.CallAfter(splconfig._alarmError)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_manageMetadataStreams.__doc__=_("Opens a dialog to quickly enable or disable metadata streaming.")

	# Track time analysis
	# Return total length of the selected tracks upon request.
	# Analysis command (SPL Assistant) will be assignable.
	_analysisMarker = None

	# Trakc time analysis requires main playlist viewer to be the foreground window.
	def _trackAnalysisAllowed(self):
		if api.getForegroundObject().windowClassName != "TStudioForm":
			# Translators: Presented when track time anlaysis cannot be performed because user is not focused on playlist viewer.
			ui.message(_("Not in playlist viewer, cannot perform track time analysis"))
			return False
		return True

	# Return total duration of a range of tracks.
	# This is used in track time analysis when multiple tracks are selected.
	# This is also called from playlist duration scripts.
	def totalTime(self, start, end):
		# Take care of errors such as the following.
		if start < 0 or end > statusAPI(0, 124, ret=True)-1:
			raise ValueError("Track range start or end position out of range")
			return
		totalLength = 0
		if start == end:
			filename = statusAPI(start, 211, ret=True)
			totalLength = statusAPI(filename, 30, ret=True)
		else:
			for track in xrange(start, end+1):
				filename = statusAPI(track, 211, ret=True)
				totalLength+=statusAPI(filename, 30, ret=True)
		return totalLength

	# Some handlers for native commands.

	# In Studio 5.0x, when deleting a track, NVDA announces wrong track item due to focus bouncing.
	# The below hack is sensitive to changes in NVDA core.
	deletedFocusObj = False

	def script_deleteTrack(self, gesture):
		self.preTrackRemoval()
		gesture.send()

	# When Escape is pressed, activate background library scan if conditions are right.
	def script_escape(self, gesture):
		gesture.send()
		if self.libraryScanning:
			if not libScanT or (libScanT and not libScanT.isAlive()):
				self.monitorLibraryScan()

	# The developer would like to get feedback from you.
	def script_sendFeedbackEmail(self, gesture):
		os.startfile("mailto:joseph.lee22590@gmail.com")
	script_sendFeedbackEmail.__doc__="Opens the default email client to send an email to the add-on developer"


	# SPL Assistant: reports status on playback, operation, etc.
	# Used layer command approach to save gesture assignments.
	# Most were borrowed from JFW and Window-Eyes layer scripts.

	# Set up the layer script environment.
	def getScript(self, gesture):
		if not self.SPLAssistant:
			return appModuleHandler.AppModule.getScript(self, gesture)
		script = appModuleHandler.AppModule.getScript(self, gesture)
		if not script:
			script = finally_(self.script_error, self.finish)
		return finally_(script, self.finish)

	def finish(self):
		self.SPLAssistant = False
		self.clearGestureBindings()
		self.bindGestures(self.__gestures)
		if self.cartExplorer:
			self.buildFNCarts()
			self.buildNumberCarts()

	def script_error(self, gesture):
		tones.beep(120, 100)
		self.finish()

	# SPL Assistant flag.
	SPLAssistant = False

	# The SPL Assistant layer driver.

	def script_SPLAssistantToggle(self, gesture):
		# Enter the layer command if an only if we're in the track list to allow easier gesture assignment.
		# 7.0: This requirement has been relaxed (commands themselves will check for specific conditions).
		# Also, do not bother if the app module is not running.
		if scriptHandler.getLastScriptRepeatCount() > 0:
			gesture.send()
			self.finish()
			return
		try:
			# 7.0: Don't bother if handle to Studio isn't found.
			if _SPLWin is None:
				# Translators: Presented when SPL Assistant cannot be invoked.
				ui.message(_("Failed to locate Studio main window, cannot enter SPL Assistant"))
				return
			if self.SPLAssistant:
				self.script_error(gesture)
				return
			# To prevent entering wrong gesture while the layer is active.
			self.clearGestureBindings()
			# 7.0: choose the required compatibility layer.
			if splconfig.SPLConfig["Advanced"]["CompatibilityLayer"] == "off": self.bindGestures(self.__SPLAssistantGestures)
			elif splconfig.SPLConfig["Advanced"]["CompatibilityLayer"] == "jfw": self.bindGestures(self.__SPLAssistantJFWGestures)
			elif splconfig.SPLConfig["Advanced"]["CompatibilityLayer"] == "wineyes": self.bindGestures(self.__SPLAssistantWEGestures)
			# 7.0: Certain commands involving number row.
			# 8.0: Also assign encoder status commands in addition to columns explorer.
			for i in xrange(5):
				self.bindGesture("kb:%s"%(i), "columnExplorer")
				self.bindGesture("kb:shift+%s"%(i), "metadataEnabled")
			for i in xrange(5, 10):
				self.bindGesture("kb:%s"%(i), "columnExplorer")
			self.SPLAssistant = True
			tones.beep(512, 50)
			if splconfig.SPLConfig["Advanced"]["CompatibilityLayer"] == "jfw": ui.message("JAWS")
			elif splconfig.SPLConfig["Advanced"]["CompatibilityLayer"] == "wineyes": ui.message("Window-Eyes")
		except WindowsError:
			return
	# Translators: Input help mode message for a layer command in Station Playlist Studio.
	script_SPLAssistantToggle.__doc__=_("The SPL Assistant layer command. See the add-on guide for more information on available commands.")


	# Status table keys
	SPLPlayStatus = 0
	SPLSystemStatus = 1
	SPLScheduledToPlay = 3
	SPLNextTrackTitle = 4
	SPLCurrentTrackTitle = 5
	SPLTemperature = 6
	SPLScheduled = 7

	# Table of child constants based on versions
	# These are scattered throughout the screen, so one can use foreground.getChild(index) to fetch them (getChild tip from Jamie Teh (NV Access)).
	# Because 5.x (an perhaps future releases) uses different screen layout, look up the needed constant from the table below (row = info needed, column = version).
	statusObjs={
		SPLPlayStatus: 6, # Play status, mic, etc.
		SPLSystemStatus: -2, # The second status bar containing system status such as up time.
		SPLScheduledToPlay: 19, # In case the user selects one or more tracks in a given hour.
		SPLScheduled: 20, # Time when the selected track will begin.
		SPLNextTrackTitle: 8, # Name and duration of the next track if any.
		SPLCurrentTrackTitle: 9, # Name of the currently playing track.
		SPLTemperature: 7, # Temperature for the current city.
	}

	_cachedStatusObjs = {}

	# Called in the layer commands themselves.
	# 16.11: in Studio 5.20, it is possible to obtain some of these via the API, hence the API method is used.
	def status(self, infoIndex):
		# Look up the cached objects first for faster response.
		if not infoIndex in self._cachedStatusObjs:
			fg = api.getForegroundObject()
			if fg is not None and fg.windowClassName != "TStudioForm":
				# 6.1: Allow gesture-based functions to look up status information even if Studio window isn't focused.
				fg = getNVDAObjectFromEvent(user32.FindWindowA("TStudioForm", None), OBJID_CLIENT, 0)
			statusObj = self.statusObjs[infoIndex]
			# 7.0: sometimes (especially when first loaded), OBJID_CLIENT fails, so resort to retrieving focused object instead.
			if fg is not None and fg.childCount > 1:
				self._cachedStatusObjs[infoIndex] = fg.getChild(statusObj)
			else: return api.getFocusObject()
		return self._cachedStatusObjs[infoIndex]

	# Status flags for Studio 5.20 API.
	_statusBarMessages=(
		("Play status: Stopped","Play status: Playing"),
		("Automation Off","Automation On"),
		("Microphone Off","Microphone On"),
		("Line-In Off","Line-In On"),
		("Record to file Off","Record to file On"),
	)

	# In the layer commands below, sayStatus function is used if screen objects or API must be used (API is for Studio 5.20 and later).
	def sayStatus(self, index):
		if self.SPLCurVersion < "5.20":
			status = self.status(self.SPLPlayStatus).getChild(index).name
		else:
			status = self._statusBarMessages[index][statusAPI(index, 39, ret=True)]
		ui.message(status if splconfig.SPLConfig["General"]["MessageVerbosity"] == "beginner" else status.split()[-1])

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
		# 16.12: Because cart edit status also shows cart insert status, verbosity control will not apply.
		if self.productVersion >= "5.20":
			cartEdit = statusAPI(5, 39, ret=True)
			cartInsert = statusAPI(6, 39, ret=True)
			if cartEdit: ui.message("Cart Edit On")
			elif not cartEdit and cartInsert: ui.message("Cart Insert On")
			else: ui.message("Cart Edit Off")
		else:
			ui.message(self.status(self.SPLPlayStatus).getChild(5).name)

	def script_sayHourTrackDuration(self, gesture):
		statusAPI(0, 27, self.announceTime)

	def script_sayHourRemaining(self, gesture):
		# 7.0: Split from playlist remaining script (formerly the playlist remainder command).
		statusAPI(1, 27, self.announceTime)

	def script_sayPlaylistRemainingDuration(self, gesture):
		obj = api.getFocusObject() if api.getForegroundObject().windowClassName == "TStudioForm" else self._focusedTrack
		if obj is None:
			ui.message("Please return to playlist viewer before invoking this command.")
			return
		if obj.role == controlTypes.ROLE_LIST:
			ui.message("00:00")
			return
		col = obj.indexOf("Duration")
		totalDuration = 0
		while obj is not None:
			segue = obj._getColumnContent(col)
			if segue is not None:
				hms = segue.split(":")
				totalDuration += (int(hms[0])*3600) + (int(hms[1])*60) + int(hms[2]) if len(hms) == 3 else (int(hms[0])*60) + int(hms[1])
			obj = obj.next
		self.announceTime(totalDuration, ms=False)

	def script_sayPlaylistModified(self, gesture):
		try:
			obj = self.status(self.SPLSystemStatus).getChild(5)
			ui.message(obj.name)
		except IndexError:
			# Translators: Presented when playlist modification is unavailable (for Studio 4.33 and earlier)
			ui.message(_("Playlist modification not available"))

	def script_sayNextTrackTitle(self, gesture):
		try:
			obj = self.status(self.SPLNextTrackTitle).firstChild
			# Translators: Presented when there is no information for the next track.
			ui.message(_("No next track scheduled or no track is playing")) if obj.name is None else ui.message(obj.name)
		except RuntimeError:
			# Translators: Presented when next track information is unavailable.
			ui.message(_("Cannot find next track information"))
		finally:
			self.finish()
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayNextTrackTitle.__doc__=_("Announces title of the next track if any")

	def script_sayCurrentTrackTitle(self, gesture):
		try:
			obj = self.status(self.SPLCurrentTrackTitle).firstChild
			# Translators: Presented when there is no information for the current track.
			ui.message(_("Cannot locate current track information or no track is playing")) if obj.name is None else ui.message(obj.name)
		except RuntimeError:
			# Translators: Presented when current track information is unavailable.
			ui.message(_("Cannot find current track information"))
		finally:
			self.finish()
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayCurrentTrackTitle.__doc__=_("Announces title of the currently playing track")

	def script_sayTemperature(self, gesture):
		try:
			obj = self.status(self.SPLTemperature).firstChild
			# Translators: Presented when there is no weather or temperature information.
			ui.message(_("Weather and temperature not configured")) if obj.name is None else ui.message(obj.name)
		except RuntimeError:
			# Translators: Presented when temperature information cannot be found.
			ui.message(_("Weather information not found"))
		finally:
			self.finish()
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayTemperature.__doc__=_("Announces temperature and weather information")

	def script_sayUpTime(self, gesture):
		obj = self.status(self.SPLSystemStatus).firstChild
		ui.message(obj.name)

	def script_sayScheduledTime(self, gesture):
		# 7.0: Scheduled is the time originally specified in Studio, scheduled to play is broadcast time based on current time.
		# 16.12: use Studio API if using 5.20.
		if self.productVersion >= "5.20":
			# Sometimes, hour markers return seconds.999 due to rounding error, hence this must be taken care of here.
			trackStarts = divmod(statusAPI(3, 27, ret=True), 1000)
			# For this method, all three components of time display (hour, minute, second) must be present.
			# In case it is midnight (0.0 but sometimes shown as 86399.999 due to rounding error), just say "midnight".
			if trackStarts in ((86399, 999), (0, 0)): ui.message("00:00:00")
			else: self.announceTime(trackStarts[0]+1 if trackStarts[1] == 999 else trackStarts[0], ms=False)
		else:
			obj = self.status(self.SPLScheduled).firstChild
			ui.message(obj.name)

	def script_sayScheduledToPlay(self, gesture):
		# 7.0: This script announces length of time remaining until the selected track will play.
		# 16.12: Use Studio 5.20 API (faster and more reliable).
		if self.productVersion >= "5.20":
			# This is the only time hour announcement should not be used in order to conform to what's displayed on screen.
			self.announceTime(statusAPI(4, 27, ret=True), includeHours=False)
		else:
			obj = self.status(self.SPLScheduledToPlay).firstChild
			ui.message(obj.name)

	def script_sayListenerCount(self, gesture):
		obj = self.status(self.SPLSystemStatus).getChild(3)
		# Translators: Presented when there is no listener count information.
		ui.message(obj.name) if obj.name is not None else ui.message(_("Listener count not found"))

	def script_sayTrackPitch(self, gesture):
		try:
			obj = self.status(self.SPLSystemStatus).getChild(4)
			ui.message(obj.name)
		except IndexError:
			# Translators: Presented when there is no information on song pitch (for Studio 4.33 and earlier).
			ui.message(_("Song pitch not available"))

	# Few toggle/misc scripts that may be excluded from the layer later.

	def script_libraryScanMonitor(self, gesture):
		if not self.libraryScanning:
			scanning = statusAPI(1, 32, ret=True)
			if scanning < 0:
				items = statusAPI(0, 32, ret=True)
				ui.message(_("{itemCount} items in the library").format(itemCount = items))
				return
			self.libraryScanning = True
			# Translators: Presented when attempting to start library scan.
			ui.message(_("Monitoring library scan"))
			self.monitorLibraryScan()
		else:
			# Translators: Presented when library scan is already in progress.
			ui.message(_("Scanning is in progress"))

	def script_markTrackForAnalysis(self, gesture):
		self.finish()
		if self._trackAnalysisAllowed():
			focus = api.getFocusObject()
			if focus.role == controlTypes.ROLE_LIST:
				# Translators: Presented when track time analysis cannot be activated.
				ui.message(_("No tracks were added, cannot perform track time analysis"))
				return
			if scriptHandler.getLastScriptRepeatCount() == 0:
				self._analysisMarker = focus.IAccessibleChildID-1
				# Translators: Presented when track time analysis is turned on.
				ui.message(_("Track time analysis activated"))
			else:
				self._analysisMarker = None
				# Translators: Presented when track time analysis is turned off.
				ui.message(_("Track time analysis deactivated"))
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_markTrackForAnalysis.__doc__=_("Marks focused track as start marker for track time analysis")

	def script_trackTimeAnalysis(self, gesture):
		self.finish()
		if self._trackAnalysisAllowed():
			focus = api.getFocusObject()
			if focus.role == controlTypes.ROLE_LIST:
				ui.message(_("No tracks were added, cannot perform track time analysis"))
				return
			if self._analysisMarker is None:
				# Translators: Presented when track time analysis cannot be used because start marker is not set.
				ui.message(_("No track selected as start of analysis marker, cannot perform time analysis"))
				return
			trackPos = focus.IAccessibleChildID-1
			analysisBegin = min(self._analysisMarker, trackPos)
			analysisEnd = max(self._analysisMarker, trackPos)
			analysisRange = analysisEnd-analysisBegin+1
			totalLength = self.totalTime(analysisBegin, analysisEnd)
			if analysisRange == 1:
				self.announceTime(totalLength)
			else:
				# Translators: Presented when time analysis is done for a number of tracks (example output: Tracks: 3, totaling 5:00).
				ui.message(_("Tracks: {numberOfSelectedTracks}, totaling {totalTime}").format(numberOfSelectedTracks = analysisRange, totalTime = self._ms2time(totalLength)))
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_trackTimeAnalysis.__doc__=_("Announces total length of tracks between analysis start marker and the current track")

	def script_switchProfiles(self, gesture):
		splconfig.triggerProfileSwitch() if splconfig._triggerProfileActive else splconfig.instantProfileSwitch()

	def script_setPlaceMarker(self, gesture):
		obj = api.getFocusObject()
		try:
			index = obj.indexOf("Filename")
		except AttributeError:
			# Translators: Presented when place marker cannot be set.
			ui.message(_("No tracks found, cannot set place marker"))
			return
		filename = obj._getColumnContent(index)
		if filename:
			self.placeMarker = (index, filename)
			# Translators: Presented when place marker track is set.
			ui.message(_("place marker set"))
		else:
			# Translators: Presented when attempting to place a place marker on an unsupported track.
			ui.message(_("This track cannot be used as a place marker track"))

	def script_findPlaceMarker(self, gesture):
		# 7.0: Place marker command will still be restricted to playlist viewer in order to prevent focus bouncing.
		if api.getForegroundObject().windowClassName != "TStudioForm":
			# Translators: Presented when attempting to move to a place marker track when not focused in playlist viewer.
			ui.message(_("You cannot move to a place marker track outside of playlist viewer."))
			return
		if self.placeMarker is None:
			# Translators: Presented when no place marker is found.
			ui.message(_("No place marker found"))
		else:
			track = self._trackLocator(self.placeMarker[1], obj=api.getFocusObject().parent.firstChild, columns=[self.placeMarker[0]])
			# 16.11: Just like Track Finder, use select track function to select the place marker track.
			selectTrack(track.IAccessibleChildID-1)
			track.setFocus(), track.setFocus()

	def script_metadataStreamingAnnouncer(self, gesture):
		# 8.0: Call the module-level function directly.
		self._metadataAnnouncer()

	# Gesture(s) for the following script cannot be changed by users.
	def script_metadataEnabled(self, gesture):
		url = int(gesture.displayName[-1])
		checked = statusAPI(url, 36, ret=True)
		if checked == 1:
			# 0 is DSP encoder status, others are servers.
			if url:
				# Translators: Status message for metadata streaming.
				status = _("Metadata streaming on URL {URLPosition} enabled").format(URLPosition = url)
			else:
				# Translators: Status message for metadata streaming.
				status = _("Metadata streaming on DSP encoder enabled")
		else:
			if url:
				# Translators: Status message for metadata streaming.
				status = _("Metadata streaming on URL {URLPosition} disabled").format(URLPosition = url)
			else:
				# Translators: Status message for metadata streaming.
				status = _("Metadata streaming on DSP encoder disabled")
		ui.message(status)

	def script_columnExplorer(self, gesture):
		focus = api.getFocusObject()
		if not isinstance(focus, SPLTrackItem):
			# Translators: Presented when attempting to announce specific columns but the focused item isn't a track.
			ui.message(_("Not a track"))
		else:
					# LTS: Call the overlay class version.
			focus.script_columnExplorer(gesture)
		self.finish()

	def script_layerHelp(self, gesture):
		compatibility = splconfig.SPLConfig["Advanced"]["CompatibilityLayer"]
		# Translators: The title for SPL Assistant help dialog.
		if compatibility == "off": title = _("SPL Assistant help")
		# Translators: The title for SPL Assistant help dialog.
		elif compatibility == "jfw": title = _("SPL Assistant help for JAWS layout")
		# Translators: The title for SPL Assistant help dialog.
		elif compatibility == "wineyes": title = _("SPL Assistant help for Window-Eyes layout")
		wx.CallAfter(gui.messageBox, SPLAssistantHelp[compatibility], title)

	def script_openOnlineDoc(self, gesture):
		os.startfile("https://github.com/josephsl/stationplaylist/wiki/SPLDevAddonGuide")

	def script_updateCheck(self, gesture):
		self.finish()
		if splupdate._SPLUpdateT is not None and splupdate._SPLUpdateT.IsRunning(): splupdate._SPLUpdateT.Stop()
		# Display the update check progress dialog (inspired by add-on installation dialog in NvDA Core).
		# #9 (7.5): Do this if and only if update channel hasn't changed, otherwise we're stuck here forever.
		if not splupdate._pendingChannelChange:
			splupdate._progressDialog = gui.IndeterminateProgressDialog(gui.mainFrame,
			# Translators: The title of the dialog presented while checking for add-on updates.
			_("Add-on update check"),
			# Translators: The message displayed while checking for newer version of Studio add-on.
			_("Checking for new version of Studio add-on..."))
		threading.Thread(target=splupdate.updateCheck, kwargs={"continuous":splconfig.SPLConfig["Update"]["AutoUpdateCheck"], "confUpdateInterval":splconfig.SPLConfig["Update"]["UpdateInterval"]}).start()


	__SPLAssistantGestures={
		"kb:p":"sayPlayStatus",
		"kb:a":"sayAutomationStatus",
		"kb:m":"sayMicStatus",
		"kb:l":"sayLineInStatus",
		"kb:r":"sayRecToFileStatus",
		"kb:t":"sayCartEditStatus",
		"kb:h":"sayHourTrackDuration",
		"kb:shift+h":"sayHourRemaining",
		"kb:d":"sayPlaylistRemainingDuration",
		"kb:y":"sayPlaylistModified",
		"kb:u":"sayUpTime",
		"kb:n":"sayNextTrackTitle",
		"kb:c":"sayCurrentTrackTitle",
		"kb:w":"sayTemperature",
		"kb:i":"sayListenerCount",
		"kb:s":"sayScheduledTime",
		"kb:shift+s":"sayScheduledToPlay",
		"kb:shift+p":"sayTrackPitch",
		"kb:shift+r":"libraryScanMonitor",
		"kb:f9":"markTrackForAnalysis",
		"kb:f10":"trackTimeAnalysis",
		"kb:f12":"switchProfiles",
		"kb:f":"findTrack",
		"kb:Control+k":"setPlaceMarker",
		"kb:k":"findPlaceMarker",
		"kb:e":"metadataStreamingAnnouncer",
		"kb:f1":"layerHelp",
		"kb:shift+f1":"openOnlineDoc",
		"kb:control+shift+u":"updateCheck",
	}

	__SPLAssistantJFWGestures={
		"kb:p":"sayPlayStatus",
		"kb:a":"sayAutomationStatus",
		"kb:m":"sayMicStatus",
		"kb:shift+l":"sayLineInStatus",
		"kb:shift+e":"sayRecToFileStatus",
		"kb:t":"sayCartEditStatus",
		"kb:h":"sayHourTrackDuration",
		"kb:shift+h":"sayHourRemaining",
		"kb:r":"sayPlaylistRemainingDuration",
		"kb:y":"sayPlaylistModified",
		"kb:u":"sayUpTime",
		"kb:n":"sayNextTrackTitle",
		"kb:shift+c":"sayCurrentTrackTitle",
		"kb:c":"toggleCartExplorer",
		"kb:w":"sayTemperature",
		"kb:l":"sayListenerCount",
		"kb:s":"sayScheduledTime",
		"kb:shift+s":"sayScheduledToPlay",
		"kb:shift+p":"sayTrackPitch",
		"kb:shift+r":"libraryScanMonitor",
		"kb:f9":"markTrackForAnalysis",
		"kb:f10":"trackTimeAnalysis",
		"kb:f12":"switchProfiles",
		"kb:f":"findTrack",
		"kb:Control+k":"setPlaceMarker",
		"kb:k":"findPlaceMarker",
		"kb:e":"metadataStreamingAnnouncer",
		"kb:f1":"layerHelp",
		"kb:shift+f1":"openOnlineDoc",
	}

	__SPLAssistantWEGestures={
		"kb:p":"sayPlayStatus",
		"kb:a":"sayAutomationStatus",
		"kb:m":"sayMicStatus",
		"kb:shift+l":"sayLineInStatus",
		"kb:shift+e":"sayRecToFileStatus",
		"kb:t":"sayCartEditStatus",
		"kb:e":"sayElapsedTime",
		"kb:r":"sayRemainingTime",
		"kb:h":"sayHourTrackDuration",
		"kb:shift+h":"sayHourRemaining",
		"kb:d":"sayPlaylistRemainingDuration",
		"kb:y":"sayPlaylistModified",
		"kb:u":"sayUpTime",
		"kb:n":"sayNextTrackTitle",
		"kb:shift+c":"sayCurrentTrackTitle",
		"kb:c":"toggleCartExplorer",
		"kb:w":"sayTemperature",
		"kb:l":"sayListenerCount",
		"kb:s":"sayScheduledTime",
		"kb:shift+s":"sayScheduledToPlay",
		"kb:shift+p":"sayTrackPitch",
		"kb:shift+r":"libraryScanMonitor",
		"kb:f9":"markTrackForAnalysis",
		"kb:f10":"trackTimeAnalysis",
		"kb:f12":"switchProfiles",
		"kb:f":"findTrack",
		"kb:Control+k":"setPlaceMarker",
		"kb:k":"findPlaceMarker",
		"kb:g":"metadataStreamingAnnouncer",
		"kb:f1":"layerHelp",
		"kb:shift+f1":"openOnlineDoc",
		"kb:control+shift+u":"updateCheck",
	}

	__gestures={
		"kb:control+alt+t":"sayRemainingTime",
		"ts(SPL):2finger_flickDown":"sayRemainingTime",
		"kb:alt+shift+t":"sayElapsedTime",
		"kb:shift+nvda+f12":"sayBroadcasterTime",
		"ts(SPL):2finger_flickUp":"sayBroadcasterTime",
		"kb:alt+nvda+1":"setEndOfTrackTime",
		"ts(SPL):2finger_flickRight":"setEndOfTrackTime",
		"kb:alt+nvda+2":"setSongRampTime",
		"ts(SPL):2finger_flickLeft":"setSongRampTime",
		"kb:alt+nvda+4":"setMicAlarm",
		"kb:control+nvda+f":"findTrack",
		"kb:nvda+f3":"findTrackNext",
		"kb:shift+nvda+f3":"findTrackPrevious",
		"kb:alt+nvda+3":"toggleCartExplorer",
		"kb:alt+nvda+r":"setLibraryScanProgress",
		"kb:control+shift+r":"startScanFromInsertTracks",
		"kb:control+shift+x":"setBrailleTimer",
		"kb:alt+NVDA+0":"openConfigDialog",
		"kb:alt+NVDA+f1":"openWelcomeDialog",
		"kb:Shift+delete":"deleteTrack",
		"kb:Shift+numpadDelete":"deleteTrack",
		"kb:escape":"escape",
		"kb:control+nvda+-":"sendFeedbackEmail",
		#"kb:control+nvda+`":"SPLAssistantToggle"
	}
