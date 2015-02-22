# Station Playlist Utilities
# Author: Joseph Lee
# Copyright 2013-2015, released under GPL.
# Adds a few utility features such as switching focus to the SPL Studio window and some global scripts, along with support for Encoders.

from functools import wraps
import threading
import os
import time
from configobj import ConfigObj
import globalPluginHandler
import api
from controlTypes import ROLE_LISTITEM
import ui
import speech
import braille
import globalVars
import scriptHandler
from NVDAObjects.IAccessible import IAccessible, getNVDAObjectFromEvent
import winUser
import winKernel
import tones
import nvwave
import gui
import wx
import addonHandler
addonHandler.initTranslation()

# Layer environment: same as the app module counterpart.

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

# SPL Studio uses WM messages to send and receive data, similar to Winamp (see NVDA sources/appModules/winamp.py for more information).
user32 = winUser.user32 # user32.dll.
SPLWin = 0 # A handle to studio window.
SPLMSG = winUser.WM_USER

# Various SPL IPC tags.
SPLPlay = 12
SPLStop = 13
SPLPause = 15
SPLAutomate = 16
SPLMic = 17
SPLLineIn = 18
SPLLibraryScanCount = 32
SPL_TrackPlaybackStatus = 104
SPLCurTrackPlaybackTime = 105

# Needed in SAM and SPL Encoder support:
SAMFocusToStudio = {} # A dictionary to record whether to switch to SPL Studio for this encoder.
SPLFocusToStudio = {}
SAMPlayAfterConnecting = {}
SPLPlayAfterConnecting = {}
SAMStreamLabels= {} # A dictionary to store custom labels for each stream.
SPLStreamLabels= {} # Same as above but optimized for SPL encoders (Studio 5.00 and later).
SAMBackgroundMonitor = {}
SPLBackgroundMonitor = {}
SAMMonitorThreads = {}
SPLMonitorThreads = {}
encoderMonCount = {"SAM":0, "SPL":0}

# Configuration management.
streamLabels = None

# On/off toggle wave files.
onFile = os.path.join(os.path.dirname(__file__), "..", "appModules", "SPL_on.wav")
offFile = os.path.join(os.path.dirname(__file__), "..", "appModules", "SPL_off.wav")

# Help message for SPL Controller
# Translators: the dialog text for SPL Controller help.
SPLConHelp=_("""
After entering SPL Controller, press:
A: Turn automation on.
Shift+A: Turn automation off.
M: Turn microphone on.
Shift+M: Turn microphone off.
N: Turn microphone on without fade.
L: Turn line in on.
Shift+L: Turn line in off.
P: Play.
U: Pause.
S: Stop with fade.
T: Instant stop.
R: Remainig time for the playing track.
Shift+R: Library scan progress.""")

# Try to see if SPL foreground object can be fetched. This is used for switching to SPL Studio window from anywhere and to switch to Studio window from SAM encoder window.

