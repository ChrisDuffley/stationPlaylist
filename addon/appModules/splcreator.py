# StationPlaylist Creator
# An app module and global plugin package for NVDA
# Copyright 2016-2026 Joseph Lee, released under GPL.

# Basic support for StationPlaylist Creator.

from typing import Any
import appModuleHandler
import addonHandler
import scriptHandler
import globalVars
import ui
import api
import controlTypes
import wx
import windowUtils
import winUser
from NVDAObjects import NVDAObject
from NVDAObjects.IAccessible import sysListView32, getNVDAObjectFromEvent
from NVDAObjects.behaviors import Dialog
from .splcommon import splconfig, splconfui, splbase, splcarts
from .skipTranslation import translate

addonHandler.initTranslation()


# Return a tuple of column headers.
# This is just a thinly disguised indexOf function from Studio's track item class.
def indexOf(creatorVersion: str) -> tuple[str, ...]:
	if creatorVersion < "6.10":
		return (
			"Artist",
			"Title",
			"Position",
			"Cue",
			"Intro",
			"Outro",
			"Segue",
			"Duration",
			"Last Scheduled",
			"7 Days",
			"Restrictions",
			"Year",
			"Album",
			"Genre",
			"Mood",
			"Energy",
			"Tempo",
			"BPM",
			"Gender",
			"Rating",
			"File Created",
			"Filename",
			"Client",
			"Other",
			"Intro Link",
			"Outro Link",
			"Language",
		)
	else:
		return (
			"Artist",
			"Title",
			"Position",
			"Cue",
			"Intro",
			"Outro",
			"Segue",
			"Duration",
			"Last Scheduled",
			"7 Days",
			"Restrictions",
			"Year",
			"Album",
			"Genre",
			"Mood",
			"Energy",
			"Tempo",
			"BPM",
			"Gender",
			"Rating",
			"File Created",
			"Filename",
			"Client",
			"Other",
			"Intro Link",
			"Outro Link",
			"Region",
		)

# Playlist editor version.
def indexOfPlaylistEditor(editorVersion: str) -> tuple[str, ...]:
	if editorVersion < "6.10":
		return (
			"Artist",
			"Title",
			"Duration",
			"Intro",
			"Outro",
			"Category",
			"Year",
			"Album",
			"Genre",
			"Mood",
			"Energy",
			"Tempo",
			"Gender",
			"Rating",
			"Filename",
			"Other",
		)
	else:
		return (
			"    Time",
			"Artist",
			"Title",
			"Duration",
			"Intro",
			"Outro",
			"Category",
			"Year",
			"Album",
			"Genre",
			"Mood",
			"Energy",
			"Tempo",
			"Gender",
			"Rating",
			"Filename",
			"Other",
		)


class SPLCreatorItem(splbase.SPLTrackItem):
	"""An entry in SPL Creator (mostly tracks)."""

	def indexOf(self, columnHeader: str) -> int | None:
		try:
			return indexOf(self.appModule.productVersion).index(columnHeader)
		except ValueError:
			return None

	@property
	def exploreColumns(self) -> list[str]:
		return splconfig.SPLConfig["ExploreColumns"]["Creator"]


class SPLPlaylistEditorItem(splbase.SPLTrackItem):
	"""An entry in SPL Creator's Playlist Editor."""

	def indexOf(self, columnHeader: str) -> int | None:
		try:
			return indexOfPlaylistEditor(self.appModule.productVersion).index(columnHeader)
		except ValueError:
			return None

	@property
	def exploreColumns(self) -> list[str]:
		return splconfig.SPLConfig["ExploreColumns"]["PlaylistEditor"]


