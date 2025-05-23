# SPL Studio base services
# An app module and global plugin package for NVDA
# Copyright 2018-2025 Joseph Lee, released under GPL.

# Base services for Studio app module and support modules

import ui
from winUser import sendMessage, user32
from logHandler import log
import addonHandler

addonHandler.initTranslation()

# Cache the handle to main Studio window.
_SPLWin: int | None = None


# Check if Studio itself is running.
# This is to make sure custom commands for SPL Assistant commands
# and other app module gestures display appropriate error messages.
# 19.02: some checks will need to omit message output.
def studioIsRunning(justChecking: bool = False) -> bool:
	# Keep the boolean flag handy because of message output.
	isStudioAlive = (_SPLWin is not None and _SPLWin == user32.FindWindowW("SPLStudio", None)) or (
		_SPLWin is None and user32.FindWindowW("SPLStudio", None) != 0
	)
	if not isStudioAlive:
		log.debug("SPL: Studio is not alive")
		if not justChecking:
			# Translators: A message informing users that Studio is not running so certain commands will not work.
			ui.message(_("Studio main window not found"))
	return isStudioAlive


# Use SPL Studio API to obtain needed values.
# A thin wrapper around user32.SendMessage function with Studio handle and WM_USER supplied.
# #45 (18.02): returns whatever result SendMessage function says.
# If NVDA is in debug mode, print arg, command and other values.
# 18.05: strengthen this by checking for the handle once more.
# #92 (19.03): SendMessage function returns something from anything (including from dead window handles),
# so really make sure Studio window handle is alive.
def studioAPI(arg: int, command: int) -> int | None:
	if not studioIsRunning(justChecking=True):
		return None
	# 25.06: global plugin can also clal this function with no Studio window handle value defined.
	global _SPLWin
	if _SPLWin is None:
		_SPLWin = user32.FindWindowW("SPLStudio", None)
	log.debug(f"SPL: Studio API wParem is {arg}, lParem is {command}")
	val = sendMessage(_SPLWin, 1024, arg, command)
	log.debug(f"SPL: Studio API result is {val}")
	# 21.03/20.09.6-LTS: SendMessage function might be stuck while Studio exits, resulting in NULL window handle.
	if not user32.FindWindowW("SPLStudio", None):
		val = None
		log.debug("Studio window is gone, Studio API result is None")
	return val


# Select a track upon request.
def selectTrack(trackIndex: int) -> None:
	studioAPI(-1, 121)
	log.debug(f"SPL: selecting track index {trackIndex}")
	studioAPI(trackIndex, 121)
