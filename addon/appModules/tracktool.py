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

	# Various column reading scripts (row with fake navigation should not be used).

	# Columns headers list:
	# Number: start substring, ending substring.
	columnHeaders = {
		1: ["Title:", ", Duration:"], #Title
		2: ["Duration:", ", Cue:"], #Duration
		3: ["Cue:", ", Overlap:"], #Cue
		4: ["Overlap:", ", Intro:"], #Overlap
		5: ["Intro:", ", Segue:"], #Intro
		6: ["Segue:", ", Filename:"], # Segue
		7: ["Filename:", None] # Actual file name.
	}

	def announceColumnHeader(self, column):
		focus = api.getFocusObject()
		if focus.windowClassName != "TListView" and focus.role != ROLE_LISTITEM:
			ui.message("Not in tracks list")
		else:
			desc = focus.description
			colstr = self.columnHeaders[column][0]
			colstrindex = desc.find(colstr)
			if colstrindex < 0:
				if colstr == "Intro:":
					ui.message("Introduction not set")
				else:
					ui.message("{columnInfo} not found".format(columnInfo = colstr[:-1]))
			else:
				if column != 7:
					colstrend = desc.find(self.columnHeaders[column][1])
				if column != 7:
					columnInfo = desc[colstrindex:colstrend]
				else:
					columnInfo = columnInfo = desc[colstrindex:]
				ui.message(columnInfo)

	def script_announceTitle(self, gesture):
		self.announceColumnHeader(1)

	def script_announceDuration(self, gesture):
		self.announceColumnHeader(2)

	def script_announceCue(self, gesture):
		self.announceColumnHeader(3)

	def script_announceOverlap(self, gesture):
		self.announceColumnHeader(4)

	def script_announceIntro(self, gesture):
		self.announceColumnHeader(5)

	def script_announceSegue(self, gesture):
		self.announceColumnHeader(6)

	def script_announceFilename(self, gesture):
		self.announceColumnHeader(7)

	__gestures={
		"kb:control+NVDA+1":"announceTitle",
		"kb:control+NVDA+2":"announceDuration",
		"kb:control+NVDA+3":"announceCue",
		"kb:control+NVDA+4":"announceOverlap",
		"kb:control+NVDA+5":"announceIntro",
		"kb:control+NVDA+6":"announceSegue",
		"kb:control+NVDA+7":"announceFilename",
	}