def fetchSPLForegroundWindow():
	# Turns out NVDA core does have a method to fetch desktop objects, so use this to find SPL window from among its children.
	dt = api.getDesktopObject()
	fg = None
	fgCount = 0
	for possibleFG in dt.children:
		if "splstudio" in possibleFG.appModule.appModuleName:
			fg = possibleFG
			fgCount+=1
	# Just in case the window is really minimized (not to the system tray)
	if fgCount == 1:
		fg = getNVDAObjectFromEvent(user32.FindWindowA("TStudioForm", None), winUser.OBJID_CLIENT, 0)
	return fg


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Translators: Script category for Station Playlist commands in input gestures dialog.
	scriptCategory = _("Station Playlist Studio")


	# Do some initialization, such as stream labels for SAM encoders.
	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		# Load stream labels (and possibly other future goodies) from a file-based database.
		global streamLabels, SAMStreamLabels, SPLStreamLabels
		streamLabels = ConfigObj(os.path.join(globalVars.appArgs.configPath, "splStreamLabels.ini"))
		# Read stream labels.
		try:
			SAMStreamLabels = dict(streamLabels["SAMEncoders"])
		except KeyError:
			SAMStreamLabels = {}
		try:
			SPLStreamLabels = dict(streamLabels["SPLEncoders"])
		except KeyError:
			SPLStreamLabels = {}

	# Save configuration file.
	"""def terminate(self):
		global streamLabels
		streamLabels["SAMEncoders"] = SAMStreamLabels
		streamLabels["SPLEncoders"] = SPLStreamLabels
		streamLabels.write()"""

			#Global layer environment (see the app module for more information).
	SPLController = False # Control SPL from anywhere.

	def getScript(self, gesture):
		if not self.SPLController:
			return globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		script = globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		if not script:
			script = finally_(self.script_error, self.finish)
		return finally_(script, self.finish)

	def finish(self):
		self.SPLController = False
		self.clearGestureBindings()
		self.bindGestures(self.__gestures)

	def script_error(self, gesture):
		tones.beep(120, 100)

	# Switch focus to SPL Studio window from anywhere.
	def script_focusToSPLWindow(self, gesture):
		# Don't do anything if we're already focus on SPL Studio.
		if "splstudio" in api.getForegroundObject().appModule.appModuleName: return
		else:
			SPLHwnd = user32.FindWindowA("SPLStudio", None) # Used ANSI version, as Wide char version always returns 0.
			if SPLHwnd == 0: ui.message(_("SPL Studio is not running."))
			else:
				SPLFG = fetchSPLForegroundWindow()
				if SPLFG == None:
					# Translators: Presented when Studio is minimized to system tray (notification area).
					ui.message(_("SPL minimized to system tray."))
				else: SPLFG.setFocus()
	# Translators: Input help mode message for a command to switch to Station Playlist Studio from any program.
	script_focusToSPLWindow.__doc__=_("Moves to SPL Studio window from other programs.")

	# The SPL Controller:
	# This layer set allows the user to control various aspects of SPL Studio from anywhere.
	def script_SPLControllerPrefix(self, gesture):
		global SPLWin
		# Error checks:
		# 1. If SPL Studio is not running, print an error message.
		# 2. If we're already  in SPL, report that the user is in SPL. This is temporary - in the end, pass this gesture to the app module portion if told to do so.
		# For SPL Controller passthrough, it needs to be enabled via Python. This is experimental.
		if "splstudio" in api.getForegroundObject().appModule.appModuleName:
			if not api.getForegroundObject().appModule.SPLConPassthrough:
				# Translators: Presented when NVDA cannot enter SPL Controller layer since SPL Studio is focused.
				ui.message(_("You are already in SPL Studio window. For status commands, use SPL Assistant commands."))
				self.finish()
				return
			else:
				api.getForegroundObject().appModule.script_SPLAssistantToggle(gesture)
				return
		SPLWin = user32.FindWindowA("SPLStudio", None)
		if SPLWin == 0:
			# Translators: Presented when Station Playlist Studio is not running.
			ui.message(_("SPL Studio is not running."))
			self.finish()
			return
		# No errors, so continue.
		if not self.SPLController:
			self.bindGestures(self.__SPLControllerGestures)
			self.SPLController = True
			# Translators: The name of a layer command set for Station Playlist Studio.
			# Hint: it is better to translate it as "SPL Control Panel."
			ui.message(_("SPL Controller"))
		else:
			self.script_error(gesture)
			self.finish()
	# Translators: Input help mode message for a layer command in Station Playlist Studio.
	script_SPLControllerPrefix.__doc__=_("SPl Controller layer command. See add-on guide for available commands.")

	# The layer commands themselves. Calls user32.SendMessage method for each script.

	def script_automateOn(self, gesture):
		winUser.sendMessage(SPLWin,SPLMSG,1,SPLAutomate)
		self.finish()

	def script_automateOff(self, gesture):
		winUser.sendMessage(SPLWin,SPLMSG,0,SPLAutomate)
		self.finish()

	def script_micOn(self, gesture):
		winUser.sendMessage(SPLWin,SPLMSG,1,SPLMic)
		nvwave.playWaveFile(onFile)
		self.finish()

	def script_micOff(self, gesture):
		winUser.sendMessage(SPLWin,SPLMSG,0,SPLMic)
		nvwave.playWaveFile(offFile)
		self.finish()

	def script_micNoFade(self, gesture):
		winUser.sendMessage(SPLWin,SPLMSG,2,SPLMic)
		self.finish()

	def script_lineInOn(self, gesture):
		winUser.sendMessage(SPLWin,SPLMSG,1,SPLLineIn)
		self.finish()

	def script_lineInOff(self, gesture):
		winUser.sendMessage(SPLWin,SPLMSG,0,SPLLineIn)
		self.finish()

	def script_stopFade(self, gesture):
		winUser.sendMessage(SPLWin,SPLMSG,0,SPLStop)
		self.finish()

	def script_stopInstant(self, gesture):
		winUser.sendMessage(SPLWin,SPLMSG,1,SPLStop)
		self.finish()

	def script_play(self, gesture):
		winUser.sendMessage(SPLWin, SPLMSG, 0, SPLPlay)
		self.finish()

	def script_pause(self, gesture):
		playingNow = winUser.sendMessage(SPLWin, SPLMSG, 0, SPL_TrackPlaybackStatus)
		# Translators: Presented when no track is playing in Station Playlist Studio.
		if not playingNow: ui.message(_("There is no track playing. Try pausing while a track is playing."))
		elif playingNow == 3: winUser.sendMessage(SPLWin, SPLMSG, 0, SPLPause)
		else: winUser.sendMessage(SPLWin, SPLMSG, 1, SPLPause)
		self.finish()

	def script_libraryScanProgress(self, gesture):
		scanned = winUser.sendMessage(SPLWin, SPLMSG, 0, SPLLibraryScanCount)
		# Translators: Announces number of items in the Studio's track library (example: 1000 items scanned).
		ui.message(_("{itemCount} items scanned").format(itemCount = scanned))
		self.finish()

	def script_remainingTime(self, gesture):
		remainingTime = winUser.sendMessage(SPLWin, SPLMSG, 3, SPLCurTrackPlaybackTime)
		# Translators: Presented when no track is playing in Station Playlist Studio.
		if remainingTime < 0: ui.message(_("There is no track playing."))
		else: ui.message(str(remainingTime/1000))
		self.finish()

	def script_conHelp(self, gesture):
		# Translators: The title for SPL Controller help dialog.
		wx.CallAfter(gui.messageBox, SPLConHelp, _("SPL Controller help"))
		self.finish()


	__SPLControllerGestures={
		"kb:p":"play",
		"kb:a":"automateOn",
		"kb:shift+a":"automateOff",
		"kb:m":"micOn",
		"kb:shift+m":"micOff",
		"kb:n":"micNoFade",
		"kb:l":"lineInOn",
		"kb:shift+l":"lineInOff",
		"kb:shift+r":"libraryScanProgress",
		"kb:s":"stopFade",
		"kb:t":"stopInstant",
		"kb:u":"pause",
		"kb:r":"remainingTime",
		"kb:f1":"conHelp"
	}


	__gestures={
		#"kb:nvda+shift+`":"focusToSPLWindow",
		#"kb:nvda+`":"SPLControllerPrefix"
	}

	# Support for Encoders
	# Each encoder is an overlay class, thus makes it easier to add encoders in the future by implementing overlay objects.
	# Each encoder, at a minimum, must support connection monitoring routines.

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.appModule.appName in ["splengine", "splstreamer"]:
			if obj.windowClassName == "TListView":
				clsList.insert(0, SAMEncoderWindow)
			elif obj.windowClassName == "SysListView32":
				if obj.role == ROLE_LISTITEM:
					clsList.insert(0, SPLEncoderWindow)

