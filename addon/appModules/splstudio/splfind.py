# SPL Studio track finder facility
# An app module and global plugin package for NVDA
# Copyright 2026 Joseph Lee, released under GPL.
# Base services to find items in playlist viewer.
# Split from splmisc module in 2026.

from typing import Any
import weakref
import gui
import wx
import core
import speech
import cursorManager
import addonHandler
from NVDAObjects import NVDAObject
from ..splcommon import splbase, splactions
from ..skipTranslation import translate

addonHandler.initTranslation()

# Various SPL IPC tags.
SPLFileDuration = 30
SPLTrackFilename = 211

# The track finder utility for find track script and other functions
# Perform a linear search to locate the track name and/or description which matches the entered value.
# Also, find column content for a specific column if requested.
# The below routines are also used in place marker track locator.
# Find text is based on NVDA cursor manager find text.

def trackFinder(
	text: str, obj: NVDAObject, directionForward: bool = True, column: list[int] | None = None
) -> None:
	# Optimization/alignment with NVDA Core: do nothing if text is empty.
	if not text:
		return
	speech.cancelSpeech()
	# Start from next/previous track if this text was searched before.
	if text == cursorManager.CursorManager._lastFindText:
		obj = obj.next if directionForward else obj.previous
	if obj is not None and not column:
		column = [obj.indexOf("Artist"), obj.indexOf("Title")]
	track = trackLocator(text, obj=obj, directionForward=directionForward, columns=column)
	# #32: Update search text even if the track with the search term in columns does not exist.
	cursorManager.CursorManager._lastFindText = text
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
def trackLocator(
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

# A common dialog for Track Finder
_findDialogOpened = False

# Track Finder error dialog.
def finderError() -> None:
	global _findDialogOpened
	if _findDialogOpened:
		gui.messageBox(
			# Translators: Text of the dialog when another find dialog is open.
			_("Another find dialog is open."),
			translate("Error"),
			style=wx.OK | wx.ICON_ERROR,
		)
	else:
		gui.messageBox(
			# Translators: Text of the dialog when a generic error has occured.
			_("An unexpected error has occured when trying to open find dialog."),
			translate("Error"),
			style=wx.OK | wx.ICON_ERROR,
		)


class SPLFindDialog(wx.Dialog):
	@classmethod
	def _instance(cls):
		return None

	def __new__(cls, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _findDialogOpened:
			raise RuntimeError("An instance of find dialog is opened")
		instance = SPLFindDialog._instance()
		if instance is None:
			return super(SPLFindDialog, cls).__new__(cls, *args, **kwargs)
		return instance

	def __init__(self, parent, obj, text, title, directionForward=True, columnSearch=False):
		global _findDialogOpened
		if SPLFindDialog._instance() is not None:
			return
		# Use a weakref so the instance can die.
		SPLFindDialog._instance = weakref.ref(self)

		super().__init__(parent, wx.ID_ANY, title)
		self.obj = obj
		self.directionForward = directionForward
		self.columnSearch = columnSearch
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		findSizerHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)

		if not columnSearch:
			# Translators: the label for find prompt in track finder dialog.
			findPrompt = _("Enter or select the name or the artist of the track you wish to &search")
		else:
			# Translators: the label for find prompt in column search dialog.
			findPrompt = _("Enter or select text to be &searched in a column")
		self.findEntry = findSizerHelper.addLabeledControl(findPrompt, wx.TextCtrl, value=text)

		if columnSearch:
			# Use default screen column order when searching column content.
			columns = list(self.obj.screenColumnOrder)
			self.columnHeaders = findSizerHelper.addLabeledControl(
				# Translators: The label in track finder to search columns.
				_("C&olumn to search:"),
				wx.Choice,
				choices=columns,
			)
			self.columnHeaders.SetSelection(0)

		# #152: add a separator if column search is active, otherwise only find prompt is displayed.
		findSizerHelper.addDialogDismissButtons(wx.OK | wx.CANCEL, separated=columnSearch)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(findSizerHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.CenterOnScreen()
		self.findEntry.SetFocus()
		_findDialogOpened = True

	def onOk(self, evt):
		global _findDialogOpened
		text = self.findEntry.Value
		# Search columns should not be None - list of integers expected.
		column = [self.columnHeaders.Selection + 1] if self.columnSearch else []
		startObj = self.obj
		# If this is called right away, we land on an invisible window.
		core.callLater(
			100,
			trackFinder,
			text,
			startObj,
			directionForward=self.directionForward,
			column=column
		)
		self.Destroy()
		_findDialogOpened = False

	def onCancel(self, evt):
		self.Destroy()
		global _findDialogOpened
		_findDialogOpened = False

	def onAppTerminate(self):
		# Call cancel function when the app terminates so the dialog can be closed.
		self.onCancel(None)


# Time range finder: a variation on track finder.
# Similar to track finder, locate tracks with duration that falls between min and max.

def timeRangeFinder(
	obj: NVDAObject | None,
	minDuration: tuple[int, int],
	maxDuration: tuple[int, int]
) -> None:
	# Exit early if Studio (local and remote) app module is gone.
	if obj is None:
		return
	# Either look up filename/track duration or duration text depending on Studio API availability.
	if obj.appModule._localStudioAPIRequired:  # Local Studio
		minTrackDuration: Any = ((minDuration[0] * 60) + minDuration[1]) * 1000
		maxTrackDuration: Any = ((maxDuration[0] * 60) + maxDuration[1]) * 1000
	else:  # Remote Studio
		minTrackDuration: Any = f"{minDuration[0]:02d}:{minDuration[1]:02d}"
		maxTrackDuration: Any = f"{maxDuration[0]:02d}:{maxDuration[1]:02d}"
	# Manually locate tracks.
	while obj is not None:
		if obj.appModule._localStudioAPIRequired:
			filename = splbase.studioAPI(obj.IAccessibleChildID - 1, SPLTrackFilename)
			trackDuration = splbase.studioAPI(filename, SPLFileDuration)
		else:
			trackDuration = obj._getColumnContentRaw(obj.indexOf("Duration"))
			# Python says "01:00:00" < "59:59" thanks to string value comparison.
			# Therefore, if there are two or more colons, convert this to an hour long track ("60:00").
			if trackDuration.count(":") > 1:
				trackDuration = "60:00"
		if minTrackDuration <= trackDuration <= maxTrackDuration:
			break
		obj = obj.next
	if obj is not None:
		# Set focus only once, as do action method on tracks will set focus twice.
		obj.setFocus()
		# Select the desired track manually.
		# Selecting tracks via splbase module requires Studio API (local Studio only).
		if obj.appModule._localStudioAPIRequired:
			splbase.selectTrack(obj.IAccessibleChildID - 1)
	else:
		wx.CallAfter(
			# Translators: Presented when a track with a duration
			# between minimum and maximum duration is not found.
			gui.messageBox,
			_("No track with duration between minimum and maximum duration."),
			# Translators: Standard error title for find error (copy this from main nvda.po).
			_("Time range find error"),
			wx.OK | wx.ICON_ERROR,
		)

class SPLTimeRangeDialog(wx.Dialog):
	@classmethod
	def _instance(cls):
		return None

	def __new__(cls, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _findDialogOpened:
			raise RuntimeError("An instance of find dialog is opened")
		instance = SPLTimeRangeDialog._instance()
		if instance is None:
			return super(SPLTimeRangeDialog, cls).__new__(cls, *args, **kwargs)
		return instance

	def __init__(self, parent, obj):
		global _findDialogOpened
		if SPLTimeRangeDialog._instance() is not None:
			return
		# Use a weakref so the instance can die.
		SPLTimeRangeDialog._instance = weakref.ref(self)

		# Translators: The title of a dialog to find tracks with duration within a specified range.
		super().__init__(parent, wx.ID_ANY, _("Time range finder"))
		self.obj = obj

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		timeRangeHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)

		minRangeGroup = gui.guiHelper.BoxSizerHelper(
			# Translators: the label for a group to specify minimum track duration in time range finder dialog.
			self,
			sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=_("Minimum duration")), wx.HORIZONTAL),
		)
		timeRangeHelper.addItem(minRangeGroup)
		self.minMinEntry = minRangeGroup.addLabeledControl(
			# Translators: the minute label in time range finder dialog.
			_("Minute"),
			gui.nvdaControls.SelectOnFocusSpinCtrl,
			min=0,
			max=59,
			initial=3,
		)
		self.minSecEntry = minRangeGroup.addLabeledControl(
			# Translators: the second label in time range finder dialog.
			_("Second"),
			gui.nvdaControls.SelectOnFocusSpinCtrl,
			min=0,
			max=59,
			initial=0,
		)

		maxRangeGroup = gui.guiHelper.BoxSizerHelper(
			# Translators: the label for a group to specify maximum track duration in time range finder dialog.
			self,
			sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=_("Maximum duration")), wx.HORIZONTAL),
		)
		timeRangeHelper.addItem(maxRangeGroup)
		self.maxMinEntry = maxRangeGroup.addLabeledControl(
			_("Minute"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=59, initial=5
		)
		self.maxSecEntry = maxRangeGroup.addLabeledControl(
			_("Second"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=59, initial=0
		)

		# #68: wx.BoxSizer.AddSizer no longer exists in wxPython 4.
		timeRangeHelper.addDialogDismissButtons(wx.OK | wx.CANCEL, separated=True)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(timeRangeHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.CenterOnScreen()
		self.minMinEntry.SetFocus()
		_findDialogOpened = True

	def onOk(self, evt):
		minDuration: tuple[int, int] = (self.minMinEntry.GetValue(), self.minSecEntry.GetValue())
		maxDuration: tuple[int, int] = (self.maxMinEntry.GetValue(), self.maxSecEntry.GetValue())
		# What if minimum is greater than maximum (subtle oversight)?
		if minDuration >= maxDuration:
			gui.messageBox(
				# Translators: Message to report wrong value for duration fields.
				_("Minimum duration is greater than the maximum duration."),
				translate("Error"),
				wx.OK | wx.ICON_ERROR,
				self,
			)
			self.minMinEntry.SetFocus()
			return
		global _findDialogOpened
		# If this is called right away, we land on an invisible window.
		core.callLater(
			100,
			timeRangeFinder,
			self.obj.next,
			minDuration,
			maxDuration
		)
		self.Destroy()
		_findDialogOpened = False

	def onCancel(self, evt):
		self.Destroy()
		global _findDialogOpened
		_findDialogOpened = False

	def onAppTerminate(self):
		# Call cancel function when the app terminates so the dialog can be closed.
		self.onCancel(None)
