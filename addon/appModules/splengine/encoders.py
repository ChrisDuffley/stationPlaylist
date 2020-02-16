# StationPlaylist encoders support
# Author: Joseph Lee
# Copyright 2015-2020, released under GPL.
# Split from main global plugin in 2015.

import threading
import time
from abc import abstractmethod
import api
import config
import ui
import speech
import scriptHandler
from NVDAObjects.IAccessible import IAccessible, sysListView32, getNVDAObjectFromEvent
from winUser import user32, sendMessage, OBJID_CLIENT
import tones
import gui
import wx
import addonHandler
addonHandler.initTranslation()

# Various SPL IPC tags.
SPLPlay = 12
SPL_TrackPlaybackStatus = 104

# Needed in Encoder support:
SPLFocusToStudio = set() # Whether to focus to Studio or not.
SPLPlayAfterConnecting = set()
SPLBackgroundMonitor = set()
SPLNoConnectionTone = set()
SPLConnectionStopOnError = set() # Whether connection status message announcements should stop when an error is encountered.

# Customized for each encoder type.
SAMStreamLabels= {} # A dictionary to store custom labels for each stream.
SPLStreamLabels= {} # Same as above but optimized for SPL encoders (Studio 5.00 and later).
ACStreamLabels= {} # Optimized for AltaCast.
SAMMonitorThreads = {}
SPLMonitorThreads = {}
ACMonitorThreads = {}
encoderMonCount = {"SAM":0, "SPL":0, "AltaCast":0}

# Configuration management.
streamLabels = None

# Load stream labels (and possibly other future goodies) from a file-based database.
def loadStreamLabels():
	global streamLabels, SAMStreamLabels, SPLStreamLabels, ACStreamLabels, SPLFocusToStudio, SPLPlayAfterConnecting, SPLBackgroundMonitor, SPLNoConnectionTone, SPLConnectionStopOnError
	import os, configobj, globalVars
	streamLabels = configobj.ConfigObj(os.path.join(globalVars.appArgs.configPath, "splStreamLabels.ini"))
	# Read stream labels.
	try:
		SAMStreamLabels = dict(streamLabels["SAMEncoders"])
	except KeyError:
		SAMStreamLabels = {}
	try:
		SPLStreamLabels = dict(streamLabels["SPLEncoders"])
	except KeyError:
		SPLStreamLabels = {}
	try:
		ACStreamLabels = dict(streamLabels["AltaCastEncoders"])
	except KeyError:
		ACStreamLabels = {}
	# Read other settings.
	if "FocusToStudio" in streamLabels:
		SPLFocusToStudio = set(streamLabels["FocusToStudio"])
	if "PlayAfterConnecting" in streamLabels:
		SPLPlayAfterConnecting = set(streamLabels["PlayAfterConnecting"])
	if "BackgroundMonitor" in streamLabels:
		SPLBackgroundMonitor = set(streamLabels["BackgroundMonitor"])
	if "NoConnectionTone" in streamLabels:
		SPLNoConnectionTone = set(streamLabels["NoConnectionTone"])
	if "ConnectionStopOnError" in streamLabels:
		SPLConnectionStopOnError = set(streamLabels["ConnectionStopOnError"])
	# 20.04: register config save handler.
	config.post_configSave.register(saveStreamLabels)

# Report number of encoders being monitored.
# 6.0: Refactor the below function to use the newer encoder config format.
def getStreamLabel(identifier):
	encoderType, encoderID = identifier.split()
	# 5.2: Use a static map.
	# 6.0: Look up the encoder type.
	if encoderType == "SAM": labels = SAMStreamLabels
	elif encoderType == "SPL": labels = SPLStreamLabels
	elif encoderType == "AltaCast": labels = ACStreamLabels
	if encoderID in labels: return labels[encoderID]
	return None

def announceEncoderConnectionStatus():
	import windowUtils
	# For SAM encoders, descend into encoder window after locating the foreground window.
	# For others, look for a specific SysListView32 control.
	desktopHwnd = api.getDesktopObject().windowHandle
	try:
		samEncoderWindow = windowUtils.findDescendantWindow(desktopHwnd, className="TfoSCEncoders")
	except LookupError:
		samEncoderWindow = 0
	if samEncoderWindow:
		try:
			samEncoderWindow = windowUtils.findDescendantWindow(samEncoderWindow, className="TListView")
		except LookupError:
			samEncoderWindow = 0
	try:
		sysListView32EncoderWindow = windowUtils.findDescendantWindow(desktopHwnd, className="SysListView32", controlID=1004)
	except LookupError:
		sysListView32EncoderWindow = 0
	if not samEncoderWindow and not sysListView32EncoderWindow:
		# Translators: presented when no streaming encoders were found when trying to obtain connection status.
		ui.message(_("No encoders found"))
	elif samEncoderWindow and sysListView32EncoderWindow:
		# Translators: presented when more than one encoder type is active when trying to obtain encoder connection status.
		ui.message(_("Only one encoder type can be active at once"))
	else:
		encoderWindow = max(samEncoderWindow, sysListView32EncoderWindow)
		encoderList = getNVDAObjectFromEvent(encoderWindow, OBJID_CLIENT, 0)
		connectedEncoders = []
		for encoder in encoderList.children:
			if isinstance(encoder, Encoder) and encoder.connected:
				connectedEncoders.append("{0} {1}".format(encoder.encoderType, str(encoder.IAccessibleChildID)))
		if len(connectedEncoders) > 0:
			# Translators: presented when at least one encoder is connected.
			ui.message(_("Connected encoders: {encodersConnected}").format(encodersConnected=", ".join(connectedEncoders)))
		else:
			# Translators: presented when no encoders are connected.
			ui.message(_("No encoders connected"))

