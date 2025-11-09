# SPL Studio common constants
# An app module and global plugin package for NVDA
# Copyright 2015-2025 Joseph Lee, released under GPL.
# Common constants across the add-on modules
# Split from splmisc module in 2025.

# Manual definitions of cart keys.
# For use in cart explorer (Studio app module) and carts without borders (global plugin)
cartKeys = (
	# Function key carts (Studio all editions)
	"f1",
	"f2",
	"f3",
	"f4",
	"f5",
	"f6",
	"f7",
	"f8",
	"f9",
	"f10",
	"f11",
	"f12",
	# Number row (all editions except Standard)
	"1",
	"2",
	"3",
	"4",
	"5",
	"6",
	"7",
	"8",
	"9",
	"0",
	"-",
	"=",
)

# Studio status messages.
# Local Studio allows fetching status bar info from anywhere via Studio API,
# including playback and automation status.
# For consistency reasons (because of the Studio status bar),
# messages in this collection will remain in English.
# Local Studio 6.11 and earlier and 6.20 have different messages.
_studioStatusMessages = (
	["Play status: Stopped", "Play status: Playing"],
	["Automation Off", "Automation On"],
	["Microphone Off", "Microphone On"],
	["Line-In Off", "Line-In On"],
	["Record to file Off", "Record to file On"],
)

_studio620StatusMessages = (
	["Play status: Stopped", "Play status: Playing"],
	["Automate Off", "Automate On"],
	["Mic Off", "Mic On"],
	["Line Off", "Line On"],
	["Record to file Off", "Record to file On"],
)

# Customize attribute access (mostly for status messages).
def __getattr__(attribute: str):
	match attribute:
		case "studioStatusMessages":  # Status bar messages
			# Return the appropriate status messages based on local Studio version (lparam = 2).
			# Base services is supposed to be a separate entity.
			from . import splbase
			if (studioVersion := splbase.studioAPI(0, 2)) is not None and studioVersion >= 620:
				return _studio620StatusMessages
			else:
				return _studioStatusMessages
		case _:
			raise AttributeError(f"module {repr(__name__)} has no attribute {repr(attribute)}")
