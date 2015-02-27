# SPL Studio Configuration Manager
# An app module and global plugin package for NVDA
# Copyright 2015 Joseph Lee and others, released under GPL.
# Provides the configuration management package for SPL Studio app module.

import os
from cStringIO import StringIO
from configobj import ConfigObj
from validate import Validator
import globalVars
import ui
import gui
import wx
from winUser import user32

# Configuration management
SPLIni = os.path.join(globalVars.appArgs.configPath, "splstudio.ini")
confspec = ConfigObj(StringIO("""
BeepAnnounce = boolean(default=false)
SayEndOfTrackTime = boolean(default=true)
EndOfTrackTime = integer(min=1, max=59, default=5)
SongRampTime = integer(min=1, max=9, default=5)
BrailleTimer = option("off", "intro", "outro", "both", default="off")
MicAlarm = integer(min=0, default="0")
TrackDial = boolean(default=false)
SayScheduledFor = boolean(default=true)
SayListenerCount = boolean(default=true)
"""), encoding="UTF-8", list_values=False)
confspec.newlines = "\r\n"
SPLConfig = None

# List of values to be converted manually.
# This will be called only once: when upgrading from prior versions to 5.0, to be removed in 5.1.
configConversions=("EndOfTrackTime", "SongRampTime")

# The accompanying function for config conversion.
# Returns config=false if errors occur, to be checked in the app module constructor.
def config4to5():
	global SPLConfig, configConversions
	for setting in configConversions:
		try:
			oldValue = str(SPLConfig[setting])
		except KeyError:
			continue
		if oldValue.isdigit():
			continue
		# If the old value doesn't conform to below conditions, start from a fresh config spec.
		try:
			if (len(oldValue) != 5
			and not oldValue.startswith("00:")
			and not oldValue.split(":")[1].isdigit()):
				return False
		finally:
			return False
		newValue = SPLConfig[setting].split(":")[1]
		SPLConfig[setting] = int(newValue)
	return True

# Display an error dialog when configuration validation fails.
def runConfigErrorDialog(errorText, errorType):
	wx.CallAfter(gui.messageBox, errorText, errorType, wx.OK|wx.ICON_ERROR)

# To be run in app module constructor.
def initConfig():
	global SPLConfig
	SPLConfig = ConfigObj(SPLIni, configspec = confspec, encoding="UTF-8")
	# 5.0 only: migrate 4.x format to 5.0, to be removed in 5.1.
	migrated = config4to5()
	# 5.1 and later: check to make sure all values are correct.
	val = Validator()
	configTest = SPLConfig.validate(val, copy=True)
	if configTest != True:
		# Hack: have a dummy config obj handy just for storing default values.
		SPLDefaults = ConfigObj(None, configspec = confspec, encoding="UTF-8")
		SPLDefaults.validate(val, copy=True)
		# Translators: Standard error title for configuration error.
		title = _("Studio add-on Configuration error")
		if not configTest or not migrated:
			# Case 1: restore settings to defaults.
			# This may happen when 4.x config had parsing issues or 5.x config validation has failed on all values.
			for setting in SPLConfig:
				SPLConfig[setting] = SPLDefaults[setting]
			# Translators: Standard dialog message when Studio configuration has problems and was reset to defaults.
			errorMessage = _("Your Studio add-on configuration has errors and was reset to factory defaults.")
		elif isinstance(configTest, dict):
			# Case 2: For 5.x and later, attempt to reconstruct the failed values.
			for setting in configTest:
				if not configTest[setting]:
					SPLConfig[setting] = SPLDefaults[setting]
			# Translators: Standard dialog message when some Studio configuration settings were reset to defaults.
			errorMessage = _("Errors were found in some of your Studio configuration settings. The affected settings were reset to defaults.")
		SPLConfig.write()
		try:
			runConfigErrorDialog(errorMessage, title)
		except AttributeError:
			pass

