# SPL Studio base services
# An app module and global plugin package for NVDA
# Copyright 2018 Joseph Lee and others, released under GPL.

# Base services for Studio app module and support modules

import ui
from winUser import sendMessage
from .spldebugging import debugOutput

# Cache the handle to main Studio window.
_SPLWin = None

# Use SPL Studio API to obtain needed values.
# A thin wrapper around user32.SendMessage function with Studio handle and WM_USER supplied.
# #45 (18.02): returns whatever result SendMessage function says.
# If debugging framework is on, print arg, command and other values.
def studioAPI(arg, command):
	if _SPLWin is None:
		debugOutput("Studio handle not found")
		return
	debugOutput("Studio API wParem is %s, lParem is %s"%(arg, command))
	val = sendMessage(_SPLWin, 1024, arg, command)
	debugOutput("Studio API result is %s"%val)
	return val

# Check if Studio itself is running.
# This is to make sure custom commands for SPL Assistant commands and other app module gestures display appropriate error messages.
def studioIsRunning():
	if _SPLWin is None:
		debugOutput("Studio handle not found")
		# Translators: A message informing users that Studio is not running so certain commands will not work.
		ui.message(_("Studio main window not found"))
		return False
	return True

# Select a track upon request.
def selectTrack(trackIndex):
	studioAPI(-1, 121)
	debugOutput("selecting track index %s"%trackIndex)
	studioAPI(trackIndex, 121)
