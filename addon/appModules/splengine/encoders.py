# StationPlaylist encoders support
# Copyright 2015-2021 Joseph Lee, released under GPL.
# Split from main global plugin in 2015, transferred to SPL Engine app module in 2020.

# #155 (21.03): remove __future__ import when NVDA runs under Python 3.10.
from __future__ import annotations
from typing import Optional
import threading
import time
import os
import weakref
from abc import abstractmethod
import api
import config
import configobj
import globalVars
import ui
import keyboardHandler
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
# Encoder labels dictionary.
SPLEncoderLabels = {}
# Move focus to Studio once connected.
SPLFocusToStudio = set()
# Play the first selected track after an encoder is connected.
SPLPlayAfterConnecting = set()
# Use a thread to monitor status changes for encoders.
SPLBackgroundMonitor = set()
# A collection of encoder status monitor threads.
SPLBackgroundMonitorThreads: dict[str, threading.Thread] = {}
# Do not play connection tone while an encoder is connecting.
SPLNoConnectionTone = set()
# Stop announcing connection status messages when an error is encountered.
SPLConnectionStopOnError = set()


# Configuration management.
encoderConfig = None


# Load encoder config (including labels and other goodies) from a file-based database.
def loadEncoderConfig() -> None:
	# 20.11 (Flake8 E501): define global variables when first used, not here due to line length.
	global encoderConfig
	encoderConfigPath = os.path.join(globalVars.appArgs.configPath, "splencoders.ini")
	# 7.1: Make sure encoder settings map isn't corrupted.
	# #131 (20.06): encoder focus error message routine was transplanted from Studio app module.
	try:
		encoderConfig = configobj.ConfigObj(encoderConfigPath)
	except configobj.ConfigObjError:
		# To avoid type and runtime errors, create an empty ConfigObj.
		open(encoderConfigPath, "w").close()
		encoderConfig = configobj.ConfigObj(encoderConfigPath)
		wx.CallAfter(
			# Translators: Message displayed if errors were found in encoder configuration file.
			gui.messageBox, _("Your encoder settings had errors and were reset to defaults."),
			# Translators: Title of the encoder settings error dialog.
			_("SPL add-on Encoder settings error"), wx.OK | wx.ICON_ERROR
		)
		return
	# Read encoder labels.
	global SPLEncoderLabels
	try:
		SPLEncoderLabels = dict(encoderConfig["EncoderLabels"])
	except KeyError:
		SPLEncoderLabels = {}
	# Read other settings.
	global SPLFocusToStudio, SPLPlayAfterConnecting, SPLBackgroundMonitor
	if "FocusToStudio" in encoderConfig:
		SPLFocusToStudio = set(encoderConfig["FocusToStudio"])
	if "PlayAfterConnecting" in encoderConfig:
		SPLPlayAfterConnecting = set(encoderConfig["PlayAfterConnecting"])
	if "BackgroundMonitor" in encoderConfig:
		SPLBackgroundMonitor = set(encoderConfig["BackgroundMonitor"])
	global SPLNoConnectionTone, SPLConnectionStopOnError
	if "NoConnectionTone" in encoderConfig:
		SPLNoConnectionTone = set(encoderConfig["NoConnectionTone"])
	if "ConnectionStopOnError" in encoderConfig:
		SPLConnectionStopOnError = set(encoderConfig["ConnectionStopOnError"])
	# 20.04: register config save and reset handlers.
	config.post_configSave.register(saveEncoderConfig)
	config.post_configReset.register(resetEncoderConfig)


# Remove encoder ID from various settings maps and sets.
# This is a private module level function in order for it to be invoked by humans alone.
def _removeEncoderID(encoderType: str, pos: str) -> None:
	encoderID = " ".join([encoderType, pos])
	# Go through each feature map/set, remove the encoder ID and manipulate encoder positions.
	for encoderSettings in (
		SPLEncoderLabels, SPLFocusToStudio,
		SPLPlayAfterConnecting, SPLBackgroundMonitor,
		SPLNoConnectionTone, SPLConnectionStopOnError
	):
		# 21.03/20.09.6-LTS: encoder settings must be either a set or a dictionary unless changed in the future.
		if not isinstance(encoderSettings, (set, dict)):
			continue
		if encoderID in encoderSettings:
			# Other than encoder labels (a dictionary), others are sets.
			if isinstance(encoderSettings, set):
				encoderSettings.remove(encoderID)
			elif isinstance(encoderSettings, dict):
				del encoderSettings[encoderID]
		# In flag sets, unless members are sorted, encoders will appear in random order
		# (a downside of using sets, as their ordering is quite unpredictable).
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
					encoderSettings.add("{} {}".format(encoderType, int(item.split()[-1]) - 1))
				elif isinstance(encoderSettings, dict):
					encoderSettings["{} {}".format(encoderType, int(item.split()[-1]) - 1)] = encoderSettings.pop(item)


