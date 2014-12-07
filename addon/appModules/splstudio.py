# Station Playlist Studio
# An app module and global plugin package for NVDA
# Copyright 2011, 2013-2014, Geoff Shang, Joseph Lee and others, released under GPL.
# The primary function of this appModule is to provide meaningful feedback to users of SplStudio
# by allowing speaking of items which cannot be easily found.
# Version 0.01 - 7 April 2011:
# Initial release: Jamie's focus hack plus auto-announcement of status items.
# Additional work done by Joseph Lee and other contributors.
# For SPL Studio Controller, focus movement, SAM Encoder support and other utilities, see the global plugin version of this app module.

# Minimum version: SPL 5.00, NvDA 2014.3.

from functools import wraps
import os
from configobj import ConfigObj
import time
import threading
import controlTypes
import appModuleHandler
import api
import globalVars
import review
import scriptHandler
import ui
import nvwave
import speech
import braille
import gui
import wx
from winUser import user32, sendMessage
from NVDAObjects.IAccessible import IAccessible
import textInfos
import tones
import addonHandler
addonHandler.initTranslation()

# The finally function for status announcement scripts in this module (source: Tyler Spivey's code).
def finally_(func, final):
	"""Calls final after func, even if it fails."""
	def wrap(f):
		@wraps(f)
		def new(*args, **kwargs):
			try:
				func(*args, **kwargs)
			finally:
				final()
		return new
	return wrap(final)

# Use appModule.productVersion to decide what to do with 4.x and 5.x.
SPLMinVersion = "5.00" # Add-on 4.0 will not work properly in SPL 4.x anymore.

# Configuration management )4.0 and later; will not be ported to 3.x).
SPLConfig = ConfigObj(os.path.join(globalVars.appArgs.configPath, "splstudio.ini"))

# A placeholder thread.
micAlarmT = None

# Braille and play a sound in response to an alarm or an event.
def messageSound(wavFile, message):
	nvwave.playWaveFile(wavFile)
	braille.handler.message(message)

# Controls which require special handling.
class SPL510TrackItem(IAccessible):

	def script_select(self, gesture):
		gesture.send()
		speech.speakMessage(self.name)

	__gestures={"kb:space":"select"}


