# StationPlaylist Track Tool
# An app module for NVDA
# Copyright 2014-2020 Joseph Lee and contributors, released under gPL.
# Functionality is based on JFW scripts for SPL Track Tool by Brian Hartgen.

# Track Tool allows a broadcaster to manage track intros, cues and so forth. Each track is a list item with descriptions such as title, file name, intro time and so forth.
# One can press TAB to move along the controls for Track Tool.

import appModuleHandler
import addonHandler
import scriptHandler
import tones
from NVDAObjects.IAccessible import sysListView32
from .splstudio import splconfig, SPLTrackItem
addonHandler.initTranslation()


# Return a tuple of column headers.
# This is just a thinly disguised indexOf function from Studio's track item class.
def indexOf(ttVersion):
	if ttVersion < "5.31":
		return ("Artist", "Title", "Duration", "Cue", "Overlap", "Intro", "Outro", "Segue", "Hook Start", "Hook Len", "Year", "Album", "CD Code", "URL 1", "URL 2", "Genre", "Mood", "Energy", "Tempo", "BPM", "Gender", "Rating", "Filename", "Client", "Other", "Intro Link", "Outro Link", "ReplayGain", "Record Label", "ISRC")
	else:
		return ("Artist", "Title", "Duration", "Cue", "Overlap", "Intro", "Outro", "Segue", "Hook Start", "Hook Len", "Year", "Album", "CD Code", "URL 1", "URL 2", "Genre", "Mood", "Energy", "Tempo", "BPM", "Gender", "Rating", "Filename", "Client", "Other", "Intro Link", "Outro Link", "ReplayGain", "Record Label", "ISRC", "Language")


class TrackToolItem(SPLTrackItem):
	"""An entry in Track Tool, used to implement some exciting features.
	"""

	# Keep a record of which column is being looked at.
	_curColumnNumber = 0

	def reportFocus(self):
		# Play a beep when intro exists.
		if ", Intro:" in self.description:
			tones.beep(550, 100)
		super(TrackToolItem, self).reportFocus()

	def indexOf(self, header):
		try:
			return indexOf(self.appModule.productVersion).index(header)
		except ValueError:
			return None

	@property
	def exploreColumns(self):
		return splconfig.SPLConfig["General"]["ExploreColumnsTT"]

	@scriptHandler.script(
		# Translators: input help mode message for columns viewer command.
		description=_("Presents data for all columns in the currently selected track"),
		gesture="kb:control+NVDA+-")
	def script_trackColumnsViewer(self, gesture):
		# #61 (18.06): a direct copy of column data gatherer from playlist transcripts.
		# 20.02: customized for Track Tool (no status column).
		import ui
		columnHeaders = indexOf(self.appModule.productVersion)
		columns = list(range(len(columnHeaders)))
		columnContents = [self._getColumnContentRaw(col) for col in columns]
		for pos in range(len(columnContents)):
			if columnContents[pos] is None: columnContents[pos] = "blank"
			# Manually add header text until column gatherer adds headers support.
			columnContents[pos] = ": ".join([columnHeaders[pos], columnContents[pos]])
		# Translators: Title of the column data window.
		ui.browseableMessage("\n".join(columnContents), title=_("Track data"))


class AppModule(appModuleHandler.AppModule):

	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		# #64 (18.07): load config database if not done already.
		splconfig.openConfig("tracktool")

	def terminate(self):
		super(AppModule, self).terminate()
		splconfig.closeConfig("tracktool")
		TrackToolItem._curColumnNumber = 0

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		import controlTypes
		if obj.windowClassName == "TTntListView.UnicodeClass":
			if obj.role == controlTypes.ROLE_LISTITEM:
				clsList.insert(0, TrackToolItem)
			elif obj.role == controlTypes.ROLE_LIST:
				clsList.insert(0, sysListView32.List)
