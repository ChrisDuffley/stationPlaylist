# StationPlaylist encoders support
# Author: Joseph Lee
# Copyright 2015-2020, released under GPL.
# Split from main global plugin in 2015.

import threading
import time
import os
from abc import abstractmethod
import api
import config
import configobj
import globalVars
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
# Move focus to Studio once connected.
SPLFocusToStudio = set()
# Play the first selected track after an encoder is connected.
SPLPlayAfterConnecting = set()
# Use a thread to monitor status changes for encoders.
SPLBackgroundMonitor = set()
# A collection of encoder status monitor threads.
SPLBackgroundMonitorThreads = {}
# Do not play connection tone while an encoder is connecting.
SPLNoConnectionTone = set()
# Stop announcing connection status messages when an error is encountered.
SPLConnectionStopOnError = set()

# Stream labels dictionary, customized for each encoder type.
SAMStreamLabels = {}
SPLStreamLabels = {}
ACStreamLabels = {}
SPLEncoderLabels = {}

# Configuration management.
streamLabels = None


# Load stream labels (and possibly other future goodies) from a file-based database.
def loadStreamLabels():
	global streamLabels, SAMStreamLabels, SPLStreamLabels, ACStreamLabels, SPLFocusToStudio, SPLPlayAfterConnecting, SPLBackgroundMonitor, SPLNoConnectionTone, SPLConnectionStopOnError, SPLEncoderLabels
	# 7.1: Make sure encoder settings map isn't corrupted.
	# #131 (20.06): transplanted from Studio app module so the error message can be shown when an encoder gains focus.
	try:
		streamLabels = configobj.ConfigObj(os.path.join(globalVars.appArgs.configPath, "splencoders.ini"))
	except:
		# To avoid type errors, create an empty dictionary.
		streamLabels = {}
		open(os.path.join(globalVars.appArgs.configPath, "splencoders.ini"), "w").close()
		wx.CallAfter(
			# Translators: Message displayed if errors were found in encoder configuration file.
			gui.messageBox, _("Your encoder settings had errors and were reset to defaults."),
			# Translators: Title of the encoder settings error dialog.
			_("SPL add-on Encoder settings error"), wx.OK | wx.ICON_ERROR)
		return
	# Read encoder labels.
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
	# #137: prepare a unified view of encoder labels.
	try:
		SPLEncoderLabels = dict(streamLabels["EncoderLabels"])
	except KeyError:
		SPLEncoderLabels = {}
	if len(SAMStreamLabels):
		for pos in SAMStreamLabels:
			SPLEncoderLabels[f"SAM {pos}"] = SAMStreamLabels[pos]
	if len(SPLStreamLabels):
		for pos in SPLStreamLabels:
			SPLEncoderLabels[f"SPL {pos}"] = SPLStreamLabels[pos]
	if len(ACStreamLabels):
		for pos in ACStreamLabels:
			SPLEncoderLabels[f"AltaCast {pos}"] = ACStreamLabels[pos]
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
	# 20.04: register config save and reset handlers.
	config.post_configSave.register(saveStreamLabels)
	config.post_configReset.register(resetStreamLabels)


# Remove encoder ID from various settings maps and sets.
# This is a private module level function in order for it to be invoked by humans alone.
def _removeEncoderID(encoderType, pos):
	encoderID = " ".join([encoderType, pos])
	# Go through each feature map/set, remove the encoder ID and manipulate encoder positions.
	for encoderSettings in (SPLFocusToStudio, SPLPlayAfterConnecting, SPLBackgroundMonitor, SPLNoConnectionTone, SPLConnectionStopOnError, SPLEncoderLabels):
		if encoderID in encoderSettings:
			# Other than encoder labels (a dictionary), others are sets.
			if isinstance(encoderSettings, set): encoderSettings.remove(encoderID)
			else: del encoderSettings[encoderID]
		# In flag sets, unless members are sorted, encoders will appear in random order (a downside of using sets, as their ordering is quite unpredictable).
		# The below list comprehension also works for dictionaries as it will iterate over keys.
		currentEncoders = sorted([x for x in encoderSettings if x.startswith(encoderType)])
		if len(currentEncoders) and encoderID < currentEncoders[-1]:
			# Locate position of the just removed encoder and move entries forward.
			start = 0
			if encoderID > currentEncoders[0]:
				for candidate in currentEncoders:
					if encoderID < candidate:
						start = currentEncoders.index(candidate)
			# Do set/dictionary entry manipulations (remove first, then add).
			for item in currentEncoders[start:]:
				if isinstance(encoderSettings, set):
					encoderSettings.remove(item)
					encoderSettings.add("{} {}".format(encoderType, int(item.split()[-1])-1))
				else:
					encoderSettings["{} {}".format(encoderType, int(item.split()[-1])-1)] = encoderSettings.pop(item)


