# SPL Studio Miscellaneous User Interfaces and internal services
# An app module and global plugin package for NVDA
# Copyright 2015-2021 Joseph Lee, released under GPL.
# Miscellaneous functions and user interfaces
# Split from config module in 2015.

# #155 (21.03): remove __future__ import when NVDA runs under Python 3.10.
from __future__ import annotations
from typing import Any, Optional
import weakref
import os
import threading
from _csv import reader  # For cart explorer.
import gui
import wx
import globalVars
import nvwave
import queueHandler
import speech
import ui
from logHandler import log
import addonHandler
from winUser import user32
from . import splbase
from . import splactions
from ..skipTranslation import translate
addonHandler.initTranslation()


# A custom combo box for cases where combo boxes are not choice controls.
class CustomComboBox(wx.ComboBox, wx.Choice):
	pass


# A common dialog for Track Finder
_findDialogOpened = False


# Track Finder error dialog.
# This will be refactored into something else.
def _finderError() -> None:
	global _findDialogOpened
	if _findDialogOpened:
		gui.messageBox(
			# Translators: Text of the dialog when another find dialog is open.
			_("Another find dialog is open."),
			translate("Error"), style=wx.OK | wx.ICON_ERROR
		)
	else:
		gui.messageBox(
			# Translators: Text of the dialog when a generic error has occured.
			_("An unexpected error has occured when trying to open find dialog."),
			translate("Error"), style=wx.OK | wx.ICON_ERROR
		)


