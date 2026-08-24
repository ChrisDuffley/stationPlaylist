# SPL Studio menu item location workaround
# An app module and global plugin package for NVDA
# Copyright 2026 Joseph Lee, released under GPL.

# Workaround for menu item location issue (NVDA 2026.1 to 2026.2)
# NVDA Core issue 19225, resolved in NVDA 2026.3 (below code is sourced from NVDA Core)
# Patch in the order of: winBindings.user32, location helper, window utils, IAccessible object/menu item.

import math
import contextlib
from collections.abc import Iterator
import ctypes.wintypes
from ctypes import (
	WINFUNCTYPE,
	c_int,
)
from ctypes.wintypes import (
	BOOL,
	LPRECT,
	HMENU,
	HWND,
	UINT,
)
import winBindings.user32
import winUser
import locationHelper
from locationHelper import RectLTRB, RectLTWH
from NVDAObjects.IAccessible import MenuItem
from logHandler import log

# NVDA Core source/winBindings/user32.py

SetThreadDpiAwarenessContext = WINFUNCTYPE(None)(("SetThreadDpiAwarenessContext", winBindings.user32.dll))
"""
Set the DPI awareness for the current thread to the provided value.

.. seealso::
	https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setthreaddpiawarenesscontext
"""
SetThreadDpiAwarenessContext.restype = winBindings.user32.DPI_AWARENESS_CONTEXT
SetThreadDpiAwarenessContext.argtypes = (
	winBindings.user32.DPI_AWARENESS_CONTEXT,  # dpiContext: The new DPI_AWARENESS_CONTEXT for the current thread
)

GetWindowDpiAwarenessContext = WINFUNCTYPE(None)(("GetWindowDpiAwarenessContext", winBindings.user32.dll))
"""
Returns the DPI_AWARENESS_CONTEXT associated with a window.

.. seealso::
	https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getwindowdpiawarenesscontext
"""
GetWindowDpiAwarenessContext.restype = winBindings.user32.DPI_AWARENESS_CONTEXT
GetWindowDpiAwarenessContext.argtypes = (
	HWND,  # hwnd: The window to query
)

GetMenu = WINFUNCTYPE(None)(("GetMenu", winBindings.user32.dll))
"""
Retrieves a handle to the menu assigned to the specified window.

.. seealso::
	https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getmenu
"""
GetMenu.restype = HMENU
GetMenu.argtypes = (
	HWND,  # hWnd: Handle to the window whose menu handle is to be retrieved
)

GetMenuItemCount = WINFUNCTYPE(None)(("GetMenuItemCount", winBindings.user32.dll))
"""
Determines the number of items in the specified menu.

.. seealso::
	https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getmenuitemcount
"""
GetMenuItemCount.restype = c_int
GetMenuItemCount.argtypes = (
	HMENU,  # hMenu: Handle to the menu to be examined
)

GetMenuItemRect = WINFUNCTYPE(None)(("GetMenuItemRect", winBindings.user32.dll))
"""
Retrieves the bounding rectangle of the specified menu item.

.. seealso::
	https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getmenuitemrect
"""
GetMenuItemRect.restype = BOOL
GetMenuItemRect.argtypes = (
	HWND,  # hWnd: Handle to the window containing the menu
	HMENU,  # hMenu: Handle to the menu
	UINT,  # uItem: Zero-based position of the menu item
	LPRECT,  # lprcItem: RECT that receives the bounding rectangle in screen coordinates
)


# NVDA Core source/locationHelper.py

def _remapRectByAnchors(rect: RectLTRB, oldAnchor: RectLTRB, newAnchor: RectLTRB) -> RectLTRB:
	"""Map a rectangle from the coordinate space of one anchor rectangle into another.

	Both anchors describe the same physical object in two coordinate spaces,
	for example a window rectangle in its DPI virtualized and its physical space.
	Every edge of the given rectangle is scaled by the size ratio of the anchors
	and offset by the anchor origins,
	rounding half up so results stay stable regardless of coordinate sign.

	:param rect: The rectangle to map, in the coordinate space of ``oldAnchor``.
	:param oldAnchor: The anchor rectangle in the source coordinate space.
	:param newAnchor: The same anchor rectangle in the target coordinate space.
	:return: The mapped rectangle in the coordinate space of ``newAnchor``.
	:raise ValueError: If ``oldAnchor`` has a zero width or height.
	"""
	if oldAnchor.width <= 0 or oldAnchor.height <= 0:
		raise ValueError(f"oldAnchor {oldAnchor} has no area")
	scaleX = newAnchor.width / oldAnchor.width
	scaleY = newAnchor.height / oldAnchor.height

	def mapX(x: int) -> int:
		return math.floor(newAnchor.left + (x - oldAnchor.left) * scaleX + 0.5)

	def mapY(y: int) -> int:
		return math.floor(newAnchor.top + (y - oldAnchor.top) * scaleY + 0.5)

	return RectLTRB(mapX(rect.left), mapY(rect.top), mapX(rect.right), mapY(rect.bottom))


