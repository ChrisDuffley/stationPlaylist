# SPL Studio playlist analyzer
# An app module and global plugin package for NVDA
# Copyright 2026 Joseph Lee, released under GPL.
# Playlist analyzer utilities and support services.
# Split from splmisc module in 2026.

import weakref
import os
import datetime
import json
import api
import gui
import wx
import core
import globalVars
import ui
import addonHandler
from NVDAObjects import NVDAObject
from ..splcommon import splactions, splconfig
from ..skipTranslation import translate

addonHandler.initTranslation()

# Playlist transcripts processor
# Takes a snapshot of the active playlist (a 2-D array) and transforms it into various formats.
# To account for expansions, let a master function call different formatters based on output format.
SPLPlaylistTranscriptFormats = []
# Local Studio 6.20 changes "Time Scheduled" to "Time".
# Present the correct column title.
_timeScheduled2Time: bool = False


# Obtain column presentation order.
# Although this is useful in playlist transcripts,
# it can also be useful for column announcement inclusion and order.
def columnPresentationOrder() -> list[str]:
	global _timeScheduled2Time
	presentationOrder = [
		column
		for column in splconfig.SPLConfig["PlaylistTranscripts"]["ColumnOrder"]
		if column in splconfig.SPLConfig["PlaylistTranscripts"]["IncludedColumns"]
	]
	if _timeScheduled2Time and "Time Scheduled" in presentationOrder:
		presentationOrder[presentationOrder.index("Time Scheduled")] = "Time"
		_timeScheduled2Time = False
	return presentationOrder


# Various post-transcript actions.
# For each converter, after transcribing the playlist, additional actions will be performed.
# Actions can include viewing the transcript,
# copying to clipboard (text style format only), and saving to a file.


def displayPlaylistTranscripts(transcript: list[str], HTMLDecoration: bool = False) -> None:
	ui.browseableMessage(
		"\n".join(transcript),
		title=_("Playlist Transcripts"),
		isHtml=HTMLDecoration,
		closeButton=True,
	)


def copyPlaylistTranscriptsToClipboard(playlistTranscripts: list[str]) -> None:
	# Security: do not copy transcripts to clipboard in secure mode.
	if globalVars.appArgs.secure:
		return
	# Only text style transcript such as pure text and Markdown supports copying contents to clipboard.
	api.copyToClip("\r\n".join(playlistTranscripts))
	# Translators: presented when playlist transcript data was copied to the clipboard.
	ui.message(_("Playlist data copied to clipboard"))


def savePlaylistTranscriptsToFile(playlistTranscripts: list[str], extension: str) -> None:
	# Security: do not save transcripts to files in secure mode.
	if globalVars.appArgs.secure:
		return
	# By default playlist transcripts will be saved to a subfolder in user's Documents folder
	# named "nvdasplPlaylistTranscripts".
	# Each transcript file will be named yyyymmdd-hhmmss-splPlaylistTranscript.ext.
	transcriptFileLocation = os.path.join(
		os.environ["userprofile"], "Documents", "nvdasplPlaylistTranscripts"
	)
	if not os.path.exists(transcriptFileLocation):
		os.mkdir(transcriptFileLocation)
	transcriptTimestamp = datetime.datetime.now()
	transcriptFilename = "{0}{1:02d}{2:02d}-{3:02d}{4:02d}{5:02d}-splPlaylistTranscript.{6}".format(
		transcriptTimestamp.year,
		transcriptTimestamp.month,
		transcriptTimestamp.day,
		transcriptTimestamp.hour,
		transcriptTimestamp.minute,
		transcriptTimestamp.second,
		extension,
	)
	transcriptPath = os.path.join(transcriptFileLocation, transcriptFilename)
	with open(transcriptPath, "w") as transcript:
		transcript.writelines(playlistTranscripts)
	ui.message("Playlist transcripts saved at {location}".format(location=transcriptPath))