class SPLFindDialog(wx.Dialog):

	@classmethod
	def _instance(cls):
		return None

	def __new__(cls, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _findDialogOpened:
			raise RuntimeError("An instance of find dialog is opened")
		instance = SPLFindDialog._instance()
		if instance is None:
			return super(SPLFindDialog, cls).__new__(cls, *args, **kwargs)
		return instance

	def __init__(self, parent, obj, text, title, columnSearch=False):
		if SPLFindDialog._instance() is not None:
			return
		# Use a weakref so the instance can die.
		SPLFindDialog._instance = weakref.ref(self)

		super().__init__(parent, wx.ID_ANY, title)
		self.obj = obj
		self.columnSearch = columnSearch
		if not columnSearch:
			# Translators: the label for find prompt in track finder dialog.
			findPrompt = _("Enter or select the name or the artist of the track you wish to &search")
		else:
			# Translators: the label for find prompt in column search dialog.
			findPrompt = _("Enter or select text to be &searched in a column")

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		findSizerHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)

		findHistory = obj.appModule.findText if obj.appModule.findText is not None else []
		# #68: use a custom combo box if this is wxPython 4.
		if isinstance(wx.ComboBox, wx.Choice):
			self.findEntry = findSizerHelper.addLabeledControl(findPrompt, wx.ComboBox, choices=findHistory)
		else:
			self.findEntry = findSizerHelper.addLabeledControl(findPrompt, CustomComboBox, choices=findHistory)
		self.findEntry.Value = text

		if columnSearch:
			from . import splconfig
			self.columnHeaders = findSizerHelper.addLabeledControl(
				# Translators: The label in track finder to search columns.
				_("C&olumn to search:"), wx.Choice,
				choices=splconfig._SPLDefaults["ColumnAnnouncement"]["ColumnOrder"]
			)
			self.columnHeaders.SetSelection(0)

		# #152 (21.01): add a separator if column search is active, otherwise only find prompt is displayed.
		findSizerHelper.addDialogDismissButtons(wx.OK | wx.CANCEL, separated=columnSearch)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(findSizerHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.CenterOnScreen()
		self.findEntry.SetFocus()

	def onOk(self, evt):
		global _findDialogOpened
		text = self.findEntry.Value
		# Studio, are you alive?
		if user32.FindWindowW("SPLStudio", None) and text:
			appMod = self.obj.appModule
			# 21.03/20.09.6-LTS: search columns should not be None - list of integers expected.
			column = [self.columnHeaders.Selection + 1] if self.columnSearch else []
			startObj = self.obj
			if (
				appMod.findText is None
				or (len(appMod.findText) and (text == appMod.findText[0] or text in appMod.findText))
			):
				startObj = startObj.next
				if appMod.findText is None:
					appMod.findText = [text]
				# #27: Move the new text to the top of the search history.
				if text in appMod.findText and text != appMod.findText[0]:
					oldTextIndex = appMod.findText.index(text)
					appMod.findText[0], appMod.findText[oldTextIndex] = appMod.findText[oldTextIndex], appMod.findText[0]
			# If this is called right away, we land on an invisible window.
			wx.CallLater(100, appMod.trackFinder, text, obj=startObj, column=column)
		self.Destroy()
		_findDialogOpened = False

	def onCancel(self, evt):
		self.Destroy()
		global _findDialogOpened
		_findDialogOpened = False

	def onAppTerminate(self):
		# Call cancel function when the app terminates so the dialog can be closed.
		self.onCancel(None)


# Time range finder: a variation on track finder.
# Similar to track finder, locate tracks with duration that falls between min and max.
class SPLTimeRangeDialog(wx.Dialog):

	@classmethod
	def _instance(cls):
		return None

	def __new__(cls, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _findDialogOpened:
			raise RuntimeError("An instance of find dialog is opened")
		instance = SPLTimeRangeDialog._instance()
		if instance is None:
			return super(SPLTimeRangeDialog, cls).__new__(cls, *args, **kwargs)
		return instance

	def __init__(self, parent, obj):
		if SPLTimeRangeDialog._instance() is not None:
			return
		# Use a weakref so the instance can die.
		SPLTimeRangeDialog._instance = weakref.ref(self)

		# Translators: The title of a dialog to find tracks with duration within a specified range.
		super().__init__(parent, wx.ID_ANY, _("Time range finder"))
		self.obj = obj

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		timeRangeHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)

		minRangeGroup = gui.guiHelper.BoxSizerHelper(
			# Translators: the label for a group to specify minimum track duration in time range finder dialog.
			self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=_("Minimum duration")), wx.HORIZONTAL)
		)
		timeRangeHelper.addItem(minRangeGroup)
		self.minMinEntry = minRangeGroup.addLabeledControl(
			# Translators: the minute label in time range finder dialog.
			_("Minute"), gui.nvdaControls.SelectOnFocusSpinCtrl,
			min=0, max=59, initial=3
		)
		self.minSecEntry = minRangeGroup.addLabeledControl(
			# Translators: the second label in time range finder dialog.
			_("Second"), gui.nvdaControls.SelectOnFocusSpinCtrl,
			min=0, max=59, initial=0
		)

		maxRangeGroup = gui.guiHelper.BoxSizerHelper(
			# Translators: the label for a group to specify maximum track duration in time range finder dialog.
			self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=_("Maximum duration")), wx.HORIZONTAL)
		)
		timeRangeHelper.addItem(maxRangeGroup)
		self.maxMinEntry = maxRangeGroup.addLabeledControl(
			_("Minute"), gui.nvdaControls.SelectOnFocusSpinCtrl,
			min=0, max=59, initial=5
		)
		self.maxSecEntry = maxRangeGroup.addLabeledControl(
			_("Second"), gui.nvdaControls.SelectOnFocusSpinCtrl,
			min=0, max=59, initial=0
		)

		# #68: wx.BoxSizer.AddSizer no longer exists in wxPython 4.
		timeRangeHelper.addDialogDismissButtons(wx.OK | wx.CANCEL, separated=True)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(timeRangeHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.CenterOnScreen()
		self.minMinEntry.SetFocus()

	def onOk(self, evt):
		minDuration = ((self.minMinEntry.GetValue() * 60) + self.minSecEntry.GetValue()) * 1000
		maxDuration = ((self.maxMinEntry.GetValue() * 60) + self.maxSecEntry.GetValue()) * 1000
		# What if minimum is greater than maximum (subtle oversight)?
		if minDuration >= maxDuration:
			gui.messageBox(
				# Translators: Message to report wrong value for duration fields.
				_("Minimum duration is greater than the maximum duration."),
				translate("Error"), wx.OK | wx.ICON_ERROR, self
			)
			self.minMinEntry.SetFocus()
			return
		self.Destroy()
		global _findDialogOpened
		if user32.FindWindowW("SPLStudio", None):
			obj = self.obj.next
			# Manually locate tracks here.
			while obj is not None:
				filename = splbase.studioAPI(obj.IAccessibleChildID - 1, 211)
				if minDuration <= splbase.studioAPI(filename, 30) <= maxDuration:
					break
				obj = obj.next
			if obj is not None:
				# Set focus only once, as do action method on tracks will set focus twice.
				obj.setFocus()
				# 16.11: Select the desired track manually.
				# #45 (18.02): call select track function in splbase module.
				splbase.selectTrack(obj.IAccessibleChildID - 1)
			else:
				wx.CallAfter(
					# Translators: Presented when a track with a duration
					# between minimum and maximum duration is not found.
					gui.messageBox, _("No track with duration between minimum and maximum duration."),
					# Translators: Standard error title for find error (copy this from main nvda.po).
					_("Time range find error"), wx.OK | wx.ICON_ERROR
				)
		_findDialogOpened = False

	def onCancel(self, evt):
		self.Destroy()
		global _findDialogOpened
		_findDialogOpened = False

	def onAppTerminate(self):
		# Call cancel function when the app terminates so the dialog can be closed.
		self.onCancel(None)


# Cart Explorer helper.

# Manual definitions of cart keys.
cartKeys = (
	# Function key carts (Studio all editions)
	"f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12",
	# Number row (all editions except Standard)
	"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="
)


def _populateCarts(
		carts: dict[str, Any], cartlst: list[str],
		modifier: str, standardEdition: bool = False, refresh: bool = False
) -> None:
	# The real cart string parser, a helper for cart explorer for building cart entries.
	# 5.2: Discard number row if SPL Standard is in use.
	if standardEdition:
		cartlst = cartlst[:12]
	# #148 (20.10): obtain cart entry position through enumerate function.
	# Pos 1 through 12 = function carts, 13 through 24 = number row carts.
	# #147 (20.10): note that 1 is subtracted from cart position as a tuple will be used to lookup cart keys.
	for pos, entry in enumerate(cartlst):
		# An unassigned cart is stored with three consecutive commas, so skip it.
		# 17.04: If refresh is on, the cart we're dealing with
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
_cartEditTimestamps: list[float] = []


# Initialize Cart Explorer i.e. fetch carts.
# Cart files list is for future use when custom cart names are used.
# if told to refresh, timestamps will be checked and updated banks will be reassigned.
# Carts dictionary is used if and only if refresh is on, as it'll modify live carts.
def cartExplorerInit(
		StudioTitle: str, cartFiles: Optional[list[str]] = None,
		refresh: bool = False, carts: Optional[dict[str, Any]] = None
) -> dict[str, Any]:
	global _cartEditTimestamps
	log.debug("SPL: refreshing Cart Explorer" if refresh else "preparing cart Explorer")
	# Use cart files in SPL's data folder to build carts dictionary.
	# use a combination of SPL user name and static cart location to locate cart bank files.
	# Once the cart banks are located, use the routines in the populate method above to assign carts.
	# Since sstandard edition does not support number row carts, skip them if told to do so.
	if carts is None:
		carts = {"standardLicense": StudioTitle.startswith("StationPlaylist Studio Standard")}
	# Obtain the "real" path for SPL via environment variables and open the cart data folder.
	# Provided that Studio was installed using default path.
	cartsDataPath = os.path.join(os.environ["PROGRAMFILES"], "StationPlaylist", "Data")
	if cartFiles is None:
		# See if multiple users are using SPl Studio.
		userNameIndex = StudioTitle.find("-")
		# Read *.cart files and process the cart entries within
		# (be careful when these cart file names change between SPL releases).
		cartFiles = ["main carts.cart", "shift carts.cart", "ctrl carts.cart", "alt carts.cart"]
		if userNameIndex >= 0:
			cartFiles = [StudioTitle[userNameIndex + 2:] + " " + cartFile for cartFile in cartFiles]
	faultyCarts = False
	if not refresh:
		_cartEditTimestamps = []
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
		if refresh and _cartEditTimestamps[cartFiles.index(f)] == cartTimestamp:
			log.debug("SPL: no changes to cart bank, skipping")
			continue
		_cartEditTimestamps.append(cartTimestamp)
		with open(cartFile) as cartInfo:
			cl = [row for row in reader(cartInfo)]
		# 17.04 (optimization): let empty string represent main cart bank to
		# avoid this being partially consulted up to 24 times.
		# The below method will just check for string length, which is faster than looking for specific substring.
		# See the comment for _populate carts method for details.
		_populateCarts(
			carts, cl[1], mod if mod != "main" else "",
			standardEdition=carts["standardLicense"], refresh=refresh
		)
		if not refresh:
			log.debug(f"SPL: carts processed so far: {(len(carts)-1)}")
	carts["faultyCarts"] = faultyCarts
	log.debug(f"SPL: total carts processed: {(len(carts)-2)}")
	return carts


# Refresh carts upon request.
# calls cart explorer init with special (internal) flags.
def cartExplorerRefresh(studioTitle: str, currentCarts: dict[str, Any]) -> dict[str, Any]:
	return cartExplorerInit(studioTitle, refresh=True, carts=currentCarts)


# Metadata and encoders management, including connection, announcement and so on.


# Gather streaming flags into a list.
# 18.04: raise runtime error if list is nothing
# (thankfully the splbase's StudioAPI will return None if Studio handle is not found).
def metadataList() -> list[Optional[int]]:
	metadata = [splbase.studioAPI(pos, 36) for pos in range(5)]
	# 21.03/20.09.6-LTS: make sure None is not included in metadata list,
	# otherwise it results in no metadata data for streams.
	# This could happen if Studio dies while retrieving metadata list with some items returning None.
	if None in metadata:
		raise RuntimeError("Studio handle not found, no metadata list to return")
	return metadata


# Metadata server connector, to be utilized from many modules.
# Servers refer to a list of connection flags to pass to Studio API,
# and if not present, will be pulled from add-on settings.
def metadataConnector(servers: Optional[list[bool]] = None) -> None:
	if servers is None:
		from . import splconfig
		servers = splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"]
	for url in range(5):
		dataLo = 0x00010000 if servers[url] else 0xffff0000
		splbase.studioAPI(dataLo | url, 36)


# Metadata status formatter.
# 18.04: say something if Studio handle is not found.
def metadataStatus() -> str:
	try:
		streams = metadataList()
	except RuntimeError:
		# Translators: presented when metadata streaming status cannot be obtained.
		return _("Cannot obtain metadata streaming status information")
	# DSP is treated specially.
	# 20.11: remove it from the streams list early so only URL's can be checked later.
	dsp = streams.pop(0)
	# Unless all URL's are streaming, use of any function is faster as it returns True
	# whenever anything inside streams list is set to 1.
	if not any(streams):
		if not dsp:
			# Translators: Status message for metadata streaming.
			return _("No metadata streaming URL's defined")
		else:
			# Translators: Status message for metadata streaming.
			return _("Metadata streaming configured for DSP encoder")
	# For others, a simple list.append will do.
	# 17.04: Use a conditional list comprehension.
	# 18.02: comprehend based on streams list from above.
	# 20.11: add positions based on enumerate function call.
	streamCount = [str(pos) for pos, stream in enumerate(streams, start=1) if stream]
	if len(streamCount) == 1:
		if dsp:
			# Translators: Status message for metadata streaming.
			return _("Metadata streaming configured for DSP encoder and URL {URL}").format(URL=streamCount[0])
		else:
			# Translators: Status message for metadata streaming.
			return _("Metadata streaming configured for URL {URL}").format(URL=streamCount[0])
	else:
		# Prepare URL list string early.
		urls = ", ".join(streamCount)
		if dsp:
			# Translators: Status message for metadata streaming.
			return _("Metadata streaming configured for DSP encoder and URL's {URL}").format(URL=urls)
		else:
			# Translators: Status message for metadata streaming.
			return _("Metadata streaming configured for URL's {URL}").format(URL=urls)


# Handle a case where instant profile ssitch occurs twice within the switch time-out.
_earlyMetadataAnnouncer: Optional[threading.Timer] = None


# Internal metadata status announcer.
# The idea is to pause for a while and announce the status message and playing the accompanying wave file.
# This is necessary in order to allow extension points to work correctly
# and to not hold up other registered action handlers.
# A special startup flag will be used so other text sequences will not be cut off.
def _metadataAnnouncerInternal(status: str, startup: bool = False) -> None:
	if not startup:
		speech.cancelSpeech()
	queueHandler.queueFunction(queueHandler.eventQueue, ui.message, status)
	nvwave.playWaveFile(os.path.join(os.path.dirname(__file__), "SPL_Metadata.wav"))
	# #51 (18.03/15.14-LTS): close link to metadata announcer thread when finished.
	global _earlyMetadataAnnouncer
	_earlyMetadataAnnouncer = None


def _earlyMetadataAnnouncerInternal(status: str, startup: bool = False) -> None:
	global _earlyMetadataAnnouncer
	if _earlyMetadataAnnouncer is not None:
		_earlyMetadataAnnouncer.cancel()
		_earlyMetadataAnnouncer = None
	_earlyMetadataAnnouncer = threading.Timer(
		2, _metadataAnnouncerInternal, args=[status], kwargs={"startup": startup}
	)
	_earlyMetadataAnnouncer.start()


# Delay the action handler if Studio handle is not found.
_delayMetadataAction = False


# Connect and/or announce metadata status when broadcast profile switching occurs.
# The config dialog active flag is only invoked when being notified while add-on settings dialog is focused.
# Settings reset flag is used to prevent metadata server connection
# when settings are reloaded from disk or reset to defaults.
def metadata_actionProfileSwitched(configDialogActive: bool = False, settingsReset: bool = False) -> None:
	from . import splconfig
	# Only connect if add-on settings is active in order to avoid wasting thread running time.
	if configDialogActive:
		metadataConnector(servers=splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"])
		return
	global _delayMetadataAction
	# Ordinarily, errors would have been dealt with, but Action.notify will catch errors and log messages.
	# #40 (18.02): the only possible error is if Studio handle is invalid, which won't be the case,
	# otherwise no point handling this action.
	# #49 (18.03): no, don't announce this if the app module is told to announce metadata status at startup only.
	if splconfig.SPLConfig["General"]["MetadataReminder"] == "instant":
		# If told to remind and connect, metadata streaming will be enabled at this time.
		# 6.0: Call Studio API twice - once to set, once more to obtain the needed information.
		# 6.2/7.0: When Studio API is called, add the value into the stream count list also.
		# 17.11: call the connector.
		# 18.02: transfered to the action handler and greatly simplified.
		# 18.04: ask the handle finder to return to this place if Studio handle isn't ready.
		# This is typically the case when launching Studio
		# and profile switch occurs while demo registration screen is up.
		handle = user32.FindWindowW("SPLStudio", None)
		if not handle:
			_delayMetadataAction = True
			return
		if not settingsReset:
			metadataConnector()
		# #47 (18.02/15.13-LTS): call the internal announcer via wx.CallLater
		# in order to not hold up action handler queue.
		# #51 (18.03/15.14-LTS): wx.CallLater isn't enough - there must be ability to cancel it.
		_earlyMetadataAnnouncerInternal(metadataStatus())


# The only job of this action handler is to call profile switch handler above with special flags.
def metadata_actionSettingsReset(factoryDefaults: bool = False) -> None:
	metadata_actionProfileSwitched(settingsReset=True)


# Playlist transcripts processor
# Takes a snapshot of the active playlist (a 2-D array) and transforms it into various formats.
# To account for expansions, let a master function call different formatters based on output format.
SPLPlaylistTranscriptFormats = []


# Obtain column presentation order.
# Although this is useful in playlist transcripts,
# it can also be useful for column announcement inclusion and order.
def columnPresentationOrder() -> list[str]:
	from . import splconfig
	return [
		column for column in splconfig.SPLConfig["PlaylistTranscripts"]["ColumnOrder"]
		if column in splconfig.SPLConfig["PlaylistTranscripts"]["IncludedColumns"]]

# Various post-transcript actions.
# For each converter, after transcribing the playlist, additional actions will be performed.
# Actions can include viewing the transcript,
# copying to clipboard (text style format only), and saving to a file.


def displayPlaylistTranscripts(transcript: list[str], HTMLDecoration: bool = False) -> None:
	ui.browseableMessage("\n".join(transcript), title=_("Playlist Transcripts"), isHtml=HTMLDecoration)


def copyPlaylistTranscriptsToClipboard(playlistTranscripts: list[str]) -> None:
	# 22.03 (security): do not copy transcripts to clipboard in secure mode.
	if globalVars.appArgs.secure:
		return
	# Only text style transcript such as pure text and Markdown supports copying contents to clipboard.
	import api
	api.copyToClip("\r\n".join(playlistTranscripts))
	# Translators: presented when playlist transcript data was copied to the clipboard.
	ui.message(_("Playlist data copied to clipboard"))


def savePlaylistTranscriptsToFile(
		playlistTranscripts: list[str], extension: str, location: Optional[str] = None
) -> None:
	# 22.03 (security): do not save transcripts to files in secure mode.
	if globalVars.appArgs.secure:
		return
	# By default playlist transcripts will be saved to a subfolder in user's Documents folder
	# named "nvdasplPlaylistTranscripts".
	# Each transcript file will be named yyyymmdd-hhmmss-splPlaylistTranscript.ext.
	transcriptFileLocation = os.path.join(os.environ["userprofile"], "Documents", "nvdasplPlaylistTranscripts")
	if not os.path.exists(transcriptFileLocation):
		os.mkdir(transcriptFileLocation)
	import datetime
	transcriptTimestamp = datetime.datetime.now()
	transcriptFilename = "{0}{1:02d}{2:02d}-{3:02d}{4:02d}{5:02d}-splPlaylistTranscript.{6}".format(
		transcriptTimestamp.year, transcriptTimestamp.month, transcriptTimestamp.day,
		transcriptTimestamp.hour, transcriptTimestamp.minute, transcriptTimestamp.second, extension
	)
	transcriptPath = os.path.join(transcriptFileLocation, transcriptFilename)
	with open(transcriptPath, "w") as transcript:
		transcript.writelines(playlistTranscripts)
	ui.message("Playlist transcripts saved at {location}".format(location=transcriptPath))


# Several converters rely on assistants for their work.
# For text file 1 and HTML list 1, it expects playlist data in the format presented by MSAA.
# Header will not be included if additional decorations will be done (mostly for HTML and others).
# Prefix and suffix denote text to be added around entries (useful for various additional decoration rules).
def playlist2msaa(
		start: Any, end: Any, additionalDecorations: bool = False, prefix: str = "", suffix: str = ""
) -> list[str]:
	playlistTranscripts = []
	# Just pure text, ready for the clipboard or writing to a txt file.
	if not additionalDecorations:
		playlistTranscripts = ["Playlist Transcripts"]
		# Add a blank line for presentational purposes.
		playlistTranscripts.append("\r\n")
	obj = start
	columnHeaders = columnPresentationOrder()
	columnPos = [obj.indexOf(column) for column in columnHeaders]
	while obj not in (None, end):
		# Exclude status column, and no need to make this readable.
		columnContents = obj._getColumnContents(columns=columnPos)
		# Filter empty columns.
		filteredContent = []
		# #148 (20.10): work directly with column content and position rather than going through column pos index.
		for column, content in enumerate(columnContents):
			if content is not None:
				filteredContent.append("{}: {}".format(columnHeaders[column], content))
		playlistTranscripts.append("{0}{1}{2}".format(prefix, "; ".join(filteredContent), suffix))
		obj = obj.next
	return playlistTranscripts


def playlist2txt(start: Any, end: Any, transcriptAction: int) -> None:
	playlistTranscripts = playlist2msaa(start, end)
	if transcriptAction == 0:
		displayPlaylistTranscripts(playlistTranscripts)
	elif transcriptAction == 1:
		copyPlaylistTranscriptsToClipboard(playlistTranscripts)
	elif transcriptAction == 2:
		savePlaylistTranscriptsToFile(playlistTranscripts, "txt")


SPLPlaylistTranscriptFormats.append(("txt", playlist2txt, "plain text with one line per entry"))


def playlist2htmlTable(start: Any, end: Any, transcriptAction: int) -> None:
	if transcriptAction == 1:
		playlistTranscripts = ["<html><head><title>Playlist Transcripts</title></head>"]
		playlistTranscripts.append("<body>")
		playlistTranscripts.append("<h1>Playlist Transcripts</h1>")
	else:
		playlistTranscripts = ["<h1>Playlist Transcripts</h1>"]
	playlistTranscripts.append("<p>")
	columnHeaders = columnPresentationOrder()
	playlistTranscripts.append(
		"<table><tr><th>{trackHeaders}</tr>".format(
			trackHeaders="<th>".join(columnHeaders)
		)
	)
	obj = start
	columnPos = [obj.indexOf(column) for column in columnHeaders]
	while obj not in (None, end):
		columnContents = obj._getColumnContents(columns=columnPos, readable=True)
		playlistTranscripts.append("<tr><td>{trackContents}</tr>".format(trackContents="<td>".join(columnContents)))
		obj = obj.next
	playlistTranscripts.append("</table>")
	if transcriptAction == 0:
		displayPlaylistTranscripts(playlistTranscripts, HTMLDecoration=True)
	elif transcriptAction == 1:
		playlistTranscripts.append("</body></html>")
		savePlaylistTranscriptsToFile(playlistTranscripts, "htm")


SPLPlaylistTranscriptFormats.append(("htmltable", playlist2htmlTable, "Table in HTML format"))


def playlist2htmlList(start: Any, end: Any, transcriptAction: int) -> None:
	if transcriptAction == 1:
		playlistTranscripts = ["<html><head><title>Playlist Transcripts</title></head>"]
		playlistTranscripts.append("<body>")
		playlistTranscripts.append("<h1>Playlist Transcripts</h1>")
	else:
		playlistTranscripts = ["<h1>Playlist Transcripts</h1>"]
	playlistTranscripts.append("<p><ol>")
	playlistTranscripts += playlist2msaa(start, end, additionalDecorations=True, prefix="<li>")
	playlistTranscripts.append("</ol>")
	if transcriptAction == 0:
		displayPlaylistTranscripts(playlistTranscripts, HTMLDecoration=True)
	elif transcriptAction == 1:
		playlistTranscripts.append("</body></html>")
		savePlaylistTranscriptsToFile(playlistTranscripts, "htm")


SPLPlaylistTranscriptFormats.append(("htmllist", playlist2htmlList, "Data list in HTML format"))


def playlist2mdTable(start: Any, end: Any, transcriptAction: int) -> None:
	playlistTranscripts = []
	columnHeaders = columnPresentationOrder()
	playlistTranscripts.append("| {headers} |\n".format(headers=" | ".join(columnHeaders)))
	obj = start
	columnPos = [obj.indexOf(column) for column in columnHeaders]
	while obj not in (None, end):
		columnContents = obj._getColumnContents(columns=columnPos, readable=True)
		playlistTranscripts.append("| {trackContents} |\n".format(trackContents=" | ".join(columnContents)))
		obj = obj.next
	if transcriptAction == 0:
		displayPlaylistTranscripts(playlistTranscripts)
	elif transcriptAction == 1:
		copyPlaylistTranscriptsToClipboard(playlistTranscripts)
	elif transcriptAction == 2:
		savePlaylistTranscriptsToFile(playlistTranscripts, "md")


SPLPlaylistTranscriptFormats.append(("mdtable", playlist2mdTable, "Table in Markdown format"))


def playlist2csv(start: Any, end: Any, transcriptAction: int) -> None:
	playlistTranscripts = []
	columnHeaders = columnPresentationOrder()
	playlistTranscripts.append("\"{0}\"\n".format("\",\"".join([col for col in columnHeaders])))
	obj = start
	columnPos = [obj.indexOf(column) for column in columnHeaders]
	while obj not in (None, end):
		columnContents = obj._getColumnContents(columns=columnPos, readable=True)
		playlistTranscripts.append("\"{0}\"\n".format("\",\"".join([content for content in columnContents])))
		obj = obj.next
	if transcriptAction == 0:
		displayPlaylistTranscripts(playlistTranscripts)
	elif transcriptAction == 1:
		copyPlaylistTranscriptsToClipboard(playlistTranscripts)
	elif transcriptAction == 2:
		savePlaylistTranscriptsToFile(playlistTranscripts, "csv")


SPLPlaylistTranscriptFormats.append(("csv", playlist2csv, "Comma-separated values"))

# Playlist transcripts help desk
_plTranscriptsDialogOpened = False


def plTranscriptsDialogError() -> None:
	gui.messageBox(
		# Translators: Text of the dialog when another playlist transcripts dialog is open.
		_("Another playlist transcripts dialog is open."), translate("Error"), style=wx.OK | wx.ICON_ERROR
	)


class SPLPlaylistTranscriptsDialog(wx.Dialog):

	@classmethod
	def _instance(cls):
		return None

	def __new__(cls, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _plTranscriptsDialogOpened:
			raise RuntimeError("An instance of playlist transcripts dialog is opened")
		instance = SPLPlaylistTranscriptsDialog._instance()
		if instance is None:
			return super(SPLPlaylistTranscriptsDialog, cls).__new__(cls, *args, **kwargs)
		return instance

	def __init__(self, parent, obj):
		if SPLPlaylistTranscriptsDialog._instance() is not None:
			return
		# Use a weakref so the instance can die.
		SPLPlaylistTranscriptsDialog._instance = weakref.ref(self)

		# Translators: the Playlist transcripts dialog title.
		super().__init__(parent, wx.ID_ANY, _("Playlist Transcripts"))
		self.obj = obj

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		plTranscriptsSizerHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)

		self.transcriptRanges = (
			# Translators: one of the playlist transcripts range options.
			_("entire playlist"),
			# Translators: one of the playlist transcripts range options.
			_("start to current item"),
			# Translators: one of the playlist transcripts range options.
			_("current item to the end"),
			# Translators: one of the playlist transcripts range options.
			_("current hour"),
		)

		# Translators: The label in playlist transcripts dialog to select playlist transcript range.
		transcriptRangeLabel = _("Transcript range:")
		self.transcriptRange = plTranscriptsSizerHelper.addLabeledControl(
			transcriptRangeLabel, wx.Choice, choices=self.transcriptRanges
		)
		self.transcriptRange.SetSelection(0)

		# Translators: The label in playlist transcripts dialog to select transcript output format.
		transcriptFormatLabel = _("Transcript format:")
		self.transcriptFormat = plTranscriptsSizerHelper.addLabeledControl(
			transcriptFormatLabel, wx.Choice, choices=[output[2] for output in SPLPlaylistTranscriptFormats]
		)
		self.transcriptFormat.Bind(wx.EVT_CHOICE, self.onTranscriptFormatSelection)
		self.transcriptFormat.SetSelection(0)

		# Translators: one of the playlist transcript actions.
		self.transcriptActions = [		_("view transcript")]
		# 22.03 (security): disable clipboard copying or file saving functions in secure mode.
		if not globalVars.appArgs.secure:
			# Translators: one of the playlist transcript actions.
			self.transcriptActions.append(_("copy to clipboard"))
			# Translators: one of the playlist transcript actions.
			self.transcriptActions.append(_("save to file"))
		# Clipboard copying is possible for plain text (0), markdown table (3), CSV (4) but not in secure mode.
		self.copy2clipPossible = [0, 3, 4]

		# Translators: The label in playlist transcripts dialog to select transcript action.
		transcriptActionLabel = _("Transcript action:")
		self.transcriptAction = plTranscriptsSizerHelper.addLabeledControl(
			transcriptActionLabel, wx.Choice, choices=self.transcriptActions
		)
		self.transcriptAction.SetSelection(0)

		plTranscriptsSizerHelper.addDialogDismissButtons(wx.OK | wx.CANCEL, separated=True)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(plTranscriptsSizerHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.CenterOnScreen()
		self.transcriptRange.SetFocus()

	def onTranscriptFormatSelection(self, evt):
		# 22.03 (security): disable options other than viewing the transcript in secure mode.
		if globalVars.appArgs.secure:
			return
		# Not all formats support all actions
		# (for example, HTML table does not support copying to clipboard unless formatting is provided).
		action = self.transcriptFormat.GetSelection()
		self.transcriptAction.Clear()
		if action in self.copy2clipPossible:
			self.transcriptAction.SetItems(self.transcriptActions)
		else:
			self.transcriptAction.SetItems(["view transcript", "save to file"])
		self.transcriptAction.SetSelection(0)

	def onOk(self, evt):
		global _plTranscriptsDialogOpened
		start = None
		end = None
		transcriptRange = self.transcriptRange.Selection
		if transcriptRange in (0, 1):
			start = self.obj.parent.firstChild
		if transcriptRange == 1:
			end = self.obj.next
		if transcriptRange == 2:
			start = self.obj
		if transcriptRange == 3:
			# Try to locate boundaries for current hour slot.
			start = self.obj.appModule._trackLocator(
				"Hour Marker", obj=self.obj, directionForward=False, columns=[self.obj.indexOf("Category")]
			)
			end = self.obj.appModule._trackLocator(
				"Hour Marker", obj=self.obj, columns=[self.obj.indexOf("Category")]
			)
			# What if current track is indeed an hour marker?
			if end == self.obj:
				end = self.obj.appModule._trackLocator(
					"Hour Marker", obj=self.obj.next, columns=[self.obj.indexOf("Category")]
				)
		wx.CallLater(
			200, SPLPlaylistTranscriptFormats[self.transcriptFormat.Selection][1],
			start, end, self.transcriptAction.Selection
		)
		self.Destroy()
		_plTranscriptsDialogOpened = False

	def onCancel(self, evt):
		self.Destroy()
		global _plTranscriptsDialogOpened
		_plTranscriptsDialogOpened = False

	def onAppTerminate(self):
		# Call cancel function when the app terminates so the dialog can be closed.
		self.onCancel(None)
