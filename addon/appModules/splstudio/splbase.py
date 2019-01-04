# SPL Studio base services
# An app module and global plugin package for NVDA
# Copyright 2018-2019 Joseph Lee and others, released under GPL.

# Base services for Studio app module and support modules

import ui
from winUser import sendMessage, user32
from .spldebugging import debugOutput
import addonHandler
addonHandler.initTranslation()

# Cache the handle to main Studio window.
_SPLWin = None

# Check if Studio itself is running.
# This is to make sure custom commands for SPL Assistant commands and other app module gestures display appropriate error messages.
# 19.02: some checks will need to omit message output.
def studioIsRunning(justChecking=False):
	# Keep the boolean flag handy because of message output.
	isStudioAlive = ((_SPLWin is not None and _SPLWin == user32.FindWindowW(u"SPLStudio", None))
	or (_SPLWin is None and user32.FindWindowW(u"SPLStudio", None) != 0))
	if not isStudioAlive:
		debugOutput("Studio is not alive")
		# Translators: A message informing users that Studio is not running so certain commands will not work.
		if not justChecking: ui.message(_("Studio main window not found"))
	return isStudioAlive

# Use SPL Studio API to obtain needed values.
# A thin wrapper around user32.SendMessage function with Studio handle and WM_USER supplied.
# #45 (18.02): returns whatever result SendMessage function says.
# If debugging framework is on, print arg, command and other values.
# 18.05: strengthen this by checking for the handle once more.
# #92 (19.03): SendMessage function returns something from anything (including from dead window handles), so really make sure Studio window handle is alive.
def studioAPI(arg, command):
	if not studioIsRunning(justChecking=True):
		return
	debugOutput("Studio API wParem is %s, lParem is %s"%(arg, command))
	val = sendMessage(_SPLWin, 1024, arg, command)
	debugOutput("Studio API result is %s"%val)
	return val

# Select a track upon request.
def selectTrack(trackIndex):
	studioAPI(-1, 121)
	debugOutput("selecting track index %s"%trackIndex)
	studioAPI(trackIndex, 121)