class SAMEncoderWindow(IAccessible):
	# Support for Sam Encoder window.

	# Few useful variables for encoder list:
	focusToStudio = False # If true, Studio will gain focus after encoder connects.
	playAfterConnecting = False # When connected, the first track will be played.
	encoderType = "SAM"
	backgroundMonitor = False # Monitor this encoder for connection status changes.


	def reportConnectionStatus(self, connecting=False):
		# Keep an eye on the stream's description field for connection changes.
		# In order to not block NVDA commands, this will be done using a different thread.
		SPLWin = user32.FindWindowA("SPLStudio", None)
		toneCounter = 0
		messageCache = ""
		# Status message flags.
		idle = False
		error = False
		encoding = False
		while True:
			time.sleep(0.001)
			try:
				if messageCache != self.description[self.description.find("Status")+8:]:
					messageCache = self.description[self.description.find("Status")+8:]
					if not messageCache.startswith("Encoding"):
						self.encoderStatusMessage(messageCache, self.IAccessibleChildID)
			except AttributeError:
				return
			if messageCache.startswith("Idle"):
				if alreadyEncoding: alreadyEncoding = False
				if encoding: encoding = False
				if not idle:
					tones.beep(250, 250)
					idle = True
					toneCounter = 0
			elif messageCache.startswith("Error"):
				# Announce the description of the error.
				if connecting: connecting= False
				if not error:
					error = True
					toneCounter = 0
				if alreadyEncoding: alreadyEncoding = False
			elif messageCache.startswith("Encoding"):
				if connecting: connecting = False
				# We're on air, so exit unless told to monitor for connection changes.
				if not encoding:
					tones.beep(1000, 150)
					self.encoderStatusMessage(messageCache, self.IAccessibleChildID)
				if self.focusToStudio and not encoding:
					if api.getFocusObject().appModule == "splstudio":
						continue
					try:
						fetchSPLForegroundWindow().setFocus()
					except AttributeError:
						pass
				focused = True
				if self.playAfterConnecting and not encoding:
					winUser.sendMessage(SPLWin, SPLMSG, 0, SPLPlay)
				if not encoding: encoding = True
			else:
				if alreadyEncoding: alreadyEncoding = False
				if encoding: encoding = False
				elif "Error" not in self.description and error: error = False
				toneCounter+=1
				if toneCounter%250 == 0:
					tones.beep(500, 50)
			if connecting: continue
			if not SAMBackgroundMonitor[self.IAccessibleChildID]: return

	# Format the status message to prepare for monitoring multiple encoders.
	def encoderStatusMessage(self, message, id):
		if encoderMonCount[self.encoderType] > 1:
			ui.message("{encoder} {encoderNumber}: {status}".format(encoder = self.encoderType, encoderNumber = id, status = message))
		else:
			ui.message(message)

	def script_connect(self, gesture):
		gesture.send()
		# Translators: Presented when SAM Encoder is trying to connect to a streaming server.
		ui.message(_("Connecting..."))
		# Oi, status thread, can you keep an eye on the connection status for me?
		if self.IAccessibleChildID not in SAMBackgroundMonitor.keys():
			SAMBackgroundMonitor[self.IAccessibleChildID] = self.backgroundMonitor
		if not self.backgroundMonitor:
			statusThread = threading.Thread(target=self.reportConnectionStatus, kwargs=dict(connecting=True))
			statusThread.name = "Connection Status Reporter " + str(self.IAccessibleChildID)
			statusThread.start()
			SAMMonitorThreads[self.IAccessibleChildID] = statusThread

	def script_disconnect(self, gesture):
		gesture.send()
		# Translators: Presented when SAM Encoder is disconnecting from a streaming server.
		ui.message(_("Disconnecting..."))

	def script_toggleFocusToStudio(self, gesture):
		if not self.focusToStudio:
			self.focusToStudio = True
			# Translators: Presented when toggling the setting to switch to Studio when connected to a streaming server.
			ui.message(_("Switch to Studio after connecting"))
		else:
			self.focusToStudio = False
			# Translators: Presented when toggling the setting to switch to Studio when connected to a streaming server.
			ui.message(_("Do not switch to Studio after connecting"))
		if self.encoderType == "SAM":
			SAMFocusToStudio[self.IAccessibleChildID] = self.focusToStudio
		elif self.encoderType == "SPL":
			SPLFocusToStudio[self.IAccessibleChildID] = self.focusToStudio
	# Translators: Input help mode message in SAM Encoder window.
	script_toggleFocusToStudio.__doc__=_("Toggles whether NVDA will switch to Studio when connected to a streaming server.")

	def script_togglePlay(self, gesture):
		if not self.playAfterConnecting:
			self.playAfterConnecting = True
			# Translators: Presented when toggling the setting to play selected song when connected to a streaming server.
			ui.message(_("Play first track after connecting"))
		else:
			self.playAfterConnecting = False
			# Translators: Presented when toggling the setting to switch to Studio when connected to a streaming server.
			ui.message(_("Do not play first track after connecting"))
		if self.encoderType == "SAM":
			SAMPlayAfterConnecting[self.IAccessibleChildID] = self.playAfterConnecting
		elif self.encoderType == "SPL":
			SPLPlayAfterConnecting[self.IAccessibleChildID] = self.playAfterConnecting
	# Translators: Input help mode message in SAM Encoder window.
	script_togglePlay.__doc__=_("Toggles whether Studio will play the first song when connected to a streaming server.")

	def script_toggleBackgroundEncoderMonitor(self, gesture):
		ui.message(str(threading.activeCount()))
		if not self.backgroundMonitor:
			self.backgroundMonitor = True
			encoderMonCount[self.encoderType] += 1 # Multiple encoders.
			ui.message("Monitoring encoder {encoderNumber}".format(encoderNumber = self.IAccessibleChildID))
		else:
			self.backgroundMonitor = False
			encoderMonCount[self.encoderType] -= 1
			ui.message("Encoder {encoderNumber} will not be monitored".format(encoderNumber = self.IAccessibleChildID))
		if self.encoderType == "SAM":
			SAMBackgroundMonitor[self.IAccessibleChildID] = self.backgroundMonitor
			threadPool = SAMMonitorThreads
		elif self.encoderType == "SPL":
			SPLBackgroundMonitor[self.IAccessibleChildID] = self.backgroundMonitor
			threadPool = SPLMonitorThreads
		if self.backgroundMonitor:
			try:
				monitoring = threadPool[self.IAccessibleChildID].isAlive()
			except KeyError:
				monitoring = False
			if not monitoring:
				statusThread = threading.Thread(target=self.reportConnectionStatus)
				statusThread.name = "Connection Status Reporter " + str(self.IAccessibleChildID)
				statusThread.start()
				threadPool[self.IAccessibleChildID] = statusThread

	def script_streamLabeler(self, gesture):
		curStreamLabel, title = self.getStreamLabel(), ""
		if not curStreamLabel: curStreamLabel = ""
		if self.encoderType == "SAM":
			title = self.IAccessibleChildID
		elif self.encoderType == "SPL":
			title = self.firstChild.name
		# Translators: The title of the stream labeler dialog (example: stream labeler for 1).
		streamTitle = _("Stream labeler for {streamEntry}").format(streamEntry = title)
		# Translators: The text of the stream labeler dialog.
		streamText = _("Enter the label for this stream")
		dlg = wx.TextEntryDialog(gui.mainFrame,
		streamText, streamTitle, defaultValue=curStreamLabel)
		def callback(result):
			global streamLabels
			if result == wx.ID_OK:
				newStreamLabel = dlg.GetValue()
				if newStreamLabel == curStreamLabel:
					return # No need to write to disk.
				else:
					if len(newStreamLabel):
						if self.encoderType == "SAM": SAMStreamLabels[str(self.IAccessibleChildID)] = dlg.GetValue()
						elif self.encoderType == "SPL": SPLStreamLabels[str(self.IAccessibleChildID)] = dlg.GetValue()
					else:
						if self.encoderType == "SAM": del SAMStreamLabels[str(self.IAccessibleChildID)]
						elif self.encoderType == "SPL": del SPLStreamLabels[(self.IAccessibleChildID)]
				streamLabels["SAMEncoders"] = SAMStreamLabels
				streamLabels["SPLEncoders"] = SPLStreamLabels
				streamLabels.write()
		gui.runScriptModalDialog(dlg, callback)
	# Translators: Input help mode message in SAM Encoder window.
	script_streamLabeler.__doc__=_("Opens a dialog to label the selected encoder.")

	# Announce complete time including seconds (slight change from global commands version).
	def script_encoderDateTime(self, gesture):
		if scriptHandler.getLastScriptRepeatCount()==0:
			text=winKernel.GetTimeFormat(winKernel.LOCALE_USER_DEFAULT, 0, None, None)
		else:
			text=winKernel.GetDateFormat(winKernel.LOCALE_USER_DEFAULT, winKernel.DATE_LONGDATE, None, None)
		ui.message(text)
	# Translators: Input help mode message for report date and time command.
	script_encoderDateTime.__doc__=_("If pressed once, reports the current time including seconds. If pressed twice, reports the current date")
	script_encoderDateTime.category=_("Station Playlist Studio")


	def initOverlayClass(self):
		# Can I switch to Studio when connected to a streaming server?
		try:
			self.focusToStudio = SAMFocusToStudio[self.IAccessibleChildID]
		except KeyError:
			pass
		# Am I being monitored for connection changes?
		try:
			self.backgroundMonitor = SAMBackgroundMonitor[self.IAccessibleChildID]
		except KeyError:
			pass

	def getStreamLabel(self):
		if str(self.IAccessibleChildID) in SAMStreamLabels:
			return SAMStreamLabels[str(self.IAccessibleChildID)]
		return None


	def reportFocus(self):
		import globalPlugins
		streamLabel = self.getStreamLabel()
		# Speak the stream label if it exists.
		if streamLabel is not None:
			try:
				self.name = "(" + streamLabel + ") " + self.name
			except TypeError:
				pass
		super(globalPlugins.SPLStudioUtils.SAMEncoderWindow, self).reportFocus()


	__gestures={
		"kb:f9":"connect",
		"kb:f10":"disconnect",
		"kb:f11":"toggleFocusToStudio",
		"kb:shift+f11":"togglePlay",
		"kb:control+f11":"toggleBackgroundEncoderMonitor",
		"kb:f12":"streamLabeler",
		"kb:NVDA+F12":"encoderDateTime"
	}

