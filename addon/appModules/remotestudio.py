# StationPlaylist Remote Studio
# An app module and global plugin package for NVDA
# Copyright 2025 Joseph Lee, released under GPL.

# Basic support for StationPlaylist Remote Studio.
# Borrows heavily from Studio as the user interface is quite similar with changes specific to Remote Studio.

from typing import Any
import collections
import ui
import api
import controlTypes
import braille
import scriptHandler
import queueHandler
from NVDAObjects import NVDAObject
from . import splstudio
from .splstudio import splmisc, splconfig


# Return a tuple of column headers.
# This is just a thinly disguised indexOf function from Studio's track item class.
def indexOf(rsVersion: str) -> tuple[str, ...]:
	# Remote Studio 6.20 defines Studio 6.11 column headers.
	# Therefore, the version parameter is not needed.
	return tuple(["Status"] + splconfig._SPLDefaults["ColumnAnnouncement"]["ColumnOrder"])


class RemoteStudioPlaylistViewerItem(splstudio.StudioPlaylistViewerItem):
	"""Track items found in Remote Studio.
	Columns are based on Studio 6.11 and earlier.
	"""

	@property
	def screenColumnOrder(self):
		# Return the actual default column order based on Studio release.
		return indexOf(self.appModule.productVersion)[1:]

	def indexOf(self, columnHeader: str) -> int | None:
		try:
			return indexOf(self.appModule.productVersion).index(columnHeader)
		except ValueError:
			return None

	# Tell NVDA to announce just the changed bits of the status bar.
	@scriptHandler.script(gestures=[f"kb:{k}" for k in ["Enter", "A", "L", "M", "N", "S", "T", "U"]])
	def script_remoteStudioActions(self, gesture):
		match gesture.displayName:
			case "enter" | "s" | "t" | "u":  # Play (Enter)/pause (U)/stop (S)/instant stop (T)
				self.appModule._statusBarChangedPosition = 0
			case "a":  # Automation
				self.appModule._statusBarChangedPosition = 1
			case "m" | "n":  # Microphone (M)/mic no fade (N)
				self.appModule._statusBarChangedPosition = 2
			case "l":  # Line-in
				self.appModule._statusBarChangedPosition = 3
			case _:  # Everything else
				pass
		gesture.send()


