# SPL Studio Configuration Manager
# An app module and global plugin package for NVDA
# Copyright 2015-2018 Joseph Lee and others, released under GPL.
# Provides the configuration management package for SPL Studio app module.
# For miscellaneous dialogs and tool, see SPLMisc module.
# For UI surrounding this module, see splconfui module.

import sys
py3 = sys.version.startswith("3")
import os
if py3:
	from io import StringIO
	import pickle
else:
	from cStringIO import StringIO
	import cPickle as pickle
from configobj import ConfigObj
from validate import Validator
import time
import datetime
import config
import globalVars
import ui
import gui
import wx
# #50 (18.03): keep an eye on update check facility.
try:
	from . import splupdate
except RuntimeError:
	splupdate = None
from . import splactions
from . import spldebugging

# Python 3 preparation (a compatibility layer until Six module is included).
rangeGen = range if py3 else xrange

# Until NVDA Core uses Python 3 (preferably 3.3 or later), use a backported version of chain map class.
# Backported by Jonathan Eunice.
# Python Package Index: https://pypi.python.org/pypi/chainmap/1.0.2
try:
	from collections import ChainMap
except ImportError:
	from .chainmap import ChainMap

# Until wx.CENTER_ON_SCREEN returns...
CENTER_ON_SCREEN = wx.CENTER_ON_SCREEN if hasattr(wx, "CENTER_ON_SCREEN") else 2

# Configuration management
SPLIni = os.path.join(globalVars.appArgs.configPath, "splstudio.ini")
SPLProfiles = os.path.join(globalVars.appArgs.configPath, "addons", "stationPlaylist", "profiles")
# New (7.0) style config.
confspec = ConfigObj(StringIO("""
[General]
BeepAnnounce = boolean(default=false)
MessageVerbosity = option("beginner", "advanced", default="beginner")
BrailleTimer = option("off", "intro", "outro", "both", default="off")
AlarmAnnounce = option("beep", "message", "both", default="beep")
TrackCommentAnnounce = option("off", "beep", "message", "both", default="off")
LibraryScanAnnounce = option("off", "ending", "progress", "numbers", default="off")
CategorySounds = boolean(default=false)
TopBottomAnnounce = boolean(default=true)
RequestsAlert = boolean(default=true)
MetadataReminder = option("off", "startup", "instant", default="off")
TimeHourAnnounce = boolean(default=true)
ExploreColumns = string_list(default=list("Artist","Title","Duration","Intro","Category","Filename","Year","Album","Genre","Time Scheduled"))
ExploreColumnsTT = string_list(default=list("Artist","Title","Duration","Cue","Overlap","Intro","Segue","Filename","Album","CD Code"))
ExploreColumnsCreator = string_list(default=list("Artist","Title","Position","Cue","Intro","Segue","Duration","Last Scheduled","7 Days","Date Restriction"))
VerticalColumnAnnounce = option(None,"Status","Artist","Title","Duration","Intro","Outro","Category","Year","Album","Genre","Mood","Energy","Tempo","BPM","Gender","Rating","Filename","Time Scheduled",default=None)
[PlaylistSnapshots]
DurationMinMax = boolean(default=true)
DurationAverage = boolean(default=true)
ArtistCount = boolean(default=true)
ArtistCountLimit = integer(min=0, max=10, default=5)
CategoryCount = boolean(default=true)
CategoryCountLimit = integer(min=0, max=10, default=5)
GenreCount = boolean(default=true)
GenreCountLimit = integer(min=0, max=10, default=5)
ShowResultsWindowOnFirstPress = boolean(default=false)
[IntroOutroAlarms]
SayEndOfTrack = boolean(default=true)
EndOfTrackTime = integer(min=1, max=59, default=5)
SaySongRamp = boolean(default=true)
SongRampTime = integer(min=1, max=9, default=5)
[MicrophoneAlarm]
MicAlarm = integer(min=0, max=7200, default="0")
MicAlarmInterval = integer(min=0, max=60, default=0)
[MetadataStreaming]
MetadataEnabled = bool_list(default=list(false,false,false,false,false))
[ColumnAnnouncement]
UseScreenColumnOrder = boolean(default=true)
ColumnOrder = string_list(default=list("Artist","Title","Duration","Intro","Outro","Category","Year","Album","Genre","Mood","Energy","Tempo","BPM","Gender","Rating","Filename","Time Scheduled"))
IncludedColumns = string_list(default=list("Artist","Title","Duration","Intro","Outro","Category","Year","Album","Genre","Mood","Energy","Tempo","BPM","Gender","Rating","Filename","Time Scheduled"))
IncludeColumnHeaders = boolean(default=true)
[PlaylistTranscripts]
ColumnOrder = string_list(default=list("Artist","Title","Duration","Intro","Outro","Category","Year","Album","Genre","Mood","Energy","Tempo","BPM","Gender","Rating","Filename","Time Scheduled"))
IncludedColumns = string_list(default=list("Artist","Title","Duration","Intro","Outro","Category","Year","Album","Genre","Mood","Energy","Tempo","BPM","Gender","Rating","Filename","Time Scheduled"))
[SayStatus]
SayScheduledFor = boolean(default=true)
SayListenerCount = boolean(default=true)
SayPlayingCartName = boolean(default=true)
SayPlayingTrackName = option("auto", "background", "off", default="auto")
SayStudioPlayerPosition = boolean(default=false)
[Advanced]
SPLConPassthrough = boolean(default=false)
CompatibilityLayer = option("off", "jfw", "wineyes", default="off")
ProfileTriggerThreshold = integer(min=5, max=60, default=15)
ConfUI2 = boolean(default=true)
[Update]
AutoUpdateCheck = boolean(default=true)
UpdateInterval = integer(min=0, max=180, default=30)
[Startup]
AudioDuckingReminder = boolean(default=true)
WelcomeDialog = boolean(default=true)
ConfUI2Intro = boolean(default=true)
"""), encoding="UTF-8", list_values=False)
confspec.newlines = "\r\n"
SPLConfig = None
# The following settings can be changed in profiles:
_mutatableSettings=("IntroOutroAlarms", "MicrophoneAlarm", "MetadataStreaming", "ColumnAnnouncement")
# 7.0: Profile-specific confspec (might be removed once a more optimal way to validate sections is found).
# Dictionary comprehension is better here.
confspecprofiles = {sect:key for sect, key in confspec.items() if sect in _mutatableSettings}
# Translators: The name of the default (normal) profile.
defaultProfileName = _("Normal profile")
# StationPlaylist components.
_SPLComponents_ = ("splstudio", "splcreator", "tracktool")
# Preview
_confui2changed = False

# 8.0: Run-time config storage and management will use ConfigHub data structure, a subclass of chain map.
# A chain map allows a dictionary to look up predefined mappings to locate a key.
# When mutating a value, chain map defaults to using the topmost (zeroth) map, which isn't desirable if one wishes to use a specific map.
# This also introduces a problem whereby new key/value pairs are created (highly undesirable if global settings are modified via scripts).
# Therefore the ConfigHub subclass modifies item getter/setter to give favorable treatment to the currently active "map" (broadcast profile in use), with a flag indicating the name of the currently active map.
# Using chain map also simplifies profile switching routine, as all that is needed is move the active map flag around.
# Finally, because this is a class, additional methods and properties are used, which frees the config dictionary from the burden of carrying global flags such as the name of the instant switch profile and others.
# To preserve backward compatibility with add-on 7.x, module-level functions formerly used for profile management will call corresponding methods in ConfigHub structure (to be deprecated in 9.0 and will be gone no later than 10.0).

