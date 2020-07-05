# StationPlaylist Remote VT Client
# An app module and global plugin package for NVDA
# Copyright 2020 Joseph Lee and others, released under GPL.

# Basic support for StationPlaylist Remote VT Client.
# Borrows heavily from creator as the user interface is quite similar with changes specific to VT Client.

import addonHandler
import globalVars
import ui
from . import splcreator
from .splstudio import SPLTrackItem
addonHandler.initTranslation()


class SPLRemotePlaylistEditorItem(SPLTrackItem):
	"""An entry in SPL VT Remote Playlist Editor.
	"""

	# Keep a record of which column is being looked at.
	_curColumnNumber = 0


class AppModule(splcreator.AppModule):

	def __init__(self, *args, **kwargs):
		super(splcreator.AppModule, self).__init__(*args, **kwargs)
		# Announce VT Client version at startup unless minimal flag is set.
		try:
			if not globalVars.appArgs.minimal:
				# No translation.
				ui.message("SPL VT Client {SPLVersion}".format(SPLVersion=self.productVersion))
		except:
			pass

	def terminate(self):
		super(splcreator.AppModule, self).terminate()
		# Clear Playlist Editor status cache, otherwise it will generate errors when Remote VT restarts without restarting NVDA.
		self._playlistEditorStatusCache.clear()

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		import controlTypes
		from NVDAObjects.IAccessible import sysListView32
		# 20.02: tracks list uses a different window class name other than "TListView".
		# Resort to window style and other tricks if other lists with the class name below is found and are not tracks list.
		if obj.windowClassName == "TTntListView.UnicodeClass":
			if obj.role == controlTypes.ROLE_LISTITEM:
				clsList.insert(0, SPLRemotePlaylistEditorItem)
			elif obj.role == controlTypes.ROLE_LIST:
				clsList.insert(0, sysListView32.List)
		# Unlike creator, there is no demo intro dialog in Remote VT.
		elif obj.windowClassName == "TAboutForm":
			from NVDAObjects.behaviors import Dialog
			clsList.insert(0, Dialog)

	# The following scripts are designed to work while using Playlist Editor.

	def isPlaylistEditor(self):
		if api.getForegroundObject().windowClassName != "TEditMain":
			ui.message(_("You are not in playlist editor"))
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
