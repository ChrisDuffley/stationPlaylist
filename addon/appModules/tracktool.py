# StationPlaylist Track Tool
# An app module for NVDA
# Copyright 2014-2025 Joseph Lee, released under gPL.
# Functionality is based on JFW scripts for SPL Track Tool by Brian Hartgen.

# Track Tool allows a broadcaster to manage track intros, cues and so forth.
# Each track is a list item with descriptions such as title, file name, intro time and so forth.
# One can press TAB to move along the controls for Track Tool.

import appModuleHandler
import addonHandler
import tones
import controlTypes
from NVDAObjects.IAccessible import sysListView32
from .splstudio import SPLTrackItem
from .splcommon import splconfig

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


class TrackToolItem(SPLTrackItem):
	"""An entry in Track Tool, used to implement some exciting features."""

	def reportFocus(self):
		# Play a beep when intro exists.
		if self._getColumnContentRaw(self.indexOf("Intro")) is not None:
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
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# #64: load config database if not done already.
		splconfig.openConfig(self.appName)

	def terminate(self):
		super().terminate()
		splconfig.closeConfig(self.appName)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.windowClassName == "TTntListView.UnicodeClass":
			if obj.role == controlTypes.Role.LISTITEM:
				clsList.insert(0, TrackToolItem)
			elif obj.role == controlTypes.Role.LIST:
				clsList.insert(0, sysListView32.List)