class ConfigHub(ChainMap):
	"""A hub of broadcast profiles, a subclass of ChainMap.
	Apart from giving favorable treatments to the active map and adding custom methods and properties, this structure is identical to chain map structure.

	The constructor takes an optional parameter that specifies which StationPlaylist component opened this map.
	The default value is None, which means Studio (splstudio.exe) app module opened this.
	"""

	def __init__(self, splComponent=None):
		# Check SPL components to make sure malicious actors don't tamper with it.
		if splComponent is None: splComponent = "splstudio"
		if splComponent not in _SPLComponents_:
			raise RuntimeError("Not a StationPlaylist component, cannot create SPL add-on Config Hub database")
		# Create a "fake" map entry, to be replaced by the normal profile later.
		super(ConfigHub, self).__init__()
		# #64 (18.07): keep an eye on which SPL component opened this map.
		self.splComponents = set()
		self.splComponents.add(splComponent)
		# 17.09 only: a private variable to be set when config must become volatile.
		# 17.10: now pull it in from command line.
		self._volatileConfig = "--spl-volatileconfig" in globalVars.appArgsExtra
		self._configInMemory = "--spl-configinmemory" in globalVars.appArgsExtra
		self._normalProfileOnly = "--spl-normalprofileonly" in globalVars.appArgsExtra
		if self.configInMemory: self._normalProfileOnly = True
		# For presentational purposes.
		self.profileNames = []
		# 17.10: if config will be stored on RAM, this step is skipped, resulting in faster startup.
		# But data conversion must take place.
		if not self.configInMemory: self.maps[0] = self._unlockConfig(SPLIni, profileName=defaultProfileName, prefill=True, validateNow=True)
		else:
			self.maps[0] = ConfigObj(None, configspec = confspec, encoding="UTF-8")
			copyProfile(_SPLDefaults, self.maps[0], complete=True)
			self.maps[0].name = defaultProfileName
			self.maps[0]["ColumnAnnouncement"]["IncludedColumns"] = set(self.maps[0]["ColumnAnnouncement"]["IncludedColumns"])
			self.maps[0]["PlaylistTranscripts"]["IncludedColumns"] = set(self.maps[0]["PlaylistTranscripts"]["IncludedColumns"])
			self.maps[0]["General"]["VerticalColumnAnnounce"] = None
		self.profileNames.append(None) # Signifying normal profile.
		# Always cache normal profile upon startup.
		# 17.10: and no, not when config is volatile.
		if not self.volatileConfig:
			self._cacheConfig(self.maps[0])
			# Remove deprecated keys.
			# This action must be performed after caching, otherwise the newly modified profile will not be saved.
			deprecatedKeys = {"General":"TrackDial", "Startup":"Studio500", "PlaylistTranscripts":"TranscriptFormat"}
			for section, key in deprecatedKeys.items():
				if key in self.maps[0][section]: del self.maps[0][section][key]
		# Moving onto broadcast profiles if any.
		# 17.10: but not when only normal profile should be used.
		if not self.normalProfileOnly:
			try:
				for profile in os.listdir(SPLProfiles):
					name, ext = os.path.splitext(profile)
					if ext == ".ini":
						self.maps.append(self._unlockConfig(os.path.join(SPLProfiles, profile), profileName=name, validateNow=True))
						self.profileNames.append(name)
			except WindowsError:
				pass
		# Runtime flags (profiles and profile switching/triggers flags come from NVDA Core's ConfigManager).
		self.profiles = self.maps
		# Active profile name is retrieved via the below property function.
		self.instantSwitch = self.profiles[0]["InstantProfile"] if ("InstantProfile" in self.profiles[0] and not self.normalProfileOnly) else None
		self.timedSwitch = None
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
		if hasattr(config, "post_configSave"):
			config.post_configSave.register(self.handlePostConfigSave)

	# Various properties
	@property
	def activeProfile(self):
		return self.profiles[0].name

	@property
	def volatileConfig(self):
		return self._volatileConfig

	@property
	def normalProfileOnly(self):
		return self._normalProfileOnly

	@property
	def configInMemory(self):
		return self._configInMemory

	@property
	def configRestricted(self):
		return self.volatileConfig or self.normalProfileOnly or self.configInMemory

	# Profile switching flags.
	_profileSwitchFlags = {"instant": 0x1, "timed": 0x2}

	@property
	def switchProfileFlags(self):
		return self._switchProfileFlags

	@property
	def instantSwitchProfileActive(self):
		return bool(self._switchProfileFlags & self._profileSwitchFlags["instant"])

	@property
	def timedSwitchProfileActive(self):
		return bool(self._switchProfileFlags & self._profileSwitchFlags["timed"])

	# Unlock (load) profiles from files.
	# LTS: Allow new profile settings to be overridden by a parent profile.
	# 8.0: Don't validate profiles other than normal profile in the beginning.
	def _unlockConfig(self, path, profileName=None, prefill=False, parent=None, validateNow=False):
		# LTS: Suppose this is one of the steps taken when copying settings when instantiating a new profile.
		# If so, go through same procedure as though config passes validation tests, as all values from parent are in the right format.
		if parent is not None:
			SPLConfigCheckpoint = ConfigObj(parent, encoding="UTF-8")
			SPLConfigCheckpoint.filename = path
			SPLConfigCheckpoint.name = profileName
			return SPLConfigCheckpoint
		# For the rest.
		global _configLoadStatus # To be mutated only during unlock routine.
		# Optimization: Profiles other than normal profile contains profile-specific sections only.
		# This speeds up profile loading routine significantly as there is no need to call a function to strip global settings.
		# 7.0: What if profiles have parsing errors?
		# If so, reset everything back to factory defaults.
		try:
			SPLConfigCheckpoint = ConfigObj(path, configspec = confspec if prefill else confspecprofiles, encoding="UTF-8")
		except:
			open(path, "w").close()
			SPLConfigCheckpoint = ConfigObj(path, configspec = confspec if prefill else confspecprofiles, encoding="UTF-8")
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
		if configTest != True:
			if not configTest:
				# Case 1: restore settings to defaults when 5.x config validation has failed on all values.
				# 6.0: In case this is a user profile, apply base configuration.
				# 8.0: Call copy profile function directly to reduce overhead.
				copyProfile(_SPLDefaults, SPLConfigCheckpoint, complete=SPLConfigCheckpoint.filename == SPLIni)
				_configLoadStatus[profileName] = "completeReset"
			elif isinstance(configTest, dict):
				# Case 2: For 5.x and later, attempt to reconstruct the failed values.
				# 6.0: Cherry-pick global settings only.
				# 7.0: Go through failed sections.
				for setting in list(configTest.keys()):
					if isinstance(configTest[setting], dict):
						for failedKey in list(configTest[setting].keys()):
							# 7.0 optimization: just reload from defaults dictionary, as broadcast profiles contain profile-specific settings only.
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
			if field not in columnOrder: invalidFields+=1
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
	def createProfile(self, path, profileName=None, parent=None):
		# 17.10: No, not when restrictions are applied.
		if self.configRestricted:
			raise RuntimeError("Broadcast profiles are volatile, only normal profile is in use, or config was loaded from memory")
		self.maps.append(self._unlockConfig(path, profileName=profileName, parent=parent, validateNow=True))
		self.profileNames.append(profileName)
		self.newProfiles.add(profileName)

	# A class version of rename and delete operations.
	# Mechanics powered by similar routines in NVDA Core's config.conf.
	def renameProfile(self, oldName, newName):
		# 17.10: No, not when restrictions are applied.
		if self.configRestricted:
			raise RuntimeError("Broadcast profiles are volatile, only normal profile is in use, or config was loaded from memory")
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
			raise RuntimeError("Broadcast profiles are volatile, only normal profile is in use, or config was loaded from memory")
		# Bring normal profile to the front if it isn't.
		# Optimization: Tell the swapper that we need index to the normal profile for this case.
		configPos = self.swapProfiles(name, defaultProfileName, showSwitchIndex=True) if self.profiles[0].name == name else self.profileIndexByName(name)
		profilePos = self.profileNames.index(name)
		try:
			os.remove(self.profiles[configPos].filename)
		except WindowsError:
			pass
		del self.profiles[configPos]
		del self.profileNames[profilePos]
		self.newProfiles.discard(name)

	def _cacheConfig(self, conf):
		# 17.10: although normal profile is taken care of when the ConfigHub loads, broadcast profiles may not know about volatile config flag.
		if self.volatileConfig: return
		global _SPLCache
		import copy
		if _SPLCache is None: _SPLCache = {}
		key = None if conf.filename == SPLIni else conf.name
		_SPLCache[key] = {}
		# 8.0: Caching the dictionary (items) is enough.
		# Do not just say dict(conf) because of referencing nature of Python, hence perform a deepcopy (copying everything to a new address).
		_SPLCache[key] = copy.deepcopy(dict(conf))

	def __delitem__(self, key):
		# Consult profile-specific key first before deleting anything.
		pos = 0 if key in _mutatableSettings else [profile.name for profile in self.maps].index(defaultProfileName)
		try:
			del self.maps[pos][key]
		except KeyError:
			raise KeyError('Key not found: {0!r}'.format(key))

	def save(self):
		# Save all config profiles.
		# 17.09: but not when they are volatile.
		# 17.10: and if in-memory config flag is set.
		if (self.volatileConfig or self.configInMemory): return
		# 7.0: Save normal profile first.
		# Temporarily merge normal profile.
		# 8.0: Locate the index instead.
		normalProfile = self.profileIndexByName(defaultProfileName)
		_preSave(self.profiles[normalProfile])
		# Disk write optimization check please.
		# 8.0: Bypass this if profiles were reset.
		if self.resetHappened or shouldSave(self.profiles[normalProfile]):
			# 6.1: Transform column inclusion data structure (for normal profile) now.
			# 7.0: This will be repeated for broadcast profiles later.
			# 8.0: Conversion will happen here, as conversion to list is necessary before writing it to disk (if told to do so).
			self.profiles[normalProfile]["ColumnAnnouncement"]["IncludedColumns"] = list(self.profiles[normalProfile]["ColumnAnnouncement"]["IncludedColumns"])
			# 18.08: also convert included columns in playlist transcripts.
			self.profiles[normalProfile]["PlaylistTranscripts"]["IncludedColumns"] = list(self.profiles[normalProfile]["PlaylistTranscripts"]["IncludedColumns"])
			self.profiles[normalProfile].write()
		del self.profiles[normalProfile]
		# Now save broadcast profiles.
		for configuration in self.profiles:
			if configuration is not None:
				# 7.0: See if profiles themselves must be saved.
				# This must be done now, otherwise changes to broadcast profiles (cached) will not be saved as presave removes them.
				# 8.0: Bypass cache check routine if this is a new profile or if reset happened.
				# Takes advantage of the fact that Python's "or" operator evaluates from left to right, considerably saving time.
				if self.resetHappened or configuration.name in self.newProfiles or (configuration.name in _SPLCache and shouldSave(configuration)):
					configuration["ColumnAnnouncement"]["IncludedColumns"] = list(configuration["ColumnAnnouncement"]["IncludedColumns"])
					_preSave(configuration)
					configuration.write()
		self.newProfiles.clear()
		self.profileHistory = None

	def _saveVolatile(self, configSaveAction=False):
		# Similar to save function except keeps the config hub alive, useful for testing new options or troubleshooting settings.
		# #73: also used to save settings when notified by config save action.
		# In case this is called when NVDA exits, just follow through, as profile history and new profiles list would be cleared as part of general process cleanup.
		if self.volatileConfig:
			raise RuntimeError("SPL config is already volatile")
		if not configSaveAction: self._volatileConfig = True
		normalProfile = self.profileIndexByName(defaultProfileName)
		_preSave(self.profiles[normalProfile])
		if self.resetHappened or shouldSave(self.profiles[normalProfile]):
			# 17.09: temporarily save a copy of the current column headers set.
			includedColumnsTemp = set(self.profiles[normalProfile]["ColumnAnnouncement"]["IncludedColumns"])
			self.profiles[normalProfile]["ColumnAnnouncement"]["IncludedColumns"] = list(self.profiles[normalProfile]["ColumnAnnouncement"]["IncludedColumns"])
			# 18.08: also for Playlist Transcripts.
			includedColumnsTemp2 = set(self.profiles[normalProfile]["PlaylistTranscripts"]["IncludedColumns"])
			self.profiles[normalProfile]["PlaylistTranscripts"]["IncludedColumns"] = list(self.profiles[normalProfile]["PlaylistTranscripts"]["IncludedColumns"])
			self.profiles[normalProfile].write()
			self.profiles[normalProfile]["ColumnAnnouncement"]["IncludedColumns"] = includedColumnsTemp
			self.profiles[normalProfile]["PlaylistTranscripts"]["IncludedColumns"] = includedColumnsTemp2
			# Don't forget to update profile cache, otherwise subsequent changes are lost.
			if configSaveAction: self._cacheConfig(self.profiles[normalProfile])
		for configuration in self.profiles:
			# Normal profile is done.
			if configuration.name == defaultProfileName: continue
			if configuration is not None:
				# 7.0: See if profiles themselves must be saved.
				# This must be done now, otherwise changes to broadcast profiles (cached) will not be saved as presave removes them.
				# 8.0: Bypass cache check routine if this is a new profile or if reset happened.
				# Takes advantage of the fact that Python's "or" operator evaluates from left to right, considerably saving time.
				if self.resetHappened or configuration.name in self.newProfiles or (configuration.name in _SPLCache and shouldSave(configuration)):
					columnHeadersTemp2 = set(configuration["ColumnAnnouncement"]["IncludedColumns"])
					configuration["ColumnAnnouncement"]["IncludedColumns"] = list(configuration["ColumnAnnouncement"]["IncludedColumns"])
					_preSave(configuration)
					configuration.write()
					configuration["ColumnAnnouncement"]["IncludedColumns"] = set(columnHeadersTemp2)
					# just like normal profile, cache the profile again provided that it was done already and if options in the cache and the live profile are different.
					if configSaveAction and configuration.name in _SPLCache: self._cacheConfig(configuration)

	def handlePostConfigSave(self):
		# Call the volatile version of save function above.
		if (self.volatileConfig or self.configInMemory): return
		self._saveVolatile(configSaveAction=True)

	# Class version of module-level functions.

	# Reset config.
	# Profile indicates the name of the profile to be reset.
	def reset(self, profile=None):
		profilePool = [] if profile is not None else self.profiles
		if profile is not None:
			if not self.profileExists(profile):
				raise ValueError("The specified profile does not exist")
			else: profilePool.append(self.profileByName(profile))
		# Preview: save confui2 changes flag.
		global _confui2changed
		_confui2changed = self["Advanced"]["ConfUI2"] != _SPLDefaults["Advanced"]["ConfUI2"]
		for conf in profilePool:
			# Retrieve the profile path, as ConfigObj.reset nullifies it.
			profilePath = conf.filename
			conf.reset()
			conf.filename = profilePath
			# Although copy profile function is used, it is really a reset.
			copyProfile(_SPLDefaults, conf, complete=profilePath == SPLIni)
			# Convert certain settings to a different format.
			conf["ColumnAnnouncement"]["IncludedColumns"] = set(_SPLDefaults["ColumnAnnouncement"]["IncludedColumns"])
		# Switch back to normal profile via a custom variant of swap routine.
		if self.profiles[0].name != defaultProfileName:
			npIndex = self.profileIndexByName(defaultProfileName)
			self.profiles[0], self.profiles[npIndex] = self.profiles[npIndex], self.profiles[0]
		# 8.0 optimization: Tell other modules that reset was done in order to postpone disk writes until the end.
		self.resetHappened = True
		# 18.08: don't forget to change type for Playlist Transcripts/included columns set.
		self["PlaylistTranscripts"]["IncludedColumns"] = set(_SPLDefaults["PlaylistTranscripts"]["IncludedColumns"])

	def profileIndexByName(self, name):
		# 8.0 optimization: Only traverse the profiles list if head (active profile) or tail does not yield profile name in question.
		if name == self.profiles[0].name:
			return 0
		elif name == self.profiles[-1].name:
			return -1
		try:
			return [profile.name for profile in self.profiles].index(name)
		except ValueError:
			raise ValueError("The specified profile does not exist")

	def profileByName(self, name):
		return self.profiles[self.profileIndexByName(name)]

	# Switch between profiles.
	# This involves promoting and demoting normal profile.
	# 17.05: The appTerminating flag is used to suppress profile switching messages.
	# 17.10: this will never be invoked if only normal profile is in use or if config was loaded from memory alone.
	def switchProfile(self, prevProfile, newProfile, appTerminating=False, switchFlags=None):
		if self.normalProfileOnly or self.configInMemory:
			raise RuntimeError("Only normal profile is in use or config was loaded from memory, cannot switch profiles")
		# There are two switch flags in use, so make sure to check the highest bit.
		if switchFlags is not None and not 0 <= switchFlags < 0x4:
			raise RuntimeError("Profile switch flag out of range")
		if not appTerminating:
			from .splconfui import _configDialogOpened
			if _configDialogOpened:
				# Translators: Presented when trying to switch to an instant switch profile when add-on settings dialog is active.
				ui.message(_("Add-on settings dialog is open, cannot switch profiles"))
				return
		self.swapProfiles(prevProfile, newProfile)
		if appTerminating: return
		# Set the prev flag manually.
		self.prevProfile = prevProfile
		# Manipulated only by profile switch start/end functions.
		self._switchProfileFlags = switchFlags
		if prevProfile is not None:
			self.switchHistory.append(newProfile)
			# Translators: Presented when switch to instant switch profile was successful.
			ui.message(_("Switching to {newProfileName}").format(newProfileName = self.activeProfile))
			# Pause automatic update checking.
			if self["Update"]["AutoUpdateCheck"]:
				if splupdate: splupdate.updateCheckTimerEnd()
		else:
			self.switchHistory.pop()
			# Translators: Presented when switching from instant switch profile to a previous profile.
			ui.message(_("Returning to {previousProfile}").format(previousProfile = self.activeProfile))
			# Resume auto update checker if told to do so.
			if self["Update"]["AutoUpdateCheck"]:
				if splupdate: splupdate.updateInit()
		# #38 (17.11/15.10-LTS): can't wait two seconds for microphone alarm to stop.
		# #40 (17.12): all taken care of by profile switched notification.
		splactions.SPLActionProfileSwitched.notify()

	# Switch start/end functions.
	# To be called from the module when starting or ending a profile switch.
	# The only difference is the switch type, which will then set appropriate flag to be passed to switchProfile method above, with xor used to set the flags.
	def switchProfileStart(self, prevProfile, newProfile, switchType):
		if switchType not in ("instant", "timed"):
			raise RuntimeError("Incorrect profile switch type specified")
		if switchType == "instant" and self.instantSwitchProfileActive:
			raise RuntimeError("Instant switch flag is already on")
		elif switchType == "timed" and self.timedSwitchProfileActive:
			raise RuntimeError("Timed switch flag is already on")
		spldebugging.debugOutput("Profile switching start: type = %s, previous profile is %s, new profile is %s"%(switchType, prevProfile, newProfile))
		self.switchProfile(prevProfile, newProfile, switchFlags=self._switchProfileFlags ^ self._profileSwitchFlags[switchType])
		# 8.0: Cache the new profile.
		global _SPLCache
		# 18.03: be sure to check if config cache is even online.
		if _SPLCache is not None and newProfile != defaultProfileName and newProfile not in _SPLCache:
			self._cacheConfig(self.profileByName(newProfile))

	def switchProfileEnd(self, prevProfile, newProfile, switchType):
		if switchType not in ("instant", "timed"):
			raise RuntimeError("Incorrect profile switch type specified")
		if switchType == "instant" and not self.instantSwitchProfileActive:
			raise RuntimeError("Instant switch flag is already off")
		elif switchType == "timed" and not self.timedSwitchProfileActive:
			raise RuntimeError("Timed switch flag is already off")
		spldebugging.debugOutput("Profile switching end: type = %s, previous profile is %s, new profile is %s"%(switchType, prevProfile, newProfile))
		self.switchProfile(prevProfile, newProfile, switchFlags=self._switchProfileFlags ^ self._profileSwitchFlags[switchType])

	# Used from config dialog and other places.
	# Show switch index is used when deleting profiles so it doesn't have to look up index for old profiles.
	def swapProfiles(self, prevProfile, newProfile, showSwitchIndex=False):
		former, current = self.profileIndexByName(prevProfile if prevProfile is not None else self.switchHistory[-1]), self.profileIndexByName(newProfile)
		self.profiles[current], self.profiles[former] = self.profiles[former], self.profiles[current]
		if showSwitchIndex: return current


