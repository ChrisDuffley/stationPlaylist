# SPL Studio Miscellaneous User Interfaces and internal services
# An app module and global plugin package for NVDA
# Copyright 2015-2018 Joseph Lee and others, released under GPL.
# Miscellaneous functions and user interfaces
# Split from config module in 2015.

import sys
py3 = sys.version.startswith("3")
import weakref
import os
import threading
from _csv import reader # For cart explorer.
import gui
import wx
import ui
import addonHandler
addonHandler.initTranslation()
from winUser import user32
from . import splbase
from .spldebugging import debugOutput
from . import splactions
from .skipTranslation import translate

# Python 3 preparation (a compatibility layer until Six module is included).
rangeGen = range if py3 else xrange

# A custom combo box for cases where combo boxes are not choice controls.
class CustomComboBox(wx.ComboBox, wx.Choice):
	pass

# A common dialog for Track Finder
_findDialogOpened = False

# Track Finder error dialog.
# This will be refactored into something else.
def _finderError():
	global _findDialogOpened
	if _findDialogOpened:
		# Translators: Text of the dialog when another find dialog is open.
		gui.messageBox(_("Another find dialog is open."),translate("Error"),style=wx.OK | wx.ICON_ERROR)
	else:
		# Translators: Text of the dialog when a generic error has occured.
		gui.messageBox(_("An unexpected error has occured when trying to open find dialog."),translate("Error"),style=wx.OK | wx.ICON_ERROR)

