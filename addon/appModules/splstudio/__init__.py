# StationPlaylist Studio
# An app module and global plugin package for NVDA
# Copyright 2011, 2013-2015, Geoff Shang, Joseph Lee and others, released under GPL.
# The primary function of this appModule is to provide meaningful feedback to users of SplStudio
# by allowing speaking of items which cannot be easily found.
# Version 0.01 - 7 April 2011:
# Initial release: Jamie's focus hack plus auto-announcement of status items.
# Additional work done by Joseph Lee and other contributors.
# For SPL Studio Controller, focus movement, SAM Encoder support and other utilities, see the global plugin version of this app module.

# Minimum version: SPL 5.00, NvDA 2015.3.

from functools import wraps
import os
import time
import threading
import controlTypes
import appModuleHandler
import api
import globalVars
import review
import eventHandler
import scriptHandler
import ui
import nvwave
import speech
import braille
import touchHandler
import gui
import wx
from winUser import user32, sendMessage
import winKernel
from NVDAObjects.IAccessible import IAccessible
import textInfos
import tones
import splconfig
import splmisc
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

# Make sure the broadcaster is running a compatible version.
SPLMinVersion = "5.00"

# Cache the handle to main Studio window.
_SPLWin = None

# Threads pool.
micAlarmT = None
libScanT = None

# Blacklisted versions of Studio where library scanning functionality is broken.
noLibScanMonitor = []

# List of known window style values to check for track items in Studio 5.0x..
known50styles = (1442938953, 1443987529, 1446084681)
known51styles = (1443991625, 1446088777)

# Braille and play a sound in response to an alarm or an event.
def messageSound(wavFile, message):
	nvwave.playWaveFile(wavFile)
	braille.handler.message(message)

# Call SPL API to obtain needed values.
# A thin wrapper around user32.SendMessage and calling a callback if defined.
# Offset is used in some time commands.
def statusAPI(arg, command, func=None, ret=False, offset=None):
	if _SPLWin is None: return
	val = sendMessage(_SPLWin, 1024, arg, command)
	if ret:
		return val
	if func:
		func(val) if not offset else func(val, offset)

# Routines for track items themselves (prepare for future work).
class SPLTrackItem(IAccessible):
	"""Track item for earlier versions of Studio such as 5.00.
	A base class for providing utility scripts when track entries are focused, such as track dial."""

	def initOverlayClass(self):
		if splconfig.SPLConfig["TrackDial"]:
			self.bindGesture("kb:rightArrow", "nextColumn")
			self.bindGesture("kb:leftArrow", "prevColumn")

	# Read selected columns.
	# But first, find where the requested column lives.
	def _indexOf(self, columnHeader):
		if self.appModule._columnHeaders is None:
			self.appModule._columnHeaders = self.parent.children[-1]
		headers = [header.name for header in self.appModule._columnHeaders.children]
		return headers.index(columnHeader)

	def reportFocus(self):
		tones.beep(800, 100)
		if not splconfig.SPLConfig["UseScreenColumnOrder"]:
			descriptionPieces = []
			for header in splconfig.SPLConfig["ColumnOrder"]:
				if header in splconfig.SPLConfig["IncludedColumns"]:
					index = self._indexOf(header)
					content = self._getColumnContent(index)
					if content:
						descriptionPieces.append("%s: %s"%(header, content))
			self.description = ", ".join(descriptionPieces)
		super(IAccessible, self).reportFocus()

	# Track Dial: using arrow keys to move through columns.
	# This is similar to enhanced arrow keys in other screen readers.

	def script_toggleTrackDial(self, gesture):
		if not splconfig.SPLConfig["TrackDial"]:
			splconfig.SPLConfig["TrackDial"] = True
			self.bindGesture("kb:rightArrow", "nextColumn")
			self.bindGesture("kb:leftArrow", "prevColumn")
			# Translators: Reported when track dial is on.
			dialText = _("Track Dial on")
			if self.appModule.SPLColNumber > 0:
				# Translators: Announced when located on a column other than the leftmost column while using track dial.
				dialText+= _(", located at column {columnHeader}").format(columnHeader = self.appModule.SPLColNumber+1)
			dialTone = 780
		else:
			splconfig.SPLConfig["TrackDial"] = False
			try:
				self.removeGestureBinding("kb:rightArrow")
				self.removeGestureBinding("kb:leftArrow")
			except KeyError:
				pass
			# Translators: Reported when track dial is off.
			dialText = _("Track Dial off")
			dialTone = 390
		if not splconfig.SPLConfig["BeepAnnounce"]:
			ui.message(dialText)
		else:
			tones.beep(dialTone, 100)
			braille.handler.message(dialText)
			if splconfig.SPLConfig["TrackDial"] and self.appModule.SPLColNumber > 0:
				# Translators: Spoken when enabling track dial while status message is set to beeps.
				speech.speakMessage(_("Column {columnNumber}").format(columnNumber = self.appModule.SPLColNumber+1))
	# Translators: Input help mode message for SPL track item.
	script_toggleTrackDial.__doc__=_("Toggles track dial on and off.")
	script_toggleTrackDial.category = _("StationPlaylist Studio")

	# Some helper functions to handle corner cases.
	# Each track item provides its own version.
	def _leftmostcol(self):
		if self.appModule._columnHeaders is None:
			self.appModule._columnHeaders = self.parent.children[-1]
		leftmost = self.appModule._columnHeaders.firstChild.name
		if not self.name or self.name == "":
			# Translators: Announced when leftmost column has no text while track dial is active.
			ui.message(_("{leftmostColumn} not found").format(leftmostColumn = leftmost))
		else:
			# Translators: Standard message for announcing column content.
			ui.message(_("{leftmostColumn}: {leftmostContent}").format(leftmostColumn = self.columnHeaders.children[self.appModule.SPLColNumber].name, leftmostContent = self.name))

	# Locate column content.
	# This is merely the proxy of the module level function defined in the misc module.
	def _getColumnContent(self, col):
		return splmisc._getColumnContent(self, col)

	# Announce column content if any.
	def announceColumnContent(self, colNumber):
		columnHeader = self.appModule._columnHeaders.children[colNumber].name
		columnContent = self._getColumnContent(colNumber)
		if columnContent:
			# Translators: Standard message for announcing column content.
			ui.message(unicode(_("{header}: {content}")).format(header = columnHeader, content = columnContent))
		else:
			# Translators: Spoken when column content is blank.
			speech.speakMessage(_("{header}: blank").format(header = columnHeader))
			# Translators: Brailled to indicate empty column content.
			braille.handler.message(_("{header}: ()").format(header = columnHeader))

	# Now the scripts.

	def script_nextColumn(self, gesture):
		if self.appModule._columnHeaders is None:
			self.appModule._columnHeaders = self.parent.children[-1]
		if (self.appModule.SPLColNumber+1) == self.appModule._columnHeaders.childCount:
			tones.beep(2000, 100)
		else:
			self.appModule.SPLColNumber +=1
		self.announceColumnContent(self.appModule.SPLColNumber)

	def script_prevColumn(self, gesture):
		if self.appModule._columnHeaders is None:
			self.appModule._columnHeaders = self.parent.children[-1]
		if self.appModule.SPLColNumber <= 0:
			tones.beep(2000, 100)
		else:
			self.appModule.SPLColNumber -=1
		if self.appModule.SPLColNumber == 0:
			self._leftmostcol()
		else:
			self.announceColumnContent(self.appModule.SPLColNumber)

	__gestures={
		#"kb:control+`":"toggleTrackDial",
	}

