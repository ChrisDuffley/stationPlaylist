# SPL Studio Configuration Manager
# An app module and global plugin package for NVDA
# Copyright 2015-2025 Joseph Lee, released under GPL.
# Provides the configuration management package for SPL Studio app module.
# For miscellaneous dialogs and tool, see SPLMisc module.
# For UI surrounding this module, see splconfui module.
# For the add-on settings specification, see splconfspec module.

from typing import Any
import os
import pickle
from collections import ChainMap
import weakref
import appModuleHandler
from configobj import ConfigObj, get_extra_values, ConfigObjError
from configobj.validate import Validator
import config
import globalVars
import ui
import gui
import wx
from logHandler import log
from . import splactions
from .splconfspec import confspec
import addonHandler
from ..skipTranslation import translate

addonHandler.initTranslation()

# Configuration management
SPLIni = os.path.join(globalVars.appArgs.configPath, "splstudio.ini")
SPLProfiles = os.path.join(globalVars.appArgs.configPath, "addons", "stationPlaylist", "profiles")
# The following settings can be changed in profiles:
_mutatableSettings = ("IntroOutroAlarms", "MicrophoneAlarm", "MetadataStreaming", "ColumnAnnouncement")
confspecprofiles = {sect: key for sect, key in confspec.items() if sect in _mutatableSettings}
# Translators: The name of the default (normal) profile.
defaultProfileName = _("Normal profile")
# StationPlaylist components.
_SPLComponents_ = ("splstudio", "splcreator", "tracktool", "splremotevt")
# In case one or more profiles had config issues, look up the error message from the following map.
_configErrors = {
	"fileReset": "Settings reset to defaults due to configuration file coruption",
	"completeReset": "All settings reset to defaults",
	"partialReset": "Some settings reset to defaults",
	"columnOrderReset": "Column announcement order reset to defaults",
	"partialAndColumnOrderReset": "Some settings, including column announcement order reset to defaults",
	"noInstantProfile": "Cannot find instant profile",
}

# Record config error status for profiles if any.
_configLoadStatus: dict[str, str] = {}  # Key = filename, value is pass or no pass.


