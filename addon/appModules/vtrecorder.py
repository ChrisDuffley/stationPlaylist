# StationPlaylist VT Recorder
# An app module and global plugin package for NVDA
# Copyright 2018-2021 Joseph Lee, released under GPL.

# Basic support for SPL Voice Track Recorder.

import appModuleHandler
import eventHandler
import globalVars
from winUser import user32
from logHandler import log


# 22.03 (security): disable the app module altogether in secure mode.
def secureModeAware(cls):
	return appModuleHandler.AppModule if globalVars.appArgs.secure else cls


@secureModeAware
class AppModule(appModuleHandler.AppModule):

	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		if user32.FindWindowW("SPLStudio", None):
			log.debug("SPL: VT Recorder is online, disabling background event tracking for Studio")
			# Python 3: using dict.items directly for maximum Python compatibility.
			# #90 (19.01/18.09.6-LTS): use Six renames if needed.
			for pid, appMod in appModuleHandler.runningTable.items():
				if appMod.appName == "splstudio":
					# The below function removes background event tracker for apps through accept events set manipulation.
					# Call the function instead of duplicating the function body.
					eventHandler.handleAppTerminate(appMod)
					break
		else:
			log.debug("SPL: Studio is not running")

	def terminate(self):
		super(AppModule, self).terminate()
		if user32.FindWindowW("SPLStudio", None):
			log.debug("SPL: VT Recorder is offline, enabling background event tracking for Studio")
			for pid, appMod in appModuleHandler.runningTable.items():
				if appMod.appName == "splstudio":
					eventHandler.requestEvents(eventName="nameChange", processId=pid, windowClassName="TStatusBar")
					eventHandler.requestEvents(eventName="nameChange", processId=pid, windowClassName="TStaticText")
					eventHandler.requestEvents(eventName="show", processId=pid, windowClassName="TRequests")
					break
		else:
			log.debug("SPL: Studio Recorder is offline and Studio is offline")
