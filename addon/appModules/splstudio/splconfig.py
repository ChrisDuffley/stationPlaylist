# SPL Studio Configuration Manager
# An app module and global plugin package for NVDA
# Copyright 2015-2021 Joseph Lee, released under GPL.
# Provides the configuration management package for SPL Studio app module.
# For miscellaneous dialogs and tool, see SPLMisc module.
# For UI surrounding this module, see splconfui module.
# For the add-on settings specification, see splconfspec module.

# #155 (21.03): remove __future__ import when NVDA runs under Python 3.10.
from __future__ import annotations
from typing import Optional, Any
import os
import pickle
from collections import ChainMap
import weakref
from configobj import ConfigObj, get_extra_values, ConfigObjError
# ConfigObj 5.1.0 and later integrates validate module.
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
addonHandler.initTranslation()
from ..skipTranslation import translate

# Configuration management
SPLIni = os.path.join(globalVars.appArgs.configPath, "splstudio.ini")
SPLProfiles = os.path.join(globalVars.appArgs.configPath, "addons", "stationPlaylist", "profiles")
SPLConfig = None
# Cache a copy of the loaded config.
# This comes in handy when saving configuration to disk. For the most part, no change occurs to config.
# This helps prolong life of a solid-state drive (preventing unnecessary writes).
_SPLCache = {}
# The following settings can be changed in profiles:
_mutatableSettings = ("IntroOutroAlarms", "MicrophoneAlarm", "MetadataStreaming", "ColumnAnnouncement")
# 7.0: Profile-specific confspec (might be removed once a more optimal way to validate sections is found).
# Dictionary comprehension is better here.
confspecprofiles = {sect: key for sect, key in confspec.items() if sect in _mutatableSettings}
# Translators: The name of the default (normal) profile.
defaultProfileName = _("Normal profile")
# StationPlaylist components.
_SPLComponents_ = ("splstudio", "splcreator", "tracktool")