# Run-time config storage and management will use ConfigHub data structure, a subclass of chain map.
# A chain map allows a dictionary to look up predefined mappings to locate a key.
# When mutating a value, chain map defaults to using the topmost (zeroth) map,
# which isn't desirable if one wishes to use a specific map.
# This also introduces a problem whereby new key/value pairs are created
# (highly undesirable if global settings are modified via scripts).
# Therefore the ConfigHub subclass modifies item getter/setter
# to give favorable treatment to the currently active "map" (broadcast profile in use),
# with a flag indicating the name of the currently active map.
# Using chain map also simplifies profile switching routine,
# as all that is needed is moving the active map flag around.
# Finally, because this is a class, additional methods and properties are used, which frees the config map
# from the burden of carrying global flags such as the name of the instant switch profile and others.
class ConfigHub(ChainMap):
	"""A hub of broadcast profiles, a subclass of ChainMap.
	Apart from giving favorable treatments to the active map and adding custom methods and properties,
	this structure is identical to chain map structure.

	The constructor takes an optional parameter that specifies which StationPlaylist component opened this map.
	The default value is None, which means Studio (splstudio.exe) app module opened this.
	"""

	def __init__(self, splComponent: str | None = None) -> None:
		# Check SPL components to make sure malicious actors don't tamper with it.
		if splComponent is None:
			splComponent = "splstudio"
		if splComponent not in _SPLComponents_:
			raise RuntimeError(
				"Not a StationPlaylist component, cannot create SPL add-on Config Hub database"
			)
		# Create a "fake" map entry, to be replaced by the normal profile later.
		# Super method is called to acknowledge the fact that this is powered by ChainMap.
		super().__init__()
		# #155: re-initialize maps to be a list of config objects to satisfy Mypy and friends.
		self.maps: list[ConfigObj] = [{}]
		# #64: keep an eye on which SPL component opened this map.
		self.splComponents: set[str] = set()
		self.splComponents.add(splComponent)
		# Config restrictions such as in-memory config come from command line.
		# Although SPL Utilities global plugin can inform NVDA about the below command-line switches,
		# handle them here also in case NVDA starts while focused on Studio window.
		self._configInMemory: bool = "--spl-configinmemory" in globalVars.unknownAppArgs
		self._normalProfileOnly: bool = "--spl-normalprofileonly" in globalVars.unknownAppArgs
		if self.configInMemory:
			self._normalProfileOnly = True
		# For presentational purposes.
		self.profileNames: list[str | None] = []
		# If config will be stored on RAM, this step is skipped, resulting in faster startup.
		# But data conversion must take place.
		if not self.configInMemory:
			self.maps[0] = self._unlockConfig(
				SPLIni, profileName=defaultProfileName, prefill=True, validateNow=True
			)
		else:
			# Get the dictionary version of default settings map.
			self.maps[0] = ConfigObj(_SPLDefaults.dict(), configspec=confspec, encoding="UTF-8")
			self.maps[0].name = defaultProfileName
			# Convert the following to runtime data structures.
			self.maps[0]["ColumnAnnouncement"]["IncludedColumns"] = set(
				self.maps[0]["ColumnAnnouncement"]["IncludedColumns"]
			)
			self.maps[0]["PlaylistTranscripts"]["IncludedColumns"] = set(
				self.maps[0]["PlaylistTranscripts"]["IncludedColumns"]
			)
			self.maps[0]["General"]["VerticalColumnAnnounce"] = None
		self.profileNames.append(None)  # Signifying normal profile.
		# Moving onto broadcast profiles if any (but not when only normal profile should be used).
		if not self.normalProfileOnly:
			try:
				for profile in os.listdir(SPLProfiles):
					name, ext = os.path.splitext(profile)
					if ext == ".ini":
						self.maps.append(
							self._unlockConfig(
								os.path.join(SPLProfiles, profile), profileName=name, validateNow=True
							)
						)
						self.profileNames.append(name)
			except WindowsError:
				pass
		# Runtime flags (profiles and profile switching flag come from NVDA Core's ConfigManager).
		self.profiles = self.maps
		# Active profile name is retrieved via the below property function.
		if "InstantProfile" in self.profiles[0] and not self.normalProfileOnly:
			self.instantSwitch = self.profiles[0]["InstantProfile"]
		else:
			self.instantSwitch = None
		self.prevProfile: str | None = None
		# A bit vector used to store profile switching flags.
		self._switchProfileFlags: int = 0
		# Switch history is a stack of previously activated profile(s), replacing prev profile flag from 7.x days.
		# Initially normal profile will sit in here.
		self.switchHistory: list[str] = [self.activeProfile]
		# #73: listen to config save/reset actions from NVDA Core.
		config.post_configSave.register(self.save)
		config.post_configReset.register(self.handlePostConfigReset)

	# Various properties
	@property
	def activeProfile(self) -> str:
		return self.profiles[0].name

	@property
	def normalProfileOnly(self) -> bool:
		return self._normalProfileOnly

	@property
	def configInMemory(self) -> bool:
		return self._configInMemory

	@property
	def configRestricted(self) -> bool:
		return self.normalProfileOnly or self.configInMemory or globalVars.appArgs.secure

	# Profile switching flags.
	_profileSwitchFlags: dict[str, int] = {"instant": 0x1}

	@property
	def switchProfileFlags(self) -> int:
		return self._switchProfileFlags

	@property
	def instantSwitchProfileActive(self) -> bool:
		return bool(self._switchProfileFlags & self._profileSwitchFlags["instant"])

	# Unlock (load) profiles from files.
	def _unlockConfig(
		self,
		path: str,
		profileName: str = "",
		prefill: bool = False,
		parent: dict[Any, Any] | None = None,
		validateNow: bool = False,
	) -> ConfigObj:
		# Profile name should be defined to help config status dictionary.
		# Resort to path's basename (without extension) if no profile name is specified.
		if not profileName:
			profileName = os.path.splitext(os.path.basename(path))[0]
		# Suppose this is one of the steps taken when copying settings when instantiating a new profile.
		# If so, go through same procedure as though config passes validation tests,
		# as all values from parent are in the right format.
		if parent is not None:
			SPLConfigCheckpoint = ConfigObj(parent, encoding="UTF-8")
			SPLConfigCheckpoint.filename = path
			SPLConfigCheckpoint.name = profileName
			return SPLConfigCheckpoint
		# For the rest.
		# To be mutated only during unlock routine.
		global _configLoadStatus
		# Profiles other than normal profile contains profile-specific sections only.
		# This speeds up profile loading routine significantly
		# as there is no need to call a function to strip global settings.
		# What if profiles have parsing errors?
		# If so, reset everything back to factory defaults.
		try:
			SPLConfigCheckpoint = ConfigObj(
				path, configspec=confspec if prefill else confspecprofiles, encoding="UTF-8"
			)
		except ConfigObjError:
			open(path, "w").close()
			SPLConfigCheckpoint = ConfigObj(
				path, configspec=confspec if prefill else confspecprofiles, encoding="UTF-8"
			)
			_configLoadStatus[profileName] = "fileReset"
		if validateNow:
			self._validateConfig(SPLConfigCheckpoint, profileName=profileName, prefill=prefill)
		try:
			self._extraInitSteps(SPLConfigCheckpoint, profileName=profileName)
		except KeyError:
			pass
		SPLConfigCheckpoint.name = profileName
		# Remove deprecated settings.
		self._removeDeprecatedSettings(SPLConfigCheckpoint)
		return SPLConfigCheckpoint

	# Config validation.
	def _validateConfig(
		self, SPLConfigCheckpoint: ConfigObj, profileName: str = "", prefill: bool = False
	) -> None:
		global _configLoadStatus
		configTest = SPLConfigCheckpoint.validate(_val, copy=prefill, preserve_errors=True)
		# Validator may return "True" if everything is okay,
		# "False" for unrecoverable error, or a dictionary of failed keys.
		if isinstance(configTest, bool) and not configTest:
			# Case 1: restore settings to defaults when config validation has failed on all values.
			defaultConfig = _SPLDefaults.dict()
			if SPLConfigCheckpoint.filename != SPLIni:
				defaultConfig = {
					sect: key for sect, key in defaultConfig.items() if sect in _mutatableSettings
				}
			SPLConfigCheckpoint.update(defaultConfig)
			_configLoadStatus[profileName] = "completeReset"
		elif isinstance(configTest, dict):
			# Case 2: for partial validation errors, attempt to reconstruct the failed values.
			for setting in list(configTest.keys()):
				if isinstance(configTest[setting], dict):
					for failedKey in list(configTest[setting].keys()):
						SPLConfigCheckpoint[setting][failedKey] = _SPLDefaults[setting][failedKey]
			SPLConfigCheckpoint.write()
			_configLoadStatus[profileName] = "partialReset"

	# Extra initialization steps such as converting value types.
	def _extraInitSteps(self, conf: ConfigObj, profileName: str = "") -> None:
		global _configLoadStatus
		columnOrder = conf["ColumnAnnouncement"]["ColumnOrder"]
		# Catch suttle errors.
		fields = _SPLDefaults["ColumnAnnouncement"]["ColumnOrder"]
		invalidFields = 0
		for field in fields:
			if field not in columnOrder:
				invalidFields += 1
		if invalidFields or len(columnOrder) != 17:
			if profileName in _configLoadStatus and _configLoadStatus[profileName] == "partialReset":
				_configLoadStatus[profileName] = "partialAndColumnOrderReset"
			else:
				_configLoadStatus[profileName] = "columnOrderReset"
			conf["ColumnAnnouncement"]["ColumnOrder"] = fields
		conf["ColumnAnnouncement"]["IncludedColumns"] = set(conf["ColumnAnnouncement"]["IncludedColumns"])
		# Artist and Title must be present at all times (quite redundant, but just in case).
		conf["ColumnAnnouncement"]["IncludedColumns"].add("Artist")
		conf["ColumnAnnouncement"]["IncludedColumns"].add("Title")
		# Same thing for included columns in Playlist Transcripts.
		conf["PlaylistTranscripts"]["IncludedColumns"] = set(conf["PlaylistTranscripts"]["IncludedColumns"])
		# Perform a similar check for metadata streaming.
		if len(conf["MetadataStreaming"]["MetadataEnabled"]) != 5:
			if profileName in _configLoadStatus and _configLoadStatus[profileName] == "partialReset":
				_configLoadStatus[profileName] = "partialAndMetadataReset"
			else:
				_configLoadStatus[profileName] = "metadataReset"
			conf["MetadataStreaming"]["MetadataEnabled"] = [False, False, False, False, False]
		# If vertical column announcement value is "None", transform this to NULL.
		if conf["General"]["VerticalColumnAnnounce"] == "None":
			conf["General"]["VerticalColumnAnnounce"] = None

	# Remove deprecated sections/keys.
	def _removeDeprecatedSettings(self, profile: ConfigObj) -> None:
		# For each deprecated/removed setting, parse section/subsection.
		# A list of 2-tuples will be returned, with each entry recording
		# the section name path tuple (requires parsing) and key, respectively.
		# However, there are certain flags that must be kept across sessions or must be handled separately.
		deprecatedSettings = get_extra_values(profile)
		for section, key in deprecatedSettings:
			if section == ():
				continue
			# Unless otherwise specified, all settings are level 1 (section/key).
			del profile[section[0]][key]

	# Create profile: public function to access the two private ones above (used when creating a new profile).
	# Mechanics borrowed from NVDA Core's config.conf with modifications for this add-on.
	def createProfile(self, path: str, name: str, parent: dict[Any, Any] | None = None) -> None:
		if self.configRestricted:
			raise RuntimeError("Config restricted: normal profile only, config in memory, or secure mode")
		self.maps.append(self._unlockConfig(path, profileName=name, parent=parent, validateNow=True))
		self.profileNames.append(name)

	# Rename and delete profiles.
	# Mechanics powered by similar routines in NVDA Core's config.conf.
	def renameProfile(self, oldName: str, newName: str) -> None:
		if self.configRestricted:
			raise RuntimeError("Config restricted: normal profile only, config in memory, or secure mode")
		newNamePath = newName + ".ini"
		newProfile = os.path.join(SPLProfiles, newNamePath)
		if oldName.lower() != newName.lower() and os.path.isfile(newProfile):
			raise RuntimeError("New profile path already exists")
		configPos = self.profileIndexByName(oldName)
		profilePos = self.profileNames.index(oldName)
		oldProfile = self.profiles[configPos].filename
		try:
			os.rename(oldProfile, newProfile)
		except WindowsError:
			pass
		self.profileNames[profilePos] = newName
		self.profiles[configPos].name = newName
		self.profiles[configPos].filename = newProfile

	def deleteProfile(self, name: str) -> None:
		if self.configRestricted:
			raise RuntimeError("Config restricted: normal profile only, config in memory, or secure mode")
		# Bring normal profile to the front if deleting the active profile.
		if name == self.activeProfile:
			self.swapProfiles(name, defaultProfileName)
		configPos = self.profileIndexByName(name)
		profilePos = self.profileNames.index(name)
		try:
			os.remove(self.profiles[configPos].filename)
		except WindowsError:
			pass
		del self.profiles[configPos]
		del self.profileNames[profilePos]

	def __delitem__(self, key):
		# Consult profile-specific key first before deleting anything.
		pos = (
			0
			if key in _mutatableSettings
			else [profile.name for profile in self.maps].index(defaultProfileName)
		)
		try:
			del self.maps[pos][key]
		except KeyError:
			raise KeyError(f"Key not found: {key!r}")

	# Perform some extra work before writing the config file.
	def _preSave(self, profile: ConfigObj) -> None:
		# Perform global setting processing only for the normal profile.
		if profile.filename == SPLIni:
			SPLSwitchProfile = self.instantSwitch
			# Cache instant profile for later use.
			if SPLSwitchProfile is not None:
				profile["InstantProfile"] = SPLSwitchProfile
			else:
				try:
					del profile["InstantProfile"]
				except KeyError:
					pass
		# For other profiles, remove global settings before writing to disk.
		else:
			# Make sure column inclusion aren't same as default values.
			if len(profile["ColumnAnnouncement"]["IncludedColumns"]) == 17:
				del profile["ColumnAnnouncement"]["IncludedColumns"]
			for setting in list(profile.keys()):
				for key in list(profile[setting].keys()):
					try:
						if profile[setting][key] == _SPLDefaults[setting][key]:
							del profile[setting][key]
					except KeyError:
						pass
				if setting in profile and not len(profile[setting]):
					del profile[setting]

	def save(self) -> None:
		# Save all config profiles unless config was loaded from memory.
		# #73: also responds to config save notification.
		# In case this is called when NVDA or last SPL component exits, just follow through,
		# as profile history and new profiles list would be cleared as part of general process cleanup.
		# Also, do not write config in secure mode.
		if self.configInMemory or globalVars.appArgs.secure:
			return
		for profile in self.profiles:
			# Without keeping a copy of config dictionary (and restoring from it later),
			# settings will be lost when presave check runs.
			profileSettings = profile.dict()
			profile["ColumnAnnouncement"]["IncludedColumns"] = list(
				profile["ColumnAnnouncement"]["IncludedColumns"]
			)
			if profile.name == defaultProfileName:
				# Also convert included columns in playlist transcripts.
				profile["PlaylistTranscripts"]["IncludedColumns"] = list(
					profile["PlaylistTranscripts"]["IncludedColumns"]
				)
			self._preSave(profile)
			profile.write()
			profile.update(profileSettings)

	# Reset or reload config.
	# Factory defaults value specifies what will happen (True = reset, False = reload).
	# Reload is identical to reset except profiles will be updated with data coming from disk.
	# Sometimes confirmation message will be shown, especially if instant switch profile is active.
	# Config dialog flag is a special flag reserved for use by add-on settings dialog.
	def reset(
		self,
		factoryDefaults: bool = False,
		askForConfirmation: bool = False,
		resetViaConfigDialog: bool = False,
	) -> None:
		if resetViaConfigDialog:
			askForConfirmation = bool(factoryDefaults and self._switchProfileFlags)
		if askForConfirmation:
			# present a confirmation message from the main thread.
			# #96: this is more so if a switch profile is active.
			# If this is done from add-on settings/reset panel, communicate 'no' with an exception.
			if (
				gui.messageBox(
					_(
						# Translators: Message displayed when attempting to reset Studio add-on settings
						# while an instant switch profile is active.
						"An instant switch profile is active. "
						"Resetting Studio add-on settings means normal profile will become active "
						"and switch profile settings will be left in unpredictable state. "
						"Are you sure you wish to reset Studio add-on settings to factory defaults?"
					),
					# Translators: The title of the confirmation dialog for Studio add-on settings reset.
					_("SPL Studio add-on reset"),
					wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING,
				)
				== wx.NO
			):
				if not resetViaConfigDialog:
					return
				else:
					raise RuntimeError("Instant switch profile must remain active, reset cannot proceed")
		# Keep complete and profile-specific defaults handy.
		defaultConfig = _SPLDefaults.dict()
		defaultProfileConfig = {
			sect: key for sect, key in defaultConfig.items() if sect in _mutatableSettings
		}
		for profile in self.profiles:
			# Retrieve the profile path, as ConfigObj.reset nullifies it.
			# ConfigObj.reload cannot be used as it leaves config in invalidated state.
			if factoryDefaults:
				profilePath = profile.filename
				profile.reset()
				profile.filename = profilePath
				sourceProfile = defaultProfileConfig if profilePath != SPLIni else defaultConfig
			else:
				sourceProfile = self._unlockConfig(
					profile.filename,
					profileName=profile.name,
					prefill=profile.filename == SPLIni,
					validateNow=True,
				).dict()
			# Just like complete reset when loading profiles, update settings from defaults.
			profile.update(sourceProfile)
			# Convert certain settings to a different format.
			profile["ColumnAnnouncement"]["IncludedColumns"] = set(
				profile["ColumnAnnouncement"]["IncludedColumns"]
			)
			# If this is normal profile, don't forget
			# to change type for Playlist Transcripts/included columns set.
			if profile.filename == SPLIni:
				profile["PlaylistTranscripts"]["IncludedColumns"] = set(
					profile["PlaylistTranscripts"]["IncludedColumns"]
				)
		# If this is a reset, switch back to normal profile via a custom variant of swap routine,
		# along with nullifying profile switches.
		if factoryDefaults:
			self.prevProfile = None
			self.switchHistory = [self.activeProfile]
			self._switchProfileFlags = 0
			if self.activeProfile != defaultProfileName:
				npIndex = self.profileIndexByName(defaultProfileName)
				self.profiles[0], self.profiles[npIndex] = self.profiles[npIndex], self.profiles[0]
		# #94: notify other subsystems to use default or reloaded settings,
		# as timers and other routines might not see default settings.
		# The below action will ultimately call profile switch handler
		# so subsystems can take appropriate action.
		splactions.SPLActionSettingsReset.notify(factoryDefaults=factoryDefaults)

	def handlePostConfigReset(self, factoryDefaults: bool = False) -> None:
		# Confirmation message must be presented on the main thread to avoid freezes.
		# For this reason, reset method should not be called from threads other than main thread
		# unless confirmation is not needed.
		wx.CallAfter(
			self.reset,
			factoryDefaults=factoryDefaults,
			askForConfirmation=factoryDefaults and self._switchProfileFlags,
		)

	def profileIndexByName(self, name: str) -> int:
		if name == self.activeProfile:
			return 0
		elif name == self.profiles[-1].name:
			return -1
		try:
			return [profile.name for profile in self.profiles].index(name)
		except ValueError:
			raise ValueError("The specified profile does not exist")

	def profileByName(self, name: str) -> ConfigObj:
		return self.profiles[self.profileIndexByName(name)]

	# Returns list of flags associated with a given profile.
	# Optional keyword arguments are to be added when called from dialogs such as add-on settings.
	# A crucial kwarg is contained, and if so, profile flags set will be returned.
	def getProfileFlags(
		self, name: str, active: str | None = None, instant: str | None = None, contained: bool = False
	) -> str | set[str]:
		flags = set()
		if active is None:
			active = self.activeProfile
		if instant is None:
			instant = self.instantSwitch
		if name == active:
			# Translators: A flag indicating the currently active broadcast profile.
			flags.add(_("active"))
		if name == instant:
			# Translators: A flag indicating the broadcast profile is an instant switch profile.
			flags.add(_("instant switch"))
		if not contained:
			return name if len(flags) == 0 else "{0} <{1}>".format(name, ", ".join(flags))
		else:
			return flags

	# Switch between profiles.
	# This involves promoting and demoting normal profile.
	# This will never be invoked if only normal profile is in use
	# or if config was loaded from memory alone.
	def switchProfile(self, prevProfile: str | None, newProfile: str, switchFlags: int) -> None:
		if self.normalProfileOnly or self.configInMemory:
			raise RuntimeError(
				"Only normal profile is in use or config was loaded from memory, cannot switch profiles"
			)
		# Check profile flags (for now, instant switch (0x1)).
		if switchFlags is not None and not 0 <= switchFlags < 0x2:
			raise RuntimeError("Profile switch flag out of range")
		self.swapProfiles(prevProfile, newProfile)
		# Set the prev flag manually.
		self.prevProfile = prevProfile
		# Manipulated only by profile switch start/end functions.
		self._switchProfileFlags = switchFlags
		if prevProfile is not None:
			self.switchHistory.append(newProfile)
			# Translators: Presented when switch to instant switch profile was successful.
			ui.message(_("Switching to {newProfileName}").format(newProfileName=self.activeProfile))
		else:
			self.switchHistory.pop()
			# Translators: Presented when switching from instant switch profile to a previous profile.
			ui.message(_("Returning to {previousProfile}").format(previousProfile=self.activeProfile))
		splactions.SPLActionProfileSwitched.notify()

	# Switch start/end functions.
	# To be called from the module when starting or ending a profile switch.
	# The only difference is the switch type, which will then set appropriate flag
	# to be passed to switchProfile method above, with xor used to set the flags.
	def switchProfileStart(self, prevProfile: str | None, newProfile: str, switchType: str) -> None:
		if switchType != "instant":
			raise RuntimeError("Incorrect profile switch type specified")
		if switchType == "instant" and self.instantSwitchProfileActive:
			raise RuntimeError("Instant switch flag is already on")
		log.debug(
			"SPL: profile switching start: "
			f"type = {switchType}, previous profile is {prevProfile}, new profile is {newProfile}"
		)
		self.switchProfile(
			prevProfile,
			newProfile,
			switchFlags=self._switchProfileFlags ^ self._profileSwitchFlags[switchType],
		)

	def switchProfileEnd(self, prevProfile: str | None, newProfile: str, switchType: str) -> None:
		if switchType != "instant":
			raise RuntimeError("Incorrect profile switch type specified")
		if switchType == "instant" and not self.instantSwitchProfileActive:
			raise RuntimeError("Instant switch flag is already off")
		log.debug(
			"SPL: profile switching end: "
			f"type = {switchType}, previous profile is {prevProfile}, new profile is {newProfile}"
		)
		self.switchProfile(
			prevProfile,
			newProfile,
			switchFlags=self._switchProfileFlags ^ self._profileSwitchFlags[switchType],
		)

	# Used from config dialog and other places.
	# Show switch index is used when deleting profiles so it doesn't have to look up index for old profiles.
	def swapProfiles(self, prevProfile: str | None, newProfile: str) -> None:
		former = self.profileIndexByName(prevProfile if prevProfile is not None else self.switchHistory[-1])
		current = self.profileIndexByName(newProfile)
		self.profiles[current], self.profiles[former] = self.profiles[former], self.profiles[current]


