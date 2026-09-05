# SPL Studio playlist analyzer
# An app module and global plugin package for NVDA
# Copyright 2026 Joseph Lee, released under GPL.

# Playlist analyzer utilities and support services.
# Includes playlist duration, snapshots, time analysis, and transcripts processor.
# Playlist analyzer invocation checks such as whether a playlist is loaded is done by the app module.
# Split from main app module and splmisc module in 2026.

from typing import Any
import weakref
import os
import datetime
import json
import collections
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

# Return total duration of a range of tracks.
# This is used in track time analysis when multiple tracks are selected.
# This is also called from playlist duration scripts.
def playlistDuration(start: NVDAObject | None = None, end: NVDAObject | None = None) -> int:
	if start is None:
		start = api.getFocusObject()
	duration = start.indexOf("Duration")
	totalDuration = 0
	obj = start
	while obj not in (None, end):
		# Technically segue.
		segue = obj._getColumnContentRaw(duration)
		# NVDA returns an empty string instead of None in order to
		# avoid errors with 64-bit SysListView32 controls.
		# For compatibility, check both None and an empty string.
		if segue not in (None, "", "00:00"):
			hms = segue.split(":")
			totalDuration += (int(hms[-2]) * 60) + int(hms[-1])
			if len(hms) == 3:
				totalDuration += int(hms[0]) * 3600
		obj = obj.next
	return totalDuration

# Playlist snapshots
# Data to be gathered comes from a set of flags.
# By default, playlist duration (including shortest and average),
# category summary and other statistics will be gathered.
def playlistSnapshots(
	obj: NVDAObject, end: NVDAObject | None, snapshotFlags: list[str] | None = None
) -> dict[str, Any]:
	# Track count and total duration are always included.
	# #155: annotate snapshot map to avoid type annotation issues when assigning key/value pairs.
	snapshot: dict[str, Any] = {}
	if snapshotFlags is None:
		snapshotFlags = [
			flag
			for flag in splconfig.SPLConfig["PlaylistSnapshots"]
			if splconfig.SPLConfig["PlaylistSnapshots"][flag]
		]
	duration = obj.indexOf("Duration")
	title = obj.indexOf("Title")
	# A tuple list of duration in seconds (integer) and track titles.
	# Used to obtain total duration, average, shortest, and longest tracks.
	trackLengths = []
	totalDuration = 0
	artist = obj.indexOf("Artist")
	artists = []
	category = obj.indexOf("Category")
	categories = []
	genre = obj.indexOf("Genre")
	genres = []
	# Have a copy of milliseconds to time display converter from the app module.
	_ms2time = obj.appModule._ms2time
	# A specific version of the playlist duration loop is needed in order to gather statistics.
	while obj not in (None, end):
		segue = obj._getColumnContentRaw(duration)
		trackTitle = obj._getColumnContentRaw(title)
		categories.append(obj._getColumnContentRaw(category))
		# Don't record artist and genre information for an hour marker (reported by a broadcaster).
		# In Remote Studio, hour marker sets "00:00" as duration, so don't add segue either.
		if categories[-1] != "Hour Marker":
			artists.append(obj._getColumnContentRaw(artist))
			genres.append(obj._getColumnContentRaw(genre))
		else:
			segue = None
		# Convert segue to an integer for ease of min/max comparison.
		# NVDA returns an empty string instead of None in order to
		# avoid errors with 64-bit SysListView32 controls.
		# For compatibility, check both None and an empty string.
		if segue not in (None, ""):
			hms = segue.split(":")
			segue = (int(hms[-2]) * 60) + int(hms[-1])
			if len(hms) == 3:
				segue += int(hms[0]) * 3600
			totalDuration += segue
			trackLengths.append((segue, trackTitle))
		obj = obj.next
	# Count track categories (for a complete playlist snapshot, categories count equals item count).
	snapshot["PlaylistItemCount"] = len(categories)
	snapshot["PlaylistTrackCount"] = len(artists)
	snapshot["PlaylistDurationTotal"] = _ms2time(totalDuration, ms=False)
	# Shortest and longest tracks.
	if "DurationMinMax" in snapshotFlags:
		trackDurations = [track[0] for track in trackLengths]
		# #159: do not record shortest/longest tracks if the playlist consists of hour markers.
		if len(trackDurations) > 0:
			# Mark min/max duration recording lines with noqa (formatted string literal is too long).
			shortest = min(trackDurations)
			shortestIndex = trackDurations.index(shortest)
			snapshot["PlaylistDurationMin"] = "{} ({})".format(  # noqa
				trackLengths[shortestIndex][1], _ms2time(trackLengths[shortestIndex][0], ms=False)
			)
			longest = max(trackDurations)
			longestIndex = trackDurations.index(longest)
			snapshot["PlaylistDurationMax"] = "{} ({})".format(  # noqa
				trackLengths[longestIndex][1], _ms2time(trackLengths[longestIndex][0], ms=False)
			)
	if "DurationAverage" in snapshotFlags:
		# #57: zero division error may occur if the playlist consists of hour markers only.
		try:
			# Track count is an integer, so use floor division.
			snapshot["PlaylistDurationAverage"] = _ms2time(
				totalDuration // snapshot["PlaylistTrackCount"], ms=False
			)
		except ZeroDivisionError:
			snapshot["PlaylistDurationAverage"] = "00:00"
	if "CategoryCount" in snapshotFlags:
		snapshot["PlaylistCategoryCount"] = collections.Counter(categories)
	if "ArtistCount" in snapshotFlags:
		snapshot["PlaylistArtistCount"] = collections.Counter(artists)
	if "GenreCount" in snapshotFlags:
		snapshot["PlaylistGenreCount"] = collections.Counter(genres)
	return snapshot

