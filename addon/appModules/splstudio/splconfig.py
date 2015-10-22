# SPL Studio Configuration Manager
# An app module and global plugin package for NVDA
# Copyright 2015 Joseph Lee and others, released under GPL.
# Provides the configuration management package for SPL Studio app module.
# For miscellaneous dialogs and tool, see SPLMisc module.

import os
from cStringIO import StringIO
from configobj import ConfigObj
from validate import Validator
import weakref
import globalVars
import ui
import api
import gui
import wx
from winUser import user32
import tones

# Configuration management
SPLIni = os.path.join(globalVars.appArgs.configPath, "splstudio.ini")
SPLProfiles = os.path.join(globalVars.appArgs.configPath, "addons", "stationPlaylist", "profiles")
confspec = ConfigObj(StringIO("""
BeepAnnounce = boolean(default=false)
MessageVerbosity = option("beginner", "advanced", default="beginner")
SayEndOfTrack = boolean(default=true)
EndOfTrackTime = integer(min=1, max=59, default=5)
SaySongRamp = boolean(default=true)
SongRampTime = integer(min=1, max=9, default=5)
BrailleTimer = option("off", "intro", "outro", "both", default="off")
MicAlarm = integer(min=0, max=7200, default="0")
MicAlarmInterval = integer(min=0, max=60, default=0)
AlarmAnnounce = option("beep", "message", "both", default="beep")
LibraryScanAnnounce = option("off", "ending", "progress", "numbers", default="off")
TrackDial = boolean(default=false)
TimeHourAnnounce = boolean(default=false)
MetadataReminder = option("off", "startup", "instant", default="off")
MetadataEnabled = bool_list(default=list(false,false,false,false,false))
UseScreenColumnOrder = boolean(default=true)
ColumnOrder = string_list(default=list("Artist","Title","Duration","Intro","Category","Filename"))
IncludedColumns = string_list(default=list("Artist","Title","Duration","Intro","Category","Filename"))
SayScheduledFor = boolean(default=true)
SayListenerCount = boolean(default=true)
SayPlayingCartName = boolean(default=true)
SPLConPassthrough = boolean(default=false)
CompatibilityLayer = option("off", "jfw", default="off")
"""), encoding="UTF-8", list_values=False)
confspec.newlines = "\r\n"
SPLConfig = None
# A pool of broadcast profiles.
SPLConfigPool = []
# Default config spec container.
_SPLDefaults = ConfigObj(None, configspec = confspec, encoding="UTF-8")
_val = Validator()
_SPLDefaults.validate(_val, copy=True)

# The following settings can be changed in profiles:
_mutatableSettings=("SayEndOfTrack","EndOfTrackTime","SaySongRamp","SongRampTime","MicAlarm","MicAlarmInterval")
# Unlock in 6.1.
#,"MetadataEnabled","UseScreenColumnOrder","ColumnOrder","IncludedColumns")

# Display an error dialog when configuration validation fails.
def runConfigErrorDialog(errorText, errorType):
	wx.CallAfter(gui.messageBox, errorText, errorType, wx.OK|wx.ICON_ERROR)

# Reset settings to defaults.
# This will be called when validation fails or when the user asks for it.
# 6.0: The below function resets a single profile. A sister function will reset all of them.
# 7.0: This will be split into several functions, with one of them being the master copy/settings transfer routine.
def resetConfig(defaults, activeConfig, intentional=False):
	for setting in activeConfig:
		activeConfig[setting] = defaults[setting]
	activeConfig.write()
	if intentional:
		# Translators: A dialog message shown when settings were reset to defaults.
		wx.CallAfter(gui.messageBox, _("Successfully applied default add-on settings."),
		# Translators: Title of the reset config dialog.
		_("Reset configuration"), wx.OK|wx.ICON_INFORMATION)

# Reset all profiles upon request.
def resetAllConfig():
	for profile in SPLConfigPool:
		# Retrieve the profile path, as ConfigObj.reset nullifies it.
		profilePath = profile.filename
		profile.reset()
		profile.filename = profilePath
		for setting in _SPLDefaults:
			profile[setting] = _SPLDefaults[setting]
	# Translators: A dialog message shown when settings were reset to defaults.
	wx.CallAfter(gui.messageBox, _("Successfully applied default add-on settings."),
	# Translators: Title of the reset config dialog.
	_("Reset configuration"), wx.OK|wx.ICON_INFORMATION)

# In case one or more profiles had config issues, look up the error message from the following map.
_configErrors ={
	"completeReset":"All settings reset to defaults",
	"partialReset":"Some settings reset to defaults",
	"columnOrderReset":"Column announcement order reset to defaults",
	"partialAndColumnOrderReset":"Some settings, including column announcement order reset to defaults",
	"noInstantProfile":"Cannot find instant profile"
}

# To be run in app module constructor.
# With the load function below, load the config upon request.
# The below init function is really a vehicle that traverses through config profiles in a loop.
# Prompt the config error dialog only once.
_configLoadStatus = {} # Key = filename, value is pass or no pass.

def initConfig():
	# Load the default config from a list of profiles.
	global SPLConfig, SPLConfigPool, _configLoadStatus, SPLActiveProfile, SPLSwitchProfile
	if SPLConfigPool is None: SPLConfigPool = []
	# Translators: The name of the default (normal) profile.
	if SPLActiveProfile is None: SPLActiveProfile = _("Normal profile")
	SPLConfigPool.append(unlockConfig(SPLIni, profileName=SPLActiveProfile, prefill=True))
	try:
		profiles = filter(lambda fn: os.path.splitext(fn)[-1] == ".ini", os.listdir(SPLProfiles))
		for profile in profiles:
			SPLConfigPool.append(unlockConfig(os.path.join(SPLProfiles, profile), profileName=os.path.splitext(profile)[0]))
	except WindowsError:
		pass
	SPLConfig = SPLConfigPool[0]
	# Locate instant profile.
	if "InstantProfile" in SPLConfig:
		try:
			SPLSwitchProfile = SPLConfigPool[getProfileIndexByName(SPLConfig["InstantProfile"])].name
		except ValueError:
			_configLoadStatus[SPLConfig.name] = "noInstantProfile"
	if len(_configLoadStatus):
		# Translators: Standard error title for configuration error.
		title = _("Studio add-on Configuration error")
		messages = []
		messages.append("One or more broadcast profiles had issues:\n\n")
		for profile in _configLoadStatus:
			error = _configErrors[_configLoadStatus[profile]]
			messages.append("{profileName}: {errorMessage}".format(profileName = profile, errorMessage = error))
		_configLoadStatus.clear()
		runConfigErrorDialog("\n".join(messages), title)

