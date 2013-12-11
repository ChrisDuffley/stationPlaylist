# Station Playlist Utilities
# Author: Joseph Lee
# Copyright 2013, released under GPL.
# Adds a few utility features such as switching focus to the SPL Studio window and some global scripts.

import winUser
from ctypes import windll
import globalPluginHandler
import api
import ui
from functools import wraps
import tones

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

# SPL Studio uses WM messages to send and receive data, similar to Winamp (see NVDA sources/appModules.winamp.py for more information).
user32 = windll.user32 # user32.dll.
SPLMSG = winUser.WM_USER

# Various SPL IPC tags.
SPLVersion = 2 # For IPC testing purposes.
SPLPlay = 12
SPLStop = 13
SPLPause = 15
SPLAutomate = 16
SPLMic = 17
SPLLineIn = 18
SPLListenerCount = 35
SPLVTPlaybackTime = 37 # VT = voice track.
SPL_TrackPlaybackStatus = 104
SPLCurTrackPlaybackTime = 105


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# The handle to SPL window (keep this guy handy).
	SPLWin = 0 #For now.

	#Global layer environment (see the app module for more information).
	SPLGlobalCMD = False # Control SPL from anywhere.
	SPLFG = api.getForegroundObject()

	def getScript(self, gesture):
		if not self.SPLGlobalCMD:
			return globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		script = globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		if not script:
			script = finally_(self.script_error, self.finish)
		return finally_(script, self.finish)

	def finish(self):
		self.SPLGlobalCMD = False
		self.clearGestureBindings()
		self.bindGestures(self.__gestures)

	def script_error(self, gesture):
		tones.beep(120, 100)

	# Try to see if SPL foreground object can be fetched. This is used for switching to SPL Studio window from anywhere.

	def fetchSPLForegroundWindow(self):
		# Let us see if SPL foreground can be fetched.
		import appModuleHandler, NVDAObjects
		# First test: is splstudio running? Tell me the handle, please.
		if user32.FindWindowA("SPLStudio", None) == 0: return None # Used ANSI version, as Wide char version always returns 0.
		# Continue with the method.
		fgTest = api.getForegroundObject()
		# In some windows, the parent of foreground window is Desktop.
		fg = fgTest.simpleParent if not isinstance(fgTest.simpleParent, NVDAObjects.window.Desktop) else fgTest
		while fg.simpleNext != None:
			if "splstudio" in appModuleHandler.getAppModuleForNVDAObject(fg).appModuleName: break
			else: fg = fg.simpleNext
		return fg

	# Switch focus to SPL Studio window from anywhere.
	def script_focusToSPLWindow(self, gesture):
		import appModuleHandler, ui
		# Don't do anything if we're already focus on SPL Studio.
		if "splstudio" in appModuleHandler.getAppModuleForNVDAObject(api.getForegroundObject()).appModuleName: return
		else: SPLFG = self.fetchSPLForegroundWindow()
		# SPL, are you running?
		if SPLFG == None: ui.message("SPL Studio is not running")
		# If user pressed Windows+M to minimize windows, give a message to switch to SPL Studio window manually. If not, move focus.
		else: SPLFG.setFocus() if SPLFG.name != "Program Manager" else ui.message("Press Alt+Tab to switch to SPL Studio window")
	script_focusToSPLWindow.__doc__="Moves to SPL Studio window from other programs."

	# The global commands driver.
	# This layer set allows the user to control various aspects of SPL Studio from anywhere.
	def script_globalCMDPrefix(self, gesture):
		import appModuleHandler
		# Erorr checks:
		# 1. If SPL Studio is not running, print an error message.
		# 2. If we're already  in SPL, report that the user is in SPL. This is temporary - in the end, pass this gesture to the app module portion.
		if "splstudio" in appModuleHandler.getAppModuleForNVDAObject(api.getForegroundObject()).appModuleName:
			ui.message("You are already in SPL Studio window. For status commands, use status layer commands.")
			self.finish()
			return
		self.SPLWin = user32.FindWindowA("SPLStudio", None)
		if self.SPLWin == 0:
			ui.message("SPL Studio is not running.")
			self.finish()
			return
		# No errors, so continue.
		if not self.SPLGlobalCMD:
			self.bindGestures(self.__SPLControllerGestures)
			self.SPLGlobalCMD = True
			ui.message("SPL Controller")
		else:
			self.script_error(gesture)
			self.finish()

	# The layer commands themselves.

	def script_automateOn(self, gesture):
		winUser.sendMessage(self.SPLWin,SPLMSG,1,SPLAutomate)
		self.finish()

	def script_automateOff(self, gesture):
		winUser.sendMessage(self.SPLWin,SPLMSG,0,SPLAutomate)
		self.finish()

	def script_micOn(self, gesture):
		winUser.sendMessage(self.SPLWin,SPLMSG,1,SPLMic)
		self.finish()

	def script_micOff(self, gesture):
		winUser.sendMessage(self.SPLWin,SPLMSG,0,SPLMic)
		self.finish()

	def script_lineInOn(self, gesture):
		winUser.sendMessage(self.SPLWin,SPLMSG,1,SPLLineIn)
		self.finish()

	def script_lineInOff(self, gesture):
		winUser.sendMessage(self.SPLWin,SPLMSG,0,SPLLineIn)
		self.finish()

	def script_stopFade(self, gesture):
		winUser.sendMessage(self.SPLWin,SPLMSG,0,SPLStop)
		self.finish()

	def script_stopInstant(self, gesture):
		winUser.sendMessage(self.SPLWin,SPLMSG,1,SPLStop)
		self.finish()

	def script_play(self, gesture):
		winUser.sendMessage(self.SPLWin, SPLMSG, 0, SPLPlay)
		self.finish()

	def script_pause(self, gesture):
		playingNow = winUser.sendMessage(self.SPLWin, SPLMSG, 0, SPL_TrackPlaybackStatus)
		if not playingNow: ui.message("There is no track playing. Try pausing while a track is playing.")
		elif playingNow == 3: winUser.sendMessage(self.SPLWin, SPLMSG, 0, SPLPause)
		else: winUser.sendMessage(self.SPLWin, SPLMSG, 1, SPLPause)
		self.finish()




	__SPLControllerGestures={
		"kb:p":"play",
		"kb:a":"automateOn",
		"kb:shift+a":"automateOff",
		"kb:m":"micOn",
		"kb:shift+m":"micOff",
		"kb:l":"lineInOn",
		"kb:shift+l":"lineInOff",
		"kb:s":"stopFade",
		"kb:t":"stopInstant",
		"kb:u":"pause"
	}


	__gestures={
		"kb:nvda+shift+`":"focusToSPLWindow",
		"kb:nvda+`":"globalCMDPrefix"
	}