# Remove encoder ID from various settings maps.
# This is a private module level function in order for it to be invoked by humans alone.
_encoderConfigRemoved = None
def _removeEncoderID(encoderType, pos):
	global _encoderConfigRemoved
	# For now, store the key to map.
	# This might become a module-level constant if other functions require this dictionary.
	key2map = {"FocusToStudio":SPLFocusToStudio, "PlayAfterConnecting":SPLPlayAfterConnecting, "BackgroundMonitor":SPLBackgroundMonitor, "NoConnectionTone":SPLNoConnectionTone, "ConnectionStopOnError": SPLConnectionStopOnError}
	encoderID = " ".join([encoderType, pos])
	# Go through each feature map, remove the encoder ID and manipulate encoder positions in these sets.
	# For each set, have a list of set items handy, otherwise set cardinality error (RuntimeError) will occur if items are removed on the fly.
	for key in key2map:
		encoderSettings = key2map[key]
		if encoderID in encoderSettings:
			encoderSettings.remove(encoderID)
			_encoderConfigRemoved = True
		# If not sorted, encoders will appear in random order (a downside of using sets, as their ordering is quite unpredictable).
		currentEncoders = sorted([x for x in encoderSettings if x.startswith(encoderType)])
		if len(currentEncoders) and encoderID < currentEncoders[-1]:
			# Same algorithm as stream label remover.
			start = 0
			if encoderID > currentEncoders[0]:
				for candidate in currentEncoders:
					if encoderID < candidate:
						start = currentEncoders.index(candidate)
			# Do set entry manipulations (remove first, then add).
			for item in currentEncoders[start:]:
				encoderSettings.remove(item)
				encoderSettings.add(" ".join([encoderType, "%s"%(int(item.split()[-1])-1)]))
		_encoderConfigRemoved = True
		if len(encoderSettings): streamLabels[key] = list(encoderSettings)
		else:
			try:
				del streamLabels[key]
			except KeyError:
				pass

# Save stream labels and various flags, called when closing app modules and when config save command is pressed.
def saveStreamLabels():
	global streamLabels, SAMStreamLabels, SPLStreamLabels, ACStreamLabels, SPLFocusToStudio, SPLPlayAfterConnecting, SPLBackgroundMonitor, SPLNoConnectionTone, SPLConnectionStopOnError
	# Gather stream labels and flags.
	streamLabels["SAMEncoders"] = dict(SAMStreamLabels)
	streamLabels["SPLEncoders"] = dict(SPLStreamLabels)
	streamLabels["AltaCastEncoders"] = dict(ACStreamLabels)
	# For flags, convert flag sets into lists.
	streamLabels["FocusToStudio"] = list(SPLFocusToStudio)
	streamLabels["PlayAfterConnecting"] = list(SPLPlayAfterConnecting)
	streamLabels["BackgroundMonitor"] = list(SPLBackgroundMonitor)
	streamLabels["NoConnectionTone"] = list(SPLNoConnectionTone)
	streamLabels["ConnectionStopOnError"] = list(SPLConnectionStopOnError)
	# To save disk space, remove empty data.
	for key in streamLabels.keys():
		if not len(streamLabels[key]): 
			del streamLabels[key]
	streamLabels.write()

# Nullify various flag sets, otherwise memory leak occurs.
# 20.04: if told to do so, save encoder settings.
def cleanup(appTerminating=False):
	global streamLabels, SAMStreamLabels, SPLStreamLabels, ACStreamLabels, SPLFocusToStudio, SPLPlayAfterConnecting, SPLBackgroundMonitor, SPLNoConnectionTone, SPLConnectionStopOnError, encoderMonCount, SAMMonitorThreads, SPLMonitorThreads, ACMonitorThreads
	if appTerminating: saveStreamLabels()
	for flag in [streamLabels, SAMStreamLabels, SPLStreamLabels, ACStreamLabels, SPLFocusToStudio, SPLPlayAfterConnecting, SPLBackgroundMonitor, SPLNoConnectionTone, SPLConnectionStopOnError, SAMMonitorThreads, SPLMonitorThreads, ACMonitorThreads]:
		if flag is not None: flag.clear()
	# Nullify stream labels.
	streamLabels = None
	# Without resetting monitor count, we end up with higher and higher value for this.
	# 7.0: Destroy threads also.
	encoderMonCount = {"SAM":0, "SPL":0, "AltaCast":0}

