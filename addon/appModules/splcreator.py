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
from NVDAObjects.IAccessible import IAccessible, sysListView32
from splstudio import splconfig, SPLTrackItem
from splstudio.splmisc import _getColumnContent, _getColumnHeader, _getColumnOrderArray, _getColumnCount
addonHandler.initTranslation()

# Return a tuple of column headers.
# This is just a thinly disguised indexOf function from Studio's track item class.
def indexOf(ttVersion):
	return ("Artist", "Title", "Position", "Cue", "Intro", "Outro", "Segue", "Duration", "Last Scheduled", "7 Days", "Date Restriction", "Year", "Album", "Genre", "Mood", "Energy", "Tempo", "BPM", "Gender", "Rating", "File Created", "Filename", "Client", "Other", "Intro Link", "Outro Link")

class SPLCreatorItem(SPLTrackItem):
	"""An entry in SPL Creator (mostly tracks).
	"""

	# Keep a record of which column is being looked at.
	_curColumnNumber = 0

	# Another tweak for SPL Creator: Announce column header if given.
	# Also take care of this when specific columns are asked.
	# This also allows display order to be checked (Studio 5.10 and later).
	def announceColumnContent(self, colNumber, header=None, individualColumns=False):
		if not header:
			# #72: directly fetch on-screen column header (not the in-memory one) by probing column order array from the list (parent).
			# #65 (18.08): use column header method (at least the method body) provided by the class itself.
			# This will work properly if the list (parent) is (or recognized as) SysListView32.List.
			header = self._getColumnHeaderRaw(self.parent._columnOrderArray[colNumber])
			# LTS: Studio 5.10 data structure change is also seen in Creator, so don't rely on column headers alone.
			internalHeaders = indexOf(self.appModule.productVersion)
			if internalHeaders[colNumber] != header:
				colNumber = internalHeaders.index(header)
		columnContent = _getColumnContent(self, colNumber)
		if columnContent:
			if py3: ui.message(str(_("{header}: {content}")).format(header = header, content = columnContent))
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

	# Now the scripts.

	def script_moveToNextColumn(self, gesture):
		if (self._curColumnNumber+1) == _getColumnCount(self):
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
		self.__class__._curColumnNumber = _getColumnCount(self)-1
		self.announceColumnContent(self._curColumnNumber)

	@property
	def exploreColumns(self):
		return splconfig.SPLConfig["General"]["ExploreColumnsCreator"]

	__gestures={
		"kb:control+alt+downArrow": None,
		"kb:control+alt+upArrow": None,
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
		SPLCreatorItem._curColumnNumber = 0

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		import controlTypes
		if obj.windowClassName in ("TListView", "TTntListView.UnicodeClass"):
			if obj.role == controlTypes.ROLE_LISTITEM:
				clsList.insert(0, SPLCreatorItem)
			elif obj.role == controlTypes.ROLE_LIST:
				clsList.insert(0, sysListView32.List)
		elif obj.windowClassName in ("TDemoRegForm", "TAboutForm"):
			from NVDAObjects.behaviors import Dialog
			clsList.insert(0, Dialog)
