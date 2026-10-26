# StationPlaylist VT Recorder
# An app module and global plugin package for NVDA
# Copyright 2018-2026 Joseph Lee, released under GPL.

# Basic support for SPL Voice Track Recorder.

from dataclasses import dataclass
import appModuleHandler
from scriptHandler import script
import api
import ui
import eventHandler
from logHandler import log
from NVDAObjects import NVDAObject
from NVDAObjects.IAccessible import IAccessible
import braille
import config
import speech
from config.configFlags import ShowMessages
from .splcommon import splbase


OUTGOING_TRACK_GROUP = "Outgoing Track"
INCOMING_TRACK_GROUP = "Incoming Track"
TRACK_TEXT_WINDOW_CLASS = "TTntStaticText.UnicodeClass"


@dataclass
class InfoParts:
	recordState: str = ""
	recordTime: str = "00:00.0"
	nextButton: str = "Start Recording"


infoParts = InfoParts()


def resetInfoParts() -> None:
	"""Restore the braille status fields to their initial recorder values."""
	infoParts.recordState = ""
	infoParts.recordTime = "00:00.0"
	infoParts.nextButton = "Start Recording"


def brailleMessage(message: str) -> None:
	"""Display a braille message indefinitely without changing the user setting."""
	oldShowBrailleMessages = config.conf["braille"]["showMessages"]
	config.conf["braille"]["showMessages"] = ShowMessages.SHOW_INDEFINITELY
	try:
		braille.handler.message(message)
	finally:
		config.conf["braille"]["showMessages"] = oldShowBrailleMessages


def displayInfos() -> None:
	"""Present the current recorder status fields on the braille display."""
	text = f"{infoParts.recordState} {infoParts.recordTime} {infoParts.nextButton}"
	brailleMessage(text)


class CustomTPanel(IAccessible):
	def event_nameChange(self):
		"""Update the displayed recording time when the recorder panel changes."""
		infoParts.recordTime = self.name or ""
		displayInfos()


class CustomTBitBtn(IAccessible):
	def event_nameChange(self):
		"""Update the displayed next-recording action when the button changes."""
		infoParts.nextButton = self.name or ""
		displayInfos()


class CustomTRadioButton(IAccessible):
	def event_gainFocus(self):
		"""Abbreviate and display the selected recording overlap mode."""
		super().event_gainFocus()
		name = self.name or ""
		displayText = {
			"automatic": "au ",
			"no overlap": "no ",
			"manual outgoing/incoming": "io ",
			"manual outgoing only": "out",
			"manual incoming only": "in ",
		}.get(name.casefold(), name)
		infoParts.recordState = displayText
		displayInfos()


class UnlabeledFields(IAccessible):
	def event_gainFocus(self):
		"""Announce the containing group label for recorder fields without labels."""
		parent = self.parent
		groupBox = parent.parent if parent else None
		label = groupBox.firstChild if groupBox else None
		if label and label.name:
			labelName = label.name.split("  ", 1)[0]
			if labelName.casefold() == "incoming track":
				labelName = "offset"
			ui.message(labelName)
		super().event_gainFocus()