class SPLFindDialog(wx.Dialog):

	_instance = None

	def __new__(cls, parent, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _findDialogOpened:
			raise RuntimeError("An instance of find dialog is opened")
		inst = cls._instance() if cls._instance else None
		if not inst:
			return super(cls, cls).__new__(cls, parent, *args, **kwargs)
		return inst

	def __init__(self, parent, obj, text, title, columnSearch=False):
		inst = SPLFindDialog._instance() if SPLFindDialog._instance else None
		if inst:
			return
		# Use a weakref so the instance can die.
		SPLFindDialog._instance = weakref.ref(self)

		super(SPLFindDialog, self).__init__(parent, wx.ID_ANY, title)
		self.obj = obj
		self.columnSearch = columnSearch
		if not columnSearch:
			findPrompt = _("Enter or select the name or the artist of the track you wish to &search")
		else:
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
			# Translators: The label in track finder to search columns.
			self.columnHeaders = findSizerHelper.addLabeledControl(_("C&olumn to search:"), wx.Choice, choices=splconfig._SPLDefaults["ColumnAnnouncement"]["ColumnOrder"])
			self.columnHeaders.SetSelection(0)

		findSizerHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON,self.onOk,id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON,self.onCancel,id=wx.ID_CANCEL)
		mainSizer.Add(findSizerHelper.sizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)
		self.findEntry.SetFocus()

	def onOk(self, evt):
		global _findDialogOpened
		text = self.findEntry.Value
		# Studio, are you alive?
		if user32.FindWindowW(u"SPLStudio", None) and text:
			appMod = self.obj.appModule
			column = [self.columnHeaders.Selection+1] if self.columnSearch else None
			startObj = self.obj
			if appMod.findText is None or (len(appMod.findText) and (text == appMod.findText[0] or text in appMod.findText)):
				startObj = startObj.next
				if appMod.findText is None: appMod.findText = [text]
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

	_instance = None

	def __new__(cls, parent, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _findDialogOpened:
			raise RuntimeError("An instance of find dialog is opened")
		inst = cls._instance() if cls._instance else None
		if not inst:
			return super(cls, cls).__new__(cls, parent, *args, **kwargs)
		return inst

	def __init__(self, parent, obj):
		inst = SPLTimeRangeDialog._instance() if SPLTimeRangeDialog._instance else None
		if inst:
			return
		# Use a weakref so the instance can die.
		SPLTimeRangeDialog._instance = weakref.ref(self)

		# Translators: The title of a dialog to find tracks with duration within a specified range.
		super(SPLTimeRangeDialog, self).__init__(parent, wx.ID_ANY, _("Time range finder"))
		self.obj = obj

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)

		minSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Minimum duration")), wx.HORIZONTAL)
		prompt = wx.StaticText(self, wx.ID_ANY, label=_("Minute"))
		minSizer.Add(prompt)
		self.minMinEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=59)
		self.minMinEntry.SetValue(3)
		self.minMinEntry.SetSelection(-1, -1)
		minSizer.Add(self.minMinEntry)
		prompt = wx.StaticText(self, wx.ID_ANY, label=_("Second"))
		minSizer.Add(prompt)
		self.minSecEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=59)
		self.minSecEntry.SetValue(0)
		self.minSecEntry.SetSelection(-1, -1)
		minSizer.Add(self.minSecEntry)
		mainSizer.Add(minSizer,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		maxSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Maximum duration")), wx.HORIZONTAL)
		prompt = wx.StaticText(self, wx.ID_ANY, label=_("Minute"))
		maxSizer.Add(prompt)
		self.maxMinEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=59)
		self.maxMinEntry.SetValue(5)
		self.maxMinEntry.SetSelection(-1, -1)
		maxSizer.Add(self.maxMinEntry)
		prompt = wx.StaticText(self, wx.ID_ANY, label=_("Second"))
		maxSizer.Add(prompt)
		self.maxSecEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=59)
		self.maxSecEntry.SetValue(0)
		self.maxSecEntry.SetSelection(-1, -1)
		maxSizer.Add(self.maxSecEntry)
		mainSizer.Add(maxSizer,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		# #68: wx.BoxSizer.AddSizer no longer exists in wxPython 4.
		mainSizer.Add(self.CreateButtonSizer(wx.OK|wx.CANCEL))
		self.Bind(wx.EVT_BUTTON,self.onOk,id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON,self.onCancel,id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)
		self.minMinEntry.SetFocus()

	def onOk(self, evt):
		minDuration = ((self.minMinEntry.GetValue() * 60) + self.minSecEntry.GetValue()) * 1000
		maxDuration = ((self.maxMinEntry.GetValue() * 60) + self.maxSecEntry.GetValue()) * 1000
		# What if minimum is greater than maximum (subtle oversight)?
		if minDuration >= maxDuration:
			gui.messageBox(
				# Translators: Message to report wrong value for duration fields.
				_("Minimum duration is greater than the maximum duration."),
				translate("Error"), wx.OK|wx.ICON_ERROR,self)
			self.minMinEntry.SetFocus()
			return
		self.Destroy()
		global _findDialogOpened
		if user32.FindWindowW(u"SPLStudio", None):
			obj = self.obj.next
			# Manually locate tracks here.
			while obj is not None:
				filename = splbase.studioAPI(obj.IAccessibleChildID-1, 211)
				if minDuration <= splbase.studioAPI(filename, 30) <= maxDuration:
					break
				obj = obj.next
			if obj is not None:
				# This time, set focus once, as doing it twice causes focus problems only if using Studio 5.10 or later.
				obj.setFocus()
				# 16.11: Select the desired track manually.
				# #45 (18.02): call select track function in splbase module.
				splbase.selectTrack(obj.IAccessibleChildID-1)
			else:
				wx.CallAfter(gui.messageBox,
				# Translators: Standard dialog message when an item one wishes to search is not found (copy this from main nvda.po).
				_("No track with duration between minimum and maximum duration."),
				# Translators: Standard error title for find error (copy this from main nvda.po).
				_("Time range find error"),wx.OK|wx.ICON_ERROR)
		_findDialogOpened = False

	def onCancel(self, evt):
		self.Destroy()
		global _findDialogOpened
		_findDialogOpened = False

	def onAppTerminate(self):
		# Call cancel function when the app terminates so the dialog can be closed.
		self.onCancel(None)


# Cart Explorer helper.

def _populateCarts(carts, cartlst, modifier, standardEdition=False, refresh=False):
	# The real cart string parser, a helper for cart explorer for building cart entries.
	# 5.2: Discard number row if SPL Standard is in use.
	if standardEdition: cartlst = cartlst[:12]
	# 18.08 (optimization): this is number row (except on Studio Standard), so assign identifier based on the below static list.
	numberRow = "1234567890-="
	for entry in cartlst:
		# An unassigned cart is stored with three consecutive commas, so skip it.
		# 17.04: If refresh is on, the cart we're dealing with is the actual carts dictionary that was built previously.
		noEntry = ",,," in entry
		if noEntry and not refresh: continue
		# Pos between 1 and 12 = function carts, 13 through 24 = number row carts, modifiers are checked.
		pos = cartlst.index(entry)+1
		# If a cart name has commas or other characters, SPL surrounds the cart name with quotes (""), so parse it as well.
		if not entry.startswith('"'): cartName = entry.split(",")[0]
		else: cartName = entry.split('"')[1]
		if pos <= 12: identifier = "f%s"%(pos)
		# For number row (except Studio Standard), subtract 13 because pos starts at 1, so by the time it comes to number row, it'll be 13.
		else: identifier = numberRow[pos-13]
		cart = identifier if not modifier else "+".join([modifier, identifier])
		if noEntry and refresh:
			if cart in carts: del carts[cart]
		else:
			carts[cart] = cartName

# Cart file timestamps.
_cartEditTimestamps = None
# Initialize Cart Explorer i.e. fetch carts.
# Cart files list is for future use when custom cart names are used.
# if told to refresh, timestamps will be checked and updated banks will be reassigned.
# Carts dictionary is used if and only if refresh is on, as it'll modify live carts.
def cartExplorerInit(StudioTitle, cartFiles=None, refresh=False, carts=None):
	global _cartEditTimestamps
	debugOutput("refreshing Cart Explorer" if refresh else "preparing cart Explorer")
	# Use cart files in SPL's data folder to build carts dictionary.
	# use a combination of SPL user name and static cart location to locate cart bank files.
	# Once the cart banks are located, use the routines in the populate method above to assign carts.
	# Since sstandard edition does not support number row carts, skip them if told to do so.
	if carts is None: carts = {"standardLicense":StudioTitle.startswith("StationPlaylist Studio Standard")}
	if refresh: carts["modifiedBanks"] = []
	# Obtain the "real" path for SPL via environment variables and open the cart data folder.
	cartsDataPath = os.path.join(os.environ["PROGRAMFILES"],"StationPlaylist","Data") # Provided that Studio was installed using default path.
	if cartFiles is None:
		# See if multiple users are using SPl Studio.
		userNameIndex = StudioTitle.find("-")
		# Read *.cart files and process the cart entries within (be careful when these cart file names change between SPL releases).
		# Until NVDA core moves to Python 3, assume that file names aren't unicode.
		cartFiles = [u"main carts.cart", u"shift carts.cart", u"ctrl carts.cart", u"alt carts.cart"]
		if userNameIndex >= 0:
			cartFiles = [StudioTitle[userNameIndex+2:]+" "+cartFile for cartFile in cartFiles]
	faultyCarts = False
	if not refresh:
		_cartEditTimestamps = []
	for f in cartFiles:
		# Only do this if told to build cart banks from scratch, as refresh flag is set if cart explorer is active in the first place.
		try:
			mod = f.split()[-2] # Checking for modifier string such as ctrl.
			# Todo: Check just in case some SPL flavors doesn't ship with a particular cart file.
		except IndexError:
			faultyCarts = True # In a rare event that the broadcaster has saved the cart bank with the name like "carts.cart".
			continue
		cartFile = os.path.join(cartsDataPath,f)
		# Cart explorer can safely assume that the cart bank exists if refresh flag is set.
		if not refresh and not os.path.isfile(cartFile): # Cart explorer will fail if whitespaces are in the beginning or at the end of a user name.
			faultyCarts = True
			continue
		debugOutput("examining carts from file %s"%cartFile)
		cartTimestamp = os.path.getmtime(cartFile)
		if refresh and _cartEditTimestamps[cartFiles.index(f)] == cartTimestamp:
			debugOutput("no changes to cart bank, skipping")
			continue
		_cartEditTimestamps.append(cartTimestamp)
		with open(cartFile) as cartInfo:
			cl = [row for row in reader(cartInfo)]
		# 17.04 (optimization): let empty string represent main cart bank to avoid this being partially consulted up to 24 times.
		# The below method will just check for string length, which is faster than looking for specific substring.
		_populateCarts(carts, cl[1], mod if mod != "main" else "", standardEdition=carts["standardLicense"], refresh=refresh) # See the comment for _populate method above.
		if not refresh:
			debugOutput("carts processed so far: %s"%(len(carts)-1))
	carts["faultyCarts"] = faultyCarts
	debugOutput("total carts processed: %s"%(len(carts)-2))
	return carts

# Refresh carts upon request.
# calls cart explorer init with special (internal) flags.
def cartExplorerRefresh(studioTitle, currentCarts):
	return cartExplorerInit(studioTitle, refresh=True, carts=currentCarts)

# Countdown timer.
# This is utilized by many services, chiefly profile triggers routine.

class SPLCountdownTimer(object):

	def __init__(self, duration, func, threshold):
		# Threshold is used to instruct this timer when to start countdown announcement.
		self.duration = duration
		self.total = duration
		self.func = func
		self.threshold = threshold

	def Start(self):
		self.timer = wx.PyTimer(self.countdown)
		ui.message(_("Countdown started"))
		# #58 (18.04.1): timers must be started from main thread.
		wx.CallAfter(self.timer.Start, 1000)

	def Stop(self):
		self.timer.Stop()

	def IsRunning(self):
		return self.timer.IsRunning()

	def countdown(self):
		self.duration -= 1
		if self.duration == 0:
			ui.message(_("Timer complete"))
			if self.func is not None:
				self.func()
			self.Stop()
		elif 0 < self.duration <= self.threshold:
			ui.message(str(self.duration))


# Metadata and encoders management, including connection, announcement and so on.

# Gather streaming flags into a list.
# 18.04: raise runtime error if list is nothing (thankfully the splbase's StudioAPI will return None if Studio handle is not found).
def metadataList():
	metadata = [splbase.studioAPI(pos, 36) for pos in rangeGen(5)]
	if metadata == [None, None, None, None, None]:
		raise RuntimeError("Studio handle not found, no metadata list to return")
	return metadata

# Metadata server connector, to be utilized from many modules.
# Servers refer to a list of connection flags to pass to Studio API, and if not present, will be pulled from add-on settings.
def metadataConnector(servers=None):
	if servers is None:
		from . import splconfig
		servers = splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"]
	for url in rangeGen(5):
		dataLo = 0x00010000 if servers[url] else 0xffff0000
		splbase.studioAPI(dataLo | url, 36)

# Metadata status formatter.
# 18.04: say something if Studio handle is not found.
def metadataStatus():
	try:
		streams = metadataList()
	except RuntimeError:
		# Translators: presented when metadata streaming status cannot be obtained.
		return _("Cannot obtain metadata streaming status information")
	# DSP is treated specially.
	dsp = streams[0]
	# For others, a simple list.append will do.
	# 17.04: Use a conditional list comprehension.
	# 18.02: comprehend based on streams list from above.
	streamCount = [str(pos) for pos in rangeGen(1, 5) if streams[pos]]
	# Announce streaming status when told to do so.
	status = None
	if not len(streamCount):
		# Translators: Status message for metadata streaming.
		if not dsp: status = _("No metadata streaming URL's defined")
		# Translators: Status message for metadata streaming.
		else: status = _("Metadata streaming configured for DSP encoder")
	elif len(streamCount) == 1:
		# Translators: Status message for metadata streaming.
		if dsp: status = _("Metadata streaming configured for DSP encoder and URL {URL}").format(URL = streamCount[0])
		# Translators: Status message for metadata streaming.
		else: status = _("Metadata streaming configured for URL {URL}").format(URL = streamCount[0])
	else:
		# Translators: Status message for metadata streaming.
		if dsp: status = _("Metadata streaming configured for DSP encoder and URL's {URL}").format(URL = ", ".join(streamCount))
		# Translators: Status message for metadata streaming.
		else: status = _("Metadata streaming configured for URL's {URL}").format(URL = ", ".join(streamCount))
	return status

# Internal metadata status announcer.
# The idea is to pause for a while and announce the status message and playing the accompanying wave file.
# This is necessary in order to allow extension points to work correctly and to not hold up other registered action handlers.
# A special startup flag will be used so other text sequences will not be cut off.
def _metadataAnnouncerInternal(status, startup=False):
	import nvwave, queueHandler, speech
	if not startup: speech.cancelSpeech()
	queueHandler.queueFunction(queueHandler.eventQueue, ui.message, status)
	nvwave.playWaveFile(os.path.join(os.path.dirname(__file__), "SPL_Metadata.wav"))
	# #51 (18.03/15.14-LTS): close link to metadata announcer thread when finished.
	global _earlyMetadataAnnouncer
	_earlyMetadataAnnouncer = None

# Handle a case where instant profile ssitch occurs twice within the switch time-out.
_earlyMetadataAnnouncer = None

def _earlyMetadataAnnouncerInternal(status, startup=False):
	global _earlyMetadataAnnouncer
	if _earlyMetadataAnnouncer is not None:
		_earlyMetadataAnnouncer.cancel()
		_earlyMetadataAnnouncer = None
	_earlyMetadataAnnouncer = threading.Timer(2, _metadataAnnouncerInternal, args=[status], kwargs={"startup": startup})
	_earlyMetadataAnnouncer.start()

# Delay the action handler if Studio handle is not found.
_delayMetadataAction = False

# Connect and/or announce metadata status when broadcast profile switching occurs.
# The config dialog active flag is only invoked when being notified while add-on settings dialog is focused.
def metadata_actionProfileSwitched(configDialogActive=False):
	from . import splconfig
	# Only connect if add-on settings is active in order to avoid wasting thread running time.
	if configDialogActive:
		metadataConnector(servers=splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"])
		return
	global _delayMetadataAction
	# Ordinarily, errors would have been dealt with, but Action.notify will catch errors and log messages.
	# #40 (18.02): the only possible error is if Studio handle is invalid, which won't be the case, otherwise no point handling this action.
	# #49 (18.03): no, don't announce this if the app module is told to announce metadata status at startup only.
	if splconfig.SPLConfig["General"]["MetadataReminder"] == "instant":
		# If told to remind and connect, metadata streaming will be enabled at this time.
		# 6.0: Call Studio API twice - once to set, once more to obtain the needed information.
		# 6.2/7.0: When Studio API is called, add the value into the stream count list also.
		# 17.11: call the connector.
		# 18.02: transfered to the action handler and greatly simplified.
		# 18.04: ask the handle finder to return to this place if Studio handle isn't ready.
		# This is typically the case when launching Studio and profile switch occurs while demo registration screen is up.
		handle = user32.FindWindowW(u"SPLStudio", None)
		if not handle:
			_delayMetadataAction = True
			return
		metadataConnector()
		# #47 (18.02/15.13-LTS): call the internal announcer via wx.CallLater in order to not hold up action handler queue.
		# #51 (18.03/15.14-LTS): wx.CallLater isn't enough - there must be ability to cancel it.
		_earlyMetadataAnnouncerInternal(metadataStatus())

splactions.SPLActionProfileSwitched.register(metadata_actionProfileSwitched)

# Playlist transcripts processor
# Takes a snapshot of the active playlist (a 2-D array) and transforms it into various formats.
# To account for expansions, let a master function call different formatters based on output format.
SPLPlaylistTranscriptFormats = []

# Obtain column presentation order.
# Although this is useful in playlist transcripts, it can also be useful for column announcement inclusion and order.
def columnPresentationOrder():
	from . import splconfig
	return [column for column in splconfig.SPLConfig["PlaylistTranscripts"]["ColumnOrder"]
		if column in splconfig.SPLConfig["PlaylistTranscripts"]["IncludedColumns"]]

# Various post-transcript actions.
# For each converter, after transcribing the playlist, additional actions will be performed.
# Actions can include viewing the transcript, copying to clipboard (text style format only), and saving to a file.

def displayPlaylistTranscripts(transcript, HTMLDecoration=False):
	ui.browseableMessage("\n".join(transcript),title=_("Playlist Transcripts"), isHtml=HTMLDecoration)

def copyPlaylistTranscriptsToClipboard(playlistTranscripts):
	# Only text style transcript such as pure text and Markdown supports copying contents to clipboard.
	import api
	api.copyToClip(u"\r\n".join(playlistTranscripts))
	ui.message(_("Playlist data copied to clipboard"))

def savePlaylistTranscriptsToFile(playlistTranscripts, extension, location=None):
	# By default playlist transcripts will be saved to a subfolder in user's Documents folder named "nvdasplPlaylistTranscripts".
	# Each transcript file will be named yyyymmdd-hhmmss-splPlaylistTranscript.ext.
	transcriptFileLocation = os.path.join(os.environ["userprofile"], "Documents", "nvdasplPlaylistTranscripts")
	if not os.path.exists(transcriptFileLocation):
		os.mkdir(transcriptFileLocation)
	import datetime
	transcriptTimestamp = datetime.datetime.now()
	transcriptFilename = "{0}{1:02d}{2:02d}-{3:02d}{4:02d}{5:02d}-splPlaylistTranscript.{6}".format(
		transcriptTimestamp.year, transcriptTimestamp.month, transcriptTimestamp.day, transcriptTimestamp.hour, transcriptTimestamp.minute, transcriptTimestamp.second, extension)
	transcriptPath = os.path.join(transcriptFileLocation, transcriptFilename)
	with open(transcriptPath, "w") as transcript:
		transcript.writelines(playlistTranscripts)
	ui.message("Playlist transcripts saved at {location}".format(location = transcriptPath))

# Several converters rely on assistants for their work.
# For text file 1 and HTML list 1, it expects playlist data in the format presented by MSAA.
# Header will not be included if additional decorations will be done (mostly for HTML and others).
# Prefix and suffix denote text to be added around entries (useful for various additional decoration rules).
def playlist2msaa(start, end, additionalDecorations=False, prefix="", suffix=""):
	playlistTranscripts = []
	#Just pure text, ready for the clipboard or writing to a txt file.
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
		for column in rangeGen(len(columnPos)):
			if columnContents[column] is not None:
				filteredContent.append("%s: %s"%(columnHeaders[column], columnContents[column]))
		playlistTranscripts.append("{0}{1}{2}".format(prefix, "; ".join(filteredContent), suffix))
		obj = obj.next
	return playlistTranscripts

def playlist2txt(start, end, transcriptAction):
	playlistTranscripts = playlist2msaa(start, end)
	if transcriptAction == 0: displayPlaylistTranscripts(playlistTranscripts)
	elif transcriptAction == 1: copyPlaylistTranscriptsToClipboard(playlistTranscripts)
	elif transcriptAction == 2: savePlaylistTranscriptsToFile(playlistTranscripts, "txt")
SPLPlaylistTranscriptFormats.append(("txt", playlist2txt, "plain text with one line per entry"))

def playlist2csv(start, end, transcriptAction):
	playlistTranscripts = []
	columnHeaders = columnPresentationOrder()
	playlistTranscripts.append("\"{0}\"\n".format("\",\"".join([col for col in columnHeaders])))
	obj = start
	columnPos = [obj.indexOf(column) for column in columnHeaders]
	while obj not in (None, end):
		columnContents = obj._getColumnContents(columns=columnPos, readable=True)
		playlistTranscripts.append("\"{0}\"\n".format("\",\"".join([content for content in columnContents])))
		obj = obj.next
	if transcriptAction == 0: displayPlaylistTranscripts(playlistTranscripts)
	elif transcriptAction == 1: copyPlaylistTranscriptsToClipboard(playlistTranscripts)
	elif transcriptAction == 2: savePlaylistTranscriptsToFile(playlistTranscripts, "csv")
SPLPlaylistTranscriptFormats.append(("csv", playlist2csv, "Comma-separated values"))

def playlist2htmlTable(start, end, transcriptAction):
	if transcriptAction == 1:
		playlistTranscripts = ["<html><head><title>Playlist Transcripts</title></head>"]
		playlistTranscripts.append("<body>")
		playlistTranscripts.append("Playlist Transcripts - use table navigation commands to review track information")
	else: playlistTranscripts = ["Playlist Transcripts - use table navigation commands to review track information"]
	playlistTranscripts.append("<p>")
	columnHeaders = columnPresentationOrder()
	playlistTranscripts.append("<table><tr><th>{trackHeaders}</tr>".format(trackHeaders = "<th>".join(columnHeaders)))
	obj = start
	columnPos = [obj.indexOf(column) for column in columnHeaders]
	while obj not in (None, end):
		columnContents = obj._getColumnContents(columns=columnPos, readable=True)
		playlistTranscripts.append("<tr><td>{trackContents}</tr>".format(trackContents = "<td>".join(columnContents)))
		obj = obj.next
	playlistTranscripts.append("</table>")
	if transcriptAction == 0: displayPlaylistTranscripts(playlistTranscripts, HTMLDecoration=True)
	elif transcriptAction == 1:
		playlistTranscripts.append("</body></html>")
		savePlaylistTranscriptsToFile(playlistTranscripts, "htm")
SPLPlaylistTranscriptFormats.append(("htmltable", playlist2htmlTable, "Table in HTML format"))

def playlist2htmlList(start, end, transcriptAction):
	if transcriptAction == 1:
		playlistTranscripts = ["<html><head><title>Playlist Transcripts</title></head>"]
		playlistTranscripts.append("<body>")
		playlistTranscripts.append("Playlist Transcripts - use list navigation commands to review track information")
	else: playlistTranscripts = ["Playlist Transcripts - use list navigation commands to review track information"]
	playlistTranscripts.append("<p><ol>")
	playlistTranscripts += playlist2msaa(start, end, additionalDecorations=True, prefix="<li>")
	playlistTranscripts.append("</ol>")
	if transcriptAction == 0: displayPlaylistTranscripts(playlistTranscripts, HTMLDecoration=True)
	elif transcriptAction == 1:
		playlistTranscripts.append("</body></html>")
		savePlaylistTranscriptsToFile(playlistTranscripts, "htm")
SPLPlaylistTranscriptFormats.append(("htmllist", playlist2htmlList, "Data list in HTML format"))

def playlist2mdTable(start, end, transcriptAction):
	playlistTranscripts = []
	columnHeaders = columnPresentationOrder()
	playlistTranscripts.append("| {headers} |\n".format(headers = " | ".join(columnHeaders)))
	obj = start
	columnPos = [obj.indexOf(column) for column in columnHeaders]
	while obj not in (None, end):
		columnContents = obj._getColumnContents(columns=columnPos, readable=True)
		playlistTranscripts.append("| {trackContents} |\n".format(trackContents = " | ".join(columnContents)))
		obj = obj.next
	if transcriptAction == 0: displayPlaylistTranscripts(playlistTranscripts)
	elif transcriptAction == 1: copyPlaylistTranscriptsToClipboard(playlistTranscripts)
	elif transcriptAction == 2: savePlaylistTranscriptsToFile(playlistTranscripts, "md")
SPLPlaylistTranscriptFormats.append(("mdtable", playlist2mdTable, "Table in Markdown format"))

# Playlist transcripts help desk
_plTranscriptsDialogOpened = False

def plTranscriptsDialogError():
	# Translators: Text of the dialog when another playlist transcripts dialog is open.
	gui.messageBox(_("Another playlist transcripts dialog is open."),translate("Error"),style=wx.OK | wx.ICON_ERROR)

class SPLPlaylistTranscriptsDialog(wx.Dialog):

	_instance = None

	def __new__(cls, parent, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _plTranscriptsDialogOpened:
			raise RuntimeError("An instance of playlist transcripts dialog is opened")
		inst = cls._instance() if cls._instance else None
		if not inst:
			return super(cls, cls).__new__(cls, parent, *args, **kwargs)
		return inst

	def __init__(self, parent, obj):
		inst = SPLPlaylistTranscriptsDialog._instance() if SPLPlaylistTranscriptsDialog._instance else None
		if inst:
			return
		# Use a weakref so the instance can die.
		SPLPlaylistTranscriptsDialog._instance = weakref.ref(self)

		# Translators: the Playlist transcripts dialog title.
		super(SPLPlaylistTranscriptsDialog, self).__init__(parent, wx.ID_ANY, _("Playlist Transcripts"))
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
		self.transcriptRange = plTranscriptsSizerHelper.addLabeledControl(_("Transcript range:"), wx.Choice, choices=self.transcriptRanges)
		self.transcriptRange.SetSelection(0)

		# Translators: The label in playlist transcripts dialog to select transcript output format.
		self.transcriptFormat = plTranscriptsSizerHelper.addLabeledControl(_("Transcript format:"), wx.Choice, choices=[output[2] for output in SPLPlaylistTranscriptFormats])
		self.transcriptFormat.Bind(wx.EVT_CHOICE, self.onTranscriptFormatSelection)
		self.transcriptFormat.SetSelection(0)

		self.transcriptActions = (
			# Translators: one of the playlist transcript actions.
			_("view transcript"),
			# Translators: one of the playlist transcript actions.
			_("copy to clipboard"),
			# Translators: one of the playlist transcript actions.
			_("save to file"),
		)
		self.copy2clipPossible = [0, 1, 4]

		# Translators: The label in playlist transcripts dialog to select transcript action.
		self.transcriptAction = plTranscriptsSizerHelper.addLabeledControl(_("Transcript action:"), wx.Choice, choices=self.transcriptActions)
		self.transcriptAction.SetSelection(0)

		plTranscriptsSizerHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON,self.onOk,id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON,self.onCancel,id=wx.ID_CANCEL)
		mainSizer.Add(plTranscriptsSizerHelper.sizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)
		self.transcriptRange.SetFocus()

	def onTranscriptFormatSelection(self, evt):
		# Not all formats support all actions (for example, HTML table does not support copying to clipboard unless formatting is provided).
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
			start = self.obj.appModule._trackLocator("Hour Marker", obj=self.obj, directionForward=False, columns=[self.obj.indexOf("Category")])
			end = self.obj.appModule._trackLocator("Hour Marker", obj=self.obj, columns=[self.obj.indexOf("Category")])
			# What if current track is indeed an hour marker?
			if end == self.obj:
				end = self.obj.appModule._trackLocator("Hour Marker", obj=self.obj.next, columns=[self.obj.indexOf("Category")])
		wx.CallLater(200, SPLPlaylistTranscriptFormats[self.transcriptFormat.Selection][1], start, end, self.transcriptAction.Selection)
		self.Destroy()
		_plTranscriptsDialogOpened = False

	def onCancel(self, evt):
		self.Destroy()
		global _plTranscriptsDialogOpened
		_plTranscriptsDialogOpened = False

	def onAppTerminate(self):
		# Call cancel function when the app terminates so the dialog can be closed.
		self.onCancel(None)