SPLConfig: ConfigHub | None = None

# Default config spec container.
_SPLDefaults = ConfigObj(None, configspec=confspec, encoding="UTF-8")
_val = Validator()
_SPLDefaults.validate(_val, copy=True)
# Track comments map.
trackComments = {}


# Open config database, used mostly from modules other than Studio.
def openConfig(splComponent: str) -> None:
	global SPLConfig
	# #64: skip this step if another SPL component (such as Creator) opened this.
	if SPLConfig is None:
		SPLConfig = ConfigHub(splComponent=splComponent)
	else:
		SPLConfig.splComponents.add(splComponent)


def initialize() -> None:
	global SPLConfig, _configLoadStatus, trackComments
	# Load the default config from a list of profiles.
	openConfig("splstudio")
	# #155: Mypy will say that SPLConfig is None when in fact it is ready
	# simply because openConfig function does not return SPLConfig.
	# Therefore do a None guard check just to tell Mypy it is safe to proceed.
	if SPLConfig is None:
		return
	# Locate instant profile and do something otherwise.
	if SPLConfig.instantSwitch is not None and SPLConfig.instantSwitch not in SPLConfig.profileNames:
		log.debug("SPL: failed to locate instant switch profile")
		_configLoadStatus[SPLConfig.activeProfile] = "noInstantProfile"
		SPLConfig.instantSwitch = None
	# Load track comments if they exist.
	# This must be a separate file (another pickle file).
	try:
		with open(os.path.join(globalVars.appArgs.configPath, "spltrackcomments.pickle"), "rb") as f:
			trackComments = pickle.load(f)
	except (IOError, EOFError, pickle.UnpicklingError):
		pass
	if len(_configLoadStatus):
		messages = []
		# Display just the error message if the only corrupt profile is the normal profile.
		if len(_configLoadStatus) == 1 and SPLConfig.activeProfile in _configLoadStatus:
			# Translators: Error message shown when add-on configuration had issues.
			messages.append("Your add-on configuration had following issues:\n\n")
			messages.append(_configErrors[_configLoadStatus[SPLConfig.activeProfile]])
		else:
			# Translators: Error message shown when add-on configuration had issues.
			messages.append("One or more broadcast profiles had issues:\n\n")
			for profile in _configLoadStatus:
				error = _configErrors[_configLoadStatus[profile]]
				messages.append(
					"{profileName}: {errorMessage}".format(profileName=profile, errorMessage=error)
				)
		_configLoadStatus.clear()
		wx.CallAfter(
			gui.messageBox,
			"\n".join(messages),
			# Translators: Standard error title for configuration error.
			_("Studio add-on Configuration error"),
			wx.OK | wx.ICON_ERROR,
		)