# NVDA Core source/windowUtils.py
DPI_AWARENESS_CONTEXT_UNAWARE = -1
"""The predefined DPI_AWARENESS_CONTEXT handle value for DPI unaware behavior."""


@contextlib.contextmanager
def _threadDpiAwarenessContext(dpiContext: int) -> Iterator[None]:
	"""Temporarily switch the current thread's DPI awareness context.

	:param dpiContext: The DPI_AWARENESS_CONTEXT handle value to apply.
	:raise OSError: If the context cannot be applied.
	"""
	previousContext = SetThreadDpiAwarenessContext(dpiContext)
	if not previousContext:
		raise OSError(f"Could not set the thread DPI awareness context {dpiContext}")
	try:
		yield
	finally:
		SetThreadDpiAwarenessContext(previousContext)


@contextlib.contextmanager
def threadDpiAwarenessContextOfWindow(window: int) -> Iterator[None]:
	"""Temporarily switch the current thread's DPI awareness context to that of the given window.

	Coordinate queries made inside this context return values
	as the given window sees them,
	which for a DPI virtualized window is its virtualized coordinate space.

	:param window: The window handle.
	:raise OSError: If the window's DPI awareness context cannot be applied,
		for example because the window handle is no longer valid.
	"""
	with _threadDpiAwarenessContext(GetWindowDpiAwarenessContext(window)):
		yield


def _fetchWindowRect(window: int) -> "locationHelper.RectLTRB":
	"""Fetch a window's bounding rectangle in the current thread's DPI awareness context.

	:param window: The window handle.
	:return: The window rectangle.
	:raise OSError: If the rectangle cannot be fetched.
	"""
	import locationHelper

	rect = ctypes.wintypes.RECT()
	if not winBindings.user32.GetWindowRect(window, ctypes.byref(rect)):
		raise ctypes.WinError()
	return locationHelper.RectLTRB.fromCompatibleType(rect)


def getPhysicalWindowRect(window: int) -> "locationHelper.RectLTRB":
	"""Fetch a window's bounding rectangle in physical screen coordinates.

	NVDA is per monitor DPI aware, so its own view of screen coordinates is physical.

	:param window: The window handle.
	:return: The window rectangle in physical screen coordinates.
	:raise OSError: If the rectangle cannot be fetched.
	"""
	return _fetchWindowRect(window)


def getWindowRectInWindowDpiContext(window: int) -> "locationHelper.RectLTRB":
	"""Fetch a window's bounding rectangle as seen from the window's own DPI awareness context.

	For a window whose coordinates are DPI virtualized by the system,
	this returns the virtualized rectangle,
	while a plain ``GetWindowRect`` call from NVDA returns the physical rectangle.
	Comparing and combining both rectangles allows converting between the two coordinate spaces
	without relying on ``PhysicalToLogicalPointForPerMonitorDPI``,
	which fails for points outside the physical window rectangle.

	:param window: The window handle.
	:return: The window rectangle in the coordinate space of the window's own DPI awareness context.
	:raise OSError: If the DPI awareness context cannot be applied or the rectangle cannot be fetched.
	"""
	with threadDpiAwarenessContextOfWindow(window):
		return _fetchWindowRect(window)


def getWindowRectInUnawareDpiContext(window: int) -> "locationHelper.RectLTRB":
	"""Fetch a window's bounding rectangle as seen by a DPI unaware process.

	This is the 96 DPI based view the system presents to DPI unaware callers.
	It applies to any window, including DPI aware ones,
	and anchors conversions from 96 DPI based coordinate spaces to physical coordinates.

	:param window: The window handle.
	:return: The window rectangle in the 96 DPI based coordinate space.
	:raise OSError: If the DPI awareness context cannot be applied or the rectangle cannot be fetched.
	"""
	with _threadDpiAwarenessContext(DPI_AWARENESS_CONTEXT_UNAWARE):
		return _fetchWindowRect(window)