class SPL510TrackItem(SPLTrackItem):
	""" Track item for Studio 5.10 and later."""

	def script_select(self, gesture):
		gesture.send()
		speech.speakMessage(self.name)
		braille.handler.handleUpdate(self)

	# Handle track dial for SPL 5.10.
	def _leftmostcol(self):
		if not self.name:
			# Translators: Presented when no track status is found in Studio 5.10.
			ui.message(_("Status not found"))
		else:
			# Translators: Status information for a checked track in Studio 5.10.
			ui.message(_("Status: {name}").format(name = self.name))

	__gestures={"kb:space":"select"}

# Translators: The text of the help command in SPL Assistant layer.
SPLAssistantHelp=_("""After entering SPL Assistant, press:
A: Automation.
C: Announce name of the currently playing track.
D: Remaining time for the playlist.
H: Duration of trakcs in this hour slot.
Shift+H: Duration of selected tracks.
I: Listener count.
L: Line-in status.
M: Microphone status.
N: Next track.
P: Playback status.
Shift+P: Pitch for the current track.
R: Record to file.
Shift+R: Monitor library scan.
S: Scheduled time for the track.
T: Cart edit mode.
U: Studio up time.
W: Weather and temperature.
Y: Playlist modification.
F9: Mark current track as start of track time analysis.
F10: Perform track time analysis.
F12: Switch to an instant switch profile.
Shift+F1: Open online user guide.""")


