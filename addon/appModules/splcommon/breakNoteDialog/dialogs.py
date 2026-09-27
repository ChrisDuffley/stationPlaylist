# Part of stationPlaylist add-on for NVDA
# Copyright 2026 Marco Steinebach <studio@windyradio.de>, released under GPL.

# Provides a dialog to easily create command-break notes for studio and creator.
# Uses breakNotes.json to save the breakNotes itself and
# helpTexts.txt for the corresponding help texts.

import gui
import wx
from gui.nvdaControls import CustomCheckListBox

from .types import CART_NAMES, CART_TYPES, DIR_FILE_TYPES, PLAYER_NAMES


class NumberDialog(wx.Dialog):
	def __init__(self, parent, title, label):
		super().__init__(parent, title=title)
		dialogSizer = wx.BoxSizer(wx.VERTICAL)
		dialogSizer.Add(
			wx.StaticText(self, label=label),
			0,
			wx.LEFT | wx.RIGHT | wx.EXPAND,
			10,
		)
		self.field = wx.TextCtrl(self)
		dialogSizer.Add(self.field, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)
		dialogSizer.Add(
			self.CreateStdDialogButtonSizer(wx.OK | wx.CANCEL),
			0,
			wx.ALL | wx.EXPAND,
			10,
		)
		self.SetSizerAndFit(dialogSizer)
		self.field.SetFocus()

	def getValue(self):
		try:
			if gui.displayDialogAsModal(self) != wx.ID_OK:
				return None
			return self.field.GetValue().strip()
		finally:
			self.Destroy()


class TextDialog(wx.Dialog):
	def __init__(self, parent, values, title="Enter text"):
		super().__init__(parent, title=title)
		dialogSizer = wx.BoxSizer(wx.VERTICAL)
		dialogSizer.Add(wx.StaticText(self, label="Enter text:"), 0, wx.ALL, 10)
		self.field = wx.ComboBox(
			self,
			choices=list(values),
			style=wx.CB_DROPDOWN,
		)
		dialogSizer.Add(self.field, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)
		dialogSizer.Add(
			self.CreateStdDialogButtonSizer(wx.OK | wx.CANCEL),
			0,
			wx.ALL | wx.EXPAND,
			10,
		)
		self.SetSizerAndFit(dialogSizer)
		self.field.SetFocus()

	def getValue(self):
		try:
			if gui.displayDialogAsModal(self) != wx.ID_OK:
				return None
			return self.field.GetValue()
		finally:
			self.Destroy()


class FileTypeDialog(wx.SingleChoiceDialog):
	def __init__(self, parent):
		super().__init__(
			parent,
			"Select the file type:",
			"Select file type",
			[label for label, _ in DIR_FILE_TYPES],
		)

	def getValue(self):
		try:
			if gui.displayDialogAsModal(self) != wx.ID_OK:
				return None
			return DIR_FILE_TYPES[self.GetSelection()][1]
		finally:
			self.Destroy()


class PathDialog:
	def __init__(self, parent, selectDirectory):
		super().__init__()
		self.parent = parent
		self.selectDirectory = selectDirectory

	def getValue(self):
		if self.selectDirectory:
			dialog = wx.DirDialog(
				self.parent,
				message="Select a folder",
				style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST,
			)
		else:
			dialog = wx.FileDialog(
				self.parent,
				message="Select a file",
				style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
			)
		try:
			if gui.displayDialogAsModal(dialog) != wx.ID_OK:
				return None
			return dialog.GetPath()
		finally:
			dialog.Destroy()



