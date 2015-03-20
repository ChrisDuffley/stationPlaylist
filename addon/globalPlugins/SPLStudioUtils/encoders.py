# StationPlaylist encoders support
# Author: Joseph Lee
# Copyright 2015, released under GPL.
# Split from main global plugin in 2015.

import threading
import os
import time
from configobj import ConfigObj
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
import gui
import wx


# SPL Studio uses WM messages to send and receive data, similar to Winamp (see NVDA sources/appModules/winamp.py for more information).
user32 = winUser.user32 # user32.dll.
SPLWin = 0 # A handle to studio window.
SPLMSG = winUser.WM_USER

# Various SPL IPC tags.
SPLPlay = 12

# Needed in Encoder support:
SPLFocusToStudio = set() # Whether to focus to Studio or not.
SPLPlayAfterConnecting = set()
SPLBackgroundMonitor = set()

# Customized for each encoder type.
SAMStreamLabels= {} # A dictionary to store custom labels for each stream.
SPLStreamLabels= {} # Same as above but optimized for SPL encoders (Studio 5.00 and later).
SAMMonitorThreads = {}
SPLMonitorThreads = {}
encoderMonCount = {"SAM":0, "SPL":0}

# Configuration management.
streamLabels = None

# Load stream labels (and possibly other future goodies) from a file-based database.
def loadStreamLabels():
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

# Report number of encoders being monitored.
def announceNumMonitoringEncoders():
	monitorCount = len(SPLBackgroundMonitor)
	if not monitorCount:
		ui.message("No encoders are being monitored")
	else:
		ui.message("Number of encoders monitored: {numberOfEncoders}".format(numberOfEncoders = monitorCount))

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

# Support for various encoders.
# Each encoder must support connection routines.