# 8.0: Run-time config storage and management will use ConfigHub data structure, a subclass of chain map.
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

	def __init__(self, splComponent=None):
		# Check SPL components to make sure malicious actors don't tamper with it.
		if splComponent is None:
			splComponent = "splstudio"
		if splComponent not in _SPLComponents_:
			raise RuntimeError("Not a StationPlaylist component, cannot create SPL add-on Config Hub database")
		# Create a "fake" map entry, to be replaced by the normal profile later.
		super(ConfigHub, self).__init__()
		# #64 (18.07): keep an eye on which SPL component opened this map.
		self.splComponents = set()
		self.splComponents.add(splComponent)
		# 17.10: config restrictions such as in-memory config come from command line.
		self._configInMemory = "--spl-configinmemory" in globalVars.appArgsExtra
		self._normalProfileOnly = "--spl-normalprofileonly" in globalVars.appArgsExtra
		if self.configInMemory:
			self._normalProfileOnly = True
		# For presentational purposes.
		self.profileNames = []
		# 17.10: if config will be stored on RAM, this step is skipped, resulting in faster startup.
		# But data conversion must take place.
		if not self.configInMemory:
			self.maps[0] = self._unlockConfig(SPLIni, profileName=defaultProfileName, prefill=True, validateNow=True)
		else:
			# 20.09: get the dictionary version of default settings map.
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
		# Always cache normal profile upon startup.
		# 17.10: and no, not when config was loaded from memory.
		if not self.configInMemory:
			self._cacheProfile(self.maps[0])
			# Remove deprecated keys.
			# This action must be performed after caching, otherwise the newly modified profile will not be saved.
			# For each deprecated/removed key, parse section/subsection.
			# #95 (19.02/18.09.7-LTS): Configobj 4.7.0 ships with a more elegant way to obtain
			# all extra values in one go, making deprecated keys definition unnecessary.
			# A list of 2-tuples will be returned, with each entry recording
			# the section name path tuple (requires parsing) and key, respectively.
			# However, there are certain keys that must be kept across sessions or must be handled separately.
			deprecatedKeys = get_extra_values(self.maps[0])
			for section, key in deprecatedKeys:
				if section == ():
					continue
				# Unless otherwise specified, all keys are level 1 (section/key).
				del self.maps[0][section[0]][key]
		# Moving onto broadcast profiles if any.
		# 17.10: but not when only normal profile should be used.
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
						# 20.10/20.09.2-LTS: remove deprecated keys from profiles, too.
						deprecatedKeys = get_extra_values(self.maps[-1])
						# Cache this profile if deprecated keys are found so that newly edited profile can be saved properly.
						if len(deprecatedKeys):
							self._cacheProfile(self.maps[-1])
						for section, key in deprecatedKeys:
							if section == ():
								continue
							# Just like normal profile, unless otherwise specified, all keys are level 1 (section/key).
							del self.maps[-1][section[0]][key]
			except WindowsError:
				pass
		# Runtime flags (profiles and profile switching flag come from NVDA Core's ConfigManager).
		self.profiles = self.maps
		# Active profile name is retrieved via the below property function.
		if "InstantProfile" in self.profiles[0] and not self.normalProfileOnly:
			self.instantSwitch = self.profiles[0]["InstantProfile"]
		else:
			self.instantSwitch = None
		self.prevProfile = None
		# A bit vector used to store profile switching flags.
		self._switchProfileFlags = 0
		# Switch history is a stack of previously activated profile(s), replacing prev profile flag from 7.x days.
		# Initially normal profile will sit in here.
		self.switchHistory = [self.activeProfile]
		# Record new profiles if any.
		self.newProfiles = set()
		# Reset flag (only engaged if reset did happen).
		self.resetHappened = False
		# #73: listen to config save/reset actions from NVDA Core.
		config.post_configSave.register(self.save)
		config.post_configReset.register(self.handlePostConfigReset)

	# Various properties
	@property
	def activeProfile(self):
		return self.profiles[0].name

	@property
	def normalProfileOnly(self):
		return self._normalProfileOnly

	@property
	def configInMemory(self):
		return self._configInMemory

	@property
	def configRestricted(self):
		return self.normalProfileOnly or self.configInMemory

	# Profile switching flags.
	_profileSwitchFlags = {"instant": 0x1}

	@property
	def switchProfileFlags(self):
		return self._switchProfileFlags

	@property
	def instantSwitchProfileActive(self):
		return bool(self._switchProfileFlags & self._profileSwitchFlags["instant"])

	# Unlock (load) profiles from files.
	# 7.0: Allow new profile settings to be overridden by a parent profile.
	# 8.0: Don't validate profiles other than normal profile in the beginning.
	def _unlockConfig(self, path, profileName=None, prefill=False, parent=None, validateNow=False):
		# 7.0: Suppose this is one of the steps taken when copying settings when instantiating a new profile.
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
		# Optimization: Profiles other than normal profile contains profile-specific sections only.
		# This speeds up profile loading routine significantly
		# as there is no need to call a function to strip global settings.
		# 7.0: What if profiles have parsing errors?
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
		# 5.2 and later: check to make sure all values are correct.
		# 7.0: Make sure errors are displayed as config keys are now sections and may need to go through subkeys.
		# 8.0: Don't validate unless told to do so.
		if validateNow:
			self._validateConfig(SPLConfigCheckpoint, profileName=profileName, prefill=prefill)
		# Until it is brought in here...
		try:
			self._extraInitSteps(SPLConfigCheckpoint, profileName=profileName)
		except KeyError:
			pass
		SPLConfigCheckpoint.name = profileName
		return SPLConfigCheckpoint

	# Config validation.
	# Separated from unlock routine in 8.0.
	def _validateConfig(self, SPLConfigCheckpoint, profileName=None, prefill=False):
		global _configLoadStatus
		configTest = SPLConfigCheckpoint.validate(_val, copy=prefill, preserve_errors=True)
		# Validator may return "True" if everything is okay,
		# "False" for unrecoverable error, or a dictionary of failed keys.
		if isinstance(configTest, bool) and not configTest:
			# Case 1: restore settings to defaults when 5.x config validation has failed on all values.
			# 6.0: In case this is a user profile, apply base configuration.
			# 8.0: Call copy profile function directly to reduce overhead.
			# 20.09: reset all settings from default settings map directly.
			defaultConfig = _SPLDefaults.dict()
			if SPLConfigCheckpoint.filename != SPLIni:
				defaultConfig = {sect: key for sect, key in defaultConfig.items() if sect in _mutatableSettings}
			SPLConfigCheckpoint.update(defaultConfig)
			_configLoadStatus[profileName] = "completeReset"
		elif isinstance(configTest, dict):
			# Case 2: For 5.x and later, attempt to reconstruct the failed values.
			# 6.0: Cherry-pick global settings only.
			# 7.0: Go through failed sections.
			for setting in list(configTest.keys()):
				if isinstance(configTest[setting], dict):
					for failedKey in list(configTest[setting].keys()):
						# 7.0 optimization: just reload from defaults dictionary,
						# as broadcast profiles contain profile-specific settings only.
						SPLConfigCheckpoint[setting][failedKey] = _SPLDefaults[setting][failedKey]
			# 7.0: Disqualified from being cached this time.
			SPLConfigCheckpoint.write()
			_configLoadStatus[profileName] = "partialReset"

	# Extra initialization steps such as converting value types.
	def _extraInitSteps(self, conf, profileName=None):
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
		# Perform a similar check for metadata streaming.
		if len(conf["MetadataStreaming"]["MetadataEnabled"]) != 5:
			if profileName in _configLoadStatus and _configLoadStatus[profileName] == "partialReset":
				_configLoadStatus[profileName] = "partialAndMetadataReset"
			else:
				_configLoadStatus[profileName] = "metadataReset"
			conf["MetadataStreaming"]["MetadataEnabled"] = [False, False, False, False, False]
		# 17.04: If vertical column announcement value is "None", transform this to NULL.
		if conf["General"]["VerticalColumnAnnounce"] == "None":
			conf["General"]["VerticalColumnAnnounce"] = None
		# 18.08: same thing for included columns in Playlist Transcripts.
		conf["PlaylistTranscripts"]["IncludedColumns"] = set(conf["PlaylistTranscripts"]["IncludedColumns"])

	# Create profile: public function to access the two private ones above (used when creating a new profile).
	# Mechanics borrowed from NVDA Core's config.conf with modifications for this add-on.
	def createProfile(self, path, name, parent=None):
		# 17.10: No, not when restrictions are applied.
		if self.configRestricted:
			raise RuntimeError("Only normal profile is in use or config was loaded from memory")
		self.maps.append(self._unlockConfig(path, profileName=name, parent=parent, validateNow=True))
		self.profileNames.append(name)
		self.newProfiles.add(name)

	# Rename and delete profiles.
	# Mechanics powered by similar routines in NVDA Core's config.conf.
	def renameProfile(self, oldName, newName):
		# 17.10: No, not when restrictions are applied.
		if self.configRestricted:
			raise RuntimeError("Only normal profile is in use or config was loaded from memory")
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
		# Just in case a new profile has been renamed...
		if oldName in self.newProfiles:
			self.newProfiles.discard(oldName)
			self.newProfiles.add(newName)

	def deleteProfile(self, name):
		# 17.10: No, not when restrictions are applied.
		if self.configRestricted:
			raise RuntimeError("Only normal profile is in use or config was loaded from memory")
		# Bring normal profile to the front if it isn't.
		# Optimization: Tell the swapper that we need index to the normal profile for this case.
		if name == self.activeProfile:
			configPos = self.swapProfiles(name, defaultProfileName, showSwitchIndex=True)
		else:
			configPos = self.profileIndexByName(name)
		profilePos = self.profileNames.index(name)
		try:
			os.remove(self.profiles[configPos].filename)
		except WindowsError:
			pass
		del self.profiles[configPos]
		del self.profileNames[profilePos]
		self.newProfiles.discard(name)

	def _cacheProfile(self, conf):
		global _SPLCache
		if _SPLCache is None:
			_SPLCache = {}
		key = None if conf.filename == SPLIni else conf.name
		# 8.0: Caching the dictionary (items) is enough.
		# Do not just copy dictionaries, as it copies references.
		# 20.09: thankfully conf.dict method performs a "deep copy" (returns a fresh dictionary with data inside).
		_SPLCache[key] = conf.dict()

	def __delitem__(self, key):
		# Consult profile-specific key first before deleting anything.
		pos = 0 if key in _mutatableSettings else [profile.name for profile in self.maps].index(defaultProfileName)
		try:
			del self.maps[pos][key]
		except KeyError:
			raise KeyError(f'Key not found: {key!r}')

	# Perform some extra work before writing the config file.
	def _preSave(self, profile):
		# Perform global setting processing only for the normal profile.
		# 7.0: if this is a second pass, index 0 may not be normal profile at all.
		# Use profile path instead.
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
			# 6.1: Make sure column inclusion aren't same as default values.
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

	def save(self):
		# Save all config profiles unless config was loaded from memory.
		# #73: also responds to config save notification.
		# In case this is called when NVDA or last SPL component exits, just follow through,
		# as profile history and new profiles list would be cleared as part of general process cleanup.
		if self.configInMemory:
			return
		# 7.0: Save normal profile first.
		# Temporarily merge normal profile.
		# 8.0: Locate the index instead.
		# 20.09: work directly with normal profile.
		normalProfile = self.profileByName(defaultProfileName)
		self._preSave(normalProfile)
		# Disk write optimization check please.
		# 8.0: Bypass this if profiles were reset.
		if self.resetHappened or _SPLCache[None] != normalProfile:
			# 6.1: Transform column inclusion data structure (for normal profile) now.
			# 7.0: This will be repeated for broadcast profiles later.
			# 8.0: Conversion will happen here, as conversion to list
			# is necessary before writing it to disk (if told to do so).
			# 17.09: before doing that, temporarily save a copy of the current column headers set.
			# 20.09: have a temporary settings dictionary handy for updating the actual profile.
			profileSettings = normalProfile.dict()
			normalProfile["ColumnAnnouncement"]["IncludedColumns"] = list(
				normalProfile["ColumnAnnouncement"]["IncludedColumns"]
			)
			# 18.08: also convert included columns in playlist transcripts.
			normalProfile["PlaylistTranscripts"]["IncludedColumns"] = list(
				normalProfile["PlaylistTranscripts"]["IncludedColumns"]
			)
			normalProfile.write()
			normalProfile.update(profileSettings)
			# Don't forget to update profile cache, otherwise subsequent changes are lost.
			self._cacheProfile(normalProfile)
		# Now save broadcast profiles.
		for profile in self.profiles:
			# Normal profile is done.
			if profile.name == defaultProfileName:
				continue
			if profile is not None:
				# 7.0: See if profiles themselves must be saved.
				# This must be done now, otherwise changes to broadcast profiles (cached) will
				# not be saved as presave removes them.
				# 8.0: Bypass cache check routine if this is a new profile or if reset happened.
				# Takes advantage of the fact that Python's "or" operator evaluates from left to right.
				# Although nothing should be returned when calling dict.get with nonexistent keys,
				# return the current profile for ease of comparison.
				if (
					self.resetHappened or profile.name in self.newProfiles
					or _SPLCache.get(profile.name, profile) != profile
				):
					# Without keeping a copy of config dictionary (and restoring from it later),
					# settings will be lost when presave check runs.
					profileSettings = profile.dict()
					profile["ColumnAnnouncement"]["IncludedColumns"] = list(profile["ColumnAnnouncement"]["IncludedColumns"])
					self._preSave(profile)
					profile.write()
					profile.update(profileSettings)
					# just like normal profile, cache the profile again provided that it was done already
					# and if options in the cache and the live profile are different.
					self._cacheProfile(profile)

	# Reset or reload config.
	# Factory defaults value specifies what will happen (True = reset, False = reload).
	# Reload is identical to reset except profiles will be updated with data coming from disk.
	# Profile indicates the name of the profile to reset or reload.
	# Sometimes confirmation message will be shown, especially if instant switch profile is active.
	# Config dialog flag is a special flag reserved for use by add-on settings dialog.
	def reset(self, factoryDefaults=False, askForConfirmation=False, resetViaConfigDialog=False):
		if resetViaConfigDialog:
			askForConfirmation = bool(factoryDefaults and self._switchProfileFlags)
		if askForConfirmation:
			# present a confirmation message from the main thread.
			# #96 (19.02/18.09.7-LTS): this is more so if a switch profile is active.
			# If this is done from add-on settings/reset panel, communicate 'no' with an exception.
			if gui.messageBox(
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
				wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING
			) == wx.NO:
				if not resetViaConfigDialog:
					return
				else:
					raise RuntimeError("Instant switch profile must remain active, reset cannot proceed")
		# 20.09: keep complete and profile-specific defaults handy.
		defaultConfig = _SPLDefaults.dict()
		defaultProfileConfig = {sect: key for sect, key in defaultConfig.items() if sect in _mutatableSettings}
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
					profile.filename, profileName=profile.name, prefill=profile.filename == SPLIni, validateNow=True
				).dict()
			# 20.09: just like complete reset when loading profiles, update settings from defaults.
			profile.update(sourceProfile)
			# Convert certain settings to a different format.
			profile["ColumnAnnouncement"]["IncludedColumns"] = set(profile["ColumnAnnouncement"]["IncludedColumns"])
			# 18.08: if this is normal profile, don't forget
			# to change type for Playlist Transcripts/included columns set.
			if profile.filename == SPLIni:
				profile["PlaylistTranscripts"]["IncludedColumns"] = set(profile["PlaylistTranscripts"]["IncludedColumns"])
				# Just like constructor, remove deprecated keys if any.
				deprecatedKeys = get_extra_values(profile)
				for section, key in deprecatedKeys:
					if section == ():
						continue
					del profile[section[0]][key]
		# If this is a reset, switch back to normal profile via a custom variant of swap routine,
		# along with nullifying profile switches.
		if factoryDefaults:
			self.prevProfile = None
			self.switchHistory = [self.activeProfile]
			self._switchProfileFlags = 0
			if self.activeProfile != defaultProfileName:
				npIndex = self.profileIndexByName(defaultProfileName)
				self.profiles[0], self.profiles[npIndex] = self.profiles[npIndex], self.profiles[0]
			# 8.0 optimization: Tell other modules that reset was done
			# in order to postpone disk writes until the end.
			self.resetHappened = True
		# #94 (19.02/18.09.7-LTS): notify other subsystems to use default or reloaded settings,
		# as timers and other routines might not see default settings.
		# The below action will ultimately call profile switch handler
		# so subsystems can take appropriate action.
		splactions.SPLActionSettingsReset.notify(factoryDefaults=factoryDefaults)

	def handlePostConfigReset(self, factoryDefaults=False):
		# Confirmation message must be presented on the main thread to avoid freezes.
		# For this reason, reset method should not be called from threads other than main thread
		# unless confirmation is not needed.
		wx.CallAfter(
			self.reset, factoryDefaults=factoryDefaults,
			askForConfirmation=factoryDefaults and self._switchProfileFlags
		)

	def profileIndexByName(self, name):
		# 8.0 optimization: Only traverse the profiles list
		# if head (active profile) or tail does not yield profile name in question.
		if name == self.activeProfile:
			return 0
		elif name == self.profiles[-1].name:
			return -1
		try:
			return [profile.name for profile in self.profiles].index(name)
		except ValueError:
			raise ValueError("The specified profile does not exist")

	def profileByName(self, name):
		return self.profiles[self.profileIndexByName(name)]

	# Returns list of flags associated with a given profile.
	# Optional keyword arguments are to be added when called from dialogs such as add-on settings.
	# A crucial kwarg is contained, and if so, profile flags set will be returned.
	def getProfileFlags(self, name, active=None, instant=None, contained=False):
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
	# 17.10: this will never be invoked if only normal profile is in use
	# or if config was loaded from memory alone.
	def switchProfile(self, prevProfile, newProfile, switchFlags):
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
		# #38 (17.11/15.10-LTS): can't wait two seconds for microphone alarm to stop.
		# #40 (17.12): all taken care of by profile switched notification.
		splactions.SPLActionProfileSwitched.notify()

	# Switch start/end functions.
	# To be called from the module when starting or ending a profile switch.
	# The only difference is the switch type, which will then set appropriate flag
	# to be passed to switchProfile method above, with xor used to set the flags.
	# 20.06: time-based profile flag is gone (only instant switch flag remains).
	def switchProfileStart(self, prevProfile, newProfile, switchType):
		if switchType != "instant":
			raise RuntimeError("Incorrect profile switch type specified")
		if switchType == "instant" and self.instantSwitchProfileActive:
			raise RuntimeError("Instant switch flag is already on")
		log.debug(
			"SPL: profile switching start: "
			f"type = {switchType}, previous profile is {prevProfile}, new profile is {newProfile}"
		)
		self.switchProfile(
			prevProfile, newProfile,
			switchFlags=self._switchProfileFlags ^ self._profileSwitchFlags[switchType]
		)
		# 8.0: Cache the new profile.
		global _SPLCache
		# 18.03: be sure to check if config cache is even online.
		if _SPLCache is not None and newProfile != defaultProfileName and newProfile not in _SPLCache:
			self._cacheProfile(self.profileByName(newProfile))

	def switchProfileEnd(self, prevProfile, newProfile, switchType):
		if switchType != "instant":
			raise RuntimeError("Incorrect profile switch type specified")
		if switchType == "instant" and not self.instantSwitchProfileActive:
			raise RuntimeError("Instant switch flag is already off")
		log.debug(
			"SPL: profile switching end: "
			f"type = {switchType}, previous profile is {prevProfile}, new profile is {newProfile}"
		)
		self.switchProfile(
			prevProfile, newProfile,
			switchFlags=self._switchProfileFlags ^ self._profileSwitchFlags[switchType]
		)

	# Used from config dialog and other places.
	# Show switch index is used when deleting profiles so it doesn't have to look up index for old profiles.
	def swapProfiles(self, prevProfile, newProfile, showSwitchIndex=False):
		former = self.profileIndexByName(prevProfile if prevProfile is not None else self.switchHistory[-1])
		current = self.profileIndexByName(newProfile)
		self.profiles[current], self.profiles[former] = self.profiles[former], self.profiles[current]
		if showSwitchIndex:
			return current


