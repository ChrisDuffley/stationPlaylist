# SPL Studio add-on debugging framework
# An app module and global plugin package for NVDA
# Copyright 2017-2020 Joseph Lee and others, released under GPL.
# Provides debug output and other diagnostics probes.

from logHandler import log
import globalVars
SPLDebuggingFramework = globalVars.appArgs.debugLogging


def debugOutput(message):
	if SPLDebuggingFramework:
		log.debug(f"SPL: {message}")