# Close config database if needed.
def closeConfig(splComponent: str) -> None:
	global SPLConfig
	# #99: if more than one instance of a given SPL component executable is running,
	# do not remove the component from the components registry.
	# The below loop will be run from the component app module's terminate method, but before that,
	# the app module associated with the component would have been deleted from the running table.
	# This is subject to change based on NVDA Core changes.
	for app in appModuleHandler.runningTable.values():
		if app.appName == splComponent:
			return
	# There's no way this function will work without SPLConfig being alive.
	if SPLConfig is None:
		raise RuntimeError("Attempting to close SPL config which no longer exists")
	SPLConfig.splComponents.discard(splComponent)
	if len(SPLConfig.splComponents) == 0:
		SPLConfig.save()
		# No need to keep config save/reset registration alive.
		config.post_configSave.unregister(SPLConfig.save)
		config.post_configReset.unregister(SPLConfig.handlePostConfigReset)
		SPLConfig = None


# Terminate the config and related subsystems.
def terminate() -> None:
	global trackComments
	# Dump and clear track comments (but not in secure mode).
	if not globalVars.appArgs.secure:
		with open(os.path.join(globalVars.appArgs.configPath, "spltrackcomments.pickle"), "wb") as f:
			pickle.dump(trackComments, f, protocol=4)
	trackComments.clear()
	trackComments = {}
	# Now save profiles.
	closeConfig("splstudio")


