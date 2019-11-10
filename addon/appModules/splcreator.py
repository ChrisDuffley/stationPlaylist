# StationPlaylist Creator
# An app module and global plugin package for NVDA
# Copyright 2016-2019 Joseph Lee and others, released under GPL.

# Basic support for StationPlaylist Creator.

import appModuleHandler
import addonHandler
import globalVars
import ui
from NVDAObjects.IAccessible import IAccessible, sysListView32
from .splstudio import splconfig, SPLTrackItem
addonHandler.initTranslation()

# Return a tuple of column headers.
# This is just a thinly disguised indexOf function from Studio's track item class.
def indexOf(creatorVersion):
	if creatorVersion >= "5.31":
		return ("Artist", "Title", "Position", "Cue", "Intro", "Outro", "Segue", "Duration", "Last Scheduled", "7 Days", "Date Restriction", "Year", "Album", "Genre", "Mood", "Energy", "Tempo", "BPM", "Gender", "Rating", "File Created", "Filename", "Client", "Other", "Intro Link", "Outro Link", "Language")
	else:
		return ("Artist", "Title", "Position", "Cue", "Intro", "Outro", "Segue", "Duration", "Last Scheduled", "7 Days", "Date Restriction", "Year", "Album", "Genre", "Mood", "Energy", "Tempo", "BPM", "Gender", "Rating", "File Created", "Filename", "Client", "Other", "Intro Link", "Outro Link")

class SPLCreatorItem(SPLTrackItem):
	"""An entry in SPL Creator (mostly tracks).
	"""

	# Keep a record of which column is being looked at.
	_curColumnNumber = 0

	def indexOf(self, header):
		try:
			return indexOf(self.appModule.productVersion).index(header)
		except ValueError:
			return None

	@property
	def exploreColumns(self):
		return splconfig.SPLConfig["General"]["ExploreColumnsCreator"]

	__gestures={
		"kb:control+alt+downArrow": None,
		"kb:control+alt+upArrow": None,
	}


class AppModule(appModuleHandler.AppModule):

	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		# Announce Creator version at startup unless minimal flag is set.
		try:
			if not globalVars.appArgs.minimal:
				# No translation.
				ui.message("SPL Creator {SPLVersion}".format(SPLVersion = self.productVersion))
		except:
			pass
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
