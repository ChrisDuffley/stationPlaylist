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
from . import splconfig, splconfui, splactions

addonHandler.initTranslation()


class AppModule(appModuleHandler.AppModule):
	# Translators: Script category for StationPlaylist add-on commands in input gestures dialog.
	scriptCategory = _("StationPlaylist")

	def onAppModuleInit(self) -> None:
		# Perform initialization tasks common across SPL suite.
		# #64: load config database if not done already.
		splconfig.openConfig(self.appName)
		splconfui.initialize()

	def onAppModuleTerminate(self) -> None:
		# Perform termination tasks common across SPL suite.
		# Call action handlers to terminate SPL suite app module subsystems.
		# Among other tasks, close any opened SPL add-on dialogs.
		splactions.SPLActionAppTerminating.notify()
		splconfig.closeConfig(self.appName)
		splconfui.terminate()

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
