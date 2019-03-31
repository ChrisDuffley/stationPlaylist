# StationPlaylist Track Tool
# An app module for NVDA
# Copyright 2014-2019 Joseph Lee and contributors, released under gPL.
# Functionality is based on JFW scripts for SPL Track Tool by Brian Hartgen.

import appModuleHandler
import addonHandler
import tones
import ui
import scriptHandler
from NVDAObjects.IAccessible import IAccessible, sysListView32
from splstudio import splconfig, SPLTrackItem
addonHandler.initTranslation()

# Track Tool allows a broadcaster to manage track intros, cues and so forth. Each track is a list item with descriptions such as title, file name, intro time and so forth.
# One can press TAB to move along the controls for Track Tool.

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

	# Tweak for Track Tool: Announce column header if given.
	# Also take care of this when specific columns are asked.
	# This also allows display order to be checked (Studio 5.10 and later).
	def announceColumnContent(self, colNumber, header=None, individualColumns=False):
		import sys
		if not header:
			# #72: directly fetch on-screen column header (not the in-memory one) by probing column order array from the list (parent).
			# #65 (18.08): use column header method (at least the method body) provided by the class itself.
			# This will work properly if the list (parent) is (or recognized as) SysListView32.List.
			header = self._getColumnHeaderRaw(self.parent._columnOrderArray[colNumber])
			# LTS: Studio 5.10 data structure change is evident in Track Tool as well, so don't rely on column headers alone.
			internalHeaders = indexOf(self.appModule.productVersion)
			if internalHeaders[colNumber] != header:
				colNumber = internalHeaders.index(header)
		columnContent = self._getColumnContentRaw(colNumber)
		if columnContent:
			if sys.version.startswith("3"): ui.message(str(_("{header}: {content}")).format(header = header, content = columnContent))
			else: ui.message(unicode(_("{header}: {content}")).format(header = header, content = columnContent))
		else:
			if individualColumns:
				# Translators: Presented when some info is not defined for a track in Track Tool (example: cue not found)
				ui.message(_("{header} not found").format(header = header))
			else:
				import speech, braille
				speech.speakMessage(_("{header}: blank").format(header = header))
				braille.handler.message(_("{header}: ()").format(header = header))

	def indexOf(self, header):
		try:
			return indexOf(self.appModule.productVersion).index(header)
		except ValueError:
			return None

	@property
	def exploreColumns(self):
		return splconfig.SPLConfig["General"]["ExploreColumnsTT"]

	__gestures={
		"kb:control+alt+downArrow": None,
		"kb:control+alt+upArrow": None,
	}


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
		if obj.windowClassName in ("TListView", "TTntListView.UnicodeClass"):
			if obj.role == controlTypes.ROLE_LISTITEM:
				clsList.insert(0, TrackToolItem)
			elif obj.role == controlTypes.ROLE_LIST:
				clsList.insert(0, sysListView32.List)
