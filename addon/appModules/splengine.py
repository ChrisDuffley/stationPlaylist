# StationPlaylist DSP Engine
# Copyright 2019 Joseph Lee and others, released under GPL.

# SPL Audio Processing Engine
# Home to various DSP DLL's including encoders.

import sys
import appModuleHandler
import controlTypes

# For SPL encoder config screen at least, control iD's are different, which allows labels to be generated easily.
encoderSettingsLabels= {
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
		super(AppModule, self).terminate()
		# 6.3: Memory leak results if encoder flag sets and other encoder support maps aren't cleaned up.
		# This also could have allowed a hacker to modify the flags set (highly unlikely) so NvDA could get confused next time Studio loads.
		# #105 (19.07): SPL Engine is responsible for hosting encoder DLL's.
		# #104 (19.07/18.09.10-LTS): any app module deriving from this (including Streamer) must clean up encoders database.
		if "globalPlugins.splUtils.encoders" in sys.modules:
			import globalPlugins.splUtils.encoders
			globalPlugins.splUtils.encoders.cleanup()

	def event_NVDAObject_init(self, obj):
		# ICQ field is incorrectly labeled as IRC.
		# After labeling it, return early so others can be labeled correctly.
		if obj.windowControlID == 1023:
			obj.name = "ICQ #"
			return
		if not obj.name and obj.role != controlTypes.ROLE_WINDOW:
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
					obj.name = encoderSettingsLabels[windowControlID][0 if controlTypes.STATE_SELECTED in configTab.getChild(activeTab).states else 1]
				except AttributeError:
					pass
			else:
				encoderSettingsLabel = encoderSettingsLabels.get(obj.windowControlID)
				if encoderSettingsLabel:
					obj.name = encoderSettingsLabel