class AppModule(appModuleHandler.AppModule):
	scriptCategory = _("StationPlaylist")

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# Announce app version at startup unless minimal flag is set.
		try:
			if not globalVars.appArgs.minimal:
				# No translation.
				ui.message("{} {}".format(self.productName, self.productVersion))
		except Exception:
			pass
		# #64: load config database if not done already.
		splconfig.openConfig(self.appName)
		splconfui.initialize()

	def terminate(self):
		super().terminate()
		splconfig.closeConfig(self.appName)
		splconfui.terminate()
		# Clear Playlist Editor status cache,
		# otherwise it will generate errors when Creator restarts without restarting NVDA.
		self._playlistEditorStatusCache.clear()
		# Clear cached column headers used to announce sorted column status.
		self.trackColumnHeaders = None
		# Clear status bar objects cache.
		self._statusBarObjs.clear()

	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: list[NVDAObject]) -> None:
		# Detect unlabeled controls whose labels are next to them (written to the screen).
		# Return right after detecting these.
		if splbase.useScreenLabelForUnlabeledObject(
			obj, [
				"TTagForm.UnicodeClass",  # Track properties
				"TTrackInsertForm"  # Insert tracks
			]
		):
			clsList.insert(0, splbase.SPLUnlabeledControl)
			return
		# Tracks list uses a different window class name other than "TListView".
		# Resort to window style and other tricks if other lists with the class name below is found
		# yet are not tracks list.
		if obj.windowClassName == "TTntListView.UnicodeClass":
			if obj.role == controlTypes.Role.LISTITEM:
				clsList.insert(0, SPLCreatorItem if obj.windowStyle in (
					1443958857,  # Creator 6.0x
					1443958849,  # Creator 6.1x
					1446056001,  # Creator 6.20
				) else SPLPlaylistEditorItem)
			elif obj.role == controlTypes.Role.LIST:
				clsList.insert(0, sysListView32.List)
		elif obj.windowClassName in ("TDemoRegForm", "TAboutForm"):
			clsList.insert(0, Dialog)

	# Cache status bar objects to improve status bar retrieval performance.
	_statusBarObjs = {}

	def _get_statusBar(self):
		# Obtaining Creator status bar is slow.
		# Therefore, cache the status bar object (based on foreground window class name).
		if (fg := api.getForegroundObject()).windowClassName in self._statusBarObjs:
			return self._statusBarObjs[fg.windowClassName]
		try:
			statusBar = getNVDAObjectFromEvent(
				windowUtils.findDescendantWindow(fg.windowHandle, className="TTntStatusBar.UnicodeClass"),
				winUser.OBJID_CLIENT, 0
			)
		except LookupError:
			statusBar = None
		if statusBar:
			self._statusBarObjs[fg.windowClassName] = statusBar
			return statusBar
		# Force NVDA to locate bottommost control.
		raise NotImplementedError

	def event_NVDAObject_init(self, obj: NVDAObject):
		if (
			obj.windowClassName == "TTntStatusBar.UnicodeClass"
			and obj.role == controlTypes.Role.STATICTEXT and not obj.name
		):
			# Status bar labels are not found in Creator and playlist editor but is written to the screen.
			obj.name = obj.displayText

	@scriptHandler.script(
		description=_("Opens SPL Studio add-on configuration dialog."),
		gestures=["kb:alt+NVDA+0", "ts(SPL):2finger_flickLeft"],
	)
	def script_openConfigDialog(self, gesture):
		# Rather than calling the config dialog open event,
		# call the open dialog function directly to avoid indirection.
		wx.CallAfter(splconfui.openAddonSettingsPanel, None)

	# Handle native Creator commands.

	# Announce track sort status (column, ascending/descending).
	# Number row gestures come from cart keys list.
	columnSortKeys = splcarts.cartKeys[12:]
	# Cache column headers (because screen traversal in Creator is slow).
	trackColumnHeaders = None

	@scriptHandler.script(gestures=[f"kb:alt+{i}" for i in splcarts.cartKeys[12:]])
	def script_reportTrackColumnSort(self, gesture):
		gesture.send()
		# Limit this to Creator (Remote VT ap module derives from this module).
		if self.appName != "splcreator":
			return
		fg = api.getForegroundObject()
		if fg.windowClassName != "TMainForm":
			return
		# Make sure "Track List" tab is showing.
		if "Track List" not in fg.firstChild.name:
			return
		column = self.columnSortKeys.index(gesture.displayName.split("+")[-1])
		if not self.trackColumnHeaders:
			trackListPropertySheet = fg.getChild(-2).firstChild.simpleFirstChild
			trackList = trackListPropertySheet.simpleLastChild.previous
			self.trackColumnHeaders = trackList.children[-1]
		# Get the last child included in list children, not last child as the former is column headers.
		columnHeader = self.trackColumnHeaders.getChild(column).name
		# Up arrow (↑) = ascending, down arrow (↓) = descending
		match columnHeader[0]:
			case "↑":
				direction = translate("{column} (ascending)".format(column=columnHeader.strip("↑↓")))
			case "↓":
				direction = translate("{column} (descending)".format(column=columnHeader.strip("↑↓")))
			case _:
				direction = columnHeader
		ui.message(direction)

	# The following scripts are designed to work while using Playlist Editor.

	def isPlaylistEditor(self) -> bool:
		if api.getForegroundObject().windowClassName != "TEditMain":
			# Translators: announced in SPL Creator and Remote VT
			# when trying to perform playlist status commands while outside of playlist editor.
			ui.message(_("You are not in playlist editor"))
			return False
		return True

	# Just like Studio, status items are scattered around the screen in Playlist Editor,
	# and takes a really long time to fetch things.
	SPLEditorDateTime = 0
	SPLEditorDuration = 1
	SPLEditorStatusBar = 2
	_playlistEditorStatusCache: dict[int, Any] = {}

	@scriptHandler.script(gesture="kb:alt+NVDA+1", speakOnDemand=True)
	def script_playlistDateTime(self, gesture):
		if self.isPlaylistEditor():
			try:
				playlistHour = self._playlistEditorStatusCache[self.SPLEditorDateTime][0]
				playlistDay = self._playlistEditorStatusCache[self.SPLEditorDateTime][1]
			except KeyError:
				playlistDateTime = api.getForegroundObject().simpleLastChild.firstChild.next
				playlistHour = playlistDateTime.simpleNext
				playlistDay = playlistHour.simpleNext.simpleNext
				self._playlistEditorStatusCache[self.SPLEditorDateTime] = [playlistHour, playlistDay]
			ui.message(" ".join([playlistDay.value, playlistHour.value]))

	@scriptHandler.script(gesture="kb:alt+NVDA+2", speakOnDemand=True)
	def script_playlistDuration(self, gesture):
		if self.isPlaylistEditor():
			try:
				playlistDuration = self._playlistEditorStatusCache[self.SPLEditorDuration]
			except KeyError:
				playlistDuration = api.getForegroundObject().simpleLastChild.firstChild
				self._playlistEditorStatusCache[self.SPLEditorDuration] = playlistDuration
			ui.message(playlistDuration.name)

	@scriptHandler.script(gesture="kb:alt+NVDA+3", speakOnDemand=True)
	def script_playlistScheduled(self, gesture):
		if self.isPlaylistEditor():
			try:
				statusBar = self._playlistEditorStatusCache[self.SPLEditorStatusBar]
			except KeyError:
				statusBar = api.getForegroundObject().firstChild.firstChild
				self._playlistEditorStatusCache[self.SPLEditorStatusBar] = statusBar
			ui.message(statusBar.getChild(2).displayText)

	@scriptHandler.script(gesture="kb:alt+NVDA+4", speakOnDemand=True)
	def script_playlistRotation(self, gesture):
		if self.isPlaylistEditor():
			try:
				statusBar = self._playlistEditorStatusCache[self.SPLEditorStatusBar]
			except KeyError:
				statusBar = api.getForegroundObject().firstChild.firstChild
				self._playlistEditorStatusCache[self.SPLEditorStatusBar] = statusBar
			ui.message(statusBar.getChild(3).displayText)
