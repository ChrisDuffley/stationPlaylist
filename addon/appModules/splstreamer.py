# StationPlaylist Streamer
# An app module and global plugin package for NVDA
# Copyright 2019 Joseph Lee and others, released under GPL.

# Support for StationPlaylist Straemer
# A standalone app used for broadcast streaming when using something other than Studio for broadcasting.
# For the most part, features are identical to SPL Engine except for Streamer UI workarounds.

from .splengine import *
from NVDAObjects.IAccessible import IAccessible

class TEditNoLabel(IAccessible):

	def _get_name(self):
		return 			"Buffer Size {0} ms".format(self.value)


class AppModule(AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# Try adding labels written to the screen in case edit fields are encountered.
		# After doing this, return immediately so SPL Engine app module can detect encoders.
		if obj.windowClassName == "TEdit" and not obj.name and controlTypes.STATE_READONLY in obj.states:
			clsList.insert(0, TEditNoLabel)
			return
		# Detect encoders.
		# #107 (19.08): for now SPL Utils global plugin will be checked, but in the future, look into supporting encoders via an app module package.
		from globalPlugins.splUtils import encoders
		if obj.windowClassName == "TListView":
			# #87: add support for table navigation commands by coercing encoder list and entries into SysListView32 family.
			if obj.role == controlTypes.ROLE_LISTITEM:
				clsList.insert(0, encoders.SAMEncoder)
			elif obj.role == controlTypes.ROLE_LIST:
				clsList.insert(0, sysListView32.List)
		elif obj.windowClassName == "SysListView32" and obj.role == controlTypes.ROLE_LISTITEM:
			clsList.insert(0, encoders.SPLEncoder)