# Called from within the app module.
def instantProfileSwitch() -> None:
	# SPLConfig, are you alive?
	if SPLConfig is None:
		raise RuntimeError("SPL config is gone, cannot switch profiles")
	# What if only normal profile is in use?
	if SPLConfig.normalProfileOnly:
		# Translators: announced when only normal profile is in use.
		ui.message(_("Only normal profile is in use"))
		return
	SPLSwitchProfile = SPLConfig.instantSwitch
	if SPLSwitchProfile is None:
		# Translators: Presented when trying to switch to an instant switch profile
		# when the instant switch profile is not defined.
		ui.message(_("No instant switch profile is defined"))
	else:
		if SPLConfig.prevProfile is None:
			if SPLConfig.activeProfile == SPLSwitchProfile:
				# Translators: Presented when trying to switch to an instant switch profile
				# when one is already using the instant switch profile.
				ui.message(_("You are already in the instant switch profile"))
				return
			# Switch to the given profile.
			SPLConfig.switchProfileStart(SPLConfig.activeProfile, SPLSwitchProfile, "instant")
		else:
			SPLConfig.switchProfileEnd(None, SPLConfig.prevProfile, "instant")


# Additional configuration and miscellaneous dialogs
# See splconfui module for basic configuration dialogs.

# Startup dialogs.


