# SPL Studio Configuration Manager
# An app module and global plugin package for NVDA
# Copyright 2015 Joseph Lee and others, released under GPL.
# Provides the configuration management package for SPL Studio app module.

import os
from cStringIO import StringIO
from configobj import ConfigObj
from validate import Validator
import weakref
import globalVars
import ui
import gui
import wx
from winUser import user32

# Configuration management
SPLIni = os.path.join(globalVars.appArgs.configPath, "splstudio.ini")
confspec = ConfigObj(StringIO("""
BeepAnnounce = boolean(default=false)
SayEndOfTrack = boolean(default=true)
EndOfTrackTime = integer(min=1, max=59, default=5)
SaySongRamp = boolean(default=true)
SongRampTime = integer(min=1, max=9, default=5)
BrailleTimer = option("off", "intro", "outro", "both", default="off")
MicAlarm = integer(min=0, default="0")
LibraryScanAnnounce = option("off", "ending", "progress", "numbers", default="off")
TrackDial = boolean(default=false)
SayScheduledFor = boolean(default=true)
SayListenerCount = boolean(default=true)
"""), encoding="UTF-8", list_values=False)
confspec.newlines = "\r\n"
SPLConfig = None

# Display an error dialog when configuration validation fails.
def runConfigErrorDialog(errorText, errorType):
	wx.CallAfter(gui.messageBox, errorText, errorType, wx.OK|wx.ICON_ERROR)

# Reset settings to defaults.
# This will be called when validation fails or when the user asks for it.
def resetConfig(defaults, activeConfig, intentional=False):
	for setting in activeConfig:
		activeConfig[setting] = defaults[setting]
	activeConfig.write()
	if intentional:
		# Translators: A dialog message shown when settings were reset to defaults.
		wx.CallAfter(gui.messageBox, _("Successfully applied default add-on settings."),
		# Translators: Title of the reset config dialog.
		_("Reset configuration"), wx.OK|wx.ICON_INFORMATION)

# To be run in app module constructor.
# With the load function below, load the config upon request.
# 6.0: The below init function is really a vehicle that traverses through config profiles in a loop.
def initConfig():
	# Load the default config.
	# Todo (6.0: go through the config beltway, loading each config along the way.
	global SPLConfig
	SPLConfig = unlockConfig(SPLIni)

# 6.0: Unlock (load) profiles from files.
def unlockConfig(path):
	SPLConfigCheckpoint = ConfigObj(path, configspec = confspec, encoding="UTF-8")
	# 5.2 and later: check to make sure all values are correct.
	val = Validator()
	configTest = SPLConfigCheckpoint.validate(val, copy=True)
	if configTest != True:
		# Hack: have a dummy config obj handy just for storing default values.
		SPLDefaults = ConfigObj(None, configspec = confspec, encoding="UTF-8")
		SPLDefaults.validate(val, copy=True)
		# Translators: Standard error title for configuration error.
		title = _("Studio add-on Configuration error")
		if not configTest:
			# Case 1: restore settings to defaults when 5.x config validation has failed on all values.
			resetConfig(SPLDefaults, SPLConfigCheckpoint)
			# Translators: Standard dialog message when Studio configuration has problems and was reset to defaults.
			errorMessage = _("Your Studio add-on configuration has errors and was reset to factory defaults.")
		elif isinstance(configTest, dict):
			# Case 2: For 5.x and later, attempt to reconstruct the failed values.
			for setting in configTest:
				if not configTest[setting]:
					SPLConfigCheckpoint[setting] = SPLDefaults[setting]
			# Translators: Standard dialog message when some Studio configuration settings were reset to defaults.
			errorMessage = _("Errors were found in some of your Studio configuration settings. The affected settings were reset to defaults.")
			SPLConfigCheckpoint.write()
		try:
			runConfigErrorDialog(errorMessage, title)
		except AttributeError:
			pass
	return SPLConfigCheckpoint

# Save configuration database.
def saveConfig():
	# 5.0: Save the one and only SPL config database.
	# Todo for 6.0: save all config profiles.
	global SPLConfig
	if SPLConfig is not None: SPLConfig.write()
	SPLConfig = None