# Configuration dialog.
class SPLConfigDialog(gui.SettingsDialog):
	# Translators: This is the label for the StationPlaylist Studio configuration dialog.
	title = _("Studio Add-on Settings")

	def makeSettings(self, settingsSizer):

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: the label for a setting in SPL add-on settings to set status announcement between words and beeps.
		self.beepAnnounceCheckbox=wx.CheckBox(self,wx.NewId(),label=_("&Beep for status announcements"))
		self.beepAnnounceCheckbox.SetValue(SPLConfig["BeepAnnounce"])
		sizer.Add(self.beepAnnounceCheckbox, border=10,flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL Add-on settings to specify end of track (outro) alarm.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&End of track alarm in seconds"))
		sizer.Add(label)
		self.endOfTrackAlarm = wx.SpinCtrl(self, wx.ID_ANY, min=1, max=59)
		self.endOfTrackAlarm.SetValue(long(SPLConfig["EndOfTrackTime"]))
		sizer.Add(self.endOfTrackAlarm)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		# Translators: The label for a setting in SPL Add-on settings to specify track intro alarm.
		label = wx.StaticText(self, wx.ID_ANY, label=_("Track &intro alarm in seconds"))
		sizer.Add(label)
		self.introAlarm = wx.SpinCtrl(self, wx.ID_ANY, min=1, max=9)
		self.introAlarm.SetValue(long(SPLConfig["SongRampTime"]))
		sizer.Add(self.introAlarm)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to control braille timer.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Braille timer:"))
		self.brailleTimerValues=[("off",_("off")),
		# Translators: One of the braille timer settings.
		("outro",_("track ending")),
		("intro",_("track intro")),
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
		SPLConfig["EndOfTrackTime"] = self.endOfTrackAlarm.Value
		SPLConfig["SongRampTime"] = self.introAlarm.Value
		SPLConfig["BrailleTimer"] = self.brailleTimerValues[self.brailleTimerList.GetSelection()][0]
		SPLConfig["MicAlarm"] = self.micAlarm.Value
		SPLConfig["TrackDial"] = self.trackDialCheckbox.Value
		super(SPLConfigDialog,  self).onOk(evt)

# Additional configuration dialogs

# Common alarm dialogs.
# Based on NVDA core's find dialog code (implemented by the author of this add-on).
class SPLAlarmDialog(wx.Dialog):
	"""A dialog providing common alarm settings.
	This dialog contains a number edit field for alarm duration and a check box to enable or disable the alarm.
	"""

	def __init__(self, parent, setting, toggleSetting, title, alarmField, alarmToggle, min, max):
		# Translators: Title of a dialog to find text.
		super(SPLAlarmDialog, self).__init__(parent, wx.ID_ANY, title)
		self.setting = setting
		self.toggleSetting = toggleSetting
		mainSizer = wx.BoxSizer(wx.VERTICAL)

		alarmSizer = wx.BoxSizer(wx.HORIZONTAL)
		alarmMessage = wx.StaticText(self, wx.ID_ANY, label=alarmField)
		alarmSizer.Add(alarmMessage)
		self.alarm= wx.SpinCtrl(self, wx.ID_ANY, min=min, max=max)
		self.alarm.SetValue(SPLConfig[setting])
		alarmSizer.Add(self.alarm)
		mainSizer.Add(alarmSizer,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)
		self.toggleCheckBox=wx.CheckBox(self,wx.NewId(),label=alarmToggle)
		self.toggleCheckBox.SetValue(SPLConfig[toggleSetting])
		mainSizer.Add(self.toggleCheckBox,border=10,flag=wx.BOTTOM)

		mainSizer.AddSizer(self.CreateButtonSizer(wx.OK|wx.CANCEL))
		self.Bind(wx.EVT_BUTTON,self.onOk,id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON,self.onCancel,id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)
		self.alarm.SetFocus()

	def onOk(self, evt):
		# Optimization: don't bother if Studio is dead and if the same value has been entered.
		if user32.FindWindowA("SPLStudio", None):
			newVal = self.alarm.GetValue()
			newToggle = self.toggleCheckBox.GetValue()
			if SPLConfig[self.setting] != newVal: SPLConfig[self.setting] = newVal
			elif SPLConfig[self.toggleSetting] != newToggle: SPLConfig[self.toggleSetting] = newToggle
		print SPLConfig[self.setting]
		self.Destroy()

	def onCancel(self, evt):
		self.Destroy()
