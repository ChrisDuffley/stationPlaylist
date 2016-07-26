# StationPlaylist Utilities
# Author: Joseph Lee
# Copyright 2013-2016, released under GPL.
# Adds a few utility features such as switching focus to the SPL Studio window and some global scripts.
# For encoder support, see the encoders package.

from functools import wraps
import os
import globalPluginHandler
import api
from controlTypes import ROLE_LISTITEM
import ui
import globalVars
from NVDAObjects.IAccessible import getNVDAObjectFromEvent
import winUser
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
SPLListenerCount = 35
SPL_TrackPlaybackStatus = 104
SPLCurTrackPlaybackTime = 105


# On/off toggle wave files.
onFile = os.path.join(os.path.dirname(__file__), "..", "..", "appModules", "splstudio", "SPL_on.wav")
offFile = os.path.join(os.path.dirname(__file__), "..", "..", "appModules", "splstudio", "SPL_off.wav")

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
E: Announce if any encoders are being monitored.
I: Announce listener count.
R: Remaining time for the playing track.
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
	scriptCategory = _("StationPlaylist Studio")

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
		# 7.4: Forget it if this is the case like the following.
		if globalVars.appArgs.secure: return
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
		# 7.4: Red flag...
		if globalVars.appArgs.secure: return
		global SPLWin
		# Error checks:
		# 1. If SPL Studio is not running, print an error message.
		# 2. If we're already  in SPL, ask the app module if SPL Assistant can be invoked with this command.
		if "splstudio" in api.getForegroundObject().appModule.appModuleName:
			if not api.getForegroundObject().appModule.SPLConPassthrough():
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

	def script_listenerCount(self, gesture):
		count = winUser.sendMessage(SPLWin, SPLMSG, 0, SPLListenerCount)
		# Translators: Announces number of stream listeners.
		ui.message(_("Listener count: {listenerCount}").format(listenerCount = count))
		self.finish()

	def script_remainingTime(self, gesture):
		remainingTime = winUser.sendMessage(SPLWin, SPLMSG, 3, SPLCurTrackPlaybackTime)
		# Translators: Presented when no track is playing in Station Playlist Studio.
		if remainingTime < 0: ui.message(_("There is no track playing."))
		else:
			# 7.0: Present remaining time in hh:mm:ss format for enhanced experience (borrowed from the app module).
			remainingTime = (remainingTime/1000)+1
			if remainingTime == 0: ui.message("00:00")
			elif 1 <= remainingTime <= 59: ui.message("00:{0}".format(str(remainingTime).zfill(2)))
			else:
				mm, ss = divmod(remainingTime, 60)
				if mm > 59:
					hh, mm = divmod(mm, 60)
					t0 = str(hh).zfill(2)
					t1 = str(mm).zfill(2)
					t2 = str(ss).zfill(2)
					ui.message(":".join([t0, t1, t2]))
				else:
					t1 = str(mm).zfill(2)
					t2 = str(ss).zfill(2)
					ui.message(":".join([t1, t2]))
		self.finish()

	def script_announceNumMonitoringEncoders(self, gesture):
		import encoders
		encoders.announceNumMonitoringEncoders()
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
		"kb:e":"announceNumMonitoringEncoders",
		"kb:i":"listenerCount",
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
		if obj.appModule.appName in ("splengine", "splstreamer"):
			import encoders
			if obj.windowClassName == "TListView":
				clsList.insert(0, encoders.SAMEncoder)
			elif obj.windowClassName == "SysListView32":
				if obj.role == ROLE_LISTITEM:
					clsList.insert(0, encoders.SPLEncoder)