# Save encoder labels and flags, called when closing app modules and/or config save command is pressed.
def saveEncoderConfig() -> None:
	# 21.03/20.09.6-LTS: is encoder config even alive?
	if encoderConfig is None:
		raise RuntimeError("Encoder config is not defined, cannot save encoder settings")
	# Gather stream labels and flags.
	# 20.11: dictionaries and sets are global items.
	encoderConfig["EncoderLabels"] = dict(SPLEncoderLabels)
	# For flags, convert flag sets into lists.
	encoderConfig["FocusToStudio"] = list(SPLFocusToStudio)
	encoderConfig["PlayAfterConnecting"] = list(SPLPlayAfterConnecting)
	encoderConfig["BackgroundMonitor"] = list(SPLBackgroundMonitor)
	encoderConfig["NoConnectionTone"] = list(SPLNoConnectionTone)
	encoderConfig["ConnectionStopOnError"] = list(SPLConnectionStopOnError)
	# To save disk space, remove empty data.
	for key in encoderConfig.keys():
		if not len(encoderConfig[key]):
			del encoderConfig[key]
	encoderConfig.write()


# Nullify various flag sets, otherwise memory leak occurs.
# 20.04: if told to do so, save encoder settings and unregister config save handler.
# In case this is called as part of a reset, unregister config save handler unconditionally.
def cleanup(appTerminating: bool = False, reset: bool = False) -> None:
	# 20.11 (Flake8 E501): apart from encoder config, other flag containers are global variables.
	global encoderConfig
	# #132 (20.05): do not proceed if encoder settings database is None (no encoders were initialized).
	if encoderConfig is None:
		return
	if appTerminating:
		saveEncoderConfig()
	if reset or appTerminating:
		config.post_configSave.unregister(saveEncoderConfig)
		config.post_configReset.unregister(resetEncoderConfig)
	for flag in [
		encoderConfig, SPLEncoderLabels,
		SPLFocusToStudio, SPLPlayAfterConnecting,
		SPLBackgroundMonitor, SPLBackgroundMonitorThreads,
		SPLNoConnectionTone, SPLConnectionStopOnError
	]:
		if flag is not None:
			flag.clear()
	# 20.04: save a "clean" copy after resetting encoder settings.
	if reset:
		encoderConfig.write()
	# Nullify encoder settings.
	encoderConfig = None


# Reset encoder settings.
# Because simply reloading settings will introduce errors,
# respond only to proper reset signal (Control+NVDA+R three times).
def resetEncoderConfig(factoryDefaults: bool = False) -> None:
	if factoryDefaults:
		cleanup(reset=True)


# Encoder configuration dialog.
_configDialogOpened = False