# Default config spec container.
# To be moved to a different place in 8.0.
_SPLDefaults = ConfigObj(None, configspec=confspec, encoding="UTF-8")
_val = Validator()
_SPLDefaults.validate(_val, copy=True)


# In case one or more profiles had config issues, look up the error message from the following map.
_configErrors = {
	"fileReset": "Settings reset to defaults due to configuration file coruption",
	"completeReset": "All settings reset to defaults",
	"partialReset": "Some settings reset to defaults",
	"columnOrderReset": "Column announcement order reset to defaults",
	"partialAndColumnOrderReset": "Some settings, including column announcement order reset to defaults",
	"noInstantProfile": "Cannot find instant profile"
}

# To be run in app module constructor.
# With the load function below, prepare config and other things upon request.
# Prompt the config error dialog only once.
_configLoadStatus = {}  # Key = filename, value is pass or no pass.
# Track comments map.
trackComments = {}


# Open config database, used mostly from modules other than Studio.
def openConfig(splComponent):
	global SPLConfig
	# #64 (18.07): skip this step if another SPL component (such as Creator) opened this.
	if SPLConfig is None:
		SPLConfig = ConfigHub(splComponent=splComponent)
	else:
		SPLConfig.splComponents.add(splComponent)


def initialize():
	global SPLConfig, _configLoadStatus, trackComments
	# Load the default config from a list of profiles.
	# 8.0: All this work will be performed when ConfigHub loads.
	# #64 (18.07): performed by openConfig function.
	openConfig("splstudio")
	# Locate instant profile and do something otherwise.
	if SPLConfig.instantSwitch is not None and SPLConfig.instantSwitch not in SPLConfig.profileNames:
		log.debug("SPL: failed to locate instant switch profile")
		_configLoadStatus[SPLConfig.activeProfile] = "noInstantProfile"
		SPLConfig.instantSwitch = None
	# 7.0: Load track comments if they exist.
	# This must be a separate file (another pickle file).
	# 8.0: Do this much later when a track is first focused.
	# For forward compatibility, work with pickle protocol 4 (Python 3.4 and later).
	try:
		with open(os.path.join(globalVars.appArgs.configPath, "spltrackcomments.pickle"), "rb") as f:
			trackComments = pickle.load(f)
	except (IOError, EOFError, pickle.UnpicklingError):
		pass
	if len(_configLoadStatus):
		messages = []
		# 6.1: Display just the error message if the only corrupt profile is the normal profile.
		if len(_configLoadStatus) == 1 and SPLConfig.activeProfile in _configLoadStatus:
			# Translators: Error message shown when add-on configuration had issues.
			messages.append("Your add-on configuration had following issues:\n\n")
			messages.append(_configErrors[_configLoadStatus[SPLConfig.activeProfile]])
		else:
			# Translators: Error message shown when add-on configuration had issues.
			messages.append("One or more broadcast profiles had issues:\n\n")
			for profile in _configLoadStatus:
				error = _configErrors[_configLoadStatus[profile]]
				messages.append("{profileName}: {errorMessage}".format(profileName=profile, errorMessage=error))
		_configLoadStatus.clear()
		wx.CallAfter(
			gui.messageBox, "\n".join(messages),
			# Translators: Standard error title for configuration error.
			_("Studio add-on Configuration error"), wx.OK | wx.ICON_ERROR
		)


