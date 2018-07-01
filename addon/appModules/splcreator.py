# StationPlaylist Creator
# An app module and global plugin package for NVDA
# Copyright 2016-2018 Joseph Lee and others, released under GPL.

# Basic support for StationPlaylist Creator.

import sys
py3 = sys.version.startswith("3")
import appModuleHandler
import addonHandler
import tones
import ui
import scriptHandler
from NVDAObjects.IAccessible import IAccessible
from splstudio import splconfig
from splstudio.splmisc import _getColumnContent, _getColumnHeader, _getColumnOrderArray, _getColumnCount
addonHandler.initTranslation()

# Python 3 preparation (a compatibility layer until Six module is included).
rangeGen = range if py3 else xrange

# Return a tuple of column headers.
# This is just a thinly disguised indexOf function from Studio's track item class.
def indexOf(ttVersion):
	return ("Artist", "Title", "Position", "Cue", "Intro", "Outro", "Segue", "Duration", "Last Scheduled", "7 Days", "Date Restriction", "Year", "Album", "Genre", "Mood", "Energy", "Tempo", "BPM", "Gender", "Rating", "File Created", "Filename", "Client", "Other", "Intro Link", "Outro Link")

class SPLCreatorItem(IAccessible):
	"""An entry in SPL Creator (mostly tracks).
	"""

	# Keep a record of which column is being looked at.
	_curColumnNumber = 0

	def initOverlayClass(self):
		# 8.0: Assign Control+NVDA+number row for Columns Explorer just like the main app module.
		for i in rangeGen(10):
			self.bindGesture("kb:control+nvda+%s"%(i), "columnExplorer")

	# Another tweak for SPL Creator: Announce column header if given.
	# Also take care of this when specific columns are asked.
	# This also allows display order to be checked (Studio 5.10 and later).
	def announceColumnContent(self, colNumber, columnHeader=None, individualColumns=False):
		if not columnHeader:
			# #72: directly fetch on-screen column header (not the in-memory one) by probing column order array from the list (parent).
			columnHeader = _getColumnHeader(self, _getColumnOrderArray(self)[colNumber])
			# LTS: Studio 5.10 data structure change is also seen in Creator, so don't rely on column headers alone.
			internalHeaders = indexOf(self.appModule.productVersion)
			if internalHeaders[colNumber] != columnHeader:
				colNumber = internalHeaders.index(columnHeader)
		columnContent = _getColumnContent(self, colNumber)
		if columnContent:
			if py3: ui.message(str(_("{header}: {content}")).format(header = columnHeader, content = columnContent))
			else: ui.message(unicode(_("{header}: {content}")).format(header = columnHeader, content = columnContent))
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
		if (self._curColumnNumber+1) == _getColumnCount(self):
			tones.beep(2000, 100)
		else:
			self.__class__._curColumnNumber +=1
		self.announceColumnContent(self._curColumnNumber)

	def script_prevColumn(self, gesture):
		if self._curColumnNumber <= 0:
			tones.beep(2000, 100)
		else:
			self.__class__._curColumnNumber -=1
		self.announceColumnContent(self._curColumnNumber)

	def script_firstColumn(self, gesture):
		self.__class__._curColumnNumber = 0
		self.announceColumnContent(self._curColumnNumber)

	def script_lastColumn(self, gesture):
		self.__class__._curColumnNumber = _getColumnCount(self)-1
		self.announceColumnContent(self._curColumnNumber)

	# Special script for Columns Explorer.

	def script_columnExplorer(self, gesture):
		# Just like the main app module, due to the below formula, columns explorer will be restricted to number commands.
		header = splconfig.SPLConfig["General"]["ExploreColumnsCreator"][int(gesture.displayName.split("+")[-1])-1]
		try:
			colNumber = indexOf(self.appModule.productVersion).index(header)
		except ValueError:
			# Translators: Presented when some info is not defined for a track in Track Tool (example: cue not found)
			ui.message(_("{headerText} not found").format(headerText = header))
			return
		if scriptHandler.getLastScriptRepeatCount() == 0: self.announceColumnContent(colNumber, columnHeader=header)
		else:
			# 18.07: an exact copy of column announcement method with changes.
			internalHeaders = indexOf(self.appModule.productVersion)
			if internalHeaders[colNumber] != header:
				colNumber = internalHeaders.index(header)
			columnContent = _getColumnContent(self, colNumber)
			if columnContent is None:
				# Translators: presented when column information for a track is empty.
				columnContent = _("blank")
			ui.browseableMessage("{0}: {1}".format(header, columnContent),
				# Translators: Title of the column data window.
				title=_("Track data"))

	__gestures={
		"kb:control+alt+rightArrow":"nextColumn",
		"kb:control+alt+leftArrow":"prevColumn",
		"kb:control+alt+home":"firstColumn",
		"kb:control+alt+end":"lastColumn",
	}


class AppModule(appModuleHandler.AppModule):

	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		# #64 (18.07): load config database if not done already.
		splconfig.openConfig("splcreator")

	def terminate(self):
		super(AppModule, self).terminate()
		splconfig.closeConfig("splcreator")

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		import controlTypes
		if obj.windowClassName in ("TListView", "TTntListView.UnicodeClass") and obj.role == controlTypes.ROLE_LISTITEM:
			clsList.insert(0, SPLCreatorItem)
		elif obj.windowClassName in ("TDemoRegForm", "TAboutForm"):
			from NVDAObjects.behaviors import Dialog
			clsList.insert(0, Dialog)