# Welcome dialog (emulating NVDA Core)
class WelcomeDialog(wx.Dialog):
	# Translators: A message giving basic information about the add-on.
	welcomeMessage = _("""Welcome to StationPlaylist add-on for NVDA,
your companion to broadcasting with SPL Studio using NVDA screen reader.

Highlights of StationPlaylist add-on include:
* Layer commands for obtaining status information
* Various ways to examine track columns
* Various ways to find tracks
* Tools to analyze the loaded playlist
* Cart Explorer to learn cart assignments
* Comprehensive settings and documentation
* Completely free, open-source and community-driven
* And much more

Visit www.stationplaylist.com for details on StationPlaylist suite of applications.
Visit StationPlaylist add-on GitHub page (https://github.com/ChrisDuffley/stationPlaylist)
for add-on details and to read the documentation.
Want to see this dialog again? Just press Alt+NVDA+F1 while using Studio to return to this dialog.

Thank you.""")

	@classmethod
	def _instance(cls):
		return None

	def __new__(cls, *args, **kwargs):
		# Make this a singleton.
		instance = WelcomeDialog._instance()
		if instance is None:
			return super(WelcomeDialog, cls).__new__(cls, *args, **kwargs)
		return instance

	def __init__(self, parent):
		if WelcomeDialog._instance() is not None:
			return
		# Use a weakref so the instance can die.
		WelcomeDialog._instance = weakref.ref(self)
		# Translators: Title of a dialog displayed when the add-on starts presenting basic information,
		# similar to NVDA's own welcome dialog.
		super().__init__(parent, title=_("Welcome to StationPlaylist add-on"))
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)

		mainSizer = wx.BoxSizer(wx.VERTICAL)

		label = wx.StaticText(self, wx.ID_ANY, label=self.welcomeMessage)
		mainSizer.Add(label, border=20, flag=wx.LEFT | wx.RIGHT | wx.TOP)

		# Translators: A checkbox to show welcome dialog.
		self.showWelcomeDialog = wx.CheckBox(
			self, wx.ID_ANY, label=_("Show welcome dialog when I start Studio")
		)
		self.showWelcomeDialog.SetValue(SPLConfig["Startup"]["WelcomeDialog"])
		mainSizer.Add(self.showWelcomeDialog, border=10, flag=wx.TOP)

		mainSizer.Add(self.CreateButtonSizer(wx.OK), flag=wx.ALIGN_CENTER_HORIZONTAL)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.showWelcomeDialog.SetFocus()
		self.CenterOnScreen()

	def onOk(self, evt):
		global SPLConfig
		SPLConfig["Startup"]["WelcomeDialog"] = self.showWelcomeDialog.Value
		self.Destroy()

	def onAppTerminate(self):
		self.Destroy()