# Output formatter for playlist snapshots.
# Pressing once will speak and/or braille it, pressing twice or more will output this info to an HTML file.
def playlistSnapshotOutput(snapshot: dict[str, Any], scriptCount: int) -> None:
	statusInfo = [
		# Translators: one of the results for playlist snapshots feature
		# for announcing total number of items in a playlist.
		_("Items: {playlistItemCount}").format(playlistItemCount=snapshot["PlaylistItemCount"])
	]
	statusInfo.append(
		# Translators: one of the results for playlist snapshots feature
		# for announcing total number of tracks in a playlist.
		_("Tracks: {playlistTrackCount}").format(playlistTrackCount=snapshot["PlaylistTrackCount"])
	)
	statusInfo.append(
		# Translators: one of the results for playlist snapshots feature
		# for announcing total duration of a playlist.
		_("Duration: {playlistTotalDuration}").format(
			playlistTotalDuration=snapshot["PlaylistDurationTotal"]
		)
	)
	if "PlaylistDurationMin" in snapshot:
		statusInfo.append(
			# Translators: one of the results for playlist snapshots feature
			# for announcing shortest track name and duration of a playlist.
			_("Shortest: {playlistShortestTrack}").format(
				playlistShortestTrack=snapshot["PlaylistDurationMin"]
			)
		)
		statusInfo.append(
			# Translators: one of the results for playlist snapshots feature
			# for announcing longest track name and duration of a playlist.
			_("Longest: {playlistLongestTrack}").format(
				playlistLongestTrack=snapshot["PlaylistDurationMax"]
			)
		)
	if "PlaylistDurationAverage" in snapshot:
		statusInfo.append(
			# Translators: one of the results for playlist snapshots feature
			# for announcing average duration for tracks in a playlist.
			_("Average: {playlistAverageDuration}").format(
				playlistAverageDuration=snapshot["PlaylistDurationAverage"]
			)
		)
	# For top artists and genres, report statistics if there is an actual common entries counter.
	if "PlaylistArtistCount" in snapshot:
		artistCount = splconfig.SPLConfig["PlaylistSnapshots"]["ArtistCountLimit"]
		artists = snapshot["PlaylistArtistCount"].most_common(None if not artistCount else artistCount)
		if scriptCount == 0:
			try:
				statusInfo.append(
					# Translators: one of the results for playlist snapshots feature
					# for announcing top artist in a playlist.
					_("Top artist: {} ({})").format(artists[0][0], artists[0][1])
				)
			except IndexError:
				statusInfo.append(
					# Translators: one of the results for playlist snapshots feature
					# when there is no top artist.
					_("Top artist: none")
				)
		elif scriptCount == 1:
			if len(artists) == 0:
				statusInfo.append(
					# Translators: one of the results for playlist snapshots feature
					# when there is no top artist (formatted for browse mode).
					_("Top artists: none")
				)
			else:
				artistList = []
				# Translators: one of the results for playlist snapshots feature,
				# a heading for a group of items.
				header = _("Top artists:")
				for item in artists:
					artist, count = item
					if artist is None:
						# Translators: one of the results for playlist snapshots feature
						# when there is no artist information.
						info = _("No artist information ({artistCount})").format(artistCount=count)
					else:
						# Translators: one of the results for playlist snapshots feature
						# for artist count information.
						info = _("{artistName} ({artistCount})").format(
							artistName=artist, artistCount=count
						)
					artistList.append(f"<li>{info}</li>")
				statusInfo.append("".join([header, "<ol>", "\n".join(artistList), "</ol>"]))
	if "PlaylistCategoryCount" in snapshot:
		categoryCount = splconfig.SPLConfig["PlaylistSnapshots"]["CategoryCountLimit"]
		categories = snapshot["PlaylistCategoryCount"].most_common(
			None if not categoryCount else categoryCount
		)
		if scriptCount == 0:
			statusInfo.append(
				# Translators: one of the results for playlist snapshots feature
				# for announcing top track category in a playlist.
				_("Top category: {} ({})").format(categories[0][0], categories[0][1])
			)
		elif scriptCount == 1:
			categoryList = []
			# Translators: one of the results for playlist snapshots feature,
			# a heading for a group of items.
			header = _("Categories:")
			for item in categories:
				category, count = item
				category = category.replace("<", "")
				category = category.replace(">", "")
				# Translators: one of the results for playlist snapshots feature
				# for category count information.
				info = _("{categoryName} ({categoryCount})").format(
					categoryName=category, categoryCount=count
				)
				categoryList.append(f"<li>{info}</li>")
			statusInfo.append("".join([header, "<ol>", "\n".join(categoryList), "</ol>"]))
	if "PlaylistGenreCount" in snapshot:
		genreCount = splconfig.SPLConfig["PlaylistSnapshots"]["GenreCountLimit"]
		genres = snapshot["PlaylistGenreCount"].most_common(None if not genreCount else genreCount)
		if scriptCount == 0:
			try:
				statusInfo.append(
					# Translators: one of the results for playlist snapshots feature
					# for announcing top genre in a playlist.
					_("Top genre: {} ({})").format(genres[0][0], genres[0][1])
				)
			except IndexError:
				statusInfo.append(
					# Translators: one of the results for playlist snapshots feature
					# when there is no top genre.
					_("Top genre: none")
				)
		elif scriptCount == 1:
			if len(genres) == 0:
				statusInfo.append(
					# Translators: one of the results for playlist snapshots feature
					# when there is no top genre (formatted for browse mode).
					_("Top genres: none")
				)
			else:
				genreList = []
				# Translators: one of the results for playlist snapshots feature,
				# a heading for a group of items.
				header = _("Top genres:")
				for item in genres:
					genre, count = item
					if genre is None:
						# Translators: one of the results for playlist snapshots feature
						# when there is no genre information for an item.
						info = _("No genre information ({genreCount})").format(genreCount=count)
					else:
						# Translators: one of the results for playlist snapshots feature
						# for genre count information.
						info = _("{genreName} ({genreCount})").format(genreName=genre, genreCount=count)
					genreList.append(f"<li>{info}</li>")
				statusInfo.append("".join([header, "<ol>", "\n".join(genreList), "</ol>"]))
	if scriptCount == 0:
		ui.message(", ".join(statusInfo))
	else:
		# Translators: The title of a window for displaying playlist snapshots information.
		ui.browseableMessage(
			"<p>".join(statusInfo),
			title=_("Playlist snapshots"),
			isHtml=True,
			closeButton=True,
		)

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
	# Timezone (tz) argument is optional (local time is used when creating transcripts file).
	transcriptTimestamp = datetime.datetime.now()  # noqa
	# Formatted string literal for transcript filename is too long (hence marked noqa).
	transcriptFilename = "{}{:02d}{:02d}-{:02d}{:02d}{:02d}-splPlaylistTranscript.{}".format(  # noqa
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
	ui.message(_("Playlist transcripts saved at {location}").format(location=transcriptPath))


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
				filteredContent.append(f"{columnHeaders[column]}: {content}")
		playlistTranscripts.append("{}{}{}".format(prefix, "; ".join(filteredContent), suffix))
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
	playlistTranscripts.append('"{}"\n'.format('","'.join([col for col in columnHeaders])))
	obj = start
	columnPos = [obj.indexOf(column) for column in columnHeaders]
	while obj not in (None, end):
		columnContents = obj._getColumnContents(columns=columnPos, readable=True)
		playlistTranscripts.append('"{}"\n'.format('","'.join([content for content in columnContents])))
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
			return super().__new__(cls, *args, **kwargs)
		return instance

	def __init__(self, parent: gui.MainFrame, obj: NVDAObject):
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

	def onTranscriptFormatSelection(self, evt: wx.CommandEvent):
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

	def onOk(self, evt: wx.CommandEvent):
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

	def onCancel(self, evt: wx.CommandEvent):
		self.Destroy()
		global _plTranscriptsDialogOpened
		_plTranscriptsDialogOpened = False

	def onAppTerminate(self):
		# Call cancel function when the app terminates so the dialog can be closed.
		self.onCancel(None)
