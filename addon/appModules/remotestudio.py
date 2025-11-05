# StationPlaylist Remote Studio
# An app module and global plugin package for NVDA
# Copyright 2025 Joseph Lee, released under GPL.

# Basic support for StationPlaylist Remote Studio.
# Borrows heavily from Studio as the user interface is quite similar with changes specific to Remote Studio.

from typing import Any
import ui
import api
from . import splstudio
from .splcommon import splconsts

class AppModule(splstudio.AppModule):
	# Remote Studio does not require Studio API to function.
	_studioAPIRequired = False

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
	# These are scattered throughout the screen, so one can use foreground.getChild(index) to fetch them
	# (getChild tip from Jamie Teh (NV Access/Mozilla)).
	# Because 6.x an possible future releases may use different screen layouts,
	# look up the needed constant from the table below
	# (row = info needed, column = version).
	# As of 2025, the below table is based on Studio 6.0.
	# #119: a list indicates iterative descent to locate the actual objects.
	statusObjs = {
		"6": {
			SPLRemoteStatus: [2, 0],  # Remote Studio status bar
			SPLTrackRemainingTime: [2, 2, -2],
			SPLTrackElapsedTime: [2, 2, -1],
			SPLNextTrackTitle: [2, 2, 2],
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
	def announcePlaylistTimes(self, index: int) -> int:
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