class AppModule(appModuleHandler.AppModule):

	# Translators: Script category for Station Playlist commands in input gestures dialog.
	scriptCategory = _("StationPlaylist Studio")
	SPLCurVersion = appModuleHandler.AppModule.productVersion
	_columnHeaders = None

	# Prepare the settings dialog among other things.
	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		if self.SPLCurVersion < SPLMinVersion:
			raise RuntimeError("Unsupported version of Studio is running, exiting app module")
		# Translators: The sign-on message for Studio app module.
		try:
			ui.message(_("Using SPL Studio version {SPLVersion}").format(SPLVersion = self.SPLCurVersion))
		except IOError:
			pass
		splconfig.initConfig()
		# Announce status changes while using other programs.
		# This requires NVDA core support and will be available in 6.0 and later (cannot be ported to earlier versions).
		# For now, handle all background events, but in the end, make this configurable.
		if hasattr(eventHandler, "requestEvents"):
			eventHandler.requestEvents(eventName="nameChange", processId=self.processID, windowClassName="TStatusBar")
			eventHandler.requestEvents(eventName="nameChange", processId=self.processID, windowClassName="TStaticText")
			self.backgroundStatusMonitor = True
		else:
			self.backgroundStatusMonitor = False
		self.prefsMenu = gui.mainFrame.sysTrayIcon.preferencesMenu
		self.SPLSettings = self.prefsMenu.Append(wx.ID_ANY, _("SPL Studio Settings..."), _("SPL settings"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, splconfig.onConfigDialog, self.SPLSettings)
		# Let me know the Studio window handle.
		threading.Thread(target=self._locateSPLHwnd).start()

	# Locate the handle for main window for caching purposes.
	def _locateSPLHwnd(self):
		hwnd = user32.FindWindowA("SPLStudio", None)
		while not hwnd:
			time.sleep(1)
			hwnd = user32.FindWindowA("SPLStudio", None)
		# Only this thread will have privilege of notifying handle's existence.
		with threading.Lock() as hwndNotifier:
			global _SPLWin
			_SPLWin = hwnd

	# Let the global plugin know if SPLController passthrough is allowed.
	def SPLConPassthrough(self):
		return splconfig.SPLConfig["SPLConPassthrough"]

	def event_NVDAObject_init(self, obj):
		# Radio button group names are not recognized as grouping, so work around this.
		if obj.windowClassName == "TRadioGroup":
			obj.role = controlTypes.ROLE_GROUPING
		# In certain edit fields and combo boxes, the field name is written to the screen, and there's no way to fetch the object for this text. Thus use review position text.
		elif obj.windowClassName in ("TEdit", "TComboBox") and not obj.name:
			fieldName, fieldObj  = review.getScreenPosition(obj)
			fieldName.expand(textInfos.UNIT_LINE)
			if obj.windowClassName == "TComboBox":
				obj.name = fieldName.text.replace(obj.windowText, "")
			else:
				obj.name = fieldName.text

	# Some controls which needs special routines.
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		role = obj.role
		windowStyle = obj.windowStyle
		if obj.windowClassName == "TTntListView.UnicodeClass" and role == controlTypes.ROLE_LISTITEM and abs(windowStyle - 1443991625)%0x100000 == 0:
			clsList.insert(0, SPL510TrackItem)
		elif obj.windowClassName == "TListView" and role in (controlTypes.ROLE_CHECKBOX, controlTypes.ROLE_LISTITEM) and abs(windowStyle - 1442938953)%0x100000 == 0:
			clsList.insert(0, SPLTrackItem)

	# Keep an eye on library scans in insert tracks window.
	libraryScanning = False
	scanCount = 0
	# For SPL 5.10: take care of some object child constant changes across builds.
	spl510used = False
	# For 5.0X and earlier: prevent NVDA from announcing scheduled time multiple times.
	scheduledTimeCache = ""
	# Track Dial (A.K.A. enhanced arrow keys)
	SPLColNumber = 0

	# Automatically announce mic, line in, etc changes
	# These items are static text items whose name changes.
	# Note: There are two status bars, hence the need to exclude Up time so it doesn't announce every minute.
	# Unfortunately, Window handles and WindowControlIDs seem to change, so can't be used.
	# Only announce changes if told to do so via the following function.
	def _TStatusBarChanged(self, obj):
		name = obj.name
		if name.startswith("  Up time:"):
			return False
		elif name.startswith("Scheduled for"):
			if self.scheduledTimeCache == name: return False
			self.scheduledTimeCache = name
			return splconfig.SPLConfig["SayScheduledFor"]
		elif "Listener" in name:
			return splconfig.SPLConfig["SayListenerCount"]
		elif name.startswith("Cart") and obj.IAccessibleChildID == 3:
			return splconfig.SPLConfig["SayPlayingCartName"]
		return True

	# Now the actual event.
	def event_nameChange(self, obj, nextHandler):
		# Do not let NvDA get name for None object when SPL window is maximized.
		if not obj.name:
			return
		# Only announce changes in status bar objects when told to do so.
		if obj.windowClassName == "TStatusBar" and self._TStatusBarChanged(obj):
			# Special handling for Play Status
			if obj.IAccessibleChildID == 1:
				if "Play status" in obj.name:
					# Strip off "  Play status: " for brevity only in main playlist window.
					ui.message(obj.name.split(":")[1][1:])
				elif "Loading" in obj.name:
					if splconfig.SPLConfig["LibraryScanAnnounce"] not in ("off", "ending"):
						# If library scan is in progress, announce its progress when told to do so.
						self.scanCount+=1
						if self.scanCount%100 == 0:
							self._libraryScanAnnouncer(obj.name[1:obj.name.find("]")], splconfig.SPLConfig["LibraryScanAnnounce"])
					if not self.libraryScanning:
						if self.productVersion not in noLibScanMonitor:
							if not self.backgroundStatusMonitor: self.libraryScanning = True
				elif "match" in obj.name:
					if splconfig.SPLConfig["LibraryScanAnnounce"] != "off" and self.libraryScanning:
						if splconfig.SPLConfig["BeepAnnounce"]: tones.beep(370, 100)
						else:
							ui.message("Scan complete with {scanCount} items".format(scanCount = obj.name.split()[3]))
					if self.libraryScanning: self.libraryScanning = False
					self.scanCount = 0
			else:
				if obj.name.endswith((" On", " Off")) and splconfig.SPLConfig["BeepAnnounce"]:
					# User wishes to hear beeps instead of words. The beeps are power on and off sounds from PAC Mate Omni.
					beep = obj.name.split()
					stat = beep[-1]
					wavDir = os.path.dirname(__file__)
					# Play a wave file based on on/off status.
					if stat == "Off":
						wavFile = os.path.join(wavDir, "SPL_off.wav")
					elif stat == "On":
						wavFile = os.path.join(wavDir, "SPL_on.wav")
					# Yet another Studio 5.10 fix: sometimes, status bar fires this event once more.
					try:
						messageSound(wavFile, obj.name)
					except:
						return
				else:
					ui.message(obj.name)
				if self.cartExplorer or int(splconfig.SPLConfig["MicAlarm"]):
					# Activate mic alarm or announce when cart explorer is active.
					self.doExtraAction(obj.name)
		# Monitor the end of track and song intro time and announce it.
		elif obj.windowClassName == "TStaticText": # For future extensions.
			if obj.simplePrevious != None:
				if obj.simplePrevious.name == "Remaining Time":
					# End of track for SPL 5.x.
					if splconfig.SPLConfig["BrailleTimer"] in ("outro", "both") and api.getForegroundObject().processID == self.processID: #and "00:00" < obj.name <= self.SPLEndOfTrackTime:
						braille.handler.message(obj.name)
					if (obj.name == "00:{0:02d}".format(splconfig.SPLConfig["EndOfTrackTime"])
					and splconfig.SPLConfig["SayEndOfTrack"]):
						self.alarmAnnounce(obj.name, 440, 200)
				elif obj.simplePrevious.name == "Remaining Song Ramp":
					# Song intro for SPL 5.x.
					if splconfig.SPLConfig["BrailleTimer"] in ("intro", "both") and api.getForegroundObject().processID == self.processID: #and "00:00" < obj.name <= self.SPLSongRampTime:
						braille.handler.message(obj.name)
					if (obj.name == "00:{0:02d}".format(splconfig.SPLConfig["SongRampTime"])
					and splconfig.SPLConfig["SaySongRamp"]):
						self.alarmAnnounce(obj.name, 512, 400, intro=True)
		nextHandler()

	# JL's additions

	# Perform extra action in specific situations (mic alarm, for example).
	def doExtraAction(self, status):
		micAlarm = int(splconfig.SPLConfig["MicAlarm"])
		if self.cartExplorer:
			if status == "Cart Edit On":
				# Translators: Presented when cart edit mode is toggled on while cart explorer is on.
				ui.message(_("Cart explorer is active"))
			elif status == "Cart Edit Off":
				# Translators: Presented when cart edit mode is toggled off while cart explorer is on.
				ui.message(_("Please reenter cart explorer to view updated cart assignments"))
		if micAlarm:
			# Play an alarm sound from Braille Sense U2.
			global micAlarmT
			micAlarmWav = os.path.join(os.path.dirname(__file__), "SPL_MicAlarm.wav")
			# Translators: Presented in braille when microphone was on for more than a specified time in microphone alarm dialog.
			micAlarmMessage = _("Warning: Microphone active")
			# Use a timer to play a tone when microphone was active for more than the specified amount.
			if status == "Microphone On":
				micAlarmT = threading.Timer(micAlarm, messageSound, args=[micAlarmWav, micAlarmMessage])
				try:
					micAlarmT.start()
				except RuntimeError:
					micAlarmT = threading.Timer(micAlarm, messageSound, args=[micAlarmWav, micAlarmMessage])
					micAlarmT.start()
			elif status == "Microphone Off":
				if micAlarmT is not None: micAlarmT.cancel()
				micAlarmT = None

	# Alarm announcement: Alarm notification via beeps, speech or both.
	def alarmAnnounce(self, timeText, tone, duration, intro=False):
		if splconfig.SPLConfig["AlarmAnnounce"] in ("beep", "both"):
			tones.beep(tone, duration)
		if splconfig.SPLConfig["AlarmAnnounce"] in ("message", "both"):
			alarmTime = int(timeText.split(":")[1])
			if intro:
				ui.message("Warning: {seconds} sec left in track introduction".format(seconds = str(alarmTime)))
			else:
				ui.message("Warning: {seconds} sec remaining".format(seconds = str(alarmTime)))


	# Hacks for gain focus events.
	def event_gainFocus(self, obj, nextHandler):
		if self.deletedFocusObj or (obj.windowClassName == "TListView" and obj.role == 0):
			self.deletedFocusObj = False
			return
		nextHandler()

	# Add or remove SPL-specific touch commands.
	# Code comes from Enhanced Touch Gestures add-on from the same author.
	# This may change if NVDA core decides to abandon touch mode concept.

	def event_appModule_gainFocus(self):
		if touchHandler.handler:
			if "SPL" not in touchHandler.availableTouchModes:
				touchHandler.availableTouchModes.append("SPL")
				# Add the human-readable representation also.
				touchHandler.touchModeLabels["spl"] = _("SPL mode")

	def event_appModule_loseFocus(self):
		if touchHandler.handler:
			# Switch to object mode.
			touchHandler.handler._curTouchMode = touchHandler.availableTouchModes[1]
			if "SPL" in touchHandler.availableTouchModes:
				# If we have too many touch modes, pop all except the original entries.
				for mode in touchHandler.availableTouchModes:
					if mode == "SPL": touchHandler.availableTouchModes.pop()
			try:
				del touchHandler.touchModeLabels["spl"]
			except KeyError:
				pass


	# Save configuration when terminating.
	def terminate(self):
		super(AppModule, self).terminate()
		splconfig.saveConfig()
		try:
			self.prefsMenu.RemoveItem(self.SPLSettings)
		except AttributeError, wx.PyDeadObjectError:
			pass
		# Manually clear the following dictionaries.
		self.carts.clear()
		self._cachedStatusObjs.clear()
		# Just to make sure:
		global _SPLWin
		if _SPLWin: _SPLWin = None


	# Script sections (for ease of maintenance):
	# Time-related: elapsed time, end of track alarm, etc.
	# Misc scripts: track finder and others.
	# SPL Assistant layer: status commands.

	# A few time related scripts (elapsed time, remaining time, etc.).

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

	# Specific to time scripts using Studio API.
	# 6.0: Split this into two functions: the announcer (below) and formatter.
	def announceTime(self, t, offset = None):
		if t <= 0:
			ui.message("00:00")
		else:
			ui.message(self._ms2time(t, offset = offset))

	# Formatter: given time in milliseconds, convert it to human-readable format.
	def _ms2time(self, t, offset = None):
		if t <= 0:
			return "00:00"
		else:
			tm = (t/1000) if not offset else (t/1000)+offset
			timeComponents = divmod(tm, 60)
			tm1 = str(timeComponents[0]).zfill(2)
			tm2 = str(timeComponents[1]).zfill(2)
			return ":".join([tm1, tm2])

	# Scripts which rely on API.
	def script_sayRemainingTime(self, gesture):
		fgWindow = api.getForegroundObject()
		if fgWindow.windowClassName == "TStudioForm":
			statusAPI(3, 105, self.announceTime, offset=1)
		else:
			ui.message(self.timeMessageErrors[1])
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayRemainingTime.__doc__=_("Announces the remaining track time.")

	def script_sayElapsedTime(self, gesture):
		fgWindow = api.getForegroundObject()
		if fgWindow.windowClassName == "TStudioForm":
			statusAPI(0, 105, self.announceTime)
		else:
			ui.message(self.timeMessageErrors[2])
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayElapsedTime.__doc__=_("Announces the elapsed time for the currently playing track.")

	def script_sayBroadcasterTime(self, gesture):
		# Says things such as "25 minutes to 2" and "5 past 11".
		fgWindow = api.getForegroundObject()
		if fgWindow.windowClassName == "TStudioForm":
			# Parse the local time and say it similar to how Studio presents broadcaster time.
			h, m = time.localtime()[3], time.localtime()[4]
			if h not in (0, 12):
				h %= 12
			if m == 0:
				if h == 0: h+=12
				# Messages in this method should not be translated.
				broadcasterTime = "{hour} o'clock".format(hour = h)
			elif 1 <= m <= 30:
				if h == 0: h+=12
				broadcasterTime = "{minute} min past {hour}".format(minute = m, hour = h)
			else:
				if h == 12: h = 1
				m = 60-m
				broadcasterTime = "{minute} min to {hour}".format(minute = m, hour = h+1)
			ui.message(broadcasterTime)
		else:
			ui.message(self.timeMessageErrors[3])
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayBroadcasterTime.__doc__=_("Announces broadcaster time.")

	def script_sayCompleteTime(self, gesture):
		# Says complete time in hours, minutes and seconds via kernel32's routines.
		if api.getForegroundObject().windowClassName == "TStudioForm":
			ui.message(winKernel.GetTimeFormat(winKernel.LOCALE_USER_DEFAULT, 0, None, None))
		else:
			ui.message(self.timeMessageErrors[4])
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayCompleteTime.__doc__=_("Announces time including seconds.")

	# Set the end of track alarm time between 1 and 59 seconds.
	# Make sure one of either settings or alarm dialogs is open.

	def script_setEndOfTrackTime(self, gesture):
		if splconfig._configDialogOpened:
			# Translators: Presented when the add-on config dialog is opened.
			wx.CallAfter(gui.messageBox, _("The add-on settings dialog is opened. Please close the settings dialog first."), _("Error"), wx.OK|wx.ICON_ERROR)
			return
		try:
			timeVal = splconfig.SPLConfig["EndOfTrackTime"]
			d = splconfig.SPLAlarmDialog(gui.mainFrame, "EndOfTrackTime", "SayEndOfTrack",
			# Translators: The title of end of track alarm dialog.
			_("End of track alarm"),
			# Translators: A dialog message to set end of track alarm (curAlarmSec is the current end of track alarm in seconds).
			_("Enter &end of track alarm time in seconds (currently {curAlarmSec})").format(curAlarmSec = timeVal),
			# Translators: A check box to toggle notification of end of track alarm.
			_("&Notify when end of track is approaching"), 1, 59)
			gui.mainFrame.prePopup()
			d.Raise()
			d.Show()
			gui.mainFrame.postPopup()
			splconfig._alarmDialogOpened = True
		except RuntimeError:
			wx.CallAfter(splconfig._alarmError)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_setEndOfTrackTime.__doc__=_("sets end of track alarm (default is 5 seconds).")

	# Set song ramp (introduction) time between 1 and 9 seconds.

	def script_setSongRampTime(self, gesture):
		if splconfig._configDialogOpened:
			wx.CallAfter(gui.messageBox, _("The add-on settings dialog is opened. Please close the settings dialog first."), _("Error"), wx.OK|wx.ICON_ERROR)
			return
		try:
			rampVal = long(splconfig.SPLConfig["SongRampTime"])
			d = splconfig.SPLAlarmDialog(gui.mainFrame, "SongRampTime", "SaySongRamp",
			# Translators: The title of song intro alarm dialog.
			_("Song intro alarm"),
			# Translators: A dialog message to set song ramp alarm (curRampSec is the current intro monitoring alarm in seconds).
			_("Enter song &intro alarm time in seconds (currently {curRampSec})").format(curRampSec = rampVal),
			# Translators: A check box to toggle notification of end of intro alarm.
			_("&Notify when end of introduction is approaching"), 1, 9)
			gui.mainFrame.prePopup()
			d.Raise()
			d.Show()
			gui.mainFrame.postPopup()
			splconfig._alarmDialogOpened = True
		except RuntimeError:
			wx.CallAfter(splconfig._alarmError)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_setSongRampTime.__doc__=_("sets song intro alarm (default is 5 seconds).")

# Tell NVDA to play a sound when mic was active for a long time.

	def script_setMicAlarm(self, gesture):
		if splconfig._configDialogOpened:
			wx.CallAfter(gui.messageBox, _("The add-on settings dialog is opened. Please close the settings dialog first."), _("Error"), wx.OK|wx.ICON_ERROR)
			return
		elif splconfig._alarmDialogOpened:
			wx.CallAfter(splconfig._alarmError)
			return
		micAlarm = str(splconfig.SPLConfig["MicAlarm"])
		if int(micAlarm):
			# Translators: A dialog message to set microphone active alarm (curAlarmSec is the current mic monitoring alarm in seconds).
			timeMSG = _("Enter microphone alarm time in seconds (currently {curAlarmSec}, 0 disables the alarm)").format(curAlarmSec = micAlarm)
		else:
			# Translators: A dialog message when microphone alarm is disabled (set to 0).
			timeMSG = _("Enter microphone alarm time in seconds (currently disabled, 0 disables the alarm)")
		dlg = wx.TextEntryDialog(gui.mainFrame,
		timeMSG,
		# Translators: The title of mic alarm dialog.
		_("Microphone alarm"),
		defaultValue=micAlarm)
		splconfig._alarmDialogOpened = True
		def callback(result):
			splconfig._alarmDialogOpened = False
			if result == wx.ID_OK:
				if not user32.FindWindowA("SPLStudio", None): return
				newVal = dlg.GetValue()
				if not newVal.isdigit():
					# Translators: The error message presented when incorrect alarm time value has been entered.
					wx.CallAfter(gui.messageBox, _("Incorrect value entered."),
					# Translators: Standard title for error dialog (copy this from main nvda.po file).
					_("Error"),wx.OK|wx.ICON_ERROR)
				else:
					if micAlarm != newVal:
						splconfig.SPLConfig["MicAlarm"] = newVal
		gui.runScriptModalDialog(dlg, callback)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_setMicAlarm.__doc__=_("Sets microphone alarm (default is 5 seconds).")

	# SPL Config management.

	def script_openConfigDialog(self, gesture):
		wx.CallAfter(splconfig.onConfigDialog, None)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_openConfigDialog.__doc__=_("Opens SPL Studio add-on configuration dialog.")

	# Other commands (track finder and others)

	# Toggle whether beeps should be heard instead of toggle announcements.

	def script_toggleBeepAnnounce(self, gesture):
		if not splconfig.SPLConfig["BeepAnnounce"]:
			splconfig.SPLConfig["BeepAnnounce"] = True
			# Translators: Reported when status announcement is set to beeps in SPL Studio.
			ui.message(_("Status announcement beeps"))
		else:
			splconfig.SPLConfig["BeepAnnounce"] = False
			# Translators: Reported when status announcement is set to words in SPL Studio.
			ui.message(_("Status announcement words"))
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_toggleBeepAnnounce.__doc__=_("Toggles status announcements between words and beeps.")

	# Braille timer.
	# Announce end of track and other info via braille.

	def script_setBrailleTimer(self, gesture):
		brailleTimer = splconfig.SPLConfig["BrailleTimer"]
		if brailleTimer == "off":
			brailleTimer = "outro"
			# Translators: A setting in braille timer options.
			ui.message(_("Braille track endings"))
		elif brailleTimer == "outro":
			brailleTimer = "intro"
			# Translators: A setting in braille timer options.
			ui.message(_("Braille intro endings"))
		elif brailleTimer == "intro":
			brailleTimer = "both"
			# Translators: A setting in braille timer options.
			ui.message(_("Braille intro and track endings"))
		else:
			brailleTimer = "off"
			# Translators: A setting in braille timer options.
			ui.message(_("Braille timer off"))
		splconfig.SPLConfig["BrailleTimer"] = brailleTimer
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_setBrailleTimer.__doc__=_("Toggles between various braille timer settings.")

	# The track finder utility for find track script and other functions
	# Perform a linear search to locate the track name and/or description which matches the entered value.
	# Also, find column content for a specific column if requested.
	# 6.0: Split this routine into two functions, with the while loop moving to a function of its own.
	# This new function will be used by track finder and place marker locator.
	findText = ""

	def trackFinder(self, text, obj, directionForward=True, column=None):
		speech.cancelSpeech()
		if column is None: 
			column = [obj._indexOf("Artist"), obj._indexOf("Title")]
		track = self._trackLocator(text, obj=obj, directionForward=directionForward, columns=column)
		if track:
			if self.findText != text: self.findText = text
			# We need to fire set focus event twice and exit this routine.
			track.setFocus(), track.setFocus()
		else:
			wx.CallAfter(gui.messageBox,
			# Translators: Standard dialog message when an item one wishes to search is not found (copy this from main nvda.po).
			_("Search string not found."),
			# Translators: Standard error title for find error (copy this from main nvda.po).
			_("Find error"),wx.OK|wx.ICON_ERROR)

	# Split from track finder in 2015.
	# Return a track with the given search criteria.
	# Column is a list of columns to be searched (if none, it'll be artist and title).
	def _trackLocator(self, text, obj=api.getFocusObject(), directionForward=True, columns=None):
		nextTrack = "next" if directionForward else "previous"
		t = time.time()
		while obj is not None:
			# Do not use column content attribute, because sometimes NVDA will say it isn't a track item when in fact it is.
			# If this happens, use the module level version of column content getter.
			# Optimization: search column texts.
			for column in columns:
				columnText = splmisc._getColumnContent(obj, column)
				if columnText and text in columnText:
					print "Track locator took %s seconds"%(time.time()-t)
					return obj
			obj = getattr(obj, nextTrack)
		print "Track locator took %s seconds"%(time.time()-t)
		return None

		# Find a specific track based on a searched text.
	# Unfortunately, the track list does not provide obj.name (it is None), however obj.description has the actual track entry.
	# For Studio 5.01 and earlier, artist label appears as the name, while in Studio 5.10, obj.name is none.
	# But first, check if track finder can be invoked.
	def _trackFinderCheck(self):
		if api.getForegroundObject().windowClassName != "TStudioForm":
			# Translators: Presented when a user attempts to find tracks but is not at the track list.
			ui.message(_("Track finder is available only in track list."))
			return False
		elif api.getForegroundObject().windowClassName == "TStudioForm" and api.getFocusObject().role == controlTypes.ROLE_LIST:
			# Translators: Presented when a user wishes to find a track but didn't add any tracks.
			ui.message(_("You need to add at least one track to find tracks."))
			return False
		return True

	def trackFinderGUI(self, columnSearch=False):
		try:
			if not columnSearch: title = "Find track"
			else: title = "Column search"
			d = splmisc.SPLFindDialog(gui.mainFrame, api.getFocusObject(), self.findText, title, columnSearch = columnSearch)
			gui.mainFrame.prePopup()
			d.Raise()
			d.Show()
			gui.mainFrame.postPopup()
			splmisc._findDialogOpened = True
		except RuntimeError:
			wx.CallAfter(splmisc._finderError)

	def script_findTrack(self, gesture):
		if self._trackFinderCheck(): self.trackFinderGUI()
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_findTrack.__doc__=_("Finds a track in the track list.")

	def script_columnSearch(self, gesture):
		if self._trackFinderCheck(): self.trackFinderGUI(columnSearch=True)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_columnSearch.__doc__=_("Finds text in columns.")

	# Find next and previous scripts.

	def script_findTrackNext(self, gesture):
		if self._trackFinderCheck():
			if self.findText == "": self.trackFinderGUI()
			else: self.trackFinder(self.findText, obj=api.getFocusObject().next)
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_findTrackNext.__doc__=_("Finds the next occurrence of the track with the name in the track list.")

	def script_findTrackPrevious(self, gesture):
		if self._trackFinderCheck():
			if self.findText == "": self.trackFinderGUI()
			else: self.trackFinder(self.findText, obj=api.getFocusObject().previous, directionForward=False)
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

	def script_toggleCartExplorer(self, gesture):
		if not self.cartExplorer:
			# Prevent cart explorer from being engaged outside of playlist viewer.
			# Todo for 6.0: Let users set cart banks.
			fg = api.getForegroundObject()
			if fg.windowClassName != "TStudioForm":
				# Translators: Presented when cart explorer cannot be entered.
				ui.message(_("You are not in playlist viewer, cannot enter cart explorer"))
				return
			self.carts = splmisc.cartExplorerInit(fg.name)
			if self.carts["faultyCarts"]:
				# Translators: presented when cart explorer could not be switched on.
				ui.message(_("Some or all carts could not be assigned, cannot enter cart explorer"))
				return
			else:
				self.cartExplorer = True
				self.cartsBuilder()
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
		if api.getForegroundObject().windowClassName != "TStudioForm":
			gesture.send()
			return
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

	def script_setLibraryScanProgress(self, gesture):
		libraryScanAnnounce = splconfig.SPLConfig["LibraryScanAnnounce"]
		if libraryScanAnnounce == "off":
			libraryScanAnnounce = "ending"
			# Translators: A setting in library scan announcement options.
			ui.message(_("Announce start and end of a library scan"))
		elif libraryScanAnnounce == "ending":
			libraryScanAnnounce = "progress"
			# Translators: A setting in library scan announcement options.
			ui.message(_("Announce the progress of a library scan"))
		elif libraryScanAnnounce == "progress":
			libraryScanAnnounce = "numbers"
			# Translators: A setting in library scan announcement options.
			ui.message(_("Announce progress and item count of a library scan"))
		else:
			libraryScanAnnounce = "off"
			# Translators: A setting in library scan announcement options.
			ui.message(_("Do not announce library scans"))
		splconfig.SPLConfig["LibraryScanAnnounce"] = libraryScanAnnounce
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_setLibraryScanProgress.__doc__=_("Toggles library scan progress settings.")

	def script_startScanFromInsertTracks(self, gesture):
		gesture.send()
		fg = api.getForegroundObject()
		if fg.windowClassName == "TTrackInsertForm":
			# Translators: Presented when library scan has started.
			ui.message(_("Scan start"))
			if self.productVersion not in noLibScanMonitor: self.libraryScanning = True

	# Report library scan (number of items scanned) in the background.
	def monitorLibraryScan(self):
		global libScanT
		if libScanT and libScanT.isAlive() and api.getForegroundObject().windowClassName == "TTrackInsertForm":
			return
		parem = 0 if self.SPLCurVersion < "5.10" else 1
		countA = statusAPI(parem, 32, ret=True)
		if countA == 0:
			self.libraryScanning = False
			return
		time.sleep(0.1)
		if api.getForegroundObject().windowClassName == "TTrackInsertForm" and self.productVersion in noLibScanMonitor:
			self.libraryScanning = False
			return
		countB = statusAPI(parem, 32, ret=True)
		if countA == countB:
			self.libraryScanning = False
			if self.SPLCurVersion >= "5.10":
				countB = statusAPI(0, 32, ret=True)
			# Translators: Presented when library scanning is finished.
			ui.message(_("{itemCount} items in the library").format(itemCount = countB))
		else:
			libScanT = threading.Thread(target=self.libraryScanReporter, args=(_SPLWin, countA, countB, parem))
			libScanT.daemon = True
			libScanT.start()

	def libraryScanReporter(self, _SPLWin, countA, countB, parem):
		scanIter = 0
		while countA != countB:
			if not self.libraryScanning: return
			countA = countB
			time.sleep(1)
			# Do not continue if we're back on insert tracks form or library scan is finished.
			if api.getForegroundObject().windowClassName == "TTrackInsertForm" or not self.libraryScanning:
				return
			countB, scanIter = statusAPI(parem, 32, ret=True), scanIter+1
			if countB < 0:
				break
			if scanIter%5 == 0 and splconfig.SPLConfig["LibraryScanAnnounce"] not in ("off", "ending"):
				self._libraryScanAnnouncer(countB, splconfig.SPLConfig["LibraryScanAnnounce"])
		self.libraryScanning = False
		if self.backgroundStatusMonitor: return
		if splconfig.SPLConfig["LibraryScanAnnounce"] != "off":
			if splconfig.SPLConfig["BeepAnnounce"]:
				tones.beep(370, 100)
			else:
				# Translators: Presented after library scan is done.
				ui.message(_("Scan complete with {itemCount} items").format(itemCount = countB))

	# Take care of library scanning announcement.
	def _libraryScanAnnouncer(self, count, announcementType):
		if announcementType == "progress":
			# Translators: Presented when library scan is in progress.
			tones.beep(550, 100) if splconfig.SPLConfig["BeepAnnounce"] else ui.message(_("Scanning"))
		elif announcementType == "numbers":
			if splconfig.SPLConfig["BeepAnnounce"]:
				tones.beep(550, 100)
				# No need to provide translatable string - just use index.
				ui.message("{0}".format(count))
			else: ui.message(_("{itemCount} items scanned").format(itemCount = count))

	# Place markers.
	placeMarker = None

	# Is the place marker set on this track?
	# Track argument is None (only useful for debugging purposes).
	def isPlaceMarkerTrack(self, track=None):
		if track is None: track = api.getFocusObject()
		index = track._indexOf("Filename")
		filename = track._getColumnContent(index)
		if self.placeMarker == (index, filename):
			return True
		return False

	# Used in delete track workaround routine.
	def preTrackRemoval(self):
		if self.isPlaceMarkerTrack(track=api.getFocusObject()):
			self.placeMarker = None

	# Some handlers for native commands.

	# In Studio 5.0x, when deleting a track, NVDA announces wrong track item due to focus bouncing.
	# The below hack is sensitive to changes in NVDA core.
	deletedFocusObj = False

	def script_deleteTrack(self, gesture):
		if self.placeMarkerObj: self.preTrackRemoval()
		gesture.send()
		if self.productVersion.startswith("5.0"):
			if api.getForegroundObject().windowClassName == "TStudioForm":
				focus = api.getFocusObject()
				if focus.IAccessibleChildID < focus.parent.childCount:
					self.deletedFocusObj = True
					focus.setFocus()
					self.deletedFocusObj = False
					focus.setFocus()

	# When Escape is pressed, activate background library scan if conditions are right.
	def script_escape(self, gesture):
		gesture.send()
		if self.libraryScanning:
			if not libScanT or (libScanT and not libScanT.isAlive()):
				self.monitorLibraryScan()


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
		self.finish()

	# SPL Assistant flag.
	SPLAssistant = False

	# The SPL Assistant layer driver.

	def script_SPLAssistantToggle(self, gesture):
		# Enter the layer command if an only if we're in the track list to allow easier gesture assignment.
		# Also, do not bother if the app module is not running.
		try:
			fg = api.getForegroundObject()
			if fg.windowClassName != "TStudioForm":
				gesture.send()
				return
			if self.SPLAssistant:
				self.script_error(gesture)
				return
			# To prevent entering wrong gesture while the layer is active.
			self.clearGestureBindings()
			# Project Rainbow: choose the required compatibility layer.
			self.bindGestures(self.__SPLAssistantGestures) if splconfig.SPLConfig["CompatibilityLayer"] == "off" else self.bindGestures(self.__SPLAssistantJFWGestures)
			self.SPLAssistant = True
			tones.beep(512, 50) if splconfig.SPLConfig["BeepAnnounce"] else ui.message("Studio")
			if splconfig.SPLConfig["CompatibilityLayer"] == "jfw": ui.message("JAWS")
		except WindowsError:
			return
	# Translators: Input help mode message for a layer command in Station Playlist Studio.
	script_SPLAssistantToggle.__doc__=_("The SPL Assistant layer command. See the add-on guide for more information on available commands.")


	# Status table keys
	SPLPlayStatus = 0
	SPLSystemStatus = 1
	SPLHourSelectedDuration = 3
	SPLNextTrackTitle = 4
	SPLCurrentTrackTitle = 5
	SPLTemperature = 6
	SPLScheduled = 7

	# Table of child constants based on versions
	# These are scattered throughout the screen, so one can use foreground.children[index] to fetch them.
	# Because 5.x (an perhaps future releases) uses different screen layout, look up the needed constant from the table below (row = info needed, column = version).
	statusObjs={
		SPLPlayStatus:[5, 6], # Play status, mic, etc.
		SPLSystemStatus:[-3, -2], # The second status bar containing system status such as up time.
		SPLHourSelectedDuration:[18, 19], # In case the user selects one or more tracks in a given hour.
		SPLScheduled:[19, 20], # Time when the selected track will begin.
		SPLNextTrackTitle:[7, 8], # Name and duration of the next track if any.
		SPLCurrentTrackTitle:[8, 9], # Name of the currently playing track.
		SPLTemperature:[6, 7], # Temperature for the current city.
	}

	_cachedStatusObjs = {}

	# Called in the layer commands themselves.
	def status(self, infoIndex):
		# Look up the cached objects first for faster response.
		if not infoIndex in self._cachedStatusObjs:
			fg = api.getForegroundObject()
			if not fg.windowClassName == "TStudioForm":
				raise RuntimeError("Not focused in playlist viewer")
			if not self.productVersion >= "5.10": statusObj = self.statusObjs[infoIndex][0]
			else: statusObj = self.statusObjs[infoIndex][1]
			self._cachedStatusObjs[infoIndex] = fg.children[statusObj]
		return self._cachedStatusObjs[infoIndex]

	# The layer commands themselves.

	def script_sayPlayStatus(self, gesture):
		# Please do not translate the following messages.
		if statusAPI(0, 104, ret=True):
			ui.message("Play status: Playing")
		else:
			ui.message("Play status: Stopped")

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
		statusAPI(0, 27, self.announceTime)

	def script_sayHourSelectedTrackDuration(self, gesture):
		obj = self.status(self.SPLHourSelectedDuration).firstChild
		ui.message(obj.name)

	def script_sayPlaylistRemainingDuration(self, gesture):
		statusAPI(1, 27, self.announceTime)

	def script_sayPlaylistModified(self, gesture):
		try:
			obj = self.status(self.SPLSystemStatus).children[5]
			ui.message(obj.name)
		except IndexError:
			# Translators: Presented when playlist modification is unavailable (for Studio 4.33 and earlier)
			ui.message(_("Playlist modification not available"))

	def script_sayNextTrackTitle(self, gesture):
		try:
			obj = self.status(self.SPLNextTrackTitle).firstChild
			# Translators: Presented when there is no information for the next track.
			ui.message(_("No next track scheduled or no track is playing")) if obj.name is None else ui.message(obj.name)
		except RuntimeError:
			# Translators: Presented when next track information is unavailable.
			ui.message(_("Cannot find next track information"))
		finally:
			self.finish()
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayNextTrackTitle.__doc__=_("Announces title of the next track if any")

	def script_sayCurrentTrackTitle(self, gesture):
		try:
			obj = self.status(self.SPLCurrentTrackTitle).firstChild
			# Translators: Presented when there is no information for the current track.
			ui.message(_("Cannot locate current track information or no track is playing")) if obj.name is None else ui.message(obj.name)
		except RuntimeError:
			# Translators: Presented when current track information is unavailable.
			ui.message(_("Cannot find current track information"))
		finally:
			self.finish()
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayCurrentTrackTitle.__doc__=_("Announces title of the next track if any")

	def script_sayTemperature(self, gesture):
		try:
			obj = self.status(self.SPLTemperature).firstChild
			# Translators: Presented when there is no weather or temperature information.
			ui.message(_("Weather and temperature not configured")) if obj.name is None else ui.message(obj.name)
		except RuntimeError:
			# Translators: Presented when temperature information cannot be found.
			ui.message(_("Weather information not found"))
		finally:
			self.finish()
	# Translators: Input help mode message for a command in Station Playlist Studio.
	script_sayTemperature.__doc__=_("Announces temperature and weather information")

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
		if not self.libraryScanning:
			if self.productVersion >= "5.10":
				scanning = statusAPI(1, 32, ret=True)
				if scanning < 0:
					items = statusAPI(0, 32, ret=True)
					ui.message(_("{itemCount} items in the library").format(itemCount = items))
					return
			self.libraryScanning = True
			# Translators: Presented when attempting to start library scan.
			ui.message(_("Monitoring library scan"))
			self.monitorLibraryScan()
		else:
			# Translators: Presented when library scan is already in progress.
			ui.message(_("Scanning is in progress"))

	# Track time analysis: return total length of the selected tracks upon request.
	# Analysis command will be assignable.
	_analysisMarker = None

	def _trackAnalysisAllowed(self):
		if api.getForegroundObject().windowClassName != "TStudioForm":
			ui.message("Not in playlist viewer, cannot perform track time analysis")
			return False
		return True

	def script_markTrackForAnalysis(self, gesture):
		self.finish()
		if self._trackAnalysisAllowed():
			focus = api.getFocusObject()
			if focus.role == controlTypes.ROLE_LIST:
				ui.message("No tracks were added, cannot perform track time analysis")
				return
			if scriptHandler.getLastScriptRepeatCount() == 0:
				self._analysisMarker = focus.IAccessibleChildID-1
				ui.message("Track time analysis activated")
			else:
				self._analysisMarker = None
				ui.message("Track time analysis deactivated")
	script_markTrackForAnalysis.__doc__=_("Marks focused track as start marker for track time analysis")

	def script_trackTimeAnalysis(self, gesture):
		self.finish()
		if self._trackAnalysisAllowed():
			focus = api.getFocusObject()
			if focus.role == controlTypes.ROLE_LIST:
				ui.message("No tracks were added, cannot perform track time analysis")
				return
			if self._analysisMarker is None:
				ui.message("No track selected as start of analysis marker, cannot perform time analysis")
				return
			trackPos = focus.IAccessibleChildID-1
			if self._analysisMarker == trackPos:
				filename = statusAPI(self._analysisMarker, 211, ret=True)
				statusAPI(filename, 30, func=self.announceTime)
			else:
				analysisBegin = min(self._analysisMarker, trackPos)
				analysisEnd = max(self._analysisMarker, trackPos)
				analysisRange = analysisEnd-analysisBegin+1
				totalLength = 0
				for track in xrange(analysisBegin, analysisEnd+1):
					filename = statusAPI(track, 211, ret=True)
					totalLength+=statusAPI(filename, 30, ret=True)
				ui.message("Tracks: {numberOfSelectedTracks}, totaling {totalTime}".format(numberOfSelectedTracks = analysisRange, totalTime = self._ms2time(totalLength)))
	script_trackTimeAnalysis.__doc__=_("Announces total length of tracks between analysis start marker and the current track")

	def script_switchProfiles(self, gesture):
		splconfig.instantProfileSwitch()

	def script_setPlaceMarker(self, gesture):
		obj = api.getFocusObject()
		index = obj._indexOf("Filename")
		filename = obj._getColumnContent(index)
		if filename:
			self.placeMarker = (index, filename)
			ui.message("place marker set")
		else:
			ui.message("This track cannot be used as a place marker track")

	def script_findPlaceMarker(self, gesture):
		if self.placeMarker is None:
			ui.message("No place marker found")
		else:
			track = self._trackLocator(self.placeMarker[1], obj=api.getFocusObject().parent.firstChild, columns=[self.placeMarker[0]])
			track.setFocus(), track.setFocus()

	def script_layerHelp(self, gesture):
		# Translators: The title for SPL Assistant help dialog.
		wx.CallAfter(gui.messageBox, SPLAssistantHelp, _("SPL Assistant help"))

	def script_openOnlineDoc(self, gesture):
		os.startfile("https://bitbucket.org/nvdaaddonteam/stationplaylist/wiki/SPLDevAddonGuide")


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
		"kb:c":"sayCurrentTrackTitle",
		"kb:w":"sayTemperature",
		"kb:i":"sayListenerCount",
		"kb:s":"sayScheduledTime",
		"kb:shift+p":"sayTrackPitch",
		"kb:shift+r":"libraryScanMonitor",
		"kb:f9":"markTrackForAnalysis",
		"kb:f10":"trackTimeAnalysis",
		"kb:f12":"switchProfiles",
		"kb:Control+k":"setPlaceMarker",
		"kb:k":"findPlaceMarker",
		"kb:f1":"layerHelp",
		"kb:shift+f1":"openOnlineDoc",
	}

	__SPLAssistantJFWGestures={
		"kb:p":"sayPlayStatus",
		"kb:a":"sayAutomationStatus",
		"kb:m":"sayMicStatus",
		"kb:shift+l":"sayLineInStatus",
		"kb:e":"sayRecToFileStatus",
		"kb:t":"sayCartEditStatus",
		"kb:h":"sayHourTrackDuration",
		"kb:shift+h":"sayHourSelectedTrackDuration",
		"kb:r":"sayPlaylistRemainingDuration",
		"kb:y":"sayPlaylistModified",
		"kb:u":"sayUpTime",
		"kb:n":"sayNextTrackTitle",
		"kb:c":"sayCurrentTrackTitle",
		"kb:w":"sayTemperature",
		"kb:l":"sayListenerCount",
		"kb:s":"sayScheduledTime",
		"kb:shift+p":"sayTrackPitch",
		"kb:shift+r":"libraryScanMonitor",
		"kb:f9":"markTrackForAnalysis",
		"kb:f10":"trackTimeAnalysis",
		"kb:f12":"switchProfiles",
		"kb:Control+k":"setPlaceMarker",
		"kb:k":"findPlaceMarker",
		"kb:f1":"layerHelp",
		"kb:shift+f1":"openOnlineDoc",
	}

	__gestures={
		"kb:control+alt+t":"sayRemainingTime",
		"ts(SPL):2finger_flickDown":"sayRemainingTime",
		"kb:alt+shift+t":"sayElapsedTime",
		"kb:shift+nvda+f12":"sayBroadcasterTime",
		"ts(SPL):2finger_flickUp":"sayBroadcasterTime",
		"kb:control+nvda+1":"toggleBeepAnnounce",
		"kb:control+nvda+2":"setEndOfTrackTime",
		"ts(SPL):2finger_flickRight":"setEndOfTrackTime",
		"kb:alt+nvda+2":"setSongRampTime",
		"ts(SPL):2finger_flickLeft":"setSongRampTime",
		"kb:control+nvda+4":"setMicAlarm",
		"kb:control+nvda+f":"findTrack",
		"kb:nvda+f3":"findTrackNext",
		"kb:shift+nvda+f3":"findTrackPrevious",
		"kb:control+nvda+3":"toggleCartExplorer",
		"kb:alt+nvda+r":"setLibraryScanProgress",
		"kb:control+shift+r":"startScanFromInsertTracks",
		"kb:control+shift+x":"setBrailleTimer",
		"kb:control+NVDA+0":"openConfigDialog",
		"kb:Shift+delete":"deleteTrack",
		"kb:Shift+numpadDelete":"deleteTrack",
		"kb:escape":"escape",
		#"kb:control+nvda+`":"SPLAssistantToggle"
	}