# Configuration dialog.
class SPLConfigDialog(gui.SettingsDialog):
	# Translators: This is the label for the StationPlaylist Studio configuration dialog.
	title = _("Studio Add-on Settings")

	def makeSettings(self, settingsSizer):

		# Translators: the label for a setting in SPL add-on settings to set status announcement between words and beeps.
		self.beepAnnounceCheckbox=wx.CheckBox(self,wx.NewId(),label=_("&Beep for status announcements"))
		self.beepAnnounceCheckbox.SetValue(SPLConfig["BeepAnnounce"])
		settingsSizer.Add(self.beepAnnounceCheckbox, border=10,flag=wx.TOP)

		self.outroSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Check box hiding method comes from Alberto Buffolino's Columns Review add-on.
		# Translators: Label for a check box in SPL add-on settings to notify when end of track (outro) is approaching.
		self.outroCheckBox=wx.CheckBox(self,wx.NewId(),label=_("&Notify when end of track is approaching"))
		self.outroCheckBox.SetValue(SPLConfig["SayEndOfTrack"])
		self.outroCheckBox.Bind(wx.EVT_CHECKBOX, self.onOutroCheck)
		self.outroSizer.Add(self.outroCheckBox, border=10,flag=wx.BOTTOM)

		# Translators: The label for a setting in SPL Add-on settings to specify end of track (outro) alarm.
		self.outroAlarmLabel = wx.StaticText(self, wx.ID_ANY, label=_("&End of track alarm in seconds"))
		self.outroSizer.Add(self.outroAlarmLabel)
		self.endOfTrackAlarm = wx.SpinCtrl(self, wx.ID_ANY, min=1, max=59)
		self.endOfTrackAlarm.SetValue(long(SPLConfig["EndOfTrackTime"]))
		self.outroSizer.Add(self.endOfTrackAlarm)
		self.onOutroCheck(None)
		settingsSizer.Add(self.outroSizer, border=10, flag=wx.BOTTOM)

		self.introSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: Label for a check box in SPL add-on settings to notify when end of intro is approaching.
		self.introCheckBox=wx.CheckBox(self,wx.NewId(),label=_("&Notify when end of introduction is approaching"))
		self.introCheckBox.SetValue(SPLConfig["SaySongRamp"])
		self.introCheckBox.Bind(wx.EVT_CHECKBOX, self.onIntroCheck)
		self.introSizer.Add(self.introCheckBox, border=10,flag=wx.BOTTOM)

		# Translators: The label for a setting in SPL Add-on settings to specify track intro alarm.
		self.introAlarmLabel = wx.StaticText(self, wx.ID_ANY, label=_("&Track intro alarm in seconds"))
		self.introSizer.Add(self.introAlarmLabel)
		self.songRampAlarm = wx.SpinCtrl(self, wx.ID_ANY, min=1, max=9)
		self.songRampAlarm.SetValue(long(SPLConfig["SongRampTime"]))
		self.introSizer.Add(self.songRampAlarm)
		self.onIntroCheck(None)
		settingsSizer.Add(self.introSizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to control braille timer.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Braille timer:"))
		self.brailleTimerValues=[("off",_("off")),
		# Translators: One of the braille timer settings.
		("outro",_("track ending")),
		# Translators: One of the braille timer settings.
		("intro",_("track intro")),
		# Translators: One of the braille timer settings.
		("both",_("track intro and ending"))]
		self.brailleTimerList = wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.brailleTimerValues])
		brailleTimerCurValue=SPLConfig["BrailleTimer"]
		selection = (x for x,y in enumerate(self.brailleTimerValues) if y[0]==brailleTimerCurValue).next()  
		try:
			self.brailleTimerList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.brailleTimerList)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.VERTICAL)
		# Translators: The label for a setting in SPL Add-on settings to change microphone alarm setting.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Microphone alarm in seconds"))
		sizer.Add(label)
		self.micAlarm = wx.TextCtrl(self, wx.ID_ANY)
		self.micAlarm.SetValue(str(SPLConfig["MicAlarm"]))
		sizer.Add(self.micAlarm)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to control library scan announcement.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Library scan announcement:"))
		self.libScanValues=[("off",_("off")),
		# Translators: One of the library scan announcement settings.
		("ending",_("start and end only")),
		# Translators: One of the library scan announcement settings.
		("progress",_("scan progress")),
		# Translators: One of the library scan announcement settings.
		("numbers",_("scan count"))]
		self.libScanList = wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.libScanValues])
		libScanCurValue=SPLConfig["LibraryScanAnnounce"]
		selection = (x for x,y in enumerate(self.libScanValues) if y[0]==libScanCurValue).next()  
		try:
			self.libScanList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.libScanList)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to toggle track dial mode on and off.
		self.trackDialCheckbox=wx.CheckBox(self,wx.NewId(),label=_("&Track Dial mode"))
		self.trackDialCheckbox.SetValue(SPLConfig["TrackDial"])
		sizer.Add(self.trackDialCheckbox, border=10,flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to announce scheduled time.
		self.scheduledForCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Announce &scheduled time for the selected track"))
		self.scheduledForCheckbox.SetValue(SPLConfig["SayScheduledFor"])
		sizer.Add(self.scheduledForCheckbox, border=10,flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to announce listener count.
		self.listenerCountCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Announce &listener count"))
		self.listenerCountCheckbox.SetValue(SPLConfig["SayListenerCount"])
		sizer.Add(self.listenerCountCheckbox, border=10,flag=wx.BOTTOM)

		# Translators: The label for a button in SPL add-on configuration dialog to reset settings to defaults.
		self.resetConfigButton = wx.Button(self, wx.ID_ANY, label=_("Reset settings"))
		self.resetConfigButton.Bind(wx.EVT_BUTTON,self.onResetConfig)
		sizer.Add(self.resetConfigButton)

	def postInit(self):
		self.beepAnnounceCheckbox.SetFocus()

	def onOk(self, evt):
		if not self.micAlarm.Value.isdigit():
			gui.messageBox(
				# Translators: Message to report wrong value for microphone alarm.
				_("Incorrect microphone alarm value entered."),
				# Translators: The title of the message box
				_("Error"), wx.OK|wx.ICON_ERROR,self)
			self.micAlarm.SetFocus()
			return
		SPLConfig["BeepAnnounce"] = self.beepAnnounceCheckbox.Value
		SPLConfig["SayEndOfTrack"] = self.outroCheckBox.Value
		SPLConfig["EndOfTrackTime"] = self.endOfTrackAlarm.Value
		SPLConfig["SaySongRamp"] = self.introCheckBox.Value
		SPLConfig["SongRampTime"] = self.songRampAlarm.Value
		SPLConfig["BrailleTimer"] = self.brailleTimerValues[self.brailleTimerList.GetSelection()][0]
		SPLConfig["MicAlarm"] = self.micAlarm.Value
		SPLConfig["LibraryScanAnnounce"] = self.libScanValues[self.libScanList.GetSelection()][0]
		SPLConfig["TrackDial"] = self.trackDialCheckbox.Value
		SPLConfig["SayScheduledFor"] = self.scheduledForCheckbox.Value
		SPLConfig["SayListenerCount"] = self.listenerCountCheckbox.Value
		super(SPLConfigDialog,  self).onOk(evt)

	# Check events for outro and intro alarms, respectively.
	def onOutroCheck(self, evt):
		if not self.outroCheckBox.IsChecked():
			self.outroSizer.Hide(self.outroAlarmLabel)
			self.outroSizer.Hide(self.endOfTrackAlarm)
		else:
			self.outroSizer.Show(self.outroAlarmLabel)
			self.outroSizer.Show(self.endOfTrackAlarm)
		self.Fit()

	def onIntroCheck(self, evt):
		if not self.introCheckBox.IsChecked():
			self.introSizer.Hide(self.introAlarmLabel)
			self.introSizer.Hide(self.songRampAlarm)
		else:
			self.introSizer.Show(self.introAlarmLabel)
			self.introSizer.Show(self.songRampAlarm)
		self.Fit()

	# Reset settings to defaults.
	def onResetConfig(self, evt):
		if gui.messageBox(
		# Translators: A message to warn about resetting SPL config settings to factory defaults.
		_("Are you sure you wish to reset SPL add-on settings to defaults?"),
		# Translators: The title of the warning dialog.
		_("Warning"),wx.YES_NO|wx.NO_DEFAULT|wx.ICON_WARNING,self
		)==wx.YES:
			val = Validator()
			SPLDefaults = ConfigObj(None, configspec = confspec, encoding="UTF-8")
			SPLDefaults.validate(val, copy=True)
			resetConfig(SPLDefaults, SPLConfig, intentional=True)
			self.Destroy()


# Open the above dialog upon request.
def onConfigDialog(evt):
	gui.mainFrame._popupSettingsDialog(SPLConfigDialog)

# Additional configuration dialogs

# A common alarm dialog
# Based on NVDA core's find dialog code (implemented by the author of this add-on).
# Only one instance can be active at a given moment (code borrowed from GUI's exit dialog routine).
_alarmDialogOpened = False

# A common alarm error dialog.
def _alarmError():
	# Translators: Text of the dialog when another alarm dialog is open.
	gui.messageBox(_("Another alarm dialog is open."),_("Error"),style=wx.OK | wx.ICON_ERROR)

class SPLAlarmDialog(wx.Dialog):
	"""A dialog providing common alarm settings.
	This dialog contains a number entry field for alarm duration and a check box to enable or disable the alarm.
	"""

	# The following comes from exit dialog class from GUI package (credit: NV Access and Zahari from Bulgaria).
	_instance = None

	def __new__(cls, parent, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _alarmDialogOpened:
			raise RuntimeError("An instance of alarm dialog is opened")
		inst = cls._instance() if cls._instance else None
		if not inst:
			return super(cls, cls).__new__(cls, parent, *args, **kwargs)
		return inst

	def __init__(self, parent, setting, toggleSetting, title, alarmPrompt, alarmToggleLabel, min, max):
		inst = SPLAlarmDialog._instance() if SPLAlarmDialog._instance else None
		if inst:
			return
		# Use a weakref so the instance can die.
		SPLAlarmDialog._instance = weakref.ref(self)

		# Now the actual alarm dialog code.
		super(SPLAlarmDialog, self).__init__(parent, wx.ID_ANY, title)
		self.setting = setting
		self.toggleSetting = toggleSetting
		mainSizer = wx.BoxSizer(wx.VERTICAL)

		alarmSizer = wx.BoxSizer(wx.HORIZONTAL)
		alarmMessage = wx.StaticText(self, wx.ID_ANY, label=alarmPrompt)
		alarmSizer.Add(alarmMessage)
		self.alarmEntry = wx.SpinCtrl(self, wx.ID_ANY, min=min, max=max)
		self.alarmEntry.SetValue(SPLConfig[setting])
		alarmSizer.Add(self.alarmEntry)
		mainSizer.Add(alarmSizer,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		self.toggleCheckBox=wx.CheckBox(self,wx.NewId(),label=alarmToggleLabel)
		self.toggleCheckBox.SetValue(SPLConfig[toggleSetting])
		mainSizer.Add(self.toggleCheckBox,border=10,flag=wx.BOTTOM)

		mainSizer.AddSizer(self.CreateButtonSizer(wx.OK|wx.CANCEL))
		self.Bind(wx.EVT_BUTTON,self.onOk,id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON,self.onCancel,id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)
		self.alarmEntry.SetFocus()

	def onOk(self, evt):
		global _alarmDialogOpened
		# Optimization: don't bother if Studio is dead and if the same value has been entered.
		if user32.FindWindowA("SPLStudio", None):
			newVal = self.alarmEntry.GetValue()
			newToggle = self.toggleCheckBox.GetValue()
			if SPLConfig[self.setting] != newVal: SPLConfig[self.setting] = newVal
			elif SPLConfig[self.toggleSetting] != newToggle: SPLConfig[self.toggleSetting] = newToggle
		self.Destroy()
		_alarmDialogOpened = False

	def onCancel(self, evt):
		self.Destroy()
		global _alarmDialogOpened
		_alarmDialogOpened = False