class EncoderConfigDialog(wx.Dialog):

	# Instance check comes from NVDA Core's Add-ons Manager (credit: NV Access)
	@classmethod
	def _instance(cls):
		return None

	def __new__(cls, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _configDialogOpened:
			raise RuntimeError("An instance of encoder settings dialog is opened")
		instance = EncoderConfigDialog._instance()
		if instance is None:
			return super(EncoderConfigDialog, cls).__new__(cls, *args, **kwargs)
		return instance

	def __init__(self, parent, obj):
		if EncoderConfigDialog._instance() is not None:
			return
		# Use a weakref so the instance can die.
		EncoderConfigDialog._instance = weakref.ref(self)

		# Encoder format text is used as part of the dialog title.
		self.obj = obj
		self.curEncoderLabel = obj.encoderLabel
		# Translators: The title of the encoder settings dialog (example: Encoder settings for SAM 1").
		title = _("Encoder settings for {name}").format(name=obj.encoderFormat)
		super().__init__(parent, wx.ID_ANY, title)
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		encoderConfigHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		# And to close this automatically when Studio dies.
		from appModules.splstudio import splactions
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)
		global _configDialogOpened
		_configDialogOpened = True

		# Translators: An edit field in encoder settings
		# to set a label for this encoder.
		self.encoderLabel = encoderConfigHelper.addLabeledControl(_("Encoder &label"), wx.TextCtrl)
		self.encoderLabel.SetValue(self.curEncoderLabel if self.curEncoderLabel is not None else "")

		# Translators: A checkbox in encoder settings
		# to set if NVDA should move focus to Studio window when connected.
		focusToStudioLabel = _("&Focus to Studio when connected")
		self.focusToStudio = encoderConfigHelper.addItem(wx.CheckBox(self, label=focusToStudioLabel))
		self.focusToStudio.SetValue(obj.focusToStudio)

		# Translators: A checkbox in encoder settings
		# to set if NVDA should play the next track when connected.
		playAfterConnectingLabel = _("&Play first track when connected")
		self.playAfterConnecting = encoderConfigHelper.addItem(wx.CheckBox(self, label=playAfterConnectingLabel))
		self.playAfterConnecting.SetValue(obj.playAfterConnecting)

		# Translators: A checkbox in encoder settings
		# to set if NVDA should monitor the status of this encoder in the background.
		backgroundMonitorLabel = _("Enable background connection &monitoring")
		self.backgroundMonitor = encoderConfigHelper.addItem(wx.CheckBox(self, label=backgroundMonitorLabel))
		self.backgroundMonitor.SetValue(obj.backgroundMonitor)

		# Translators: A checkbox in encoder settings
		# to set if NVDA should play connection progress tone.
		connectionToneLabel = _("Play connection status &beep while connecting")
		self.connectionTone = encoderConfigHelper.addItem(wx.CheckBox(self, label=connectionToneLabel))
		self.connectionTone.SetValue(obj.connectionTone)

		# Translators: A checkbox in encoder settings
		# to set if NVDA should announce connection progress until an encoder connects.
		announceStatusUntilConnectedLabel = _("Announce connection &status until encoder connects")
		self.announceStatusUntilConnected = encoderConfigHelper.addItem(
			wx.CheckBox(self, label=announceStatusUntilConnectedLabel)
		)
		self.announceStatusUntilConnected.SetValue(obj.announceStatusUntilConnected)

		encoderConfigHelper.addDialogDismissButtons(wx.OK | wx.CANCEL, separated=True)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(encoderConfigHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.CenterOnScreen()
		self.encoderLabel.SetFocus()

	def onOk(self, evt):
		self.obj.focusToStudio = self.focusToStudio.Value
		self.obj.playAfterConnecting = self.playAfterConnecting.Value
		self.obj.backgroundMonitor = self.backgroundMonitor.Value
		self.obj.connectionTone = self.connectionTone.Value
		self.obj.announceStatusUntilConnected = self.announceStatusUntilConnected.Value
		newEncoderLabel = self.encoderLabel.Value
		if newEncoderLabel is None:
			newEncoderLabel = ""
		self.obj.encoderLabel = newEncoderLabel
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
def announceEncoderConnectionStatus() -> None:
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
		sysListView32EncoderWindow = windowUtils.findDescendantWindow(
			desktopHwnd, className="SysListView32", controlID=1004
		)
	except LookupError:
		sysListView32EncoderWindow = 0
	if not samEncoderWindow and not sysListView32EncoderWindow:
		# Translators: presented when no streaming encoders were found when trying to obtain connection status.
		ui.message(_("No encoders found"))
	elif samEncoderWindow and sysListView32EncoderWindow:
		# Translators: presented when more than one encoder type is active
		# when trying to obtain encoder connection status.
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
			encodersConnectedMessage = _("Connected encoders: {encodersConnected}").format(
				encodersConnected=", ".join(connectedEncoders)
			)
		else:
			# Translators: presented when no encoders are connected.
			encodersConnectedMessage = _("No encoders connected")
		ui.message(encodersConnectedMessage)


class Encoder(IAccessible):
	"""Represents an encoder from within StationPlaylist Studio or Streamer.
	This abstract base encoder provides scripts for all encoders such as encoder settings dialog
	and toggling focusing to Studio when connected.
	Subclasses must provide scripts to handle encoder connection and connection announcement routines.
	Most importantly, each encoder class must provide a unique string to identify the encoder type
	(e.g. SAM for SAM encoder).
	"""

	def _get_name(self):
		encoderLabel = self.encoderLabel
		name = super(Encoder, self).name
		# Announce encoder label if it exists.
		if encoderLabel is not None:
			try:
				name = "(" + encoderLabel + ") " + name
			except TypeError:
				pass
		return name

	# Some helper functions
	# 17.08: most are properties.

	# Get the encoder identifier.
	# This consists of two or three letter abbreviations for the encoder and the child ID.
	@property
	def encoderId(self) -> str:
		return f"{self.encoderType} {self.IAccessibleChildID}"

	# Get and set encoder labels (hence encoder label is not really a property, although it may appear to be so).

	@property
	def encoderLabel(self) -> Optional[str]:
		return SPLEncoderLabels.get(self.encoderId, None)

	@encoderLabel.setter
	def encoderLabel(self, newEncoderLabel: str) -> None:
		if not isinstance(newEncoderLabel, str):
			raise TypeError("Encoder label must be a string")
		if len(newEncoderLabel):
			SPLEncoderLabels[self.encoderId] = newEncoderLabel
		else:
			try:
				del SPLEncoderLabels[self.encoderId]
			except KeyError:
				pass

	@property
	def focusToStudio(self) -> bool:
		return self.encoderId in SPLFocusToStudio

	@focusToStudio.setter
	def focusToStudio(self, flag: bool) -> None:
		if not isinstance(flag, bool):
			raise TypeError("Flag must be a boolean")
		if flag:
			SPLFocusToStudio.add(self.encoderId)
		else:
			SPLFocusToStudio.discard(self.encoderId)

	@property
	def playAfterConnecting(self) -> bool:
		return self.encoderId in SPLPlayAfterConnecting

	@playAfterConnecting.setter
	def playAfterConnecting(self, flag: bool) -> None:
		if not isinstance(flag, bool):
			raise TypeError("Flag must be a boolean")
		if flag:
			SPLPlayAfterConnecting.add(self.encoderId)
		else:
			SPLPlayAfterConnecting.discard(self.encoderId)

	@property
	def backgroundMonitor(self) -> bool:
		return self.encoderId in SPLBackgroundMonitor

	@backgroundMonitor.setter
	def backgroundMonitor(self, flag: bool) -> None:
		if not isinstance(flag, bool):
			raise TypeError("Flag must be a boolean")
		if flag:
			SPLBackgroundMonitor.add(self.encoderId)
		else:
			SPLBackgroundMonitor.discard(self.encoderId)

	# For the next two properties, setter should invert the flag.

	@property
	def connectionTone(self) -> bool:
		return self.encoderId not in SPLNoConnectionTone

	@connectionTone.setter
	def connectionTone(self, flag: bool) -> None:
		if not isinstance(flag, bool):
			raise TypeError("Flag must be a boolean")
		if not flag:
			SPLNoConnectionTone.add(self.encoderId)
		else:
			SPLNoConnectionTone.discard(self.encoderId)

	@property
	def announceStatusUntilConnected(self) -> bool:
		return self.encoderId not in SPLConnectionStopOnError

	@announceStatusUntilConnected.setter
	def announceStatusUntilConnected(self, flag: bool) -> None:
		if not isinstance(flag, bool):
			raise TypeError("Flag must be a boolean")
		if not flag:
			SPLConnectionStopOnError.add(self.encoderId)
		else:
			SPLConnectionStopOnError.discard(self.encoderId)

	# Format the status message to prepare for monitoring multiple encoders.
	def encoderStatusMessage(self, message: str) -> None:
		# #79 (18.10.1/18.09.3-lts): wxPython 4 is more strict about where timers can be invoked from.
		# An exception will be logged if called from a thread other than the main one.
		# This is especially the case with some speech synthesizers and/or braille displays.
		try:
			# #135 (20.06): find out how many background monitor threads for this encoder type are still active.
			# #136 (20.07): encoder monitoring can cross encoder type boundaries
			# (multiple encoder types can be monitored at once).
			# Include encoder ID if multiple encoders have one encoder entry being monitored.
			if len([thread for thread in SPLBackgroundMonitorThreads.values() if thread.is_alive()]) > 1:
				ui.message("{}: {}".format(self.encoderId, message))
			else:
				ui.message(message)
		except Exception:
			pass

	# Encoder connection reporter thread.
	# By default background encoding (no manual connect) is assumed.
	def connectStart(self, manualConnect: bool = False) -> None:
		# 20.09: don't bother if another thread is monitoring this encoder.
		if self.encoderId in SPLBackgroundMonitorThreads and SPLBackgroundMonitorThreads[self.encoderId].is_alive():
			return
		statusThread = threading.Thread(
			target=self.reportConnectionStatus, kwargs=dict(manualConnect=manualConnect)
		)
		statusThread.start()
		SPLBackgroundMonitorThreads[self.encoderId] = statusThread

	# #103: the abstract method that is responsible for announcing connection status.
	@abstractmethod
	def reportConnectionStatus(self, manualConnect: bool = False) -> None:
		raise NotImplementedError

	# Respond to encoders being connected.
	# Almost identical to version 17.08 iteration except for being private.
	def _onConnect(self) -> None:
		# Do not proceed if already focused on Studio window.
		if api.getFocusObject().appModule.appName == "splstudio":
			return
		# #150 (20.10/20.09.2-LTS): announce a message if Studio window is minimized.
		if self.focusToStudio:
			import windowUtils
			try:
				studioWindow = windowUtils.findDescendantWindow(
					api.getDesktopObject().windowHandle, visible=True, className="TStudioForm"
				)
				user32.SetForegroundWindow(studioWindow)
			except LookupError:
				# Translators: presented when SPL Studio window is minimized.
				ui.message(_("SPL Studio is minimized to system tray."))
		if self.playAfterConnecting:
			# Do not interupt the currently playing track.
			SPLWin = user32.FindWindowW("SPLStudio", None)
			if sendMessage(SPLWin, 1024, 0, SPL_TrackPlaybackStatus) == 0:
				sendMessage(SPLWin, 1024, 0, SPLPlay)

	# Now the flag configuration scripts.

	@scriptHandler.script(
		# Translators: Input help mode message for an encoder settings command.
		description=_("Toggles whether NVDA will switch to Studio when connected to a streaming server."),
		gesture="kb:f11"
	)
	def script_toggleFocusToStudio(self, gesture):
		if not self.focusToStudio:
			# Translators: Presented when toggling the setting
			# to switch to Studio when connected to a streaming server.
			ui.message(_("Switch to Studio after connecting"))
		else:
			# Translators: Presented when toggling the setting
			# to switch to Studio when connected to a streaming server.
			ui.message(_("Do not switch to Studio after connecting"))
		self.focusToStudio = not self.focusToStudio

	@scriptHandler.script(
		# Translators: Input help mode message for an encoder settings command.
		description=_("Toggles whether Studio will play the first song when connected to a streaming server."),
		gesture="kb:shift+f11"
	)
	def script_togglePlay(self, gesture):
		if not self.playAfterConnecting:
			# Translators: Presented when toggling the setting
			# to play the selected track in Studio when connected to a streaming server.
			ui.message(_("Play first track after connecting"))
		else:
			# Translators: Presented when toggling the setting
			# to play the selected track in Studio when connected to a streaming server.
			ui.message(_("Do not play first track after connecting"))
		self.playAfterConnecting = not self.playAfterConnecting

	@scriptHandler.script(
		# Translators: Input help mode message for an encoder settings command.
		description=_("Toggles whether NVDA will monitor the selected encoder in the background."),
		gesture="kb:control+f11"
	)
	def script_toggleBackgroundEncoderMonitor(self, gesture):
		if scriptHandler.getLastScriptRepeatCount() == 0:
			if not self.backgroundMonitor:
				# Translators: Presented when toggling the setting
				# to monitor the selected encoder in the background.
				monitorMessage = _("Monitoring encoder {encoderNumber}").format(
					encoderNumber=self.IAccessibleChildID
				)
			else:
				# Translators: Presented when toggling the setting
				# to monitor the selected encoder in the background.
				monitorMessage = _("Encoder {encoderNumber} will not be monitored").format(
					encoderNumber=self.IAccessibleChildID
				)
			ui.message(monitorMessage)
			self.backgroundMonitor = not self.backgroundMonitor
			if self.backgroundMonitor:
				try:
					monitoring = SPLBackgroundMonitorThreads[self.encoderId].is_alive()
				except KeyError:
					monitoring = False
				if not monitoring:
					self.connectStart()
		else:
			SPLBackgroundMonitor.clear()
			# Translators: Announced when background encoder monitoring is canceled.
			ui.message(_("Encoder monitoring canceled"))

	@scriptHandler.script(
		# Translators: Input help mode message for an encoder settings command.
		description=_("Opens a dialog to erase encoder labels and settings from an encoder that was deleted."),
		gesture="kb:control+f12"
	)
	def script_encoderLabelsSettingsEraser(self, gesture):
		# 17.12: early versions of wxPython 4 does not have number entry dialog, so replace it with a combo box.
		dlg = wx.SingleChoiceDialog(
			gui.mainFrame,
			# Translators: The text of the stream configuration eraser dialog.
			_("Enter the position of the encoder you wish to delete or will delete"),
			# Translators: The title of the encoder settings eraser dialog.
			_("Encoder label and settings eraser"),
			choices=[str(pos) for pos in range(1, self.simpleParent.childCount)]
		)
		dlg.SetSelection(self.IAccessibleChildID - 1)

		def callback(result):
			if result == wx.ID_OK:
				_removeEncoderID(self.encoderType, dlg.GetStringSelection())
		gui.runScriptModalDialog(dlg, callback)

	# stream settings.
	@scriptHandler.script(
		# Translators: Input help mode message for a command in StationPlaylist add-on.
		description=_("Shows encoder settings dialog to configure various encoder settings such as encoder label."),
		gestures=["kb:alt+NVDA+0", "kb:f12"],
		category=_("StationPlaylist")
	)
	def script_openEncoderConfigDialog(self, gesture):
		try:
			d = EncoderConfigDialog(gui.mainFrame, self)
			gui.mainFrame.prePopup()
			d.Raise()
			d.Show()
			gui.mainFrame.postPopup()
		except RuntimeError:
			from ..skipTranslation import translate
			wx.CallAfter(
				# Translators: Text of the dialog when another encoder settings dialog is open.
				gui.messageBox, _("Another encoder settings dialog is open."),
				translate("Error"), style=wx.OK | wx.ICON_ERROR
			)

	# Announce complete time including seconds (slight change from global commands version).
	@scriptHandler.script(
		description=_(
			# Translators: Input help mode message for report date and time command.
			"If pressed once, reports the current time including seconds. "
			"If pressed twice, reports the current date"
		),
		gesture="kb:NVDA+F12",
		category=_("StationPlaylist")
	)
	def script_encoderDateTime(self, gesture):
		import winKernel
		if scriptHandler.getLastScriptRepeatCount() == 0:
			text = winKernel.GetTimeFormatEx(winKernel.LOCALE_NAME_USER_DEFAULT, 0, None, None)
		else:
			text = winKernel.GetDateFormatEx(winKernel.LOCALE_NAME_USER_DEFAULT, winKernel.DATE_LONGDATE, None, None)
		ui.message(text)

	# Various column announcement scripts.
	# This base class implements encoder position and labels.
	@scriptHandler.script(gesture="kb:control+NVDA+1")
	def script_announceEncoderPosition(self, gesture):
		# Translators: describes the current encoder position.
		ui.message(_("Position: {pos}").format(pos=self.IAccessibleChildID))

	@scriptHandler.script(gesture="kb:control+NVDA+2")
	def script_announceEncoderLabel(self, gesture):
		try:
			encoderLabel = self.encoderLabel
		except TypeError:
			encoderLabel = None
		if encoderLabel:
			# Translators: describes the current encoder label if any.
			ui.message(_("Label: {label}").format(label=encoderLabel))
		else:
			# Translators: describes the current encoder label if any.
			ui.message(_("No encoder label"))

	def initOverlayClass(self):
		# Load encoder settings upon request.
		if encoderConfig is None:
			loadEncoderConfig()
		# 6.2: Make sure background monitor threads are started if the flag is set.
		if self.backgroundMonitor:
			if self.encoderId in SPLBackgroundMonitorThreads:
				if not SPLBackgroundMonitorThreads[self.encoderId].is_alive():
					del SPLBackgroundMonitorThreads[self.encoderId]
				# If it is indeed alive...
				# Otherwise another thread will be created to keep an eye on this encoder (undesirable).
				else:
					return
			self.connectStart()


class SAMEncoder(Encoder, sysListView32.ListItem):
	# Support for Sam Encoders.

	encoderType = "SAM"

	def _moveToRow(self, row):
		# In addition to moving to the next or previous encoder entry, set focus on the new encoder entry once more.
		super(SAMEncoder, self)._moveToRow(row)
		if row is not None:
			row.setFocus()

	@property
	def encoderFormat(self) -> str:
		return self.getChild(1).name

	@property
	def connected(self) -> bool:
		return self.getChild(2).name == "Encoding"

	def reportConnectionStatus(self, manualConnect: bool = False) -> None:
		# A fake child object holds crucial information about connection status.
		# In order to not block NVDA commands, this will be done using a different thread.
		attemptTime = time.time()
		messageCache = ""
		# Status message flags.
		error = False
		connecting = False
		encoding = False
		# #141 (20.07): prevent multiple connection follow-up actions while background monitoring is on.
		connectedBefore = False
		while True:
			time.sleep(0.001)
			try:
				status = self.getChild(2).name
				statusDetails = self.getChild(3).name
			except AttributeError:
				# Seen when NVDA exits while connecting or background monitor is on.
				return
			# Encoding status object will die if encoder entry is deleted while being monitored.
			if not status:
				return
			# Status and description are two separate texts.
			if not messageCache.startswith(status):
				messageCache = "; ".join([status, statusDetails])
				if not messageCache:
					return
				if not messageCache.startswith("Encoding"):
					self.encoderStatusMessage(messageCache)
			if messageCache.startswith("Idle"):
				encoding = False
				if manualConnect and (error or connecting):
					manualConnect = False
			elif messageCache.startswith("Error"):
				# Announce the description of the error.
				if manualConnect and not self.announceStatusUntilConnected:
					manualConnect = False
				error = True
				encoding = False
				connecting = False
			elif messageCache.startswith("Encoding"):
				manualConnect = False
				connecting = False
				# We're on air, so exit unless told to monitor for connection changes.
				if not encoding:
					tones.beep(1000, 150)
					self.encoderStatusMessage(messageCache)
					# #141 (20.07): do not focus to Studio or play first selected track
					# if background monitoring is on and this encoder was connected before.
					# Don't forget that follow-up actions should be performed
					# if this is a manual connect (no background monitoring).
					if not self.backgroundMonitor or (self.backgroundMonitor and not connectedBefore):
						# 20.09: queue actions such as focus to Studio and playing the selected track.
						wx.CallAfter(self._onConnect)
						connectedBefore = True
					encoding = True
			else:
				connecting = True
				encoding = False
				if "Error" not in messageCache and error:
					error = False
				currentTime = time.time()
				if currentTime - attemptTime >= 0.5 and self.connectionTone:
					tones.beep(500, 50)
					attemptTime = currentTime
			if not manualConnect and not self.backgroundMonitor:
				return

	@scriptHandler.script(gesture="kb:f9")
	def script_connect(self, gesture):
		gesture.send()
		# Translators: Presented when an Encoder is trying to connect to a streaming server.
		ui.message(_("Connecting..."))
		# Oi, status thread, can you keep an eye on the connection status for me?
		# To be packaged into a new function in 7.0.
		if not self.backgroundMonitor:
			self.connectStart(manualConnect=True)

	@scriptHandler.script(gesture="kb:f10")
	def script_disconnect(self, gesture):
		gesture.send()
		# Translators: Presented when an Encoder is disconnecting from a streaming server.
		ui.message(_("Disconnecting..."))

	# Connecting/disconnecting all encoders at once.
	# Control+F9/Control+F10 hotkeys are broken. Thankfully, context menu retains these commands.
	# #143 (20.09): manually open context menu and activate the correct item
	# through keyboard key press emulation (keyboard gesture send loop).
	# Presses refer to how many times down arrow must be 'pressed' once context menu opens.

	def _samContextMenu(self, presses: int) -> None:
		import itertools
		keyboardHandler.KeyboardInputGesture.fromName("applications").send()
		for key in itertools.repeat("downArrow", presses):
			keyboardHandler.KeyboardInputGesture.fromName(key).send()
		keyboardHandler.KeyboardInputGesture.fromName("enter").send()

	@scriptHandler.script(gesture="kb:control+f9")
	def script_connectAll(self, gesture):
		ui.message(_("Connecting..."))
		self._samContextMenu(6)
		# Oi, status thread, can you keep an eye on the connection status for me?
		if not self.backgroundMonitor:
			self.connectStart(manualConnect=True)

	@scriptHandler.script(gesture="kb:control+f10")
	def script_disconnectAll(self, gesture):
		ui.message(_("Disconnecting..."))
		self._samContextMenu(7)

	# Announce SAM columns: encoder name/type, status and description.
	@scriptHandler.script(gesture="kb:control+NVDA+3")
	def script_announceEncoderFormat(self, gesture):
		ui.message("{0}: {1}".format(self.getChild(1).columnHeaderText, self.encoderFormat))

	@scriptHandler.script(gesture="kb:control+NVDA+4")
	def script_announceEncoderStatus(self, gesture):
		ui.message("{0}: {1}".format(self.getChild(2).columnHeaderText, self.getChild(2).name))

	@scriptHandler.script(gesture="kb:control+NVDA+5")
	def script_announceEncoderStatusDesc(self, gesture):
		ui.message("{0}: {1}".format(self.getChild(3).columnHeaderText, self.getChild(3).name))


class SPLEncoder(Encoder):
	# Support for SPL Encoder window.

	encoderType = "SPL"

	@property
	def encoderFormat(self) -> str:
		return self.getChild(0).name

	@property
	def connected(self) -> bool:
		status = self.getChild(1).name
		return "Kbps" in status or "Connected" in status

	def reportConnectionStatus(self, manualConnect: bool = False) -> None:
		# Same routine as SAM encoder: use a thread to prevent blocking NVDA commands.
		attemptTime = time.time()
		messageCache = ""
		# Status flags.
		connecting = False
		connected = False
		connectedBefore = False
		while True:
			time.sleep(0.001)
			try:
				status = self.getChild(1).name
			except AttributeError:
				# Seen when NVDA exits while connecting or background monitor is on.
				return
			if messageCache != status:
				messageCache = status
				if not messageCache:
					return
				if "Kbps" not in messageCache:
					self.encoderStatusMessage(messageCache)
			# 20.09: If all encoders are told to connect but then auto-connect stops for the selected encoder,
			# a manually started thread (invoked by a user command) will continue to run.
			# Therefore forcefully stop this thread if the latter message appears.
			if messageCache in ("Disconnected", "AutoConnect stopped."):
				connected = False
				if manualConnect and connecting:
					manualConnect = False
			elif "Unable to connect" in messageCache or "Failed" in messageCache or status == "AutoConnect stopped.":
				if manualConnect and not self.announceStatusUntilConnected:
					manualConnect = False
				if connected:
					connected = False
			elif "Kbps" in messageCache or "Connected" in messageCache:
				connecting = False
				manualConnect = False
				# We're on air, so exit.
				if not connected:
					tones.beep(1000, 150)
					# Same as SAM encoder: do not do this while background monitoring is on
					# and this encoder was once connected before unless this is a manual connect.
					if not self.backgroundMonitor or (self.backgroundMonitor and not connectedBefore):
						# 20.09: queue actions such as focus to Studio and playing the selected track.
						wx.CallAfter(self._onConnect)
						connectedBefore = True
					connected = True
			else:
				if connected:
					connected = False
				if not connecting:
					connecting = True
				if "Kbps" not in messageCache:
					currentTime = time.time()
					if currentTime - attemptTime >= 0.5 and self.connectionTone:
						tones.beep(500, 50)
						attemptTime = currentTime
			if not manualConnect and not self.backgroundMonitor:
				return

	# Connect selected encoders.
	# #143 (20.09): just like SAM encoder's connect/disconnect all routines, use key press emulation.

	@scriptHandler.script(
		# Translators: input hep command for an encoder connection command.
		description=_("Connects the selected encoder."),
		gesture="kb:f9"
	)
	def script_connect(self, gesture):
		if self.getChild(1).name not in ("Disconnected", "AutoConnect stopped."):
			return
		ui.message(_("Connecting..."))
		for key in ("applications", "downArrow", "enter"):
			keyboardHandler.KeyboardInputGesture.fromName(key).send()
		# Same as SAM's connection routine, but this time, keep an eye on self.name and a different connection flag.
		if not self.backgroundMonitor:
			self.connectStart(manualConnect=True)

	@scriptHandler.script(
		# Translators: input hep command for an encoder connection command.
		description=_("Connects all encoders."),
		gesture="kb:control+f9"
	)
	def script_connectAll(self, gesture):
		connectButton = api.getForegroundObject().getChild(2)
		if connectButton.name == "Disconnect":
			return
		ui.message(_("Connecting..."))
		# Juggle the focus around.
		connectButton.doAction()
		self.setFocus()
		if not self.backgroundMonitor:
			self.connectStart(manualConnect=True)

	# Announce SPL Encoder columns: encoder settings and transfer rate.
	@scriptHandler.script(gesture="kb:control+NVDA+3")
	def script_announceEncoderSettings(self, gesture):
		ui.message("{0}: {1}".format(self.firstChild.columnHeaderText, self.encoderFormat))

	@scriptHandler.script(gesture="kb:control+NVDA+4")
	def script_announceEncoderTransfer(self, gesture):
		ui.message("{0}: {1}".format(self.getChild(1).columnHeaderText, self.getChild(1).name))


class AltaCastEncoder(SPLEncoder):
	# Support for AltaCast Encoder window.
	# Deriving from Edcast (now unsupported), user interface resembles SPL Encoder.

	encoderType = "AltaCast"
