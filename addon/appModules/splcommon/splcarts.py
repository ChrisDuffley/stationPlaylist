# SPL Studio carts manager
# An app module and global plugin package for NVDA
# Copyright 2015-2026 Joseph Lee, released under GPL.
# Base services to support cart explorer in local and Remote Studio.
# Split from splmisc module in 2025.

from typing import Any
import os
from _csv import reader  # For cart explorer.
from logHandler import log

# Manual definitions of cart keys.
# For use in cart explorer (Studio app module) and carts without borders (global plugin)
cartKeys = (
	# Function key carts (Studio all editions and Remote Studio without modifiers)
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

# Cart Explorer helper for local and Remote Studio
# While mechanics are similar, local and Remote Studio store carts in different formats
# (comma-separated values for local Studio, one cart per line in a dedicated data file for Remote Studio).
# Therefore, some functions will be duplicated.

def _populateCarts(
	carts: dict[str, Any],
	cartlst: list[str],
	modifier: str,
	standardEdition: bool = False,
	refresh: bool = False,
) -> None:
	# The real cart string parser, a helper for cart explorer for building cart entries.
	# Discard number row if SPL Standard is in use.
	if standardEdition:
		cartlst = cartlst[:12]
	# #148: obtain cart entry position through enumerate function.
	# Pos 1 through 12 = function carts, 13 through 24 = number row carts.
	# #147: note that 1 is subtracted from cart position as a tuple will be used to lookup cart keys.
	for pos, entry in enumerate(cartlst):
		# An unassigned cart is stored with three consecutive commas, so skip it.
		# If refresh is on, the cart we're dealing with
		# is the actual carts dictionary that was built previously.
		noEntry = ",,," in entry
		if noEntry and not refresh:
			continue
		# If a cart name has commas or other characters, SPL surrounds the cart name with quotes (""),
		# so parse it as well.
		if not entry.startswith('"'):
			cartName = entry.split(",")[0]
		else:
			cartName = entry.split('"')[1]
		cart = cartKeys[pos] if not modifier else "+".join([modifier, cartKeys[pos]])
		if noEntry and refresh:
			if cart in carts:
				del carts[cart]
		else:
			carts[cart] = cartName


# Cart file timestamps.
cartEditTimestamps: list[float] = []
cartEditRemoteTimestamps: float | None = None


# Initialize local Studio carts.
def _cartExplorerInitLocal(
	cartsDataPath: str,
	StudioTitle: str,
	refresh: bool = False,
	carts: dict[str, Any] | None = None,
) -> dict[str, Any]:
	global cartEditTimestamps
	# Use cart files in SPL's data folder to build carts dictionary.
	# use a combination of SPL user name and static cart location to locate cart bank files.
	# Once the cart banks are located, use the routines in the populate method above to assign carts.
	# Since sstandard edition does not support number row carts, skip them if told to do so.
	if carts is None:
		carts = {"standardLicense": StudioTitle.startswith("StationPlaylist Studio Standard")}
	# See if multiple users are using SPl Studio.
	userNameIndex = StudioTitle.find("-")
	# Read *.cart files and process the cart entries within
	# (be careful when these cart file names change between SPL releases).
	cartFiles = ["main carts.cart", "shift carts.cart", "ctrl carts.cart", "alt carts.cart"]
	if userNameIndex >= 0:
		cartFiles = [StudioTitle[userNameIndex + 2 :] + " " + cartFile for cartFile in cartFiles]
	faultyCarts = False
	if not refresh:
		cartEditTimestamps = []
	for f in cartFiles:
		# Only do this if told to build cart banks from scratch,
		# as refresh flag is set if cart explorer is active in the first place.
		try:
			mod = f.split()[-2]  # Checking for modifier string such as ctrl.
			# Todo: Check just in case some SPL flavors doesn't ship with a particular cart file.
		except IndexError:
			# In a rare event that the broadcaster has saved the cart bank with the name like "carts.cart".
			faultyCarts = True
			continue
		cartFile = os.path.join(cartsDataPath, f)
		# Cart explorer can safely assume that the cart bank exists if refresh flag is set.
		# But it falls apart if whitespaces are in the beginning or at the end of a user name.
		if not refresh and not os.path.isfile(cartFile):
			faultyCarts = True
			continue
		log.debug(f"SPL: examining carts from file {cartFile}")
		cartTimestamp = os.path.getmtime(cartFile)
		if refresh and cartEditTimestamps[cartFiles.index(f)] == cartTimestamp:
			log.debug("SPL: no changes to cart bank, skipping")
			continue
		cartEditTimestamps.append(cartTimestamp)
		with open(cartFile) as cartInfo:
			cl = [row for row in reader(cartInfo)]
		# Let empty string represent main cart bank to avoid this being partially consulted up to 24 times.
		# The below method will just check for string length, which is faster than looking for specific substring.
		# See the comment for _populate carts method for details.
		_populateCarts(
			carts,
			cl[1],
			mod if mod != "main" else "",
			standardEdition=carts["standardLicense"],
			refresh=refresh,
		)
		if not refresh:
			log.debug(f"SPL: carts processed so far: {(len(carts)-1)}")
	carts["faultyCarts"] = faultyCarts
	log.debug(f"SPL: total carts processed: {(len(carts)-2)}")
	return carts


# Initialize Remote Studio carts.
def _cartExplorerInitRemote(
	cartsDataPath: str,
	refresh: bool = False,
	carts: dict[str, Any] | None = None,
) -> dict[str, Any]:
	global cartEditRemoteTimestamps
	if carts is None:
		carts = {"faultyCarts": False}
	cartFile = os.path.join(cartsDataPath, "RemoteStudio.dat")
	# Check for existence of Remote Studio data file.
	if not os.path.isfile(cartFile):
		return {"faultyCarts": True}
	# The file stores Remote Studio settings in addition to cart assignments.
	# This file is changed whenever Remote Studio's options screen is closed.
	remoteStudioSettingsTimestamp = os.path.getmtime(cartFile)
	# Cart data has not changed.
	if refresh and cartEditRemoteTimestamps == remoteStudioSettingsTimestamp:
		carts["refresh"] = False
		return carts
	cartEditRemoteTimestamps = remoteStudioSettingsTimestamp
	# Parse remote Studio data file.
	# Each cart entry is on its own line (starting at line 14 for Remote Studio 6.20).
	# A local file or local Studio slot can be assigned (twelve slots, F1 through F12).
	# Local file: path (the entire path is recorded)
	# Studio cart: "* ({bankFile}{position})" e.g. MF05 for F5 (main cart position 5)
	log.debug(f"SPL: examining carts from file {cartFile}")
	with open(cartFile) as cartInfo:
		# Twelve cart slots in Remote Studio (starting on line 14)
		cl = [row for row in reader(cartInfo)][13:25]
	for pos, entry in enumerate(cl):
		if entry:
			remoteCartEntry = entry[0]
			if remoteCartEntry.startswith("*"):
				# Studio (remote) cart (parse the cart bank+position string of the form * ({cartBank}{pos}))
				remoteCartEntry = remoteCartEntry.partition("(")[-1][:-1]
				bank, position = remoteCartEntry[:2], int(remoteCartEntry[2:]) - 1
				# At least Studio cart position is known, so obtain it from cart keys.
				position = cartKeys[position]
				# Add appropriate modifiers (SF = Shift, CF = Control, AF = Alt, MF = none)
				match bank:
					case "SF":
						remoteCartEntry = f"Shift+{position}"
					case "CF":
						remoteCartEntry = f"Control+{position}"
					case "AF":
						remoteCartEntry = f"Alt+{position}"
					case _:
						remoteCartEntry = position
				remoteCartEntry = f"Studio cart ({remoteCartEntry})"
			else:
				# Local cart (only include base file name without the extension)
				remoteCartEntry = os.path.basename(remoteCartEntry).rpartition(".")[0]
				remoteCartEntry = f"Local cart ({remoteCartEntry})"
			carts[cartKeys[pos]] = remoteCartEntry
	# For compatibility with local Studio (Studio Pro is required, so set standard license flag to false)
	carts["standardLicense"] = False
	log.debug(f"SPL: total carts processed: {(len(carts)-2)}")
	# Set refresh flag to true so NVDA can notify users.
	if refresh:
		carts["refresh"] = True
	return carts


# Initialize Cart Explorer i.e. fetch carts.
# if told to refresh, timestamps will be checked and updated banks will be reassigned.
# Carts dictionary is used if and only if refresh is on, as it'll modify live carts.
def cartExplorerInit(
	StudioTitle: str,
	remoteStudio: bool = False,
	refresh: bool = False,
	carts: dict[str, Any] | None = None,
) -> dict[str, Any]:
	log.debug("SPL: refreshing Cart Explorer" if refresh else "preparing cart Explorer")
	# Use files in SPL's data folder to build carts dictionary
	# (local Studio = cart files, Remote Studio = app data).
	# Obtain the "real" path for SPL via environment variables and open the cart data folder.
	# Provided that Studio was installed using default path for 32-bit x86 programs.
	cartsDataPath = os.path.join(os.environ["PROGRAMFILES(X86)"], "StationPlaylist", "Data")
	if remoteStudio:
		return _cartExplorerInitRemote(cartsDataPath, refresh=refresh, carts=carts)
	else:
		return _cartExplorerInitLocal(cartsDataPath, StudioTitle, refresh=refresh, carts=carts)


# Refresh carts upon request.
# calls cart explorer init with special (internal) flags.
def cartExplorerRefresh(
	studioTitle: str,
	currentCarts: dict[str, Any],
	remoteStudio: bool = False
) -> dict[str, Any]:
	return cartExplorerInit(studioTitle, remoteStudio=remoteStudio, refresh=True, carts=currentCarts)
