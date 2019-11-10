# StationPlaylist Utilities
# Author: Joseph Lee
# Copyright 2013-2019, released under GPL.
# Adds a few utility features such as switching focus to the SPL Studio window and some global scripts.
# For encoder support, see the encoders package.

from functools import wraps
import globalPluginHandler
import api
import ui
import globalVars
import config
from NVDAObjects.IAccessible import getNVDAObjectFromEvent
from winUser import user32, sendMessage, OBJID_CLIENT
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
SPLWin = 0 # A handle to studio window.

# Various SPL IPC tags.
SPLVersion = 2
SPLPlay = 12
SPLStop = 13
SPLPause = 15
SPLAutomate = 16
SPLMic = 17
SPLLineIn = 18
SPLCartPlayer = 19
SPLLibraryScanCount = 32
SPLListenerCount = 35
SPLStatusInfo = 39
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
C: Announce name and duration of the currently playing track.
E: Announce connected encoders if any.
I: Announce listener count.
Q: Announce Studio status information.
R: Remaining time for the playing track.
Shift+R: Library scan progress.
Function keys and number row keys with or without Shift, Alt, and Control keys: Play carts.""")

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Translators: Script category for StationPlaylist commands in input gestures dialog.
	scriptCategory = _("StationPlaylist")

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		# #19.04/18.09.8-LTS: don't even think about proceeding in secure screens.
		# Also, skip over the rest if appx is in effect.
		if globalVars.appArgs.secure or config.isAppX: return

	#Global layer environment (see the app module for more information).
	SPLController = False # Control SPL from anywhere.
	# Manual definitions of cart keys.
	fnCartKeys = ("f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12")
	numCartKeys = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=")

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
		# Don't do anything if we're already focus on SPL Studio.
		if "splstudio" in api.getForegroundObject().appModule.appModuleName: return
		SPLHwnd = user32.FindWindowW(u"SPLStudio", None)
		if not SPLHwnd: ui.message(_("SPL Studio is not running."))
		# 17.01: SetForegroundWindow function is better, as there's no need to traverse top-level windows and allows users to "switch" to SPL window if the window is minimized.
		else: user32.SetForegroundWindow(user32.FindWindowW(u"TStudioForm", None))
	# Translators: Input help mode message for a command to switch to StationPlaylist Studio from any program.
	script_focusToSPLWindow.__doc__=_("Moves to SPL Studio window from other programs.")

	# The SPL Controller:
	# This layer set allows the user to control various aspects of SPL Studio from anywhere.
	def script_SPLControllerPrefix(self, gesture):
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
		SPLWin = user32.FindWindowW(u"SPLStudio", None)
		if SPLWin == 0:
			# Translators: Presented when StationPlaylist Studio is not running.
			ui.message(_("SPL Studio is not running."))
			self.finish()
			return
		# No errors, so continue.
		if not self.SPLController:
			self.bindGestures(self.__SPLControllerGestures)
			# 17.12: also bind cart keys.
			# Exclude number row if Studio Standard is running.
			cartKeys = self.fnCartKeys
			if not getNVDAObjectFromEvent(user32.FindWindowW(u"TStudioForm", None), OBJID_CLIENT, 0).name.startswith("StationPlaylist Studio Standard"):
				cartKeys+=self.numCartKeys
			for cart in cartKeys:
				self.bindGesture("kb:%s"%cart, "cartsWithoutBorders")
				self.bindGesture("kb:shift+%s"%cart, "cartsWithoutBorders")
				self.bindGesture("kb:control+%s"%cart, "cartsWithoutBorders")
				self.bindGesture("kb:alt+%s"%cart, "cartsWithoutBorders")
			self.SPLController = True
			# Translators: The name of a layer command set for StationPlaylist add-on.
			# Hint: it is better to translate it as "SPL Control Panel."
			ui.message(_("SPL Controller"))
		else:
			self.script_error(gesture)
			self.finish()
	# Translators: Input help mode message for a layer command in StationPlaylist add-on.
	script_SPLControllerPrefix.__doc__=_("SPl Controller layer command. See add-on guide for available commands.")

	# The layer commands themselves. Calls user32.SendMessage method for each script.

	def script_automateOn(self, gesture):
		sendMessage(SPLWin,1024,1,SPLAutomate)
		self.finish()

	def script_automateOff(self, gesture):
		sendMessage(SPLWin,1024,0,SPLAutomate)
		self.finish()

	def script_micOn(self, gesture):
		sendMessage(SPLWin,1024,1,SPLMic)
		self.finish()

	def script_micOff(self, gesture):
		sendMessage(SPLWin,1024,0,SPLMic)
		self.finish()

	def script_micNoFade(self, gesture):
		sendMessage(SPLWin,1024,2,SPLMic)
		self.finish()

	def script_lineInOn(self, gesture):
		sendMessage(SPLWin,1024,1,SPLLineIn)
		self.finish()

	def script_lineInOff(self, gesture):
		sendMessage(SPLWin,1024,0,SPLLineIn)
		self.finish()

	def script_stopFade(self, gesture):
		sendMessage(SPLWin,1024,0,SPLStop)
		self.finish()

	def script_stopInstant(self, gesture):
		sendMessage(SPLWin,1024,1,SPLStop)
		self.finish()

	def script_play(self, gesture):
		sendMessage(SPLWin, 1024, 0, SPLPlay)
		self.finish()

	def script_pause(self, gesture):
		playingNow = sendMessage(SPLWin, 1024, 0, SPL_TrackPlaybackStatus)
		# Translators: Presented when no track is playing in StationPlaylist Studio.
		if not playingNow: ui.message(_("There is no track playing. Try pausing while a track is playing."))
		elif playingNow == 3: sendMessage(SPLWin, 1024, 0, SPLPause)
		else: sendMessage(SPLWin, 1024, 1, SPLPause)
		self.finish()

	def script_libraryScanProgress(self, gesture):
		scanned = sendMessage(SPLWin, 1024, 1, SPLLibraryScanCount)
		if scanned >= 0:
			# Translators: Announces number of items in the Studio's track library (example: 1000 items scanned).
			ui.message(_("Scan in progress with {itemCount} items scanned").format(itemCount = scanned))
		else:
			# Translators: Announces number of items in the Studio's track library (example: 1000 items scanned).
			ui.message(_("Scan complete with {itemCount} items scanned").format(itemCount = sendMessage(SPLWin, 1024, 0, SPLLibraryScanCount)))
		self.finish()

	def script_listenerCount(self, gesture):
		# Translators: Announces number of stream listeners.
		ui.message(_("Listener count: {listenerCount}").format(listenerCount = sendMessage(SPLWin, 1024, 0, SPLListenerCount)))
		self.finish()

	def script_remainingTime(self, gesture):
		remainingTime = sendMessage(SPLWin, 1024, 3, SPLCurTrackPlaybackTime)
		# Translators: Presented when no track is playing in StationPlaylist Studio.
		if remainingTime < 0: ui.message(_("There is no track playing."))
		else:
			# 7.0: Present remaining time in hh:mm:ss format for enhanced experience (borrowed from the app module).
			# 17.09 optimization: perform in-place string construction instead of using objects and building a list, results in fewer bytecode instructions.
			# The string formatter will zero-fill minutes and seconds if less than 10.
			# 19.11.1/18.09.13-LTS: use floor division due to division differences between Python 2 and 3.
			remainingTime = (remainingTime//1000)+1
			if remainingTime == 0: ui.message("00:00")
			elif 1 <= remainingTime <= 59:
				ui.message("00:{ss:02d}".format(ss = remainingTime))
			else:
				mm, ss = divmod(remainingTime, 60)
				if mm > 59:
					hh, mm = divmod(mm, 60)
					ui.message("{hh:02d}:{mm:02d}:{ss:02d}".format(hh = hh, mm = mm, ss = ss))
				else:
					ui.message("{mm:02d}:{ss:02d}".format(mm = mm, ss = ss))
		self.finish()

	def script_encoderStatus(self, gesture):
		# Go through below procedure, as custom commands can be assigned for this script.
		SPLWin = user32.FindWindowW(u"SPLStudio", None)
		if not SPLWin:
			ui.message(_("SPL Studio is not running."))
			self.finish()
			return
		from . import encoders
		encoders.announceEncoderConnectionStatus()
		self.finish()
	# Translators: Input help message for a SPL Controller command.
	script_encoderStatus.__doc__ = _("Announces stream encoder status from other programs")

	def script_statusInfo(self, gesture):
		# Go through below procedure, as custom commands can be assigned for this script.
		SPLWin = user32.FindWindowW(u"SPLStudio", None)
		if not SPLWin:
			ui.message(_("SPL Studio is not running."))
			self.finish()
			return
		# Studio 5.20 and later allows fetching status bar info from anywhere via Studio API, including playback and automation status.
		# For consistency reasons (because of the Studio status bar), messages in this method will remain in English.
		statusInfo = []
		playingNow = sendMessage(SPLWin, 1024, 0, SPL_TrackPlaybackStatus)
		statusInfo.append("Play status: playing" if playingNow else "Play status: stopped")
		statusInfo.append("Automation On" if sendMessage(SPLWin, 1024, 1, SPLStatusInfo) else "Automation Off")
		statusInfo.append("Microphone On" if sendMessage(SPLWin, 1024, 2, SPLStatusInfo) else "Microphone Off")
		statusInfo.append("Line-In On" if sendMessage(SPLWin, 1024, 3, SPLStatusInfo) else "Line-In Off")
		statusInfo.append("Record to file On" if sendMessage(SPLWin, 1024, 4, SPLStatusInfo) else "Record to file Off")
		cartEdit = sendMessage(SPLWin, 1024, 5, SPLStatusInfo)
		cartInsert = sendMessage(SPLWin, 1024, 6, SPLStatusInfo)
		if cartEdit: statusInfo.append("Cart Edit On")
		elif not cartEdit and cartInsert: statusInfo.append("Cart Insert On")
		else: statusInfo.append("Cart Edit Off")
		ui.message("; ".join(statusInfo))
		self.finish()
	# Translators: Input help message for a SPL Controller command.
	script_statusInfo.__doc__ = _("Announces Studio status such as track playback status from other programs")

	def script_currentTrackTitle(self, gesture):
		studioAppMod = getNVDAObjectFromEvent(user32.FindWindowW(u"TStudioForm", None), OBJID_CLIENT, 0).appModule
		studioAppMod.script_sayCurrentTrackTitle(None)
		self.finish()

	def script_nextTrackTitle(self, gesture):
		studioAppMod = getNVDAObjectFromEvent(user32.FindWindowW(u"TStudioForm", None), OBJID_CLIENT, 0).appModule
		studioAppMod.script_sayNextTrackTitle(None)
		self.finish()

	def script_cartsWithoutBorders(self, gesture):
		try:
			modifier, cart = gesture.displayName.split("+")
		except ValueError:
			modifier, cart = None, gesture.displayName
		# Pull in modifier values from the following list.
		modifier = (None, "shift", "ctrl", "alt").index(modifier)
		# #85 (18.11.1/18.09.5-LTS): Cart index formula has changed in Studio 5.30.
		# Both start with the following.
		cart = (self.fnCartKeys+self.numCartKeys).index(cart)+1
		# Studio 5.20 and earlier requires setting high (cart) and low (modifier) words (multiplying by 64K+1).
		if sendMessage(SPLWin, 1024, 0, SPLVersion) < 530:
			cart = (cart * 0x00010000) + modifier+1
		# Whereas simplified to cart bank setup in Studio 5.30 and later.
		else: cart += (modifier * 24)
		sendMessage(SPLWin,1024,cart,SPLCartPlayer)
		self.finish()

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
		"kb:e":"encoderStatus",
		"kb:i":"listenerCount",
		"kb:q":"statusInfo",
		"kb:c":"currentTrackTitle",
		"kb:shift+c":"nextTrackTitle",
		"kb:h":"conHelp"
	}

	__gestures={}