# Default config spec container.
# To be moved to a different place in 8.0.
_SPLDefaults = ConfigObj(None, configspec = confspec, encoding="UTF-8")
_val = Validator()
_SPLDefaults.validate(_val, copy=True)

# Display an error dialog when configuration validation fails.
def runConfigErrorDialog(errorText, errorType):
	wx.CallAfter(gui.messageBox, errorText, errorType, wx.OK|wx.ICON_ERROR)

# In case one or more profiles had config issues, look up the error message from the following map.
_configErrors ={
	"fileReset":"Settings reset to defaults due to configuration file coruption",
	"completeReset":"All settings reset to defaults",
	"partialReset":"Some settings reset to defaults",
	"columnOrderReset":"Column announcement order reset to defaults",
	"partialAndColumnOrderReset":"Some settings, including column announcement order reset to defaults",
	"noInstantProfile":"Cannot find instant profile"
}

# To be run in app module constructor.
# With the load function below, prepare config and other things upon request.
# Prompt the config error dialog only once.
_configLoadStatus = {} # Key = filename, value is pass or no pass.
# Track comments map.
trackComments = {}

# Open config database, used mostly from modules other than Studio.
def openConfig(splComponent):
	global SPLConfig
	# #64 (18.07): skip this step if another SPL component (such as Creator) opened this.
	if SPLConfig is None: SPLConfig = ConfigHub(splComponent=splComponent)
	else: SPLConfig.splComponents.add(splComponent)

