# StationPlaylist Studio add-on installation tasks
# Copyright 2015-2017 Joseph Lee and others, released under GPL.

# Provides needed routines during add-on installation and removal.
# Routines are partly based on other add-ons, particularly Place Markers by Noelia Martinez (thanks add-on authors).

import sys
import gui
import wx
import addonHandler
addonHandler.initTranslation()

def onInstall():
	# #17.12: Windows 7 SP1 or higher is required.
	if sys.getwindowsversion().build < 7601:
		# Translators: Presented when attempting to install Studio add-on on unsupported Windows releases.
		gui.messageBox(_("You are using an older version of Windows. This add-on requires Windows 7 Service Pack 1 or later."),
			# Translators: Title of a dialog shown when installing Studio add-on on old Windows releases.
			_("Old Windows version"), wx.OK | wx.ICON_ERROR)
		raise RuntimeError("SPL: minimum Windows version requirement not met, aborting")
	import os, shutil, inputCore
	profiles = os.path.join(os.path.dirname(__file__), "..", "stationPlaylist", "profiles")
	# Import old profiles.
	if os.path.exists(profiles):
		newProfiles = os.path.join(os.path.dirname(__file__), "profiles")
		try:
			shutil.copytree(profiles, newProfiles)
		except IOError:
			pass
	# 7.4 only: prepare LTS presentation file (an empty text file)
	#open(os.path.join(os.path.dirname(__file__), "ltsprep"), "w").close()
	# 17.04 only: Global Plugin module name has changed, so pull in the old gestures if defined.
	userGestures = inputCore.manager.userGestureMap._map
	# Is the new module in there?
	if "globalPlugins.splUtils" not in [script[0][0] for script in list(userGestures.values())]:
		for gesture, script in userGestures.items():
			if script[0][0] == "globalPlugins.SPLStudioUtils":
				# Prevent repeated gesture assignment.
				try:
					inputCore.manager.userGestureMap.remove(gesture, "globalPlugins.splUtils", script[0][1], script[0][2])
				except ValueError:
					pass
				inputCore.manager.userGestureMap.add(gesture, "globalPlugins.splUtils", script[0][1], script[0][2])
		inputCore.manager.userGestureMap.save()
