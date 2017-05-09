# StationPlaylist Utilities
# Author: Joseph Lee
# Copyright 2013-2017, released under GPL.
# Adds a few utility features such as switching focus to the SPL Studio window and some global scripts.
# For encoder support, see the encoders package.

from functools import wraps
import globalPluginHandler
import api
import ui
import globalVars
import winUser
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

# SPL Studio uses WM messages to send and receive data, similar to Winamp (see NVDA sources/appModules/winamp.py for more information).
user32 = winUser.user32 # user32.dll.
SPLWin = 0 # A handle to studio window.

# Various SPL IPC tags.
SPLVersion = 2
SPLPlay = 12
SPLStop = 13
SPLPause = 15
SPLAutomate = 16
SPLMic = 17
SPLLineIn = 18
SPLLibraryScanCount = 32
SPLListenerCount = 35
SPLStatusInfo = 39 #Studio 5.20 and later.
SPL_TrackPlaybackStatus = 104
SPLCurTrackPlaybackTime = 105

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
Q: Announce Studio status information.
R: Remaining time for the playing track.
Shift+R: Library scan progress.""")


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
			script = self.script_error
		return finally_(script, self.finish)

	def finish(self):
		self.SPLController = False
		self.clearGestureBindings()
		self.bindGestures(self.__gestures)

	def script_error(self, gesture):
		import tones
		tones.beep(120, 100)

	# Switch focus to SPL Studio window from anywhere.
	def script_focusToSPLWindow(self, gesture):
		# 7.4: Forget it if this is the case like the following.
		if globalVars.appArgs.secure: return
		# Don't do anything if we're already focus on SPL Studio.
		if "splstudio" in api.getForegroundObject().appModule.appModuleName: return
		else:
			SPLHwnd = user32.FindWindowA("SPLStudio", None) # Used ANSI version, as Wide char version always returns 0.
			if not SPLHwnd: ui.message(_("SPL Studio is not running."))
			else:
				# 17.01: SetForegroundWindow function is better, as there's no need to traverse top-level windows and allows users to "switch" to SPL window if the window is minimized.
				user32.SetForegroundWindow(user32.FindWindowA("TStudioForm", None))
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
		winUser.sendMessage(SPLWin,1024,1,SPLAutomate)
		self.finish()

	def script_automateOff(self, gesture):
		winUser.sendMessage(SPLWin,1024,0,SPLAutomate)
		self.finish()

	def script_micOn(self, gesture):
		winUser.sendMessage(SPLWin,1024,1,SPLMic)
		self.finish()

	def script_micOff(self, gesture):
		winUser.sendMessage(SPLWin,1024,0,SPLMic)
		self.finish()

	def script_micNoFade(self, gesture):
		winUser.sendMessage(SPLWin,1024,2,SPLMic)
		self.finish()

	def script_lineInOn(self, gesture):
		winUser.sendMessage(SPLWin,1024,1,SPLLineIn)
		self.finish()

	def script_lineInOff(self, gesture):
		winUser.sendMessage(SPLWin,1024,0,SPLLineIn)
		self.finish()

	def script_stopFade(self, gesture):
		winUser.sendMessage(SPLWin,1024,0,SPLStop)
		self.finish()

	def script_stopInstant(self, gesture):
		winUser.sendMessage(SPLWin,1024,1,SPLStop)
		self.finish()

	def script_play(self, gesture):
		winUser.sendMessage(SPLWin, 1024, 0, SPLPlay)
		self.finish()

	def script_pause(self, gesture):
		playingNow = winUser.sendMessage(SPLWin, 1024, 0, SPL_TrackPlaybackStatus)
		# Translators: Presented when no track is playing in Station Playlist Studio.
		if not playingNow: ui.message(_("There is no track playing. Try pausing while a track is playing."))
		elif playingNow == 3: winUser.sendMessage(SPLWin, 1024, 0, SPLPause)
		else: winUser.sendMessage(SPLWin, 1024, 1, SPLPause)
		self.finish()

	def script_libraryScanProgress(self, gesture):
		scanned = winUser.sendMessage(SPLWin, 1024, 1, SPLLibraryScanCount)
		if scanned >= 0:
			# Translators: Announces number of items in the Studio's track library (example: 1000 items scanned).
			ui.message(_("Scan in progress with {itemCount} items scanned").format(itemCount = scanned))
		else:
			# Translators: Announces number of items in the Studio's track library (example: 1000 items scanned).
			ui.message(_("Scan complete with {itemCount} items scanned").format(itemCount = winUser.sendMessage(SPLWin, 1024, 0, SPLLibraryScanCount)))
		self.finish()

	def script_listenerCount(self, gesture):
		# Translators: Announces number of stream listeners.
		ui.message(_("Listener count: {listenerCount}").format(listenerCount = winUser.sendMessage(SPLWin, 1024, 0, SPLListenerCount)))
		self.finish()

	def script_remainingTime(self, gesture):
		remainingTime = winUser.sendMessage(SPLWin, 1024, 3, SPLCurTrackPlaybackTime)
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

	def script_statusInfo(self, gesture):
		SPLWin = user32.FindWindowA("SPLStudio", None) # Used ANSI version, as Wide char version always returns 0.
		if not SPLWin:
			ui.message(_("SPL Studio is not running."))
			self.finish()
			return
		# For consistency reasons (because of the Studio status bar), messages in this method will remain in English.
		statusInfo = []
		# 17.04: For Studio 5.10 and up, announce playback and automation status.
		playingNow = winUser.sendMessage(SPLWin, 1024, 0, SPL_TrackPlaybackStatus)
		statusInfo.append("Play status: playing" if playingNow else "Play status: stopped")
		# For automation, Studio 5.11 and earlier does not have an easy way to detect this flag, thus resort to using playback status.
		if winUser.sendMessage(SPLWin, 1024, 0, SPLVersion) < 520:
			statusInfo.append("Automation on" if playingNow == 2 else "Automation off")
		else:
			statusInfo.append("Automation on" if winUser.sendMessage(SPLWin, 1024, 1, SPLStatusInfo) else "Automation off")
			# 5.20 and later.
			statusInfo.append("Microphone on" if winUser.sendMessage(SPLWin, 1024, 2, SPLStatusInfo) else "Microphone off")
			statusInfo.append("Line-inon" if winUser.sendMessage(SPLWin, 1024, 3, SPLStatusInfo) else "Line-in off")
			statusInfo.append("Record to file on" if winUser.sendMessage(SPLWin, 1024, 4, SPLStatusInfo) else "Record to file off")
			cartEdit = winUser.sendMessage(SPLWin, 1024, 5, SPLStatusInfo)
			cartInsert = winUser.sendMessage(SPLWin, 1024, 6, SPLStatusInfo)
			if cartEdit: statusInfo.append("Cart Edit on")
			elif not cartEdit and cartInsert: statusInfo.append("Cart Insert on")
			else: statusInfo.append("Cart Edit off")
		ui.message("; ".join(statusInfo))
		self.finish()
	# Translators: Input help message for a SPL Controller command.
	script_statusInfo.__doc__ = _("Announces Studio status such as track playback status from other programs")

	def script_conHelp(self, gesture):
		import gui, wx
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
		"kb:q":"statusInfo",
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
			import controlTypes, encoders
			if obj.windowClassName == "TListView":
				clsList.insert(0, encoders.SAMEncoder)
			elif obj.windowClassName == "SysListView32" and obj.role == controlTypes.ROLE_LISTITEM:
					clsList.insert(0, encoders.SPLEncoder)
