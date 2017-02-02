# SPL Studio add-on debugging framework
# An app module and global plugin package for NVDA
# Copyright 2017 Joseph Lee and others, released under GPL.
# Provides debug output and other diagnostics probes.

from logHandler import log

try:
	import globalVars
	SPLDebuggingFramework = globalVars.appArgs.debugLogging
except AttributeError:
	SPLDebuggingFramework = None

def debugOutput(message):
	if SPLDebuggingFramework:
		log.debug(message)

