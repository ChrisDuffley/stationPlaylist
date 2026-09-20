# -*- coding: utf-8 -*-

import ctypes
import globalPluginHandler
from scriptHandler import script
import api
import controlTypes
import gui
import winUser
import wx
import NVDAObjects.behaviors
import speech
from . import breakNote

WM_REPLACESEL = 0x00C2
WM_SETTEXT = 0x000C


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
  def _createBreakNoteResult(self, windowHandle, result):
    if result is None:
      wx.CallLater (100, speech.speakMessage, "Break note insertion canceled!")
      return
    # clear whole text field
    emptyBuffer = ctypes.create_unicode_buffer("")
    winUser.sendMessage(
      windowHandle,
      WM_SETTEXT,
      0,
      ctypes.addressof(emptyBuffer),
    )
    # send created break note to the text field.
    textBuffer = ctypes.create_unicode_buffer(result)
    winUser.sendMessage(
      windowHandle,
      WM_REPLACESEL,
      True,
      ctypes.addressof(textBuffer),
    )
    wx.CallLater (100, speech.speakMessage, "Break note inserted into text field.")

  @script(  
    gesture="kb:windows+alt+i")
  def script_testBreakNoteDialog(self, gesture):
    textField = api.getFocusObject()
    isEditableText = (
      textField.role == controlTypes.Role.EDITABLETEXT
      or controlTypes.State.EDITABLE in textField.states
      or isinstance(textField, NVDAObjects.behaviors.EditableText)
    )
    if not isEditableText:
      wx.CallAfter(
        gui.messageBox,
        "The break note dialog can only be opened from an input field.",
        "Break note",
        wx.OK | wx.ICON_ERROR,
        gui.mainFrame,
      )
      return

    wx.CallAfter(
      breakNote.createBreakNote,
      lambda result: self._createBreakNoteResult(
        textField.windowHandle,
        result,
      ),
    )