# Encoder configuration dialog.
_configDialogOpened = False

class EncoderConfigDialog(wx.Dialog):

	# The following comes from exit dialog class from GUI package (credit: NV Access and Zahari from Bulgaria).
	_instance = None

	def __new__(cls, parent, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _configDialogOpened:
			raise RuntimeError("An instance of encoder settings dialog is opened")
		inst = cls._instance() if cls._instance else None
		if not inst:
			return super(cls, cls).__new__(cls, parent, *args, **kwargs)
		return inst

	def __init__(self, parent, obj):
		inst = EncoderConfigDialog._instance() if EncoderConfigDialog._instance else None
		if inst:
			return
		# Use a weakref so the instance can die.
		import weakref
		EncoderConfigDialog._instance = weakref.ref(self)

		self.obj = obj
		self.curStreamLabel, title = obj.getStreamLabel(getTitle=True)
		# Translators: The title of the encoder settings dialog (example: Encoder settings for SAM 1").
		super(EncoderConfigDialog, self).__init__(parent, wx.ID_ANY, _("Encoder settings for {name}").format(name = title))
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		encoderConfigHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		# And to close this automatically when Studio dies.
		from appModules.splstudio import splactions
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)
		global _configDialogOpened
		_configDialogOpened = True

		# Translators: An edit field in encoder settings to set stream label for this encoder.
		self.streamLabel = encoderConfigHelper.addLabeledControl(_("Stream &label"), wx.TextCtrl)
		self.streamLabel.SetValue(self.curStreamLabel if self.curStreamLabel is not None else "")

		# Translators: A checkbox in encoder settings to set if NvDA should switch focus to Studio window when connected.
		self.focusToStudio = encoderConfigHelper.addItem(wx.CheckBox(self, label=_("&Focus to Studio when connected")))
		self.focusToStudio.SetValue(obj.encoderId in SPLFocusToStudio)
		# Translators: A checkbox in encoder settings to set if NvDA should play the next track when connected.
		self.playAfterConnecting = encoderConfigHelper.addItem(wx.CheckBox(self, label=_("&Play first track when connected")))
		self.playAfterConnecting.SetValue(obj.encoderId in SPLPlayAfterConnecting)
		# Translators: A checkbox in encoder settings to set if NvDA should monitor the status of this encoder in the background.
		self.backgroundMonitor = encoderConfigHelper.addItem(wx.CheckBox(self, label=_("Enable background connection &monitoring")))
		self.backgroundMonitor.SetValue(obj.encoderId in SPLBackgroundMonitor)
		# Translators: A checkbox in encoder settings to set if NvDA should play connection progress tone.
		self.noConnectionTone = encoderConfigHelper.addItem(wx.CheckBox(self, label=_("Play connection status &beep while connecting")))
		self.noConnectionTone.SetValue(obj.encoderId not in SPLNoConnectionTone)
		# Translators: A checkbox in encoder settings to set if NVDA should announce connection progress until an encoder connects.
		self.connectionStopOnError = encoderConfigHelper.addItem(wx.CheckBox(self, label=_("Announce connection &status until encoder connects")))
		self.connectionStopOnError.SetValue(obj.encoderId not in SPLConnectionStopOnError)

		encoderConfigHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON,self.onOk,id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON,self.onCancel,id=wx.ID_CANCEL)
		mainSizer.Add(encoderConfigHelper.sizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)
		self.streamLabel.SetFocus()

	def onOk(self, evt):
		setFlags = self.obj._setFlags
		encoderId = self.obj.encoderId
		setFlags(encoderId, self.focusToStudio.Value, SPLFocusToStudio, "FocusToStudio", save=False)
		setFlags(encoderId, self.playAfterConnecting.Value, SPLPlayAfterConnecting, "PlayAfterConnecting", save=False)
		setFlags(encoderId, self.backgroundMonitor.Value, SPLBackgroundMonitor, "BackgroundMonitor", save=False)
		# Invert the following two flags.
		setFlags(encoderId, not self.noConnectionTone.Value, SPLNoConnectionTone, "NoConnectionTone", save=False)
		setFlags(encoderId, not self.connectionStopOnError.Value, SPLConnectionStopOnError, "ConnectionStopOnError", save=False)
		newStreamLabel = self.streamLabel.Value
		if newStreamLabel is None: newStreamLabel = ""
		self.obj.setStreamLabel(newStreamLabel)
		self.Destroy()
		global _configDialogOpened
		_configDialogOpened = False

	def onCancel(self, evt):
		self.Destroy()
		global _configDialogOpened
		_configDialogOpened = False

	def onAppTerminate(self):
		self.onCancel(None)