# Close config database if needed.
def closeConfig(splComponent):
	global SPLConfig, _SPLCache
	# #99 (19.06/18.09.9-LTS): if more than one instance of a given SPL component executable is running,
	# do not remove the component from the components registry.
	import appModuleHandler
	# The below loop will be run from the component app module's terminate method, but before that,
	# the app module associated with the component would have been deleted from the running table.
	# This is subject to change based on NVDA Core changes.
	for app in appModuleHandler.runningTable.values():
		if app.appName == splComponent:
			return
	SPLConfig.splComponents.discard(splComponent)
	if len(SPLConfig.splComponents) == 0:
		SPLConfig.save()
		# No need to keep config save/reset registration alive.
		config.post_configSave.unregister(SPLConfig.save)
		config.post_configReset.unregister(SPLConfig.handlePostConfigReset)
		SPLConfig = None
		_SPLCache.clear()
		_SPLCache = None


# Terminate the config and related subsystems.
def terminate():
	global SPLConfig, _SPLCache
	# Dump track comments.
	with open(os.path.join(globalVars.appArgs.configPath, "spltrackcomments.pickle"), "wb") as f:
		pickle.dump(trackComments, f, protocol=4)
	# Now save profiles.
	# 8.0: Call the save method.
	# #64 (18.07): separated into its own function in 2018.
	closeConfig("splstudio")