class CartDialog(wx.Dialog):
	def __init__(self, parent, element, showPosition=False):
		super().__init__(parent, title=f"{element.name}")
		self.element = element
		dialogSizer = wx.BoxSizer(wx.VERTICAL)

		cartTypeLabel = wx.StaticText(self, label="Select the cart &type:")
		self.cartTypeCombo = wx.ComboBox(
			self,
			choices=[cartType[0] for cartType in CART_TYPES],
			style=wx.CB_READONLY,
		)
		self.cartTypeCombo.SetSelection(0)
		dialogSizer.Add(cartTypeLabel, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 10)
		dialogSizer.Add(self.cartTypeCombo, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)

		cartNameLabel = wx.StaticText(self, label="Select the cart:")
		self.cartNameCombo = wx.ComboBox(
			self,
			choices=CART_NAMES,
			style=wx.CB_READONLY,
		)
		self.cartNameCombo.SetSelection(0)
		dialogSizer.Add(cartNameLabel, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 10)
		dialogSizer.Add(self.cartNameCombo, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)

		if showPosition:
			positionLabel = wx.StaticText(
				self, label=f"Enter the &{element.kind}:"
			)
			self.positionField = wx.TextCtrl(self)
			dialogSizer.Add(
				positionLabel, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 10
			)
			dialogSizer.Add(
				self.positionField, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10
			)

		dialogSizer.Add(
			self.CreateStdDialogButtonSizer(wx.OK | wx.CANCEL),
			0,
			wx.ALL | wx.EXPAND,
			10,
		)
		self.SetSizerAndFit(dialogSizer)
		self.cartTypeCombo.SetFocus()

	def getValue(self):
		try:
			if gui.displayDialogAsModal(self) != wx.ID_OK:
				return None
			cartTypeCode = CART_TYPES[self.cartTypeCombo.GetSelection()][1]
			cartNumber = self.cartNameCombo.GetSelection() + 1
			cartValue = f"{cartTypeCode}{cartNumber:02d}"
			if hasattr(self, "positionField"):
				position = self.positionField.GetValue().strip()
				allowEmpty = self.element.allowEmpty
				minimum = self.element.minimum
				maximum = self.element.maximum
				if allowEmpty and not position:
					return cartValue
				if not position or not position.isdigit():
					wx.MessageBox(
						"Please enter a whole number.",
						"Invalid position",
						wx.OK | wx.ICON_ERROR,
						self,
					)
					self.positionField.SetFocus()
					return self.getValue()
				num = int(position)
				if (minimum is not None and num < minimum) or (
					maximum is not None and num > maximum
				):
					wx.MessageBox(
						f"Please enter a whole number between {minimum} and {maximum}.",
						"Invalid position",
						wx.OK | wx.ICON_ERROR,
						self,
					)
					self.positionField.SetFocus()
					return self.getValue()
				cartValue += f"={position}"
			return cartValue
		finally:
			self.Destroy()



class DSPEffectDialog(wx.Dialog):
	def __init__(self, parent, element):
		super().__init__(parent, title="DSP effect")
		self.element = element
		dialogSizer = wx.BoxSizer(wx.VERTICAL)

		effectNumberLabel = wx.StaticText(
			self, label=f"Enter the &{element.kind}:"
		)
		self.effectNumberField = wx.TextCtrl(self)
		dialogSizer.Add(
			effectNumberLabel, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 10
		)
		dialogSizer.Add(
			self.effectNumberField, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10
		)

		effectStateLabel = wx.StaticText(self, label="Select the DSP effect &state:")
		self.effectStateCombo = wx.ComboBox(
			self,
			choices=["on", "off"],
			style=wx.CB_READONLY,
		)
		self.effectStateCombo.SetSelection(0)
		dialogSizer.Add(
			effectStateLabel, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 10
		)
		dialogSizer.Add(
			self.effectStateCombo, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10
		)

		dialogSizer.Add(
			self.CreateStdDialogButtonSizer(wx.OK | wx.CANCEL),
			0,
			wx.ALL | wx.EXPAND,
			10,
		)
		self.SetSizerAndFit(dialogSizer)
		self.effectNumberField.SetFocus()

	def getValue(self):
		try:
			if gui.displayDialogAsModal(self) != wx.ID_OK:
				return None
			effectNumber = self.effectNumberField.GetValue().strip()
			allowEmpty = self.element.allowEmpty
			minimum = self.element.minimum
			maximum = self.element.maximum
			if allowEmpty and not effectNumber:
				return ""
			if not effectNumber or not effectNumber.isdigit():
				wx.MessageBox(
					"Please enter a whole number.",
					"Invalid DSP effect",
					wx.OK | wx.ICON_ERROR,
					self,
				)
				self.effectNumberField.SetFocus()
				return self.getValue()
			num = int(effectNumber)
			if (minimum is not None and num < minimum) or (
				maximum is not None and num > maximum
			):
				wx.MessageBox(
					f"Please enter a whole number between {minimum} and {maximum}.",
					"Invalid DSP effect",
					wx.OK | wx.ICON_ERROR,
					self,
				)
				self.effectNumberField.SetFocus()
				return self.getValue()
			state = "1" if self.effectStateCombo.GetSelection() == 0 else "0"
			return f"{effectNumber}={state}"
		finally:
			self.Destroy()