# Unlock (load) profiles from files.
def unlockConfig(path, profileName=None, prefill=False):
	global _configLoadStatus # To be mutated only during unlock routine.
	SPLConfigCheckpoint = ConfigObj(path, configspec = confspec, encoding="UTF-8")
	# 5.2 and later: check to make sure all values are correct.
	configTest = SPLConfigCheckpoint.validate(_val, copy=prefill)
	if configTest != True:
		# Translators: Standard error title for configuration error.
		title = _("Studio add-on Configuration error")
		if not configTest:
			# Case 1: restore settings to defaults when 5.x config validation has failed on all values.
			# 6.0: In case this is a user profile, apply base configuration.
			baseProfile = _SPLDefaults if prefill else SPLConfigPool[0]
			resetConfig(baseProfile, SPLConfigCheckpoint)
			_configLoadStatus[profileName] = "completeReset"
		elif isinstance(configTest, dict):
			# Case 2: For 5.x and later, attempt to reconstruct the failed values.
			# 6.0: Cherry-pick global settings only.
			for setting in configTest:
				if not configTest[setting]:
					if prefill: # Base profile only.
						SPLConfigCheckpoint[setting] = _SPLDefaults[setting]
					else: # Broadcast profiles.
						if setting not in _mutatableSettings:
							SPLConfigCheckpoint[setting] = SPLConfigPool[0][setting]
						else: SPLConfigCheckpoint[setting] = _SPLDefaults[setting]
			SPLConfigCheckpoint.write()
			_configLoadStatus[profileName] = "partialReset"
	# Do this only for base profile.
	if prefill: _extraInitSteps(SPLConfigCheckpoint, profileName=profileName)
	else: _applyBaseSettings(SPLConfigCheckpoint)
	# Unlock in 6.1.
	#if not prefill: _applyBaseSettings(SPLConfigCheckpoint)
	SPLConfigCheckpoint.name = profileName
	return SPLConfigCheckpoint

# Extra initialization steps such as converting value types.
def _extraInitSteps(conf, profileName=None):
	global _configLoadStatus
	columnOrder = conf["ColumnOrder"]
	# Catch suttle errors.
	fields = ["Artist","Title","Duration","Intro","Category","Filename"]
	invalidFields = 0
	for field in fields:
		if field not in columnOrder: invalidFields+=1
	if invalidFields or len(columnOrder) != 6:
		if profileName in _configLoadStatus and _configLoadStatus[profileName] == "partialReset":
			_configLoadStatus[profileName] = "partialAndColumnOrderReset"
		else:
			_configLoadStatus[profileName] = "columnOrderReset"
		columnOrder = fields
	conf["ColumnOrder"] = columnOrder
	conf["IncludedColumns"] = set(conf["IncludedColumns"])
	# Artist and Title must be present at all times (quite redundant, but just in case).
	conf["IncludedColumns"].add("Artist")
	conf["IncludedColumns"].add("Title")
	# Perform a similar check for metadata streaming.
	# Unlock in 6.1.
	"""if len(conf["MetadataEnabled"]) != 5:
		if profileName in _configLoadStatus and _configLoadStatus[profileName] == "partialReset":
			_configLoadStatus[profileName] = "partialAndMetadataReset"
		else:
			_configLoadStatus[profileName] = "metadataReset"
		conf["MetadataEnabled"] = [False, False, False, False, False]"""

# Apply base profile if loading user-defined broadcast profiles.
def _applyBaseSettings(conf):
	for setting in SPLConfigPool[0]:
		# Ignore profile-specific settings.
		if setting not in _mutatableSettings:
			conf[setting] = SPLConfigPool[0][setting]

# Instant profile switch helpers.
# A number of helper functions assisting instatn switch profile routine, including sorting and locating the needed profile upon request.

# Fetch the profile index with a given name.
def getProfileIndexByName(name):
	return [profile.name for profile in SPLConfigPool].index(name)

# And:
def getProfileByName(name):
	return SPLConfigPool[getProfileIndexByName(name)]

# Is the config pool itself sorted?
# This check is performed when displaying broadcast profiles.
def isConfigPoolSorted():
		profileNames = [profile.name for profile in SPLConfigPool][1:]
		for pos in xrange(len(profileNames)-1):
			if profileNames[pos] > profileNames[pos+1]:
				return False
		return True


# Perform some extra work before writing the config file.
def _preSave(conf):
	# 6.1: Transform column inclusion data structure now.
	# Unlock in 6.1.
	#conf["IncludedColumns"] = list(conf["IncludedColumns"])
	# Perform global setting processing only for the normal profile.
	if SPLConfigPool.index(conf) == 0:
		conf["IncludedColumns"] = list(conf["IncludedColumns"])
		# Cache instant profile for later use.
		if SPLSwitchProfile is not None:
			conf["InstantProfile"] = SPLSwitchProfile
		else:
			try:
				del conf["InstantProfile"]
			except KeyError:
				pass
		# 6.0 only: Remove obsolete keys.
		if "MetadataURL" in conf:
			del conf["MetadataURL"]
	# For other profiles, remove global settings before writing to disk.
	else:
		# 6.1: Make sure column order and inclusion aren't same as default values.
		# Unlock in 6.1.
		"""includedColumns = set(_SPLDefaults["IncludedColumns"])
		if conf["IncludedColumns"] == includedColumns:
			del conf["IncludedColumns"]
		if conf["ColumnOrder"] == ["Artist","Title","Duration","Intro","Category","Filename"]:
			del conf["ColumnOrder"]"""
		for setting in conf.keys():
			if setting not in _mutatableSettings or (setting in _mutatableSettings and conf[setting] == _SPLDefaults[setting]):
				del conf[setting]