# And to open the above dialog and any other dialogs.
def showStartupDialogs() -> None:
	if globalVars.appArgs.minimal:
		return
	if SPLConfig["Startup"]["WelcomeDialog"]:
		gui.mainFrame.prePopup()
		WelcomeDialog(gui.mainFrame).Show()
		gui.mainFrame.postPopup()


# Message verbosity pool.
# This is a multimap, consisting of category, value and message.
# Most of the categories are same as confspec keys,
# hence the below message function is invoked when settings are changed.
def message(category: str, value: str) -> None:
	verbosityLevels = ("beginner", "advanced")
	ui.message(messagePool[category][value][verbosityLevels.index(SPLConfig["General"]["MessageVerbosity"])])


messagePool: dict[str, Any] = {
	"BrailleTimer": {
		"off": (
			# Translators: A setting in braille timer options.
			_("Braille timer off"),
			translate("Off"),
		),
		"outro": (
			# Translators: A setting in braille timer options.
			_("Braille track endings"),
			# Translators: A setting in braille timer options.
			_("Outro"),
		),
		"intro": (
			# Translators: A setting in braille timer options.
			_("Braille intro endings"),
			# Translators: A setting in braille timer options.
			_("Intro"),
		),
		"both": (
			# Translators: A setting in braille timer options.
			_("Braille intro and track endings"),
			# Translators: A setting in braille timer options.
			_("Both"),
		),
	},
	"LibraryScanAnnounce": {
		"off": (
			# Translators: A setting in library scan announcement options.
			_("Do not announce library scans"),
			translate("Off"),
		),
		"ending": (
			# Translators: A setting in library scan announcement options.
			_("Announce start and end of a library scan"),
			_("Start and end only"),
		),
		"progress": (
			# Translators: A setting in library scan announcement options.
			_("Announce the progress of a library scan"),
			_("Scan progress"),
		),
		"numbers": (
			# Translators: A setting in library scan announcement options.
			_("Announce progress and item count of a library scan"),
			_("Scan count"),
		),
	},
}
