# SPL Studio Actions
# An app module and global plugin package for NVDA
# Copyright 2017-2021 Joseph Lee, released under GPL.
# Defines various actions to be carried out by various add-on modules, powered by extension points.
# This module provides services for other modules, not the other way around.
# Thus, importing other add-on modules should not be attempted unless granted.

# An action is a notification about something that has happened or about to happen.
# In SPL add-on, an action is prefixed by SPLAction*.

import extensionPoints

# Studio handle found, app module is fully ready.
SPLActionAppReady = extensionPoints.Action()
# Add-on settings were loaded.
SPLActionSettingsLoaded = extensionPoints.Action()
# Switching broadcast profiles.
SPLActionProfileSwitched = extensionPoints.Action()
# Settings are being saved.
SPLActionSettingsSaved = extensionPoints.Action()
# Settings are reloading or set to factory defaults.
SPLActionSettingsReset = extensionPoints.Action()
# Studio is terminating.
SPLActionAppTerminating = extensionPoints.Action()
