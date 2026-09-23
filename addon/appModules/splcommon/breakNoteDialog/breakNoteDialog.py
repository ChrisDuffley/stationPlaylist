# Part of stationPlaylist add-on for NVDA
# Copyright 2026 Marco Steinebach <studio@windyradio.de>, released under GPL.

# Provides a dialog to easily create command-break notes for studio and creator.
# Uses breakNotes.json to save the breakNotes itself and
# helpTexts.txt for the corresponding help texts.

import weakref
import gui
import ui
import wx

from .dialogs import (
	CartDialog,
	CartTypeDialog,
	DSPEffectNumberDialog,
	DSPEffectStateDialog,
	FavoriteDialog,
	FileTypeDialog,
	HookHourDialog,
	NumberDialog,
	PathDialog,
	PlayerDialog,
	RecordFileDialog,
	TextDialog,
	VolumeDialog,
)
from .storage import ELEMENT_VALUES_FILE, BreakNoteStorage
from .types import NUMBER_PATTERN, PLAYER_NAMES, bnType


class BreakNoteDialog:
	_instance: "weakref.ReferenceType[BreakNoteDialog] | None" = None

	def __new__(cls, *args, **kwargs):
		# Make this a singleton.
		instance = cls._instance() if cls._instance else None
		if instance is None:
			return super(BreakNoteDialog, cls).__new__(cls)
		raise RuntimeError("An instance of BreakNoteDialog is active")

	def __init__(self, elements, storage: BreakNoteStorage, filterSelection=0):
		inst = BreakNoteDialog._instance() if BreakNoteDialog._instance else None
		if inst:
			return
		# Use a weakref so the instance can die.
		BreakNoteDialog._instance = weakref.ref(self)

		self.elements = elements
		self.storage = storage
		self.filterSelection = filterSelection

	def saveElementValues(self, elements, path=ELEMENT_VALUES_FILE):
		self.storage.filterSelection = self.filterSelection
		self.storage.saveElementValues(elements, path)

	def saveElementFavorites(self, elements, path=ELEMENT_VALUES_FILE):
		self.storage.saveElementFavorites(elements, path)

	def editElementFavorites(self, parent, elements):
		favoriteStates = FavoriteDialog(parent, elements).getValues()
		if favoriteStates is None:
			return False
		for element, isFavorite in zip(elements, favoriteStates):
			element.isFavorite = isFavorite
		self.saveElementFavorites(elements)
		return True


	def _formatNumericValue(self, value):
		if isinstance(value, int):
			return str(value)
		normalized = format(value, "f")
		if "." in normalized:
			normalized = normalized.rstrip("0").rstrip(".")
		if normalized in ("-0", "-0.0"):
			return "0"
		return normalized or "0"


	def getNumberValue(self, parent, element):
		kind = element.kind
		title = f"enter {kind} for {element.name}"
		if element.unit:
			title += f" in {element.unit}"
		if element.minimum is not None and element.maximum is not None:
			title += f", between {element.minimum} and {element.maximum}"
		label = kind
		allowEmpty = element.allowEmpty
		allowZero = element.allowZero
		minimum = element.minimum
		maximum = element.maximum

		while True:
			enteredValue = NumberDialog(parent, title, f"&{label}").getValue()
			if enteredValue is None:
				return None

			if allowEmpty and not enteredValue:
				return ""
			if not enteredValue or enteredValue in {"+", "-", ".", "+.", "-."}:
				numberValue = None
			else:
				if not NUMBER_PATTERN.fullmatch(enteredValue):
					numberValue = None
				else:
					try:
						numberValue = float(enteredValue)
					except ValueError:
						numberValue = None

			if (
				numberValue is not None
				and (minimum is None or numberValue >= minimum)
				and (maximum is None or numberValue <= maximum)
				and (numberValue != 0 or allowZero)
			):
				return self._formatNumericValue(numberValue)

			wx.MessageBox(
				(
					f"Please enter a number between {minimum} and {maximum}."
					if minimum is not None and maximum is not None
					else "Please enter a number."
				),
				"Invalid number",
				wx.OK | wx.ICON_ERROR,
				parent,
			)


	def getTextValue(self, parent, element):
		enteredText = TextDialog(parent, element.textValues).getValue()
		if enteredText is None:
			return None

		if not enteredText.strip():
			wx.MessageBox(
				"Please enter some text.",
				"Invalid text",
				wx.OK | wx.ICON_ERROR,
				parent,
			)
			return None

		if enteredText not in element.textValues:
			element.textValues += (enteredText,)
		return enteredText


	def getTypeAndPathValue(self, parent, element):
		typeCode = FileTypeDialog(parent).getValue()
		if typeCode is None:
			return None
		path = PathDialog(parent, element.type == bnType.typeAndDir).getValue()
		return None if path is None else (typeCode, path)


	def getPlayerVolumeValue(self, parent):
		playerNumber = PlayerDialog(parent).getValue()
		if playerNumber is None:
			return None

		while True:
			enteredValue = VolumeDialog(
				parent,
				PLAYER_NAMES[playerNumber - 1],
			).getValue()
			if enteredValue is None:
				return None

			if enteredValue.isdigit() and 0 <= int(enteredValue) <= 100:
				return f"{playerNumber}={int(enteredValue)}"

			wx.MessageBox(
				"Please enter a whole number between 0 and 100.",
				"Invalid volume",
				wx.OK | wx.ICON_ERROR,
				parent,
			)


	def getCartValue(self, parent, breakNoteCode, element):
		cartTypeCode = CartTypeDialog(parent).getValue()
		if cartTypeCode is None:
			return None
		cartNumber = CartDialog(parent).getValue()
		if cartNumber is None:
			return None

		cartValue = f"{cartTypeCode}{cartNumber:02d}"
		if breakNoteCode == "C":
			position = self.getNumberValue(
				parent,
				element,
			)
			if position is None:
				return None
			if position:
				cartValue += f"={position}"
		return cartValue


	def getRecordValue(self, parent, element):
		duration = self.getNumberValue(parent, element)
		if duration is None:
			return None

		fileName = RecordFileDialog(parent).getValue()
		if fileName is None:
			return None

		return (f"[{duration}]" if duration else "") + fileName


	def getHookValue(self, parent, element):
		hookPrefix = HookHourDialog(parent).getValue()
		if hookPrefix is None:
			return None

		trackNumber = self.getNumberValue(parent, element)
		if trackNumber is None:
			return None
		return f"={hookPrefix}{trackNumber}"


	def getDSPValue(self, parent):
		while True:
			effectNumber = DSPEffectNumberDialog(parent).getValue()
			if effectNumber is None:
				return None

			if effectNumber.isdigit() and 1 <= int(effectNumber) <= 20:
				break

			wx.MessageBox(
				"Please enter a whole number between 1 and 20.",
				"Invalid DSP effect",
				wx.OK | wx.ICON_ERROR,
				parent,
			)

		state = DSPEffectStateDialog(parent).getValue()
		if state is None:
			return None

		return f"{effectNumber}={state}"


	def getElementLabel(self, element):
		if element.type == bnType.onOff:
			state = "on" if element.value == 1 else "off"
			return f"{element.name} ({state})"
		return element.name


	def showBreakNoteDialog(self):
		elements = self.elements
		dialog = wx.Dialog(
			None,
			title="Create a break note",
		)
		mainSizer = wx.BoxSizer(wx.VERTICAL)

		description = wx.TextCtrl(
			dialog,
			value=(
				"select a break note in the list. Press the space bar to edit the "
				"parameters of the selected break note, if any."
			),
			style=wx.TE_READONLY,
		)
		mainSizer.Add(description, 0, wx.ALL | wx.EXPAND, 10)

		filterSizer = wx.BoxSizer(wx.HORIZONTAL)
		filterLabel = wx.StaticText(dialog, label="&Filter:")
		elementFilter = wx.ComboBox(
			dialog,
			choices=[
				"show all break notes",
				"show favorite break notes",
			],
			style=wx.CB_READONLY,
		)
		elementFilter.SetSelection(self.filterSelection)
		filterSizer.Add(filterLabel, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
		filterSizer.Add(elementFilter, 1, wx.RIGHT | wx.EXPAND, 10)
		editFavoritesButton = wx.Button(dialog, label="&Edit favorites")
		filterSizer.Add(editFavoritesButton, 0)
		mainSizer.Add(filterSizer, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)

		listLabel = wx.StaticText(
			dialog,
			label="&Select a break note to create:",
		)
		elementList = wx.ListBox(dialog)
		helpLabel = wx.StaticText(dialog, label="&Help text:")
		helpField = wx.TextCtrl(
			dialog,
			style=wx.TE_MULTILINE | wx.TE_READONLY,
		)

		textInPlaylistLabel = wx.StaticText(
			dialog,
			label="&Text to be displayed in the playlist:",
		)
		textInPlaylist = wx.TextCtrl(dialog)
		durationLabel = wx.StaticText(dialog, label="&Duration:")
		duration = wx.TextCtrl(dialog)

		mainSizer.Add(durationLabel, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)
		mainSizer.Add(duration, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)
		mainSizer.Add(textInPlaylistLabel, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)
		mainSizer.Add(textInPlaylist, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)
		mainSizer.Add(listLabel, 0, wx.ALL, 10)
		mainSizer.Add(elementList, 1, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)
		mainSizer.Add(helpLabel, 0, wx.TOP | wx.LEFT | wx.RIGHT, 10)
		mainSizer.Add(helpField, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)

		visibleElements = []

		def getSelectedElement():
			# The list contains only the currently visible subset of elements.
			selection = elementList.GetSelection()
			return visibleElements[selection] if selection >= 0 else None

		def updateHelpText(event):
			selectedElement = getSelectedElement()
			helpField.SetValue(selectedElement.helpText if selectedElement else "")
			textInPlaylist.ChangeValue(
				selectedElement.textInPlaylist if selectedElement else ""
			)
			duration.ChangeValue(selectedElement.duration if selectedElement else "")
			checkbox.SetValue(
				selectedElement.isConcurrent if selectedElement else False
			)
			event.Skip()

		elementList.Bind(wx.EVT_LISTBOX, updateHelpText)

		def saveSelectedElement(event):
			selection = elementList.GetSelection()
			if selection >= 0:
				selectedElement = visibleElements[selection]
				for elementIndex, element in enumerate(elements):
					element.isLastSelected = element is selectedElement
				self.saveElementValues(elements)
			updateHelpText(event)

		elementList.Bind(wx.EVT_LISTBOX, saveSelectedElement)

		def updateElementList(event=None):
			nonlocal visibleElements
			# Rebuild the list after changing the filter or favorite flags while
			# retaining the current selection whenever possible.
			self.filterSelection = elementFilter.GetSelection()
			self.saveElementValues(elements)
			selectedElementID = (
				getSelectedElement().ID if elementList.GetSelection() >= 0 else None
			)
			showFavorites = elementFilter.GetSelection() == 1
			visibleElements = [
				element for element in elements
				if self.filterSelection == 0 or element.isFavorite
			]
			elementList.SetItems(
				[self.getElementLabel(element) for element in visibleElements]
			)
			selectedIndex = next(
				(
					elementIndex
					for elementIndex, element in enumerate(visibleElements)
					if element.ID == (selectedElementID or 0)
				),
				wx.NOT_FOUND,
			)
			if selectedIndex == wx.NOT_FOUND and not selectedElementID:
				selectedIndex = next(
					(
						elementIndex
						for elementIndex, element in enumerate(visibleElements)
						if element.isLastSelected
					),
					wx.NOT_FOUND,
				)
			if selectedIndex != wx.NOT_FOUND:
				elementList.SetSelection(selectedIndex)
				updateHelpText(wx.CommandEvent())
			else:
				updateHelpText(wx.CommandEvent())

		elementFilter.Bind(wx.EVT_COMBOBOX, updateElementList)

		def editFavorites(event):
			if self.editElementFavorites(dialog, elements):
				updateElementList()
			event.Skip()

		editFavoritesButton.Bind(wx.EVT_BUTTON, editFavorites)

		def updateTextInPlaylist(event):
			selectedElement = getSelectedElement()
			if selectedElement:
				selectedElement.textInPlaylist = textInPlaylist.GetValue()
				self.saveElementValues(elements)
			event.Skip()

		textInPlaylist.Bind(wx.EVT_TEXT, updateTextInPlaylist)

		def updateDuration(event):
			selectedElement = getSelectedElement()
			value = duration.GetValue().strip()
			if selectedElement and (not value or value.isdigit() and int(value) > 0):
				selectedElement.duration = value
				self.saveElementValues(elements)
			event.Skip()

		duration.Bind(wx.EVT_TEXT, updateDuration)

		checkbox = wx.CheckBox(dialog, label="This is a &concurrent break note")

		def updateCheckbox(event):
			selectedElement = getSelectedElement()
			if selectedElement:
				selectedElement.isConcurrent = checkbox.GetValue()
			event.Skip()

		checkbox.Bind(wx.EVT_CHECKBOX, updateCheckbox)

		def showElementMenu(event):
			if event.GetKeyCode() != wx.WXK_SPACE:
				event.Skip()
				return

			selectedElement = getSelectedElement()
			if selectedElement is None:
				return

			# Some break notes need dedicated dialogs because their parameter
			# syntax combines several values (for example cart type and number).
			if selectedElement.code == "PlayerVol":
				value = self.getPlayerVolumeValue(dialog)
				if value is not None:
					selectedElement.value = value
				return
			if selectedElement.code in ("C", "O"):
				value = self.getCartValue(dialog, selectedElement.code, selectedElement)
				if value is not None:
					selectedElement.value = value
				return
			if selectedElement.ID == 46:
				value = self.getRecordValue(dialog, selectedElement)
				if value is not None:
					selectedElement.value = value
				return
			if selectedElement.ID == 27:
				value = self.getHookValue(dialog, selectedElement)
				if value is not None:
					selectedElement.value = value
				return
			if selectedElement.code == "Dsp":
				value = self.getDSPValue(dialog)
				if value is not None:
					selectedElement.value = value
				return
			if selectedElement.type == bnType.onOff:
				selectedElement.value = 0 if selectedElement.value == 1 else 1
				elementList.SetString(
					elementList.GetSelection(), self.getElementLabel(selectedElement)
				)
				return
			if selectedElement.type == bnType.noParm:
				ui.message ("Parameters not allowed for the selected break note")
				return
			if selectedElement.type in (bnType.typeAndDir, bnType.typeAndFile):
				value = self.getTypeAndPathValue(dialog, selectedElement)
				if value is None:
					return
				if selectedElement.ID == 25:
					position = self.getNumberValue(
						dialog,
						selectedElement,
					)
					if position is None:
						return
					selectedElement.position = position
				selectedElement.value = value
				return
			if selectedElement.type == bnType.file:
				with wx.FileDialog(
					dialog,
					message="Select a file",
					style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
				) as fileDialog:
					if gui.displayDialogAsModal(fileDialog) == wx.ID_OK:
						selectedElement.value = fileDialog.GetPath()
				return
			if selectedElement.type == bnType.dir:
				with wx.DirDialog(
					dialog,
					message="Select a folder",
					style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST,
				) as dirDialog:
					if gui.displayDialogAsModal(dirDialog) == wx.ID_OK:
						selectedElement.value = dirDialog.GetPath()
				return
			if selectedElement.type == bnType.number:
				numberValue = self.getNumberValue(dialog, selectedElement)
				if numberValue is not None:
					selectedElement.value = numberValue
				return
			if selectedElement.type == bnType.text:
				enteredText = self.getTextValue(dialog, selectedElement)
				if enteredText is not None:
					selectedElement.value = enteredText
					self.saveElementValues(elements)
				return
			if selectedElement.type == bnType.menu:
				menu = wx.Menu()
				menuItems = {}
				for menuIndex, menuLabel in enumerate(selectedElement.menuItems):
					menuItem = menu.Append(wx.ID_ANY, menuLabel)
					menuItems[menuItem.GetId()] = menuIndex

				def saveMenuValue(menuEvent):
					selectedElement.value = menuItems[menuEvent.GetId()]
					menuEvent.Skip()

				for menuItem in menu.GetMenuItems():
					menu.Bind(wx.EVT_MENU, saveMenuValue, menuItem)

				try:
					elementList.PopupMenu(menu)
				finally:
					menu.Destroy()
				return

		elementList.Bind(wx.EVT_KEY_DOWN, showElementMenu)

		mainSizer.Add(checkbox, 0, wx.ALL, 10)

		buttonSizer = dialog.CreateStdDialogButtonSizer(wx.OK | wx.CANCEL)
		mainSizer.Add(buttonSizer, 0, wx.ALL | wx.EXPAND, 10)
		okButton = dialog.FindWindowById(wx.ID_OK)
		if okButton is None:
			raise RuntimeError("The dialog OK button could not be found.")

		def validateDuration(event):
			value = duration.GetValue().strip()
			if value and (not value.isdigit() or int(value) <= 0):
				wx.MessageBox(
					"Duration must be empty or a number greater than 0.",
					"Invalid duration",
					wx.OK | wx.ICON_ERROR,
					dialog,
				)
				duration.SetFocus()
				return
			event.Skip()

		okButton.Bind(wx.EVT_BUTTON, validateDuration)

		dialog.SetSizerAndFit(mainSizer)
		updateElementList()

		def notifyNVDAFocus():
			if not dialog.IsShown():
				return
			dialog.Raise()
			elementList.SetFocus()
			try:
				focusObject = getNVDAObjectFromEvent(
					elementList.GetHandle(),
					winUser.OBJID_CLIENT,
					0,
				)
			except LookupError:
				return

		def setInitialFocus(event=None):
			if event is not None:
				event.Skip()
			if dialog.IsShown():
				notifyNVDAFocus()

		def focusShownDialog(event):
			event.Skip()
			if event.IsShown():
				# Focus can be restored to the source control while the modal dialog
				# is being shown, so set it again after wx has activated the dialog.
				wx.CallAfter(notifyNVDAFocus)

		dialog.Bind(wx.EVT_SHOW, focusShownDialog)
		wx.CallAfter(setInitialFocus)

		try:
			result = gui.displayDialogAsModal(dialog)
			if result == wx.ID_OK:
				return getSelectedElement()
			else:
				return None
		finally:
			dialog.Destroy()
