# StationPlaylist Studio
# An app module and global plugin package for NVDA
# Copyright 2011, 2013-2019, Geoff Shang, Joseph Lee and others, released under GPL.
# The primary function of this appModule is to provide meaningful feedback to users of SplStudio
# by allowing speaking of items which cannot be easily found.
# Version 0.01 - 7 April 2011:
# Initial release: Jamie's focus hack plus auto-announcement of status items.
# Additional work done by Joseph Lee and other contributors.
# For SPL Studio Controller, focus movement, SAM Encoder support and other utilities, see the global plugin version of this app module.

# Minimum version: SPL 5.10, NvDA 2017.4.

import sys
import os
import time
import threading
import six
import controlTypes
import appModuleHandler
import api
import globalVars
import scriptHandler
import ui
import nvwave
import speech
import braille
import touchHandler
import gui
import wx
from winUser import user32, OBJID_CLIENT
from NVDAObjects import NVDAObject, NVDAObjectTextInfo
from NVDAObjects.IAccessible import IAccessible, getNVDAObjectFromEvent, sysListView32
from NVDAObjects.behaviors import Dialog, RowWithFakeNavigation, RowWithoutCellObjects
import textInfos
import tones
from . import splbase
from . import splconfig
from . import splconfui
from . import splmisc
from . import splactions
import addonHandler
addonHandler.initTranslation()
from .spldebugging import debugOutput
from .skipTranslation import translate

# Make sure the broadcaster is running a compatible version.
SPLMinVersion = "5.11"

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
		wx.CallAfter(micAlarmT2.Start, splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarmInterval"] * 1000)

# Category sounds dictionary (key = category, value = tone pitch).
_SPLCategoryTones = {
	"Break Note":415,
	"Timed Break Note":208,
	"<Manual Intro>":600,
}

# Routines for track items themselves (prepare for future work).
# #65 (18.07): this base class represents trakc items across StationPlaylist suites such as Studio, Creator and Track Tool.
class SPLTrackItem(sysListView32.ListItem):
	"""An abstract class representing track items across SPL suite of applications such as Studio, Creator and Track Tool.
	This class provides basic properties, scripts and methods such as Columns Explorer and others.
	Subclasses should provide custom routines for various attributes, including global ones to suit their needs.

	Each subclass is named after the app module name where tracks are encountered, such as SPLStudioTrackItem for Studio.
	Subclasses of module-specific subclasses are named after SPL version, for example SPL510TrackItem for studio 5.10.
	"""

	def _get_name(self):
		return self.IAccessibleObject.accName(self.IAccessibleChildID)

	def _get_description(self):
		# SysListView32.ListItem nullifies description, so resort to fetching it via IAccessible.
		return self.IAccessibleObject.accDescription(self.IAccessibleChildID)

	def script_moveToNextColumn(self, gesture):
		if (self._curColumnNumber+1) == self.parent.columnCount:
			tones.beep(2000, 100)
		else:
			self.__class__._curColumnNumber +=1
		self.announceColumnContent(self._curColumnNumber)

	def script_moveToPreviousColumn(self, gesture):
		if self._curColumnNumber <= 0:
			tones.beep(2000, 100)
		else:
			self.__class__._curColumnNumber -=1
		self.announceColumnContent(self._curColumnNumber)

	def script_firstColumn(self, gesture):
		self.__class__._curColumnNumber = 0
		self.announceColumnContent(self._curColumnNumber)

	def script_lastColumn(self, gesture):
		self.__class__._curColumnNumber = self.parent.columnCount-1
		self.announceColumnContent(self._curColumnNumber)

	@scriptHandler.script(
		# Translators: input help mode message for column explorer commands.
		description=_("Pressing once announces data for a track column, pressing twice will present column data in a browse mode window"),
		# 19.02: script decorator can take in a list of gestures, thus take advantage of it.
		gestures=["kb:control+nvda+%s"%(i) for i in six.moves.range(10)],
		category=_("StationPlaylist Studio"))
	def script_columnExplorer(self, gesture):
		# LTS: Just in case Control+NVDA+number row command is pressed...
		# Due to the below formula, columns explorer will be restricted to number commands.
		columnPos = int(gesture.displayName.split("+")[-1])-1
		header = self.exploreColumns[columnPos]
		column = self.indexOf(header)
		if column is not None:
			# #61 (18.06): pressed once will announce column data, twice will present it in a browse mode window.
			if scriptHandler.getLastScriptRepeatCount() == 0: self.announceColumnContent(column, header=header)
			else:
				columnContent = self._getColumnContentRaw(column)
				if columnContent is None:
					# Translators: presented when column information for a track is empty.
					columnContent = _("blank")
				ui.browseableMessage("{0}: {1}".format(header, columnContent),
					# Translators: Title of the column data window.
					title=_("Track data"))
		else:
			# Translators: Presented when a specific column header is not found.
			ui.message(_("{headerText} not found").format(headerText = header))

	__gestures={
		"kb:control+alt+home":"firstColumn",
		"kb:control+alt+end":"lastColumn",
	}

class SPLStudioTrackItem(SPLTrackItem):
	"""A base class for providing utility scripts when SPL Studio track entries are focused, such as location text and column navigation."""

	# Keep a record of which column is being looked at.
	_curColumnNumber = None

	# Locate the real column index for a column header.
	# This is response to a situation where columns were rearranged yet testing shows in-memory arrangement remains the same.
	# Subclasses must provide this function.
	def _origIndexOf(self, columnHeader):
		return None

	# Read selected columns.
	# But first, find where the requested column lives.
	# 8.0: Make this a public function.
	def indexOf(self, columnHeader):
		try:
			return self._origIndexOf(columnHeader)
		except ValueError:
			return None

	def reportFocus(self):
		# initialize column navigation tracker.
		if self.__class__._curColumnNumber is None: self.__class__._curColumnNumber = 0
		if splconfig.SPLConfig["General"]["CategorySounds"]:
			category = self._getColumnContentRaw(self.indexOf("Category"))
			if category in _SPLCategoryTones:
				tones.beep(_SPLCategoryTones[category], 50)
		# LTS: Comments please.
		if splconfig.SPLConfig["General"]["TrackCommentAnnounce"] != "off":
			self.announceTrackComment(0)
		# 6.3: Catch an unusual case where screen order is off yet column order is same as screen order and NvDA is told to announce all columns.
		# 17.04: Even if vertical column commands are performed, build description pieces for consistency.
		if splconfig._shouldBuildDescriptionPieces():
			descriptionPieces = []
			columnsToInclude = splconfig.SPLConfig["ColumnAnnouncement"]["IncludedColumns"]
			includeColumnHeaders = splconfig.SPLConfig["ColumnAnnouncement"]["IncludeColumnHeaders"]
			for header in splconfig.SPLConfig["ColumnAnnouncement"]["ColumnOrder"]:
				if header in columnsToInclude:
					index = self.indexOf(header)
					if index is None: continue # Header not found, mostly encountered in Studio 5.0x.
					content = self._getColumnContentRaw(index)
					if content:
						descriptionPieces.append("%s: %s"%(header, content) if includeColumnHeaders else content)
			self.description = ", ".join(descriptionPieces)
		if self.appModule._announceColumnOnly is None:
			super(IAccessible, self).reportFocus()
		else:
			self.appModule._announceColumnOnly = None
			verticalColumnAnnounce = splconfig.SPLConfig["General"]["VerticalColumnAnnounce"]
			if verticalColumnAnnounce == "Status" or (verticalColumnAnnounce is None and self._curColumnNumber == 0):
				self._leftmostcol()
			else:
				self.announceColumnContent(self._curColumnNumber if verticalColumnAnnounce is None else self.indexOf(verticalColumnAnnounce), header=verticalColumnAnnounce, reportStatus=self.name is not None)
		# 7.0: Let the app module keep a reference to this track.
		self.appModule._focusedTrack = self

	# A friendly way to report track position via location text.
	def _get_locationText(self):
		# Translators: location text for a playlist item (example: item 1 of 10).
		return _("Item {current} of {total}").format(current = self.IAccessibleChildID, total = splbase.studioAPI(0, 124))

	# #12 (18.04): select and set focus to this track.
	def doAction(self, index=None):
		splbase.selectTrack(self.IAccessibleChildID-1)
		self.setFocus(), self.setFocus()

	# Some helper functions to handle corner cases.
	# Each track item provides its own version.
	def _leftmostcol(self):
		pass

	# Obtain column contents for all columns for this track.
	# A convenience method that calls column content getter for a list of columns.
	# Readable flag will transform None into an empty string, suitable for output.
	# #61 (18.07): readable flag will become a string parameter to be used in columns viewer.
	def _getColumnContents(self, columns=None, readable=False):
		if columns is None:
			columns = list(six.moves.range(18))
		columnContents = [self._getColumnContentRaw(col) for col in columns]
		if readable:
			for pos in six.moves.range(len(columnContents)):
				if columnContents[pos] is None: columnContents[pos] = ""
		return columnContents

	# Announce column content if any.
	# 7.0: Add an optional header in order to announce correct header information in columns explorer.
	# 17.04: Allow checked status in 5.1x and later to be announced if this is such a case (vertical column navigation).)
	def announceColumnContent(self, colNumber, header=None, reportStatus=False):
		# #65 (18.08): use column header method (at least the method body) provided by the class itself.
		# This will work properly if the list (parent) is (or recognized as) SysListView32.List.
		columnHeader = header if header is not None else self._getColumnHeaderRaw(self.parent._columnOrderArray[colNumber])
		columnContent = self._getColumnContentRaw(self.indexOf(columnHeader))
		status = self.name + " " if reportStatus else ""
		if columnContent:
			# Translators: Standard message for announcing column content.
			if sys.version.startswith("3"): ui.message(str(_("{checkStatus}{header}: {content}")).format(checkStatus = status, header = columnHeader, content = columnContent))
			else: ui.message(unicode(_("{checkStatus}{header}: {content}")).format(checkStatus = status, header = columnHeader, content = columnContent))
		else:
			# Translators: Spoken when column content is blank.
			speech.speakMessage(_("{checkStatus}{header}: blank").format(checkStatus = status, header = columnHeader))
			# Translators: Brailled to indicate empty column content.
			braille.handler.message(_("{checkStatus}{header}: ()").format(checkStatus = status, header = columnHeader))

	# Now the scripts.
	# Because Studio track item requires special handling for status column, first and previous column scripts will be part of this and other subclasses here.

	def script_moveToPreviousColumn(self, gesture):
		if self._curColumnNumber <= 0:
			tones.beep(2000, 100)
		else:
			self.__class__._curColumnNumber -=1
		if self._curColumnNumber == 0:
			self._leftmostcol()
		else:
			self.announceColumnContent(self._curColumnNumber)

	def script_firstColumn(self, gesture):
		self.__class__._curColumnNumber = 0
		self._leftmostcol()

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

	def script_moveToNextRow(self, gesture):
		newTrack = self.next
		if newTrack is None and splconfig.SPLConfig["General"]["TopBottomAnnounce"]:
			tones.beep(2000, 100)
		else:
			self.appModule._announceColumnOnly = True
			newTrack._curColumnNumber = self._curColumnNumber
			newTrack.setFocus(), newTrack.setFocus()
			splbase.selectTrack(newTrack.IAccessibleChildID-1)

	def script_moveToPreviousRow(self, gesture):
		newTrack = self.previous
		if newTrack is None and splconfig.SPLConfig["General"]["TopBottomAnnounce"]:
			tones.beep(2000, 100)
		else:
			self.appModule._announceColumnOnly = True
			newTrack._curColumnNumber = self._curColumnNumber
			newTrack.setFocus(), newTrack.setFocus()
			splbase.selectTrack(newTrack.IAccessibleChildID-1)

	# Overlay class version of Columns Explorer.

	@property
	def exploreColumns(self):
		return splconfig.SPLConfig["General"]["ExploreColumns"]

	def script_trackColumnsViewer(self, gesture):
		# #61 (18.06): a direct copy of column data gatherer from playlist transcripts.
		# 18.07: just call the gatherer function with "blank" as the readable string and add column header afterwards.
		columns = list(six.moves.range(18))
		columnContents = [self._getColumnContentRaw(col) for col in columns]
		columnHeaders = ["Status"] + splconfig._SPLDefaults["ColumnAnnouncement"]["ColumnOrder"]
		for pos in six.moves.range(len(columnContents)):
			if columnContents[pos] is None: columnContents[pos] = "blank"
			# Manually add header text until column gatherer adds headers support.
			columnContents[pos] = ": ".join([columnHeaders[pos], columnContents[pos]])
		# Translators: Title of the column data window.
		ui.browseableMessage("\n".join(columnContents), title=_("Track data"))
	# Translators: input help mode message for columns viewer command.
	script_trackColumnsViewer.__doc__ = _("Presents data for all columns in the currently selected track")

	# Track comments.

	# Track comment announcer.
	# Levels indicate what should be done.
	# 0 indicates reportFocus, subsequent levels indicate script repeat count+1.
	def announceTrackComment(self, level):
		filename = self._getColumnContentRaw(self.indexOf("Filename"))
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
				# 16.12: timed break notes shows an odd value for filename (seconds in integers followed by a colon), potentially confusing users.)
				if filename and not filename.endswith(":"):
					self._trackCommentsEntry(filename, "")
				else:
					# Translators: Presented when focused on a track other than an actual track (such as hour marker).
					ui.message(_("Comments cannot be added to this kind of track"))

	# A proxy function to call the track comments entry dialog.
	def _trackCommentsEntry(self, filename, comment):
		dlg = wx.TextEntryDialog(gui.mainFrame,
		_("Track comment"),
		# Translators: The title of the track comments dialog.
		_("Track comment"), value=comment)
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
		"kb:downArrow":"nextTrack",
		"kb:upArrow":"prevTrack",
		"kb:control+NVDA+-":"trackColumnsViewer",
		"kb:Alt+NVDA+C":"announceTrackComment"
	}