class AppModule(appModuleHandler.AppModule):

	# Translators: Script category for Station Playlist commands in input gestures dialog.
	scriptCategory = _("Station Playlist Studio")

	# Play beeps instead of announcing toggles.
	beepAnnounce = False
	SPLCurVersion = appModuleHandler.AppModule.productVersion

	def event_NVDAObject_init(self, obj):
		# Radio button group names are not recognized as grouping, so work around this.
		if obj.windowClassName == "TRadioGroup":
			obj.role = controlTypes.ROLE_GROUPING
		# In certain edit fields and combo boxes, the field name is written to the screen, and there's no way to fetch the object for this text. Thus use review position text.
		elif obj.windowClassName in ["TEdit", "TComboBox"] and obj.name is None:
			fieldName, fieldObj  = review.getScreenPosition(obj)
			fieldName.expand(textInfos.UNIT_LINE)
			if obj.windowClassName == "TComboBox":
				obj.name = fieldName.text.replace(obj.windowText, "")
			else:
				obj.name = fieldName.text

	# Some controls which needs special routines.
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		fg = api.getForegroundObject()
		role = obj.role
		if obj.windowClassName == "TTntListView.UnicodeClass" and fg.windowClassName == "TStudioForm" and role == controlTypes.ROLE_LISTITEM and obj.name is not None:
			clsList.insert(0, SPL510TrackItem)

	# populate end of track and intro time alarm settings separately.
	try:
		SPLEndOfTrackTime = SPLConfig["EndOfTrackTime"]
	except KeyError:
		SPLEndOfTrackTime = "00:05"
	try:
		SPLSongRampTime = SPLConfig["SongRampTime"]
	except KeyError:
		SPLSongRampTime = "00:05"
	# Keep an eye on library scans in insert tracks window.
	libraryScanning = False
	scanCount = 0
	# Microphone alarm.
	try:
		micAlarm = int(SPLConfig["MicAlarm"])
	except KeyError:
		micAlarm = 0

	# Automatically announce mic, line in, etc changes
	# These items are static text items whose name changes.
	# Note: There are two status bars, hence the need to exclude Up time so it doesn't announce every minute.
	# Unfortunately, Window handles and WindowControlIDs seem to change, so can't be used.
	def event_nameChange(self, obj, nextHandler):
		# Do not let NvDA get name for None object when SPL window is maximized.
		if not obj.name:
			return
		else:
			if obj.windowClassName == "TStatusBar" and not obj.name.startswith("  Up time:"):
				# Special handling for Play Status
				fgWinClass = api.getForegroundObject().windowClassName
				if obj.IAccessibleChildID == 1:
					if fgWinClass == "TStudioForm":
						# Strip off "  Play status: " for brevity only in main playlist window.
						ui.message(obj.name[15:])
					elif fgWinClass == "TTrackInsertForm" and self.libraryScanProgress > 0:
						# If library scan is in progress, announce its progress.
						self.scanCount+=1
						if self.scanCount%100 == 0:
							if self.libraryScanProgress == self.libraryScanMessage:
								tones.beep(550, 100) if self.beepAnnounce else ui.message("Scanning")
							elif self.libraryScanProgress == self.libraryScanNumbers:
								if self.beepAnnounce: tones.beep(550, 100)
								ui.message(obj.name[1:obj.name.find("]")])
						if "Loading" in obj.name and not self.libraryScanning:
							self.libraryScanning = True
						elif "match" in obj.name and self.libraryScanning:
							tones.beep(370, 100) if self.beepAnnounce else ui.message("Scan complete")
							self.libraryScanning = False
							self.scanCount = 0
				else:
					if self.beepAnnounce:
						# Even with beeps enabled, be sure to announce scheduled time and name of the playing cart.
						if obj.name.startswith("Scheduled for") or obj.name.startswith("Cart") and obj.IAccessibleChildID == 3:
							ui.message(obj.name)
						elif not (obj.name.endswith(" On") or obj.name.endswith(" Off")):
							# Announce status information that does not contain toggle messages.
							ui.message(obj.name)
						else:
							# User wishes to hear beeps instead of words. The beeps are power on and off sounds from PAC Mate Omni.
							beep = obj.name.split(" ")
							stat = beep[-1]
							wavDir = os.path.dirname(__file__)
							# Play a wave file based on on/off status.
							if stat == "Off":
								wavFile = os.path.join(wavDir, "SPL_off.wav")
							elif stat == "On":
								wavFile = os.path.join(wavDir, "SPL_on.wav")
							messageSound(wavFile, obj.name)
					else:
						ui.message(obj.name)
					if self.cartExplorer or self.micAlarm:
						# Activate mic alarm or announce when cart explorer is active.
						self.doExtraAction(obj.name)
			# Monitor the end of track and song intro time and announce it.
			elif obj.windowClassName == "TStaticText": # For future extensions.
				if obj.simplePrevious != None and obj.simplePrevious.name == "Remaining Time":
					# End of track for SPL 5.x.
					if self.brailleTimer in [self.brailleTimerEnding, self.brailleTimerBoth]: #and "00:00" < obj.name <= self.SPLEndOfTrackTime:
						braille.handler.message(obj.name)
					if obj.name == self.SPLEndOfTrackTime:
						tones.beep(440, 200)
				elif obj.simplePrevious != None and obj.simplePrevious.name == "Remaining Song Ramp":
					# Song intro for SPL 5.x.
					if self.brailleTimer in [self.brailleTimerIntro, self.brailleTimerBoth]: #and "00:00" < obj.name <= self.SPLSongRampTime:
						braille.handler.message(obj.name)
					if obj.name == self.SPLSongRampTime:
						tones.beep(512, 400)
			# Clean this mess with a more elegant solution.
		nextHandler()

	# JL's additions

	# Perform extra action in specific situations (mic alarm, for example).
	def doExtraAction(self, status):
		global micAlarmT
		if self.cartExplorer:	
			if status == "Cart Edit On":
				# Translators: Presented when cart edit mode is toggled on while cart explorer is on.
				ui.message(_("Cart explorer is active"))
			elif status == "Cart Edit Off":
				# Translators: Presented when cart edit mode is toggled off while cart explorer is on.
				ui.message(_("Please reenter cart explorer to view updated cart assignments"))
		if self.micAlarm:
			# Play an alarm sound from Braille Sense U2.
			micAlarmWav = os.path.join(os.path.dirname(__file__), "SPL_MicAlarm.wav")
			# Translators: Presented in braille when microphone was on for more than a specified time in microphone alarm dialog.
			micAlarmMessage = _("Warning: Microphone active")
			# Use a timer to play a tone when microphone was active for more than the specified amount.
			if status == "Microphone On":
				micAlarmT = threading.Timer(self.micAlarm, messageSound, args=[micAlarmWav, micAlarmMessage])
				try:
					micAlarmT.start()
				except RuntimeError:
					micAlarmT = threading.Timer(self.micAlarm, messageSound, args=[micAlarmWav, micAlarmMessage])
					micAlarmT.start()
			elif status == "Microphone Off":
				if micAlarmT is not None: micAlarmT.cancel()
				micAlarmT = None


				# Continue monitoring library scans among other focus loss management.
	def event_loseFocus(self, obj, nextHandler):
		fg = api.getForegroundObject()
		if fg.windowClassName == "TTrackInsertForm":
			if self.libraryScanning: self.monitorLibraryScan()
		nextHandler()

	# Save configuration when terminating.
	def terminate(self):
		global SPLConfig
		if SPLConfig is not None: SPLConfig.write()

	# Script sections (for ease of maintenance):
	# Time-related: elapsed time, end of track alarm, etc.
	# Misc scripts: track finder and others.
	# SPL Assistant layer: status commands.

	# A few time related scripts (elapsed time, remaining time, etc.).

	# Time location constants for SPL 5.x.
	SPLElapsedTime = 3
	SPLBroadcasterTime = 13
	SPLCompleteTime = 15

	# Speak any time-related errors.
	# Message type: error message.
	timeMessageErrors={
		# Translators: Presented when remaining time is unavailable.
		1:_("Remaining time not available"),
		# Translators: Presented when elapsed time is unavailable.
		2:_("Elapsed time not available"),
		# Translators: Presented when broadcaster time is unavailable.
			3:_("Broadcaster time not available"),
		# Translators: Presented when time information is unavailable.
		4:_("Cannot obtain time in hours, minutes and seconds")
	}

	# Let the scripts call the below time message function to reduce code duplication and to improve readability.
	def timeMessage(self, messageType, timeObj, timeObjChild=0):
		fgWindow = api.getForegroundObject()
		if fgWindow.windowClassName == "TStudioForm":
			if timeObjChild == 0:
				obj = fgWindow.children[timeObj].firstChild
			else: obj = fgWindow.children[timeObj].children[timeObjChild]
			msg = obj.name
		else:
			msg = self.timeMessageErrors[messageType]
		ui.message(msg)

	def script_sayRemainingTime(self, gesture):
		if self.SPLCurVersion >= SPLMinVersion :
			self.timeMessage(1, 2, timeObjChild=1)
		else:
			# Translators: Presented when trying to use an add-on command in an unsupported version of StationPlaylist Studio.
			ui.message(_("This version of Studio is no longer supported"))
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayRemainingTime.__doc__=_("Announces the remaining track time.")

	def script_sayElapsedTime(self, gesture):
		if self.SPLCurVersion >= SPLMinVersion :
			self.timeMessage(2, self.SPLElapsedTime, timeObjChild=1)
		else:
			ui.message(_("This version of Studio is no longer supported"))
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayElapsedTime.__doc__=_("Announces the elapsed time for the currently playing track.")

	def script_sayBroadcasterTime(self, gesture):
		# Says things such as "25 minutes to 2" and "5 past 11".
		if self.SPLCurVersion >= SPLMinVersion :
			self.timeMessage(3, self.SPLBroadcasterTime)
		else:
			ui.message(_("This version of Studio is no longer supported"))
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayBroadcasterTime.__doc__=_("Announces broadcaster time.")

	def script_sayCompleteTime(self, gesture):
		# Says complete time in hours, minutes and seconds.
		if self.SPLCurVersion >= SPLMinVersion :
			self.timeMessage(4, self.SPLCompleteTime)
		else:
			ui.message(_("This version of Studio is no longer supported"))
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayCompleteTime.__doc__=_("Announces time including seconds.")

	# Set the end of track alarm time between 1 and 59 seconds.

	def script_setEndOfTrackTime(self, gesture):
		timeVal = long(self.SPLEndOfTrackTime[-2:])
		# Translators: A dialog message to set end of track alarm (curAlarmSec is the current end of track alarm in seconds).
		timeMSG = _("Enter end of track alarm time in seconds (currently {curAlarmSec})").format(curAlarmSec = timeVal)
		dlg = wx.NumberEntryDialog(gui.mainFrame,
		timeMSG, "",
		# Translators: The title of end of track alarm dialog.
		_("End of track alarm"),
		timeVal, 1, 59)
		def callback(result):
			global SPLConfig
			if result == wx.ID_OK:
				if dlg.GetValue() <= 9: newAlarmSec = "0" + str(dlg.GetValue())
				else: newAlarmSec = str(dlg.GetValue())
				self.SPLEndOfTrackTime = self.SPLEndOfTrackTime.replace(self.SPLEndOfTrackTime[-2:], newAlarmSec)
				# Just in case the ini file doesn't exist.
				if SPLConfig is not None: SPLConfig["EndOfTrackTime"] = self.SPLEndOfTrackTime
		gui.runScriptModalDialog(dlg, callback)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_setEndOfTrackTime.__doc__=_("sets end of track alarm (default is 5 seconds).")

	# Set song ramp (introduction) time between 1 and 9 seconds.

	def script_setSongRampTime(self, gesture):
		rampVal = self.SPLSongRampTime[-2:]
		# Translators: A dialog message to set song ramp alarm (curRampSec is the current intro monitoring alarm in seconds).
		timeMSG = _("Enter song intro alarm time in seconds (currently {curRampSec})").format(curRampSec = rampVal if int(rampVal) >= 10 else rampVal[-1])
		dlg = wx.TextEntryDialog(gui.mainFrame,
		timeMSG,
		# Translators: The title of song intro alarm dialog.
		_("Song intro alarm"),
		defaultValue=rampVal if int(rampVal) >= 10 else rampVal[-1])
		def callback(result):
			if result == wx.ID_OK:
				if not dlg.GetValue().isdigit() or int(dlg.GetValue()) < 1 or int(dlg.GetValue()) > 9:
					# Translators: The error message presented when incorrect alarm time value has been entered.
					wx.CallAfter(gui.messageBox, _("Incorrect value entered."),
					# Translators: Standard title for error dialog (copy this from main nvda.po file).
					_("Error"),wx.OK|wx.ICON_ERROR)
				else:
					newAlarmSec = "0" + dlg.GetValue()
					self.SPLSongRampTime = self.SPLSongRampTime.replace(self.SPLSongRampTime[-2:], newAlarmSec)
					if SPLConfig is not None: SPLConfig["SongRampTime"] = self.SPLSongRampTime
		gui.runScriptModalDialog(dlg, callback)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_setSongRampTime.__doc__=_("sets song intro alarm (default is 5 seconds).")

