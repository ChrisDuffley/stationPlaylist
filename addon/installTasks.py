# StationPlaylist add-on installation tasks
# Copyright 2015-2025 Joseph Lee, released under GPL.

# Provides needed routines during add-on installation and removal.
# Partly based on other add-ons, particularly Place Markers by Noelia Martinez (thanks add-on authors).

import addonHandler

addonHandler.initTranslation()


def onInstall():
	import os
	import shutil
	import gui
	import wx
	import winVersion
	import globalVars

	# Do not present dialogs if minimal mode is set.
	currentWinVer = winVersion.getWinVer()
	# StationPlaylist add-on requires Windows 10 22H2 or later.
	# Translators: title of the error dialog shown when trying to install the add-on in unsupported systems.
	# Unsupported systems include Windows versions earlier than 10 and unsupported feature updates.
	unsupportedWindowsReleaseTitle = _("Unsupported Windows release")
	minimumWinVer = winVersion.WIN10_22H2
	if currentWinVer < minimumWinVer:
		gui.messageBox(
			_(
				# Translators: Dialog text shown when trying to install the add-on on
				# releases earlier than minimum supported release.
				"You are using {releaseName} ({build}), a Windows release not supported by this add-on.\n"
				"This add-on requires {supportedReleaseName} ({supportedBuild}) or later."
			).format(
				releaseName=currentWinVer.releaseName,
				build=currentWinVer.build,
				supportedReleaseName=minimumWinVer.releaseName,
				supportedBuild=minimumWinVer.build,
			),
			unsupportedWindowsReleaseTitle,
		)
		raise RuntimeError("Attempting to install StationPlaylist add-on on Windows releases earlier than 10")
	profiles = os.path.join(os.path.dirname(__file__), "..", "stationPlaylist", "profiles")
	# Import old profiles.
	if os.path.exists(profiles):
		newProfiles = os.path.join(os.path.dirname(__file__), "profiles")
		try:
			shutil.copytree(profiles, newProfiles)
		except IOError:
			pass
