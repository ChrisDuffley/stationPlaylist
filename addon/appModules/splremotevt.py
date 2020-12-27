# StationPlaylist Remote VT Client
# An app module and global plugin package for NVDA
# Copyright 2020-2021 Joseph Lee, released under GPL.

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
	pass


class AppModule(splcreator.AppModule):

	def __init__(self, *args, **kwargs):
		super(splcreator.AppModule, self).__init__(*args, **kwargs)
		# Announce VT Client version at startup unless minimal flag is set.
		try:
			if not globalVars.appArgs.minimal:
				# No translation.
				ui.message("SPL VT Client {SPLVersion}".format(SPLVersion=self.productVersion))
		except Exception:
			pass

	def terminate(self):
		super(splcreator.AppModule, self).terminate()
		# Just like Creator, clear Playlist Editor status cache,
		# otherwise it will generate errors when Remote VT restarts without restarting NVDA.
		self._playlistEditorStatusCache.clear()

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		import controlTypes
		from NVDAObjects.IAccessible import sysListView32
		# 20.02: tracks list uses a different window class name other than "TListView".
		# Resort to window style and other tricks if other lists with the class name below is found
		# yet are not tracks list.
		if obj.windowClassName == "TTntListView.UnicodeClass":
			if obj.role == controlTypes.ROLE_LISTITEM:
				clsList.insert(0, SPLRemotePlaylistEditorItem)
			elif obj.role == controlTypes.ROLE_LIST:
				clsList.insert(0, sysListView32.List)
		# Unlike creator, there is no demo intro dialog in Remote VT.
		elif obj.windowClassName == "TAboutForm":
			from NVDAObjects.behaviors import Dialog
			clsList.insert(0, Dialog)

	# Playlist editor is same as Creator except it responds a bit faster.
	# Without keeping a copy of status cache, NVDA will announce wrong values
	# as Creator app module's cache will be used.
	_playlistEditorStatusCache = {}
