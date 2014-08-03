# Station Playlist Utilities
# Author: Joseph Lee
# Copyright 2013-2014, released under GPL.
# Adds a few utility features such as switching focus to the SPL Studio window and some global scripts, along with support for Sam Encoder.

from ctypes import windll
from functools import wraps
import os
import time
from configobj import ConfigObj # Configuration management; configspec will be used to store app module and global plugin settings in one ini file.
import globalPluginHandler
import api
import ui
import speech
import braille
import config # Look up the user config folder, to be used in 4.0 and later.
import review
import textInfos
from NVDAObjects.IAccessible import IAccessible
import winUser
import tones
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
user32 = windll.user32 # user32.dll.
SPLMSG = winUser.WM_USER

# Various SPL IPC tags.
SPLPlay = 12
SPLStop = 13
SPLPause = 15
SPLAutomate = 16
SPLMic = 17
SPLLineIn = 18
SPL_TrackPlaybackStatus = 104
SPLCurTrackPlaybackTime = 105

# Needed in SAM Encoder support:
SAMFocusToStudio = {} # A dictionary to record whether to switch to SPL Studio for this encoder.
SAMStreamLabels= {} # A dictionary to store custom labels for each stream.
SAMStaticStreamLabels = {} # The static stream label dictionary which is used to avoid unnecesary file writes.

# Configuration management.
Config = None

# If the SAM encoder labels are modified, try writing them to disk.

# Try to see if SPL foreground object can be fetched. This is used for switching to SPL Studio window from anywhere and to switch to Studio window from SAM encoder window.

