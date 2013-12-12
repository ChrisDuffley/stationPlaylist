# Station Playlist Studio
# An app module and global plugin package for NVDA
# Copyright 2011, 2013, Geoff Shang, Joseph Lee and others, released under GPL.
# The primary function of this appModule is to provide meaningful feedback to users of SplStudio
# by allowing speaking of items which cannot be easily found.
# Version 0.01 - 7 April 2011:
# Initial release: Jamie's focus hack plus auto-announcement of status items.
# Additional work done by Joseph Lee and other contributors.
# For SPL Studio Controller, focus movement and other utilities, see the global plugin version of this app module.

import controlTypes
from controlTypes import ROLE_GROUPING
import appModuleHandler
import api
import ui
from NVDAObjects.IAccessible import IAccessible
import tones
from functools import wraps

# The finally function for the toggle scripts in this module (source: Tyler Spivey's code).
def finally_(func, final):
	"""Calls final after func, even if it fails."""
	def wrap(f):
		@wraps(f)
		def new(*args, **kwargs):
			try:
				func(*args, **kwargs)
			finally:
				final()
		return new
	return wrap(final)


class AppModule(appModuleHandler.AppModule):
	# GS: The following was written by James Teh <jamie@NVAccess.org
	#It gets around a problem where double focus events are fired when moving around the playlist.
	#Hopefully it will be possible to remove this when it is fixed in Studio.>
	def event_NVDAObject_init(self, obj):
		if obj.windowClassName == "TListView" and obj.role in (controlTypes.ROLE_CHECKBOX, controlTypes.ROLE_LISTITEM) and controlTypes.STATE_FOCUSED not in obj.states:
			# These lists seem to fire a focus event on the previously focused item before firing focus on the new item.
			# Try to filter this out.
			obj.shouldAllowIAccessibleFocusEvent = False
		# Radio button group names are not recognized as grouping, so work around this.
		if obj.windowClassName == "TRadioGroup": obj.role = ROLE_GROUPING


	# Automatically announce mic, line in, etc changes
	# These items are static text items whose name changes.
	# Note: There are two status bars, hence the need to exclude Up time so it doesn't announce every minute.
	# Unfortunately, Window handles and WindowControlIDs seem to change, so can't be used.
	def event_nameChange(self, obj, nextHandler):
		# Do not let NvDA get name for None object when SPL window is maximized.
		if obj.name == None: return
		else:
			if obj.windowClassName == "TStatusBar" and not obj.name.startswith("  Up time:"):
				# Special handling for Play Status
				if obj.IAccessibleChildID == 1:
					# Strip off "  Play status: " for brevity
					ui.message(obj.name[15:])
				else:
					ui.message(obj.name)
		nextHandler()

# JL's additions

	# Various status scripts.
	# To save keyboard commands, layered commands will be used.
	# Most were borrowed from JFW and Window-Eyes layer scripts.

	# Set up the layer script environment.
	def getScript(self, gesture):
		if not self.SPLPrefix: return appModuleHandler.AppModule.getScript(self, gesture)
		script = appModuleHandler.AppModule.getScript(self, gesture)
		if not script: script = finally_(self.script_error, self.finish)
		return finally_(script, self.finish)

	def finish(self):
		self.SPLPrefix = False
		self.clearGestureBindings()
		self.bindGestures(self.__gestures)

	def script_error(self, gesture):
		tones.beep(120, 100)

	# Let us meet the scripts themselves.

	def script_sayRemainingTime(self, gesture):
		fgWindow = api.getForegroundObject()
		# While Studio is on focus, the playback window with remaining time info is right next door. Parse the window title.
		timeWindowStr = fgWindow.parent.next.name.split(" ")
		# We want the first part only, the time itself.
		remainingTime = timeWindowStr[0]
		ui.message(remainingTime)
	script_sayRemainingTime.__doc__="Announces the remaining track time."

	# The layer commands themselves.
	# First layer: basic status such as playback, automation, etc.
	SPLPrefix = False

	# The children constants for fetching status information from the SPL Studio window.
	SPLPlayStatus = 5 # Play status, mic, etc.
	SPLHourTrackDuration = 17 # For track duration for the given hour marker.
	SPLHourSelectedDuration = 18 # In case the user selects one or more tracks in a given hour.

	# The prefix layer driver.

	def script_prefixToggle(self, gesture):
		if self.SPLPrefix:
			self.script_error(gesture)
			return
		self.bindGestures(self.__PrefixGestures)
		self.SPLPrefix = True
		tones.beep(512, 10)

	# Whichever layer we use, get the appropriate children from the foreground window.
	def getStatusChild(self, childIndex):
		childObj = api.getForegroundObject().children[childIndex]
		return childObj

	# Basic status such as playback and mic.

	def script_sayPlayStatus(self, gesture):
		obj = self.getStatusChild(self.SPLPlayStatus).children[0]
		ui.message(obj.name)

	def script_sayAutomationStatus(self, gesture):
		obj = self.getStatusChild(self.SPLPlayStatus).children[1]
		ui.message(obj.name)

	def script_sayMicStatus(self, gesture):
		obj = self.getStatusChild(self.SPLPlayStatus).children[2]
		ui.message(obj.name)

	def script_sayLineInStatus(self, gesture):
		obj = self.getStatusChild(self.SPLPlayStatus).children[3]
		ui.message(obj.name)

	def script_sayHourTrackDuration(self, gesture):
		obj = self.getStatusChild(self.SPLHourTrackDuration).firstChild
		ui.message(obj.name)

	def script_sayHourSelectedTrackDuration(self, gesture):
		obj = self.getStatusChild(self.SPLHourSelectedDuration).firstChild
		ui.message(obj.name)


	__PrefixGestures={
		"kb:s":"sayPlayStatus",
		"kb:a":"sayAutomationStatus",
		"kb:m":"sayMicStatus",
		"kb:l":"sayLineInStatus",
		"kb:h":"sayHourTrackDuration",
		"kb:shift+h":"sayHourSelectedTrackDuration"
	}

	__gestures={
		"kb:control+alt+t":"sayRemainingTime",
		"kb:nvda+shift+p":"prefixToggle"
	}