class RecordAllDialog(wx.Dialog):
	def __init__(self, parent, element):
		super().__init__(parent, title=f"Record to file - {element.name}")
		self.element = element
		dialogSizer = wx.BoxSizer(wx.VERTICAL)

		modeLabel = wx.StaticText(self, label="Record &mode:")
		self.modeCombo = wx.ComboBox(
			self,
			choices=["on", "off", "only set file"],
			style=wx.CB_READONLY,
		)
		self.modeCombo.SetSelection(0)
		dialogSizer.Add(modeLabel, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 10)
		dialogSizer.Add(self.modeCombo, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)

		durationLabel = wx.StaticText(
			self,
			label=f"Enter the &{element.kind} (between {element.minimum} and {element.maximum}):"
		)
		self.durationField = wx.TextCtrl(self)
		dialogSizer.Add(durationLabel, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 10)
		dialogSizer.Add(self.durationField, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)

		def updateDurationVisibility(event=None):
			visible = self.modeCombo.GetSelection() == 0
			durationLabel.Show(visible)
			self.durationField.Show(visible)
			if not visible:
				self.durationField.SetValue("")
			self.Layout()

		self.modeCombo.Bind(wx.EVT_COMBOBOX, updateDurationVisibility)
		updateDurationVisibility()

		fileNameLabel = wx.StaticText(self, label="&File name:")
		fileNameSizer = wx.BoxSizer(wx.HORIZONTAL)
		self.fileNameField = wx.TextCtrl(self)
		fileNameSizer.Add(self.fileNameField, 1, wx.RIGHT, 5)
		browseButton = wx.Button(self, label="&Browse...")
		fileNameSizer.Add(browseButton, 0)
		dialogSizer.Add(fileNameLabel, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 10)
		dialogSizer.Add(fileNameSizer, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)

		def browseForFile(event):
			with wx.FileDialog(
				self,
				message="Select a file",
				style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
			) as fileDialog:
				if gui.displayDialogAsModal(fileDialog) == wx.ID_OK:
					self.fileNameField.SetValue(fileDialog.GetPath())

		browseButton.Bind(wx.EVT_BUTTON, browseForFile)

		dialogSizer.Add(
			self.CreateStdDialogButtonSizer(wx.OK | wx.CANCEL),
			0,
			wx.ALL | wx.EXPAND,
			10,
		)
		self.SetSizerAndFit(dialogSizer)
		self.modeCombo.SetFocus()

	def getValue(self):
		try:
			if gui.displayDialogAsModal(self) != wx.ID_OK:
				return None
			mode = self.modeCombo.GetSelection()
			duration = self.durationField.GetValue().strip()
			allowEmpty = self.element.allowEmpty
			minimum = self.element.minimum
			maximum = self.element.maximum
			if duration and (not duration.isdigit() or not minimum <= int(duration) <= maximum):
				wx.MessageBox(
					f"Duration must be empty or a number between {minimum} and {maximum}.",
					"Invalid duration",
					wx.OK | wx.ICON_ERROR,
					self,
				)
				self.durationField.SetFocus()
				return self.getValue()
			fileName = self.fileNameField.GetValue().strip()
			if " " in fileName and not (fileName.startswith('"') and fileName.endswith('"')):
				fileName = f'"{fileName}"'
			modeSuffix = ("1", "0", "")[mode]
			durationPart = f"[{duration}]" if duration else ""
			fileNamePart = f"={fileName}" if fileName else ""
			return f"{modeSuffix}{durationPart}{fileNamePart}"
		finally:
			self.Destroy()