class Encoder(IAccessible):
	"""Represents an encoder from within StationPlaylist Studio or Streamer.
	This base encoder provides scripts for all encoders such as stream labeler and toggling focusing to Studio when connected.
	Subclasses must provide scripts to handle encoder connection and connection announcement routines.
	In addition, they must implement the required actions to set options such as focusing to Studio, storing stream labels and so on, as each subclass relies on a feature map.
	For example, for SAM encoder class, the feature map is SAM* where * denotes the feature in question.
	Lastly, each encoder class must provide a unique identifying string to identify the type of the encoder (e.g. SAM for SAM encoder).
	"""

	# Few useful variables for encoder list:
	focusToStudio = False # If true, Studio will gain focus after encoder connects.
	playAfterConnecting = False # When connected, the first track will be played.
	backgroundMonitor = False # Monitor this encoder for connection status changes.

	# Format the status message to prepare for monitoring multiple encoders.
	def encoderStatusMessage(self, message, id):
		if encoderMonCount[self.encoderType] > 1:
			ui.message("{encoder} {encoderNumber}: {status}".format(encoder = self.encoderType, encoderNumber = id, status = message))
		else:
			ui.message(message)

	def script_toggleFocusToStudio(self, gesture):
		if not self.focusToStudio:
			self.focusToStudio = True
			# Translators: Presented when toggling the setting to switch to Studio when connected to a streaming server.
			ui.message(_("Switch to Studio after connecting"))
		else:
			self.focusToStudio = False
			# Translators: Presented when toggling the setting to switch to Studio when connected to a streaming server.
			ui.message(_("Do not switch to Studio after connecting"))
		self._set_FocusToStudio()
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
		self.setPlayAfterConnecting()
	# Translators: Input help mode message in SAM Encoder window.
	script_togglePlay.__doc__=_("Toggles whether Studio will play the first song when connected to a streaming server.")

	def script_toggleBackgroundEncoderMonitor(self, gesture):
		if not self.backgroundMonitor:
			self.backgroundMonitor = True
			encoderMonCount[self.encoderType] += 1 # Multiple encoders.
			ui.message("Monitoring encoder {encoderNumber}".format(encoderNumber = self.IAccessibleChildID))
		else:
			self.backgroundMonitor = False
			encoderMonCount[self.encoderType] -= 1
			ui.message("Encoder {encoderNumber} will not be monitored".format(encoderNumber = self.IAccessibleChildID))
		threadPool = self.setBackgroundMonitor()
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
		curStreamLabel, title = self.getStreamLabel(getTitle=True)
		if not curStreamLabel: curStreamLabel = ""
		# Translators: The title of the stream labeler dialog (example: stream labeler for 1).
		streamTitle = _("Stream labeler for {streamEntry}").format(streamEntry = title)
		# Translators: The text of the stream labeler dialog.
		streamText = _("Enter the label for this stream")
		dlg = wx.TextEntryDialog(gui.mainFrame,
		streamText, streamTitle, defaultValue=curStreamLabel)
		def callback(result):
			if result == wx.ID_OK:
				newStreamLabel = dlg.GetValue()
				if newStreamLabel == curStreamLabel:
					return # No need to write to disk.
				else: self.setStreamLabel(newStreamLabel)
		gui.runScriptModalDialog(dlg, callback)
	# Translators: Input help mode message in SAM Encoder window.
	script_streamLabeler.__doc__=_("Opens a dialog to label the selected encoder.")

	def script_streamLabelEraser(self, gesture):
		ui.message("Stream label successor in progress")
		# Translators: The title of the stream label eraser.
		streamEraserTitle = _("Stream label eraser")
		# Translators: The text of the stream label eraser dialog.
		streamEraserText = _("Enter the position of the encoder you wish to delete or will delete")
		dlg = wx.NumberEntryDialog(gui.mainFrame,
		streamEraserText, "", streamEraserTitle, self.IAccessibleChildID, 1, self.simpleParent.childCount)
		def callback(result):
			if result == wx.ID_OK:
				self.removeStreamLabel(str(dlg.GetValue()))
		gui.runScriptModalDialog(dlg, callback)
	# Translators: Input help mode message in SAM Encoder window.
	script_streamLabelEraser.__doc__=_("Opens a dialog to erase stream labels from an encoder that was deleted.")

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
		# Load stream labels upon request.
		if not streamLabels: loadStreamLabels()
		encoderIdentifier = " ".join([self.encoderType, str(self.IAccessibleChildID)])
		# Can I switch to Studio when connected to a streaming server?
		try:
			self.focusToStudio = encoderIdentifier in SPLFocusToStudio
		except KeyError:
			pass
		# Am I being monitored for connection changes?
		try:
			self.backgroundMonitor = encoderIdentifier in SPLBackgroundMonitor
		except KeyError:
			pass

	def reportFocus(self):
		try:
			streamLabel = self.getStreamLabel()[0]
		except TypeError:
			streamLabel = None
		# Speak the stream label if it exists.
		if streamLabel is not None:
			try:
				self.name = "(" + streamLabel + ") " + self.name
			except TypeError:
				pass
		super(Encoder, self).reportFocus()


	__gestures={
		"kb:f11":"toggleFocusToStudio",
		"kb:shift+f11":"togglePlay",
		"kb:control+f11":"toggleBackgroundEncoderMonitor",
		"kb:f12":"streamLabeler",
		"kb:control+f12":"streamLabelEraser",
		"kb:NVDA+F12":"encoderDateTime"
	}