# NVDA Core source/NVDAObjects/IAccessible/__init__.py
#: Window message asking a popup menu window for the handle of the menu it displays,
#: defined in winuser.h.
_MN_GETHMENU = 0x01E1
#: The system window class of popup menu windows.
_MENU_POPUP_WINDOW_CLASS = "#32768"
#: Menu handles of popup menu windows, cached to avoid repeated cross process messages.
_menuHandleCache: dict[int, int] = {}
#: Maximum number of cached menu handles. The cache is cleared wholesale beyond this,
#: it only needs to cover the handful of popup windows alive at any moment.
_MENU_HANDLE_CACHE_LIMIT = 8
#: How long to wait for a popup menu window to answer the menu handle query, in milliseconds.
_MENU_HANDLE_FETCH_TIMEOUT_MS = 500
#: Maximum per edge difference in pixels for an MSAA menu location to still count as
#: matching the raw Win32 menu item rectangle, allowing for independent rounding of edges.
_MENU_ITEM_RECT_TOLERANCE_PX = 1


def _rectsMatchWithinTolerance(first: RectLTRB, second: RectLTRB) -> bool:
	"""Whether two rectangles are equal within the per edge menu item tolerance."""
	return all(
		abs(firstEdge - secondEdge) <= _MENU_ITEM_RECT_TOLERANCE_PX
		for firstEdge, secondEdge in zip(first, second)
	)


def _getPopupMenuHandle(window: int, ignoreCache: bool = False) -> int | None:
	"""Fetch the menu handle of a #32768 popup menu window, with a small cache per window handle.

	:param window: The popup menu window.
	:param ignoreCache: Bypass and refresh the cached handle,
		used after a cached handle turned out to be stale.
	:return: The menu handle, or None if it cannot be fetched.
	"""
	if not ignoreCache:
		cached = _menuHandleCache.get(window)
		if cached:
			return cached
	menuHandleResult = ctypes.c_size_t()
	if not winBindings.user32.SendMessageTimeout(
		window,
		_MN_GETHMENU,
		0,
		0,
		winUser.SMTO_ABORTIFHUNG,
		_MENU_HANDLE_FETCH_TIMEOUT_MS,
		ctypes.byref(menuHandleResult),
	):
		return None
	menuHandle = menuHandleResult.value
	if menuHandle:
		if len(_menuHandleCache) >= _MENU_HANDLE_CACHE_LIMIT:
			_menuHandleCache.clear()
		_menuHandleCache[window] = menuHandle
	return menuHandle


def _getMenuItemRectsInWindowDpiContext(
	window: int,
	isPopupWindow: bool,
	itemIndex: int | None = None,
) -> list[RectLTRB] | None:
	"""Fetch Win32 menu item rectangles as seen from the menu window's own DPI awareness context.

	:param window: The #32768 window for a popup menu, otherwise the window owning the menu bar.
	:param isPopupWindow: Whether ``window`` is a #32768 popup menu window.
	:param itemIndex: The zero based position of the single item to fetch,
		or None to fetch every item of the menu.
	:return: The item rectangles in menu order, or None if they cannot be fetched.
	"""

	def fetchRects(menuHandle: int) -> list[RectLTRB] | None:
		if itemIndex is None:
			itemCount = GetMenuItemCount(menuHandle)
			if itemCount < 0:
				return None
			itemIndexes = range(itemCount)
		else:
			# GetMenuItemRect fails for an out of range index, so the index needs no range check.
			itemIndexes = (itemIndex,)
		rects = []
		try:
			with threadDpiAwarenessContextOfWindow(window):
				for index in itemIndexes:
					rect = ctypes.wintypes.RECT()
					if not GetMenuItemRect(window, menuHandle, index, ctypes.byref(rect)):
						return None
					rects.append(RectLTRB.fromCompatibleType(rect))
		except OSError:
			log.debugWarning(f"Could not apply the DPI awareness context of window {window}")
			return None
		return rects

	if isPopupWindow:
		menuHandle = _getPopupMenuHandle(window)
	else:
		menuHandle = GetMenu(window)
	if not menuHandle:
		log.debugWarning(f"No menu handle for window {window}, isPopupWindow={isPopupWindow}")
		return None
	itemRects = fetchRects(menuHandle)
	if itemRects is None and isPopupWindow and itemIndex is None:
		# The cached menu handle may be stale because window handles get reused.
		# A single item fetch is not retried here, because an out of range index fails
		# the same way. The caller falls back to fetching every item, which does retry.
		menuHandle = _getPopupMenuHandle(window, ignoreCache=True)
		if menuHandle:
			itemRects = fetchRects(menuHandle)
	if itemRects is None:
		log.debugWarning(
			f"Could not fetch the menu item rectangles for window {window}, itemIndex={itemIndex}",
		)
	return itemRects