def initialize():
	# Load the default config from a list of profiles.
	# 8.0: All this work will be performed when ConfigHub loads.
	global SPLConfig, _configLoadStatus, trackComments
	# 7.0: Store the config as a dictionary.
	# This opens up many possibilities, including config caching, loading specific sections only and others (the latter saves memory).
	# 8.0: Replaced by ConfigHub object.
	# #64 (18.07): perfomed by openConfig function.
	openConfig("splstudio")
	# Locate instant profile and do something otherwise.
	if SPLConfig.instantSwitch is not None and SPLConfig.instantSwitch not in SPLConfig.profileNames:
		spldebugging.debugOutput("Failed to locate instant switch profile")
		_configLoadStatus[SPLConfig.activeProfile] = "noInstantProfile"
		SPLConfig.instantSwitch = None
	# LTS: Load track comments if they exist.
	# This must be a separate file (another pickle file).
	# 8.0: Do this much later when a track is first focused.
	try:
		trackComments = pickle.load(file(os.path.join(globalVars.appArgs.configPath, "spltrackcomments.pickle"), "r"))
	except (IOError, EOFError):
		pass
	if len(_configLoadStatus):
		# Translators: Standard error title for configuration error.
		title = _("Studio add-on Configuration error")
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
				messages.append("{profileName}: {errorMessage}".format(profileName = profile, errorMessage = error))
		_configLoadStatus.clear()
		runConfigErrorDialog("\n".join(messages), title)
	# Fire up profile triggers.
	# 17.10: except when normal profile only flag is specified.
	if not SPLConfig.normalProfileOnly: initProfileTriggers()
	# 7.1: Make sure encoder settings map isn't corrupted.
	try:
		streamLabels = ConfigObj(os.path.join(globalVars.appArgs.configPath, "splStreamLabels.ini"))
	except:
		open(os.path.join(globalVars.appArgs.configPath, "splStreamLabels.ini"), "w").close()
		# Translators: Message displayed if errors were found in encoder configuration file.
		runConfigErrorDialog(_("Your encoder settings had errors and were reset to defaults. If you have stream labels configured for various encoders, please add them again."),
		# Translators: Title of the encoder settings error dialog.
		_("Encoder settings error"))