class SAMEncoder(Encoder):
	# Support for Sam Encoders.

	encoderType = "SAM"

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
		alreadyEncoding = False
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
			if not " ".join([self.encoderType, str(self.IAccessibleChildID)]) in SPLBackgroundMonitor: return

	def script_connect(self, gesture):
		gesture.send()
		# Translators: Presented when SAM Encoder is trying to connect to a streaming server.
		ui.message(_("Connecting..."))
		# Oi, status thread, can you keep an eye on the connection status for me?
		if not self.backgroundMonitor:
			statusThread = threading.Thread(target=self.reportConnectionStatus, kwargs=dict(connecting=True))
			statusThread.name = "Connection Status Reporter " + str(self.IAccessibleChildID)
			statusThread.start()
			SAMMonitorThreads[self.IAccessibleChildID] = statusThread

	def script_disconnect(self, gesture):
		gesture.send()
		# Translators: Presented when SAM Encoder is disconnecting from a streaming server.
		ui.message(_("Disconnecting..."))

	def _set_FocusToStudio(self):
		SAMIdentifier = " ".join([self.encoderType, str(self.IAccessibleChildID)])
		if self.focusToStudio and not SAMIdentifier in SPLFocusToStudio:
			SPLFocusToStudio.add(SAMIdentifier)
		elif not self.focusToStudio and SAMIdentifier in SPLFocusToStudio:
			SPLFocusToStudio.remove(SAMIdentifier)

	def setPlayAfterConnecting(self):
		SAMIdentifier = " ".join([self.encoderType, str(self.IAccessibleChildID)])
		if self.playAfterConnecting and not SAMIdentifier in SPLPlayAfterConnecting:
			SPLPlayAfterConnecting.add(SAMIdentifier)
		elif not self.playAfterConnecting and SAMIdentifier in SPLPlayAfterConnecting:
			SPLPlayAfterConnecting.remove(SAMIdentifier)

	def setBackgroundMonitor(self):
		SAMIdentifier = " ".join([self.encoderType, str(self.IAccessibleChildID)])
		if self.backgroundMonitor and not SAMIdentifier in SPLBackgroundMonitor:
			SPLBackgroundMonitor.add(SAMIdentifier)
		elif not self.backgroundMonitor and SAMIdentifier in SPLBackgroundMonitor:
			SPLBackgroundMonitor.remove(SAMIdentifier)
		return SAMMonitorThreads


	def getStreamLabel(self, getTitle=False):
		if str(self.IAccessibleChildID) in SAMStreamLabels:
			streamLabel = SAMStreamLabels[str(self.IAccessibleChildID)]
			return streamLabel, self.IAccessibleChildID if getTitle else streamLabel
		return None, self.IAccessibleChildID if getTitle else None

	def setStreamLabel(self, newStreamLabel):
		if len(newStreamLabel):
			SAMStreamLabels[str(self.IAccessibleChildID)] = newStreamLabel
		else:
			del SAMStreamLabels[str(self.IAccessibleChildID)]
		streamLabels["SAMEncoders"] = SAMStreamLabels
		streamLabels.write()

	def removeStreamLabel(self, pos):
		# An application of map successor algorithm.
		labelLength = len(SAMStreamLabels)
		if not labelLength or pos > max(SAMStreamLabels.keys()): return
		elif labelLength  == 1:
			if not pos in SAMStreamLabels:
				pos = SPLStreamLabels.keys()[0]
				oldPosition = int(pos)
				SAMStreamLabels[str(oldPosition-1)] = SAMStreamLabels[pos]
			del SAMStreamLabels[pos]
		else:
			encoderPositions = sorted(SAMStreamLabels.keys())
						# What if the position happens to be the last stream label position?
			if pos == max(encoderPositions): del SPLStreamLabels[pos]
			# Find the exact or closest successor.
			else:
				startPosition = 0
				if pos == min(encoderPositions):
					del SAMStreamLabels[pos]
					startPosition = 1
				elif pos > min(encoderPositions):
					for candidate in encoderPositions:
						if candidate >= pos:
							startPositionCandidate = encoderPositions.index(candidate)
							startPosition = startPositionCandidate+1 if candidate == pos else startPositionCandidate
							break
				# Now move them forward.
				for position in encoderPositions[startPosition:]:
					oldPosition = int(position)
					SAMStreamLabels[str(oldPosition-1)] = SAMStreamLabels[position]
					del SAMStreamLabels[position]
		streamLabels["SAMEncoders"] = SAMStreamLabels
		streamLabels.write()


	__gestures={
		"kb:f9":"connect",
		"kb:f10":"disconnect"
	}


