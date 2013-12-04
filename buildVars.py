# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
# add-on Name
	"addon-name" : "StationPlaylist",
	# Add-on description
	# TRANSLATORS: Summary for this add-on to be shown on installation and add-on information.
	"addon-summary" : _("Station Playlist Studio"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on installation and add-on information
	"addon-description" : _("""Enhances support for Station Playlist Studio.
In addition, adds status commands for the studio from everywhere."""),
	# version
	"addon-version" : "0.01",
	# Author(s)
	"addon-author" : "Geoff Shang, Joseph Lee and other contributors",
	# URL for the add-on documentation support
	"addon-url" : "http://addons.nvda-project.org/"
}

import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "appModules", "*.py"),
    os.path.join("addon", "globalPlugins", "*.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py", "docHandler.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
