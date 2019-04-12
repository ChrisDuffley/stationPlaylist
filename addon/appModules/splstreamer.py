# StationPlaylist Streamer
# An app module and global plugin package for NVDA
# Copyright 2019 Joseph Lee and others, released under GPL.

# Support for StationPlaylist Straemer
# A standalone app used for broadcast streaming when using something other than Studio for broadcasting.

import appModuleHandler
import controlTypes
from NVDAObjects.IAccessible import IAccessible

class TEditNoLabel(IAccessible):

	def _get_name(self):
		return 			"Buffer Size {0} ms".format(self.value)


class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# Try adding labels written to the screen in case edit fields are encountered.
		if obj.windowClassName == "TEdit" and not obj.name and controlTypes.STATE_READONLY in obj.states:
			clsList.insert(0, TEditNoLabel)
