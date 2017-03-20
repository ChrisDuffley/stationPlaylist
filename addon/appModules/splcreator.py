# StationPlaylist Creator
# An app module and global plugin package for NVDA
# Copyright 2016-2017 Joseph Lee and others, released under GPL.

# Basic support for StationPlaylist Creator.

import appModuleHandler


class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.windowClassName in ("TDemoRegForm", "TAboutForm"):
			from NVDAObjects.behaviors import Dialog
			clsList.insert(0, Dialog)
