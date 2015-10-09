# StationPlaylist Studio add-on installation tasks
# Copyright 2015 Joseph Lee and others, released under GPL.

# Provides needed routines during add-on installation and removal.
# Routines are partly based on other add-ons, particularly Place Markers by Noelia Martinez (thanks add-on authors).

import addonHandler
import os
import shutil
from configobj import ConfigObj
from cStringIO import StringIO
import globalVars

SPLIni = os.path.join(globalVars.appArgs.configPath, "splstudio.ini")

# Old (5.0) style config.
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
TimeHourAnnouncement = boolean(default=false)
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

# New style config (used during profile conversion).
_conversionConfig = {
	"BeepAnnounce":"General",
	"MessageVerbosity":"General",
	"BrailleTimer":"General",
	"AlarmAnnounce":"General",
	"LibraryScanAnnounce":"General",
	"TrackDial":"General",
	"TimeHourAnnouncement":"General",
	"SayEndOfTrack":"IntroOutroAlarms",
	"EndOfTrackTime":"IntroOutroAlarms",
	"SaySongRamp":"IntroOutroAlarms",
	"SongRampTime":"IntroOutroAlarms",
	"MicAlarm":"MicAlarm",
	"MicAlarmInterval":"MicAlarm",
	"MetadataReminder":"MetadataStreaming",
	"MetadataEnabled":"MetadataStreaming",
	"UseScreenColumnOrder":"ColumnAnnouncement",
	"ColumnOrder":"ColumnAnnouncement",
	"IncludedColumns":"ColumnAnnouncement",
	"SayScheduledFor":"SayStatus",
	"SayListenerCount":"SayStatus",
	"SayPlayingCartName":"SayStatus",
	"SPLConPassthrough":"Advanced",
	"CompatibilityLayer":"Advanced",
}

# Invoked when upgrading to 7.0 (to be removed in 7.2).
def config6to7(path):
	profile = ConfigObj(path, configspec = confspec, encoding="UTF-8")
	# For now, manually convert.
	# 7.2: Remove old config to save disk space.
	for setting in _conversionConfig.keys():
		if setting in profile:
			print "setting found"
			section = _conversionConfig[setting]
			if section not in profile:
				print "section not found"
				profile[section] = {}
			else:
				print "section found"
			try:
				profile[section][setting] = profile[setting]
			except:
				pass
	profile.write()


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
