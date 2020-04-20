# StationPlaylist Streamer
# An app module and global plugin package for NVDA
# Copyright 2019-2020 Joseph Lee and others, released under GPL.

# Support for StationPlaylist Straemer
# A standalone app used for broadcast streaming when using something other than Studio for broadcasting.
# For the most part, features are identical to SPL Engine except for Streamer UI workarounds.

from .splengine import *
from NVDAObjects.IAccessible import IAccessible


class TEditNoLabel(IAccessible):

	def _get_name(self):
		return "Buffer Size {0} ms".format(self.value)


class AppModule(AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# Try adding labels written to the screen in case edit fields are encountered.
		# After doing this, return immediately so SPL Engine app module can detect encoders.
		if obj.windowClassName == "TEdit" and not obj.name and controlTypes.STATE_READONLY in obj.states:
			clsList.insert(0, TEditNoLabel)
			return
		# #107 (19.08): the rest is defined in SPL Engine app module.
		super(AppModule, self).chooseNVDAObjectOverlayClasses(obj, clsList)
