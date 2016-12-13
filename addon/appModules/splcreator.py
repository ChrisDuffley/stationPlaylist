# StationPlaylist Creator
# An app module and global plugin package for NVDA
# Copyright 2016, Joseph Lee and others, released under GPL.

import controlTypes
import appModuleHandler
import api
from NVDAObjects.behaviors import Dialog
import addonHandler
addonHandler.initTranslation()


class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.windowClassName in ("TDemoRegForm", "TAboutForm"):
			clsList.insert(0, Dialog)
