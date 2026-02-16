# StationPlaylist Recorder
# An app module and global plugin package for NVDA
# Copyright 2026 Joseph Lee, released under GPL.

# Basic support for StationPlaylist Recorder.

import appModuleHandler
from NVDAObjects import NVDAObject
from .splcommon import splbase


class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: list[NVDAObject]) -> None:
		# Detect unlabeled controls whose labels are next to them (written to the screen).
		# Return right after detecting these.
		if splbase.useScreenLabelForUnlabeledObject(
			obj, [
				"TOptionsForm"  # Recorder options
			]
		):
			clsList.insert(0, splbase.SPLUnlabeledControl)