# Called from within the app module.
def instantProfileSwitch():
	# 17.10: What if only normal profile is in use?
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
			# 6.1: Do to referencing nature of Python, use the profile index function
			# to locate the index for the soon to be deactivated profile.
			# 7.0: Store the profile name instead in order to prevent profile index mangling if profiles are deleted.
			# Pass in the prev profile, which will be None for instant profile switch.
			# 7.0: Now activate "activeProfile" argument which controls the behavior of the function below.
			# 8.0: Work directly with profile names.
			# 18.03: call switch profile start method directly.
			# To the outside, a profile switch took place.
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
* Layer commands for obtaining status information.
* Various ways to examine track columns.
* Various ways to find tracks.
* Cart Explorer to learn cart assignments.
* Comprehensive settings and documentation.
* Completely free, open-source and community-driven.
* And much more.

Visit www.stationplaylist.com for details on StationPlaylist suite of applications.
Visit StationPlaylist entry on NVDA Community Add-ons page (addons.nvda-project.org)
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
		self.showWelcomeDialog = wx.CheckBox(self, wx.ID_ANY, label=_("Show welcome dialog when I start Studio"))
		self.showWelcomeDialog.SetValue(SPLConfig["Startup"]["WelcomeDialog"])
		mainSizer.Add(self.showWelcomeDialog, border=10, flag=wx.TOP)

		mainSizer.Add(self.CreateButtonSizer(wx.OK), flag=wx.ALIGN_CENTER_HORIZONTAL)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.showWelcomeDialog.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		global SPLConfig
		SPLConfig["Startup"]["WelcomeDialog"] = self.showWelcomeDialog.Value
		self.Destroy()

	def onAppTerminate(self):
		self.Destroy()


