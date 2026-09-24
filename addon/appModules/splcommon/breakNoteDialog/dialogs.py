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


class RecordFileDialog(wx.TextEntryDialog):
	def __init__(self, parent):
		super().__init__(
			parent,
			"Enter the file name, or leave empty for the default:",
			"Record to a file",
			"",
		)

	def getValue(self):
		try:
			if gui.displayDialogAsModal(self) != wx.ID_OK:
				return None
			return self.GetValue()
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