class PlayerVolumeDialog(wx.Dialog):
	def __init__(self, parent, element):
		super().__init__(parent, title=f"Player volume - {element.name}")
		self.element = element
		dialogSizer = wx.BoxSizer(wx.VERTICAL)

		playerLabel = wx.StaticText(self, label="Select the &player:")
		self.playerCombo = wx.ComboBox(
			self,
			choices=PLAYER_NAMES,
			style=wx.CB_READONLY,
		)
		self.playerCombo.SetSelection(0)
		dialogSizer.Add(playerLabel, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 10)
		dialogSizer.Add(self.playerCombo, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)

		volumeLabel = wx.StaticText(
			self, label=f"Enter the &{element.kind}:"
		)
		self.volumeField = wx.TextCtrl(self)
		dialogSizer.Add(volumeLabel, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 10)
		dialogSizer.Add(self.volumeField, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)

		dialogSizer.Add(
			self.CreateStdDialogButtonSizer(wx.OK | wx.CANCEL),
			0,
			wx.ALL | wx.EXPAND,
			10,
		)
		self.SetSizerAndFit(dialogSizer)
		self.playerCombo.SetFocus()

	def getValue(self):
		try:
			if gui.displayDialogAsModal(self) != wx.ID_OK:
				return None
			playerIndex = self.playerCombo.GetSelection()
			playerNumber = playerIndex + 1
			volume = self.volumeField.GetValue().strip()
			allowEmpty = self.element.allowEmpty
			minimum = self.element.minimum
			maximum = self.element.maximum
			if allowEmpty and not volume:
				return f"{playerNumber}="
			if not volume or not volume.isdigit():
				wx.MessageBox(
					"Please enter a whole number.",
					"Invalid volume",
					wx.OK | wx.ICON_ERROR,
					self,
				)
				self.volumeField.SetFocus()
				return self.getValue()
			num = int(volume)
			if (minimum is not None and num < minimum) or (
				maximum is not None and num > maximum
			):
				wx.MessageBox(
					f"Please enter a whole number between {minimum} and {maximum}.",
					"Invalid volume",
					wx.OK | wx.ICON_ERROR,
					self,
				)
				self.volumeField.SetFocus()
				return self.getValue()
			return f"{playerNumber}={num}"
		finally:
			self.Destroy()


class PlayFileDialog(wx.Dialog):
	def __init__(self, parent):
		super().__init__(parent, title="Play a file")
		dialogSizer = wx.BoxSizer(wx.VERTICAL)

		typeLabel = wx.StaticText(self, label="Select the file &type:")
		self.typeCombo = wx.ComboBox(
			self,
			choices=[label for label, _ in DIR_FILE_TYPES],
			style=wx.CB_READONLY,
		)
		self.typeCombo.SetSelection(0)
		dialogSizer.Add(typeLabel, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 10)
		dialogSizer.Add(self.typeCombo, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)

		fileLabel = wx.StaticText(self, label="Select the &file:")
		fileSizer = wx.BoxSizer(wx.HORIZONTAL)
		self.fileField = wx.TextCtrl(self)
		fileSizer.Add(self.fileField, 1, wx.RIGHT, 5)
		browseButton = wx.Button(self, label="&Browse...")
		fileSizer.Add(browseButton, 0)
		dialogSizer.Add(fileLabel, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 10)
		dialogSizer.Add(fileSizer, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)

		def browseForFile(event):
			with wx.FileDialog(
				self,
				message="Select a file",
				style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
			) as fileDialog:
				if gui.displayDialogAsModal(fileDialog) == wx.ID_OK:
					self.fileField.SetValue(fileDialog.GetPath())

		browseButton.Bind(wx.EVT_BUTTON, browseForFile)

		dialogSizer.Add(
			self.CreateStdDialogButtonSizer(wx.OK | wx.CANCEL),
			0,
			wx.ALL | wx.EXPAND,
			10,
		)
		self.SetSizerAndFit(dialogSizer)
		self.typeCombo.SetFocus()

	def getValue(self):
		try:
			if gui.displayDialogAsModal(self) != wx.ID_OK:
				return None
			typeCode = DIR_FILE_TYPES[self.typeCombo.GetSelection()][1]
			file = self.fileField.GetValue().strip()
			return (typeCode, file)
		finally:
			self.Destroy()


