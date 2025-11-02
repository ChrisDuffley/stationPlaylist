# StationPlaylist Remote Studio
# An app module and global plugin package for NVDA
# Copyright 2025 Joseph Lee, released under GPL.

# Basic support for StationPlaylist Remote Studio.
# Borrows heavily from Studio as the user interface is quite similar with changes specific to Remote Studio.

from typing import Any
import api
from . import splstudio
from .splstudio import splmisc

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
			for cart in splmisc.cartKeys[:12]:
				self.bindGesture(f"kb:{cart}", "cartExplorer")
		else:
			self.clearGestureBindings()
			self.bindGestures(self.__gestures)

	# Check to make sure a playlist is indeed loaded by checking track count.
	def playlistLoaded(self) -> bool:
		return bool(getattr(api.getFocusObject(), "rowCount", 0))
