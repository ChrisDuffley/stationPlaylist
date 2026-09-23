# part of stationPlaylist addOn for NVDA
# Copyright 2026 Marco Steinebach <studio@windyradio.de>, released under GPL.

# provides a dialog to easily create command-break notes for studio and creator.
# uses breakNotes.json to save the breakNotes itself and 
# helpTexts.txt for the corresponding help texts.

from __future__ import annotations

import re
from dataclasses import dataclass
from enum import Enum


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