# Save stream labels and various flags, called when closing app modules and when config save command is pressed.
def saveStreamLabels():
	global streamLabels, SAMStreamLabels, SPLStreamLabels, ACStreamLabels, SPLFocusToStudio, SPLPlayAfterConnecting, SPLBackgroundMonitor, SPLNoConnectionTone, SPLConnectionStopOnError, SPLEncoderLabels
	# Gather stream labels and flags.
	# 20.07: for consistency, old stream label maps must be cleared first.
	SAMStreamLabels.clear()
	for pos in [encoderId.split(" ")[1] for encoderId in SPLEncoderLabels if encoderId.startswith("SAM")]:
		SAMStreamLabels[pos] = SPLEncoderLabels[f"SAM {pos}"]
	streamLabels["SAMEncoders"] = dict(SAMStreamLabels)
	SPLStreamLabels.clear()
	for pos in [encoderId.split(" ")[1] for encoderId in SPLEncoderLabels if encoderId.startswith("SPL")]:
		SPLStreamLabels[pos] = SPLEncoderLabels[f"SPL {pos}"]
	streamLabels["SPLEncoders"] = dict(SPLStreamLabels)
	ACStreamLabels.clear()
	for pos in [encoderId.split(" ")[1] for encoderId in SPLEncoderLabels if encoderId.startswith("AltaCast")]:
		ACStreamLabels[pos] = SPLEncoderLabels[f"AltaCast {pos}"]
	streamLabels["AltaCastEncoders"] = dict(ACStreamLabels)
	streamLabels["EncoderLabels"] = dict(SPLEncoderLabels)
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
# 20.04: if told to do so, save encoder settings and unregister config save handler.
# In case this is called as part of a reset, unregister config save handler unconditionally.
def cleanup(appTerminating=False, reset=False):
	global streamLabels, SAMStreamLabels, SPLStreamLabels, ACStreamLabels, SPLFocusToStudio, SPLPlayAfterConnecting, SPLBackgroundMonitor, SPLBackgroundMonitorThreads, SPLNoConnectionTone, SPLConnectionStopOnError, SPLEncoderLabels
	# #132 (20.05): do not proceed if encoder settings database is None (no encoders were initialized).
	if streamLabels is None: return
	if appTerminating: saveStreamLabels()
	if reset or appTerminating:
		config.post_configSave.unregister(saveStreamLabels)
		config.post_configReset.unregister(resetStreamLabels)
	for flag in [streamLabels, SAMStreamLabels, SPLStreamLabels, ACStreamLabels, SPLFocusToStudio, SPLPlayAfterConnecting, SPLBackgroundMonitor, SPLBackgroundMonitorThreads, SPLNoConnectionTone, SPLConnectionStopOnError, SPLEncoderLabels]:
		if flag is not None: flag.clear()
	# 20.04: save a "clean" copy after resetting encoder settings.
	if reset: streamLabels.write()
	# Nullify encoder settings.
	streamLabels = None