def postTranscriptsAction(
	playlistTranscripts: list[str], transcriptAction: int, extension: str, HTMLDecoration: bool = False
) -> None:
	match transcriptAction:
		case 0:  # View transcripts
			displayPlaylistTranscripts(playlistTranscripts, HTMLDecoration=HTMLDecoration)
		case 1:  # Copy transcripts (text formats only)
			copyPlaylistTranscriptsToClipboard(playlistTranscripts)
		case 2:  # Save transcripts
			savePlaylistTranscriptsToFile(playlistTranscripts, extension)
		case _:  # Unknown action
			raise RuntimeError(f"SPL: unknown playlist transcripts action: {transcriptAction}")


# Several converters rely on assistants for their work.
# For text file 1 and HTML list 1, it expects playlist data in the format presented by MSAA.
# Header will not be included if additional decorations will be done (mostly for HTML and others).
# Prefix and suffix denote text to be added around entries (useful for various additional decoration rules).
def playlist2msaa(
	start: NVDAObject,
	end: NVDAObject | None,
	additionalDecorations: bool = False,
	prefix: str = "",
	suffix: str = ""
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
		# #148: work directly with column content and position rather than going through column pos index.
		for column, content in enumerate(columnContents):
			if content:
				filteredContent.append("{}: {}".format(columnHeaders[column], content))
		playlistTranscripts.append("{0}{1}{2}".format(prefix, "; ".join(filteredContent), suffix))
		obj = obj.next
	return playlistTranscripts


def playlist2txt(start: NVDAObject, end: NVDAObject | None, transcriptAction: int) -> None:
	playlistTranscripts = playlist2msaa(start, end)
	postTranscriptsAction(playlistTranscripts, transcriptAction, "txt")


SPLPlaylistTranscriptFormats.append(("txt", playlist2txt, "plain text with one line per entry"))


def playlist2htmlTable(start: NVDAObject, end: NVDAObject | None, transcriptAction: int) -> None:
	if transcriptAction == 1:
		playlistTranscripts = ["<html><head><title>Playlist Transcripts</title></head>"]
		playlistTranscripts.append("<body>")
		playlistTranscripts.append("<h1>Playlist Transcripts</h1>")
	else:
		playlistTranscripts = ["<h1>Playlist Transcripts</h1>"]
	playlistTranscripts.append("<p>")
	columnHeaders = columnPresentationOrder()
	playlistTranscripts.append(
		"<table><tr><th>{trackHeaders}</tr>".format(trackHeaders="<th>".join(columnHeaders))
	)
	obj = start
	columnPos = [obj.indexOf(column) for column in columnHeaders]
	while obj not in (None, end):
		columnContents = obj._getColumnContents(columns=columnPos, readable=True)
		playlistTranscripts.append(
			"<tr><td>{trackContents}</tr>".format(trackContents="<td>".join(columnContents))
		)
		obj = obj.next
	playlistTranscripts.append("</table>")
	# HTML table processor does not support copy operation.
	if transcriptAction == 1:
		playlistTranscripts.append("</body></html>")
		transcriptAction = 2
	postTranscriptsAction(playlistTranscripts, transcriptAction, "htm", HTMLDecoration=True)


SPLPlaylistTranscriptFormats.append(("htmltable", playlist2htmlTable, "Table in HTML format"))


def playlist2htmlList(start: NVDAObject, end: NVDAObject | None, transcriptAction: int) -> None:
	if transcriptAction == 1:
		playlistTranscripts = ["<html><head><title>Playlist Transcripts</title></head>"]
		playlistTranscripts.append("<body>")
		playlistTranscripts.append("<h1>Playlist Transcripts</h1>")
	else:
		playlistTranscripts = ["<h1>Playlist Transcripts</h1>"]
	playlistTranscripts.append("<p><ol>")
	playlistTranscripts += playlist2msaa(start, end, additionalDecorations=True, prefix="<li>")
	playlistTranscripts.append("</ol>")
	# HTML list processor does not support copy operation.
	if transcriptAction == 1:
		playlistTranscripts.append("</body></html>")
		transcriptAction = 2
	postTranscriptsAction(playlistTranscripts, transcriptAction, "htm", HTMLDecoration=True)


SPLPlaylistTranscriptFormats.append(("htmllist", playlist2htmlList, "Data list in HTML format"))


def playlist2mdTable(start: NVDAObject, end: NVDAObject | None, transcriptAction: int) -> None:
	playlistTranscripts = []
	columnHeaders = columnPresentationOrder()
	playlistTranscripts.append("| {headers} |\n".format(headers=" | ".join(columnHeaders)))
	obj = start
	columnPos = [obj.indexOf(column) for column in columnHeaders]
	while obj not in (None, end):
		columnContents = obj._getColumnContents(columns=columnPos, readable=True)
		playlistTranscripts.append("| {trackContents} |\n".format(trackContents=" | ".join(columnContents)))
		obj = obj.next
	postTranscriptsAction(playlistTranscripts, transcriptAction, "md")


SPLPlaylistTranscriptFormats.append(("mdtable", playlist2mdTable, "Table in Markdown format"))


def playlist2csv(start: NVDAObject, end: NVDAObject | None, transcriptAction: int) -> None:
	playlistTranscripts = []
	columnHeaders = columnPresentationOrder()
	playlistTranscripts.append('"{0}"\n'.format('","'.join([col for col in columnHeaders])))
	obj = start
	columnPos = [obj.indexOf(column) for column in columnHeaders]
	while obj not in (None, end):
		columnContents = obj._getColumnContents(columns=columnPos, readable=True)
		playlistTranscripts.append('"{0}"\n'.format('","'.join([content for content in columnContents])))
		obj = obj.next
	postTranscriptsAction(playlistTranscripts, transcriptAction, "csv")


SPLPlaylistTranscriptFormats.append(("csv", playlist2csv, "Comma-separated values"))


def playlist2json(start: NVDAObject, end: NVDAObject | None, transcriptAction: int) -> None:
	playlistTranscripts = []
	columnHeaders = columnPresentationOrder()
	obj = start
	columnPos = [obj.indexOf(column) for column in columnHeaders]
	while obj not in (None, end):
		columnContents = obj._getColumnContents(columns=columnPos)
		# Transform column contents into header:content dictionary.
		columnHeadersContents = {}
		for header, content in zip(columnHeaders, columnContents):
			if content:
				columnHeadersContents[header] = content
		playlistTranscripts.append(columnHeadersContents)
		obj = obj.next
	# Transform the tabbed json output to a list as that is what display/copy/save methods want.
	playlistTranscripts = [json.dumps(playlistTranscripts, indent="\t")]
	postTranscriptsAction(playlistTranscripts, transcriptAction, "json")


SPLPlaylistTranscriptFormats.append(("json", playlist2json, "JSON (JavaScript Object Notation)"))

# Playlist transcripts help desk
_plTranscriptsDialogOpened = False


def plTranscriptsDialogError() -> None:
	gui.messageBox(
		# Translators: Text of the dialog when another playlist transcripts dialog is open.
		_("Another playlist transcripts dialog is open."),
		translate("Error"),
		style=wx.OK | wx.ICON_ERROR,
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
		global _plTranscriptsDialogOpened
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
		self.transcriptActions = [_("view transcript")]
		# Security: disable clipboard copying or file saving functions in secure mode.
		if not globalVars.appArgs.secure:
			# Translators: one of the playlist transcript actions.
			self.transcriptActions.append(_("copy to clipboard"))
			# Translators: one of the playlist transcript actions.
			self.transcriptActions.append(_("save to file"))
		# Clipboard copying is possible for plain text (0), markdown table (3), CSV (4), json (5)
		# but not in secure mode.
		self.copy2clipPossible = [0, 3, 4, 5]

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
		_plTranscriptsDialogOpened = True

	def onTranscriptFormatSelection(self, evt):
		# Security: disable options other than viewing the transcript in secure mode.
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
		global _plTranscriptsDialogOpened, _timeScheduled2Time
		_timeScheduled2Time = "Time" in self.obj.screenColumnOrder
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
		core.callLater(
			200,
			SPLPlaylistTranscriptFormats[self.transcriptFormat.Selection][1],
			start,
			end,
			self.transcriptAction.Selection,
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