class AppModule(splstudio.AppModule):
	# Remote Studio does not require Studio API to function.
	_studioAPIRequired = False

	def terminate(self):
		super().terminate()
		# Clear app module flags and attributes.
		self._pastStatusBarContent = None
	
	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: list[NVDAObject]) -> None:
		# Same as local Studio but with different window style flags.
		if (
			obj.windowClassName == "TTntListView.UnicodeClass"
			and obj.role == controlTypes.Role.LISTITEM
			and obj.windowStyle == 1443991621
		):
			clsList.insert(0, RemoteStudioPlaylistViewerItem)
		super().chooseNVDAObjectOverlayClasses(obj, clsList)

	# Status bar is one long text separated by vertical bars (|).
	# Record status bar contents when Remote Studio is connected to a local Studio instance.
	_pastStatusBarContent: str | None = None

	# Tell NVDA to announce just the changed bits of the status bar.
	def event_foreground(self, obj: NVDAObject, nextHandler: collections.abc.Callable[[], None]):
		# Record the current status bar text if the app module doesn't know about it.
		if obj.windowClassName == "TStudioForm" and not self._pastStatusBarContent:
			self._pastStatusBarContent = self.status(self.SPLRemoteStatus).displayText
		nextHandler()

	def event_nameChange(self, obj: NVDAObject, nextHandler: collections.abc.Callable[[], None]):
		if obj.windowClassName == "TStatusBar":
			# Only announce the changed parts of the status bar except when connecting the first time.
			if "|" in obj.name:
				if self._pastStatusBarContent:
					statusBarText = obj.name.split("  |  ")
					oldStatusBarText = self._pastStatusBarContent.split("  |  ")
					changedStatusBarContent = []
					for pos in range(len(statusBarText)):
						if statusBarText[pos] != oldStatusBarText[pos]:
							changedStatusBarContent.append(statusBarText[pos])
					for content in changedStatusBarContent:
						queueHandler.queueFunction(queueHandler.eventQueue, self.doRemoteStudioExtraAction, content)
				self._pastStatusBarContent = obj.name
			else:
				# Announce connection status in Remote Studio.
				ui.message(obj.name)
		# Monitor the end of track and song intro time and announce it.
		elif obj.windowClassName == "TStaticText":
			if obj.simplePrevious is not None:
				if obj.simplePrevious.name == "Track Starts" and obj.parent.parent.firstChild.name == "Remaining":
					# End of track text.
					if (
						splconfig.SPLConfig["General"]["BrailleTimer"] in ("outro", "both")
						and api.getForegroundObject().processID == self.processID
						# Only braille if end of track text is within track outro alarm threshold.
						and self._trackAlarmWithinThreshold(obj.name, splconfig.SPLConfig["IntroOutroAlarms"]["EndOfTrackTime"])
					):
						braille.handler.message(obj.name)
					if (
						obj.name
						== "00:{0:02d}".format(splconfig.SPLConfig["IntroOutroAlarms"]["EndOfTrackTime"])
						and splconfig.SPLConfig["IntroOutroAlarms"]["SayEndOfTrack"]
					):
						self.alarmAnnounce(obj.name, 440, 200)
				elif obj.simplePrevious.name == "Track Starts" and obj.parent.parent.firstChild.name == "Song Ramp":
					# Song intro content.
					if (
						splconfig.SPLConfig["General"]["BrailleTimer"] in ("intro", "both")
						and api.getForegroundObject().processID == self.processID
						# Only braille if track ramp text is within track intro alarm threshold.
						and self._trackAlarmWithinThreshold(obj.name, splconfig.SPLConfig["IntroOutroAlarms"]["SongRampTime"])
					):
						braille.handler.message(obj.name)
					if (
						obj.name
						== "00:{0:02d}".format(splconfig.SPLConfig["IntroOutroAlarms"]["SongRampTime"])
						and splconfig.SPLConfig["IntroOutroAlarms"]["SaySongRamp"]
					):
						self.alarmAnnounce(obj.name, 512, 400, intro=True)
		nextHandler()

	def doRemoteStudioExtraAction(self, content: str) -> None:
		# Do play a beep when asked.
		if content.endswith((" On", " Off")):
			self._toggleMessage(content)
		else:
			ui.message(content)
		if splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarm"]:
			# Activate mic alarm or announce when cart explorer is active.
			self.doExtraAction(content)


	def _trackAlarmWithinThreshold(self, trackTime: str, threshold: int) -> bool:
		trackTimeComponents = [int(component) for component in trackTime.split(":")]
		# Assume hh:mm:ss.
		if len(trackTimeComponents) == 2:
			trackTimeComponents.insert(0, 0)
		trackTimeSeconds = (trackTimeComponents[0] * 3600) + (trackTimeComponents[1] * 60) + trackTimeComponents[2]
		return trackTimeSeconds <= threshold

	# Cart explorer (Remote Studio)
	cartExplorer = False
	# The carts dictionary (key = cart gesture, item = cart name).
	carts: dict[str, Any] = {}

	# Assigning and building carts.

	def cartsBuilder(self, build: bool = True) -> None:
		# A function to build and return cart commands.
		# Remote Studio offers twelve carts (function keys only).
		if build:
			for cart in splmisc.cartKeys[:12]:
				self.bindGesture(f"kb:{cart}", "cartExplorer")
		else:
			self.clearGestureBindings()
			self.bindGestures(self.__gestures)

	# Check to make sure a playlist is indeed loaded by checking track count.
	def playlistLoaded(self) -> bool:
		focus = api.getFocusObject()
		if isinstance(focus, RemoteStudioPlaylistViewerItem):
			return True
		return bool(getattr(focus, "rowCount", 0))

	# Status table keys
	# Unlike local Studio, Remote Studio may not have an API, so screen traversal must be done.
	# This is applicable to SPL Assistant commands and other scripts.
	SPLRemoteStatus = 0
	SPLTrackRemainingTime = 1
	SPLTrackElapsedTime = 2
	SPLNextTrackTitle = 3
	SPLCurrentTrackTitle = 4
	SPLTrackStarts = 5
	SPLTrackStartsIn = 6
	SPLPlaylistRemain = 7
	SPLTotalForHour = 8
	SPLTemperature = 9

	# Table of child constants based on versions
	# Same as local Studio: scattered around the screen, so use foreground.getChild(index) to fetch them
	# As of 2025, the below table is based on local Studio 6.10 interface.
	statusObjs = {
		"6": {
			SPLRemoteStatus: [2, 0],  # Remote Studio status bar
			SPLTrackRemainingTime: [2, 2, -2],
			SPLTrackElapsedTime: [2, 2, -1],
			SPLNextTrackTitle: [2, 2, 2, 0],
			SPLCurrentTrackTitle: [2, 2, 9],
			SPLTrackStarts: [2, 2, -3],
			SPLTrackStartsIn: [2, 2, -6],
			SPLPlaylistRemain: [2, 2, -5],
			SPLTotalForHour: [2, 2, -4],
			SPLTemperature: [2, 2, 3, 1],  # Temperature for the current city.
		},
	}

	_cachedStatusObjs: dict[int, Any] = {}

	# Announce elapsed and remaining times differently across local and Remote Studio
	# (local Studio = Studio API, Remote Studio = screen traversal).
	def announceTrackTime(self, trackTime: str) -> None:
		# Track time parameter can be either "remaining" or "elapsed".
		match trackTime:
			case "remaining":
				ui.message(self.status(self.SPLTrackRemainingTime).name)
			case "elapsed":
				ui.message(self.status(self.SPLTrackElapsedTime).name)
			case _:
				raise ValueError(f"Unrecognized track time announcement command: {trackTime}")

	# Report status bar contents such as microphone status.
	# Remote Studio: parse status bar text.
	def sayStatus(self, index: int) -> None:
		# No, status index must be an integer (compatibility with local Studio).
		# Status bar is empty if not connected.
		status = self.status(self.SPLRemoteStatus).displayText
		if not status:
			# Translators: presented when Remote Studio status cannot be obtained.
			ui.message(_("No Remote Studio status Information"))
			return
		# Status text is separated by vertical lines.
		status = status.split("  |  ")[index]
		if splconfig.SPLConfig["General"]["MessageVerbosity"] == "advanced":
			status = status.split()[-1]
		ui.message(status)

	# SPL Assistant layer commands requiring Remote Studio specific procedure.

	def script_sayHourTrackDuration(self, gesture):
		ui.message(self.status(self.SPLTotalForHour).lastChild.name)

	def script_sayHourRemaining(self, gesture):
		ui.message(self.status(self.SPLPlaylistRemain).getChild(1).name)

	def script_sayHourOvertime(self, gesture):
		ui.message(self.status(self.SPLPlaylistRemain).firstChild.name)

	def script_sayScheduledTime(self, gesture):
		# Scheduled is the time originally specified in Studio,
		# scheduled to play is broadcast time based on current time.
		ui.message(self.status(self.SPLTrackStarts).firstChild.name)

	def script_sayScheduledToPlay(self, gesture):
		# This script announces length of time remaining until the selected track will play.
		ui.message(self.status(self.SPLTrackStartsIn).firstChild.name)
