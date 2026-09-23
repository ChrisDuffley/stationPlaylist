# part of stationPlaylist addOn for NVDA
# Copyright 2026 Marco Steinebach <studio@windyradio.de>, released under GPL.

# provides a dialog to easily create command-break notes for studio and creator.
# uses breakNotes.json to save the breakNotes itself and 
# helpTexts.txt for the corresponding help texts.

import json
from pathlib import Path

import globalVars

from .types import BreakNoteElement, bnType


ELEMENTS_FILE = Path(__file__).with_name("breakNotes.json")
BREAK_NOTE_SETTINGS_DIR = Path(globalVars.appArgs.configPath) / "stationPlaylist"
ELEMENT_VALUES_FILE = BREAK_NOTE_SETTINGS_DIR / "breakNoteSettings.json"
HELP_TEXTS_FILE = Path(__file__).with_name("helpTexts.txt")
LAST_SELECTED_ELEMENT_KEY = "_lastSelectedElementID"
FILTER_SELECTION_KEY = "_filterSelection"
FAVORITE_ELEMENT_IDS_KEY = "_favoriteElementIDs"


class BreakNoteStorage:
	def __init__(self, filterSelection=0):
		self.filterSelection = filterSelection

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

		favoriteElementIDs = elementValues.get(FAVORITE_ELEMENT_IDS_KEY, [])
		if not isinstance(favoriteElementIDs, list) or any(
			not isinstance(elementID, int) or isinstance(elementID, bool) or elementID <= 0
			for elementID in favoriteElementIDs
		):
			raise ValueError(f"{FAVORITE_ELEMENT_IDS_KEY} must be a list of positive integers.")
		favoriteIDSet = set(favoriteElementIDs)

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

		# Validate the JSON definition while converting it to typed elements.
		# Invalid add-on data should fail early instead of producing bad notes.
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
					isFavorite=elementID in favoriteIDSet,
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
		# Store only user-editable values; the element definitions remain in
		# breakNotes.json so updates to the add-on can change their metadata.
		values = {}
		selectedElementID = None
		favoriteElementIDs = []
		for element in elements:
			if element.isLastSelected:
				selectedElementID = element.ID
			if element.isFavorite:
				favoriteElementIDs.append(element.ID)
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
		if favoriteElementIDs:
			values[FAVORITE_ELEMENT_IDS_KEY] = favoriteElementIDs
		values[FILTER_SELECTION_KEY] = self.filterSelection

		path.parent.mkdir(parents=True, exist_ok=True)
		with path.open("w", encoding="utf-8", newline="\n") as valuesFile:
			json.dump(values, valuesFile, ensure_ascii=False, indent=2)
			valuesFile.write("\n")

	def saveElementFavorites(self, elements, path=ELEMENT_VALUES_FILE):
		# Store favorite flags in the user config file instead of mutating the
		# add-on definition file, so the defaults remain clean and updateable.
		values = {}
		if path.exists():
			with path.open(encoding="utf-8") as valuesFile:
				values = json.load(valuesFile)
			if not isinstance(values, dict):
				raise ValueError("The element values file must contain a JSON object.")
		values[FAVORITE_ELEMENT_IDS_KEY] = [
			element.ID for element in elements if element.isFavorite
		]
		path.parent.mkdir(parents=True, exist_ok=True)
		with path.open("w", encoding="utf-8", newline="\n") as valuesFile:
			json.dump(values, valuesFile, ensure_ascii=False, indent=2)
			valuesFile.write("\n")
