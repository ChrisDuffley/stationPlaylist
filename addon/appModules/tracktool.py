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
from NVDAObjects.IAccessible import sysListView32
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


class AppModule(appModuleHandler.AppModule):
	scriptCategory = _("StationPlaylist")

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
		# Detect unlabeled controls whose labels are next to them (written to the screen).
		# Return right after detecting these.
		if splbase.useScreenLabelForUnlabeledObject(
			obj, [
				"TTagForm.UnicodeClass"  # Track properties
			]
		):
			clsList.insert(0, splbase.SPLUnlabeledControl)
			return
		if obj.windowClassName == "TTntListView.UnicodeClass":
			if obj.role == controlTypes.Role.LISTITEM:
				clsList.insert(0, TrackToolItem)
			elif obj.role == controlTypes.Role.LIST:
				clsList.insert(0, sysListView32.List)

	def event_NVDAObject_init(self, obj: NVDAObject):
		if obj.windowClassName == "TStatusBar" and obj.role == controlTypes.Role.STATICTEXT and not obj.name:
			# Status bar labels are not found in Track Toolbut is written to the screen.
			obj.name = obj.displayText

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
