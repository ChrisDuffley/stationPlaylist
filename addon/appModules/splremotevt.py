# StationPlaylist Remote VT Client
# An app module and global plugin package for NVDA
# Copyright 2020-2026 Joseph Lee, released under GPL.

# Basic support for StationPlaylist Remote VT Client.
# Borrows heavily from creator as the user interface is quite similar with changes specific to VT Client.

from typing import Any
import addonHandler
import controlTypes
from NVDAObjects import NVDAObject
from NVDAObjects.IAccessible import sysListView32
from NVDAObjects.behaviors import Dialog
from . import splcreator

addonHandler.initTranslation()


class SPLRemotePlaylistEditorItem(splcreator.SPLPlaylistEditorItem):
	"""An entry in SPL VT Remote Playlist Editor."""

	pass


class AppModule(splcreator.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: list[NVDAObject]) -> None:
		# Tracks list uses a different window class name other than "TListView".
		# Resort to window style and other tricks if other lists with the class name below is found
		# yet are not tracks list.
		if obj.windowClassName == "TTntListView.UnicodeClass":
			if obj.role == controlTypes.Role.LISTITEM:
				clsList.insert(0, SPLRemotePlaylistEditorItem)
			elif obj.role == controlTypes.Role.LIST:
				clsList.insert(0, sysListView32.List)
			return
		# Unlike creator, there is no demo intro dialog in Remote VT.
		elif obj.windowClassName == "TAboutForm":
			clsList.insert(0, Dialog)
		super().chooseNVDAObjectOverlayClasses(obj, clsList)

	# Cache status bar objects to improve status bar retrieval performance.
	# This is a separate cache from Creator.
	_statusBarObjs = {}
	# Playlist editor is same as Creator except it responds a bit faster.
	# Without keeping a copy of status cache, NVDA will announce wrong values
	# as Creator app module's cache will be used.
	_playlistEditorStatusCache: dict[int, Any] = {}
