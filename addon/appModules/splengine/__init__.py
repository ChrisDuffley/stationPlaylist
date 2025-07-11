# StationPlaylist DSP Engine
# Copyright 2019-2025 Joseph Lee, released under GPL.

# SPL Audio Processing Engine
# Home to various DSP DLL's including encoders.

import appModuleHandler
import controlTypes
from NVDAObjects import NVDAObject
from NVDAObjects.IAccessible import sysListView32
from . import encoders

# For SPL encoder config screen at least, control iD's are different,
# which allows labels to be generated easily.
encoderSettingsLabels = {
	1008: "Quality",
	1009: "Sample Rate",
	1010: "Channels",
	1013: "Server IP",
	1014: "Server Port",
	1015: "Encoder Password",
	1016: "Mountpoint",
	1017: "Server Type",
	1018: "Encoder Type",
	1019: ("Reconnect Seconds", "Server Name"),
	1020: ("Encoder Username", "Server Description"),
	1021: "Website URL",
	1022: "Stream Genre",
	1024: ("AIM", "Archive Directory"),
	1025: ("IRC", "Log Level"),
	1026: "Log File",
}


class AppModule(appModuleHandler.AppModule):
	def terminate(self):
		super().terminate()
		# Memory leak results if encoder flag sets and other encoder support maps aren't cleaned up.
		# This also could have allowed a hacker to modify the flags set (highly unlikely)
		# so NVDA could get confused next time Studio loads.
		# #105: SPL Engine is responsible for hosting encoder DLL's.
		# #104: any app module deriving from this (including Streamer)
		# must clean up encoders database.
		# #98: this is still the case even though encoders support is part of the SPL Engine app module package.
		# This introduces a side effect where encoders database might be reopened
		# if both SPL Engine and Streamer are active and one of them dies.
		# For now, ignore this condition.
		encoders.cleanup(appTerminating=True)

	def event_NVDAObject_init(self, obj: NVDAObject):
		# ICQ field is incorrectly labeled as IRC.
		# After labeling it, return early so others can be labeled correctly.
		if obj.windowControlID == 1023:
			obj.name = "ICQ #"
			return
		if not obj.name and obj.role != controlTypes.Role.WINDOW:
			# Same ID's are used across controls, distinguishable by looking at which configuration tab is active.
			windowControlID = obj.windowControlID
			if windowControlID in (1019, 1020, 1024, 1025):
				# Labels are split between parent window and the actual control, thus attribute error is seen.
				try:
					configTab = obj.parent.parent.previous.previous.previous.firstChild
				except AttributeError:
					configTab = obj.parent.parent.parent.previous.previous.previous.firstChild
				activeTab = 0 if windowControlID in (1019, 1020) else 1
				try:
					if controlTypes.State.SELECTED in configTab.getChild(activeTab).states:
						obj.name = encoderSettingsLabels[windowControlID][0]
					else:
						obj.name = encoderSettingsLabels[windowControlID][1]
				except AttributeError:
					pass
			else:
				encoderSettingsLabel = encoderSettingsLabels.get(obj.windowControlID)
				if encoderSettingsLabel:
					obj.name = encoderSettingsLabel

	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: list[NVDAObject]) -> None:
		# Detect encoders.
		if obj.windowClassName == "TListView":
			# #87: add support for table navigation commands
			# by coercing encoder list and entries into SysListView32 family.
			if obj.role == controlTypes.Role.LISTITEM:
				clsList.insert(0, encoders.SAMEncoder)
			elif obj.role == controlTypes.Role.LIST:
				clsList.insert(0, sysListView32.List)
		elif obj.windowClassName == "SysListView32" and obj.role == controlTypes.Role.LISTITEM:
			# #113: AltaCast encoder list has a name whereas SPL Encoder doesn't.
			clsList.insert(0, encoders.AltaCastEncoder if obj.parent.name == "List1" else encoders.SPLEncoder)