# Cache a copy of the loaded config.
# This comes in handy when saving configuration to disk. For the most part, no change occurs to config.
# This helps prolong life of a solid-state drive (preventing unnecessary writes).
_SPLCache = {}

# Record profile triggers.
# Each record (profile name) consists of seven fields organized as a list:
# A bit vector specifying which days should this profile be active, the first five fields needed for constructing a datetime.datetime object used to look up when to trigger this profile, and an integer specifying the duration in minutes.
profileTriggers = {} # Using a pickle is quite elegant.
profileTriggers2 = {} # For caching purposes.
# Profile triggers pickle.
SPLTriggersFile = os.path.join(globalVars.appArgs.configPath, "spltriggers.pickle")
# Trigger timer.
triggerTimer = None

# Prepare the triggers dictionary and other runtime support.
def initProfileTriggers():
	# Make sure config hub is ready.
	if SPLConfig is None:
		raise RuntimeError("ConfigHub is unavailable, profile triggers manager cannot start")
	global profileTriggers, profileTriggers2
	try:
		profileTriggers = pickle.load(file(SPLTriggersFile, "r"))
	except IOError:
		profileTriggers = {}
	# Cache profile triggers, used to compare the runtime dictionary against the cache.
	profileTriggers2 = dict(profileTriggers)
	# Is the triggers dictionary and the config pool in sync?
	if len(profileTriggers):
		spldebugging.debugOutput("trigger profiles found, verifying existence of profiles")
		nonexistent = []
		for profile in list(profileTriggers.keys()):
			try:
				SPLConfig.profileIndexByName(profile)
			except ValueError:
				spldebugging.debugOutput("profile %s does not exist"%profile)
				nonexistent.append(profile)
				del profileTriggers[profile]
		if len(nonexistent):
			# Translators: Message presented indicating missing time-based profiles.
			wx.CallAfter(gui.messageBox, _("Could not locate the following time-based profile(s):\n{profiles}").format(profiles = ", ".join(nonexistent)),
			# Translators: The title of a dialog shown when some time-based profiles doesn't exist.
			_("Time-based profiles missing"), wx.OK|wx.ICON_ERROR)
	triggerStart()

# Locate time-based profiles if any.
# A 4-tuple will be returned, containing the next trigger time (for time delta calculation), the profile name for this trigger time, whether an immediate switch is necessary, and if so, the duration delta for profiles with duration entry specified.
def nextTimedProfile(current=None):
	if current is None: current = datetime.datetime.now()
	# No need to proceed if no timed profiles are defined.
	if not len(profileTriggers): return None
	possibleTriggers = []
	for profile in list(profileTriggers.keys()):
		shouldBeSwitched = False
		entry = list(profileTriggers[profile])
		# Construct the comparison datetime (see the profile triggers spec).
		triggerTime = datetime.datetime(entry[1], entry[2], entry[3], entry[4], entry[5])
		# Hopefully the trigger should be ready before the show, but sometimes it isn't.
		if current > triggerTime:
			# #52 (18.03/15.14-LTS): check the duration field first.
			durationDelta = (current-triggerTime).seconds
			if durationDelta < (entry[6]*60):
				# Return the tuple immediately, as the show is more important.
				return (triggerTime, profile, True, (entry[6]*60) - durationDelta)
			else: profileTriggers[profile] = setNextTimedProfile(profile, entry[0], datetime.time(entry[4], entry[5]), date=current, duration=entry[6])
		possibleTriggers.append((triggerTime, profile, shouldBeSwitched, None))
	return min(possibleTriggers) if len(possibleTriggers) else None

# Some helpers used in locating next air date/time.

# Set the next timed profile.
# Bits indicate the trigger days vector, hhmm is time, with the optional date being a specific date otherwise current date.
def setNextTimedProfile(profile, bits, switchTime, date=None, duration=0):
	if date is None: date = datetime.datetime.now()
	dayIndex = date.weekday()
	triggerCandidate = 64 >> dayIndex
	currentTime = datetime.time(date.hour, date.minute, date.second, date.microsecond)
	# Case 1: Show hasn't begun.
	if (bits & triggerCandidate) and currentTime < switchTime:
		delta = 0
	else:
		# Case 2: This is a weekly show.
		if bits == triggerCandidate:
			delta = 7
		else:
			import math
			# Scan the bit vector until finding the correct date and calculate the resulting delta (dayIndex modulo 7).
			# Take away the current trigger bit as this is invoked once the show air date has passed.
			days = bits-triggerCandidate if bits & triggerCandidate else bits
			currentDay = int(math.log(triggerCandidate, 2))
			nextDay = int(math.log(days, 2))
			# Hoping the resulting vector will have some bits set to 1...
			if triggerCandidate > days:
				delta = currentDay-nextDay
			else:
				triggerBit = -1
				for bit in rangeGen(currentDay-1, -1, -1):
					if 2 ** bit & days:
						triggerBit = bit
						break
				if triggerBit > -1:
					delta = currentDay-triggerBit
				else:
					delta = 7-(nextDay-currentDay)
	date += datetime.timedelta(delta)
	return [bits, date.year, date.month, date.day, switchTime.hour, switchTime.minute, duration]

