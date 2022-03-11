# StationPlaylist Streamer
# An app module and global plugin package for NVDA
# Copyright 2019-2021 Joseph Lee, released under GPL.

# Support for StationPlaylist Straemer
# A standalone app used for broadcast streaming when using something other than Studio for broadcasting.
# For the most part, features are identical to SPL Engine except for Streamer UI workarounds.

# An alias of SPL Engine app module with UI workarounds, so inform linters such as Flake8.
from .splengine import *  # NOQA: F403
import globalVars
from NVDAObjects.IAccessible import IAccessible


class TEditNoLabel(IAccessible):

	def _get_name(self):
		return "Buffer Size {0} ms".format(self.value)


# 22.03 (security): disable the app module altogether in secure mode.
def disableInSecureMode(cls):
	return appModuleHandler.AppModule if globalVars.appArgs.secure else cls


# #155 (21.03): AppModule base class comes from SPL Engine app module but Mypy doesn't know that.
# On the other hand, Flake8 says parts of the below line are undefined, so ignore it.
@disableInSecureMode
class AppModule(AppModule):  # type: ignore[no-redef]  # NOQA: F405

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		import controlTypes
		# Try adding labels written to the screen in case edit fields are encountered.
		# After doing this, return immediately so SPL Engine app module can detect encoders.
		if obj.windowClassName == "TEdit" and not obj.name and controlTypes.State.READONLY in obj.states:
			clsList.insert(0, TEditNoLabel)
			return
		# #107 (19.08): the rest is defined in SPL Engine app module.
		super(AppModule, self).chooseNVDAObjectOverlayClasses(obj, clsList)