class SPLEncoderWindow(SAMEncoderWindow):
	# Support for SPL Encoder window.

	# A few more subclass flags.
	encoderType = "SPL"

	def reportConnectionStatus(self, connecting=False):
		# Same routine as SAM encoder: use a thread to prevent blocking NVDA commands.
		SPLWin = user32.FindWindowA("SPLStudio", None)
		attempt = 0
		messageCache = ""
		# Status flags.
		connected = False
		while True:
			time.sleep(0.001)
			try:
				statChild = self.children[1]
			except IndexError:
				return # Don't leave zombie objects around.
			if messageCache != statChild.name:
				messageCache = statChild.name
				if "Kbps" not in messageCache:
					self.encoderStatusMessage(messageCache, self.IAccessibleChildID)
			if messageCache == "Disconnected":
				connected = False
				if connecting: continue
			elif messageCache == "Connected":
				connecting = False
				# We're on air, so exit.
				if not connected: tones.beep(1000, 150)
				if self.focusToStudio and not connected:
					try:
						fetchSPLForegroundWindow().setFocus()
					except AttributeError:
						pass
				if self.playAfterConnecting and not connected:
					winUser.sendMessage(SPLWin, SPLMSG, 0, SPLPlay)
				if not connected: connected = True
			elif "Unable to connect" in messageCache or "Failed" in messageCache:
				if connected: connected = False
			else:
				if connected: connected = False
				if not "Kbps" in messageCache:
					attempt += 1
					if attempt%250 == 0:
						tones.beep(500, 50)
						if attempt>= 500 and statChild.name == "Disconnected":
							tones.beep(250, 250)
				if connecting: continue
			if not SPLBackgroundMonitor[self.IAccessibleChildID]: return

	def script_connect(self, gesture):
		# Same as SAM's connection routine, but this time, keep an eye on self.name and a different connection flag.
		connectButton = api.getForegroundObject().children[2]
		if connectButton.name == "Disconnect": return
		ui.message(_("Connecting..."))
		# Juggle the focus around.
		connectButton.doAction()
		self.setFocus()
		# Same as SAM encoders.
		if self.IAccessibleChildID not in SPLBackgroundMonitor.keys():
			SPLBackgroundMonitor[self.IAccessibleChildID] = self.backgroundMonitor
		if not self.backgroundMonitor:
			statusThread = threading.Thread(target=self.reportConnectionStatus, kwargs=dict(connecting=True))
			statusThread.name = "Connection Status Reporter"
			statusThread.start()
			SPLMonitorThreads[self.IAccessibleChildID] = statusThread
	script_connect.__doc__=_("Connects to a streaming server.")


	def initOverlayClass(self):
		# Can I switch to Studio when connected to a streaming server?
		try:
			self.focusToStudio = SPLFocusToStudio[self.IAccessibleChildID]
		except KeyError:
			pass
		try:
			self.backgroundMonitor = SPLBackgroundMonitor[self.IAccessibleChildID]
		except KeyError:
			self.backgroundMonitor = False

	def getStreamLabel(self):
		if str(self.IAccessibleChildID) in SPLStreamLabels:
			return SPLStreamLabels[str(self.IAccessibleChildID)]
		return None


	__gestures={
		"kb:f9":"connect",
		"kb:f10":None
	}


