# SPL Studio base app module
# An app module and global plugin package for NVDA
# Copyright 2026 Joseph Lee, released under GPL.

# Base blueprint app module for StationPlaylist
# Provides common app module attributes and methods across SPL suite of apps.
# Mostly based on local Studio app module.

import appModuleHandler
import addonHandler
import scriptHandler
import wx
from . import splconfui

addonHandler.initTranslation()


class AppModule(appModuleHandler.AppModule):
	# Translators: Script category for StationPlaylist add-on commands in input gestures dialog.
	scriptCategory = _("StationPlaylist")

	# SPL Config management among others.

	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Opens SPL Studio add-on configuration dialog."),
		gesture="kb:alt+NVDA+0",
	)
	def script_openConfigDialog(self, gesture):
		# Rather than calling the config dialog open event,
		# call the open dialog function directly to avoid indirection.
		wx.CallAfter(splconfui.openAddonSettingsPanel, None)
