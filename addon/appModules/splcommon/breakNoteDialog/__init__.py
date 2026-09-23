# part of stationPlaylist addOn for NVDA
# Copyright 2026 Marco Steinebach <studio@windyradio.de>, released under GPL.

# provides a dialog to easily create command-break notes for studio and creator.
# uses breakNotes.json to save the breakNotes itself and 
# helpTexts.txt for the corresponding help texts.

import ctypes
import wx
import api
import winUser
import NVDAObjects
import controlTypes
from scriptHandler import script
import ui

from .breakNoteDialog import BreakNoteDialog
from .storage import (
	ELEMENTS_FILE,
	ELEMENT_VALUES_FILE,
	HELP_TEXTS_FILE,
	BreakNoteStorage,
)
from .types import bnType

WM_REPLACESEL = 0x00C2
WM_SETTEXT = 0x000C


def breakNoteDialogAllowed(
	obj: NVDAObjects.NVDAObject,
	windowClassName: str,
) -> bool:
	# Limit the overlay to the additional-parameters edit field of the
	# Insert Tracks dialog and only when a Break Note track type is selected.
	if (
		obj.windowClassName != windowClassName
		or obj.role != controlTypes.Role.EDITABLETEXT
	):
		return False
	# check if dialog title is correct
	curObj = api.getForegroundObject()
	if (
		curObj is None
		or curObj.name != "Insert Tracks"
	):
		return False
	# The edit box is usually in the "Additional Parameters" group.
	# Some versions nest the group differently, so fall back to the parent chain.
	parent = obj.simpleParent or obj.parent
	if parent is None:
		return False
	if (
		parent.name != "Additional Parameters"
		or parent.windowClassName != "TGroupBox"
	):
		ancestor = parent
		while ancestor is not None:
			if (
				ancestor.name == "Additional Parameters"
				and ancestor.windowClassName == "TGroupBox"
			):
				parent = ancestor
				break
			nextAncestor = ancestor.simpleParent or ancestor.parent
			if nextAncestor is ancestor:
				break
			ancestor = nextAncestor
		if (
			parent is None
			or parent.name != "Additional Parameters"
			or parent.windowClassName != "TGroupBox"
		):
			return False
	curObj = parent.simpleNext
	if curObj is None:
		return False
	# in Studio this should be the Group of radio buttons for track type,
	# in creator the radio buttons itself.
	if (
		curObj.name == "Track Type"
		and curObj.windowClassName == "TRadioGroup"
	):
		curObj = curObj.simpleFirstChild
	if (
		curObj is None
		or curObj.windowClassName not in ("TGroupButton", "TRadioButton")
	):
		return False
	# we are on a radio button, now go to the first one
	firstSibling = curObj
	while firstSibling.simplePrevious:
		firstSibling = firstSibling.simplePrevious
	curObj = firstSibling
	# iterate through all siblings and find the checked Break Note radio button.
	while curObj:
		if (
			(
				curObj.name == "Break Note"
				or curObj.name == "Timed Break Note"
			)
			and controlTypes.State.CHECKED in curObj.states
		):
			return True
		curObj = curObj.simpleNext
	return False

class breakNoteDialogOverlay(NVDAObjects.NVDAObject):
	@script(
		gesture="kb:windows+alt+i")
	def script_breakNoteDialog(self, gesture):
		"""Open the break note dialog."""
		wx.CallAfter(self.createBreakNote)

	def initOverlayClass(self):
		self.filterSelection = 0
		self.storage = BreakNoteStorage(self.filterSelection)

	def loadHelpTexts(self, path=HELP_TEXTS_FILE):
		return self.storage.loadHelpTexts(path)

	def loadElements(self, path=ELEMENTS_FILE):
		elements = self.storage.loadElements(path)
		self.filterSelection = self.storage.filterSelection
		return elements

	def saveElementValues(self, elements, path=ELEMENT_VALUES_FILE):
		self.storage.filterSelection = self.filterSelection
		self.storage.saveElementValues(elements, path)

	def saveElementFavorites(self, elements, path=ELEMENT_VALUES_FILE):
		self.storage.saveElementFavorites(elements, path)

	def createTextFromBreakNote(self, element):
		# Convert the structured selection back to StationPlaylist's break-note
		# command syntax, including quoting paths that contain spaces.
		if element.code == "":
			return "" if element.value is None else str(element.value)

		concurrentPrefix = "!" if element.isConcurrent else ""
		value = "" if element.value is None else element.value
		if element.code == "TestMode":
			value = f"={'on' if value == 1 else 'off'}"
		if element.type == bnType.text and value:
			if element.code:
				value = f"{'' if element.code.endswith('=') else '='}{value}"
		if element.type in (bnType.typeAndDir, bnType.typeAndFile):
			if value is None:
				value = ""
			else:
				typeCode, path = value
				path = f'"{path}"' if " " in path else path
				position = f"[{element.position}]" if element.position else ""
				value = f"{typeCode}{position}{path}"
		if element.type in (bnType.dir, bnType.file) and " " in str(value):
			value = f'"{value}"'
		return f"*{concurrentPrefix}{element.code}{value}"


	def createBreakNote(self, elements=None):
		if elements is None:
			elements = self.loadElements()

		dialog = BreakNoteDialog(elements, self.storage, self.filterSelection)
		selectedElement = dialog.showBreakNoteDialog()
		self.filterSelection = dialog.filterSelection
		result = (
			self.createTextFromBreakNote(selectedElement)
			if selectedElement is not None
			else None
		)
		if result is not None and selectedElement.textInPlaylist:
			result += f"* {selectedElement.textInPlaylist}"
		if result is not None and selectedElement.duration:
			result = f"{selectedElement.duration}:{result}"

		if result is None:
			wx.CallLater(100, ui.message, "Break note insertion canceled!")
			return

		# Replace the source field's contents through the Win32 edit-control
		# messages; this also works when wx does not expose the native control.
		emptyBuffer = ctypes.create_unicode_buffer("")
		winUser.sendMessage(
			self.windowHandle,
			WM_SETTEXT,
			0,
			ctypes.addressof(emptyBuffer),
		)
		textBuffer = ctypes.create_unicode_buffer(result)
		winUser.sendMessage(
			self.windowHandle,
			WM_REPLACESEL,
			True,
			ctypes.addressof(textBuffer),
		)
		wx.CallLater(100, ui.message, "Break note inserted into text field.")