class AppModule(appModuleHandler.AppModule):
	def __init__(self, processID: int, appName: str | None = None):
		"""Initialize track caches and suspend Studio background event tracking."""
		super().__init__(processID, appName)
		if splbase.studioIsRunning(justChecking=True):
			log.debug("SPL: VT Recorder is online, disabling background event tracking for Studio")
			for appMod in appModuleHandler.runningTable.values():
				if appMod.appName == "splstudio":
					# The below function removes background event tracker for apps through accept events set manipulation.
					# Call the function instead of duplicating the function body.
					eventHandler.handleAppTerminate(appMod)
					break
		else:
			log.debug("SPL: Studio is not running")
		# for caching
		self.outgoingTrack: NVDAObject | None = None
		self.outgoingTrackName = ""
		self.incomingTrack: NVDAObject | None = None
		self.incomingTrackName = ""

	def terminate(self):
		"""Reset recorder state and restore Studio event tracking when applicable."""
		resetInfoParts()
		super().terminate()
		if splbase.studioIsRunning(justChecking=True):
			log.debug("SPL: VT Recorder is offline, enabling background event tracking for Studio")
			for pid, appMod in appModuleHandler.runningTable.items():
				if appMod.appName == "splstudio":
					eventHandler.requestEvents(
						eventName="nameChange", processId=pid, windowClassName="TStatusBar"
					)
					eventHandler.requestEvents(
						eventName="nameChange", processId=pid, windowClassName="TStaticText"
					)
					eventHandler.requestEvents(eventName="show", processId=pid, windowClassName="TRequests")
					break
		else:
			log.debug("SPL: Studio Recorder is offline and Studio is offline")

	def checkOutgoingAndIncomingTrack(self):
		"""Locate and cache the current outgoing and incoming track descriptions."""
		if self.outgoingTrack == None:
			self.outgoingTrack = self.findObject(OUTGOING_TRACK_GROUP, TRACK_TEXT_WINDOW_CLASS)
			self.outgoingTrackName = self._normaliseTrackName(self.outgoingTrack, "Outgoing track not found.")
		if self.incomingTrack == None:
			self.incomingTrack = self.findObject(INCOMING_TRACK_GROUP, TRACK_TEXT_WINDOW_CLASS)
			self.incomingTrackName = self._normaliseTrackName(self.incomingTrack, "Incoming track not found.")

	def _normaliseTrackName(self, track: NVDAObject | None, notFoundMessage: str) -> str:
		"""Convert a track object's multiline name into a single spoken string."""
		if track is None or track.name is None:
			return notFoundMessage
		return " - ".join(track.name.splitlines())

	def objectBelongsTo(self, obj: NVDAObject, groupBoxName: str) -> bool:
		"""Return whether an object belongs to the named recorder group box."""
		parent = obj.parent
		if parent is None:
			return False
		groupBox = parent.parent
		if groupBox is None or groupBox.windowClassName != "TGroupBox":
			return False
		groupBoxLabel = groupBox.firstChild
		if groupBoxLabel is None:
			return False
		return groupBoxLabel.name is not None and groupBoxLabel.name.startswith(groupBoxName)

	def findObject(self, groupBoxName: str, windowClassName: str) -> NVDAObject | None:
		"""Find the first foreground-window object matching a group and class."""
		objectsToSearch = [api.getForegroundObject()]
		while objectsToSearch:
			obj = objectsToSearch.pop()
			if obj.windowClassName == windowClassName and self.objectBelongsTo(obj, groupBoxName):
				return obj
			objectsToSearch.extend(reversed(obj.children))
		return None

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		"""Assign recorder-specific overlays to relevant accessible controls."""
		if obj.windowClassName == "TPanel":
			if self.objectBelongsTo(obj, "VT Recorder"):
				clsList.insert(0, CustomTPanel)
		elif (
			api.getForegroundObject().windowClassName == "TVTRecorderForm"
			and obj.windowClassName == "TGroupButton"
		):
			clsList.insert(0, CustomTRadioButton)
		elif obj.windowClassName == "TBitBtn":
			clsList.insert(0, CustomTBitBtn)
		elif obj.windowClassName == "TSpinEditMS" or obj.windowClassName == "TTntComboBox.UnicodeClass":
			clsList.insert(0, UnlabeledFields)

	@script(gesture="kb:NVDA+Control+1")
	def script_sayOutgoingAndIncomingTrack(self, gesture):
		"""Speak both tracks when VT Recorder is the foreground application."""
		if api.getForegroundObject().windowClassName != "TVTRecorderForm":
			return
		self.checkOutgoingAndIncomingTrack()
		speech.speakMessage(f"Outgoing: {self.outgoingTrackName} - incoming: {self.incomingTrackName}")

	@script(gesture="kb:NVDA+Control+2")
	def script_sayOutgoingTrack(self, gesture):
		"""Speak the outgoing track when VT Recorder is the foreground application."""
		if api.getForegroundObject().windowClassName != "TVTRecorderForm":
			return
		self.checkOutgoingAndIncomingTrack()
		speech.speakMessage(self.outgoingTrackName)

	@script(gesture="kb:NVDA+Control+3")
	def script_sayIncomingTrack(self, gesture):
		"""Speak the incoming track when VT Recorder is the foreground application."""
		if api.getForegroundObject().windowClassName != "TVTRecorderForm":
			return
		self.checkOutgoingAndIncomingTrack()
		speech.speakMessage(self.incomingTrackName)

	@script(gesture="kb:NVDA+Control+4")
	def script_brailleOutgoingAndIncomingTrack(self, gesture):
		"""Display both tracks in braille when VT Recorder is foreground."""
		if api.getForegroundObject().windowClassName != "TVTRecorderForm":
			return
		self.checkOutgoingAndIncomingTrack()
		brailleMessage(f"Out: {self.outgoingTrackName}; in: {self.incomingTrackName}")

	@script(gesture="kb:NVDA+Control+5")
	def script_brailleOutgoingTrack(self, gesture):
		"""Display the outgoing track in braille when VT Recorder is foreground."""
		if api.getForegroundObject().windowClassName != "TVTRecorderForm":
			return
		self.checkOutgoingAndIncomingTrack()
		brailleMessage(self.outgoingTrackName)

	@script(gesture="kb:NVDA+Control+6")
	def script_brailleIncomingTrack(self, gesture):
		"""Display the incoming track in braille when VT Recorder is foreground."""
		if api.getForegroundObject().windowClassName != "TVTRecorderForm":
			return
		self.checkOutgoingAndIncomingTrack()
		brailleMessage(self.incomingTrackName)