# Save configuration database.
def saveConfig():
	# Save all config profiles.
	global SPLConfig, SPLConfigPool, SPLActiveProfile, SPLPrevProfile, SPLSwitchProfile
	# Apply any global settings changed in profiles to normal configuration.
	if SPLConfigPool.index(SPLConfig) > 0:
		for setting in SPLConfig:
			if setting not in _mutatableSettings:
				SPLConfigPool[0][setting] = SPLConfig[setting]
	for configuration in SPLConfigPool:
		if configuration is not None:
			_preSave(configuration)
			# Save broadcast profiles first.
			if SPLConfigPool.index(configuration) > 0:
				configuration.write()
	# Global flags, be gone.
	if "Reset" in SPLConfigPool[0]:
		del SPLConfigPool[0]["Reset"]
	SPLConfigPool[0].write()
	SPLConfig = None
	SPLConfigPool = None
	SPLActiveProfile = None
	SPLPrevProfile = None
	SPLSwitchProfile = None

# Switch between profiles.
SPLActiveProfile = None
SPLPrevProfile = None
SPLSwitchProfile = None

# Called from within the app module.
def instantProfileSwitch():
	global SPLPrevProfile, SPLConfig, SPLActiveProfile
	if _configDialogOpened:
		# Translators: Presented when trying to switch to an instant switch profile when add-on settings dialog is active.
		ui.message(_("Add-on settings dialog is open, cannot switch profiles"))
		return
	if SPLSwitchProfile is None:
		# Translators: Presented when trying to switch to an instant switch profile when the instant switch profile is not defined.
		ui.message(_("No instant switch profile is defined"))
	else:
		if SPLPrevProfile is None:
			if SPLActiveProfile == SPLSwitchProfile:
				# Translators: Presented when trying to switch to an instant switch profile when one is already using the instant switch profile.
				ui.message(_("You are already in the instant switch profile"))
				return
			# Switch to the given profile.
			switchProfileIndex = getProfileIndexByName(SPLSwitchProfile)
			SPLPrevProfile = SPLConfigPool.index(SPLConfig)
			SPLConfig = SPLConfigPool[switchProfileIndex]
			# Translators: Presented when switch to instant switch profile was successful.
			ui.message(_("Switching profiles"))
			# Use the focus.appModule's metadata reminder method if told to do so now.
			if SPLConfig["MetadataReminder"] in ("startup", "instant"):
				api.getFocusObject().appModule._metadataAnnouncer(reminder=True)
		else:
			SPLConfig = SPLConfigPool[SPLPrevProfile]
			SPLActiveProfile = SPLConfig.name
			SPLPrevProfile = None
			# Translators: Presented when switching from instant switch profile to a previous profile.
			ui.message(_("Returning to previous profile"))
			# 6.2: Don't forget to switch streaming status around.
			if SPLConfig["MetadataReminder"] in ("startup", "instant"):
				api.getFocusObject().appModule._metadataAnnouncer(reminder=True)


# Configuration dialog.
_configDialogOpened = False

