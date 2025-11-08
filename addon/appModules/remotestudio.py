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
from NVDAObjects import NVDAObject
from . import splstudio
from .splcommon import splbase, splconfig, splconsts


class RemoteStudioPlaylistViewerItem(splstudio.StudioPlaylistViewerItem):
	"""Track items found in Remote Studio.
	Columns are based on Studio 6.11 and earlier.
	"""
	pass


class AppModule(splstudio.AppModule):
	# Remote Studio does not require Studio API to function.
	_studioAPIRequired = False

	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: list[NVDAObject]) -> None:
		# Same as local Studio but with different window style flags.
		if (
			obj.windowClassName == "TTntListView.UnicodeClass"
			and obj.role == controlTypes.Role.LISTITEM
			and obj.windowStyle == 1443991621
		):
			clsList.insert(0, RemoteStudioPlaylistViewerItem)
		super().chooseNVDAObjectOverlayClasses(obj, clsList)

	def event_nameChange(self, obj: NVDAObject, nextHandler: collections.abc.Callable[[], None]):
		if obj.windowClassName == "TStatusBar":
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
						and splbase.studioAPI(3, SPLCurTrackPlaybackTime) < (
							splconfig.SPLConfig["IntroOutroAlarms"]["EndOfTrackTime"] * 1000  # Milliseconds
						)
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
						and splbase.studioAPI(4, SPLCurTrackPlaybackTime) < (
							splconfig.SPLConfig["IntroOutroAlarms"]["SongRampTime"] * 1000  # Milliseconds
						)
					):
						braille.handler.message(obj.name)
					if (
						obj.name
						== "00:{0:02d}".format(splconfig.SPLConfig["IntroOutroAlarms"]["SongRampTime"])
						and splconfig.SPLConfig["IntroOutroAlarms"]["SaySongRamp"]
					):
						self.alarmAnnounce(obj.name, 512, 400, intro=True)
		nextHandler()

	# Cart explorer (Remote Studio)
	cartExplorer = False
	# The carts dictionary (key = cart gesture, item = cart name).
	carts: dict[str, Any] = {}

	# Assigning and building carts.

	def cartsBuilder(self, build: bool = True) -> None:
		# A function to build and return cart commands.
		# Remote Studio offers twelve carts (function keys only).
		if build:
			for cart in splconsts.cartKeys[:12]:
				self.bindGesture(f"kb:{cart}", "cartExplorer")
		else:
			self.clearGestureBindings()
			self.bindGestures(self.__gestures)

	# Check to make sure a playlist is indeed loaded by checking track count.
	def playlistLoaded(self) -> bool:
		return bool(getattr(api.getFocusObject(), "rowCount", 0))

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

	# Announce playlist times
	# Remote Studio: use screen traversal.
	def announcePlaylistTimes(self, index: int) -> None:
		# Playlist times index is an integer (Remote Studio: for compatibility with local Studio/API).
		match index:
			case 0:  # Hour duration
				ui.message(self.status(self.SPLTotalForHour).lastChild.name)
			case 1:  # Hour remaining
				ui.message(self.status(self.SPLPlaylistRemain).getChild(1).name)
			case 2:  # Overtime
				ui.message(self.status(self.SPLPlaylistRemain).firstChild.name)
			case 3:  # Scheduled/track starts
				# Scheduled is the time originally specified in Studio,
				# scheduled to play is broadcast time based on current time.
				ui.message(self.status(self.SPLTrackStarts).firstChild.name)
			case 4:  # Track starts in
				# Announces length of time remaining until the selected track will play.
				ui.message(self.status(self.SPLTrackStartsIn).firstChild.name)
			case _:
				raise ValueError(f"Unrecognized playlist time announcement command: {index}")