class Encoder(IAccessible):
	"""Represents an encoder from within StationPlaylist Studio or Streamer.
	This abstract base encoder provides scripts for all encoders such as stream labeler and toggling focusing to Studio when connected.
	Subclasses must provide scripts to handle encoder connection and connection announcement routines.
	In addition, they must implement the required actions to set options such as focusing to Studio, storing stream labels and so on, as each subclass relies on a feature map.
	For example, for SAM encoder class, the feature map is SAM* where * denotes the feature in question.
	Lastly, each encoder class must provide a unique identifying string to identify the type of the encoder (e.g. SAM for SAM encoder).
	"""

	# Some helper functions
	# 17.08: most are properties.

	# Get the encoder identifier.
	# This consists of two or three letter abbreviations for the encoder and the child ID.
	@property
	def encoderId(self):
		return " ".join([self.encoderType, str(self.IAccessibleChildID)])

	@property
	def focusToStudio(self):
		try:
			return self.encoderId in SPLFocusToStudio
		except KeyError:
			return False

	@property
	def playAfterConnecting(self):
		try:
			return self.encoderId in SPLPlayAfterConnecting
		except KeyError:
			return False

	@property
	def backgroundMonitor(self):
		try:
			return self.encoderId in SPLBackgroundMonitor
		except KeyError:
			return False

	@property
	def connectionTone(self):
		try:
			return self.encoderId not in SPLNoConnectionTone
		except KeyError:
			return True

	@property
	def announceStatusUntilConnected(self):
		try:
			return self.encoderId not in SPLConnectionStopOnError
		except KeyError:
			return True

	# Format the status message to prepare for monitoring multiple encoders.
	def encoderStatusMessage(self, message, encoderId):
		# #79 (18.10.1/18.09.3-lts): wxPython 4 is more strict about where timers can be invoked from, and the below function is called from a thread other than the main one, which causes an exception to be logged.
		# This is especially the case with some speech synthesizers and/or braille displays.
		try:
			if encoderMonCount[self.encoderType] > 1:
				# Translators: Status message for encoder monitoring.
				ui.message(_("{encoder} {encoderNumber}: {status}").format(encoder = self.encoderType, encoderNumber = encoderId, status = message))
			else:
				ui.message(message)
		except:
			pass

	# Encoder connection reporter thread.
	# By default background encoding (no manual connect) is assumed.
	def connectStart(self, manualConnect=False):
		statusThread = threading.Thread(target=self.reportConnectionStatus, kwargs=dict(manualConnect=manualConnect))
		statusThread.start()
		self.threadPool[self.IAccessibleChildID] = statusThread

	# #103: the abstract method that is responsible for announcing connection status.
	@abstractmethod
	def reportConnectionStatus(self, manualConnect=False):
		raise NotImplementedError

	# A master flag setter.
	# Set or clear a given flag for the encoder given its ID, flag and flag container (currently a feature set).
	# Also take in the flag key for storing it into the settings file.
	# The flag will then be written to the configuration file.
	# 7.0: Don't dump flags to disk unless told.
	def _setFlags(self, encoderId, flag, flagMap, flagKey, save=True):
		if flag and not encoderId in flagMap:
			flagMap.add(encoderId)
		elif not flag and encoderId in flagMap:
			flagMap.remove(encoderId)
		# No need to store an empty flag map.
		if len(flagMap): streamLabels[flagKey] = list(flagMap)
		else:
			try:
				del streamLabels[flagKey]
			except KeyError:
				pass
		if save: streamLabels.write()

	# Now the flag configuration scripts.

	@scriptHandler.script(
		# Translators: Input help mode message in SAM Encoder window.
		description=_("Toggles whether NVDA will switch to Studio when connected to a streaming server."),
		gesture="kb:f11"
	)
	def script_toggleFocusToStudio(self, gesture):
		if not self.focusToStudio:
			# Translators: Presented when toggling the setting to switch to Studio when connected to a streaming server.
			ui.message(_("Switch to Studio after connecting"))
		else:
			# Translators: Presented when toggling the setting to switch to Studio when connected to a streaming server.
			ui.message(_("Do not switch to Studio after connecting"))
		self._setFlags(self.encoderId, not self.focusToStudio, SPLFocusToStudio, "FocusToStudio")

	@scriptHandler.script(
		# Translators: Input help mode message in SAM Encoder window.
		description=_("Toggles whether Studio will play the first song when connected to a streaming server."),
		gesture="kb:shift+f11"
	)
	def script_togglePlay(self, gesture):
		if not self.playAfterConnecting:
			# Translators: Presented when toggling the setting to play selected song when connected to a streaming server.
			ui.message(_("Play first track after connecting"))
		else:
			# Translators: Presented when toggling the setting to switch to Studio when connected to a streaming server.
			ui.message(_("Do not play first track after connecting"))
		self._setFlags(self.encoderId, not self.playAfterConnecting, SPLPlayAfterConnecting, "PlayAfterConnecting")

	@scriptHandler.script(
		# Translators: Input help mode message in SAM Encoder window.
		description=_("Toggles whether NVDA will monitor the selected encoder in the background."),
		gesture="kb:control+f11"
	)
	def script_toggleBackgroundEncoderMonitor(self, gesture):
		if scriptHandler.getLastScriptRepeatCount()==0:
			if not self.backgroundMonitor:
				encoderMonCount[self.encoderType] += 1 # Multiple encoders.
				# Translators: Presented when toggling the setting to monitor the selected encoder.
				ui.message(_("Monitoring encoder {encoderNumber}").format(encoderNumber = self.IAccessibleChildID))
			else:
				encoderMonCount[self.encoderType] -= 1
				# Translators: Presented when toggling the setting to monitor the selected encoder.
				ui.message(_("Encoder {encoderNumber} will not be monitored").format(encoderNumber = self.IAccessibleChildID))
			self._setFlags(self.encoderId, not self.backgroundMonitor, SPLBackgroundMonitor, "BackgroundMonitor")
			if self.backgroundMonitor:
				try:
					monitoring = self.threadPool[self.IAccessibleChildID].is_alive()
				except KeyError:
					monitoring = False
				if not monitoring: self.connectStart()
		else:
			for encoderType in encoderMonCount:
				encoderMonCount[encoderType] = 0
			SPLBackgroundMonitor.clear()
			# Translators: Announced when background encoder monitoring is canceled.
			ui.message(_("Encoder monitoring canceled"))

	@scriptHandler.script(
		# Translators: Input help mode message in SAM Encoder window.
		description=_("Opens a dialog to label the selected encoder."),
		gesture="kb:f12"
	)
	def script_streamLabeler(self, gesture):
		curStreamLabel, title = self.getStreamLabel(getTitle=True)
		if not curStreamLabel: curStreamLabel = ""
		# Translators: The title of the stream labeler dialog (example: stream labeler for 1).
		streamTitle = _("Stream labeler for {streamEntry}").format(streamEntry = title)
		# Translators: The text of the stream labeler dialog.
		streamText = _("Enter the label for this stream")
		dlg = wx.TextEntryDialog(gui.mainFrame,
		streamText, streamTitle, value=curStreamLabel)
		def callback(result):
			if result == wx.ID_OK:
				newStreamLabel = dlg.GetValue()
				if newStreamLabel == curStreamLabel:
					return # No need to write to disk.
				else: self.setStreamLabel(newStreamLabel)
		gui.runScriptModalDialog(dlg, callback)

	def removeStreamConfig(self, pos):
		# An application of map successor algorithm.
		global _encoderConfigRemoved
		_removeEncoderID(self.encoderType, pos)
		streamLabelsMap = self.streamLabelsMap
		labelLength = len(streamLabelsMap)
		if not labelLength or pos > max(streamLabelsMap.keys()):
			if _encoderConfigRemoved is not None:
				streamLabels.write()
				_encoderConfigRemoved = None
			return
		elif labelLength  == 1:
			if not pos in streamLabelsMap:
				pos = list(streamLabelsMap.keys())[0]
				oldPosition = int(pos)
				streamLabelsMap[str(oldPosition-1)] = streamLabelsMap[pos]
			del streamLabelsMap[pos]
		else:
			encoderPositions = sorted(streamLabelsMap.keys())
			# What if the position happens to be the last stream label position?
			if pos == max(encoderPositions): del streamLabelsMap[pos]
			else:
				# Find the exact or closest successor.
				startPosition = 0
				if pos == min(encoderPositions):
					del streamLabelsMap[pos]
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
					streamLabelsMap[str(oldPosition-1)] = streamLabelsMap[position]
					del streamLabelsMap[position]
		streamLabels[self.encoderType + "Encoders"] = streamLabelsMap
		streamLabels.write()

	@scriptHandler.script(
		# Translators: Input help mode message in SAM Encoder window.
		description=_("Opens a dialog to erase stream labels and settings from an encoder that was deleted."),
		gesture="kb:control+f12"
	)
	def script_streamLabelEraser(self, gesture):
		choices = [str(pos) for pos in range(1, self.simpleParent.childCount)]
		# Translators: The title of the stream configuration eraser dialog.
		streamEraserTitle = _("Stream label and settings eraser")
		# Translators: The text of the stream configuration eraser dialog.
		streamEraserText = _("Enter the position of the encoder you wish to delete or will delete")
		# 17.12: early versions of wxPython 4 does not have number entry dialog, so replace it with a combo box.
		dlg = wx.SingleChoiceDialog(gui.mainFrame,
		streamEraserText, streamEraserTitle, choices=choices)
		dlg.SetSelection(self.IAccessibleChildID-1)
		def callback(result):
			if result == wx.ID_OK:
				self.removeStreamConfig(dlg.GetStringSelection())
		gui.runScriptModalDialog(dlg, callback)

	# stream settings.
	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Shows encoder configuration dialog to configure various encoder settings such as stream label."),
		gesture="kb:alt+NVDA+0",
		category=_("StationPlaylist")
	)
	def script_encoderSettings(self, gesture):
		try:
			d = EncoderConfigDialog(gui.mainFrame, self)
			gui.mainFrame.prePopup()
			d.Raise()
			d.Show()
			gui.mainFrame.postPopup()
		except RuntimeError:
			from ..skipTranslation import translate
			# Translators: Text of the dialog when another alarm dialog is open.
			wx.CallAfter(gui.messageBox, _("Another encoder settings dialog is open."),translate("Error"),style=wx.OK | wx.ICON_ERROR)

	# Announce complete time including seconds (slight change from global commands version).
	@scriptHandler.script(
		# Translators: Input help mode message for report date and time command.
		description=_("If pressed once, reports the current time including seconds. If pressed twice, reports the current date"),
		gesture="kb:NVDA+F12",
		category=_("StationPlaylist")
	)
	def script_encoderDateTime(self, gesture):
		import winKernel
		if scriptHandler.getLastScriptRepeatCount()==0:
			text=winKernel.GetTimeFormat(winKernel.LOCALE_USER_DEFAULT, 0, None, None)
		else:
			text=winKernel.GetDateFormat(winKernel.LOCALE_USER_DEFAULT, winKernel.DATE_LONGDATE, None, None)
		ui.message(text)

	# Various column announcement scripts.
	# This base class implements encoder position and stream labels.
	@scriptHandler.script(gesture="kb:control+NVDA+1")
	def script_announceEncoderPosition(self, gesture):
		ui.message(_("Position: {pos}").format(pos = self.IAccessibleChildID))

	@scriptHandler.script(gesture="kb:control+NVDA+2")
	def script_announceEncoderLabel(self, gesture):
		try:
			streamLabel = self.getStreamLabel()[0]
		except TypeError:
			streamLabel = None
		if streamLabel:
			ui.message(_("Label: {label}").format(label = streamLabel))
		else:
			ui.message(_("No stream label"))

	def initOverlayClass(self):
		global encoderMonCount
		# Load stream labels upon request.
		if streamLabels is None: loadStreamLabels()
		# 6.2: Make sure background monitor threads are started if the flag is set.
		if self.backgroundMonitor:
			threadPool = self.threadPool
			if self.IAccessibleChildID in threadPool:
				if not threadPool[self.IAccessibleChildID].is_alive():
					del threadPool[self.IAccessibleChildID]
				# If it is indeed alive... Otherwise another thread will be created to keep an eye on this encoder (undesirable).
				else: return
			self.connectStart()
			encoderMonCount[self.encoderType] += 1

	def reportFocus(self):
		try:
			streamLabel = self.getStreamLabel()[0]
		except TypeError:
			streamLabel = None
		# Announce stream label if it exists.
		if streamLabel is not None:
			try:
				self.name = "(" + streamLabel + ") " + self.name
			except TypeError:
				pass
		super(Encoder, self).reportFocus()

