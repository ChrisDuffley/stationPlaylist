
# StationPlaylist Track Tool
# An app module for NVDA
# Copyright 2014 Joseph Lee and contributors, released under gPL.
# Functionality is based on JFW scripts for SPL Track Tool by Brian Hartgen.

import appModuleHandler
import addonHandler
import api
import tones
from controlTypes import ROLE_LIST, ROLE_LISTITEM
addonHandler.initTranslation()
from NVDAObjects.IAccessible import IAccessible
import scriptHandler
import ui

# Track Tool allows a broadcaster to manage track intros, cues and so forth. Each track is a list item with descriptions such as title, file name, intro time and so forth.
# One can press TAB to move along the controls for Track Tool.


class AppModule(appModuleHandler.AppModule):

	def event_gainFocus(self, obj, nextHandler):
		if obj.windowClassName == "TListView" and obj.role == ROLE_LISTITEM:
			# Play a beep when intro exists.
			if ", Intro:" in obj.description:
				tones.beep(550, 100)
		nextHandler()
