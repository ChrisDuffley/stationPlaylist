# StationPlaylist Track Tool
# An app module for NVDA
# Copyright 2014-2015 Joseph Lee and contributors, released under gPL.
# Functionality is based on JFW scripts for SPL Track Tool by Brian Hartgen.

import appModuleHandler
import addonHandler
import api
import tones
import speech
import braille
from controlTypes import ROLE_LISTITEM
import ui
from NVDAObjects.IAccessible import IAccessible
from splstudio import splconfig
from splstudio.splmisc import _getColumnContent
addonHandler.initTranslation()

# Track Tool allows a broadcaster to manage track intros, cues and so forth. Each track is a list item with descriptions such as title, file name, intro time and so forth.
# One can press TAB to move along the controls for Track Tool.

class TrackToolItem(IAccessible):
	"""An entry in Track Tool, used to implement some exciting features.
	"""

	def reportFocus(self):
		# Play a beep when intro exists.
		if ", Intro:" in self.description:
			tones.beep(550, 100)
		super(TrackToolItem, self).reportFocus()

	def initOverlayClass(self):
		if self.appModule.TTDial:
			self.bindGesture("kb:rightArrow", "nextColumn")
			self.bindGesture("kb:leftArrow", "prevColumn")
		# See if Track Dial toggle for Studio is defined, and if so, pull it in.
		import inputCore
		userGestures = inputCore.manager.userGestureMap._map
		for gesture in userGestures:
			if userGestures[gesture][0][2] == "toggleTrackDial":
				self.bindGesture(gesture, "toggleTrackDial")

			# Track Dial for Track Tool.

	def script_toggleTrackDial(self, gesture):
		if splconfig.SPLConfig is None:
			# Translators: Presented when only Track Tool is running (Track Dial requires Studio to be running as well).
			ui.message(_("Only Track Tool is running, Track Dial is unavailable"))
			return
		if not self.appModule.TTDial:
			self.appModule.TTDial = True
			self.bindGesture("kb:rightArrow", "nextColumn")
			self.bindGesture("kb:leftArrow", "prevColumn")
			dialText = _("Track Dial on")
			if self.appModule.SPLColNumber > 0:
				dialText+= _(", located at column {columnHeader}").format(columnHeader = self.appModule.SPLColNumber+1)
			dialTone = 780
		else:
			self.appModule.TTDial = False
			try:
				self.removeGestureBinding("kb:rightArrow")
				self.removeGestureBinding("kb:leftArrow")
			except KeyError:
				pass
			dialText = _("Track Dial off")
			dialTone = 390
		if not splconfig.SPLConfig["General"]["BeepAnnounce"]:
			ui.message(dialText)
		else:
			tones.beep(dialTone, 100)
			braille.handler.message(dialText)
			if self.appModule.TTDial and self.appModule.SPLColNumber > 0:
				speech.speakMessage("Column {columnNumber}".format(columnNumber = self.appModule.SPLColNumber+1))
	# Translators: Input help mode message for SPL track item.
	script_toggleTrackDial.__doc__=_("Toggles track dial on and off.")
	script_toggleTrackDial.category = _("StationPlaylist Studio")

	# Tweak for Track Tool: Announce column header if given.
	# Also take care of this when specific columns are asked.
	def announceColumnContent(self, colNumber, columnHeader=None, individualColumns=False):
		if not columnHeader: columnHeader = self.columnHeaders.children[colNumber].name
		columnContent = _getColumnContent(self, colNumber)
		if columnContent:
			ui.message("{header}: {content}".format(header = columnHeader, content = columnContent))
		else:
			if individualColumns:
				# Translators: Presented when some info is not defined for a track in Track Tool (example: cue not found)
				ui.message("{header} not found".format(header = columnHeader))
			else:
				speech.speakMessage("{header}: blank".format(header = columnHeader))
				braille.handler.message("{header}: ()".format(header = columnHeader))

	# Now the scripts.

	def script_nextColumn(self, gesture):
		self.columnHeaders = self.parent.children[-1]
		if (self.appModule.SPLColNumber+1) == self.columnHeaders.childCount:
			tones.beep(2000, 100)
		else:
			self.appModule.SPLColNumber +=1
		self.announceColumnContent(self.appModule.SPLColNumber)

	def script_prevColumn(self, gesture):
		self.columnHeaders = self.parent.children[-1]
		if self.appModule.SPLColNumber <= 0:
			tones.beep(2000, 100)
		else:
			self.appModule.SPLColNumber -=1
		self.announceColumnContent(self.appModule.SPLColNumber)

	__gestures={
		#"kb:control+`":"toggleTrackDial",
	}


class AppModule(appModuleHandler.AppModule):

	TTDial = False
	SPLColNumber = 0

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.windowClassName in ("TListView", "TTntListView.UnicodeClass") and obj.role == ROLE_LISTITEM:
			clsList.insert(0, TrackToolItem)

	# Various column reading scripts (row with fake navigation should not be used).
	# 6.0: Cache column header indecies.
	headerToIndex={}

	def announceColumnContent(self, headerText):
		item = api.getFocusObject()
		if not isinstance(item, TrackToolItem):
			# Translators: Presented when trying to perform Track Tool commands when not focused in the track list.
			ui.message(_("Not in tracks list"))
		elif item.name is None and item.description is None:
			# Translators: Presented when no tracks are added to Track Tool.
			ui.message(_("No tracks added"))
		else:
			# Cached values always takes precedence.
			if headerText not in self.headerToIndex:
				columnHeaders = item.parent.children[-1].children
				for header in columnHeaders:
					if header.name == headerText:
						self.headerToIndex[headerText] = columnHeaders.index(header)
			pos = self.headerToIndex[headerText]
			try:
				item.announceColumnContent(pos, columnHeader=headerText)
			except AttributeError:
				ui.message(_("Not in tracks list"))


	def script_announceArtist(self, gesture):
		# Special case for artist field to make it compatible with old add-on releases.
		item = api.getFocusObject()
		if isinstance(item, TrackToolItem):
			if item.name is None:
				# Translators: Presented when artist information is not found for a track in Track Tool.
				ui.message(_("No artist"))
			else:
				# Translators: Presents artist information for a track in Track Tool.
				ui.message(_("Artist: {artistName}").format(artistName = item.name))
		else:
			ui.message(_("Not in tracks list"))

	def script_announceTitle(self, gesture):
		self.announceColumnContent("Title")

	def script_announceDuration(self, gesture):
		self.announceColumnContent("Duration")

	def script_announceCue(self, gesture):
		self.announceColumnContent("Cue")

	def script_announceOverlap(self, gesture):
		self.announceColumnContent("Overlap")

	def script_announceIntro(self, gesture):
		# Special case for intro to make it compatible with old add-on releases.
		item = api.getFocusObject()
		if isinstance(item, TrackToolItem) and "Intro:" not in item.description:
			# Translators: Presented when intro is not defined for a track in Track Tool.
			ui.message(_("Introduction not set"))
		else: self.announceColumnContent("Intro")

	def script_announceSegue(self, gesture):
		self.announceColumnContent("Segue")

	def script_announceFilename(self, gesture):
		self.announceColumnContent("Filename")

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