def _physicalLocationFromMenuLocation(
	window: int,
	childID: int,
	isPopupWindow: bool,
	location: RectLTWH,
) -> RectLTWH:
	"""Convert an MSAA menu location to physical screen coordinates when needed.

	The OLEACC menu proxy reports menu locations
	in the 96 DPI based coordinate space of the menu's window
	when NVDA and the application differ in bitness,
	and in physical screen coordinates when they match.
	The window's own DPI awareness plays no role.
	The rest of NVDA expects physical screen coordinates everywhere (#19225).
	Such a location is detected by comparing it against the raw Win32 menu item rectangle,
	expressed both in physical coordinates and in the 96 DPI based space.
	A location matching the physical rectangle is already correct and passes through unchanged.
	A location matching the 96 DPI based rectangle is mapped to physical coordinates,
	using the window rectangle in both coordinate spaces as anchors.
	The mapping is done by hand instead of via ``LogicalToPhysicalPointForPerMonitorDPI``
	because that function rejects points outside the physical window rectangle,
	which the involved points regularly are.

	:param window: The #32768 window for a popup menu, otherwise the window owning the menu bar.
	:param childID: The MSAA child ID of the menu item, 1 based.
	:param isPopupWindow: Whether ``window`` is a #32768 popup menu window.
	:param location: The location reported by MSAA for the menu item.
	:return: The location in physical screen coordinates,
		or the unchanged input location when no conversion is needed or possible.
	"""
	try:
		physRect = getPhysicalWindowRect(window)
		unawareRect = getWindowRectInUnawareDpiContext(window)
	except OSError:
		log.debugWarning(f"Could not fetch the window rectangles for window {window}")
		return location
	if unawareRect == physRect:
		# Both coordinate spaces are identical, for example at 100 percent display scaling.
		return location
	if unawareRect.width <= 0 or unawareRect.height <= 0:
		return location
	try:
		winContextRect = getWindowRectInWindowDpiContext(window)
	except OSError:
		log.debugWarning(f"Could not fetch the window DPI context rectangle for window {window}")
		return location
	if winContextRect.width <= 0 or winContextRect.height <= 0:
		return location
	candidateRects = None
	if childID >= 1:
		# The child ID of an OLEACC proxy menu item is its 1 based menu position,
		# so a single rectangle is enough.
		candidateRects = _getMenuItemRectsInWindowDpiContext(window, isPopupWindow, itemIndex=childID - 1)
	if not candidateRects:
		# Menu items exposed by the application itself carry child ID 0, and an application
		# may number them in a way unrelated to the menu position, so every item of the
		# menu is a match candidate.
		candidateRects = _getMenuItemRectsInWindowDpiContext(window, isPopupWindow)
	if not candidateRects:
		return location
	try:
		locationLTRB = location.toLTRB()
	except ValueError:
		# MSAA locations are not validated, so a negative width or height is possible.
		log.debugWarning(f"MSAA reported the invalid menu location {location} for window {window}")
		return location
	# The raw item rectangles are in the window's own coordinate space. Express them in
	# both spaces the MSAA location could be in.
	for itemRect in candidateRects:
		itemRectPhysical = _remapRectByAnchors(itemRect, winContextRect, physRect)
		if _rectsMatchWithinTolerance(locationLTRB, itemRectPhysical):
			# The location already is physical, nothing to do.
			return location
	for itemRect in candidateRects:
		itemRectUnaware = _remapRectByAnchors(itemRect, winContextRect, unawareRect)
		if _rectsMatchWithinTolerance(locationLTRB, itemRectUnaware):
			return _remapRectByAnchors(locationLTRB, unawareRect, physRect).toLTWH()
	log.debugWarning(
		f"MSAA menu location {locationLTRB} matches no menu item rectangle of window {window} "
		"in either coordinate space, leaving it untouched",
	)
	return location


class SPLWorkaroundMenuItem(MenuItem):
	def _get_location(self) -> RectLTWH | None:
		location = super()._get_location()
		if not location or not self.windowHandle:
			return location
		return _physicalLocationFromMenuLocation(
			self.windowHandle,
			self.IAccessibleChildID,
			self.windowClassName == _MENU_POPUP_WINDOW_CLASS,
			location,
		)
