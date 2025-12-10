# StationPlaylist Track Tool
# An app module for NVDA
# Copyright 2014-2026 Joseph Lee, released under gPL.
# Functionality is based on JFW scripts for SPL Track Tool by Brian Hartgen.

# Track Tool allows a broadcaster to manage track intros, cues and so forth.
# Each track is a list item with descriptions such as title, file name, intro time and so forth.
# One can press TAB to move along the controls for Track Tool.

import appModuleHandler
import addonHandler
import tones
import controlTypes
import scriptHandler
import wx
import ui
import api
from NVDAObjects import NVDAObject
from NVDAObjects.IAccessible import IAccessible, sysListView32
from .splcommon import splconfig, splconfui, splbase, splcarts
from .skipTranslation import translate

addonHandler.initTranslation()


# Return a tuple of column headers.
# This is just a thinly disguised indexOf function from Studio's track item class.
def indexOf(ttVersion: str) -> tuple[str, ...]:
	if ttVersion < "6.10":
		return (
			"Artist",
			"Title",
			"Duration",
			"Cue",
			"Overlap",
			"Intro",
			"Outro",
			"Segue",
			"Hook Start",
			"Hook Len",
			"Year",
			"Album",
			"CD Code",
			"URL 1",
			"URL 2",
			"Genre",
			"Mood",
			"Energy",
			"Tempo",
			"BPM",
			"Gender",
			"Rating",
			"Filename",
			"Client",
			"Other",
			"Intro Link",
			"Outro Link",
			"ReplayGain",
			"Record Label",
			"ISRC",
			"Language",
			"Restrictions",
			"Exclude from Requests",
		)
	elif ttVersion == "6.10":
		return (
			"Artist",
			"Title",
			"Duration",
			"Cue",
			"Overlap",
			"Intro",
			"Outro",
			"Segue",
			"Hook Start",
			"Hook Len",
			"Year",
			"Album",
			"CD Code",
			"URL 1",
			"URL 2",
			"Genre",
			"Mood",
			"Energy",
			"Tempo",
			"BPM",
			"Gender",
			"Rating",
			"Filename",
			"Client",
			"Other",
			"Track Date",
			"Intro Link",
			"Outro Link",
			"ReplayGain",
			"Record Label",
			"ISRC",
			"Language",
			"Restrictions",
			"Exclude from Requests",
		)
	else:
		return (
			"Artist",
			"Title",
			"Duration",
			"Cue",
			"Overlap",
			"Intro",
			"Outro",
			"Segue",
			"Hook Start",
			"Hook Len",
			"Year",
			"Album",
			"CD Code",
			"URL 1",
			"URL 2",
			"Genre",
			"Mood",
			"Energy",
			"Tempo",
			"BPM",
			"Gender",
			"Rating",
			"Filename",
			"Client",
			"Other",
			"Track Date",
			"Intro Link",
			"Outro Link",
			"Gain",
			"Record Label",
			"ISRC",
			"Region",
			"Restrictions",
			"Exclude from Requests",
		)


class TrackToolItem(splbase.SPLTrackItem):
	"""An entry in Track Tool, used to implement some exciting features."""

	def reportFocus(self):
		# Play a beep when intro exists.
		if self._getColumnContentRaw(self.indexOf("Intro")) not in (None, ""):
			tones.beep(550, 100)
		super(TrackToolItem, self).reportFocus()

	def indexOf(self, columnHeader: str) -> int | None:
		try:
			return indexOf(self.appModule.productVersion).index(columnHeader)
		except ValueError:
			return None

	@property
	def exploreColumns(self) -> list[str]:
		return splconfig.SPLConfig["ExploreColumns"]["TrackTool"]


# Time pickers (including track properties) does not expose the correct tree.
# Thankfully, when up or down arrows are pressed, value change event is raised to change the window text.
class SPLTimePicker(IAccessible):
	def _get_name(self):
		# Time picker labels are to the left of the picker control.
		labelObj = api.getDesktopObject().objectFromPoint(self.location[0] - 8, self.location[1] + 8)
		if labelObj:
			return labelObj.name

	def _get_value(self):
		return self.windowText


class AppModule(appModuleHandler.AppModule):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# #64: load config database if not done already.
		splconfig.openConfig(self.appName)
		splconfui.initialize()

	def terminate(self):
		super().terminate()
		splconfig.closeConfig(self.appName)
		splconfui.terminate()

	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: list[NVDAObject]) -> None:
		if obj.windowClassName == "TTntListView.UnicodeClass":
			if obj.role == controlTypes.Role.LISTITEM:
				clsList.insert(0, TrackToolItem)
			elif obj.role == controlTypes.Role.LIST:
				clsList.insert(0, sysListView32.List)
		# Track properties time picker and friends.
		elif obj.windowClassName == "TDateTimePicker":
			clsList.insert(0, SPLTimePicker)

	def event_NVDAObject_init(self, obj: NVDAObject):
		if obj.windowClassName == "TStatusBar" and obj.role == controlTypes.Role.STATICTEXT and not obj.name:
			# Status bar labels are not found in Track Toolbut is written to the screen.
			obj.name = obj.displayText
		elif obj.windowClassName in [
			"TEdit",
			"TComboBox",
			"TTntEdit.UnicodeClass",
			"TTntComboBox.UnicodeClass",
			"TMemo",
			"TSpinEditMS"
		] and api.getForegroundObject().windowClassName == "TTagForm.UnicodeClass":  # Track properties
			# In certain edit fields and combo boxes, the field name is written to the screen,
			# and there's no way to fetch the object for this text.
			# In some cases, labels are next to objects but not exposed by MSAA.
			# Fetch the label by specifying the screen location where the label might be found.
			labelObj = api.getDesktopObject().objectFromPoint(
				obj.location[0] - 8,  # To the left of the unlabeled control
				obj.location[1] + 8  # Try to place the "cursor" inside the label object
			)
			if labelObj:
				obj.name = labelObj.name

	@scriptHandler.script(
		description=_("Opens SPL Studio add-on configuration dialog."),
		gestures=["kb:alt+NVDA+0", "ts(SPL):2finger_flickLeft"],
	)
	def script_openConfigDialog(self, gesture):
		# Rather than calling the config dialog open event,
		# call the open dialog function directly to avoid indirection.
		wx.CallAfter(splconfui.openAddonSettingsPanel, None)

	# Handle native Track Tool commands.

	# Announce track sort status (column, ascending/descending).
	# Number row gestures come from cart keys list.
	columnSortKeys = splcarts.cartKeys[12:]

	@scriptHandler.script(gestures=[f"kb:alt+{i}" for i in splcarts.cartKeys[12:]])
	def script_reportTrackColumnSort(self, gesture):
		gesture.send()
		fg = api.getForegroundObject()
		if not fg.windowClassName.startswith("TIntroTiming"):
			return
		column = self.columnSortKeys.index(gesture.displayName.split("+")[-1])
		# Get the last child included in list children, not last child as the former is column headers.
		columnHeader = fg.getChild(-2).children[-1].getChild(column).name
		# Up arrow (↑) = ascending, down arrow (↓) = descending
		match columnHeader[0]:
			case "↑":
				direction = translate("{column} (ascending)".format(column=columnHeader.strip("↑↓")))
			case "↓":
				direction = translate("{column} (descending)".format(column=columnHeader.strip("↑↓")))
			case _:
				direction = columnHeader
		ui.message(direction)