class SPL510TrackItem(SPLStudioTrackItem):
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
		return splconfig._SPLDefaults["ColumnAnnouncement"]["ColumnOrder"].index(columnHeader)+1

	# Handle column announcement for SPL 5.10.
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
1 through 0: Announce columns via Columns Explorer (0 is tenth column slot).
F8: Take playlist snapshots such as track count, longest track and so on.
Shift+F8: Obtain playlist transcripts in a variety of formats.
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
1 through 0: Announce columns via Columns Explorer (0 is tenth column slot).
F8: Take playlist snapshots such as track count, longest track and so on.
Shift+F8: Obtain playlist transcripts in a variety of formats.
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
1 through 0: Announce columns via Columns Explorer (0 is tenth column slot).
F8: Take playlist snapshots such as track count, longest track and so on.
Shift+F8: Obtain playlist transcripts in a variety of formats.
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
		for index in six.moves.range(childCount-1, -1, -1):
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

# Temporary Cue time pickers does not expose the correct tree.
# Thankfully, when up or down arrows are pressed, display text changes.
class SPLTimePicker(IAccessible):

	def script_changeTimePickerValue(self, gesture):
		gesture.send()
		import treeInterceptorHandler
		obj=api.getFocusObject()
		treeInterceptor=obj.treeInterceptor
		if isinstance(treeInterceptor,treeInterceptorHandler.DocumentTreeInterceptor) and not treeInterceptor.passThrough:
			obj=treeInterceptor
		try:
			info=obj.makeTextInfo(textInfos.POSITION_CARET)
		except (NotImplementedError, RuntimeError):
			info=obj.makeTextInfo(textInfos.POSITION_FIRST)
		info.expand(textInfos.UNIT_LINE)
		speech.speakTextInfo(info,unit=textInfos.UNIT_LINE,reason=controlTypes.REASON_CARET)

	__gestures={
		"kb:upArrow":"changeTimePickerValue",
		"kb:downArrow":"changeTimePickerValue"
	}


