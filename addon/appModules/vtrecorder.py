# StationPlaylist VT Recorder
# An app module and global plugin package for NVDA
# Copyright 2018 Joseph Lee and others, released under GPL.

# Basic support for SPL Voice Track Recorder.

import appModuleHandler
import eventHandler
from winUser import user32
from splstudio import spldebugging

class AppModule(appModuleHandler.AppModule):

	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		if user32.FindWindowW(u"SPLStudio", None):
			spldebugging.debugOutput("Studio Recorder is online, attempting to disable background event tracking for Studio")
			# Python 3: using dict.items directly for maximum Python compatibility.
			# #90 (19.01/18.09.6-LTS): use six renames if needed.
			for pid, appMod in appModuleHandler.runningTable.items():
				if appMod.appName == "splstudio":
					# The below function removes background event tracker for apps through accept events set manipulation.
					# Call the function instead of duplicating the function body.
					eventHandler.handleAppTerminate(appMod)
					break
		else:
			spldebugging.debugOutput("Studio is not running")

	def terminate(self):
		super(AppModule, self).terminate()
		if user32.FindWindowW(u"SPLStudio", None):
			spldebugging.debugOutput("Studio Recorder is offline, enabling background event tracking for Studio with Studio active")
			for pid, appMod in appModuleHandler.runningTable.items():
				if appMod.appName == "splstudio":
					eventHandler.requestEvents(eventName="nameChange", processId=pid, windowClassName="TStatusBar")
					eventHandler.requestEvents(eventName="nameChange", processId=pid, windowClassName="TStaticText")
					eventHandler.requestEvents(eventName="show", processId=pid, windowClassName="TRequests")
					break
		else:
			spldebugging.debugOutput("Studio Recorder is offline and Studio is offline")