# Tell NVDA to play a sound when mic was active for a long time.

	def script_setMicAlarm(self, gesture):
		if self.micAlarm:
			# Translators: A dialog message to set microphone active alarm (curAlarmSec is the current mic monitoring alarm in seconds).
			timeMSG = _("Enter microphone alarm time in seconds (currently {curAlarmSec}, 0 disables the alarm)").format(curAlarmSec = self.micAlarm)
		else:
			# Translators: A dialog message when microphone alarm is disabled (set to 0).
			timeMSG = _("Enter microphone alarm time in seconds (currently disabled, 0 disables the alarm)")
		dlg = wx.TextEntryDialog(gui.mainFrame,
		timeMSG,
		# Translators: The title of mic alarm dialog.
		_("Microphone alarm"),
		defaultValue=str(self.micAlarm))
		def callback(result):
			if result == wx.ID_OK:
				if not dlg.GetValue().isdigit():
					# Translators: The error message presented when incorrect alarm time value has been entered.
					wx.CallAfter(gui.messageBox, _("Incorrect value entered."),
					# Translators: Standard title for error dialog (copy this from main nvda.po file).
					_("Error"),wx.OK|wx.ICON_ERROR)
				else:
					self.micAlarm = int(dlg.GetValue())
					if SPLConfig is not None: SPLConfig["MicAlarm"] = self.micAlarm
		gui.runScriptModalDialog(dlg, callback)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_setMicAlarm.__doc__=_("Sets microphone alarm (default is 5 seconds).")

	# Other commands (track finder and others)

	# Toggle whether beeps should be heard instead of toggle announcements.

	def script_toggleBeepAnnounce(self, gesture):
		if not self.beepAnnounce:
			self.beepAnnounce = True
			# Translators: Reported when toggle announcement is set to beeps in SPL Studio.
			ui.message(_("Toggle announcement beeps"))
		else:
			self.beepAnnounce = False
			# Translators: Reported when toggle announcement is set to words in SPL Studio.
			ui.message(_("Toggle announcement words"))
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_toggleBeepAnnounce.__doc__=_("Toggles option change announcements between words and beeps.")

	# Braille timer.
	# Announce end of track and other info via braille.
	brailleTimer = 0
	brailleTimerEnding = 1
	brailleTimerIntro = 2
	brailleTimerBoth = 3 # Both as in intro and track ending.

	# Braille timer settings list and the toggle script.
	brailleTimerSettings=(
		# Translators: A setting in braille timer options.
		(_("Braille timer off")),
		# Translators: A setting in braille timer options.
		(_("Braille track endings")),
		# Translators: A setting in braille timer options.
		(_("Braille intro endings")),
		# Translators: A setting in braille timer options.
		(_("Braille intro and track endings"))
	)

	def script_setBrailleTimer(self, gesture):
		self.brailleTimer= self.brailleTimer+1 if self.brailleTimer < len(self.brailleTimerSettings)-1 else 0
		ui.message(self.brailleTimerSettings[self.brailleTimer])
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_setBrailleTimer.__doc__=_("Toggles between various braille timer settings.")

	# The track finder utility for find track script.
	# Perform a linear search to locate the track name and/or description which matches the entered value.
	findText = ""

	def trackFinder(self, text, obj, directionForward=True):
		while obj is not None:
			if text in obj.description or (obj.name and text in obj.name and self.productVersion < "5.10"):
				self.findText = text
				# We need to fire set focus event twice and exit this routine.
				obj.setFocus(), obj.setFocus()
				return
			else:
				obj = obj.next if directionForward else obj.previous
		wx.CallAfter(gui.messageBox,
		# Translators: Standard dialog message when an item one wishes to search is not found (copy this from main nvda.po).
		_("Search string not found."),
		# Translators: Standard error title for find error (copy this from main nvda.po).
		_("Find error"),wx.OK|wx.ICON_ERROR)

	# Find a specific track based on a searched text.
	# Unfortunately, the track list does not provide obj.name (it is None), however obj.description has the actual track entry.

	def script_findTrack(self, gesture):
		if api.getForegroundObject().windowClassName != "TStudioForm":
			# Translators: Presented when a user attempts to find tracks but is not at the track list.
			ui.message(_("Track finder is available only in track list."))
		elif api.getForegroundObject().windowClassName == "TStudioForm" and api.getFocusObject().role == controlTypes.ROLE_LIST:
			# Translators: Presented when a user wishes to find a track but didn't add any tracks.
			ui.message(_("You need to add at least one track to find tracks."))
		else:
			startObj = api.getFocusObject()
			# Translators: The text of the dialog for finding tracks.
			searchMSG = _("Enter the name of the track you wish to search.")
			dlg = wx.TextEntryDialog(gui.mainFrame,
			searchMSG,
			# Translators: The title of the find tracks dialog.
			_("Find track"), defaultValue=self.findText)
			def callback(result):
				if result == wx.ID_OK:
					if dlg.GetValue() is None: return
					elif dlg.GetValue() == self.findText: self.trackFinder(dlg.GetValue(), startObj.next)
					else: self.trackFinder(dlg.GetValue(), startObj)
			gui.runScriptModalDialog(dlg, callback)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_findTrack.__doc__=_("Finds a track in the track list.")

	# Find next and previous scripts.

	def script_findTrackNext(self, gesture):
		if api.getForegroundObject().windowClassName != "TStudioForm": ui.message(_("Track finder is available only in track list."))
		elif api.getForegroundObject().windowClassName == "TStudioForm" and api.getFocusObject().role == controlTypes.ROLE_LIST: ui.message(_("You need to add at least one track to find tracks."))
		else:
			if self.findText == "": self.script_findTrack(gesture)
			else: self.trackFinder(self.findText, api.getFocusObject().next)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_findTrackNext.__doc__=_("Finds the next occurrence of the track with the name in the track list.")

	def script_findTrackPrevious(self, gesture):
		if api.getForegroundObject().windowClassName != "TStudioForm": ui.message(_("Track finder is available only in track list."))
		elif api.getForegroundObject().windowClassName == "TStudioForm" and api.getFocusObject().role == controlTypes.ROLE_LIST: ui.message(_("You need to add at least one track to find tracks."))
		else:
			if self.findText == "":
				self.script_findTrack(gesture)
			else: self.trackFinder(self.findText, api.getFocusObject().previous, directionForward=False)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_findTrackPrevious.__doc__=_("Finds previous occurrence of the track with the name in the track list.")

	# Cart explorer
	cartExplorer = False
	carts = {} # The carts dictionary (key = cart gesture, item = cart name).

	# Assigning carts.

	def buildFNCarts(self):
		# Used xrange, as it is much faster; change this to range if NvDA core decides to use Python 3.
		for i in xrange(12):
			self.bindGesture("kb:f%s"%(i+1), "cartExplorer")
			self.bindGesture("kb:shift+f%s"%(i+1), "cartExplorer")
			self.bindGesture("kb:control+f%s"%(i+1), "cartExplorer")
			self.bindGesture("kb:alt+f%s"%(i+1), "cartExplorer")

	def buildNumberCarts(self):
		for i in xrange(10):
			self.bindGesture("kb:%s"%(i), "cartExplorer")
			self.bindGesture("kb:shift+%s"%(i), "cartExplorer")
			self.bindGesture("kb:control+%s"%(i), "cartExplorer")
			self.bindGesture("kb:alt+%s"%(i), "cartExplorer")
		# Take care of dash and equals.
		self.bindGesture("kb:-", "cartExplorer"), self.bindGesture("kb:=", "cartExplorer")
		self.bindGesture("kb:shift+-", "cartExplorer"), self.bindGesture("kb:shift+=", "cartExplorer")
		self.bindGesture("kb:control+-", "cartExplorer"), self.bindGesture("kb:control+=", "cartExplorer")
		self.bindGesture("kb:alt+-", "cartExplorer"), self.bindGesture("kb:alt+=", "cartExplorer")

	def cartsBuilder(self, build=True):
		# A function to build and return cart commands.
		if build:
			self.buildFNCarts()
			self.buildNumberCarts()
		else:
			self.clearGestureBindings()
			self.bindGestures(self.__gestures)

	def cartsStr2Carts(self, cartEntry, modifier, n):
		# Parse the cart entry string and insert the cart/cart name pairs into the carts dictionary.
		# n between 1 and 12 = function carts, 13 through 24 = number row carts, modifiers are checked.
		# If a cart name has commas or other characters, SPL surrounds the cart name with quotes (""), so parse it as well.
		if not cartEntry.startswith('""'): cartName = cartEntry.split(",")[0]
		else: cartName = cartEntry.split('""')[1]
		if n <= 12: identifier = "f"+str(n)
		elif 12 < n < 22: identifier = str(n-12)
		elif n == 22: identifier = "0"
		elif n == 23: identifier = "-"
		else: identifier = "="
		if modifier == "": cart = identifier
		elif modifier == "ctrl": cart = "control+%s"%identifier
		else: cart = "%s+%s"%(modifier, identifier)
		self.carts[cart] = cartName

	def cartsReader(self):
		# Use cart files in SPL's data folder to build carts dictionary.
		# use a combination of SPL user name and static cart location to locate cart bank files.
		# Once the cart banks are located, use the routines in the populate method below to assign carts.
		# Todo: refactor this function by splitting it into several functions.
		def _populateCarts(c, modifier):
			# The real cart string parser, a helper for cart explorer for building cart entries.
			cartlst = c.split("\",\"") # c = cart text.
			# Get rid of unneeded quotes in cart entries.
			cartlst[0], cartlst[-1] = cartlst[0][1:], cartlst[-1][:-1]
			n = 0 # To keep track of how many entries were processed, also used to detect license type.
			for i in cartlst:
				n+=1
				# An unassigned cart is stored with three consecutive commas, so skip it.
				if ",,," in i: continue
				else: self.cartsStr2Carts(i, modifier, n) # See the comment on str2carts for more information.
			return n
		# Back at the reader, locate the cart files and process them.
		# Obtain the "real" path for SPL via environment variables and open the cart data folder.
		cartsDataPath = os.path.join(os.environ["PROGRAMFILES"],"StationPlaylist","Data") # Provided that Studio was installed using default path.
		# See if multiple users are using SPl Studio.
		userName = api.getForegroundObject().name
		userNameIndex = userName.find("-")
		# Read *.cart files and process the cart entries within (be careful when these cart file names change between SPL releases).
		cartFiles = [u"main carts.cart", u"shift carts.cart", u"ctrl carts.cart", u"alt carts.cart"]
		if userNameIndex >= 0:
			cartFiles = [userName[userNameIndex+2:]+" "+cartFile for cartFile in cartFiles]
		cartReadSuccess = True # Just in case some or all carts were not read successfully.
		cartCount = 0 # Count how many cart assignments are possible.
		for f in cartFiles:
			try:
				mod = f.split()[-2] # Checking for modifier string such as ctrl.
				# Todo: Check just in case some SPL flavors doesn't ship with a particular cart file.
			except IndexError:
				cartReadSuccess = False # In a rare event that the broadcaster has saved the cart bank with the name like "carts.cart".
				continue
			cartFile = os.path.join(cartsDataPath,f)
			if not os.path.isfile(cartFile): # Cart explorer will fail if whitespaces are in the beginning or at the end of a user name.
				cartReadSuccess = False
				continue
			cartInfo = open(cartFile)
			cl = cartInfo.readlines() # cl = cart list.
			cartInfo.close()
			del cl[0] # Throw away the empty line (again be careful if the cart file format changes in a future release).
			preprocessedCarts = cl[0].strip()
			cartCount += _populateCarts(preprocessedCarts, "") if mod == "main" else _populateCarts(preprocessedCarts, mod) # See the comment for _populate method above.
		return cartReadSuccess, cartCount

	def script_toggleCartExplorer(self, gesture):
		if not self.cartExplorer:
			cartsRead, cartCount = self.cartsReader()
			if not cartsRead:
				# Translators: presented when cart explorer could not be switched on.
				ui.message(_("Some or all carts could not be assigned, cannot enter cart explorer"))
				return
			else:
				self.cartExplorer = True
				self.cartsBuilder()
				self.carts["standardLicense"] = True if cartCount < 96 else False
				# Translators: Presented when cart explorer is on.
				ui.message(_("Entering cart explorer"))
		else:
			self.cartExplorer = False
			self.cartsBuilder(build=False)
			self.carts.clear()
			# Translators: Presented when cart explorer is off.
			ui.message(_("Exiting cart explorer"))
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_toggleCartExplorer.__doc__=_("Toggles cart explorer to learn cart assignments.")

	def script_cartExplorer(self, gesture):
		if scriptHandler.getLastScriptRepeatCount() >= 1: gesture.send()
		else:
			if gesture.displayName in self.carts: ui.message(self.carts[gesture.displayName])
			elif self.carts["standardLicense"] and (len(gesture.displayName) == 1 or gesture.displayName[-2] == "+"):
				# Translators: Presented when cart command is unavailable.
				ui.message(_("Cart command unavailable"))
			else:
				# Translators: Presented when there is no cart assigned to a cart command.
				ui.message(_("Cart unassigned"))

	# Library scan announcement
	# Announces progress of a library scan (launched from insert tracks dialog by pressing Control+Shift+R or from rescan option from Options dialog).
	libraryScanProgress = 0 # Announce at the beginning and at the end of a scan.
	libraryScanMessage = 2 # Just announce "scanning".
	libraryScanNumbers = 3 # Announce number of items scanned.

	# Library scan announcement settings list and the toggle script.
	libraryProgressSettings=(
		# Translators: A setting in library scan announcement options.
		(_("Do not announce library scans")),
		# Translators: A setting in library scan announcement options.
		(_("Announce start and end of a library scan")),
		# Translators: A setting in library scan announcement options.
		(_("Announce the progress of a library scan")),
		# Translators: A setting in library scan announcement options.
		(_("Announce progress and item count of a library scan"))
	)

	def script_setLibraryScanProgress(self, gesture):
		self.libraryScanProgress = self.libraryScanProgress+1 if self.libraryScanProgress < len(self.libraryProgressSettings)-1 else 0
		ui.message(self.libraryProgressSettings[self.libraryScanProgress])
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_setLibraryScanProgress.__doc__=_("Toggles library scan progress settings.")

	def script_startScanFromInsertTracks(self, gesture):
		gesture.send()
		fg = api.getForegroundObject()
		if fg.windowClassName == "TTrackInsertForm":
			# Translators: Presented when library scan has started.
			ui.message(_("Scan start"))
			self.libraryScanning = True

	# Report library scan (number of items scanned) in the background.
	def monitorLibraryScan(self):
		SPLWin = user32.FindWindowA("SPLStudio", None)
		countA = sendMessage(SPLWin, 1024, 0, 32)
		time.sleep(0.1)
		countB = sendMessage(SPLWin, 1024, 0, 32)
		if countA == countB:
			self.libraryScanning = False
			# Translators: Presented when library scanning is finished.
			ui.message(_("{itemCount} items in the library").format(itemCount = countB))
		else:
			t = threading.Thread(target=self.libraryScanReporter, args=(SPLWin, countA, countB))
			t.name = "SPLLibraryScanReporter"
			t.daemon = True
			t.start()

	def libraryScanReporter(self, SPLWin, countA, countB):
		scanIter = 0
		while countA != countB:
			countA = countB
			time.sleep(1)
			# Do not continue if we're back on insert tracks form.
			if api.getForegroundObject().windowClassName == "TTrackInsertForm":
				return
			countB, scanIter = sendMessage(SPLWin, 1024, 0, 32), scanIter+1
			if scanIter%5 == 0:
				if self.libraryScanProgress == self.libraryScanMessage:
					# Translators: Presented when library scan is in progress.
					tones.beep(550, 100) if self.beepAnnounce else ui.message(_("Scanning"))
				elif self.libraryScanProgress == self.libraryScanNumbers:
					if self.beepAnnounce:
						tones.beep(550, 100)
						ui.message("{itemCount}".format(itemCount = countB))
					else: ui.message(_("{itemCount} items scanned").format(itemCount = countB))
		self.libraryScanning = False
		if self.libraryScanProgress:
			if self.beepAnnounce: tones.beep(370, 100)
			else:
				# Translators: Presented after library scan is done.
				ui.message(_("Scan complete with {itemCount} items").format(itemCount = countB))

	# SPL Assistant: reports status on playback, operation, etc.
	# Used layer command approach to save gesture assignments.
	# Most were borrowed from JFW and Window-Eyes layer scripts.

	# Set up the layer script environment.
	def getScript(self, gesture):
		if not self.SPLAssistant:
			return appModuleHandler.AppModule.getScript(self, gesture)
		script = appModuleHandler.AppModule.getScript(self, gesture)
		if not script:
			script = finally_(self.script_error, self.finish)
		return finally_(script, self.finish)

	def finish(self):
		self.SPLAssistant = False
		self.clearGestureBindings()
		self.bindGestures(self.__gestures)
		if self.cartExplorer:
			self.buildFNCarts()
			self.buildNumberCarts()

	def script_error(self, gesture):
		tones.beep(120, 100)

	# SPL Assistant flag.
	SPLAssistant = False

	# The SPL Assistant layer driver.

	def script_SPLAssistantToggle(self, gesture):
		# Enter the layer command if an only if we're in the track list to allow easier gesture assignment.
		if api.getForegroundObject().windowClassName != "TStudioForm":
			gesture.send()
			return
		if self.SPLAssistant:
			self.script_error(gesture)
			return
		# To prevent entering wrong gesture while the layer is active.
		self.clearGestureBindings()
		self.bindGestures(self.__SPLAssistantGestures)
		self.SPLAssistant = True
		tones.beep(512, 10)
	# Translators: Input help mode message for a layer command in Station Playlist Studio.
	script_SPLAssistantToggle.__doc__=_("The SPL Assistant layer command. See the add-on guide for more information on available commands.")

	# Status table keys
	SPLPlayStatus = 0
	SPLSystemStatus = 1
	SPLHourTrackDuration = 2
	SPLHourSelectedDuration = 3
	SPLNextTrackTitle = 4
	SPLPlaylistRemainingDuration = 5
	SPLTemperature = 6
	SPLScheduled = 7

	# Table of child constants based on versions
	# These are scattered throughout the screen, so one can use foreground.children[index] to fetch them.
	# Because 4.x and 5.x (an perhaps future releases) uses different screen layout, look up the needed constant from the table below (row = info needed, column = version).
	statusObjs={
		SPLPlayStatus:[0, 5], # Play status, mic, etc.
		SPLSystemStatus:[-2, -3], # The second status bar containing system status such as up time.
		SPLHourTrackDuration:[13, 17], # For track duration for the given hour marker.
		SPLHourSelectedDuration:[14, 18], # In case the user selects one or more tracks in a given hour.
		SPLScheduled:[15, 19], # Time when the selected track will begin.
		SPLNextTrackTitle:[2, 7], # Name and duration of the next track if any.
		SPLPlaylistRemainingDuration:[12, 16], # Remaining time for the current playlist.
		SPLTemperature:[1, 6], # Temperature for the current city.
	}

	# Called in the layer commands themselves.
	def status(self, infoIndex):
		ver, fg = self.productVersion, api.getForegroundObject()
		if ver.startswith("4"): statusObj = self.statusObjs[infoIndex][0]
		elif ver.startswith("5"): statusObj = self.statusObjs[infoIndex][1]
		return fg.children[statusObj]

	# The layer commands themselves.

	def script_sayPlayStatus(self, gesture):
		obj = self.status(self.SPLPlayStatus).children[0]
		ui.message(obj.name)

	def script_sayAutomationStatus(self, gesture):
		obj = self.status(self.SPLPlayStatus).children[1]
		ui.message(obj.name)

	def script_sayMicStatus(self, gesture):
		obj = self.status(self.SPLPlayStatus).children[2]
		ui.message(obj.name)

	def script_sayLineInStatus(self, gesture):
		obj = self.status(self.SPLPlayStatus).children[3]
		ui.message(obj.name)

	def script_sayRecToFileStatus(self, gesture):
		obj = self.status(self.SPLPlayStatus).children[4]
		ui.message(obj.name)

	def script_sayCartEditStatus(self, gesture):
		obj = self.status(self.SPLPlayStatus).children[5]
		ui.message(obj.name)

	def script_sayHourTrackDuration(self, gesture):
		obj = self.status(self.SPLHourTrackDuration).firstChild
		ui.message(obj.name)

	def script_sayHourSelectedTrackDuration(self, gesture):
		obj = self.status(self.SPLHourSelectedDuration).firstChild
		ui.message(obj.name)

	def script_sayPlaylistRemainingDuration(self, gesture):
		obj = self.status(self.SPLPlaylistRemainingDuration).children[1]
		ui.message(obj.name)

	def script_sayPlaylistModified(self, gesture):
		try:
			obj = self.status(self.SPLSystemStatus).children[5]
			ui.message(obj.name)
		except IndexError:
			# Translators: Presented when playlist modification is unavailable (for Studio 4.33 and earlier)
			ui.message(_("Playlist modification not available"))

	def script_sayNextTrackTitle(self, gesture):
		obj = self.status(self.SPLNextTrackTitle).firstChild
		# Translators: Presented when there is no information for the next track.
		ui.message(_("No next track scheduled or no track is playing")) if obj.name is None else ui.message(obj.name)

	def script_sayTemperature(self, gesture):
		obj = self.status(self.SPLTemperature).firstChild
		# Translators: Presented when there is nn weather or temperature information.
		ui.message(_("Weather and temperature not configured")) if obj.name is None else ui.message(obj.name)

	def script_sayUpTime(self, gesture):
		obj = self.status(self.SPLSystemStatus).firstChild
		ui.message(obj.name)

	def script_sayScheduledTime(self, gesture):
		obj = self.status(self.SPLScheduled).firstChild
		ui.message(obj.name)

	def script_sayListenerCount(self, gesture):
		obj = self.status(self.SPLSystemStatus).children[3]
		# Translators: Presented when there is no listener count information.
		ui.message(obj.name) if obj.name is not None else ui.message(_("Listener count not found"))

	def script_sayTrackPitch(self, gesture):
		try:
			obj = self.status(self.SPLSystemStatus).children[4]
			ui.message(obj.name)
		except IndexError:
			# Translators: Presented when there is no information on song pitch (for Studio 4.33 and earlier).
			ui.message(_("Song pitch not available"))

	# Few toggle/misc scripts that may be excluded from the layer later.

	def script_libraryScanMonitor(self, gesture):
		if self.productVersion < "5.10":
			if not self.libraryScanning:
				self.libraryScanning = True
				# Translators: Presented when attempting to start library scan.
				ui.message(_("Monitoring library scan"))
				self.monitorLibraryScan()
			else:
				# Translators: Presented when library scan is already in progress.
				ui.message(_("Scanning is in progress"))
		else:
			# In 5.10, library scan count returns total count.
			SPLWin = user32.FindWindowA("SPLStudio", None)
			items = sendMessage(SPLWin, 1024, 0, 32)
			ui.message(_("{itemCount} items in the library").format(itemCount = items))


	__SPLAssistantGestures={
		"kb:p":"sayPlayStatus",
		"kb:a":"sayAutomationStatus",
		"kb:m":"sayMicStatus",
		"kb:l":"sayLineInStatus",
		"kb:r":"sayRecToFileStatus",
		"kb:t":"sayCartEditStatus",
		"kb:h":"sayHourTrackDuration",
		"kb:shift+h":"sayHourSelectedTrackDuration",
		"kb:d":"sayPlaylistRemainingDuration",
		"kb:y":"sayPlaylistModified",
		"kb:u":"sayUpTime",
		"kb:n":"sayNextTrackTitle",
		"kb:w":"sayTemperature",
		"kb:i":"sayListenerCount",
		"kb:s":"sayScheduledTime",
		"kb:shift+p":"sayTrackPitch",
		"kb:shift+r":"libraryScanMonitor"
	}

	__gestures={
		"kb:control+alt+t":"sayRemainingTime",
		"kb:alt+shift+t":"sayElapsedTime",
		"kb:shift+nvda+f12":"sayBroadcasterTime",
		"kb:control+nvda+1":"toggleBeepAnnounce",
		"kb:control+nvda+2":"setEndOfTrackTime",
		"kb:alt+nvda+2":"setSongRampTime",
		"kb:control+nvda+4":"setMicAlarm",
		"kb:control+nvda+f":"findTrack",
		"kb:nvda+f3":"findTrackNext",
		"kb:shift+nvda+f3":"findTrackPrevious",
		"kb:control+nvda+3":"toggleCartExplorer",
		"kb:alt+nvda+r":"setLibraryScanProgress",
		"kb:control+shift+r":"startScanFromInsertTracks",
		"kb:control+shift+x":"setBrailleTimer",
		#"kb:control+nvda+`":"SPLAssistantToggle"
	}
