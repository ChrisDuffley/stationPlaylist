# Station Playlist Audio Engine
# Author: Joseph Lee
# Copyright 2014, released under GPL.
# Mainly used for encoder window support.

import threading
import os
import time
from configobj import ConfigObj
import appModuleHandler
import api
import ui
import speech
import braille
import controlTypes
import globalVars
import winUser
import tones
import gui
import wx
import addonHandler
addonHandler.initTranslation()

# SPL Studio uses WM messages to send and receive data, similar to Winamp (see NVDA sources/appModules/winamp.py for more information).
user32 = winUser.user32 # user32.dll.
SPLWin = 0 # A handle to studio window.
SPLMSG = winUser.WM_USER

# Needed in encoder connection support
SPLPlay = 12

# Needed in SAM and SPL Encoder support:
SAMFocusToStudio = {} # A dictionary to record whether to switch to SPL Studio for this encoder.
SPLFocusToStudio = {}
SAMPlayAfterConnecting = {}
SPLPlayAfterConnecting = {}
SAMStreamLabels= {} # A dictionary to store custom labels for each stream.
SPLStreamLabels= {} # Same as above but optimized for SPL encoders (Studio 5.00 and later).

# Stream labels
labels = ConfigObj(os.path.join(globalVars.appArgs.configPath, "splStreamLabels.ini"))
try:
	SAMStreamLabels = dict(labels["SAMEncoders"])
except KeyError:
	SAMStreamLabels = {}
try:
	SPLStreamLabels = dict(labels["SPLEncoders"])
except KeyError:
	SPLStreamLabels = {}


# Try to see if SPL foreground object can be fetched. This is used for switching to SPL Studio window from anywhere and to switch to Studio window from encoder windows.

def fetchSPLForegroundWindow():
	# Turns out NVDA core does have a method to fetch desktop objects, so use this to find SPL window from among its children.
	dt = api.getDesktopObject()
	for fg in dt.children:
		if "splstudio" in fg.appModule.appModuleName: return fg
	return None