# Reset encoder settings.
# Because simply reloading settings will introduce errors, respond only to proper reset signal (Control+NVDA+R three times).
def resetStreamLabels(factoryDefaults=False):
	if factoryDefaults: cleanup(reset=True)


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

		# Encoder format text is used as part of the dialog title.
		self.obj = obj
		self.curEncoderLabel = obj.getStreamLabel()
		# Translators: The title of the encoder settings dialog (example: Encoder settings for SAM 1").
		super(EncoderConfigDialog, self).__init__(parent, wx.ID_ANY, _("Encoder settings for {name}").format(name=obj.encoderFormat))
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		encoderConfigHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		# And to close this automatically when Studio dies.
		from appModules.splstudio import splactions
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)
		global _configDialogOpened
		_configDialogOpened = True

		# Translators: An edit field in encoder settings to set a label for this encoder.
		self.encoderLabel = encoderConfigHelper.addLabeledControl(_("Encoder &label"), wx.TextCtrl)
		self.encoderLabel.SetValue(self.curEncoderLabel if self.curEncoderLabel is not None else "")

		# Translators: A checkbox in encoder settings to set if NvDA should switch focus to Studio window when connected.
		self.focusToStudio = encoderConfigHelper.addItem(wx.CheckBox(self, label=_("&Focus to Studio when connected")))
		self.focusToStudio.SetValue(obj.focusToStudio)
		# Translators: A checkbox in encoder settings to set if NvDA should play the next track when connected.
		self.playAfterConnecting = encoderConfigHelper.addItem(wx.CheckBox(self, label=_("&Play first track when connected")))
		self.playAfterConnecting.SetValue(obj.playAfterConnecting)
		# Translators: A checkbox in encoder settings to set if NvDA should monitor the status of this encoder in the background.
		self.backgroundMonitor = encoderConfigHelper.addItem(wx.CheckBox(self, label=_("Enable background connection &monitoring")))
		self.backgroundMonitor.SetValue(obj.backgroundMonitor)
		# Translators: A checkbox in encoder settings to set if NvDA should play connection progress tone.
		self.connectionTone = encoderConfigHelper.addItem(wx.CheckBox(self, label=_("Play connection status &beep while connecting")))
		self.connectionTone.SetValue(obj.connectionTone)
		# Translators: A checkbox in encoder settings to set if NVDA should announce connection progress until an encoder connects.
		self.announceStatusUntilConnected = encoderConfigHelper.addItem(wx.CheckBox(self, label=_("Announce connection &status until encoder connects")))
		self.announceStatusUntilConnected.SetValue(obj.announceStatusUntilConnected)

		encoderConfigHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(encoderConfigHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)
		self.encoderLabel.SetFocus()

	def onOk(self, evt):
		setFlags = self.obj._setFlags
		encoderId = self.obj.encoderId
		setFlags(encoderId, self.focusToStudio.Value, SPLFocusToStudio)
		setFlags(encoderId, self.playAfterConnecting.Value, SPLPlayAfterConnecting)
		setFlags(encoderId, self.backgroundMonitor.Value, SPLBackgroundMonitor)
		# Invert the following two flags.
		setFlags(encoderId, not self.connectionTone.Value, SPLNoConnectionTone)
		setFlags(encoderId, not self.announceStatusUntilConnected.Value, SPLConnectionStopOnError)
		newEncoderLabel = self.encoderLabel.Value
		if newEncoderLabel is None: newEncoderLabel = ""
		self.obj.setStreamLabel(newEncoderLabel)
		self.Destroy()
		global _configDialogOpened
		_configDialogOpened = False

	def onCancel(self, evt):
		self.Destroy()
		global _configDialogOpened
		_configDialogOpened = False

	def onAppTerminate(self):
		self.onCancel(None)


# Announce connected encoders if any.
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
				connectedEncoders.append(encoder.encoderId)
		if len(connectedEncoders) > 0:
			# Translators: presented when at least one encoder is connected.
			ui.message(_("Connected encoders: {encodersConnected}").format(encodersConnected=", ".join(connectedEncoders)))
		else:
			# Translators: presented when no encoders are connected.
			ui.message(_("No encoders connected"))