def fetchSPLForegroundWindow():
	# Turns out NVDA core does have a method to fetch desktop objects, so use this to find SPL window from among its children.
	dt = api.getDesktopObject()
	for fg in dt.children:
		if "splstudio" in fg.appModule.appModuleName: return fg
	return None


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Translators: Script category for Station Playlist commands in input gestures dialog.
	scriptCategory = _("Station Playlist Studio")

	# The handle to SPL window (keep this guy handy).
	SPLWin = 0 #For now.

	# Do some initialization, such as stream labels for SAM encoders.
	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		# Load add-on configuration from a file (todo: use configspec to read only certain sectoins).
		global config
		config = ConfigObj(os.path.join(config.getUserDefaultConfigPath(), "splstudio.ini"))
		# Read stream labels.
		streamLabelPath = os.path.join(os.path.dirname(__file__), "SAMStreamLabels.ini")
		if os.path.isfile(streamLabelPath) and os.path.getsize(streamLabelPath) > 0:
			labels = open(streamLabelPath)
			for label in labels:
				labelStr = label.strip()
				labelEntry = labelStr.split("=")
				# Assign both static and realtime dictionaries.
				SAMStaticStreamLabels[labelEntry[0]] = labelEntry[1]
				SAMStreamLabels[labelEntry[0]] = labelEntry[1]
			labels.close()

	# Save configuration file.
	def terminate(self):
		global config
		config.write()

			#Global layer environment (see the app module for more information).
	SPLController = False # Control SPL from anywhere.

	def getScript(self, gesture):
		if not self.SPLController:
			return globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		script = globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		if not script: script = finally_(self.script_error, self.finish)
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
				# Translators: Presented when Studio is minimized to system tray (notification area).
				if SPLFG == None: ui.message(_("SPL minimized to system tray."))
				else: SPLFG.setFocus()
	# Translators: Input help mode message for a command to switch to Station Playlist Studio from any program.
	script_focusToSPLWindow.__doc__=_("Moves to SPL Studio window from other programs.")

	# The SPL Controller:
	# This layer set allows the user to control various aspects of SPL Studio from anywhere.
	def script_SPLControllerPrefix(self, gesture):
		# Error checks:
		# 1. If SPL Studio is not running, print an error message.
		# 2. If we're already  in SPL, report that the user is in SPL. This is temporary - in the end, pass this gesture to the app module portion.
		if "splstudio" in api.getForegroundObject().appModule.appModuleName:
			# Translators: Presented when NVDA cannot enter SPL Controller layer since SPL Studio is focused.
			ui.message(_("You are already in SPL Studio window. For status commands, use SPL Assistant commands."))
			self.finish()
			return
		self.SPLWin = user32.FindWindowA("SPLStudio", None)
		if self.SPLWin == 0:
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
		# Translators: Presented when no track is playing in Station Playlist Studio.
		if not playingNow: ui.message(_("There is no track playing. Try pausing while a track is playing."))
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
		#"kb:nvda+shift+`":"focusToSPLWindow",
		#"kb:nvda+`":"SPLControllerPrefix"
	}

	# Support for Sam Encoder
	# Sam encoder is a Winamp plug-in, so we can use overlay class.
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		fg = api.getForegroundObject()
		if obj.windowClassName == "TListView" and fg.windowClassName == "TfoSCEncoders":
			clsList.insert(0, self.SAMEncoderWindow)

	class SAMEncoderWindow(IAccessible):
		# Support for Sam Encoder window.

		# Few useful variables for encoder list:
		focusToStudio = False # If true, Studio will gain focus after encoder connects.

		def script_connect(self, gesture):
			gesture.send()
			# Translators: Presented when SAM Encoder is trying to connect to a streaming server.
			ui.message(_("Connecting..."))
			# Keep an eye on the stream's description field until connected or error occurs.
			while True:
				time.sleep(0.001)
				info = review.getScreenPosition(self)[0]
				info.expand(textInfos.UNIT_LINE)
				if "Error" in info.text:
					# Announce the description of the error.
					ui.message(self.description[self.description.find("Status")+8:])
					break
				elif "Encoding" in info.text:
					# We're on air, so exit.
					if self.focusToStudio: fetchSPLForegroundWindow().setFocus()
					tones.beep(1000, 150)
					break
		# Translators: Input help mode message in SAM Encoder window.
		script_connect.__doc__=_("Connects to a streaming server.")

		def script_disconnect(self, gesture):
			gesture.send()
			# Translators: Presented when SAM Encoder is disconnecting from a streaming server.
			ui.message(_("Disconnecting..."))
		# Translators: Input help mode message in SAM Encoder window.
		script_disconnect.__doc__=_("Disconnects from a streaming server.")

		def script_toggleFocusToStudio(self, gesture):
			if not self.focusToStudio:
				self.focusToStudio = True
				SAMFocusToStudio[self.name] = True
				# Translators: Presented when toggling the setting to switch to Studio when connected to a streaming server.
				ui.message(_("Switch to Studio after connecting"))
			else:
				self.focusToStudio = False
				SAMFocusToStudio[self.name] = False
				# Translators: Presented when toggling the setting to switch to Studio when connected to a streaming server.
				ui.message(_("Do not switch to Studio after connecting"))
		# Translators: Input help mode message in SAM Encoder window.
		script_toggleFocusToStudio.__doc__=_("Toggles whether NVDA will switch to Studio when connected to a streaming server.")

		def script_streamLabeler(self, gesture):
			# Translators: The title of the stream labeler dialog (example: stream labeler for 1).
			streamTitle = _("Stream labeler for {streamEntry}").format(streamEntry = self.name)
			# Translators: The text of the stream labeler dialog.
			streamText = _("Enter the label for this stream")
			dlg = wx.TextEntryDialog(gui.mainFrame,
			streamText, streamTitle, defaultValue=""if self.name not in SAMStreamLabels else SAMStreamLabels[self.name])
			def callback(result):
				global config
				if result == wx.ID_OK:
					if dlg.GetValue() != "": config["SAMStreamLabels"][self.name] = dlg.GetValue()
					else: del config["SAMStreamLabels"][self.name]
			gui.runScriptModalDialog(dlg, callback)
		# Translators: Input help mode message in SAM Encoder window.
		script_streamLabeler.__doc__=_("Opens a dialog to label the selected encoder.")


		def initOverlayClass(self):
			# Can I switch to Studio when connected to a streaming server?
			try:
				self.focusToStudio = SAMFocusToStudio[self.name]
			except KeyError:
				pass

		def event_gainFocus(self):
			try:
				global config
				streamLabel = config["SAMStreamLabels"][self.name]
			except KeyError:
				streamLabel = None
			# Speak the stream label if it exists.
			if streamLabel is not None: speech.speakMessage(streamLabel)
			super(type(self), self).reportFocus()
			# Braille the stream label if present.
			if streamLabel is not None:
				brailleStreamLabel = self.name + ": " + streamLabel
				braille.handler.message(brailleStreamLabel)


		__gestures={
			"kb:f9":"connect",
			"kb:f10":"disconnect",
			"kb:f11":"toggleFocusToStudio",
			"kb:f12":"streamLabeler"
		}

