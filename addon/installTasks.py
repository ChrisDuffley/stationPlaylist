# StationPlaylist Studio add-on installation tasks
# Copyright 2015 Joseph Lee and others, released under GPL.

# Provides needed routines during add-on installation and removal.
# Routines are partly based on other add-ons, particularly Place Markers by Noelia Martinez (thanks add-on authors).

import addonHandler
import os
import shutil
import globalVars

def onInstall():
	profiles = os.path.join(os.path.dirname(__file__), "..", "stationPlaylist", "profiles")
	# Backup profiles to be picked up by the newly installed app module when it starts for the first time.
	if os.path.exists(profiles):
		profileBackups = os.path.join(globalVars.appArgs.configPath, "__SPLProfiles")
		try:
			shutil.copytree(profiles, profileBackups)
		except IOError:
			pass
