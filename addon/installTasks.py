# StationPlaylist add-on installation tasks
# Copyright 2015-2021 Joseph Lee, released under GPL.

# Provides needed routines during add-on installation and removal.
# Routines are partly based on other add-ons, particularly Place Markers by Noelia Martinez (thanks add-on authors).

import addonHandler
addonHandler.initTranslation()


def onInstall():
	import sys
	import gui
	import wx
	# #17.12: Windows 7 SP1 or higher is required.
	if sys.getwindowsversion().build < 7601:
		gui.messageBox(
			# Translators: Presented when attempting to install StationPlaylist add-on on unsupported Windows releases.
			_("You are using an older version of Windows. This add-on requires Windows 7 Service Pack 1 or later."),
			# Translators: Title of a dialog shown when installing StationPlaylist add-on on old Windows releases.
			_("Old Windows version"), wx.OK | wx.ICON_ERROR)
		raise RuntimeError("SPL: minimum Windows version requirement not met, aborting")
	import os
	import shutil
	profiles = os.path.join(os.path.dirname(__file__), "..", "stationPlaylist", "profiles")
	# Import old profiles.
	if os.path.exists(profiles):
		newProfiles = os.path.join(os.path.dirname(__file__), "profiles")
		try:
			shutil.copytree(profiles, newProfiles)
		except IOError:
			pass
