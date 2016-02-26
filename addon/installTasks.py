# StationPlaylist Studio add-on installation tasks
# Copyright 2015-2016 Joseph Lee and others, released under GPL.

# Provides needed routines during add-on installation and removal.
# Routines are partly based on other add-ons, particularly Place Markers by Noelia Martinez (thanks add-on authors).

import addonHandler
import os
import shutil
from configobj import ConfigObj
from cStringIO import StringIO
import globalVars

SPLIni = os.path.join(globalVars.appArgs.configPath, "splstudio.ini")
SPLIni7 = os.path.join(globalVars.appArgs.configPath, "splstudio7.ini")

# New style config (used during profile conversion).
_conversionConfig = {
	"BeepAnnounce":"General",
	"MessageVerbosity":"General",
	"BrailleTimer":"General",
	"AlarmAnnounce":"General",
	"LibraryScanAnnounce":"General",
	"TrackDial":"General",
	"TimeHourAnnounce":"General",
	"SayEndOfTrack":"IntroOutroAlarms",
	"EndOfTrackTime":"IntroOutroAlarms",
	"SaySongRamp":"IntroOutroAlarms",
	"SongRampTime":"IntroOutroAlarms",
	"MicAlarm":"MicrophoneAlarm",
	"MicAlarmInterval":"MicrophoneAlarm",
	"MetadataReminder":"General",
	"MetadataEnabled":"MetadataStreaming",
	"UseScreenColumnOrder":"ColumnAnnouncement",
	"ColumnOrder":"ColumnAnnouncement",
	"IncludedColumns":"ColumnAnnouncement",
	"SayScheduledFor":"SayStatus",
	"SayListenerCount":"SayStatus",
	"SayPlayingCartName":"SayStatus",
	"SayPlayingTrackName":"SayStatus",
	"SPLConPassthrough":"Advanced",
	"CompatibilityLayer":"Advanced",
	"AudioDuckingReminder":"Startup",
}

# Invoked when upgrading to 7.0 (to be removed in 7.2).
def config6to7(path):
	# Sometimes, an exception could be thrown if ConfigObj says it cannot parse the config file, so skip offending files.
	# This means the unlock function in splconfig will handle this case.
	try:
		profile = ConfigObj(path)
	except:
		return
	# Optimization: no need to convert if sectionized.
	for section in ["General", "IntroOutroAlarms", "MicrophoneAlarm", "ColumnAnnouncement", "MetadataStreaming", "SayStatus", "Advanced", "Startup"]:
		if section in profile:
			return
	# For now, manually convert.
	# 7.2: Remove old config to save disk space.
	for setting in _conversionConfig.keys():
		if setting in profile:
			section = _conversionConfig[setting]
			if section not in profile:
				profile[section] = {}
				profile[section][setting] = profile[setting]
			else:
				try:
					profile[section][setting] = profile[setting]
				except:
					pass
	# Just in case studio is running.
	# If so, when the app module exits, it'll rewrite the whole config, so save the converted config somewhere to be imported by the app module later.
	if path == SPLIni:
		profile7 = ConfigObj(SPLIni7)
		for key in profile:
			profile7[key] = profile[key]
		# 7.0 only: Change track name announcement value, to be removed in add-on 7.1.
		sayPlayingTrackName = profile["SayPlayingTrackName"]
		if sayPlayingTrackName == "True": sayPlayingTrackName = "auto"
		elif sayPlayingTrackName == "Background": sayPlayingTrackName = "background"
		elif sayPlayingTrackName == "False": sayPlayingTrackName = "off"
		profile7["SayStatus"]["SayPlayingTrackName"] = sayPlayingTrackName
		profile7.write()
	else: profile.write()


def onInstall():
	# 7.0: Convert config formats, starting with normal profile.
	config6to7(SPLIni)
	profiles = os.path.join(os.path.dirname(__file__), "..", "stationPlaylist", "profiles")
	# Import old profiles.
	if os.path.exists(profiles):
		newProfiles = os.path.join(os.path.dirname(__file__), "profiles")
		try:
			shutil.copytree(profiles, newProfiles)
		except IOError:
			pass
		# Import profiles to the new config format.
		# Do this after profiles are safely copied.
		try:
			profiles = filter(lambda fn: os.path.splitext(fn)[-1] == ".ini", os.listdir(newProfiles))
			for profile in profiles:
				config6to7(os.path.join(newProfiles, profile))
		except WindowsError:
			pass
