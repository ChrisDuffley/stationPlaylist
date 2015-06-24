# StationPlaylist Track Tool
# An app module for NVDA
# Copyright 2014-2015 Joseph Lee and contributors, released under gPL.
# Functionality is based on JFW scripts for SPL Track Tool by Brian Hartgen.

import ctypes
import appModuleHandler
import addonHandler
import api
import tones
import speech
import braille
from controlTypes import ROLE_LISTITEM
import ui
import winKernel
from winUser import sendMessage
from NVDAObjects.IAccessible import IAccessible, sysListView32
from splstudio import splconfig
addonHandler.initTranslation()

# Track Tool allows a broadcaster to manage track intros, cues and so forth. Each track is a list item with descriptions such as title, file name, intro time and so forth.
# One can press TAB to move along the controls for Track Tool.
# The below code is an unoptimized version for add-on 5.0.
# Add-on 5.1 will enable Track Dial, and 6.0 will feature optimized code, deriving from SPL Studio code.

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

			# Add-on 5.1: Track Dial for Track Tool.

	def script_toggleTrackDial(self, gesture):
		if not self.appModule.TTDial:
			self.appModule.TTDial = True
			self.bindGesture("kb:rightArrow", "nextColumn")
			self.bindGesture("kb:leftArrow", "prevColumn")
			dialText = "Track Dial on"
			if self.appModule.SPLColNumber > 0:
				dialText+= ", located at column {columnHeader}".format(columnHeader = self.appModule.SPLColNumber+1)
			dialTone = 780
		else:
			self.appModule.TTDial = False
			try:
				self.removeGestureBinding("kb:rightArrow")
				self.removeGestureBinding("kb:leftArrow")
			except KeyError:
				pass
			dialText = "Track Dial off"
			dialTone = 390
		if not splconfig.SPLConfig["BeepAnnounce"]:
			ui.message(dialText)
		else:
			tones.beep(dialTone, 100)
			braille.handler.message(dialText)
			if self.appModule.TTDial and self.appModule.SPLColNumber > 0:
				speech.speakMessage("Column {columnNumber}".format(columnNumber = self.appModule.SPLColNumber+1))
	# Translators: Input help mode message for SPL track item.
	script_toggleTrackDial.__doc__=_("Toggles track dial on and off.")
	script_toggleTrackDial.category = "StationPlaylist Studio"

	# Locate column content.
	def _getColumnContent(self, col):
	# See main splstudio app module.
		buffer=None
		processHandle=self.processHandle
		sizeofLVITEM = ctypes.sizeof(sysListView32.LVITEM)
		internalItem=winKernel.virtualAllocEx(processHandle,None,sizeofLVITEM,winKernel.MEM_COMMIT,winKernel.PAGE_READWRITE)
		try:
			internalText=winKernel.virtualAllocEx(processHandle,None,520,winKernel.MEM_COMMIT,winKernel.PAGE_READWRITE)
			try:
				item=sysListView32.LVITEM(iItem=self.IAccessibleChildID-1,mask=sysListView32.LVIF_TEXT|sysListView32.LVIF_COLUMNS,iSubItem=col,pszText=internalText,cchTextMax=260)
				winKernel.writeProcessMemory(processHandle,internalItem,ctypes.byref(item),sizeofLVITEM,None)
				len = sendMessage(self.windowHandle,sysListView32.LVM_GETITEMTEXTW, (self.IAccessibleChildID-1), internalItem)
				if len:
					winKernel.readProcessMemory(processHandle,internalItem,ctypes.byref(item),sizeofLVITEM,None)
					buffer=ctypes.create_unicode_buffer(len)
					winKernel.readProcessMemory(processHandle,item.pszText,buffer,ctypes.sizeof(buffer),None)
			finally:
				winKernel.virtualFreeEx(processHandle,internalText,0,winKernel.MEM_RELEASE)
		finally:
			winKernel.virtualFreeEx(processHandle,internalItem,0,winKernel.MEM_RELEASE)
		return buffer.value if buffer else None

	# Tweak for Track Tool: Announce column header if given.
	def announceColumnContent(self, colNumber, columnHeader=None):
		if not columnHeader: columnHeader = self.columnHeaders.children[colNumber].name
		columnContent = self._getColumnContent(colNumber)
		if columnContent:
			ui.message("{header}: {content}".format(header = columnHeader, content = columnContent))
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
	# Add-on 5.0: Keep the below routine.
	# 5.1/6.0: Use SysListView32.

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

	# Up to add-on 5.0.
	def announceColumnHeader(self, column):
		focus = api.getFocusObject()
		if focus.windowClassName not in  ("TListView", "TTntListView.UnicodeClass") and focus.role != ROLE_LISTITEM:
			# Translators: Presented when trying to perform Track Tool commands when not focused in the track list.
			ui.message(_("Not in tracks list"))
		elif focus.name is None and focus.description is None:
			# Translators: Presented when no tracks are added to Track Tool.
			ui.message(_("No tracks added"))
		else:
			if column != 1:
				desc = focus.description
				colstr = self.columnHeaders[column][0]
				if colstr not in desc:
					if colstr == "Intro:":
						# Translators: Presented when intro is not defined for a track in Track Tool.
						columnInfo = _("Introduction not set")
					else:
						# Translators: Presented when some info is not defined for a track in Track Tool (example: cue not found)
						columnInfo = _("{columnInfo} not found").format(columnInfo = colstr[:-1])
				else:
					colstrindex = desc.find(colstr)
					if column == 8:
						columnInfo = desc[colstrindex:]
					else:
						colstrend = colstrindex+desc[colstrindex:].find(self.columnHeaders[column][1])
						columnInfo = desc[colstrindex:colstrend]
			else:
				if focus.name is None:
					# Translators: Presented when artist information is not found for a track in Track Tool.
					columnInfo = _("No artist")
				else:
					# Translators: Presents artist information for a track in Track Tool.
					columnInfo = _("Artist: {artistName}").format(artistName = focus.name)
			ui.message(columnInfo)

	# 5.1: Superseeds column announcement method.
	# 6.0: Cache column header indecies.
	#headerToIndex={}

	"""def announceColumnContent(self, headerText):
		item = api.getFocusObject()
		columnHeaders = item.parent.children[-1].children
		for header in columnHeaders:
			if header.name == headerText:
				pos = columnHeaders.index(header)
		item.announceColumnContent(pos, columnHeader=headerText)"""


	def script_announceArtist(self, gesture):
		self.announceColumnHeader(1)
		#self.announceColumnContent("Artist")

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