# Find if another profile is occupying the specified time slot.
def duplicateExists(map, profile, bits, hour, min, duration):
	if len(map) == 0 or (len(map) == 1 and profile in map): return False
	# Convert hours and minutes to an integer for faster comparison.
	start1 = (hour*60) + min
	end1 = start1+duration
	# A possible duplicate may exist simply because of bits.
	# 17.09: find a replacement for the below expression that'll work across Python releases.
	for item in filter(lambda p: p != profile, map.keys()):
		if map[item][0] == bits:
			entry = map[item]
			start2 = (entry[4] * 60) + entry[5]
			end2 = start2+entry[6]
			if start1 <= start2 <= end1 or start2 <= start1 <= end2:
				return True
	return False

# Start the trigger timer based on above information.
# Can be restarted if needed.
def triggerStart(restart=False):
	global SPLConfig, triggerTimer
	# Restart the timer when called from triggers dialog in order to prevent multiple timers from running.
	if triggerTimer is not None and triggerTimer.IsRunning() and restart:
		triggerTimer.Stop()
		triggerTimer = None
	queuedProfile = nextTimedProfile()
	if queuedProfile is not None:
		try:
			SPLTriggerProfile = queuedProfile[1]
		except ValueError:
			SPLTriggerProfile = None
		# 17.08: The config hub object will now keep an eye on this.
		SPLConfig.timedSwitch = SPLTriggerProfile
		# We are in the midst of a show, so switch now.
		if queuedProfile[2]:
			# Only come here if this is the first time this function is run (startup).
			if not restart: triggerProfileSwitch(durationDelta = queuedProfile[3])
			else:
				# restart the timer if required.
				global _SPLTriggerEndTimer
				if _SPLTriggerEndTimer is not None and _SPLTriggerEndTimer.IsRunning():
					_SPLTriggerEndTimer.Stop()
					_SPLTriggerEndTimer = wx.PyTimer(triggerProfileSwitch)
					_SPLTriggerEndTimer.Start(queuedProfile[3] * 1000, True)
				else: triggerProfileSwitch(durationDelta = queuedProfile[3])
		else:
			switchAfter = (queuedProfile[0] - datetime.datetime.now())
			if switchAfter.days == 0 and switchAfter.seconds <= 3600:
				time.sleep((switchAfter.microseconds+1000) / 1000000.0)
				from .splmisc import SPLCountdownTimer
				triggerTimer = SPLCountdownTimer(switchAfter.seconds, triggerProfileSwitch, SPLConfig["Advanced"]["ProfileTriggerThreshold"])
				triggerTimer.Start()

# Dump profile triggers pickle away.
def saveProfileTriggers():
	global triggerTimer, profileTriggers, profileTriggers2
	if triggerTimer is not None and triggerTimer.IsRunning():
		triggerTimer.Stop()
		triggerTimer = None
	# Unless it is a daily show, profile triggers would not have been modified.
	# This trick is employed in order to reduce unnecessary disk writes.
	if profileTriggers != profileTriggers2:
		pickle.dump(profileTriggers, file(SPLTriggersFile, "wb"))
	profileTriggers = None
	profileTriggers2 = None

# Copy settings across profiles.
# Setting complete flag controls whether profile-specific settings are applied (true otherwise, only set when resetting profiles).
# 8.0: Simplified thanks to in-place swapping.
# 17.10: is this necessary now?
def copyProfile(sourceProfile, targetProfile, complete=False):
	for section in list(sourceProfile.keys()) if complete else _mutatableSettings:
		targetProfile[section] = dict(sourceProfile[section])

# Last but not least...
# Module level version of get profile flags function.
# Optional keyword arguments are to be added when called from dialogs such as add-on settings.
# A crucial kwarg is contained, and if so, profile flags set will be returned.
def getProfileFlags(name, active=None, instant=None, triggers=None, contained=False):
	flags = set()
	if active is None: active = SPLConfig.activeProfile
	if instant is None: instant = SPLConfig.instantSwitch
	if triggers is None: triggers = profileTriggers
	if name == active:
		# Translators: A flag indicating the currently active broadcast profile.
		flags.add(_("active"))
	if name == instant:
		# Translators: A flag indicating the broadcast profile is an instant switch profile.
		flags.add(_("instant switch"))
	if name in triggers:
		# Translators: A flag indicating the time-based triggers profile.
		flags.add(_("time-based"))
	if not contained:
		return name if len(flags) == 0 else "{0} <{1}>".format(name, ", ".join(flags))
	else: return flags

# Perform some extra work before writing the config file.
def _preSave(conf):
	# Perform global setting processing only for the normal profile.
	# 7.0: if this is a second pass, index 0 may not be normal profile at all.
	# Use profile path instead.
	if conf.filename == SPLIni:
		SPLSwitchProfile = SPLConfig.instantSwitch
		# Cache instant profile for later use.
		if SPLSwitchProfile is not None:
			conf["InstantProfile"] = SPLSwitchProfile
		else:
			try:
				del conf["InstantProfile"]
			except KeyError:
				pass
	# For other profiles, remove global settings before writing to disk.
	else:
		# 6.1: Make sure column inclusion aren't same as default values.
		if len(conf["ColumnAnnouncement"]["IncludedColumns"]) == 17:
			del conf["ColumnAnnouncement"]["IncludedColumns"]
		for setting in list(conf.keys()):
			for key in list(conf[setting].keys()):
				try:
					if conf[setting][key] == _SPLDefaults[setting][key]:
						del conf[setting][key]
				except KeyError:
					pass
			if setting in conf and not len(conf[setting]):
				del conf[setting]

# Check if the profile should be written to disk.
# For the most part, no setting will be modified.
def shouldSave(profile):
	tree = None if profile.filename == SPLIni else profile.name
	# 8.0: Streamline the whole process by comparing values alone instead of walking the entire dictionary.
	# The old loop will be kept in 7.x/LTS for compatibility and to reduce risks associated with accidental saving/discard.
	return _SPLCache[tree] != profile

# Close config database if needed.
def closeConfig(splComponent):
	global SPLConfig, _SPLCache
	SPLConfig.splComponents.discard(splComponent)
	if len(SPLConfig.splComponents) == 0:
		SPLConfig.save()
		SPLConfig = None
		_SPLCache.clear()
		_SPLCache = None