class HookDialog(wx.Dialog):
	def __init__(self, parent, element):
		super().__init__(parent, title="Hook playback")
		self.element = element
		dialogSizer = wx.BoxSizer(wx.VERTICAL)

		hourLabel = wx.StaticText(self, label="Select the &hour to hook:")
		self.hourCombo = wx.ComboBox(
			self,
			choices=["Current hour", "Next hour"],
			style=wx.CB_READONLY,
		)
		self.hourCombo.SetSelection(0)
		dialogSizer.Add(hourLabel, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 10)
		dialogSizer.Add(self.hourCombo, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)

		trackLabel = wx.StaticText(
			self, label=f"Enter the &{element.kind}:"
		)
		self.trackField = wx.TextCtrl(self)
		dialogSizer.Add(trackLabel, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 10)
		dialogSizer.Add(self.trackField, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)

		dialogSizer.Add(
			self.CreateStdDialogButtonSizer(wx.OK | wx.CANCEL),
			0,
			wx.ALL | wx.EXPAND,
			10,
		)
		self.SetSizerAndFit(dialogSizer)
		self.hourCombo.SetFocus()

	def getValue(self):
		try:
			if gui.displayDialogAsModal(self) != wx.ID_OK:
				return None
			hourPrefix = "" if self.hourCombo.GetSelection() == 0 else "N"
			trackNumber = self.trackField.GetValue().strip()
			allowEmpty = self.element.allowEmpty
			minimum = self.element.minimum
			maximum = self.element.maximum
			if allowEmpty and not trackNumber:
				return f"={hourPrefix}"
			if not trackNumber or not trackNumber.isdigit():
				wx.MessageBox(
					"Please enter a whole number.",
					"Invalid track number",
					wx.OK | wx.ICON_ERROR,
					self,
				)
				self.trackField.SetFocus()
				return self.getValue()
			num = int(trackNumber)
			if (minimum is not None and num < minimum) or (
				maximum is not None and num > maximum
			):
				wx.MessageBox(
					f"Please enter a whole number between {minimum} and {maximum}.",
					"Invalid track number",
					wx.OK | wx.ICON_ERROR,
					self,
				)
				self.trackField.SetFocus()
				return self.getValue()
			return f"={hourPrefix}{trackNumber}"
		finally:
			self.Destroy()


