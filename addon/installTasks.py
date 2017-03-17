# StationPlaylist Studio add-on installation tasks
# Copyright 2015-2017 Joseph Lee and others, released under GPL.

# Provides needed routines during add-on installation and removal.
# Routines are partly based on other add-ons, particularly Place Markers by Noelia Martinez (thanks add-on authors).

def onInstall():
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
	if "globalPlugins.splUtils" not in [script[0][0] for script in userGestures.values()]:
		for gesture, script in userGestures.iteritems():
			if script[0][0] == "globalPlugins.SPLStudioUtils":
				# Prevent repeated gesture assignment.
				try:
					inputCore.manager.userGestureMap.remove(gesture, "globalPlugins.splUtils", script[0][1], script[0][2])
				except ValueError:
					pass
				inputCore.manager.userGestureMap.add(gesture, "globalPlugins.splUtils", script[0][1], script[0][2])
		inputCore.manager.userGestureMap.save()
