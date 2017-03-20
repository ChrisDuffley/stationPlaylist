# StationPlaylist Track Tool
# An app module for NVDA
# Copyright 2014-2017 Joseph Lee and contributors, released under gPL.
# Functionality is based on JFW scripts for SPL Track Tool by Brian Hartgen.

import appModuleHandler
import addonHandler
import tones
import ui
from NVDAObjects.IAccessible import IAccessible
from splstudio import splconfig
from splstudio.splmisc import _getColumnContent
addonHandler.initTranslation()

# Track Tool allows a broadcaster to manage track intros, cues and so forth. Each track is a list item with descriptions such as title, file name, intro time and so forth.
# One can press TAB to move along the controls for Track Tool.

# Return a tuple of column headers.
# This is just a thinly disguised indexOf function from Studio's track item class.
def indexOf(ttVersion):
	if ttVersion < "5.2":
		return ("Artist","Title","Duration","Cue","Overlap","Intro","Outro","Segue","Year","Album","CD Code","URL 1","URL 2","Genre","Mood","Energy","Tempo","BPM","Gender","Rating","Filename","Client","Other","Intro Link","Outro Link")
	else:
		return ("Artist","Title","Duration","Cue","Overlap","Intro","Outro","Segue","Hook Start","Hook Len","Year","Album","CD Code","URL 1","URL 2","Genre","Mood","Energy","Tempo","BPM","Gender","Rating","Filename","Client","Other","Intro Link","Outro Link","ReplayGain")

class TrackToolItem(IAccessible):
	"""An entry in Track Tool, used to implement some exciting features.
	"""

	def reportFocus(self):
		# Play a beep when intro exists.
		if ", Intro:" in self.description:
			tones.beep(550, 100)
		super(TrackToolItem, self).reportFocus()

	def initOverlayClass(self):
		# 8.0: Assign Control+NVDA+number row for Columns Explorer just like the main app module.
		for i in xrange(10):
			self.bindGesture("kb:control+nvda+%s"%(i), "columnExplorer")

	# Tweak for Track Tool: Announce column header if given.
	# Also take care of this when specific columns are asked.
	# This also allows display order to be checked (Studio 5.10 and later).
	def announceColumnContent(self, colNumber, columnHeader=None, individualColumns=False):
		if not columnHeader:
			columnHeader = self.columnHeaders.children[colNumber].name
			# LTS: Studio 5.10 data structure change is evident in Track Tool as well, so don't rely on column headers alone.
			internalHeaders = indexOf(self.appModule.productVersion)
			if internalHeaders[colNumber] != columnHeader:
				colNumber = internalHeaders.index(columnHeader)
		columnContent = _getColumnContent(self, colNumber)
		if columnContent:
			ui.message(unicode(_("{header}: {content}")).format(header = columnHeader, content = columnContent))
		else:
			if individualColumns:
				# Translators: Presented when some info is not defined for a track in Track Tool (example: cue not found)
				ui.message(_("{header} not found").format(header = columnHeader))
			else:
				import speech, braille
				speech.speakMessage(_("{header}: blank").format(header = columnHeader))
				braille.handler.message(_("{header}: ()").format(header = columnHeader))

	# Now the scripts.

	def script_nextColumn(self, gesture):
		self.columnHeaders = self.parent.children[-1]
		if (self.appModule.SPLColNumber+1) == self.columnHeaders.childCount:
			tones.beep(2000, 100)
		else:
			self.appModule.SPLColNumber +=1
		self.announceColumnContent(self.appModule.SPLColNumber)

	def script_prevColumn(self, gesture):
		self.columnHeaders = self.parent.children[-1]
		if self.appModule.SPLColNumber <= 0:
			tones.beep(2000, 100)
		else:
			self.appModule.SPLColNumber -=1
		self.announceColumnContent(self.appModule.SPLColNumber)

	# Special script for Columns Explorer.

	def script_columnExplorer(self, gesture):
		# Just like the main app module, due to the below formula, columns explorer will be restricted to number commands.
		header = splconfig.SPLConfig["General"]["ExploreColumnsTT"][int(gesture.displayName.split("+")[-1])-1]
		# Several corner cases.
		# Look up track name if artist is the header name.
		if header == "Artist":
			if self.name is None:
				# Translators: Presented when artist information is not found for a track in Track Tool.
				ui.message(_("No artist"))
			else:
				# Translators: Presents artist information for a track in Track Tool.
				ui.message(_("Artist: {artistName}").format(artistName = self.name))
		# Special case for intro to make it compatible with old add-on releases.
		elif header == "Intro" and "Intro:" not in self.description:
			# Translators: Presented when intro is not defined for a track in Track Tool.
			ui.message(_("Introduction not set"))
		else:
			try:
				self.announceColumnContent(indexOf(self.appModule.productVersion).index(header), columnHeader=header)
			except ValueError:
				# Translators: Presented when some info is not defined for a track in Track Tool (example: cue not found)
				ui.message(_("{headerText} not found").format(headerText = header))

	__gestures={
		"kb:control+alt+rightArrow":"nextColumn",
		"kb:control+alt+leftArrow":"prevColumn",
	}


class AppModule(appModuleHandler.AppModule):

	SPLColNumber = 0

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		import controlTypes
		if obj.windowClassName in ("TListView", "TTntListView.UnicodeClass") and obj.role == controlTypes.ROLE_LISTITEM:
			clsList.insert(0, TrackToolItem)