class FolderDialog(wx.Dialog):
	def __init__(self, parent, element, showPosition=False):
		super().__init__(parent, title=f"{element.name}")
		self.element = element
		dialogSizer = wx.BoxSizer(wx.VERTICAL)

		typeLabel = wx.StaticText(self, label="Select the file &type:")
		self.typeCombo = wx.ComboBox(
			self,
			choices=[label for label, _ in DIR_FILE_TYPES],
			style=wx.CB_READONLY,
		)
		self.typeCombo.SetSelection(0)
		dialogSizer.Add(typeLabel, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 10)
		dialogSizer.Add(self.typeCombo, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)

		folderLabel = wx.StaticText(self, label="Select the &folder:")
		folderSizer = wx.BoxSizer(wx.HORIZONTAL)
		self.folderField = wx.TextCtrl(self)
		folderSizer.Add(self.folderField, 1, wx.RIGHT, 5)
		browseButton = wx.Button(self, label="&Browse...")
		folderSizer.Add(browseButton, 0)
		dialogSizer.Add(folderLabel, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 10)
		dialogSizer.Add(folderSizer, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)

		def browseForFolder(event):
			with wx.DirDialog(
				self,
				message="Select a folder",
				style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST,
			) as dirDialog:
				if gui.displayDialogAsModal(dirDialog) == wx.ID_OK:
					self.folderField.SetValue(dirDialog.GetPath())

		browseButton.Bind(wx.EVT_BUTTON, browseForFolder)

		if showPosition:
			positionLabel = wx.StaticText(
				self, label=f"Enter the &{element.kind}:"
			)
			self.positionField = wx.TextCtrl(self)
			dialogSizer.Add(
				positionLabel, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 10
			)
			dialogSizer.Add(
				self.positionField, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10
			)

		dialogSizer.Add(
			self.CreateStdDialogButtonSizer(wx.OK | wx.CANCEL),
			0,
			wx.ALL | wx.EXPAND,
			10,
		)
		self.SetSizerAndFit(dialogSizer)
		self.typeCombo.SetFocus()

	def getValue(self):
		try:
			if gui.displayDialogAsModal(self) != wx.ID_OK:
				return None
			typeCode = DIR_FILE_TYPES[self.typeCombo.GetSelection()][1]
			folder = self.folderField.GetValue().strip()
			if hasattr(self, "positionField"):
				position = self.positionField.GetValue().strip()
				allowEmpty = self.element.allowEmpty
				minimum = self.element.minimum
				maximum = self.element.maximum
				if allowEmpty and not position:
					return (typeCode, folder, "")
				if not position or not position.isdigit():
					wx.MessageBox(
						"Please enter a whole number.",
						"Invalid position",
						wx.OK | wx.ICON_ERROR,
						self,
					)
					self.positionField.SetFocus()
					return self.getValue()
				num = int(position)
				if (minimum is not None and num < minimum) or (
					maximum is not None and num > maximum
				):
					wx.MessageBox(
						f"Please enter a whole number between {minimum} and {maximum}.",
						"Invalid position",
						wx.OK | wx.ICON_ERROR,
						self,
					)
					self.positionField.SetFocus()
					return self.getValue()
				return (typeCode, folder, position)
			return (typeCode, folder)
		finally:
			self.Destroy()


class FavoriteDialog(wx.Dialog):
	def __init__(self, parent, elements):
		super().__init__(parent, title="Edit favorites", size=(500, 600))
		self.elements = elements
		dialogSizer = wx.BoxSizer(wx.VERTICAL)
		dialogSizer.Add(
			wx.StaticText(self, label="&Select favorite break notes:"),
			0,
			wx.LEFT | wx.RIGHT | wx.TOP,
			10,
		)
		self.favoriteList = CustomCheckListBox(
			self,
			choices=[element.name for element in elements],
		)
		dialogSizer.Add(self.favoriteList, 1, wx.ALL | wx.EXPAND, 10)
		for index, element in enumerate(elements):
			self.favoriteList.Check(index, check=element.isFavorite)
		if elements:
			self.favoriteList.SetSelection(0)
		dialogSizer.Add(
			self.CreateStdDialogButtonSizer(wx.OK | wx.CANCEL),
			0,
			wx.ALL | wx.EXPAND,
			10,
		)
		self.SetSizer(dialogSizer)
		self.Layout()
		self.favoriteList.SetFocus()

	def getValues(self):
		try:
			if gui.displayDialogAsModal(self) != wx.ID_OK:
				return None
			return [
				self.favoriteList.IsChecked(index)
				for index in range(len(self.elements))
			]
		finally:
			self.Destroy()