class SPLEncoder(Encoder):
	# Support for SPL Encoder window.

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
			if not " ".join([self.encoderType, str(self.IAccessibleChildID)]) in SPLBackgroundMonitor: return

	def script_connect(self, gesture):
		# Same as SAM's connection routine, but this time, keep an eye on self.name and a different connection flag.
		connectButton = api.getForegroundObject().children[2]
		if connectButton.name == "Disconnect": return
		ui.message(_("Connecting..."))
		# Juggle the focus around.
		connectButton.doAction()
		self.setFocus()
		# Same as SAM encoders.
		if not self.backgroundMonitor:
			statusThread = threading.Thread(target=self.reportConnectionStatus, kwargs=dict(connecting=True))
			statusThread.name = "Connection Status Reporter"
			statusThread.start()
			SPLMonitorThreads[self.IAccessibleChildID] = statusThread
	script_connect.__doc__=_("Connects to a streaming server.")

	def _set_FocusToStudio(self):
		SPLIdentifier = " ".join([self.encoderType, str(self.IAccessibleChildID)])
		if self.focusToStudio and not SPLIdentifier in SPLFocusToStudio:
			SPLFocusToStudio.add(SPLIdentifier)
		elif not self.focusToStudio and SPLIdentifier in SPLFocusToStudio:
			SPLFocusToStudio.remove(SPLIdentifier)

	def setPlayAfterConnecting(self):
		SPLIdentifier = " ".join([self.encoderType, str(self.IAccessibleChildID)])
		if self.playAfterConnecting and not SPLIdentifier in SPLPlayAfterConnecting:
			SPLPlayAfterConnecting.add(SPLIdentifier)
		elif not self.playAfterConnecting and SPLIdentifier in SPLPlayAfterConnecting:
			SPLPlayAfterConnecting.remove(SPLIdentifier)

	def setBackgroundMonitor(self):
		SPLIdentifier = " ".join([self.encoderType, str(self.IAccessibleChildID)])
		if self.backgroundMonitor and not SPLIdentifier in SPLBackgroundMonitor:
			SPLBackgroundMonitor.add(SPLIdentifier)
		elif not self.backgroundMonitor and SPLIdentifier in SPLBackgroundMonitor:
			SPLBackgroundMonitor.remove(SPLIdentifier)
		return SPLMonitorThreads

	def getStreamLabel(self, getTitle=False):
		if str(self.IAccessibleChildID) in SPLStreamLabels:
			streamLabel = SPLStreamLabels[str(self.IAccessibleChildID)]
			return streamLabel, self.firstChild.name if getTitle else streamLabel
		return (None, self.firstChild.name) if getTitle else None

	def setStreamLabel(self, newStreamLabel):
		if len(newStreamLabel):
			SPLStreamLabels[str(self.IAccessibleChildID)] = newStreamLabel
		else:
			del SPLStreamLabels[str(self.IAccessibleChildID)]
		streamLabels["SPLEncoders"] = SPLStreamLabels
		streamLabels.write()

	def removeStreamLabel(self, pos):
		labelLength = len(SPLStreamLabels)
		if not labelLength or pos > max(SPLStreamLabels.keys()): return
		elif labelLength  == 1:
			if not pos in SPLStreamLabels:
				pos = SPLStreamLabels.keys()[0]
				oldPosition = int(pos)
				SPLStreamLabels[str(oldPosition-1)] = SPLStreamLabels[pos]
			del SPLStreamLabels[pos]
		else:
			encoderPositions = sorted(SPLStreamLabels.keys())
			if pos == max(encoderPositions): del SPLStreamLabels[pos]
			else:
				# Find the exact or closest successor.
				startPosition = 0
				if pos == min(encoderPositions):
					del SPLStreamLabels[pos]
					startPosition = 1
				elif pos > min(encoderPositions):
					for candidate in encoderPositions:
						if candidate >= pos:
							startPositionCandidate = encoderPositions.index(candidate)
							startPosition = startPositionCandidate+1 if candidate == pos else startPositionCandidate
							break
				# Now move them forward.
				for position in encoderPositions[startPosition:]:
					oldPosition = int(position)
					SPLStreamLabels[str(oldPosition-1)] = SPLStreamLabels[position]
					del SPLStreamLabels[position]
		streamLabels["SPLEncoders"] = SPLStreamLabels
		streamLabels.write()


	__gestures={
		"kb:f9":"connect",
	}