class SAMEncoder(Encoder, sysListView32.ListItem):
	# Support for Sam Encoders.

	encoderType = "SAM"

	def _get_name(self):
		return self.IAccessibleObject.accName(self.IAccessibleChildID)

	def _get_description(self):
		# #87 (18.09.6-LTS only): SysListView32.ListItem nullifies description, so resort to fetching it via IAccessible.
		return self.IAccessibleObject.accDescription(self.IAccessibleChildID)

	def _moveToRow(self, row):
		# In addition to moving to the next or previous encoder entry, set focus on the new encoder entry once more.
		super(SAMEncoder, self)._moveToRow(row)
		if row is not None: row.setFocus()

	@property
	def connected(self):
		return self._getColumnContentRaw(2) == "Encoding"

	def reportConnectionStatus(self, manualConnect=False):
		# A fake child object holds crucial information about connection status.
		# In order to not block NVDA commands, this will be done using a different thread.
		SPLWin = user32.FindWindowW("SPLStudio", None)
		# #123 (20.03): conection attempt counting is deprecated, replaced by time intervals.
		connectionAttempt = 0
		attemptTime = time.time()
		messageCache = ""
		# Status message flags.
		idle = False
		error = False
		connecting = False
		encoding = False
		alreadyEncoding = False
		while True:
			time.sleep(0.001)
			try:
				status = self._getColumnContentRaw(2)
				statusDetails = self._getColumnContentRaw(3)
			except:
				return # Don't leave zombie objects around.
			# Encoding status object will die if encoder entry is deleted while being monitored.
			if not status: return
			# Status and description are two separate texts.
			if not messageCache.startswith(status):
				messageCache = "; ".join([status, statusDetails])
				if not messageCache: return
				if not messageCache.startswith("Encoding"):
					self.encoderStatusMessage(messageCache, self.IAccessibleChildID)
			if messageCache.startswith("Idle"):
				if alreadyEncoding: alreadyEncoding = False
				if encoding: encoding = False
				if not idle:
					tones.beep(250, 250)
					idle = True
					connectionAttempt = 0
				if manualConnect and (error or connecting): manualConnect = False
			elif messageCache.startswith("Error"):
				# Announce the description of the error.
				if manualConnect and not self.announceStatusUntilConnected: manualConnect = False
				if not error:
					error = True
					connectionAttempt = 0
				if alreadyEncoding: alreadyEncoding = False
				if connecting: connecting = False
			elif messageCache.startswith("Encoding"):
				if manualConnect: manualConnect = False
				if connecting: connecting = False
				# We're on air, so exit unless told to monitor for connection changes.
				if not encoding:
					tones.beep(1000, 150)
					self.encoderStatusMessage(messageCache, self.IAccessibleChildID)
				if self.focusToStudio and not encoding:
					if api.getFocusObject().appModule == "splstudio":
						continue
					user32.SetForegroundWindow(user32.FindWindowW("TStudioForm", None))
				# #37 (17.08.1): if run from another function, the message will not be sent, so must be done here.
				if self.playAfterConnecting and not encoding:
					# Do not interupt the currently playing track.
					if sendMessage(SPLWin, 1024, 0, SPL_TrackPlaybackStatus) == 0:
						sendMessage(SPLWin, 1024, 0, SPLPlay)
				if not encoding: encoding = True
			else:
				if not connecting: connecting = True
				if alreadyEncoding: alreadyEncoding = False
				if encoding: encoding = False
				elif "Error" not in messageCache and error: error = False
				connectionAttempt+=1
				currentTime = time.time()
				if currentTime-attemptTime >= 0.5 and self.connectionTone:
					tones.beep(500, 50)
					attemptTime = currentTime
			if manualConnect: continue
			if not self.backgroundMonitor: return

	@scriptHandler.script(gesture="kb:f9")
	def script_connect(self, gesture):
		gesture.send()
		# Translators: Presented when an Encoder is trying to connect to a streaming server.
		ui.message(_("Connecting..."))
		# Oi, status thread, can you keep an eye on the connection status for me?
		# To be packaged into a new function in 7.0.
		if not self.backgroundMonitor: self.connectStart(manualConnect=True)

	@scriptHandler.script(gesture="kb:f10")
	def script_disconnect(self, gesture):
		gesture.send()
		# Translators: Presented when an Encoder is disconnecting from a streaming server.
		ui.message(_("Disconnecting..."))

	# Connecting/disconnecting all encoders at once.
	# Control+F9/Control+F10 hotkeys are broken. Thankfully, context menu retains these commands.
	# Use object navigation and key press emulation hack.

	def _samContextMenu(self, pos):
		def _samContextMenuActivate(pos):
			speech.cancelSpeech()
			focus =api.getFocusObject()
			focus.getChild(pos).doAction()
		import keyboardHandler
		contextMenu = keyboardHandler.KeyboardInputGesture.fromName("applications")
		contextMenu.send()
		wx.CallLater(100, _samContextMenuActivate, pos)
		time.sleep(0.2)

	@scriptHandler.script(gesture="kb:control+f9")
	def script_connectAll(self, gesture):
		ui.message(_("Connecting..."))
		speechMode = speech.speechMode
		speech.speechMode = 0
		wx.CallAfter(self._samContextMenu, 7)
		# Oi, status thread, can you keep an eye on the connection status for me?
		if not self.backgroundMonitor: self.connectStart(manualConnect=True)
		speech.speechMode = speechMode

	@scriptHandler.script(gesture="kb:control+f10")
	def script_disconnectAll(self, gesture):
		ui.message(_("Disconnecting..."))
		speechMode = speech.speechMode
		speech.speechMode = 0
		wx.CallAfter(self._samContextMenu, 8)
		time.sleep(0.5)
		speech.speechMode = speechMode
		speech.cancelSpeech()

	# Announce SAM columns: encoder name/type, status and description.
	@scriptHandler.script(gesture="kb:control+NVDA+3")
	def script_announceEncoderFormat(self, gesture):
		ui.message(_("Format: {encoderFormat}").format(encoderFormat = self.getChild(1).name))

	@scriptHandler.script(gesture="kb:control+NVDA+4")
	def script_announceEncoderStatus(self, gesture):
		ui.message(_("Status: {encoderStatus}").format(encoderStatus = self.getChild(2).name))

	@scriptHandler.script(gesture="kb:control+NVDA+5")
	def script_announceEncoderStatusDesc(self, gesture):
		ui.message(_("Description: {encoderDescription}").format(encoderDescription = self.getChild(3).name))

	@property
	def threadPool(self):
		return SAMMonitorThreads

	@property
	def streamLabelsMap(self):
		return SAMStreamLabels

	def getStreamLabel(self, getTitle=False):
		if str(self.IAccessibleChildID) in SAMStreamLabels:
			streamLabel = SAMStreamLabels[str(self.IAccessibleChildID)]
			return streamLabel, self.IAccessibleChildID if getTitle else streamLabel
		return None, self.IAccessibleChildID if getTitle else None

	def setStreamLabel(self, newStreamLabel):
		if len(newStreamLabel):
			SAMStreamLabels[str(self.IAccessibleChildID)] = newStreamLabel
		else:
			try:
				del SAMStreamLabels[str(self.IAccessibleChildID)]
			except KeyError:
				pass
		streamLabels["SAMEncoders"] = SAMStreamLabels
		streamLabels.write()

