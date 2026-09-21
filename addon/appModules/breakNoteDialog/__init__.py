import json
import re
import ctypes
from enum import Enum
from dataclasses import dataclass
from pathlib import Path

import gui
import wx
import api
import speech
import winUser
import eventHandler
import NVDAObjects
import controlTypes
from NVDAObjects.IAccessible import getNVDAObjectFromEvent
from scriptHandler import script
from logHandler import log

WM_REPLACESEL = 0x00C2
WM_SETTEXT = 0x000C


BREAK_NOTE_DIALOG_HINT = "Enter your break note"


def getBreakNoteDialogHint():
  import inputCore

  gestureNameByIdentifier = {
    gesture: None
    for gesture, scriptName in getattr(
      breakNoteDialogOverlay,
      "_breakNoteDialogOverlay__gestures",
      {},
    ).items()
    if scriptName == "breakNoteDialog"
  }
  for gestureMap in (
    inputCore.manager.localeGestureMap,
    inputCore.manager.userGestureMap,
  ):
    mappings = {}
    for cls, gesture, scriptName in gestureMap.getScriptsForAllGestures():
      if cls is breakNoteDialogOverlay:
        mappings.setdefault(gesture, []).append(scriptName)
    for gesture, scriptNames in mappings.items():
      if scriptNames[-1] == "breakNoteDialog":
        gestureNameByIdentifier[gesture] = None
      else:
        gestureNameByIdentifier.pop(gesture, None)

  for gesture in gestureNameByIdentifier:
    try:
      gestureName = inputCore.getDisplayTextForGestureIdentifier(gesture)[1]
    except LookupError:
      log.exception("Unable to determine the break note dialog gesture.")
      continue
    return (
      f"{BREAK_NOTE_DIALOG_HINT} or press {gestureName} "
      "to open break note dialog."
    )
  return BREAK_NOTE_DIALOG_HINT


class bnType(Enum):
  noParm = "noParm"
  file = "file"
  dir = "dir"
  typeAndDir = "typeAndDir"
  typeAndFile = "typeAndFile"
  number = "number"
  onOff = "onOff"
  special = "special"
  menu = "menu"
  text = "text"


@dataclass
class BreakNoteElement:
  ID: int
  name: str
  type: bnType
  helpText: str
  code: str
  isFavourite: bool = False
  isLastSelected: bool = False
  value: int | str | tuple[str, str] | None = None
  position: str = ""
  minimum: int | float | None = None
  maximum: int | float | None = None
  kind: str = ""
  unit: str = ""
  allowZero: bool = False
  allowEmpty: bool = False
  menuItems: tuple[str, ...] = ()
  isConcurrent: bool = False
  textInPlaylist: str = ""
  textValues: tuple[str, ...] = ()
  duration: str = ""


ELEMENTS_FILE = Path(__file__).with_name("elements.json")
ELEMENT_VALUES_FILE = Path(__file__).with_name("elementValues.json")
HELP_TEXTS_FILE = Path(__file__).with_name("helpTexts.txt")
LAST_SELECTED_ELEMENT_KEY = "_lastSelectedElementID"
FILTER_SELECTION_KEY = "_filterSelection"
DIR_FILE_TYPES = (
  ("Songs", "0"),
  ("Spots", "1"),
  ("Jingles", "2"),
  ("Commercials", "5"),
  ("Voice Intros", "7"),
  ("Voice Outros", "8"),
)
PLAYER_NAMES = (
  "Main Player",
  "Voice Track Player",
  "Cart Player 1",
  "Cart Player 2",
  "Microphone",
  "Line Output",
  "Mixer",
  "Monitor Output",
)
NUMBER_PATTERN = re.compile(r"^[+-]?(?:\d+\.?\d*|\.\d+)$")
CART_TYPES = (
  ("Main cart", "M"),
  ("Shift cart", "S"),
  ("Control cart", "C"),
  ("Alt cart", "A"),
)
CART_NAMES = tuple(
  [f"F{index} -" for index in range(1, 13)]
  + [f"{index} -" for index in range(1, 13)]
)