class AppModule(appModuleHandler.AppModule):

	# Translators: Script category for Station Playlist commands in input gestures dialog.
	scriptCategory = _("StationPlaylist Studio")
	SPLCurVersion = appModuleHandler.AppModule.productVersion
	_focusedTrack = None
	_announceColumnOnly = None # Used only if vertical column navigation commands are used.
	_SPLStudioMonitor = None # Monitor Studio API routines.

	# Prepare the settings dialog among other things.
	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		if self.SPLCurVersion < SPLMinVersion:
			raise RuntimeError("Unsupported version of Studio is running, exiting app module")
		debugOutput("Using SPL Studio version %s"%self.SPLCurVersion)
		# #84: if foreground object is defined, this is a true Studio start, otherwise this is an NVDA restart with Studio running.
		# The latter is possible because app module constructor can run before NVDA finishes initializing, particularly if system focus is located somewhere other than Taskbar.
		# Note that this is an internal implementation detail and is subject to change without notice.
		debugOutput("Studio is starting" if api.getForegroundObject() is not None else "Studio is already running")
		# 17.09: do this if minimal startup flag is not present.
		try:
			if not globalVars.appArgs.minimal:
				# Translators: The sign-on message for Studio app module.
				ui.message(_("Using SPL Studio version {SPLVersion}").format(SPLVersion = self.SPLCurVersion))
		except:
			pass
		# #40 (17.12): react to profile switches.
		# #94 (19.03/18.09.7-LTS): also listen to profile reset action.
		splactions.SPLActionProfileSwitched.register(self.actionProfileSwitched)
		splactions.SPLActionSettingsReset.register(self.actionSettingsReset)
		debugOutput("loading add-on settings")
		splconfig.initialize()
		# Announce status changes while using other programs.
		# This requires NVDA core support and will be available in 6.0 and later (cannot be ported to earlier versions).
		# For now, handle all background events, but in the end, make this configurable.
		import eventHandler
		eventHandler.requestEvents(eventName="nameChange", processId=self.processID, windowClassName="TStatusBar")
		eventHandler.requestEvents(eventName="nameChange", processId=self.processID, windowClassName="TStaticText")
		# Also for requests window.
		eventHandler.requestEvents(eventName="show", processId=self.processID, windowClassName="TRequests")
		self.backgroundStatusMonitor = True
		debugOutput("preparing GUI subsystem")
		try:
			self.prefsMenu = gui.mainFrame.sysTrayIcon.preferencesMenu
			self.SPLSettings = self.prefsMenu.Append(wx.ID_ANY, _("SPL Studio Settings..."), _("SPL settings"))
			gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, splconfui.onConfigDialog, self.SPLSettings)
		except AttributeError:
			debugOutput("failed to initialize GUI subsystem")
			self.prefsMenu = None
		# #82 (18.11/18.09.5-lts): notify others when Studio window gets focused the first time in order to synchronize announcement order.
		self._initStudioWindowFocused = threading.Event()
		# Let me know the Studio window handle.
		# 6.1: Do not allow this thread to run forever (seen when evaluation times out and the app module starts).
		self.noMoreHandle = threading.Event()
		debugOutput("locating Studio window handle")
		# If this is started right away, foreground and focus objects will be NULL according to NVDA if NVDA restarts while Studio is running.
		t= threading.Thread(target=self._locateSPLHwnd)
		wx.CallAfter(t.start)
		# Display startup dialogs if any.
		# 17.10: not when minimal startup flag is set.
		# 18.08.1: sometimes, wxPython 4 says wx.App isn't ready.
		try:
			if not globalVars.appArgs.minimal: wx.CallAfter(splconfig.showStartupDialogs)
		except:
			pass

	# Locate the handle for main window for caching purposes.
	def _locateSPLHwnd(self):
		hwnd = user32.FindWindowW(u"SPLStudio", None)
		while not hwnd:
			time.sleep(1)
			# If the demo copy expires and the app module begins, this loop will spin forever.
			# Make sure this loop catches this case.
			if self.noMoreHandle.isSet():
				self.noMoreHandle.clear()
				self.noMoreHandle = None
				return
			hwnd = user32.FindWindowW(u"SPLStudio", None)
		# Only this thread will have privilege of notifying handle's existence.
		with threading.Lock() as hwndNotifier:
			splbase._SPLWin = hwnd
			debugOutput("Studio handle is %s"%hwnd)
		# #41 (18.04): start background monitor.
		# 18.08: unless Studio is exiting.
		try:
			self._SPLStudioMonitor = wx.PyTimer(self.studioAPIMonitor)
			wx.CallAfter(self._SPLStudioMonitor.Start, 1000)
		except:
			pass
		# Remind me to broadcast metadata information.
		# 18.04: also when delayed action is needed because metadata action handler couldn't locate Studio handle itself.
		if splconfig.SPLConfig["General"]["MetadataReminder"] == "startup" or splmisc._delayMetadataAction:
			splmisc._delayMetadataAction = False
			# If told to remind and connect, metadata streaming will be enabled at this time.
			# 6.0: Call Studio API twice - once to set, once more to obtain the needed information.
			# 6.2/7.0: When Studio API is called, add the value into the stream count list also.
			# 17.11: call the connector.
			splmisc.metadataConnector()
			# #40 (18.02): call the internal announcer in order to not hold up action handler queue.
			# #51 (18.03/15.14-LTS): if this is called within two seconds (status time-out), status will be announced multiple times.
			# 18.04: hopefully the error message won't be shown as this is supposed to run right after locating Studio handle.
			# #82 (18.11/18.09.5-lts): wait until Studio window shows up (foreground or background) for the first time.
			# #83: if NVDA restarts while Studio is running and foreground window is something other than playlist viewer, the below method won't work at all.
			# Thankfully, NVDA's notion of foreground window depends on a global variable, and if it is not set, this is a restart with Studio running, so just announce it.
			if api.getForegroundObject() is not None:
				self._initStudioWindowFocused.wait()
			splmisc._earlyMetadataAnnouncerInternal(splmisc.metadataStatus(), startup=True)

	# Studio API heartbeat.
	# Although useful for library scan detection, it can be extended to cover other features.

	def studioAPIMonitor(self):
		# Only proceed if Studio handle is valid.
		if not user32.FindWindowW(u"SPLStudio", None):
			if self._SPLStudioMonitor is not None:
				self._SPLStudioMonitor.Stop()
				self._SPLStudioMonitor = None
				return
		# #41 (18.04): background library scan detection.
		# Thankfully, current lib scan reporter function will not proceed when library scan is happening via Insert Tracks dialog.
		# #92 (19.01.1/18.09.7-LTS): if Studio dies, zero will be returned, so check for window handle once more.
		if splbase.studioAPI(1, 32) >= 0:
			if not user32.FindWindowW(u"SPLStudio", None): return
			if not self.libraryScanning: self.script_libraryScanMonitor(None)
		# #86 (18.12/18.09.6-LTS): certain internal markers require presence of a playlist, otherwise unexpected things may happen.
		if not splbase.studioAPI(0, 124):
			if self._focusedTrack is not None: self._focusedTrack = None
			if self._analysisMarker is not None: self._analysisMarker = None

	# Let the global plugin know if SPLController passthrough is allowed.
	def SPLConPassthrough(self):
		return splconfig.SPLConfig["Advanced"]["SPLConPassthrough"]

	# Can the global plugin use pilot features?
	def SPLUtilsPilotFeatures(self):
		return splconfig.SPLConfig.testDrive

	# The only job of the below event is to notify others that Studio window has appeared for the first time.
	# This is used to coordinate various status announcements.

	def event_foreground(self, obj, nextHandler):
		if not self._initStudioWindowFocused.isSet() and obj.windowClassName == "TStudioForm":
			self._initStudioWindowFocused.set()
		nextHandler()

	def event_NVDAObject_init(self, obj):
		# From 0.01: previously focused item fires focus event when it shouldn't.
		if obj.windowClassName == "TListView" and obj.role in (controlTypes.ROLE_CHECKBOX, controlTypes.ROLE_LISTITEM) and controlTypes.STATE_FOCUSED not in obj.states:
			obj.shouldAllowIAccessibleFocusEvent = False
		# Radio button group names are not recognized as grouping, so work around this.
		elif obj.windowClassName == "TRadioGroup":
			obj.role = controlTypes.ROLE_GROUPING
		# In certain edit fields and combo boxes, the field name is written to the screen, and there's no way to fetch the object for this text. Thus use review position text.
		elif obj.windowClassName in ("TEdit", "TComboBox") and not obj.name:
			import review
			fieldName, fieldObj  = review.getScreenPosition(obj)
			fieldName.expand(textInfos.UNIT_LINE)
			if obj.windowClassName == "TComboBox":
				obj.name = fieldName.text.replace(obj.windowText, "")
			else:
				obj.name = fieldName.text

	# Some controls which needs special routines.
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		role = obj.role
		try:
			windowStyle = obj.windowStyle
		except AttributeError:
			windowStyle = 0
		if obj.windowClassName == "TTntListView.UnicodeClass":
			if role == controlTypes.ROLE_LISTITEM:
				# Track item window style has changed in Studio 5.31.
				trackItemWindowStyle = 1443991617 if self.productVersion >= "5.31" else 1443991625
				if abs(windowStyle - trackItemWindowStyle)%0x100000 == 0:
					clsList.insert(0, SPL510TrackItem)
			# #69 (18.08): allow actual list views to be treated as SysListView32.List so column count and other data can be retrieved easily.
			elif role == controlTypes.ROLE_LIST:
				clsList.insert(0, sysListView32.List)
		# 7.2: Recognize known dialogs.
		elif obj.windowClassName in ("TDemoRegForm", "TOpenPlaylist"):
			clsList.insert(0, Dialog)
		# For About dialog in Studio 5.1x and later.
		elif obj.windowClassName == "TAboutForm" and self.SPLCurVersion >= "5.1":
			clsList.insert(0, ReversedDialog)
		# Temporary cue time picker and friends.
		elif obj.windowClassName == "TDateTimePicker":
			clsList.insert(0, SPLTimePicker)

	# Keep an eye on library scans in insert tracks window.
	libraryScanning = False
	scanCount = 0
	# Prevent NVDA from announcing scheduled time multiple times.
	scheduledTimeCache = ""

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
						if self.productVersion not in noLibScanMonitor: self.libraryScanning = True
				elif "match" in obj.name:
					if splconfig.SPLConfig["General"]["LibraryScanAnnounce"] != "off" and self.libraryScanning:
						if splconfig.SPLConfig["General"]["BeepAnnounce"]: tones.beep(370, 100)
						else:
							# Translators: Presented when library scan is complete.
							ui.message(_("Scan complete with {scanCount} items").format(scanCount = obj.name.split()[3]))
					if self.libraryScanning: self.libraryScanning = False
					self.scanCount = 0
			else:
				# 16.12: Because cart edit text shows cart insert status, exclude this from toggle state announcement.
				if obj.name.endswith((" On", " Off")) and not obj.name.startswith("Cart "):
					self._toggleMessage(obj.name)
				else:
					ui.message(obj.name)
				if self.cartExplorer or splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarm"]:
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
		# Be sure to only deal with cart mode changes if Cart Explorer is on.
		# Optimization: Return early if the below condition is true.
		if self.cartExplorer and status.startswith("Cart") and status.endswith((" On", " Off")):
			# 17.01: The best way to detect Cart Edit off is consulting file modification time.
			# Automatically reload cart information if this is the case.
			if status in ("Cart Edit Off", "Cart Insert On"):
				self.carts = splmisc.cartExplorerRefresh(api.getForegroundObject().name, self.carts)
			# Translators: Presented when cart modes are toggled while cart explorer is on.
			ui.message(_("Cart explorer is active"))
			return
		# Microphone alarm and alarm interval if defined.
		global micAlarmT, micAlarmT2
		micAlarm = splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarm"]
		# #38 (17.11/15.10-lts): only enter microphone alarm area if alarm should be turned on.
		if not micAlarm:
			if micAlarmT is not None: micAlarmT.cancel()
			micAlarmT = None
			if micAlarmT2 is not None: micAlarmT2.Stop()
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
				if micAlarmT is not None: micAlarmT.cancel()
				micAlarmT = None
				if micAlarmT2 is not None: micAlarmT2.Stop()
				micAlarmT2 = None

	# Respond to profile switches if asked.
	def actionProfileSwitched(self):
		# #38 (17.11/15.10-LTS): obtain microphone alarm status.
		if splbase._SPLWin is not None: self.doExtraAction(self.sayStatus(2, statusText=True))

	def actionSettingsReset(self, factoryDefaults=False):
		global micAlarmT, micAlarmT2
		# Regardless of factory defaults flag, turn off microphone alarm timers.
		if micAlarmT is not None: micAlarmT.cancel()
		micAlarmT = None
		if micAlarmT2 is not None: micAlarmT2.Stop()
		micAlarmT2 = None
		if splbase._SPLWin is not None: self.doExtraAction(self.sayStatus(2, statusText=True))

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

	# React to show events from certain windows.

	def event_show(self, obj, nextHandler):
		if obj.windowClassName == "TRequests" and splconfig.SPLConfig["General"]["RequestsAlert"]:
			nvwave.playWaveFile(os.path.join(os.path.dirname(__file__), "SPL_Requests.wav"))
		nextHandler()

	# Save configuration and perform other tasks when terminating.
	def terminate(self):
		super(AppModule, self).terminate()
		debugOutput("terminating app module")
		# 6.3: Memory leak results if encoder flag sets and other encoder support maps aren't cleaned up.
		# This also could have allowed a hacker to modify the flags set (highly unlikely) so NvDA could get confused next time Studio loads.
		if "globalPlugins.splUtils.encoders" in sys.modules:
			import globalPlugins.splUtils.encoders
			globalPlugins.splUtils.encoders.cleanup()
		# #39 (17.11/15.10-lts): terminate microphone alarm/interval threads, otherwise errors are seen.
		# #40 (17.12): replace this with a handler that responds to app module exit signal.
		# Also allows profile switch handler to unregister itself as well.
		# At the same time, close any opened SPL add-on dialogs.
		splactions.SPLActionProfileSwitched.unregister(self.actionProfileSwitched)
		splactions.SPLActionSettingsReset.unregister(self.actionSettingsReset)
		splactions.SPLActionAppTerminating.notify()
		debugOutput("closing microphone alarm/interval thread")
		global micAlarmT, micAlarmT2
		if micAlarmT is not None: micAlarmT.cancel()
		micAlarmT = None
		if micAlarmT2 is not None: micAlarmT2.Stop()
		micAlarmT2 = None
		debugOutput("saving add-on settings")
		splconfig.terminate()
		# reset column number for column navigation commands.
		if self._focusedTrack: self._focusedTrack.__class__._curColumnNumber = None
		# Delete focused track reference.
		self._focusedTrack = None
		# #86: track time analysis marker should be gone, too.
		self._analysisMarker = None
		# #41: We're done monitoring Studio API.
		if self._SPLStudioMonitor is not None:
			self._SPLStudioMonitor.Stop()
			self._SPLStudioMonitor = None
		# #54 (18.04): no more PyDeadObjectError in wxPython 4, so catch ALL exceptions until NVDA stable release with wxPython 4 is out.
		# 18.08: call appropriate Remove function based on wxPython version in use.
		# 18.09: use wx.Menu.Remove directly.
		try:
			self.prefsMenu.Remove(self.SPLSettings)
		except: #(RuntimeError, AttributeError):
			pass
		# Tell the handle finder thread it's time to leave this world.
		self.noMoreHandle.set()
		# Manually clear the following dictionaries.
		self.carts.clear()
		self._cachedStatusObjs.clear()
		# Don't forget to reset timestamps for cart files.
		splmisc._cartEditTimestamps = [0, 0, 0, 0]
		# Just to make sure:
		if splbase._SPLWin: splbase._SPLWin = None
		# 17.10: remove add-on specific command-line switches.
		# This is necessary in order to restore full config functionality when NVDA restarts.
		for cmdSwitch in globalVars.appArgsExtra:
			if cmdSwitch.startswith("--spl-"): globalVars.appArgsExtra.remove(cmdSwitch)

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
				# 17.08: Return the generated string directly.
				# 17.09: use modulo formatter to reduce instruction count.
				return "{hh:02d}:{mm:02d}:{ss:02d}".format(hh = hh, mm = mm, ss = ss)
			else:
				return "{mm:02d}:{ss:02d}".format(mm = mm, ss = ss)

	# Scripts which rely on API.
	def script_sayRemainingTime(self, gesture):
		if splbase.studioIsRunning(): self.announceTime(splbase.studioAPI(3, 105), offset=1)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayRemainingTime.__doc__=_("Announces the remaining track time.")

	def script_sayElapsedTime(self, gesture):
		if splbase.studioIsRunning(): self.announceTime(splbase.studioAPI(0, 105))
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayElapsedTime.__doc__=_("Announces the elapsed time for the currently playing track.")

	def script_sayBroadcasterTime(self, gesture):
		if not splbase.studioIsRunning(): return
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
				if h == 0: h+=12
				# Messages in this method should not be translated.
				ui.message("{hour} o'clock".format(hour = h))
			elif 1 <= m <= 30:
				if h == 0: h+=12
				ui.message("{minute} min past {hour}".format(minute = m, hour = h))
			else:
				if h == 12: h = 1
				m = 60-m
				ui.message("{minute} min to {hour}".format(minute = m, hour = h+1))
		else:
			self.announceTime(3600-(m*60+localtime[5]), ms=False)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayBroadcasterTime.__doc__=_("Announces broadcaster time. If pressed twice, reports minutes and seconds left to top of the hour.")

	def script_sayCompleteTime(self, gesture):
		if not splbase.studioIsRunning(): return
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
			wx.CallAfter(gui.messageBox, _("The add-on settings dialog is opened. Please close the settings dialog first."), translate("Error"), wx.OK|wx.ICON_ERROR)
			return
		try:
			d = splconfui.AlarmsCenter(gui.mainFrame, level)
			gui.mainFrame.prePopup()
			d.Raise()
			d.Show()
			gui.mainFrame.postPopup()
			splconfui._alarmDialogOpened = True
		except RuntimeError:
			wx.CallAfter(splconfig._alarmError)

	# Set the end of track alarm time between 1 and 59 seconds.

	def script_setEndOfTrackTime(self, gesture):
		self.alarmDialog(1)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_setEndOfTrackTime.__doc__=_("Sets end of track alarm (default is 5 seconds).")

	# Set song ramp (introduction) time between 1 and 9 seconds.

	def script_setSongRampTime(self, gesture):
		self.alarmDialog(2)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_setSongRampTime.__doc__=_("Sets song intro alarm (default is 5 seconds).")

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
	# 17.08: now it is a list that records search history.
	findText = None

	def trackFinder(self, text, obj, directionForward=True, column=None):
		speech.cancelSpeech()
		# #32 (17.06/15.8 LTS): Update search text even if the track with the search term in columns does not exist.
		# #27 (17.08): especially if the search history is empty.
		# Thankfully, track finder dialog will populate the first item, but it is better to check a second time for debugging purposes.
		if self.findText is None: self.findText = []
		if text not in self.findText: self.findText.insert(0, text)
		# #33 (17.06/15.8-LTS): In case the track is NULL (seen when attempting to perform forward search from the last track and what not), this function should fail instead of raising attribute error.
		if obj is not None and column is None:
			column = [obj.indexOf("Artist"), obj.indexOf("Title")]
		track = self._trackLocator(text, obj=obj, directionForward=directionForward, columns=column)
		if track:
			# We need to fire set focus event twice and exit this routine (return if 5.0x).
			# 16.10.1/15.2 LTS: Just select this track in order to prevent a dispute between NVDA and SPL in regards to focused track.
			# 16.11: Call setFocus if it is post-5.01, as SPL API can be used to select the desired track.
			splbase.selectTrack(track.IAccessibleChildID-1)
			track.setFocus(), track.setFocus()
		else:
			wx.CallAfter(gui.messageBox,
			# Translators: Standard dialog message when an item one wishes to search is not found (copy this from main nvda.po).
			_("Search string not found."),
			translate("Find Error"),wx.OK|wx.ICON_ERROR)

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
				columnText = obj._getColumnContentRaw(column)
				if columnText and text in columnText:
					return obj
			obj = getattr(obj, nextTrack)
		return None

	# Find a specific track based on a searched text.
	# But first, check if track finder can be invoked.
	# Attempt level specifies which track finder to open (0 = Track Finder, 1 = Column Search, 2 = Time range).
	def _trackFinderCheck(self, attemptLevel):
		if not splbase.studioIsRunning(): return False
		playlistErrors = self.canPerformPlaylistCommands(announceErrors=False)
		if playlistErrors == self.SPLPlaylistNotFocused:
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
		# 17.06/15.8-LTS: use Studio API to find out if a playlist is even loaded, otherwise Track Finder will fail to notice a playlist.
		# #81 (18.12): all taken care of by playlist checker method.
		elif playlistErrors == self.SPLPlaylistNotLoaded:
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
			startObj =  api.getFocusObject()
			if api.getForegroundObject().windowClassName == "TStudioForm" and startObj.role == controlTypes.ROLE_LIST:
				startObj = startObj.firstChild
			d = splmisc.SPLFindDialog(gui.mainFrame, startObj, self.findText[0] if self.findText and len(self.findText) else "", title, columnSearch = columnSearch)
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
			if self.findText is None: self.trackFinderGUI()
			else:
				startObj = api.getFocusObject()
				if api.getForegroundObject().windowClassName == "TStudioForm" and startObj.role == controlTypes.ROLE_LIST:
					startObj = startObj.firstChild
				self.trackFinder(self.findText[0], obj=startObj.next)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_findTrackNext.__doc__=_("Finds the next occurrence of the track with the name in the track list.")

	def script_findTrackPrevious(self, gesture):
		if self._trackFinderCheck(0):
			if self.findText is None: self.trackFinderGUI()
			else:
				startObj = api.getFocusObject()
				if api.getForegroundObject().windowClassName == "TStudioForm" and startObj.role == controlTypes.ROLE_LIST:
					startObj = startObj.lastChild
				self.trackFinder(self.findText[0], obj=startObj.previous, directionForward=False)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_findTrackPrevious.__doc__=_("Finds previous occurrence of the track with the name in the track list.")

	# Time range finder.
	# Locate a track with duration falling between min and max.

	def script_timeRangeFinder(self, gesture):
		if self._trackFinderCheck(2):
			try:
				d = splmisc.SPLTimeRangeDialog(gui.mainFrame, api.getFocusObject())
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
		for i in six.moves.range(12):
			self.bindGesture("kb:f%s"%(i+1), "cartExplorer")
			self.bindGesture("kb:shift+f%s"%(i+1), "cartExplorer")
			self.bindGesture("kb:control+f%s"%(i+1), "cartExplorer")
			self.bindGesture("kb:alt+f%s"%(i+1), "cartExplorer")

	def buildNumberCarts(self):
		# It is much faster to work directly with number row keys.
		for i in "1234567890-=":
			self.bindGesture("kb:%s"%(i), "cartExplorer")
			self.bindGesture("kb:shift+%s"%(i), "cartExplorer")
			self.bindGesture("kb:control+%s"%(i), "cartExplorer")
			self.bindGesture("kb:alt+%s"%(i), "cartExplorer")

	def cartsBuilder(self, build=True):
		# A function to build and return cart commands.
		if build:
			self.buildFNCarts()
			self.buildNumberCarts()
		else:
			self.clearGestureBindings()
			self.bindGestures(self.__gestures)

	def script_toggleCartExplorer(self, gesture):
		if not splbase.studioIsRunning(): return
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
			splmisc._cartEditTimestamps = None
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
			ui.message(_("Scan start")) if not splconfig.SPLConfig["General"]["BeepAnnounce"] else tones.beep(740, 100)
			if self.productVersion not in noLibScanMonitor: self.libraryScanning = True

	# Report library scan (number of items scanned) in the background.
	def monitorLibraryScan(self):
		global libScanT
		if libScanT and libScanT.isAlive() and api.getForegroundObject().windowClassName == "TTrackInsertForm":
			return
		if splbase.studioAPI(1, 32) < 0:
			self.libraryScanning = False
			return
		time.sleep(0.1)
		if api.getForegroundObject().windowClassName == "TTrackInsertForm" and self.productVersion in noLibScanMonitor:
			self.libraryScanning = False
			return
		# 17.04: Library scan may have finished while this thread was sleeping.
		if splbase.studioAPI(1, 32) < 0:
			self.libraryScanning = False
			# Translators: Presented when library scanning is finished.
			ui.message(_("{itemCount} items in the library").format(itemCount = splbase.studioAPI(0, 32)))
		else:
			libScanT = threading.Thread(target=self.libraryScanReporter)
			libScanT.daemon = True
			libScanT.start()

	def libraryScanReporter(self):
		scanIter = 0
		# 17.04: Use the constant directly, as 5.10 and later provides a convenient method to detect completion of library scans.
		scanCount = splbase.studioAPI(1, 32)
		while scanCount >= 0:
			if not self.libraryScanning or not user32.FindWindowW(u"SPLStudio", None): return
			time.sleep(1)
			# Do not continue if we're back on insert tracks form or library scan is finished.
			if api.getForegroundObject().windowClassName == "TTrackInsertForm" or not self.libraryScanning:
				return
			# Scan count may have changed during sleep.
			scanCount = splbase.studioAPI(1, 32)
			if scanCount < 0:
				break
			scanIter+=1
			if scanIter%5 == 0 and splconfig.SPLConfig["General"]["LibraryScanAnnounce"] not in ("off", "ending"):
				self._libraryScanAnnouncer(scanCount, splconfig.SPLConfig["General"]["LibraryScanAnnounce"])
		self.libraryScanning = False
		# 18.04: what if config database died?
		if splconfig.SPLConfig and splconfig.SPLConfig["General"]["LibraryScanAnnounce"] != "off":
			if splconfig.SPLConfig["General"]["BeepAnnounce"]:
				tones.beep(370, 100)
			else:
				# Translators: Presented after library scan is done.
				ui.message(_("Scan complete with {itemCount} items").format(itemCount = splbase.studioAPI(0, 32)))

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
		filename = track._getColumnContentRaw(index)
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

	# The script version to open the manage metadata URL's dialog.
	def script_manageMetadataStreams(self, gesture):
		# Do not even think about opening this dialog if handle to Studio isn't found.
		if splbase._SPLWin is None:
			# Translators: Presented when streaming dialog cannot be shown.
			ui.message(_("Cannot open metadata streaming dialog"))
			return
		if splconfui._configDialogOpened or splconfui._metadataDialogOpened:
			# Translators: Presented when the add-on config dialog is opened.
			wx.CallAfter(gui.messageBox, _("The add-on settings dialog or the metadata streaming dialog is opened. Please close the opened dialog first."), translate("Error"), wx.OK|wx.ICON_ERROR)
			return
		try:
			# #44 (18.02): do not rely on Studio API function object as its workings (including arguments) may change.
			# Use a flag to tell the streaming dialog that this is invoked from somewhere other than add-on settings dialog.
			d = splconfui.MetadataStreamingDialog(gui.mainFrame, configDialogActive=False)
			gui.mainFrame.prePopup()
			d.Raise()
			d.Show()
			gui.mainFrame.postPopup()
			splconfui._metadataDialogOpened = True
		except RuntimeError:
			wx.CallAfter(splconfig._alarmError)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_manageMetadataStreams.__doc__=_("Opens a dialog to quickly enable or disable metadata streaming.")

	# Playlist Analyzer
	# These include track time analysis, playlist snapshots, and some form of playlist transcripts and others.
	# Although not directly related to this, track finder and its friends, as well as remaining playlist duration command also fall under playlist analyzer.
	# A playlist must be loaded and visible in order for these to work, or for some, most recent focused track must be known.

	# Possible playlist errors.
	SPLPlaylistNoErrors = 0
	SPLPlaylistNotFocused = 1
	SPLPlaylistNotLoaded = 2
	SPLPlaylistLastFocusUnknown = 3

	def canPerformPlaylistCommands(self, playlistViewerRequired=True, mustSelectTrack=False, announceErrors=True):
		# #81: most commands do require that playlist viewer must be the foreground window (focused), hence the keyword argument.
		# Also let NvDA announce generic error messages listed below if told to do so, and for some cases, not at all because the caller will announce them.
		playlistViewerFocused = api.getForegroundObject().windowClassName == "TStudioForm"
		if playlistViewerRequired and not playlistViewerFocused:
			# Translators: an error message presented when performing some playlist commands while focused on places other than Playlist Viewer.
			if announceErrors: ui.message(_("Please return to playlist viewer before invoking this command."))
			return self.SPLPlaylistNotFocused
		if not splbase.studioAPI(0, 124):
			# Translators: an error message presented when performing some playlist commands while no playlist has been loaded.
			if announceErrors: ui.message(_("No playlist has been loaded."))
			return self.SPLPlaylistNotLoaded
		if mustSelectTrack and self._focusedTrack is None:
			# Translators: an error message presented when performing some playlist commands while no tracks are selected/focused.
			if announceErrors: ui.message(_("Please select a track from playlist viewer before invoking this command."))
			return self.SPLPlaylistLastFocusUnknown
		return self.SPLPlaylistNoErrors

	# Track time analysis/Playlist snapshots
	# Return total length of the selected tracks upon request.
	# Analysis command (SPL Assistant) will be assignable.
	# Also gather various data about the playlist.
	_analysisMarker = None

	# Trakc time analysis and playlist snapshots, and to some extent, some parts of playlist transcripts  require main playlist viewer to be the foreground window.
	# Track time analysis does require knowing the start and ending track, while others do not.
	def _trackAnalysisAllowed(self, mustSelectTrack=True):
		if not splbase.studioIsRunning():
			return False
		# #81 (18.12): just return result of consulting playlist dispatch along with error messages if any.
		playlistErrors = self.canPerformPlaylistCommands(mustSelectTrack=mustSelectTrack, announceErrors=False)
		if playlistErrors == self.SPLPlaylistNotFocused:
			# Translators: Presented when playlist analyzer cannot be performed because user is not focused on playlist viewer.
			ui.message(_("Not in playlist viewer, cannot perform playlist analysis."))
			return False
		elif playlistErrors == self.SPLPlaylistNotLoaded:
			# Translators: reported when no playlist has been loaded when trying to perform playlist analysis.
			ui.message(_("No playlist to analyze."))
			return False
		elif playlistErrors == self.SPLPlaylistLastFocusUnknown:
			# Translators: Presented when playlist analysis cannot be activated.
			ui.message(_("No tracks are selected, cannot perform playlist analysis."))
			return False
		return True

	# Return total duration of a range of tracks.
	# This is used in track time analysis when multiple tracks are selected.
	# This is also called from playlist duration scripts.
	def playlistDuration(self, start=None, end=None):
		if start is None: start = api.getFocusObject()
		duration = start.indexOf("Duration")
		totalDuration = 0
		obj = start
		while obj not in (None, end):
			# Technically segue.
			segue = obj._getColumnContentRaw(duration)
			if segue not in (None, "00:00"):
				hms = segue.split(":")
				totalDuration += (int(hms[-2])*60) + int(hms[-1])
				if len(hms) == 3: totalDuration += int(hms[0])*3600
			obj = obj.next
		return totalDuration

	# Segue version of this will be used in some places (the below is the raw duration).)
	def playlistDurationRaw(self, start, end):
		# Take care of errors such as the following.
		if start < 0 or end > splbase.studioAPI(0, 124)-1:
			raise ValueError("Track range start or end position out of range")
			return
		totalLength = 0
		if start == end:
			filename = splbase.studioAPI(start, 211)
			totalLength = splbase.studioAPI(filename, 30)
		else:
			for track in six.moves.range(start, end+1):
				filename = splbase.studioAPI(track, 211)
				totalLength+=splbase.studioAPI(filename, 30)
		return totalLength

	# Playlist snapshots
	# Data to be gathered comes from a set of flags.
	# By default, playlist duration (including shortest and average), category summary and other statistics will be gathered.
	def playlistSnapshots(self, obj, end, snapshotFlags=None):
		# #55 (18.05): is this a complete snapshot?
		completePlaylistSnapshot = obj.IAccessibleChildID == 1 and end is None
		# Track count and total duration are always included.
		snapshot = {}
		if snapshotFlags is None:
			snapshotFlags = [flag for flag in splconfig.SPLConfig["PlaylistSnapshots"] if splconfig.SPLConfig["PlaylistSnapshots"][flag]]
		duration = obj.indexOf("Duration")
		title = obj.indexOf("Title")
		artist = obj.indexOf("Artist")
		artists = []
		min, max = None, None
		minTitle, maxTitle = None, None
		totalDuration = 0
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
			# Shortest and longest tracks.
			# #22: assign min to the first segue in order to not forget title of the shortest track.
			if segue and (min is None or segue < min):
				min = segue
				minTitle = trackTitle
			if segue and segue > max:
				max = segue
				maxTitle = trackTitle
			if segue not in (None, "00:00"):
				hms = segue.split(":")
				totalDuration += (int(hms[-2])*60) + int(hms[-1])
				if len(hms) == 3: totalDuration += int(hms[0])*3600
			obj = obj.next
		# #55 (18.05): use total track count if it is an entire playlist, if not, resort to categories count.
		if completePlaylistSnapshot: snapshot["PlaylistItemCount"] = splbase.studioAPI(0, 124)
		else: snapshot["PlaylistItemCount"] = len(categories)
		snapshot["PlaylistTrackCount"] = len(artists)
		snapshot["PlaylistDurationTotal"] = self._ms2time(totalDuration, ms=False)
		if "DurationMinMax" in snapshotFlags:
			snapshot["PlaylistDurationMin"] = "%s (%s)"%(minTitle, min)
			snapshot["PlaylistDurationMax"] = "%s (%s)"%(maxTitle, max)
		if "DurationAverage" in snapshotFlags:
			# #57 (18.04): zero division error may occur if the playlist consists of hour markers only.
			try:
				snapshot["PlaylistDurationAverage"] = self._ms2time(totalDuration/snapshot["PlaylistTrackCount"], ms=False)
			except ZeroDivisionError:
				snapshot["PlaylistDurationAverage"] = "00:00"
		if "CategoryCount" in snapshotFlags or "ArtistCount" in snapshotFlags or "GenreCount" in snapshotFlags:
			import collections
			if "CategoryCount" in snapshotFlags: snapshot["PlaylistCategoryCount"] = collections.Counter(categories)
			if "ArtistCount" in snapshotFlags: snapshot["PlaylistArtistCount"] = collections.Counter(artists)
			if "GenreCount" in snapshotFlags: snapshot["PlaylistGenreCount"] = collections.Counter(genres)
		return snapshot

	# Output formatter for playlist snapshots.
	# Pressing once will speak and/or braille it, pressing twice or more will output this info to an HTML file.

	def playlistSnapshotOutput(self, snapshot, scriptCount):
		# Translators: one of the results for playlist snapshots feature for announcing total number of items in a playlist.
		statusInfo = [_("Items: {playlistItemCount}").format(playlistItemCount = snapshot["PlaylistItemCount"])]
		# Translators: one of the results for playlist snapshots feature for announcing total number of tracks in a playlist.
		statusInfo.append(_("Tracks: {playlistTrackCount}").format(playlistTrackCount = snapshot["PlaylistTrackCount"]))
		# Translators: one of the results for playlist snapshots feature for announcing total duration of a playlist.
		statusInfo.append(_("Duration: {playlistTotalDuration}").format(playlistTotalDuration = snapshot["PlaylistDurationTotal"]))
		if "PlaylistDurationMin" in snapshot:
			# Translators: one of the results for playlist snapshots feature for announcing shortest track name and duration of a playlist.
			statusInfo.append(_("Shortest: {playlistShortestTrack}").format(playlistShortestTrack = snapshot["PlaylistDurationMin"]))
			# Translators: one of the results for playlist snapshots feature for announcing longest track name and duration of a playlist.
			statusInfo.append(_("Longest: {playlistLongestTrack}").format(playlistLongestTrack = snapshot["PlaylistDurationMax"]))
		if "PlaylistDurationAverage" in snapshot:
			# Translators: one of the results for playlist snapshots feature for announcing average duration for tracks in a playlist.
			statusInfo.append(_("Average: {playlistAverageDuration}").format(playlistAverageDuration = snapshot["PlaylistDurationAverage"]))
		if "PlaylistArtistCount" in snapshot:
			artistCount = splconfig.SPLConfig["PlaylistSnapshots"]["ArtistCountLimit"]
			artists = snapshot["PlaylistArtistCount"].most_common(None if not artistCount else artistCount)
			if scriptCount == 0:
				try:
					# Translators: one of the results for playlist snapshots feature for announcing top artist in a playlist.
					statusInfo.append(_("Top artist: %s (%s)")%(artists[0][:]))
				except IndexError:
					statusInfo.append(_("Top artist: none"))
			elif scriptCount == 1:
				artistList = []
				# Translators: one of the results for playlist snapshots feature, a heading for a group of items.
				header = _("Top artists:")
				for item in artists:
					artist, count = item
					if artist is None:
						info = _("No artist information ({artistCount})").format(artistCount = count)
					else:
						info = _("{artistName} ({artistCount})").format(artistName = artist, artistCount = count)
					artistList.append("<li>%s</li>"%info)
				statusInfo.append("".join([header, "<ol>", "\n".join(artistList), "</ol>"]))
		if "PlaylistCategoryCount" in snapshot:
			categoryCount = splconfig.SPLConfig["PlaylistSnapshots"]["CategoryCountLimit"]
			categories = snapshot["PlaylistCategoryCount"].most_common(None if not categoryCount else categoryCount)
			if scriptCount == 0:
				# Translators: one of the results for playlist snapshots feature for announcing top track category in a playlist.
				statusInfo.append(_("Top category: %s (%s)")%(categories[0][:]))
			elif scriptCount == 1:
				categoryList = []
				# Translators: one of the results for playlist snapshots feature, a heading for a group of items.
				header = _("Categories:")
				for item in categories:
					category, count = item
					category = category.replace("<", "")
					category = category.replace(">", "")
					info = _("{categoryName} ({categoryCount})").format(categoryName = category, categoryCount = count)
					categoryList.append("<li>%s</li>"%info)
				statusInfo.append("".join([header, "<ol>", "\n".join(categoryList), "</ol>"]))
		if "PlaylistGenreCount" in snapshot:
			genreCount = splconfig.SPLConfig["PlaylistSnapshots"]["GenreCountLimit"]
			genres = snapshot["PlaylistGenreCount"].most_common(None if not genreCount else genreCount)
			if scriptCount == 0:
				try:
					# Translators: one of the results for playlist snapshots feature for announcing top genre in a playlist.
					statusInfo.append(_("Top genre: %s (%s)")%(genres[0][:]))
				except IndexError:
					statusInfo.append(_("Top genre: none"))
			elif scriptCount == 1:
				genreList = []
				# Translators: one of the results for playlist snapshots feature, a heading for a group of items.
				header = _("Top genres:")
				for item in genres:
					genre, count = item
					if genre is None:
						info = _("No genre information ({genreCount})").format(genreCount = count)
					else:
						info = _("{genreName} ({genreCount})").format(genreName = genre, genreCount = count)
					genreList.append("<li>%s</li>"%info)
				statusInfo.append("".join([header, "<ol>", "\n".join(genreList), "</ol>"]))
		if scriptCount == 0:
			ui.message(", ".join(statusInfo))
		else:
			# Translators: The title of a window for displaying playlist snapshots information.
			ui.browseableMessage("<p>".join(statusInfo),title=_("Playlist snapshots"), isHtml=True)

	# Some handlers for native commands.

	# In Studio 5.0x, when deleting a track, NVDA announces wrong track item due to focus bouncing (not the case in 5.10 and later).
	# The below hack is sensitive to changes in NVDA core.
	deletedFocusObj = False

	@scriptHandler.script(gestures=["kb:Shift+delete", "kb:Shift+numpadDelete"])
	def script_deleteTrack(self, gesture):
		self.preTrackRemoval()
		gesture.send()

	# When Escape is pressed, activate background library scan if conditions are right.
	@scriptHandler.script(gesture="kb:escape")
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
			script = self.script_error
		# Just use finally function from the global plugin to reduce code duplication.
		import globalPlugins.splUtils
		return globalPlugins.splUtils.finally_(script, self.finish)

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
			if splbase._SPLWin is None:
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
			for i in six.moves.range(5):
				self.bindGesture("kb:%s"%(i), "columnExplorer")
				self.bindGesture("kb:shift+%s"%(i), "metadataEnabled")
			for i in six.moves.range(5, 10):
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
	SPLScheduledToPlay = 2
	SPLNextTrackTitle = 3
	SPLNextPlayer = 4
	SPLCurrentTrackTitle = 5
	SPLCurrentPlayer = 6
	SPLTemperature = 7
	SPLScheduled = 8

	# Table of child constants based on versions
	# These are scattered throughout the screen, so one can use foreground.getChild(index) to fetch them (getChild tip from Jamie Teh (NV Access)).
	# Because 5.x (an perhaps future releases) uses different screen layout, look up the needed constant from the table below (row = info needed, column = version).
	# As of 18.05, the below table is based on Studio 5.10.
	statusObjs={
		SPLPlayStatus: 6, # Play status, mic, etc.
		SPLSystemStatus: -2, # The second status bar containing system status such as up time.
		SPLScheduledToPlay: 19, # In case the user selects one or more tracks in a given hour.
		SPLScheduled: 20, # Time when the selected track will begin.
		SPLNextTrackTitle: 8, # Name and duration of the next track if any.
		SPLNextPlayer: 11, # Name and duration of the next track if any.
		SPLCurrentTrackTitle: 9, # Name of the currently playing track.
		SPLCurrentPlayer: 12, # Name of the currently playing track.
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
				# 17.08: several SPL Controller commands will use this route.
				fg = getNVDAObjectFromEvent(user32.FindWindowW(u"TStudioForm", None), OBJID_CLIENT, 0)
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
	def sayStatus(self, index, statusText=False):
		if self.SPLCurVersion < "5.20":
			status = self.status(self.SPLPlayStatus).getChild(index).name
		else:
			status = self._statusBarMessages[index][splbase.studioAPI(index, 39)]
		# #38 (17.11/15.10-LTS): return status text if asked.
		if statusText: return status
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
			cartEdit = splbase.studioAPI(5, 39)
			cartInsert = splbase.studioAPI(6, 39)
			if cartEdit: ui.message("Cart Edit On")
			elif not cartEdit and cartInsert: ui.message("Cart Insert On")
			else: ui.message("Cart Edit Off")
		else:
			ui.message(self.status(self.SPLPlayStatus).getChild(5).name)

	def script_sayHourTrackDuration(self, gesture):
		self.announceTime(splbase.studioAPI(0, 27))

	def script_sayHourRemaining(self, gesture):
		# 7.0: Split from playlist remaining script (formerly the playlist remainder command).
		self.announceTime(splbase.studioAPI(1, 27))

	def script_sayPlaylistRemainingDuration(self, gesture):
		if self.canPerformPlaylistCommands() == self.SPLPlaylistNoErrors:
			obj = api.getFocusObject()
			if obj.role == controlTypes.ROLE_LIST:
				obj = obj.firstChild
			self.announceTime(self.playlistDuration(start=obj), ms=False)

	def script_sayPlaylistModified(self, gesture):
		obj = self.status(self.SPLSystemStatus).getChild(5)
		# Translators: presented when playlist modification message isn't shown.
		ui.message(obj.name if obj.name else _("Playlist modification not available"))

	def script_sayNextTrackTitle(self, gesture):
		if not splbase.studioIsRunning():
			self.finish()
			return
		try:
			obj = self.status(self.SPLNextTrackTitle).firstChild
			# Translators: Presented when there is no information for the next track.
			nextTrack = _("No next track scheduled or no track is playing") if obj.name is None else obj.name
			# #34 (17.08): normally, player position (name of the internal player in Studio) would not be announced, but might be useful for some broadcasters with mixers.
			if splconfig.SPLConfig["SayStatus"]["SayStudioPlayerPosition"]:
				player = self.status(self.SPLNextPlayer).firstChild.name
				ui.message(", ".join([player, nextTrack]))
			else:
				ui.message(nextTrack)
		except RuntimeError:
			# Translators: Presented when next track information is unavailable.
			ui.message(_("Cannot find next track information"))
		finally:
			self.finish()
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayNextTrackTitle.__doc__=_("Announces title of the next track if any")

	def script_sayCurrentTrackTitle(self, gesture):
		if not splbase.studioIsRunning():
			self.finish()
			return
		try:
			obj = self.status(self.SPLCurrentTrackTitle).firstChild
			# Translators: Presented when there is no information for the current track.
			currentTrack = _("Cannot locate current track information or no track is playing") if obj.name is None else obj.name
			# #34 (17.08): see the note on next track script above.
			if splconfig.SPLConfig["SayStatus"]["SayStudioPlayerPosition"]:
				player = self.status(self.SPLCurrentPlayer).firstChild.name
				ui.message(", ".join([player, currentTrack]))
			else:
				ui.message(currentTrack)
		except RuntimeError:
			# Translators: Presented when current track information is unavailable.
			ui.message(_("Cannot find current track information"))
		finally:
			self.finish()
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayCurrentTrackTitle.__doc__=_("Announces title of the currently playing track")

	def script_sayTemperature(self, gesture):
		if not splbase.studioIsRunning():
			self.finish()
			return
		try:
			obj = self.status(self.SPLTemperature).firstChild
			# Translators: Presented when there is no weather or temperature information.
			ui.message(obj.name if obj.name else _("Weather and temperature not configured"))
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
			trackStarts = divmod(splbase.studioAPI(3, 27), 1000)
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
			self.announceTime(splbase.studioAPI(4, 27), includeHours=False)
		else:
			obj = self.status(self.SPLScheduledToPlay).firstChild
			ui.message(obj.name)

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
			if splbase.studioAPI(1, 32) < 0:
				ui.message(_("{itemCount} items in the library").format(itemCount = splbase.studioAPI(0, 32)))
				return
			self.libraryScanning = True
			# Translators: Presented when attempting to start library scan.
			ui.message(_("Monitoring library scan")) if not splconfig.SPLConfig["General"]["BeepAnnounce"] else tones.beep(740, 100)
			self.monitorLibraryScan()
		else:
			# Translators: Presented when library scan is already in progress.
			ui.message(_("Scanning is in progress"))

	def script_markTrackForAnalysis(self, gesture):
		self.finish()
		if self._trackAnalysisAllowed():
			focus = api.getFocusObject()
			if scriptHandler.getLastScriptRepeatCount() == 0:
				self._analysisMarker = focus.IAccessibleChildID-1
				# Translators: Presented when track time analysis is turned on.
				ui.message(_("Playlist analysis activated"))
			else:
				self._analysisMarker = None
				# Translators: Presented when track time analysis is turned off.
				ui.message(_("Playlist analysis deactivated"))
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_markTrackForAnalysis.__doc__=_("Marks focused track as start marker for various playlist analysis commands")

	def script_trackTimeAnalysis(self, gesture):
		self.finish()
		if self._trackAnalysisAllowed():
			if self._analysisMarker is None:
				# Translators: Presented when track time analysis cannot be used because start marker is not set.
				ui.message(_("No track selected as start of analysis marker, cannot perform time analysis"))
				return
			focus = api.getFocusObject()
			trackPos = focus.IAccessibleChildID-1
			analysisBegin = min(self._analysisMarker, trackPos)
			analysisEnd = max(self._analysisMarker, trackPos)
			analysisRange = analysisEnd-analysisBegin+1
			# #75 (18.08): use segue instead as it gives more accurate information as to the actual total duration.
			# Add a 1 because track position subtracts it for comparison purposes.
			# 18.10: rework this so this feature can work on track objects directly.
			totalLength = self.playlistDuration(start=focus.parent.getChild(analysisBegin), end=focus.parent.getChild(analysisEnd+1))
			# Playlist duration method returns raw seconds, so do not force milliseconds, and in case of multiple tracks, multiply this by 1000.
			if analysisRange == 1:
				self.announceTime(totalLength, ms=False)
			else:
				# Translators: Presented when time analysis is done for a number of tracks (example output: Tracks: 3, totaling 5:00).
				ui.message(_("Tracks: {numberOfSelectedTracks}, totaling {totalTime}").format(numberOfSelectedTracks = analysisRange, totalTime = self._ms2time(totalLength*1000)))
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_trackTimeAnalysis.__doc__=_("Announces total length of tracks between analysis start marker and the current track")

	def script_takePlaylistSnapshots(self, gesture):
		if not splbase.studioIsRunning():
			self.finish()
			return
		if not self._trackAnalysisAllowed(mustSelectTrack=False):
			self.finish()
			return
		obj = api.getFocusObject()
		if obj.role == controlTypes.ROLE_LIST:
			obj = obj.firstChild
		scriptCount = scriptHandler.getLastScriptRepeatCount()
		# Display the decorated HTML window on the first press if told to do so.
		if splconfig.SPLConfig["PlaylistSnapshots"]["ShowResultsWindowOnFirstPress"]:
			scriptCount += 1
		# Never allow this to be invoked more than twice, as it causes performance degredation and multiple HTML windows are opened.
		if scriptCount >= 2:
			self.finish()
			return
		# #55 (18.04): partial playlist snapshots require start and end range.
		# Analysis marker is an integer, so locate the correct track.
		start = obj.parent.firstChild if self._analysisMarker is None else None
		end = None
		if self._analysisMarker is not None:
			trackPos = obj.IAccessibleChildID-1
			analysisBegin = min(self._analysisMarker, trackPos)
			analysisEnd = max(self._analysisMarker, trackPos)
			start = obj.parent.getChild(analysisBegin)
			end = obj.parent.getChild(analysisEnd).next
		# Speak and braille on the first press, display a decorated HTML message for subsequent presses.
		self.playlistSnapshotOutput(self.playlistSnapshots(start, end), scriptCount)
		self.finish()
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_takePlaylistSnapshots.__doc__=_("Presents playlist snapshot information such as number of tracks and top artists")

	def script_playlistTranscripts(self, gesture):
		if not splbase.studioIsRunning():
			self.finish()
			return
		if not self._trackAnalysisAllowed(mustSelectTrack=False):
			self.finish()
			return
		obj = api.getFocusObject()
		if obj.role == controlTypes.ROLE_LIST:
			obj = obj.firstChild
		try:
			d = splmisc.SPLPlaylistTranscriptsDialog(gui.mainFrame, obj)
			gui.mainFrame.prePopup()
			d.Raise()
			d.Show()
			gui.mainFrame.postPopup()
			splmisc._plTranscriptsDialogOpened = True
		except RuntimeError:
			wx.CallAfter(splmisc.plTranscriptsDialogError)
		self.finish()

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
		filename = obj._getColumnContentRaw(index)
		if filename:
			self.placeMarker = (index, filename)
			# Translators: Presented when place marker track is set.
			ui.message(_("place marker set"))
		else:
			# Translators: Presented when attempting to place a place marker on an unsupported track.
			ui.message(_("This track cannot be used as a place marker track"))

	def script_findPlaceMarker(self, gesture):
		# 7.0: Place marker command will still be restricted to playlist viewer in order to prevent focus bouncing.
		# #81: no more custom message for place marker track, as the generic one will be enough for now.
		if self.canPerformPlaylistCommands() == self.SPLPlaylistNoErrors:
			if self.placeMarker is None:
				# Translators: Presented when no place marker is found.
				ui.message(_("No place marker found"))
			else:
				track = self._trackLocator(self.placeMarker[1], obj=api.getFocusObject().parent.firstChild, columns=[self.placeMarker[0]])
				# 16.11: Just like Track Finder, use select track function to select the place marker track.
				splbase.selectTrack(track.IAccessibleChildID-1)
				track.setFocus(), track.setFocus()

	def script_metadataStreamingAnnouncer(self, gesture):
		# 8.0: Call the module-level function directly.
		# 18.04: obtain results via the misc module.
		# 18.08.1: metadata status function takes no arguments.
		ui.message(splmisc.metadataStatus())

	# Gesture(s) for the following script cannot be changed by users.
	def script_metadataEnabled(self, gesture):
		url = int(gesture.displayName[-1])
		if splbase.studioAPI(url, 36):
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
		# 18.09: show appropriate user guide version based on currently installed channel.
		SPLAddonManifest = addonHandler.Addon(os.path.join(os.path.dirname(__file__), "..", "..")).manifest
		updateChannel = SPLAddonManifest.get("updateChannel")
		if "-dev" in SPLAddonManifest['version'] or updateChannel == "dev":
			os.startfile("https://github.com/josephsl/stationplaylist/wiki/SPLDevAddonGuide")
		else: 
			os.startfile("https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide")

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
		"kb:f8":"takePlaylistSnapshots",
		"kb:shift+f8":"playlistTranscripts",
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
		"kb:f8":"takePlaylistSnapshots",
		"kb:shift+f8":"playlistTranscripts",
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
		"kb:f8":"takePlaylistSnapshots",
		"kb:shift+f8":"playlistTranscripts",
		"kb:f9":"markTrackForAnalysis",
		"kb:f10":"trackTimeAnalysis",
		"kb:f12":"switchProfiles",
		"kb:f":"findTrack",
		"kb:Control+k":"setPlaceMarker",
		"kb:k":"findPlaceMarker",
		"kb:g":"metadataStreamingAnnouncer",
		"kb:f1":"layerHelp",
		"kb:shift+f1":"openOnlineDoc",
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
		"kb:alt+nvda+-":"sendFeedbackEmail",
	}
