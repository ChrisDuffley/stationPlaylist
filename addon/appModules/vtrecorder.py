# StationPlaylist VT Recorder
# An app module and global plugin package for NVDA
# Copyright 2018-2025 Joseph Lee, released under GPL.

# Basic support for SPL Voice Track Recorder.

import appModuleHandler
import eventHandler
from logHandler import log
from .splcommon import splbase


class AppModule(appModuleHandler.AppModule):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		if splbase.studioIsRunning(justChecking=True):
			log.debug("SPL: VT Recorder is online, disabling background event tracking for Studio")
			for appMod in appModuleHandler.runningTable.values():
				if appMod.appName == "splstudio":
					# The below function removes background event tracker for apps through accept events set manipulation.
					# Call the function instead of duplicating the function body.
					eventHandler.handleAppTerminate(appMod)
					break
		else:
			log.debug("SPL: Studio is not running")

	def terminate(self):
		super().terminate()
		if splbase.studioIsRunning(justChecking=True):
			log.debug("SPL: VT Recorder is offline, enabling background event tracking for Studio")
			for pid, appMod in appModuleHandler.runningTable.items():
				if appMod.appName == "splstudio":
					eventHandler.requestEvents(
						eventName="nameChange", processId=pid, windowClassName="TStatusBar"
					)
					eventHandler.requestEvents(
						eventName="nameChange", processId=pid, windowClassName="TStaticText"
					)
					eventHandler.requestEvents(eventName="show", processId=pid, windowClassName="TRequests")
					break
		else:
			log.debug("SPL: Studio Recorder is offline and Studio is offline")