# And to open the above dialog and any other dialogs.
# 18.09: return immediately after opening old ver dialog if minimal flag is set.
def showStartupDialogs(oldVer=False):
	# Old version reminder if this is such a case.
	# 17.10: and also used to give people a chance to switch to LTS.
	# 20.06: controlled by a temporary flag that can come and go.
	# To be resurrected later.
	if globalVars.appArgs.minimal:
		return
	if SPLConfig["Startup"]["WelcomeDialog"]:
		gui.mainFrame.prePopup()
		WelcomeDialog(gui.mainFrame).Show()
		gui.mainFrame.postPopup()


# Message verbosity pool.
# To be moved to its own module in add-on 7.0.
# This is a multimap, consisting of category, value and message.
# Most of the categories are same as confspec keys,
# hence the below message function is invoked when settings are changed.
def message(category, value):
	verbosityLevels = ("beginner", "advanced")
	ui.message(messagePool[category][value][verbosityLevels.index(SPLConfig["General"]["MessageVerbosity"])])


messagePool = {
	"BeepAnnounce": {
		True: (
			# Translators: Reported when status announcement is set to beeps in SPL Studio.
			_("Status announcement beeps"),
			# Translators: Reported when status announcement is set to beeps in SPL Studio.
			_("Beeps")),
		False: (
			# Translators: Reported when status announcement is set to beeps in SPL Studio.
			_("Status announcement words"),
			# Translators: Reported when status announcement is set to beeps in SPL Studio.
			_("Words"))},
	"BrailleTimer": {
		"off": (
			# Translators: A setting in braille timer options.
			_("Braille timer off"), translate("Off")),
		"outro": (
			# Translators: A setting in braille timer options.
			_("Braille track endings"),
			# Translators: A setting in braille timer options.
			_("Outro")),
		"intro": (
			# Translators: A setting in braille timer options.
			_("Braille intro endings"),
			# Translators: A setting in braille timer options.
			_("Intro")),
		"both": (
			# Translators: A setting in braille timer options.
			_("Braille intro and track endings"),
			# Translators: A setting in braille timer options.
			_("Both"))},
	"LibraryScanAnnounce": {
		"off": (
			# Translators: A setting in library scan announcement options.
			_("Do not announce library scans"), translate("Off")),
		"ending": (
			# Translators: A setting in library scan announcement options.
			_("Announce start and end of a library scan"), _("Start and end only")),
		"progress": (
			# Translators: A setting in library scan announcement options.
			_("Announce the progress of a library scan"), _("Scan progress")),
		"numbers": (
			# Translators: A setting in library scan announcement options.
			_("Announce progress and item count of a library scan"), _("Scan count"))}
}
