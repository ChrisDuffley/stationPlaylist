# StationPlaylist add-on installation tasks
# Copyright 2015-2025 Joseph Lee, released under GPL.

# Provides needed routines during add-on installation and removal.
# Partly based on other add-ons, particularly Place Markers by Noelia Martinez (thanks add-on authors).

import os
import shutil

def onInstall():
	profiles = os.path.join(os.path.dirname(__file__), "..", "stationPlaylist", "profiles")
	# Import old profiles.
	if os.path.exists(profiles):
		newProfiles = os.path.join(os.path.dirname(__file__), "profiles")
		try:
			shutil.copytree(profiles, newProfiles)
		except IOError:
			pass
