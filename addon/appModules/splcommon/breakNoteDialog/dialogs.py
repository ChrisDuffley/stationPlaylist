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
	def __init__(self, parent, values):
		super().__init__(parent, title="Enter text")
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


class PlayerDialog(wx.SingleChoiceDialog):
	def __init__(self, parent):
		super().__init__(parent, "Select the player:", "Select player", PLAYER_NAMES)

	def getValue(self):
		try:
			if gui.displayDialogAsModal(self) != wx.ID_OK:
				return None
			return self.GetSelection() + 1
		finally:
			self.Destroy()


class VolumeDialog(NumberDialog):
	def __init__(self, parent, playerName):
		super().__init__(
			parent,
			"Player volume",
			f"Enter volume, between 0 and 100, for {playerName}:",
		)


class CartTypeDialog(wx.SingleChoiceDialog):
	def __init__(self, parent):
		super().__init__(
			parent,
			"Select the cart type:",
			"Select cart type",
			[cartType[0] for cartType in CART_TYPES],
		)

	def getValue(self):
		try:
			if gui.displayDialogAsModal(self) != wx.ID_OK:
				return None
			return CART_TYPES[self.GetSelection()][1]
		finally:
			self.Destroy()


class CartDialog(wx.SingleChoiceDialog):
	def __init__(self, parent):
		super().__init__(parent, "Select the cart:", "Select cart", CART_NAMES)

	def getValue(self):
		try:
			if gui.displayDialogAsModal(self) != wx.ID_OK:
				return None
			return self.GetSelection() + 1
		finally:
			self.Destroy()


class HookHourDialog(wx.SingleChoiceDialog):
	def __init__(self, parent):
		super().__init__(
			parent,
			"Select the hour to hook:",
			"Select hook hour",
			("Current hour", "Next hour"),
		)

	def getValue(self):
		try:
			if gui.displayDialogAsModal(self) != wx.ID_OK:
				return None
			return "" if self.GetSelection() == 0 else "N"
		finally:
			self.Destroy()


class DSPEffectNumberDialog(NumberDialog):
	def __init__(self, parent):
		super().__init__(parent, "DSP effect", "Enter the DSP effect number (1-20):")


class DSPEffectStateDialog(wx.SingleChoiceDialog):
	def __init__(self, parent):
		super().__init__(
			parent,
			"Select the DSP effect state:",
			"DSP effect state",
			("on", "off"),
		)

	def getValue(self):
		try:
			if gui.displayDialogAsModal(self) != wx.ID_OK:
				return None
			return "1" if self.GetSelection() == 0 else "0"
		finally:
			self.Destroy()


class RecordAllDialog(wx.Dialog):
	def __init__(self, parent):
		super().__init__(parent, title="Record to file")
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

		durationLabel = wx.StaticText(self, label="Enter a duration between 1 and 99999")
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
			if duration and (not duration.isdigit() or not 1 <= int(duration) <= 99999):
				wx.MessageBox(
					"Duration must be empty or a number between 1 and 99999.",
					"Invalid duration",
					wx.OK | wx.ICON_ERROR,
					self,
				)
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
