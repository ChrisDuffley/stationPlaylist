# StationPlaylist Streamer
# An app module and global plugin package for NVDA
# Copyright 2019 Joseph Lee and others, released under GPL.

# Support for StationPlaylist Straemer
# A standalone app used for broadcast streaming when using something other than Studio for broadcasting.

import appModuleHandler
import controlTypes
from NVDAObjects.IAccessible import IAccessible

# For SPL encoder config screen at least, control iD's are different, which allows labels to be generated easily.
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
}

class TEditNoLabel(IAccessible):

	def _get_name(self):
		return 			"Buffer Size {0} ms".format(self.value)


class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		if not obj.name and obj.role != controlTypes.ROLE_WINDOW:
			# Same ID's are used for two different things, distinguishable by looking at which configuration ab is active.
			windowControlID = obj.windowControlID
			if windowControlID in (1019, 1020):
				# Labels are split between parent window and the actual control, thus attribute error is seen.
				try:
					configTab = obj.parent.parent.previous.previous.previous.firstChild
				except AttributeError:
					configTab = obj.parent.parent.parent.previous.previous.previous.firstChild
				try:
					obj.name = encoderSettingsLabels[windowControlID][0 if controlTypes.STATE_SELECTED in configTab.firstChild.states else 1]
				except AttributeError:
					pass
			else:
				encoderSettingsLabel = encoderSettingsLabels.get(obj.windowControlID)
				if encoderSettingsLabel:
					obj.name = encoderSettingsLabel

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# Try adding labels written to the screen in case edit fields are encountered.
		if obj.windowClassName == "TEdit" and not obj.name and controlTypes.STATE_READONLY in obj.states:
			clsList.insert(0, TEditNoLabel)