class Encoder(IAccessible):
	"""Represents an encoder from within StationPlaylist Studio or Streamer.
	This abstract base encoder provides scripts for all encoders such as encoder settings dialog and toggling focusing to Studio when connected.
	Subclasses must provide scripts to handle encoder connection and connection announcement routines.
	Most importantly, each encoder class must provide a unique identifying string to identify the type of the encoder (e.g. SAM for SAM encoder).
	"""

	# Some helper functions
	# 17.08: most are properties.

	# Get the encoder identifier.
	# This consists of two or three letter abbreviations for the encoder and the child ID.
	@property
	def encoderId(self):
		return f"{self.encoderType} {self.IAccessibleChildID}"

	# Get and set encoder labels (hence encoder label is not really a property, although it may appear to be so).

	@property
	def encoderLabel(self):
		try:
			return SPLEncoderLabels[self.encoderId]
		except KeyError:
			return None

	@encoderLabel.setter
	def encoderLabel(self, newEncoderLabel):
		if len(newEncoderLabel):
			SPLEncoderLabels[self.encoderId] = newEncoderLabel
		else:
			try:
				del SPLEncoderLabels[self.encoderId]
			except KeyError:
				pass

	@property
	def focusToStudio(self):
		return self.encoderId in SPLFocusToStudio

	@property
	def playAfterConnecting(self):
		return self.encoderId in SPLPlayAfterConnecting

	@property
	def backgroundMonitor(self):
		return self.encoderId in SPLBackgroundMonitor

	@property
	def connectionTone(self):
		return self.encoderId not in SPLNoConnectionTone

	@property
	def announceStatusUntilConnected(self):
		return self.encoderId not in SPLConnectionStopOnError

	# Format the status message to prepare for monitoring multiple encoders.
	def encoderStatusMessage(self, message):
		# #79 (18.10.1/18.09.3-lts): wxPython 4 is more strict about where timers can be invoked from, and the below function is called from a thread other than the main one, which causes an exception to be logged.
		# This is especially the case with some speech synthesizers and/or braille displays.
		try:
			# #135 (20.06): find out how many background monitor threads for this encoder type are still active.
			# #136 (20.07): encoder monitoring can cross encoder type boundaries (multiple encoder types can be monitored at once).
			# Include encoder ID if multiple encoders have one encoder entry being monitored.
			if len([thread for thread in SPLBackgroundMonitorThreads.values() if thread.is_alive()]) > 1:
				ui.message("{}: {}".format(self.encoderId, message))
			else:
				ui.message(message)
		except:
			pass

	# Encoder connection reporter thread.
	# By default background encoding (no manual connect) is assumed.
	def connectStart(self, manualConnect=False):
		# 20.09: don't bother if another thread is monitoring this encoder.
		if self.encoderId in SPLBackgroundMonitorThreads and SPLBackgroundMonitorThreads[self.encoderId].is_alive(): return
		statusThread = threading.Thread(target=self.reportConnectionStatus, kwargs=dict(manualConnect=manualConnect))
		statusThread.start()
		SPLBackgroundMonitorThreads[self.encoderId] = statusThread

	# #103: the abstract method that is responsible for announcing connection status.
	@abstractmethod
	def reportConnectionStatus(self, manualConnect=False):
		raise NotImplementedError

	# A master flag setter.
	# Set or clear a given flag for the encoder given its ID, flag and flag container (currently a feature set).
	# Also take in the flag key for storing it into the settings file.
	# The flag will then be written to the configuration file.
	# 7.0: Don't dump flags to disk unless told.
	# 20.04: do not dump flags to disk at all, as a dedicated save action will do it.
	# 20.09 optimization: unconditionally do set add/discard.
	def _setFlags(self, encoderId, flag, flagMap):
		flagMap.add(encoderId) if flag else flagMap.discard(encoderId)

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
		self._setFlags(self.encoderId, not self.focusToStudio, SPLFocusToStudio)

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
		self._setFlags(self.encoderId, not self.playAfterConnecting, SPLPlayAfterConnecting)

	@scriptHandler.script(
		# Translators: Input help mode message in SAM Encoder window.
		description=_("Toggles whether NVDA will monitor the selected encoder in the background."),
		gesture="kb:control+f11"
	)
	def script_toggleBackgroundEncoderMonitor(self, gesture):
		if scriptHandler.getLastScriptRepeatCount() == 0:
			if not self.backgroundMonitor:
				# Translators: Presented when toggling the setting to monitor the selected encoder.
				ui.message(_("Monitoring encoder {encoderNumber}").format(encoderNumber=self.IAccessibleChildID))
			else:
				# Translators: Presented when toggling the setting to monitor the selected encoder.
				ui.message(_("Encoder {encoderNumber} will not be monitored").format(encoderNumber=self.IAccessibleChildID))
			self._setFlags(self.encoderId, not self.backgroundMonitor, SPLBackgroundMonitor)
			if self.backgroundMonitor:
				try:
					monitoring = SPLBackgroundMonitorThreads[self.encoderId].is_alive()
				except KeyError:
					monitoring = False
				if not monitoring: self.connectStart()
		else:
			SPLBackgroundMonitor.clear()
			# Translators: Announced when background encoder monitoring is canceled.
			ui.message(_("Encoder monitoring canceled"))

	@scriptHandler.script(
		# Translators: Input help mode message in SAM Encoder window.
		description=_("Opens a dialog to erase encoder labels and settings from an encoder that was deleted."),
		gesture="kb:control+f12"
	)
	def script_encoderSettingsEraser(self, gesture):
		choices = [str(pos) for pos in range(1, self.simpleParent.childCount)]
		# Translators: The title of the encoder settings eraser dialog.
		encoderSettingsEraserTitle = _("Encoder label and settings eraser")
		# Translators: The text of the stream configuration eraser dialog.
		encoderSettingsEraserText = _("Enter the position of the encoder you wish to delete or will delete")
		# 17.12: early versions of wxPython 4 does not have number entry dialog, so replace it with a combo box.
		dlg = wx.SingleChoiceDialog(gui.mainFrame, encoderSettingsEraserText, encoderSettingsEraserTitle, choices=choices)
		dlg.SetSelection(self.IAccessibleChildID-1)
		def callback(result):
			if result == wx.ID_OK:
				_removeEncoderID(self.encoderType, dlg.GetStringSelection())
		gui.runScriptModalDialog(dlg, callback)

	# stream settings.
	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Shows encoder settings dialog to configure various encoder settings such as encoder label."),
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
			wx.CallAfter(gui.messageBox, _("Another encoder settings dialog is open."), translate("Error"), style=wx.OK | wx.ICON_ERROR)

	# Announce complete time including seconds (slight change from global commands version).
	@scriptHandler.script(
		# Translators: Input help mode message for report date and time command.
		description=_("If pressed once, reports the current time including seconds. If pressed twice, reports the current date"),
		gesture="kb:NVDA+F12",
		category=_("StationPlaylist")
	)
	def script_encoderDateTime(self, gesture):
		import winKernel
		if scriptHandler.getLastScriptRepeatCount() == 0:
			text = winKernel.GetTimeFormat(winKernel.LOCALE_USER_DEFAULT, 0, None, None)
		else:
			text = winKernel.GetDateFormat(winKernel.LOCALE_USER_DEFAULT, winKernel.DATE_LONGDATE, None, None)
		ui.message(text)

	# Various column announcement scripts.
	# This base class implements encoder position and labels.
	@scriptHandler.script(gesture="kb:control+NVDA+1")
	def script_announceEncoderPosition(self, gesture):
		ui.message(_("Position: {pos}").format(pos=self.IAccessibleChildID))

	@scriptHandler.script(gesture="kb:control+NVDA+2")
	def script_announceEncoderLabel(self, gesture):
		try:
			encoderLabel = self.getStreamLabel()
		except TypeError:
			encoderLabel = None
		if encoderLabel:
			ui.message(_("Label: {label}").format(label=encoderLabel))
		else:
			ui.message(_("No encoder label"))

	def initOverlayClass(self):
		# Load encoder settings upon request.
		if streamLabels is None: loadStreamLabels()
		# 6.2: Make sure background monitor threads are started if the flag is set.
		if self.backgroundMonitor:
			if self.encoderId in SPLBackgroundMonitorThreads:
				if not SPLBackgroundMonitorThreads[self.encoderId].is_alive():
					del SPLBackgroundMonitorThreads[self.encoderId]
				# If it is indeed alive... Otherwise another thread will be created to keep an eye on this encoder (undesirable).
				else: return
			self.connectStart()

	def reportFocus(self):
		try:
			encoderLabel = self.getStreamLabel()
		except TypeError:
			encoderLabel = None
		# Announce encoder label if it exists.
		if encoderLabel is not None:
			try:
				self.name = "(" + encoderLabel + ") " + self.name
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
	def encoderFormat(self):
		return self.getChild(1).name

	@property
	def connected(self):
		return self._getColumnContentRaw(2) == "Encoding"

	def reportConnectionStatus(self, manualConnect=False):
		# A fake child object holds crucial information about connection status.
		# In order to not block NVDA commands, this will be done using a different thread.
		SPLWin = user32.FindWindowW("SPLStudio", None)
		attemptTime = time.time()
		messageCache = ""
		# Status message flags.
		idle = False
		error = False
		connecting = False
		encoding = False
		# #141 (20.07): prevent multiple connection follow-up actions while background monitoring is on.
		connectedBefore = False
		while True:
			time.sleep(0.001)
			try:
				status = self._getColumnContentRaw(2)
				statusDetails = self._getColumnContentRaw(3)
			except:
				# Don't leave zombie objects around.
				return
			# Encoding status object will die if encoder entry is deleted while being monitored.
			if not status: return
			# Status and description are two separate texts.
			if not messageCache.startswith(status):
				messageCache = "; ".join([status, statusDetails])
				if not messageCache: return
				if not messageCache.startswith("Encoding"):
					self.encoderStatusMessage(messageCache)
			if messageCache.startswith("Idle"):
				if encoding: encoding = False
				if not idle:
					tones.beep(250, 250)
					idle = True
				if manualConnect and (error or connecting): manualConnect = False
			elif messageCache.startswith("Error"):
				# Announce the description of the error.
				if manualConnect and not self.announceStatusUntilConnected: manualConnect = False
				if not error:
					error = True
				if encoding: encoding = False
				if connecting: connecting = False
			elif messageCache.startswith("Encoding"):
				if manualConnect: manualConnect = False
				if connecting: connecting = False
				# We're on air, so exit unless told to monitor for connection changes.
				if not encoding:
					tones.beep(1000, 150)
					self.encoderStatusMessage(messageCache)
					# #141 (20.07): do not focus to Studio or play first selected track if background monitoring is on and this encoder was connected before.
					# Don't forget that follow-up actions should be performed if this is a manual connect (no background monitoring).
					if not self.backgroundMonitor or (self.backgroundMonitor and not connectedBefore):
						if self.focusToStudio:
							user32.SetForegroundWindow(user32.FindWindowW("TStudioForm", None))
						# #37 (17.08.1): if run from another function, the message will not be sent, so must be done here.
						if self.playAfterConnecting:
							# Do not interupt the currently playing track.
							if sendMessage(SPLWin, 1024, 0, SPL_TrackPlaybackStatus) == 0:
								sendMessage(SPLWin, 1024, 0, SPLPlay)
						if not connectedBefore: connectedBefore = True
					if not encoding: encoding = True
			else:
				if not connecting: connecting = True
				if encoding: encoding = False
				elif "Error" not in messageCache and error: error = False
				currentTime = time.time()
				if currentTime-attemptTime >= 0.5 and self.connectionTone:
					tones.beep(500, 50)
					attemptTime = currentTime
			if not manualConnect and not self.backgroundMonitor: return

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
			focus = api.getFocusObject()
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
		ui.message(_("Format: {encoderFormat}").format(encoderFormat=self.encoderFormat))

	@scriptHandler.script(gesture="kb:control+NVDA+4")
	def script_announceEncoderStatus(self, gesture):
		ui.message(_("Status: {encoderStatus}").format(encoderStatus=self.getChild(2).name))

	@scriptHandler.script(gesture="kb:control+NVDA+5")
	def script_announceEncoderStatusDesc(self, gesture):
		ui.message(_("Description: {encoderDescription}").format(encoderDescription=self.getChild(3).name))