def breakNoteDialogAllowed(
  obj: NVDAObjects.NVDAObject,
  windowClassName: str,
) -> bool:
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
    log.info("Dialogtitle is wrong!")
    if curObj:
      log.info(curObj.name)
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
      obj.name = getBreakNoteDialogHint()
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

  def loadHelpTexts(self, path=HELP_TEXTS_FILE):
    helpTexts = {}
    currentKey = None
    currentLines = []

    with path.open(encoding="utf-8") as helpTextsFile:
      for line in helpTextsFile:
        line = line.rstrip("\r\n")
        if line.startswith("[") and line.endswith("]"):
          if currentKey is not None:
            helpTexts[currentKey] = "\n".join(currentLines).strip()
          currentKey = line[1:-1]
          if not currentKey or currentKey in helpTexts:
            raise ValueError(f"Invalid or duplicate help text key: {currentKey!r}.")
          currentLines = []
        elif currentKey is None:
          if line.strip():
            raise ValueError("Help text content must follow a section key.")
        else:
          currentLines.append(line)

    if currentKey is not None:
      helpTexts[currentKey] = "\n".join(currentLines).strip()

    return helpTexts


  def loadElements(self, path=ELEMENTS_FILE):
    with path.open(encoding="utf-8") as elementsFile:
      values = json.load(elementsFile)

    if not isinstance(values, list):
      raise ValueError("The elements file must contain a JSON array.")

    helpTexts = self.loadHelpTexts()
    if ELEMENT_VALUES_FILE.exists():
      with ELEMENT_VALUES_FILE.open(encoding="utf-8") as valuesFile:
        elementValues = json.load(valuesFile)
      if not isinstance(elementValues, dict):
        raise ValueError("The element values file must contain a JSON object.")
    else:
      elementValues = {}

    lastSelectedElementID = elementValues.get(LAST_SELECTED_ELEMENT_KEY)
    self.filterSelection = elementValues.get(FILTER_SELECTION_KEY, 0)
    if (
      not isinstance(self.filterSelection, int)
      or isinstance(self.filterSelection, bool)
      or self.filterSelection not in (0, 1)
    ):
      raise ValueError(f"{FILTER_SELECTION_KEY} must be 0 or 1.")
    if (
      lastSelectedElementID is not None
      and (
        not isinstance(lastSelectedElementID, int)
        or isinstance(lastSelectedElementID, bool)
        or lastSelectedElementID <= 0
      )
    ):
      raise ValueError(
        f"{LAST_SELECTED_ELEMENT_KEY} must be a positive integer."
      )

    elements = []
    elementIDs = set()
    for value in values:
      elementID = value.get("ID")
      if not isinstance(elementID, int) or isinstance(elementID, bool) or elementID <= 0:
        raise ValueError(
          f"Element {value.get('name', '<unnamed>')!r} must define a positive integer ID."
        )
      if elementID in elementIDs:
        raise ValueError(f"Duplicate element ID: {elementID}.")
      elementIDs.add(elementID)

      elementType = bnType(value["type"])
      minimum = value.get("minimum")
      maximum = value.get("maximum")
      kind = value.get("kind", "")
      unit = value.get("unit", "")
      allowZero = value.get("allowZero")
      allowEmpty = value.get("allowEmpty", False)
      menuItems = tuple(value.get("menuItems", ()))
      if elementType == bnType.number and (minimum is None or maximum is None):
        raise ValueError(
          f"Number element {value['name']!r} must define minimum and maximum."
        )
      if elementType == bnType.number and not isinstance(allowZero, bool):
        raise ValueError(
          f"Number element {value['name']!r} must define allowZero as a boolean."
        )
      if elementType == bnType.number and not isinstance(allowEmpty, bool):
        raise ValueError(
          f"Number element {value['name']!r} must define allowEmpty as a boolean."
        )
      if elementType == bnType.number and (
        not isinstance(kind, str) or not kind.strip()
        or not isinstance(unit, str)
      ):
        raise ValueError(
          f"Number element {value['name']!r} must define kind as a non-empty "
          "string and unit as a string."
        )
      if elementType == bnType.menu and not menuItems:
        raise ValueError(
          f"Menu element {value['name']!r} must define menuItems."
        )
      isFavourite = value.get("isFavourite", False)
      if not isinstance(isFavourite, bool):
        raise ValueError(
          f"Element {value['name']!r} must define isFavourite as a boolean."
        )
      storedValues = elementValues.get(value["name"], {})
      if not isinstance(storedValues, dict):
        raise ValueError(
          f"Values for element {value['name']!r} must be a JSON object."
        )
      elements.append(
        BreakNoteElement(
          ID=elementID,
          name=value["name"],
          type=elementType,
          helpText=helpTexts[value["helpTextKey"]],
          code=value["code"],
          isFavourite=isFavourite,
          isLastSelected=elementID == lastSelectedElementID,
          value=0 if elementType == bnType.onOff else None,
          minimum=minimum,
          maximum=maximum,
          kind=kind,
          unit=unit,
          allowZero=allowZero if isinstance(allowZero, bool) else False,
          allowEmpty=allowEmpty if isinstance(allowEmpty, bool) else False,
          menuItems=menuItems,
          isConcurrent=value.get("isConcurrent", False),
          textInPlaylist=storedValues.get(
            "textInPlaylist", value.get("textInPlaylist", "")
          ),
          textValues=tuple(
            storedValues.get("textValues", value.get("textValues", ()))
          ),
          duration=storedValues.get("duration", value.get("duration", "")),
        )
      )

    return tuple(elements)


  def saveElementValues(self, elements, path=ELEMENT_VALUES_FILE):
    values = {}
    selectedElementID = None
    for element in elements:
      if element.isLastSelected:
        selectedElementID = element.ID
      storedValue = {}
      if element.textInPlaylist:
        storedValue["textInPlaylist"] = element.textInPlaylist
      if element.textValues:
        storedValue["textValues"] = list(element.textValues)
      if element.duration:
        storedValue["duration"] = element.duration
      if storedValue:
        values[element.name] = storedValue
    if selectedElementID is not None:
      values[LAST_SELECTED_ELEMENT_KEY] = selectedElementID
    values[FILTER_SELECTION_KEY] = self.filterSelection

    with path.open("w", encoding="utf-8", newline="\n") as valuesFile:
      json.dump(values, valuesFile, ensure_ascii=False, indent=2)
      valuesFile.write("\n")


  def saveElementFavourites(self, elements, path=ELEMENTS_FILE):
    with path.open(encoding="utf-8") as elementsFile:
      values = json.load(elementsFile)
    elementsByID = {element.ID: element for element in elements}
    for value in values:
      element = elementsByID.get(value.get("ID"))
      if element is not None:
        value["isFavourite"] = element.isFavourite
    with path.open("w", encoding="utf-8", newline="\n") as elementsFile:
      json.dump(values, elementsFile, ensure_ascii=False, indent=2)
      elementsFile.write("\n")


  def editElementFavourites(self, parent, elements):
    dialog = wx.Dialog(parent, title="Edit favourites", size=(500, 600))
    dialogSizer = wx.BoxSizer(wx.VERTICAL)
    favouriteList = wx.ListBox(dialog, style=wx.LB_SINGLE)
    favouriteStates = [element.isFavourite for element in elements]

    def getFavouriteLabel(elementIndex):
      status = "checked" if favouriteStates[elementIndex] else "not checked"
      return f"{elements[elementIndex].name} [{status}]"

    favouriteList.SetItems([
      getFavouriteLabel(elementIndex)
      for elementIndex in range(len(elements))
    ])
    dialogSizer.Add(favouriteList, 1, wx.ALL | wx.EXPAND, 10)

    def toggleFavourite(event):
      if event.GetKeyCode() == wx.WXK_SPACE:
        selection = favouriteList.GetSelection()
        if selection >= 0:
          favouriteStates[selection] = not favouriteStates[selection]
          favouriteList.SetString(selection, getFavouriteLabel(selection))
        return
      event.Skip()

    favouriteList.Bind(wx.EVT_KEY_DOWN, toggleFavourite)
    buttonSizer = dialog.CreateStdDialogButtonSizer(wx.OK | wx.CANCEL)
    dialogSizer.Add(buttonSizer, 0, wx.ALL | wx.EXPAND, 10)
    dialog.SetSizer(dialogSizer)
    dialog.Layout()

    try:
      if gui.displayDialogAsModal(dialog) != wx.ID_OK:
        return False
      for element, isFavourite in zip(elements, favouriteStates):
        element.isFavourite = isFavourite
      self.saveElementFavourites(elements)
      return True
    finally:
      dialog.Destroy()


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
      numberDialog = wx.Dialog(parent, title=title)
      dialogSizer = wx.BoxSizer(wx.VERTICAL)
      numberLabel = wx.StaticText(
        numberDialog,
        label=label,
      )
      dialogSizer.Add(numberLabel, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)
      numberField = wx.TextCtrl(numberDialog)
      dialogSizer.Add(numberField, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)
      buttonSizer = numberDialog.CreateStdDialogButtonSizer(wx.OK | wx.CANCEL)
      dialogSizer.Add(buttonSizer, 0, wx.ALL | wx.EXPAND, 10)
      numberDialog.SetSizerAndFit(dialogSizer)
      numberField.SetFocus()

      try:
        if numberDialog.ShowModal() != wx.ID_OK:
          return None
        enteredValue = numberField.GetValue().strip()
      finally:
        numberDialog.Destroy()

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
    textDialog = wx.Dialog(parent, title="Enter text")
    dialogSizer = wx.BoxSizer(wx.VERTICAL)
    textLabel = wx.StaticText(textDialog, label="Enter text:")
    dialogSizer.Add(textLabel, 0, wx.ALL, 10)
    textComboBox = wx.ComboBox(
      textDialog,
      choices=list(element.textValues),
      style=wx.CB_DROPDOWN,
    )
    dialogSizer.Add(textComboBox, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)
    buttonSizer = textDialog.CreateStdDialogButtonSizer(wx.OK | wx.CANCEL)
    dialogSizer.Add(buttonSizer, 0, wx.ALL | wx.EXPAND, 10)
    textDialog.SetSizerAndFit(dialogSizer)
    textComboBox.SetFocus()

    try:
      if textDialog.ShowModal() != wx.ID_OK:
        return None
      enteredText = textComboBox.GetValue()
    finally:
      textDialog.Destroy()

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
    typeDialog = wx.SingleChoiceDialog(
      parent,
      "Select the file type:",
      "Select file type",
      [label for label, _ in DIR_FILE_TYPES],
    )
    try:
      if typeDialog.ShowModal() != wx.ID_OK:
        return None
      typeCode = DIR_FILE_TYPES[typeDialog.GetSelection()][1]
    finally:
      typeDialog.Destroy()

    if element.type == bnType.typeAndDir:
      pathDialog = wx.DirDialog(
        parent,
        message="Select a folder",
        style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST,
      )
    else:
      pathDialog = wx.FileDialog(
        parent,
        message="Select a file",
        style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
      )
    try:
      if pathDialog.ShowModal() != wx.ID_OK:
        return None
      return (typeCode, pathDialog.GetPath())
    finally:
      pathDialog.Destroy()


  def getPlayerVolumeValue(self, parent):
    playerDialog = wx.SingleChoiceDialog(
        parent,
        "Select the player:",
        "Select player",
        PLAYER_NAMES,
    )
    try:
        if playerDialog.ShowModal() != wx.ID_OK:
          return None
        playerNumber = playerDialog.GetSelection() + 1
    finally:
        playerDialog.Destroy()

    while True:
        volumeDialog = wx.Dialog(parent, title="Player volume")
        dialogSizer = wx.BoxSizer(wx.VERTICAL)
        volumeLabel = wx.StaticText(
          volumeDialog,
          label=(
            f"Enter volume, between 0 and 100, for "
            f"{PLAYER_NAMES[playerNumber - 1]}:"
          ),
        )
        dialogSizer.Add(volumeLabel, 0, wx.ALL, 10)
        volumeField = wx.TextCtrl(volumeDialog)
        dialogSizer.Add(volumeField, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)
        buttonSizer = volumeDialog.CreateStdDialogButtonSizer(wx.OK | wx.CANCEL)
        dialogSizer.Add(buttonSizer, 0, wx.ALL | wx.EXPAND, 10)
        volumeDialog.SetSizerAndFit(dialogSizer)
        volumeField.SetFocus()

        try:
          if volumeDialog.ShowModal() != wx.ID_OK:
            return None
          enteredValue = volumeField.GetValue().strip()
        finally:
          volumeDialog.Destroy()

        if enteredValue.isdigit() and 0 <= int(enteredValue) <= 100:
          return f"{playerNumber}={int(enteredValue)}"

        wx.MessageBox(
          "Please enter a whole number between 0 and 100.",
          "Invalid volume",
          wx.OK | wx.ICON_ERROR,
          parent,
        )


  def getCartValue(self, parent, breakNoteCode, element):
    cartTypeDialog = wx.SingleChoiceDialog(
        parent,
        "Select the cart type:",
        "Select cart type",
        [cartType[0] for cartType in CART_TYPES],
    )
    try:
        if cartTypeDialog.ShowModal() != wx.ID_OK:
          return None
        cartTypeCode = CART_TYPES[cartTypeDialog.GetSelection()][1]
    finally:
        cartTypeDialog.Destroy()

    cartDialog = wx.SingleChoiceDialog(
        parent,
        "Select the cart:",
        "Select cart",
        CART_NAMES,
    )
    try:
        if cartDialog.ShowModal() != wx.ID_OK:
          return None
        cartNumber = cartDialog.GetSelection() + 1
    finally:
        cartDialog.Destroy()

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

    fileDialog = wx.TextEntryDialog(
      parent,
      "Enter the file name, or leave empty for the default:",
      "Record to a file",
      "",
    )
    try:
      if fileDialog.ShowModal() != wx.ID_OK:
        return None
      fileName = fileDialog.GetValue()
    finally:
      fileDialog.Destroy()

    return (f"[{duration}]" if duration else "") + fileName


  def getHookValue(self, parent, element):
    hookDialog = wx.SingleChoiceDialog(
      parent,
      "Select the hour to hook:",
      "Select hook hour",
      ("Current hour", "Next hour"),
    )
    try:
      if hookDialog.ShowModal() != wx.ID_OK:
        return None
      hookPrefix = "" if hookDialog.GetSelection() == 0 else "N"
    finally:
      hookDialog.Destroy()

    trackNumber = self.getNumberValue(parent, element)
    if trackNumber is None:
      return None
    return f"={hookPrefix}{trackNumber}"


  def getDSPValue(self, parent):
    while True:
      effectDialog = wx.TextEntryDialog(
        parent,
        "Enter the DSP effect number (1-20):",
        "DSP effect",
        "",
      )
      try:
        if effectDialog.ShowModal() != wx.ID_OK:
          return None
        effectNumber = effectDialog.GetValue().strip()
      finally:
        effectDialog.Destroy()

      if effectNumber.isdigit() and 1 <= int(effectNumber) <= 20:
        break

      wx.MessageBox(
        "Please enter a whole number between 1 and 20.",
        "Invalid DSP effect",
        wx.OK | wx.ICON_ERROR,
        parent,
      )

    stateDialog = wx.SingleChoiceDialog(
      parent,
      "Select the DSP effect state:",
      "DSP effect state",
      ("on", "off"),
    )
    try:
      if stateDialog.ShowModal() != wx.ID_OK:
        return None
      state = "1" if stateDialog.GetSelection() == 0 else "0"
    finally:
      stateDialog.Destroy()

    return f"{effectNumber}={state}"


  def getElementLabel(self, element):
    if element.type == bnType.onOff:
      state = "on" if element.value == 1 else "off"
      return f"{element.name} ({state})"
    return element.name


  def showBreakNoteDialog(self, elements):
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
    elementFilter = wx.ComboBox(
      dialog,
      choices=[
        "show all break notes",
        "show favourite break notes",
      ],
      style=wx.CB_READONLY,
    )
    elementFilter.SetSelection(self.filterSelection)
    filterSizer.Add(elementFilter, 1, wx.RIGHT | wx.EXPAND, 10)
    editFavouritesButton = wx.Button(dialog, label="Edit favourites")
    filterSizer.Add(editFavouritesButton, 0)
    mainSizer.Add(filterSizer, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)

    listLabel = wx.StaticText(dialog, label="Select a break note to create:")
    elementList = wx.ListBox(dialog)
    helpLabel = wx.StaticText(dialog, label="Help text:")
    helpField = wx.TextCtrl(
      dialog,
      style=wx.TE_MULTILINE | wx.TE_READONLY,
    )

    textInPlaylistLabel = wx.StaticText(
      dialog,
      label="Text to be displayed in the playlist",
    )
    textInPlaylist = wx.TextCtrl(dialog)
    durationLabel = wx.StaticText(dialog, label="Duration")
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
      self.filterSelection = elementFilter.GetSelection()
      self.saveElementValues(elements)
      selectedElementID = (
        getSelectedElement().ID if elementList.GetSelection() >= 0 else None
      )
      showFavourites = elementFilter.GetSelection() == 1
      visibleElements = [
        element for element in elements
        if self.filterSelection == 0 or element.isFavourite
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

    def editFavourites(event):
      if self.editElementFavourites(dialog, elements):
        updateElementList()
      event.Skip()

    editFavouritesButton.Bind(wx.EVT_BUTTON, editFavourites)

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

    checkbox = wx.CheckBox(dialog, label="Is concurrent break note?")

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
        speech.speakMessage ("This break note has no parameters to select!")
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
          if fileDialog.ShowModal() == wx.ID_OK:
            selectedElement.value = fileDialog.GetPath()
        return
      if selectedElement.type == bnType.dir:
        with wx.DirDialog(
          dialog,
          message="Select a folder",
          style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST,
        ) as dirDialog:
          if dirDialog.ShowModal() == wx.ID_OK:
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
      eventHandler.queueEvent("gainFocus", focusObject)

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


  def createTextFromBreakNote(self, element):
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

    selectedElement = self.showBreakNoteDialog(elements)
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
      wx.CallLater(100, speech.speakMessage, "Break note insertion canceled!")
      return

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
    wx.CallLater(100, speech.speakMessage, "Break note inserted into text field.")