# Terminate the config and related subsystems.
def terminate():
	global SPLConfig, _SPLCache, _SPLTriggerEndTimer, _triggerProfileActive
	# #30 (17.05): If we come here before a time-based profile expires, the trigger end timer will meet a painful death.
	if _SPLTriggerEndTimer is not None and _SPLTriggerEndTimer.IsRunning():
		_SPLTriggerEndTimer.Stop()
		_SPLTriggerEndTimer = None
		SPLConfig.switchProfile(None, SPLConfig.prevProfile, appTerminating=True)
		_triggerProfileActive = False
	# Close profile triggers dictionary.
	# 17.10: but if only the normal profile is in use, it won't do anything.
	if not SPLConfig.normalProfileOnly: saveProfileTriggers()
	# Dump track comments.
	pickle.dump(trackComments, file(os.path.join(globalVars.appArgs.configPath, "spltrackcomments.pickle"), "wb"))
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
		# Translators: Presented when trying to switch to an instant switch profile when the instant switch profile is not defined.
		ui.message(_("No instant switch profile is defined"))
	else:
		if SPLConfig.prevProfile is None:
			if SPLConfig.activeProfile == SPLSwitchProfile:
				# Translators: Presented when trying to switch to an instant switch profile when one is already using the instant switch profile.
				ui.message(_("You are already in the instant switch profile"))
				return
			# Switch to the given profile.
			# 6.1: Do to referencing nature of Python, use the profile index function to locate the index for the soon to be deactivated profile.
			# 7.0: Store the profile name instead in order to prevent profile index mangling if profiles are deleted.
			# Pass in the prev profile, which will be None for instant profile switch.
			# 7.0: Now activate "activeProfile" argument which controls the behavior of the function below.
			# 8.0: Work directly with profile names.
			# 18.03: call switch profile start method directly.
			# To the outside, a profile switch took place.
			SPLConfig.switchProfileStart(SPLConfig.activeProfile, SPLSwitchProfile, "instant")
		else:
			SPLConfig.switchProfileEnd(None, SPLConfig.prevProfile, "instant")

# The triggers version of the above function.
_SPLTriggerEndTimer = None
# Record if time-based profile is active or not.
_triggerProfileActive = False

# Duration delta refers to update profile switch duration (in seconds) while switching in the middle of a show.
def triggerProfileSwitch(durationDelta=None):
	global SPLConfig, triggerTimer, _SPLTriggerEndTimer, _triggerProfileActive
	SPLTriggerProfile = SPLConfig.timedSwitch
	if SPLTriggerProfile is None and _triggerProfileActive:
		raise RuntimeError("Trigger profile flag cannot be active when the trigger profile itself isn't defined")
	if SPLConfig.prevProfile is None:
		if SPLConfig.activeProfile == SPLTriggerProfile:
			# Translators: Presented when trying to switch to an instant switch profile when one is already using the instant switch profile.
			ui.message(_("A profile trigger is already active"))
			return
		SPLConfig.switchProfileStart(SPLConfig.activeProfile, SPLTriggerProfile, "timed")
		# Set the global trigger flag to inform various subsystems such as add-on settings dialog.
		_triggerProfileActive = True
		# Set the next trigger date and time.
		triggerSettings = profileTriggers[SPLTriggerProfile]
		# Set next trigger if no duration is specified.
		if triggerSettings[6] == 0:
			profileTriggers[SPLTriggerProfile] = setNextTimedProfile(SPLTriggerProfile, triggerSettings[0], datetime.time(triggerSettings[4], triggerSettings[5]))
		else:
			_SPLTriggerEndTimer = wx.PyTimer(triggerProfileSwitch)
			_SPLTriggerEndTimer.Start(triggerSettings[6] * 60 * 1000 if durationDelta is None else durationDelta * 1000, True)
	else:
		SPLConfig.switchProfileEnd(None, SPLConfig.prevProfile, "timed")
		_triggerProfileActive = False
		# Stop the ending timer.
		if _SPLTriggerEndTimer is not None and _SPLTriggerEndTimer.IsRunning():
			_SPLTriggerEndTimer.Stop()
			_SPLTriggerEndTimer = None

# Let SPL track item know if it needs to build description pieces.
# To be renamed and used in other places in 7.0.
def _shouldBuildDescriptionPieces():
	return (not SPLConfig["ColumnAnnouncement"]["UseScreenColumnOrder"]
	and (SPLConfig["ColumnAnnouncement"]["ColumnOrder"] != _SPLDefaults["ColumnAnnouncement"]["ColumnOrder"]
	or len(SPLConfig["ColumnAnnouncement"]["IncludedColumns"]) != 17))

# Additional configuration and miscellaneous dialogs
# See splconfui module for basic configuration dialogs.

# Startup dialogs.