class SPLEncoder(Encoder):
	# Support for SPL Encoder window.

	encoderType = "SPL"

	@property
	def encoderFormat(self):
		return self.getChild(0).name

	@property
	def connected(self):
		status = self._getColumnContentRaw(1)
		return "Kbps" in status or "Connected" in status

	def reportConnectionStatus(self, manualConnect=False):
		# Same routine as SAM encoder: use a thread to prevent blocking NVDA commands.
		SPLWin = user32.FindWindowW("SPLStudio", None)
		attemptTime = time.time()
		messageCache = ""
		# Status flags.
		connecting = False
		connected = False
		connectedBefore = False
		while True:
			time.sleep(0.001)
			try:
				status = self._getColumnContentRaw(1)
			except:
				# Don't leave zombie objects around.
				return
			if messageCache != status:
				messageCache = status
				if not messageCache: return
				if "Kbps" not in messageCache:
					self.encoderStatusMessage(messageCache)
			# 20.09: If all encoders are told to connect but then auto-connect stops for the selected encoder, a manually started thread (invoked by a user command) will continue to run.
			# Therefore forcefully stop this thread if the latter message appears.
			if messageCache in ("Disconnected", "AutoConnect stopped."):
				connected = False
				if manualConnect and connecting: manualConnect = False
			elif "Unable to connect" in messageCache or "Failed" in messageCache or status == "AutoConnect stopped.":
				if manualConnect and not self.announceStatusUntilConnected: manualConnect = False
				if connected: connected = False
			elif "Kbps" in messageCache or "Connected" in messageCache:
				connecting = False
				manualConnect = False
				# We're on air, so exit.
				if not connected:
					tones.beep(1000, 150)
					# Same as SAM encoder: do not do this while background monitoring is on and this encoder was once connected before unless this is a manual connect.
					if not self.backgroundMonitor or (self.backgroundMonitor and not connectedBefore):
						if self.focusToStudio:
							user32.SetForegroundWindow(user32.FindWindowW("TStudioForm", None))
						if self.playAfterConnecting:
							if sendMessage(SPLWin, 1024, 0, SPL_TrackPlaybackStatus) == 0:
								sendMessage(SPLWin, 1024, 0, SPLPlay)
						if not connectedBefore: connectedBefore = True
					if not connected: connected = True
			else:
				if connected: connected = False
				if not connecting: connecting = True
				if "Kbps" not in messageCache:
					currentTime = time.time()
					if currentTime-attemptTime >= 0.5 and self.connectionTone:
						tones.beep(500, 50)
						attemptTime = currentTime
			if not manualConnect and not self.backgroundMonitor: return

	@scriptHandler.script(
		# Translators: input hep command for an encoder connection command.
		description=_("Connects to a streaming server."),
		gestures=["kb:f9", "kb:control+f9"]
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
		ui.message(_("Encoder Settings: {setting}").format(setting=self.encoderFormat))

	@scriptHandler.script(gesture="kb:control+NVDA+4")
	def script_announceEncoderTransfer(self, gesture):
		ui.message(_("Transfer Rate: {transferRate}").format(transferRate=self.getChild(1).name))


class AltaCastEncoder(SPLEncoder):
	# Support for AltaCast Encoder window.
	# Deriving from Edcast (now unsupported), user interface resembles SPL Encoder.

	encoderType = "AltaCast"