class AppModule(appModuleHandler.AppModule):

	# Translators: Script category for Station Playlist commands in input gestures dialog.
	scriptCategory = _("Station Playlist Studio")


	def terminate(self):
		global labels, SAMStreamLabels, SPLStreamLabels
		labels["SAMEncoders"] = SAMStreamLabels
		labels["SPLEncoders"] = SPLStreamLabels
		labels.write()

	# Announce stream labels
	def event_gainFocus(self, obj, nextHandler):
		if self.connecting: return
		streamLabel = self._get_streamLabel(obj)
		if streamLabel is not None:
			speech.speakMessage(streamLabel)
			brailleStreamLabel = str(obj.IAccessibleChildID) + ":" + streamLabel
			braille.handler.message(brailleStreamLabel)
		nextHandler()


	# Few setup routines for scripts.

	def isEncoderWindow(self, obj, fg=None):
		# The foreground variable is intended for debugging purposes and should not be set from outside the Python Console.
		if not fg: fg = api.getForegroundObject()
		if obj.role == controlTypes.ROLE_LISTITEM:
			if obj.windowClassName == "TListView" and fg.windowClassName == "TfoSCEncoders":
				return "SAM"
			elif obj.windowClassName == "SysListView32" and fg.windowClassName == "#32770":
				return "SPL"
		return None

	def _get_streamLabel(self, encoder, fg=None):
		streamLabel = None
		encoderType = self.isEncoderWindow(encoder, fg=fg)
		if encoderType == "SAM":
			try:
				streamLabel = SAMStreamLabels[encoder.name]
			except KeyError:
				pass
		elif encoderType == "SPL":
			try:
				streamLabel = SPLStreamLabels[str(encoder.firstChild.rowNumber)]
			except KeyError:
				pass
		return streamLabel

	# Routines for each encoder
	# Mostly connection monitoring

	def connect_sam(self, encoderWindow, gesture):
		gesture.send()
		# Translators: Presented when SAM Encoder is trying to connect to a streaming server.
		ui.message(_("Connecting..."))
		# Oi, status thread, can you keep an eye on the connection status for me?
		statusThread = threading.Thread(target=self.reportConnectionStatus_sam, args=(encoderWindow,))
		statusThread.name = "Connection Status Reporter"
		statusThread.start()

	def reportConnectionStatus_sam(self, encoderWindow):
		# Keep an eye on the stream's description field until connected or error occurs.
		# In order to not block NVDA commands, this will be done using a different thread.
		SPLWin = user32.FindWindowA("SPLStudio", None)
		toneCounter = 0
		while True:
			time.sleep(0.001)
			toneCounter+=1
			if toneCounter%250 == 0: tones.beep(500, 50) # Play status tones every second.
			if "Error" in encoderWindow.description:
				# Announce the description of the error.
				ui.message(encoderWindow.description[encoderWindow.description.find("Status")+8:])
				break
			elif "Encoding" in encoderWindow.description or "Encoded" in encoderWindow.description:
				# We're on air, so exit.
				tones.beep(1000, 150)
				break
		try:
			focusToStudio = SAMFocusToStudio[encoderWindow.name]
		except KeyError:
			focusToStudio = False
		try:
			playAfterConnecting = SAMPlayAfterConnecting[encoderWindow.name]
		except KeyError:
			playAfterConnecting = False
		if focusToStudio:
			fetchSPLForegroundWindow().setFocus()
		if playAfterConnecting:
			winUser.sendMessage(SPLWin, SPLMSG, 0, SPLPlay)

	# Only needed in SPL Encoder to prevent focus announcement.
	connecting = False

	def connect_spl(self, encoderWindow):
		# Same as SAM's connection routine, but this time, keep an eye on self.name and a different connection flag.
		self.connecting = True
		connectButton = api.getForegroundObject().children[2]
		if connectButton.name == "Disconnect":
			self.connecting = False
			return
		ui.message(_("Connecting..."))
		# Juggle the focus around.
		connectButton.doAction()
		encoderWindow.setFocus()
		# Same as SAM encoders.
		statusThread = threading.Thread(target=self.reportConnectionStatus_spl, args=(encoderWindow,))
		statusThread.name = "Connection Status Reporter"
		statusThread.start()

	def reportConnectionStatus_spl(self, encoderWindow):
		# Same routine as SAM encoder: use a thread to prevent blocking NVDA commands.
		SPLWin = user32.FindWindowA("SPLStudio", None)
		attempt = 0
		connected = False
		while True:
			time.sleep(0.001)
			attempt += 1
			if attempt%250 == 0: tones.beep(500, 50)
			if "Unable to connect" in encoderWindow.name:
				ui.message(encoderWindow.children[1].name)
				break
			if encoderWindow.children[1].name == "Connected":
				# We're on air, so exit.
				tones.beep(1000, 150)
				break
		self.connecting = False
		try:
			focusToStudio = SPLFocusToStudio[str(encoderWindow.firstChild.rowNumber)]
		except KeyError:
			focusToStudio = False
		try:
			playAfterConnecting = SPLPlayAfterConnecting[str(encoderWindow.firstChild.rowNumber)]
		except KeyError:
			playAfterConnecting = False
		if focusToStudio:
			fetchSPLForegroundWindow().setFocus()
		if playAfterConnecting:
			winUser.sendMessage(SPLWin, SPLMSG, 0, SPLPlay)


	# Encoder scripts

	def script_connect(self, gesture):
		focus = api.getFocusObject()
		encoder = self.isEncoderWindow(focus)
		if encoder is None:
			return
		elif encoder == "SAM":
			self.connect_sam(focus, gesture)
		else:
			self.connect_spl(focus)

	def script_disconnect(self, gesture):
		gesture.send()
		if self.isEncoderWindow(api.getFocusObject()) == "SAM":
			# Translators: Presented when SAM Encoder is disconnecting from a streaming server.
			ui.message(_("Disconnecting..."))

	def script_toggleFocusToStudio(self, gesture):
		focus = api.getFocusObject()
		encoder = self.isEncoderWindow(focus)
		if not encoder:
			return
		if encoder == "SAM":
			try:
				focusToStudio = SAMFocusToStudio[focus.name]
			except KeyError:
				focusToStudio = False
		elif encoder == "SPL":
			try:
				focusToStudio = SPLFocusToStudio[str(focus.firstChild.rowNumber)]
			except KeyError:
				focusToStudio = False
		if not focusToStudio:
			focusToStudio = True
			# Translators: Presented when toggling the setting to switch to Studio when connected to a streaming server.
			ui.message(_("Switch to Studio after connecting"))
		else:
			focusToStudio = False
			# Translators: Presented when toggling the setting to switch to Studio when connected to a streaming server.
			ui.message(_("Do not switch to Studio after connecting"))
		if encoder == "SAM":
			SAMFocusToStudio[focus.name] = focusToStudio
		elif encoder == "SPL":
			SPLFocusToStudio[str(focus.firstChild.rowNumber)] = focusToStudio
	# Translators: Input help mode message in SAM Encoder window.
	script_toggleFocusToStudio.__doc__=_("Toggles whether NVDA will switch to Studio when connected to a streaming server.")

	def script_togglePlay(self, gesture):
		focus = api.getFocusObject()
		encoder = self.isEncoderWindow(focus)
		if not encoder:
			return
		if encoder == "SAM":
			try:
				playAfterConnecting = SAMPlayAfterConnecting[focus.name]
			except KeyError:
				playAfterConnecting = False
		elif encoder == "SPL":
			try:
				playAfterConnecting = SPLPlayAfterConnecting[str(focus.firstChild.rowNumber)]
			except KeyError:
				playAfterConnecting = False
		if not playAfterConnecting:
			playAfterConnecting = True
			# Translators: Presented when toggling the setting to play selected song when connected to a streaming server.
			ui.message(_("Play first track after connecting"))
		else:
			playAfterConnecting = False
			# Translators: Presented when toggling the setting to switch to Studio when connected to a streaming server.
			ui.message(_("Do not play first track after connecting"))
		if encoder == "SAM":
			SAMPlayAfterConnecting[focus.name] = playAfterConnecting
		elif encoder == "SPL":
			SPLPlayAfterConnecting[str(focus.firstChild.rowNumber)] = playAfterConnecting
	# Translators: Input help mode message in SAM Encoder window.
	script_togglePlay.__doc__=_("Toggles whether Studio will play the first song when connected to a streaming server.")

	def script_streamLabeler(self, gesture):
		encoder = api.getFocusObject()
		encoderType = self.isEncoderWindow(encoder)
		if not encoderType:
			return
		else:
			curStreamLabel = self._get_streamLabel(encoder)
			if encoderType == "SAM":
				titleText = encoder.name
			elif encoderType == "SPL":
				titleText = encoder.firstChild.name
			# Translators: The title of the stream labeler dialog (example: stream labeler for 1).
			streamTitle = _("Stream labeler for {streamEntry}").format(streamEntry = titleText)
			# Translators: The text of the stream labeler dialog.
			streamText = _("Enter the label for this stream")
			dlg = wx.TextEntryDialog(gui.mainFrame,
			streamText, streamTitle, defaultValue=curStreamLabel)
			def callback(result):
				if result == wx.ID_OK:
					if dlg.GetValue() != "":
						if encoderType == "SAM": SAMStreamLabels[encoder.name] = dlg.GetValue()
						elif encoderType == "SPL":
							SPLStreamLabels[str(encoder.firstChild.rowNumber)] = dlg.GetValue()
					else:
						if encoderType == "SAM": del SAMStreamLabels[encoder.name]
						elif encoderType == "SPL":
							del SPLStreamLabels[str(encoder.firstChild.rowNumber)]
			gui.runScriptModalDialog(dlg, callback)
	# Translators: Input help mode message in SAM Encoder window.
	script_streamLabeler.__doc__=_("Opens a dialog to label the selected encoder.")

	__gestures={
		"kb:f9":"connect",
		"kb:f10":"disconnect",
		"kb:f11":"toggleFocusToStudio",
		"kb:shift+f11":"togglePlay",
		"kb:f12":"streamLabeler"
	}

