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
		if obj.windowClassName in ["TListView", "TTntListView.UnicodeClass"] and obj.role == ROLE_LISTITEM:
			# Play a beep when intro exists.
			if ", Intro:" in obj.description:
				tones.beep(550, 100)
		nextHandler()

	# Various column reading scripts (row with fake navigation should not be used).

	# Columns headers list:
	# Number: start substring, ending substring.
	columnHeaders = {
		2: ["Title:", ", Duration:"], #Title
		3: ["Duration:", ", "], #Duration
		4: ["Cue:", ", "], #Cue
		5: ["Overlap:", ", "], #Overlap
		6: ["Intro:", ", "], #Intro
		7: ["Segue:", ", "], # Segue
		8: ["Filename:", None] # Actual file name.
	}

	def announceColumnHeader(self, column):
		focus = api.getFocusObject()
		if focus.windowClassName != "TListView" and focus.role != ROLE_LISTITEM:
			ui.message("Not in tracks list")
		elif focus.name is None and focus.description is None:
			ui.message("No tracks added")
		else:
			if column != 1:
				desc = focus.description
				colstr = self.columnHeaders[column][0]
				if colstr not in desc:
					if colstr == "Intro:":
						columnInfo = "Introduction not set"
					else:
						columnInfo = "{columnInfo} not found".format(columnInfo = colstr[:-1])
				else:
					colstrindex = desc.find(colstr)
					if column == 8:
						columnInfo = desc[colstrindex:]
					else:
						colstrend = colstrindex+desc[colstrindex:].find(self.columnHeaders[column][1])
						columnInfo = desc[colstrindex:colstrend]
			else:
				if focus.name is None:
					columnInfo = "No artist"
				else:
					columnInfo = "Artist: {artistName}".format(artistName = focus.name)
			ui.message(columnInfo)

	def script_announceArtist(self, gesture):
		self.announceColumnHeader(1)

	def script_announceTitle(self, gesture):
		self.announceColumnHeader(2)

	def script_announceDuration(self, gesture):
		self.announceColumnHeader(3)

	def script_announceCue(self, gesture):
		self.announceColumnHeader(4)

	def script_announceOverlap(self, gesture):
		self.announceColumnHeader(5)

	def script_announceIntro(self, gesture):
		self.announceColumnHeader(6)

	def script_announceSegue(self, gesture):
		self.announceColumnHeader(7)

	def script_announceFilename(self, gesture):
		self.announceColumnHeader(8)

	__gestures={
		"kb:control+NVDA+1":"announceArtist",
		"kb:control+NVDA+2":"announceTitle",
		"kb:control+NVDA+3":"announceDuration",
		"kb:control+NVDA+4":"announceCue",
		"kb:control+NVDA+5":"announceOverlap",
		"kb:control+NVDA+6":"announceIntro",
		"kb:control+NVDA+7":"announceSegue",
		"kb:control+NVDA+8":"announceFilename",
	}