class SPLConfigDialog(gui.SettingsDialog):
	# Translators: This is the label for the StationPlaylist Studio configuration dialog.
	title = _("Studio Add-on Settings")

	def makeSettings(self, settingsSizer):

		# Broadcast profile controls were inspired by Config Profiles dialog in NVDA Core.
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to select a broadcast profile.
		label = wx.StaticText(self, wx.ID_ANY, label=_("Broadcast &profile:"))
		# Sort profiles for display purposes (the config pool might not be sorted).
		sortedProfiles = [profile.name for profile in SPLConfigPool]
		# No need to sort if the only living profile is the normal configuration or there is one other profile besides this.
		# Optimization: Only sort if config pool itself isn't  - usually after creating, renaming or deleting profile(s).
		if len(sortedProfiles) > 2 and not isConfigPoolSorted():
			firstProfile = SPLConfigPool[0].name
			sortedProfiles = [firstProfile] + sorted(sortedProfiles[1:])
		self.profiles = wx.Choice(self, wx.ID_ANY, choices=sortedProfiles)
		self.profiles.Bind(wx.EVT_CHOICE, self.onProfileSelection)
		try:
			self.profiles.SetSelection(sortedProfiles.index(SPLConfig.name))
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.profiles)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		# Profile controls code credit: NV Access (except copy button).
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label of a button to create a new broadcast profile.
		item = newButton = wx.Button(self, label=_("&New"))
		item.Bind(wx.EVT_BUTTON, self.onNew)
		sizer.Add(item)
		# Translators: The label of a button to copy a broadcast profile.
		item = copyButton = wx.Button(self, label=_("Cop&y"))
		item.Bind(wx.EVT_BUTTON, self.onCopy)
		sizer.Add(item)
		# Translators: The label of a button to rename a broadcast profile.
		item = self.renameButton = wx.Button(self, label=_("&Rename"))
		item.Bind(wx.EVT_BUTTON, self.onRename)
		sizer.Add(item)
		# Translators: The label of a button to delete a broadcast profile.
		item = self.deleteButton = wx.Button(self, label=_("&Delete"))
		item.Bind(wx.EVT_BUTTON, self.onDelete)
		sizer.Add(item)
		# Translators: The label of a button to toggle instant profile switching on and off.
		if SPLSwitchProfile is None: switchLabel = _("Enable instant profile switching")
		else:
			# Translators: The label of a button to toggle instant profile switching on and off.
			switchLabel = _("Disable instant profile switching")
		item = self.instantSwitchButton = wx.Button(self, label=switchLabel)
		item.Bind(wx.EVT_BUTTON, self.onInstantSwitch)
		self.switchProfile = SPLSwitchProfile
		self.activeProfile = SPLActiveProfile
		# Used as sanity check in case switch profile is renamed or deleted.
		self.switchProfileRenamed = False
		self.switchProfileDeleted = False
		sizer.Add(item)
		if SPLConfigPool.index(SPLConfig) == 0:
			self.renameButton.Disable()
			self.deleteButton.Disable()
			self.instantSwitchButton.Disable()
		settingsSizer.Add(sizer)

	# Translators: the label for a setting in SPL add-on settings to set status announcement between words and beeps.
		self.beepAnnounceCheckbox=wx.CheckBox(self,wx.NewId(),label=_("&Beep for status announcements"))
		self.beepAnnounceCheckbox.SetValue(SPLConfig["BeepAnnounce"])
		settingsSizer.Add(self.beepAnnounceCheckbox, border=10,flag=wx.TOP)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to set message verbosity.
		label = wx.StaticText(self, wx.ID_ANY, label=_("Message &verbosity:"))
		# Translators: One of the message verbosity levels.
		self.verbosityLevels=[("beginner",_("beginner")),
		# Translators: One of the message verbosity levels.
		("advanced",_("advanced"))]
		self.verbosityList = wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.verbosityLevels])
		currentVerbosity=SPLConfig["MessageVerbosity"]
		selection = (x for x,y in enumerate(self.verbosityLevels) if y[0]==currentVerbosity).next()  
		try:
			self.verbosityList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.verbosityList)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

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
		self.endOfTrackAlarm.SetSelection(-1, -1)
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
		self.songRampAlarm.SetSelection(-1, -1)
		self.introSizer.Add(self.songRampAlarm)
		self.onIntroCheck(None)
		settingsSizer.Add(self.introSizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to control braille timer.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Braille timer:"))
		self.brailleTimerValues=[("off",_("Off")),
		# Translators: One of the braille timer settings.
		("outro",_("Track ending")),
		# Translators: One of the braille timer settings.
		("intro",_("Track intro")),
		# Translators: One of the braille timer settings.
		("both",_("Track intro and ending"))]
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

		self.micSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL Add-on settings to change microphone alarm setting.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Microphone alarm in seconds"))
		self.micSizer.Add(label)
		self.micAlarm = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=7200)
		self.micAlarm.SetValue(long(SPLConfig["MicAlarm"]))
		self.micAlarm.SetSelection(-1, -1)
		self.micSizer.Add(self.micAlarm)

		# Translators: The label for a setting in SPL Add-on settings to specify mic alarm interval.
		self.micAlarmIntervalLabel = wx.StaticText(self, wx.ID_ANY, label=_("Microphone alarm &interval in seconds"))
		self.micSizer.Add(self.micAlarmIntervalLabel)
		self.micAlarmInterval = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=60)
		self.micAlarmInterval.SetValue(long(SPLConfig["MicAlarmInterval"]))
		self.micAlarmInterval.SetSelection(-1, -1)
		self.micSizer.Add(self.micAlarmInterval)
		settingsSizer.Add(self.micSizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to control alarm announcement type.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Alarm notification:"))
		# Translators: One of the alarm notification options.
		self.alarmAnnounceValues=[("beep",_("beep")),
		# Translators: One of the alarm notification options.
		("message",_("message")),
		# Translators: One of the alarm notification options.
		("both",_("both beep and message"))]
		self.alarmAnnounceList = wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.alarmAnnounceValues])
		alarmAnnounceCurValue=SPLConfig["AlarmAnnounce"]
		selection = (x for x,y in enumerate(self.alarmAnnounceValues) if y[0]==alarmAnnounceCurValue).next()  
		try:
			self.alarmAnnounceList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.alarmAnnounceList)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to control library scan announcement.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Library scan announcement:"))
		self.libScanValues=[("off",_("Off")),
		# Translators: One of the library scan announcement settings.
		("ending",_("Start and end only")),
		# Translators: One of the library scan announcement settings.
		("progress",_("Scan progress")),
		# Translators: One of the library scan announcement settings.
		("numbers",_("Scan count"))]
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

		self.hourAnnounceCheckbox=wx.CheckBox(self,wx.NewId(),label="Include &hours when announcing track or playlist duration")
		self.hourAnnounceCheckbox.SetValue(SPLConfig["TimeHourAnnounce"])
		settingsSizer.Add(self.hourAnnounceCheckbox, border=10,flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to toggle track dial mode on and off.
		self.trackDialCheckbox=wx.CheckBox(self,wx.NewId(),label=_("&Track Dial mode"))
		self.trackDialCheckbox.SetValue(SPLConfig["TrackDial"])
		settingsSizer.Add(self.trackDialCheckbox, border=10,flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: the label for a setting in SPL add-on settings to be notified that metadata streaming is enabled.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Metadata streaming notification and connection"))
		self.metadataValues=[("off",_("Off")),
		# Translators: One of the metadata notification settings.
		("startup",_("When Studio starts")),
		# Translators: One of the metadata notification settings.
		("instant",_("When instant switch profile is active"))]
		self.metadataList = wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.metadataValues])
		metadataCurValue=SPLConfig["MetadataReminder"]
		selection = (x for x,y in enumerate(self.metadataValues) if y[0]==metadataCurValue).next()  
		try:
			self.metadataList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.metadataList)
		self.metadataStreams = SPLConfig["MetadataEnabled"]
		# Translators: The label of a button to manage column announcements.
		item = manageMetadataButton = wx.Button(self, label=_("Configure metadata &streaming connection options..."))
		item.Bind(wx.EVT_BUTTON, self.onManageMetadata)
		sizer.Add(item)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to toggle custom column announcement.
		self.columnOrderCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Announce columns in the &order shown on screen"))
		self.columnOrderCheckbox.SetValue(SPLConfig["UseScreenColumnOrder"])
		self.columnOrder = SPLConfig["ColumnOrder"]
		self.includedColumns = SPLConfig["IncludedColumns"]
		settingsSizer.Add(self.columnOrderCheckbox, border=10,flag=wx.BOTTOM)
		# Translators: The label of a button to manage column announcements.
		item = manageColumnsButton = wx.Button(self, label=_("&Manage track column announcements..."))
		item.Bind(wx.EVT_BUTTON, self.onManageColumns)
		settingsSizer.Add(item)

		# Translators: the label for a setting in SPL add-on settings to announce scheduled time.
		self.scheduledForCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Announce &scheduled time for the selected track"))
		self.scheduledForCheckbox.SetValue(SPLConfig["SayScheduledFor"])
		settingsSizer.Add(self.scheduledForCheckbox, border=10,flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to announce listener count.
		self.listenerCountCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Announce &listener count"))
		self.listenerCountCheckbox.SetValue(SPLConfig["SayListenerCount"])
		settingsSizer.Add(self.listenerCountCheckbox, border=10,flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to announce currently playing cart.
		self.cartNameCheckbox=wx.CheckBox(self,wx.NewId(),label=_("&Announce name of the currently playing cart"))
		self.cartNameCheckbox.SetValue(SPLConfig["SayPlayingCartName"])
		settingsSizer.Add(self.cartNameCheckbox, border=10,flag=wx.BOTTOM)

		# Translators: The label of a button to open advanced options such as using SPL Controller command to invoke Assistant layer.
		item = advancedOptButton = wx.Button(self, label=_("&Advanced options..."))
		item.Bind(wx.EVT_BUTTON, self.onAdvancedOptions)
		self.splConPassthrough = SPLConfig["SPLConPassthrough"]
		self.compLayer = SPLConfig["CompatibilityLayer"]
		settingsSizer.Add(item)

		# Translators: The label for a button in SPL add-on configuration dialog to reset settings to defaults.
		self.resetConfigButton = wx.Button(self, wx.ID_ANY, label=_("Reset settings"))
		self.resetConfigButton.Bind(wx.EVT_BUTTON,self.onResetConfig)
		settingsSizer.Add(self.resetConfigButton)

	def postInit(self):
		global _configDialogOpened
		_configDialogOpened = True
		self.profiles.SetFocus()

	def onOk(self, evt):
		global SPLConfig, SPLActiveProfile, _configDialogOpened, SPLSwitchProfile, SPLPrevProfile
		selectedProfile = self.profiles.GetStringSelection()
		SPLConfig = getProfileByName(selectedProfile)
		SPLConfig["BeepAnnounce"] = self.beepAnnounceCheckbox.Value
		SPLConfig["MessageVerbosity"] = self.verbosityLevels[self.verbosityList.GetSelection()][0]
		SPLConfig["SayEndOfTrack"] = self.outroCheckBox.Value
		SPLConfig["EndOfTrackTime"] = self.endOfTrackAlarm.Value
		SPLConfig["SaySongRamp"] = self.introCheckBox.Value
		SPLConfig["SongRampTime"] = self.songRampAlarm.Value
		SPLConfig["BrailleTimer"] = self.brailleTimerValues[self.brailleTimerList.GetSelection()][0]
		SPLConfig["MicAlarm"] = self.micAlarm.Value
		SPLConfig["MicAlarmInterval"] = self.micAlarmInterval.Value
		SPLConfig["AlarmAnnounce"] = self.alarmAnnounceValues[self.alarmAnnounceList.GetSelection()][0]
		SPLConfig["LibraryScanAnnounce"] = self.libScanValues[self.libScanList.GetSelection()][0]
		SPLConfig["TimeHourAnnounce"] = self.hourAnnounceCheckbox.Value
		SPLConfig["TrackDial"] = self.trackDialCheckbox.Value
		SPLConfig["MetadataReminder"] = self.metadataValues[self.metadataList.GetSelection()][0]
		SPLConfig["MetadataEnabled"] = self.metadataStreams
		SPLConfig["UseScreenColumnOrder"] = self.columnOrderCheckbox.Value
		SPLConfig["ColumnOrder"] = self.columnOrder
		SPLConfig["IncludedColumns"] = self.includedColumns
		SPLConfig["SayScheduledFor"] = self.scheduledForCheckbox.Value
		SPLConfig["SayListenerCount"] = self.listenerCountCheckbox.Value
		SPLConfig["SayPlayingCartName"] = self.cartNameCheckbox.Value
		SPLConfig["SPLConPassthrough"] = self.splConPassthrough
		SPLConfig["CompatibilityLayer"] = self.compLayer
		SPLActiveProfile = SPLConfig.name
		SPLSwitchProfile = self.switchProfile
		# Without nullifying prev profile while switch profile is undefined, NVDA will assume it can switch back to that profile when it can't.
		# It also causes NVDA to display wrong label for switch button.
		if self.switchProfile is None:
			SPLPrevProfile = None
		_configDialogOpened = False
		super(SPLConfigDialog,  self).onOk(evt)

	def onCancel(self, evt):
		global _configDialogOpened, SPLActiveProfile, SPLSwitchProfile, SPLConfig
		SPLActiveProfile = self.activeProfile
		if self.switchProfileRenamed or self.switchProfileDeleted:
			SPLSwitchProfile = self.switchProfile
		if self.switchProfileDeleted:
			SPLConfig = SPLConfigPool[0]
		_configDialogOpened = False
		super(SPLConfigDialog,  self).onCancel(evt)

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

	# Load settings from profiles.
	def onProfileSelection(self, evt):
		# Don't rely on SPLConfig here, as we don't want to interupt the show.
		selection = self.profiles.GetSelection()
		selectedProfile = self.profiles.GetStringSelection()
		# Play a tone to indicate active profile.
		if SPLActiveProfile == selectedProfile:
			tones.beep(512, 40)
		if selection == 0:
			self.renameButton.Disable()
			self.deleteButton.Disable()
			self.instantSwitchButton.Disable()
		else:
			self.renameButton.Enable()
			self.deleteButton.Enable()
			if selectedProfile != self.switchProfile:
				self.instantSwitchButton.Label = _("Enable instant profile switching")
			else:
				self.instantSwitchButton.Label = _("Disable instant profile switching")
			self.instantSwitchButton.Enable()
		curProfile = getProfileByName(selectedProfile)
		self.outroCheckBox.SetValue(curProfile["SayEndOfTrack"])
		self.endOfTrackAlarm.SetValue(long(curProfile["EndOfTrackTime"]))
		self.onOutroCheck(None)
		self.introCheckBox.SetValue(curProfile["SaySongRamp"])
		self.songRampAlarm.SetValue(long(curProfile["SongRampTime"]))
		self.onIntroCheck(None)
		self.micAlarm.SetValue(long(curProfile["MicAlarm"]))
		self.micAlarmInterval.SetValue(long(curProfile["MicAlarmInterval"]))
		# 6.1: Take care of profile-specific column and metadata settings.
		# Unlock in 6.1.
		"""self.metadataStreams = curProfile["MetadataEnabled"]
		self.columnOrderCheckbox.SetValue(curProfile["UseScreenColumnOrder"])
		self.columnOrder = curProfile["ColumnOrder"]
		self.includedColumns = curProfile["IncludedColumns"]"""

	# Profile controls.
	# Rename and delete events come from GUI/config profiles dialog from NVDA core.
	def onNew(self, evt):
		self.Disable()
		NewProfileDialog(self).Show()

	def onCopy(self, evt):
		self.Disable()
		NewProfileDialog(self, copy=True).Show()

	def onRename(self, evt):
		global SPLConfigPool
		oldName = self.profiles.GetStringSelection()
		index = self.profiles.Selection
		configPos = getProfileIndexByName(oldName)
		# Translators: The label of a field to enter a new name for a broadcast profile.
		with wx.TextEntryDialog(self, _("New name:"),
				# Translators: The title of the dialog to rename a profile.
				_("Rename Profile"), defaultValue=oldName) as d:
			if d.ShowModal() == wx.ID_CANCEL:
				return
			newName = api.filterFileName(d.Value)
		if oldName == newName: return
		newNamePath = newName + ".ini"
		newProfile = os.path.join(SPLProfiles, newNamePath)
		if oldName.lower() != newName.lower() and os.path.isfile(newProfile):
			# Translators: An error displayed when renaming a configuration profile
			# and a profile with the new name already exists.
			gui.messageBox(_("That profile already exists. Please choose a different name."),
				_("Error"), wx.OK | wx.ICON_ERROR, self)
			return
		oldNamePath = oldName + ".ini"
		oldProfile = os.path.join(SPLProfiles, oldNamePath)
		os.rename(oldProfile, newProfile)
		if self.switchProfile == oldName:
			self.switchProfile = newName
			self.switchProfileRenamed = True
		if self.activeProfile == oldName:
			self.activeProfile = newName
		SPLConfigPool[configPos].name = newName
		SPLConfigPool[configPos].filename = newProfile
		self.profiles.SetString(index, newName)
		self.profiles.Selection = index
		self.profiles.SetFocus()

	def onDelete(self, evt):
		index = self.profiles.Selection
		name = self.profiles.GetStringSelection()
		configPos = getProfileIndexByName(name)
		if gui.messageBox(
			# Translators: The confirmation prompt displayed when the user requests to delete a broadcast profile.
			_("Are you sure you want to delete this profile? This cannot be undone."),
			# Translators: The title of the confirmation dialog for deletion of a profile.
			_("Confirm Deletion"),
			wx.YES | wx.NO | wx.ICON_QUESTION, self
		) == wx.NO:
			return
		global SPLConfigPool, SPLSwitchProfile, SPLPrevProfile
		path = SPLConfigPool[configPos].filename
		del SPLConfigPool[configPos]
		try:
			os.remove(path)
		except WindowsError:
			pass
		if name == self.switchProfile or name == self.activeProfile:
			self.switchProfile = None
			SPLPrevProfile = None
			self.switchProfileDeleted = True
		self.profiles.Delete(index)
		self.profiles.SetString(0, SPLConfigPool[0].name)
		self.activeProfile = SPLConfigPool[0].name
		self.profiles.Selection = 0
		self.onProfileSelection(None)
		self.profiles.SetFocus()

	def onInstantSwitch(self, evt):
		selection = self.profiles.GetSelection()
		selectedName = self.profiles.GetStringSelection()
		if self.switchProfile is None or (selectedName != self.switchProfile):
			self.instantSwitchButton.Label = _("Disable instant profile switching")
			self.switchProfile = selectedName
			tones.beep(1000, 500)
		else:
			self.instantSwitchButton.Label = _("Enable instant profile switching")
			self.switchProfile = None
			tones.beep(500, 500)

	# Manage metadata streaming.
	def onManageMetadata(self, evt):
		self.Disable()
		MetadataStreamingDialog(self).Show()

	# Manage column announcements.
	def onManageColumns(self, evt):
		self.Disable()
		ColumnAnnouncementsDialog(self).Show()

	# Advanced options.
	# See advanced options class for more details.
	def onAdvancedOptions(self, evt):
		self.Disable()
		AdvancedOptionsDialog(self).Show()

	# Reset settings to defaults.
	# This affects the currently selected profile.
	def onResetConfig(self, evt):
		if gui.messageBox(
		# Translators: A message to warn about resetting SPL config settings to factory defaults.
		_("Are you sure you wish to reset SPL add-on settings to defaults?"),
		# Translators: The title of the warning dialog.
		_("Warning"),wx.YES_NO|wx.NO_DEFAULT|wx.ICON_WARNING,self
		)==wx.YES:
			# Reset all profiles.
			resetAllConfig()
			global SPLConfig, SPLActiveProfile, _configDialogOpened, SPLSwitchProfile, SPLPrevProfile
			SPLConfig = SPLConfigPool[0]
			SPLActiveProfile = SPLConfig.name
			# Workaround: store the reset flag in the normal profile to prevent config databases from becoming references to old generation.
			SPLConfig["Reset"] = True
		if SPLSwitchProfile is not None:
			SPLSwitchProfile = None
		SPLPrevProfile = None
		_configDialogOpened = False
		self.Destroy()


# Open the above dialog upon request.
def onConfigDialog(evt):
	# 5.2: Guard against alarm dialogs.
	if _alarmDialogOpened:
		# Translators: Presented when an alarm dialog is opened.
		wx.CallAfter(gui.messageBox, _("An alarm dialog is already opened. Please close the alarm dialog first."), _("Error"), wx.OK|wx.ICON_ERROR)
	else: gui.mainFrame._popupSettingsDialog(SPLConfigDialog)

# Helper dialogs for add-on settings dialog.

# New broadcast profile dialog: Modification of new config profile dialog from NvDA Core.
class NewProfileDialog(wx.Dialog):

	def __init__(self, parent, copy=False):
		self.copy = copy
		if not self.copy:
			# Translators: The title of the dialog to create a new broadcast profile.
			dialogTitle = _("New Profile")
		else:
			# Translators: The title of the dialog to copy a broadcast profile.
			dialogTitle = _("Copy Profile")
		super(NewProfileDialog, self).__init__(parent, title=dialogTitle)
		mainSizer = wx.BoxSizer(wx.VERTICAL)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label of a field to enter the name of a new broadcast profile.
		sizer.Add(wx.StaticText(self, label=_("Profile name:")))
		item = self.profileName = wx.TextCtrl(self)
		sizer.Add(item)
		mainSizer.Add(sizer)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to select a base  profile for copying.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Base profile:"))
		self.baseProfiles = wx.Choice(self, wx.ID_ANY, choices=parent.profiles.GetItems())
		try:
			self.baseProfiles.SetSelection(self.baseProfiles.GetItems().index(parent.profiles.GetStringSelection()))
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.baseProfiles)
		if not self.copy:
			sizer.Hide(label)
			sizer.Hide(self.baseProfiles)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		mainSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.profileName.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		global SPLConfigPool
		profileNames = [profile.name for profile in SPLConfigPool]
		name = api.filterFileName(self.profileName.Value)
		if not name:
			return
		if name in profileNames:
			# Translators: An error displayed when the user attempts to create a profile which already exists.
			gui.messageBox(_("That profile already exists. Please choose a different name."),
				_("Error"), wx.OK | wx.ICON_ERROR, self)
			return
		namePath = name + ".ini"
		if not os.path.exists(SPLProfiles):
			os.mkdir(SPLProfiles)
		newProfilePath = os.path.join(SPLProfiles, namePath)
		SPLConfigPool.append(unlockConfig(newProfilePath, profileName=name))
		if self.copy:
			newProfile = SPLConfigPool[-1]
			baseProfile = getProfileByName(self.baseProfiles.GetStringSelection())
			for setting in baseProfile:
				try:
					# Go through all settings (including profile-specific ones for now).
					# 6.1/7.0: Only iterate through mutatable keys.
					if baseProfile[setting] != newProfile[setting]:
						newProfile[setting] = baseProfile[setting]
				except KeyError:
					pass
		parent = self.Parent
		parent.profiles.Append(name)
		parent.profiles.Selection = parent.profiles.Count - 1
		parent.onProfileSelection(None)
		parent.profiles.SetFocus()
		parent.Enable()
		self.Destroy()
		return

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()

# Metadata reminder controller.
# Select notification/streaming URL's for metadata streaming.
_metadataDialogOpened = False

class MetadataStreamingDialog(wx.Dialog):
	"""A dialog to toggle metadata streaming quickly and from add-on settings dialog.
	"""
	_instance = None

	def __new__(cls, parent, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _metadataDialogOpened:
			raise RuntimeError("An instance of metadata stremaing dialog is opened")
		inst = cls._instance() if cls._instance else None
		if not inst:
			return super(cls, cls).__new__(cls, parent, *args, **kwargs)
		return inst

	def __init__(self, parent, func=None):
		inst = MetadataStreamingDialog._instance() if MetadataStreamingDialog._instance else None
		if inst:
			return
		# Use a weakref so the instance can die.
		MetadataStreamingDialog._instance = weakref.ref(self)

		super(MetadataStreamingDialog, self).__init__(parent, title=_("Metadata streaming options"))
		self.func = func

		# WX's CheckListBox isn't user friendly.
		# Therefore use checkboxes laid out across the top.
		self.checkedStreams = []
		# Add the DSP encoder checkbox first before adding other URL's.
		checkedDSP=wx.CheckBox(self,wx.NewId(),label="DSP encoder")
		if func:
			streaming = func(0, 36, ret=True)
			if streaming == -1: streaming += 1
			checkedDSP.SetValue(streaming)
		else: checkedDSP.SetValue(SPLConfig["MetadataEnabled"][0])
		self.checkedStreams.append(checkedDSP)
		# Now the rest.
		for url in xrange(1, 5):
			checkedURL=wx.CheckBox(self,wx.NewId(),label="URL {URL}".format(URL = url))
			if func:
				streaming = func(url, 36, ret=True)
				if streaming == -1: streaming += 1
				checkedURL.SetValue(streaming)
			else: checkedURL.SetValue(SPLConfig["MetadataEnabled"][url])
			self.checkedStreams.append(checkedURL)

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		# First, a help text.
		if func is None: labelText=_("Select the URL for metadata streaming upon request.")
		else: labelText=_("Check to enable metadata streaming, uncheck to disable.")
		label = wx.StaticText(self, wx.ID_ANY, label=labelText)
		mainSizer.Add(label,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		for checkedStream in self.checkedStreams:
			sizer.Add(checkedStream)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		if self.func is not None:
			self.applyCheckbox=wx.CheckBox(self,wx.NewId(),label="&Apply streaming changes to the selected profile")
			self.applyCheckbox.SetValue(SPLConfig["BeepAnnounce"])
			mainSizer.Add(self.applyCheckbox, border=10,flag=wx.TOP)

		mainSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.checkedStreams[0].SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		global _metadataDialogOpened
		if self.func is None: parent = self.Parent
		metadataEnabled = []
		for url in xrange(5):
			if self.func is None: parent.metadataStreams[url] = self.checkedStreams[url].Value
			else:
				dataLo = 0x00010000 if self.checkedStreams[url].Value else 0xffff0000
				self.func(dataLo | url, 36)
				if self.applyCheckbox.Value: metadataEnabled.append(self.checkedStreams[url].Value)
		if self.func is None:
			parent.profiles.SetFocus()
			parent.Enable()
		else:
			# 6.1: Store just toggled settings to profile if told to do so.
			if len(metadataEnabled): SPLConfig["MetadataEnabled"] = metadataEnabled
		self.Destroy()
		_metadataDialogOpened = False
		return

	def onCancel(self, evt):
		global _metadataDialogOpened
		if self.func is None: self.Parent.Enable()
		self.Destroy()
		_metadataDialogOpened = False

# Column announcement manager.
# Select which track columns should be announced and in which order.
class ColumnAnnouncementsDialog(wx.Dialog):

	def __init__(self, parent):
		super(ColumnAnnouncementsDialog, self).__init__(parent, title=_("Manage column announcements"))

		# Same as metadata dialog (wx.CheckListBox isn't user friendly).
		# Gather values for checkboxes except artist and title.
		self.checkedColumns = []
		for column in ("Duration", "Intro", "Category", "Filename"):
			checkedColumn=wx.CheckBox(self,wx.NewId(),label=column)
			checkedColumn.SetValue(column in SPLConfig["IncludedColumns"])
			self.checkedColumns.append(checkedColumn)

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		# First, a help text.
		label = wx.StaticText(self, wx.ID_ANY, label=_("Select columns to be announced (artist and title are announced by default"))
		mainSizer.Add(label,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		for checkedColumn in self.checkedColumns:
			sizer.Add(checkedColumn)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to select a base  profile for copying.
		label = wx.StaticText(self, wx.ID_ANY, label=_("Column &order:"))
		# WXPython Phoenix contains RearrangeList to allow item orders to be changed automatically.
		# Because WXPython Classic doesn't include this, work around by using a variant of list box and move up/down buttons.
		self.trackColumns= wx.ListBox(self, wx.ID_ANY, choices=parent.columnOrder)
		self.trackColumns.Bind(wx.EVT_LISTBOX,self.onColumnSelection)
		try:
			self.trackColumns.SetSelection(0)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.trackColumns)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a button in SPL add-on configuration dialog to reset settings to defaults.
		self.upButton = wx.Button(self, wx.ID_ANY, label=_("Move &up"))
		self.upButton.Bind(wx.EVT_BUTTON,self.onMoveUp)
		self.upButton.Disable()
		sizer.Add(self.upButton)
				# Translators: The label for a button in SPL add-on configuration dialog to reset settings to defaults.
		self.dnButton = wx.Button(self, wx.ID_ANY, label=_("Move &down"))
		self.dnButton.Bind(wx.EVT_BUTTON,self.onMoveDown)
		sizer.Add(self.dnButton)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		mainSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.checkedColumns[0].SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		parent.columnOrder = self.trackColumns.GetItems()
		# Make sure artist and title are always included.
		parent.includedColumns.add("Artist")
		parent.includedColumns.add("Title")
		for checkbox in self.checkedColumns:
			action = parent.includedColumns.add if checkbox.Value else parent.includedColumns.remove
			action(checkbox.Label)
		parent.profiles.SetFocus()
		parent.Enable()
		self.Destroy()
		return

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()

	def onColumnSelection(self, evt):
		selIndex = self.trackColumns.GetSelection()
		self.upButton.Disable() if selIndex == 0 else self.upButton.Enable()
		if selIndex == self.trackColumns.GetCount()-1:
			self.dnButton.Disable()
		else: self.dnButton.Enable()

	def onMoveUp(self, evt):
		tones.beep(1000, 200)
		selIndex = self.trackColumns.GetSelection()
		if selIndex > 0:
			selItem = self.trackColumns.GetString(selIndex)
			self.trackColumns.Delete(selIndex)
			self.trackColumns.Insert(selItem, selIndex-1)
			self.trackColumns.Select(selIndex-1)
			self.onColumnSelection(None)

	def onMoveDown(self, evt):
		tones.beep(500, 200)
		selIndex = self.trackColumns.GetSelection()
		if selIndex < self.trackColumns.GetCount()-1:
			selItem = self.trackColumns.GetString(selIndex)
			self.trackColumns.Delete(selIndex)
			self.trackColumns.Insert(selItem, selIndex+1)
			self.trackColumns.Select(selIndex+1)
			self.onColumnSelection(None)
			# Hack: Wen the last item is selected, forcefully move the focus to "move up" button.
			# This will cause NVDA to say "unavailable" as focus is lost momentarily. A bit anoying but a necessary hack.
			if self.FindFocus().GetId() == wx.ID_OK:
				self.upButton.SetFocus()

# Advanced options
# This dialog houses advanced options such as using SPL Controller command to invoke SPL Assistant.
# More options will be added in Project Rainbow.
class AdvancedOptionsDialog(wx.Dialog):

	def __init__(self, parent):
		super(AdvancedOptionsDialog, self).__init__(parent, title=_("Advanced options"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: A checkbox to toggle if SPL Controller command can be used to invoke Assistant layer.
		self.splConPassthroughCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Allow SPL C&ontroller command to invoke SPL Assistant layer"))
		self.splConPassthroughCheckbox.SetValue(SPLConfig["SPLConPassthrough"])
		sizer.Add(self.splConPassthroughCheckbox, border=10,flag=wx.TOP)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		self.compLayerCheckbox=wx.CheckBox(self,wx.NewId(),label="Screen &reader compatibility Mode (experimental)")
		# Project Rainbow: change the UI for this control.
		self.compLayerCheckbox.SetValue(SPLConfig["CompatibilityLayer"] != "off")
		sizer.Add(self.compLayerCheckbox, border=10,flag=wx.TOP)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		mainSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.splConPassthroughCheckbox.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		parent.splConPassthrough = self.splConPassthroughCheckbox.Value
		comp = "jfw" if self.compLayerCheckbox.Value else "off"
		parent.compLayer = comp
		parent.profiles.SetFocus()
		parent.Enable()
		self.Destroy()
		return

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()

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
		self.alarmEntry.SetSelection(-1, -1)
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

# Message verbosity pool.
# To be moved to its own module in add-on 7.0.
# This is a multimap, consisting of category, value and message.
# Most of the categories are same as confspec keys, hence the below message function is invoked when settings are changed.
def message(category, value):
	verbosityLevels = ("beginner", "advanced")
	ui.message(messagePool[category][value][verbosityLevels.index(SPLConfig["MessageVerbosity"])])

messagePool={
	"BeepAnnounce":
		{True:
			# Translators: Reported when status announcement is set to beeps in SPL Studio.
			(_("Status announcement beeps"),
			# Translators: Reported when status announcement is set to beeps in SPL Studio.
			_("Beeps")),
		False:
			# Translators: Reported when status announcement is set to beeps in SPL Studio.
			(_("Status announcement words"),
			# Translators: Reported when status announcement is set to beeps in SPL Studio.
			_("Words"))},
	"BrailleTimer":
		{"off":
			# Translators: A setting in braille timer options.
			(_("Braille timer off"), _("Off")),
		"outro":
			# Translators: A setting in braille timer options.
			(_("Braille track endings"),
						# Translators: A setting in braille timer options.
			_("Outro")),
		"intro":
			# Translators: A setting in braille timer options.
			(_("Braille intro endings"),
						# Translators: A setting in braille timer options.
			_("Intro")),
		"both":
			# Translators: A setting in braille timer options.
			(_("Braille intro and track endings"),
						# Translators: A setting in braille timer options.
			_("Both"))},
	"LibraryScanAnnounce":
		{"off":
			# Translators: A setting in library scan announcement options.
			(_("Do not announce library scans"), _("Off")),
		"ending":
			# Translators: A setting in library scan announcement options.
			(_("Announce start and end of a library scan"),
			_("Start and end only")),
		"progress":
			# Translators: A setting in library scan announcement options.
			(_("Announce the progress of a library scan"),
			_("Scan progress")),
		"numbers":
			# Translators: A setting in library scan announcement options.
			(_("Announce progress and item count of a library scan"),
			_("Scan count"))}}