class SPLEncoder(Encoder):
	# Support for SPL Encoder window.

	encoderType = "SPL"

	@property
	def connected(self):
		status = self._getColumnContentRaw(1)
		return "Kbps" in status or "Connected" in status

	def reportConnectionStatus(self, manualConnect=False):
		# Same routine as SAM encoder: use a thread to prevent blocking NVDA commands.
		SPLWin = user32.FindWindowW("SPLStudio", None)
		# #123 (20.03): same deprecation as SAM encoder.
		connectionAttempt = 0
		attemptTime = time.time()
		messageCache = ""
		# Status flags.
		connecting = False
		connected = False
		while True:
			time.sleep(0.001)
			try:
				status = self._getColumnContentRaw(1)
			except:
				return # Don't leave zombie objects around.
			if messageCache != status:
				messageCache = status
				if not messageCache: return
				if "Kbps" not in messageCache:
					self.encoderStatusMessage(messageCache, self.IAccessibleChildID)
			if messageCache == "Disconnected":
				connected = False
				if manualConnect and connecting: manualConnect = False
			elif "Unable to connect" in messageCache or "Failed" in messageCache or status == "AutoConnect stopped.":
				if manualConnect and not self.announceStatusUntilConnected: manualConnect = False
				if connected: connected = False
			elif "Kbps" in messageCache or "Connected" in messageCache:
				connecting = False
				manualConnect = False
				# We're on air, so exit.
				if not connected: tones.beep(1000, 150)
				if self.focusToStudio and not connected:
					user32.SetForegroundWindow(user32.FindWindowW("TStudioForm", None))
				if self.playAfterConnecting and not connected:
					if sendMessage(SPLWin, 1024, 0, SPL_TrackPlaybackStatus) == 0:
						sendMessage(SPLWin, 1024, 0, SPLPlay)
				if not connected: connected = True
			else:
				if connected: connected = False
				if not connecting: connecting = True
				if not "Kbps" in messageCache:
					connectionAttempt += 1
					currentTime = time.time()
					if currentTime-attemptTime >= 0.5 and self.connectionTone:
						tones.beep(500, 50)
						attemptTime = currentTime
			if manualConnect: continue
			if not self.backgroundMonitor: return

	@scriptHandler.script(
		# Translators: input hep command for an encoder connection command.
		description=_("Connects to a streaming server."),
		gesture="kb:f9"
	)
	def script_connect(self, gesture):
		# Same as SAM's connection routine, but this time, keep an eye on self.name and a different connection flag.
		connectButton = api.getForegroundObject().getChild(2)
		if connectButton.name == "Disconnect": return
		ui.message(_("Connecting..."))
		# Juggle the focus around.
		connectButton.doAction()
		self.setFocus()
		# Same as SAM encoders.
		if not self.backgroundMonitor: self.connectStart(manualConnect=True)

	# Announce SPL Encoder columns: encoder settings and transfer rate.
	@scriptHandler.script(gesture="kb:control+NVDA+3")
	def script_announceEncoderSettings(self, gesture):
		ui.message(_("Encoder Settings: {setting}").format(setting = self.getChild(0).name))

	@scriptHandler.script(gesture="kb:control+NVDA+4")
	def script_announceEncoderTransfer(self, gesture):
		ui.message(_("Transfer Rate: {transferRate}").format(transferRate = self.getChild(1).name))

	@property
	def threadPool(self):
		return SPLMonitorThreads

	@property
	def streamLabelsMap(self):
		return SPLStreamLabels

	def getStreamLabel(self, getTitle=False):
		if str(self.IAccessibleChildID) in SPLStreamLabels:
			streamLabel = SPLStreamLabels[str(self.IAccessibleChildID)]
			return streamLabel, self.firstChild.name if getTitle else streamLabel
		return (None, self.firstChild.name) if getTitle else None

	def setStreamLabel(self, newStreamLabel):
		if len(newStreamLabel):
			SPLStreamLabels[str(self.IAccessibleChildID)] = newStreamLabel
		else:
			try:
				del SPLStreamLabels[str(self.IAccessibleChildID)]
			except KeyError:
				pass
		streamLabels["SPLEncoders"] = SPLStreamLabels
		streamLabels.write()

class AltaCastEncoder(SPLEncoder):
	# Support for AltaCast Encoder window.
	# Deriving from Edcast (now unsupported), user interface resembles SPL Encoder.

	encoderType = "AltaCast"

	@property
	def threadPool(self):
		return ACMonitorThreads

	@property
	def streamLabelsMap(self):
		return ACStreamLabels

	def getStreamLabel(self, getTitle=False):
		if str(self.IAccessibleChildID) in ACStreamLabels:
			streamLabel = ACStreamLabels[str(self.IAccessibleChildID)]
			return streamLabel, self.firstChild.name if getTitle else streamLabel
		return (None, self.firstChild.name) if getTitle else None

	def setStreamLabel(self, newStreamLabel):
		if len(newStreamLabel):
			ACStreamLabels[str(self.IAccessibleChildID)] = newStreamLabel
		else:
			try:
				del ACStreamLabels[str(self.IAccessibleChildID)]
			except KeyError:
				pass
		streamLabels["AltaCastEncoders"] = ACStreamLabels
		streamLabels.write()
