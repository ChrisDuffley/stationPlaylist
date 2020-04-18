# StationPlaylist Creator
# An app module and global plugin package for NVDA
# Copyright 2016-2020 Joseph Lee and others, released under GPL.

# Basic support for StationPlaylist Creator.

import appModuleHandler
import addonHandler
import scriptHandler
import globalVars
import ui
import api
from NVDAObjects.IAccessible import sysListView32
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

	@scriptHandler.script(
		# Translators: input help mode message for columns viewer command.
		description=_("Presents data for all columns in the currently selected track"),
		gesture="kb:control+NVDA+-")
	def script_trackColumnsViewer(self, gesture):
		# #61 (18.06): a direct copy of column data gatherer from playlist transcripts.
		# 20.02: customized for Creator (no status column).
		columnHeaders = indexOf(self.appModule.productVersion)
		columns = list(range(len(columnHeaders)))
		columnContents = [self._getColumnContentRaw(col) for col in columns]
		for pos in range(len(columnContents)):
			if columnContents[pos] is None: columnContents[pos] = "blank"
			# Manually add header text until column gatherer adds headers support.
			columnContents[pos] = ": ".join([columnHeaders[pos], columnContents[pos]])
		# Translators: Title of the column data window.
		ui.browseableMessage("\n".join(columnContents), title=_("Track data"))

	__gestures = {
		"kb:control+alt+downArrow": None,
		"kb:control+alt+upArrow": None,
	}


class SPLPlaylistEditorItem(SPLTrackItem):
	"""An entry in SPL Creator's Playlist Editor.
	"""

	# Keep a record of which column is being looked at.
	_curColumnNumber = 0

	__gestures = {
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
				ui.message("SPL Creator {SPLVersion}".format(SPLVersion=self.productVersion))
		except:
			pass
		# #64 (18.07): load config database if not done already.
		splconfig.openConfig("splcreator")

	def terminate(self):
		super(AppModule, self).terminate()
		splconfig.closeConfig("splcreator")
		SPLCreatorItem._curColumnNumber = 0
		# Clear Playlist Editor status cache, otherwise it will generate errors when Creator restarts without restarting NVDA.
		self._playlistEditorStatusCache.clear()

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		import controlTypes
		# 20.02: tracks list uses a different window class name other than "TListView".
		# Resort to window style and other tricks if other lists with the class name below is found and are not tracks list.
		if obj.windowClassName == "TTntListView.UnicodeClass":
			if obj.role == controlTypes.ROLE_LISTITEM:
				clsList.insert(0, SPLCreatorItem if obj.windowStyle == 1443958857 else SPLPlaylistEditorItem)
			elif obj.role == controlTypes.ROLE_LIST:
				clsList.insert(0, sysListView32.List)
		elif obj.windowClassName in ("TDemoRegForm", "TAboutForm"):
			from NVDAObjects.behaviors import Dialog
			clsList.insert(0, Dialog)

	# The following scripts are designed to work while using Playlist Editor.

	def isPlaylistEditor(self):
		if api.getForegroundObject().windowClassName != "TEditMain":
			ui.message("You are not in playlist editor")
			return False
		return True

	# Just like Studio, status items are scattered around the screen in Playlist Editor, and takes a really long time to fetch things.
	SPLEditorDateTime = 0
	SPLEditorDuration = 1
	SPLEditorStatusBar = 2
	_playlistEditorStatusCache = {}

	@scriptHandler.script(gesture="kb:alt+NVDA+1")
	def script_playlistDateTime(self, gesture):
		if self.isPlaylistEditor():
			try:
				playlistHour = self._playlistEditorStatusCache[self.SPLEditorDateTime][0]
				playlistDay = self._playlistEditorStatusCache[self.SPLEditorDateTime][1]
			except KeyError:
				playlistDateTime = api.getForegroundObject().simpleLastChild.firstChild.next
				playlistHour = playlistDateTime.simpleNext
				playlistDay = playlistHour.simpleNext.simpleNext
				self._playlistEditorStatusCache[self.SPLEditorDateTime] = [playlistHour, playlistDay]
			ui.message(" ".join([playlistDay.value, playlistHour.value]))

	@scriptHandler.script(gesture="kb:alt+NVDA+2")
	def script_playlistDuration(self, gesture):
		if self.isPlaylistEditor():
			try:
				playlistDuration = self._playlistEditorStatusCache[self.SPLEditorDuration]
			except KeyError:
				playlistDuration = api.getForegroundObject().simpleLastChild.firstChild
				self._playlistEditorStatusCache[self.SPLEditorDuration] = playlistDuration
			ui.message(playlistDuration.name)

	@scriptHandler.script(gesture="kb:alt+NVDA+3")
	def script_playlistScheduled(self, gesture):
		if self.isPlaylistEditor():
			try:
				statusBar = self._playlistEditorStatusCache[self.SPLEditorStatusBar]
			except KeyError:
				statusBar = api.getForegroundObject().firstChild.firstChild
				self._playlistEditorStatusCache[self.SPLEditorStatusBar] = statusBar
			ui.message(statusBar.getChild(2).name)

	@scriptHandler.script(gesture="kb:alt+NVDA+4")
	def script_playlistRotation(self, gesture):
		if self.isPlaylistEditor():
			try:
				statusBar = self._playlistEditorStatusCache[self.SPLEditorStatusBar]
			except KeyError:
				statusBar = api.getForegroundObject().firstChild.firstChild
				self._playlistEditorStatusCache[self.SPLEditorStatusBar] = statusBar
			ui.message(statusBar.getChild(3).name)