# Audio ducking reminder (NVDA 2016.1 and later).
class AudioDuckingReminder(wx.Dialog):
	"""A dialog to remind users to turn off audio ducking (NVDA 2016.1 and later).
	"""

	def __init__(self, parent):
		# Translators: Title of a dialog displayed when the add-on starts reminding broadcasters to disable audio ducking.
		super(AudioDuckingReminder, self).__init__(parent, title=_("SPL Studio and audio ducking"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)

		# Translators: A message displayed if audio ducking should be disabled.
		label = wx.StaticText(self, wx.ID_ANY, label=_("""NVDA 2016.1 and later allows NVDA to decrease volume of background audio including that of Studio.
		In order to not disrupt the listening experience of your listeners, please disable audio ducking either by:
		* Opening synthesizer dialog in NVDA and selecting 'no ducking' from audio ducking mode combo box.
		* Press NVDA+Shift+D to set it to 'no ducking'."""))
		mainSizer.Add(label,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		# Translators: A checkbox to turn off audio ducking reminder message.
		self.audioDuckingReminder=wx.CheckBox(self,wx.ID_ANY,label=_("Do not show this message again"))
		self.audioDuckingReminder.SetValue(not SPLConfig["Startup"]["AudioDuckingReminder"])
		mainSizer.Add(self.audioDuckingReminder, border=10,flag=wx.TOP)

		mainSizer.Add(self.CreateButtonSizer(wx.OK), flag=wx.ALIGN_CENTER_HORIZONTAL)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.audioDuckingReminder.SetFocus()
		self.Center(wx.BOTH | CENTER_ON_SCREEN)

	def onOk(self, evt):
		global SPLConfig
		if self.audioDuckingReminder.Value:
			SPLConfig["Startup"]["AudioDuckingReminder"] = not self.audioDuckingReminder.Value
		self.Destroy()

# Welcome dialog (emulating NvDA Core)
class WelcomeDialog(wx.Dialog):

	# Translators: A message giving basic information about the add-on.
	welcomeMessage=_("""Welcome to StationPlaylist Studio add-on for NVDA,
your companion to broadcasting with SPL Studio using NVDA screen reader.

Highlights of StationPlaylist Studio add-on include:
* Layer commands for obtaining status information.
* Various ways to examine track columns.
* Various ways to find tracks.
* Cart Explorer to learn cart assignments.
* Comprehensive settings and documentation.
* Check for add-on updates automatically or manually.
* Completely free, open-source and community-driven.
* And much more.

Visit www.stationplaylist.com for details on StationPlaylist Studio.
Visit StationPlaylist entry on NVDA Community Add-ons page (addons.nvda-project.org) for more information on the add-on and to read the documentation.
Want to see this dialog again? Just press Alt+NVDA+F1 while using Studio to return to this dialog.
Have something to say about the add-on? Press Control+NVDA+hyphen (-) to send a feedback to the developer of this add-on using your default email program.

Thank you.""")

	def __init__(self, parent):
		# Translators: Title of a dialog displayed when the add-on starts presenting basic information, similar to NVDA's own welcome dialog.
		super(WelcomeDialog, self).__init__(parent, title=_("Welcome to StationPlaylist Studio add-on"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)

		label = wx.StaticText(self, wx.ID_ANY, label=self.welcomeMessage)
		mainSizer.Add(label,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		# Translators: A checkbox to show welcome dialog.
		self.showWelcomeDialog=wx.CheckBox(self,wx.ID_ANY,label=_("Show welcome dialog when I start Studio"))
		self.showWelcomeDialog.SetValue(SPLConfig["Startup"]["WelcomeDialog"])
		mainSizer.Add(self.showWelcomeDialog, border=10,flag=wx.TOP)

		mainSizer.Add(self.CreateButtonSizer(wx.OK), flag=wx.ALIGN_CENTER_HORIZONTAL)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.showWelcomeDialog.SetFocus()
		self.Center(wx.BOTH | CENTER_ON_SCREEN)

	def onOk(self, evt):
		global SPLConfig
		SPLConfig["Startup"]["WelcomeDialog"] = self.showWelcomeDialog.Value
		self.Destroy()

# And to open the above dialog and any other dialogs.
# LTS18: return immediately after opening old ver dialog if minimal flag is set.
def showStartupDialogs(oldVer=False, oldVerReturn=False):
	# Old version reminder if this is such a case.
	# 17.10: and also used to give people a chance to switch to LTS.
	# To be resurrected later.
	#if oldVer and os.path.exists(os.path.join(globalVars.appArgs.configPath, "addons", "stationPlaylist", "ltsprep")):
		#if gui.messageBox("You are using an older version of Windows. From 2018 onwards, Studio add-on will not support versions earlier than Windows 7 Service Pack 1. Add-on 15.x LTS (long-term support) versions will support Windows versions such as Windows XP until mid-2018. Would you like to switch to long-term support release?", "Long-Term Support version", wx.YES | wx.NO | wx.CANCEL | wx.CENTER | wx.ICON_QUESTION) == wx.YES:
			#splupdate.SPLUpdateChannel = "lts"
			#os.remove(os.path.join(globalVars.appArgs.configPath, "addons", "stationPlaylist", "ltsprep"))
	#if oldVerReturn: return
	if SPLConfig["Startup"]["WelcomeDialog"]:
		gui.mainFrame.prePopup()
		WelcomeDialog(gui.mainFrame).Show()
		gui.mainFrame.postPopup()
	import audioDucking
	if SPLConfig["Startup"]["AudioDuckingReminder"] and audioDucking.isAudioDuckingSupported():
		gui.mainFrame.prePopup()
		AudioDuckingReminder(gui.mainFrame).Show()
		gui.mainFrame.postPopup()
	# Preview: present intro message for multi-page add-on settings interface (NVDA 2018.2 and later).
	import versionInfo
	if (versionInfo.version_year, versionInfo.version_major) >= (2018, 2) and SPLConfig["Startup"]["ConfUI2Intro"]:
		SPLConfig["Startup"]["ConfUI2Intro"] = False
		wx.CallAfter(gui.messageBox, "It appears you are running NVDA 2018.2 or later. NVDA 2018.2 brings a redesigned NVDA Settings interface that allows you to visit all settings categories and make changes to various options without opening individual preferences dialogs. Inspired by this change, Studio add-on will display its add-on settings in multi-page interface format where settings are grouped under categories. If you want the old add-on settings interface where you opened dialogs for various options, open add-on settings, go to Advanced, then uncheck a checkbox named 'Use multi-page add-on settings interface (preview)', then select OK and restart NVDA. To return to the new format, repeat these steps, this time checking the checkbox.", "New add-on settings interface", wx.OK|wx.ICON_INFORMATION)

# Message verbosity pool.
# To be moved to its own module in add-on 7.0.
# This is a multimap, consisting of category, value and message.
# Most of the categories are same as confspec keys, hence the below message function is invoked when settings are changed.
def message(category, value):
	verbosityLevels = ("beginner", "advanced")
	ui.message(messagePool[category][value][verbosityLevels.index(SPLConfig["General"]["MessageVerbosity"])])

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

# Handle several cases that disables update feature completely (or partially).
SPLUpdateErrorNone = 0
SPLUpdateErrorGeneric = 1
SPLUpdateErrorSecureMode = 2
SPLUpdateErrorTryBuild = 3
SPLUpdateErrorSource = 4
SPLUpdateErrorAppx = 5
SPLUpdateErrorAddonsManagerUpdate = 6
SPLUpdateErrorNoNetConnection = 7

# These conditions are set when NVDA starts and cannot be changed at runtime, hence major errors.
# This means no update channel selection, no retrys, etc.
SPLUpdateMajorErrors = (SPLUpdateErrorSecureMode, SPLUpdateErrorTryBuild, SPLUpdateErrorSource, SPLUpdateErrorAppx, SPLUpdateErrorAddonsManagerUpdate)

updateErrorMessages={
	# Translators: one of the error messages when trying to update the add-on.
	SPLUpdateErrorGeneric: _("An error occured while checking for add-on update. Please check NVDA log for details."),
	# Translators: one of the error messages when trying to update the add-on.
	SPLUpdateErrorSecureMode: _("NVDA is in secure mode. Please restart with secure mode disabled before checking for add-on updates."),
	# Translators: one of the error messages when trying to update the add-on.
	SPLUpdateErrorTryBuild: _("This is a try build of StationPlaylist Studio add-on. Please install the latest stable release to receive updates again."),
	# Translators: one of the error messages when trying to update the add-on.
	SPLUpdateErrorSource: _("Update checking not supported while running NVDA from source. Please run this add-on from an installed or a portable version of NVDA."),
	# Translators: one of the error messages when trying to update the add-on.
	SPLUpdateErrorAppx: _("This is a Windows Store version of NVDA. Add-on updating is supported on desktop version of NVDA."),
	# Translators: one of the error messages when trying to update the add-on.
	SPLUpdateErrorAddonsManagerUpdate: _("Cannot update add-on directly. Please check for add-on updates by going to add-ons manager."),
	# Translators: one of the error messages when trying to update the add-on.
	SPLUpdateErrorNoNetConnection: _("No internet connection. Please connect to the internet before checking for add-on update."),
}

# Check to really make sure add-on updating is supported.
# Contrary to its name, 0 means yes, otherwise no.
# For most cases, it'll return no errors except for scenarios outlined below.
# The generic error (1) is meant to catch all errors not listed here, and for now, not used.
def isAddonUpdatingSupported():
	if globalVars.appArgs.secure:
		return SPLUpdateErrorSecureMode
	if "--spl-customtrybuild" in globalVars.appArgsExtra:
		return SPLUpdateErrorTryBuild
	import versionInfo
	if not versionInfo.updateVersionType:
		return SPLUpdateErrorSource
	# NVDA 2018.1 and later.
	if config.isAppX:
		return SPLUpdateErrorAppx
	# Provided that NVDA issue 3208 is implemented.
	if hasattr(addonHandler, "checkForAddonUpdate"):
		return SPLUpdateErrorAddonsManagerUpdate
	return SPLUpdateErrorNone

def canUpdate():
	return isAddonUpdatingSupported() == SPLUpdateErrorNone
