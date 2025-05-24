# StationPlaylist Add-on User Guide

Revision: June 2025 for StationPlaylist add-on 25.06

Author: Christopher Duffley (formerly Joseph Lee)

IMPORTANT: as of March 24, 2023, Joseph Lee no longer maintains this add-on.

## Introduction

Thank you for choosing StationPlaylist add-on for NVDA. This add-on guide is designed to get you started using StationPlaylist Studio and related applications with NVDA.

If you are new to NVDA, consult the NVDA user guide to familiarize yourself with how NVDA works and commands. If you are new to StationPlaylist (SPL) Studio or any SPL suite of applications, please read the user guides for these programs to get to know various operations available in SPL Studio and related applications.

## About the add-on and this guide

The add-on and this guide is shaped by you, the NVDA users around the world. If you wish to suggest features, report bugs or want to say hi, please use the contact information at the end of this document to contact the author.

Notes:

1. The features and commands described in this guide may change as new add-on versions are released.
2. Formerly StationPlaylist Studio add-on, the add-on has been renamed to StationPlaylist add-on in June 2019.

## What is StationPlaylist Studio

StationPlaylist Studio (oftened shortened to SPL or just Studio) is a radio broadcasting software which assists broadcasters with streaming live or recorded shows over the internet. In addition to live shows, SPL Studio assists a station with playback of songs around the clock, playing jingles at specific times and more.

## What does the StationPlaylist add-on do

StationPlaylist add-on for NVDA contains following features to support Studio and related applications:

* Announcing toggle states of various controls such as automation.
* Ability to obtain playback and other status information from within SPL Studio.
* Ability to configure status announcement verbosity.
* announcing playback time such as remaining time for the current track.
* Managing SPL Studio functions from other programs.
* Announcement of when the end of track and song intros are approaching.
* A dedicated mode to learn cart machine assignments and play carts from anywhere.
* A handy alarm to let you know your microphone has been turned on for a while.
* Playlist summarization and analysis features including viewing statistics about a loaded playlist and saving a transcript of the playlist in a variety of formats.
* A central configuration dialog to configure various add-on settings.
* Customize NVDA's behavior on a per show basis via broadcast profiles.
* Switch between broadcast profiles instantly.
* Ability to switch to SPL Studio from any program.
* Assisting with broadcasting via support for Spatial Audio's SAM encoder and StationPlaylist's own SPL encoder and others.

And so much more.

### The SPL suite

In addition to StationPlaylist Studio, this add-on comes with support for the following:

* StationPlaylist Creator (including Playlist Editor)
* Track Tool
* Remote VT client
* StationPlaylist Streamer
* SAM Encoders
* SPL Encoders
* AltaCast encoders

Certain commands will work across Studio and apps listed above, while others are specific to Studio, Track Tool, or encoders. See the sections below for details.

## Add-on requirements and versions

StationPlaylist add-on requires the following:

* An evaluation or a registered copy of StationPlaylist Studio 5.50 or later installed on a computer running Windows 10 or later.
* Optional: an evaluation or registered copy of StationPlaylist Creator and/or StationPlaylist Streamer, version 5.50 or later.
* Optional: Remote VT client
* Optional: an evaluation or registered copy of SAM Encoders.
* Optional: AltaCast Winamp plugin (one must copy AltaCast Winamp plugin DLL to Studio's plugins folder for Studio to recognize AltaCast).
* NVDA 2024.1 or later. Certain features will require later versions of NVDA.

## Installing and updating the add-on

You can install and update StationPlaylist add-on through NV Access add-on store. By default, the latest stable version of the add-on compatible with the NVDA version you are using will be listed.

Notes:

1. Installing the add-on on a computer running an unsupported version of Studio is not supported.
2. You need to disable audio ducking (NVDA+Shift+D), otherwise volume of audio from Studio will be lowered each time NVDA speaks.
3. This add-on includes touchscreen commands. To use touchscreen commands, you need a touch capable computer with at least five touch points and NVDA must be installed as portable version does not support touch commands.
4. Certain commands will be limited or disabled completely if NVDA is running in secure mode such as in secure screens. For best results, do not copy this add-on to secure screens.
5. Some add-on commands support speech on demand mode to announce information via speech while keeping other announcements silent.

### Welcome dialog

When you start Studio after installing the add-on for the first time, a welcome dialog will be presented, giving you essential information about the add-on and basic concepts. After dismissing this dialog, from Studio window, press Alt+NVDA+F1 to reopen this dialog.

## Using SPl suite with NVDA

This section describes features available when using SPL suite of applications with this add-on.

### StationPlaylist Studio

#### About add-on commands

You can use many of the native SPL Studio commands to control the program. In addition, NVDA provides additional commands (including layer commands) to read status information and to control SPL Studio from anywhere. In addition, a dedicated touchscreen mode for Studio called "SPL mode" is available on touchscreen computers to perform touch gestures.

#### The layer commands

NVDA provides two layer command sets when using Studio to perform various tasks and announce status information:

* SPL Assistant: this layer set, available from within SPL Studio, allows you to obtain various SPL status information such as whether a track is playing, automation status and so on.
* SPL Controller: this command set, available everywhere, allows you to control SPL Studio from anywhere, including playing the next track and turning microphone on and off.

We'll meet these layer commands and how to use them throughout this guide.

Note: the layer entry commands are not assigned so you can assign your own commands. So whenever you see SPL Assistant or SPL Controller, substitute your command (e.g. if you have assigned NVDA+grave accent for SPL Controller, press NVDA+Grave to access SPL Controller layer).

#### Playlist Viewer

When you start or switch to SPL Studio, you'll be placed in Playlist Viewer. This screen shows a list of tracks you have added to be played via Studio. On top of the track listings is an hour marker to tell you the tracks you have added for this hour.

For each trakc in the playlist, a check mark is available to select tracks for playback. As you select tracks in the playlist, Studio will show the total length of the playlist, useful if you wish to know if the selected track fills the current hour slot.

If you press NVDA+Up Arrow (not the numpad up arrow in desktop layout; NVDA+L in laptop layout) or NVDA+Tab, NVDA will tell you the track information such as duration, artist, whether the track is selected for playback and so on. You can also let NVDA play a beep to indicate the track category, and when you reach top or bottom of the playlist, NVDA will play a beep to let you know of this fact. You can configure these behaviors from add-on settings.

Note: for best experience, tell Studio to use accessibility mode from options dialog.

#### Track playback controlls within Studio window

You can use native SPL Studio commands to control track playback. Here is a list of the commands:

* ENTER or P: play the selected track.
* U: Pause or continue playing the track.
* S: Stop track with fade out.
* T: Instant stop.
* Alt+Down arrow: Skip to next track.

From Studio window, to see if a track is playing, press the SPL Assistant command. NVDA will play a beep. Then press P, and NVDA will announce if the track is playing or stopped.

#### Reviewing information about a track

Visually, Playlist Viewer entries are organized as a table. Each row corresponds to track entries and various information about a track (called tags) is spread across 18 columns. On the far left is a check mark that denotes whether the track is selected for playback, and one can use the mouse to reorder other columns.

You can use NVDA's table navigation commands to move between columns such as artist, duration, category and so on (termed Column Navigator). That is, you can press Control+Alt+left or right arrows to move through columns, and Control+Alt+up or down arrows to move vertically (next or previous row while staying at the column of your choosing, either the column you are reviewing or a specific column). You can also press Control+Alt+Home or End to review leftmost or rightmost column. NVDA will announce "edge of table" when you reach the edge of the track item row or the first or last trakc on the playlist viewer (the latter if you enabled top and bottom notifications).

#### Columns Explorer

Another way to review track columns is telling NVDA which columns you'd like to obtain information from. This is called Columns Explorer and is activated when you press Control+NVDA+number row when focused on a track.

By default, the following columns or slots are defined:

1. Artist
2. Title
3. Duration
4. Intro
5. Outro
6. Category
7. Year
8. Album
9. Genre
10. Mood

Note: Position 10 is 0 (zero) key. Notice that these are the first ten columns from left to right unless reordered.

To configure column slots, open add-on settings, select Columns Explorer category, then click Columns Explorer button. You'll be greeted with ten combo boxes (one per column slot) where you can select columns you'd like to explore when Control+NVDA+column slot (1 through 0) keys are pressed.

#### Customizing column announcements

By default, NVDA will announce all available information about a track. However, you can ask NVDA to not announce certain columns, change column announcement order, or prevent announcement of column header text such as Artist, Genre and so on.

To customize column order or exclude certain columns from being announced, open add-on settings, then navigate to Column Announcements category. After unchecking "Announce columns in the order shown on screen" checkbox, customize custom column inclusion and/or order as follows:

* Column inclusion: from a list of column checkboxes, check or uncheck columns you wish NVDA to announce or suppress, respectively.
* Column order: This list shows column announcement order. Use up/down buttons to change column order position for the selected column.

To let NVDA only announce column content, from NVDA's document formatting settings panel, uncheck "Row/column headers". With the setting turned on, NVDA may say things such as, "Artist: artist name", otherwise NVDA will say, "artist name".

Notes:

1. To return to default behavior of announcing columns in screen order and/or announce all columns, from Column Announcements category in add-on settings, check "Announce columns in the order shown on screen". Artist and title are always announced.
2. You can quickly toggle screen versus custom column order announcement for track columns by pressing NVDA+V while focused on a track in Studio's playlist viewer.
3. To make column header announcement setting applicable in Studio, create a configuration profile (either manually activated or an app-specific profile for Studio).

#### Track comments

In case you receive a request from someone and need to write it down, you can use track comments feature to add, change, review or remove comments (notes) for tracks. As you move through tracks, you may hear NVDA say, "has comment" or play a beep to indicate existence of a track comment for the selected track. Press Alt+NVDA+C to let NVDA announce track comments if any, or press it twice to copy track comment to the clipboard so you can review it from somewhere.

To add a track comment, press Alt+NVDA+C three times. Type your comment and press ENTER. Leaving the track comment empty will remove track comments.

Note: You cannot add track comments to hour markers, break notes and other such tracks.

#### Listener requests

From time to time, listeners may chime in and request a track or two to be played. Provided that you are using the StationPlaylist request scripts on your website, you can be notified of request arrival. When this happens, NVDA will play a beep to notify you of this. Once requests arrive, press Control+Q from StationPlaylist to open requests window.

Note: in order to use this, StationPlaylist must be set to pop up requests window when requests arrive.

#### Playlist and time information

As you work with SPL Studio, the following commands are available to obtain various information about current playlist and the currently playing track:

* Alt+Shift+T: announces elapsed time for the currently playing trakc.
* Control+Alt+T: Announces the remaining time for the currently playing track.
* NVDA+Shift+F12: Announces broadcaster time (time as reported by Studio such as 5 minutes to 2). Pressing this command twice will announce minutes and secondsl eft until top of the next hour.
* SPL Assistant, H: Announces the duration of the playlist for the hour slot.
* SPL Assistant, Shift+H: Announces remaining track duration for the current hour slot.
* SPL Assistant, O: Announces playlist hour over/under by (example: +02:00).
* SPL Assistant, P: Announces whether a track is playing.
* SPL Assistant, C: Announces the title of the currently playing track and playback player, if any.
* SPL Assistant, N: Announces name and duration of the next track if selected, as well as the player that will be used to play the track.
* SPL Assistant, S: Announces the time when the selected track will be played (scheduled).
* SPL Assistant, Shift+S: Announces length of time before the current track will play (i.e. starts in; you should use this command about a second after moving to a new track).
* SPL Assistant, D: Announces duration of the remaining tracks in the playlist (may become inaccurate (up to several seconds) for very long playlists).
* SPL Assistant, Y: Announces whether the currently loaded playlist has been modified.
* SPL Assistant, F8: Takes a snapshot of the current playlist and presents information about the playlist on a window. These include total duration of the playlist (from start to finish), name of the longest track, number of categories and so on.
* SPL Assistant, Shift+F8: transcribes playlist data in a number of formats. See Playlist Transcripts section for details.

In addition, you can assign a command via NVDA's Input Gestures dialog to announce time in hours, minutes and seconds as reported by Studio.

Note: for current and next track commands, you can ask NVDA to announce internal player used for playback, as Studio uses multiple internal players for track playback.

#### Setting options and announcing option status

Besides track and time information, NVDA allows you to use native Studio commands to change various options such as microphone on or off, automation and so on. As you change these options, NVDA will announce new values either as words or beeps. To change these options, use the Studio commands as follows:

* A: Toggle automation.
* L: Line-in.
* M: Microphone on/off.
* N: Microphone on/off without fade.
* R: Enable or disable record to file.
* Control+T: Cart edit/insert mode on or off. If status message is set to beeps and if cart insert mode is active, you will hear "insert" when you press this command and status changes to cart insert mode on.
* Control+D: Control keys enable/disable (Studio 6.10 and later).

To announce current values for these options, enter SPL Assistant layer, then press the corresponding native command from the list above (except where noted). For example, to hear if automation is enabled, enter SPL Assistant then press A.

Additional commands and exceptions for SPL Assistant layer include:

* U: Studio up time.
* T: Cart edit mode status. To change cart edit mode status, press Control+T (Control+T is a Studio command).
* I: Listener count (I as in "Internet listeners").
* Control+K: Drop a place marker on the selected track.
* K: Move to a predefined marker track. See place marker section for more details.
* Shift+P: Pitch for the current track.
* Shift+R: Report library scan results (number of items scanned) or track current library scan in the background.
* W: Weather and temperature (see below).
* F1: Shows a dialog listing available layer commands.
* F9: Mark the start of track time analysis.
* F10: Performs track time analysis. See track time analysis section for more details.
* F12: Switches between current and an instant switch profile. See instant switch profile section for more details.

Note: When the microphone is turned on with or without fade, pressing M from SPL Assistant will tell you the current microphone status.

#### SPL Assistant command layout

NVDA isn't the only screen reader with scripts for Studio. There are scripts for JAWS for Windows and Window-Eyes that provides similar functionality to NVDA add-on.

The SPL Assistant layer commands described throughout this guide are the default commands when the add-on is first installed. You can change SPL Assistant command layout between NVDA (default) and JAWS by going to Advanced Settings in add-on settings dialog.

Following are SPL Assistant command assignments when JAWS for Windows layout is active:

* C: Cart Explorer (you can toggle this by pressing Alt+NVDA+3).
* L: Listener count.
* R: Playlist duration.

Other SPL Assistant commands described in this guide are same across all layouts.

#### Playlist Analyzer

These allow you to obtain information about a loaded playlist, including total running time, top genre, storing playlist data to a file and others. You can perform these functions on an entire playlist or a portion of it.

The Playlist Analyzer features include:

* Track time analysis: announce total duration of part of a playlist.
* Playlist snapshots: present information about the playlist or a part of it, including top artist, total and average duration of tracks loaded and others.
* Playlist transcripts: view, copy, or store playlist data in a variety of formats to the clipboard or files.

Note: playlist analysis range is defined by presence of playlist analysis marker (if not defined, the entire playlist will be analyzed, otherwise a partial analysis will take place). To limit analysis scope, move to the starting track and press SPL Assistant, F9. Then move around the playlist until you come across another item, then perform an analysis command (see below). To analyze an entire playlist, clear playlist analysis marker by entering SPL Assistant, then press F9 twice quickly, or for playlist transcripts, select "entire playlist" when asked to define transcript range.

##### Track time analysis

If you are unsure as to length of time required to play selected tracks, you can ask NVDA to perform track time analysis. First, move to the starting track, then press SPL Assistant, F9 to mark the track as start analysis marker. Then move to the last track and press SPL Assistant, F10. NVDA will announce number of tracks followed by total length of the selected tracks. Analysis can be performed even if you select tracks backwards (that is, if you wish to count total length of the tracks prior to the marked track).

Note: You can assign a custom command for time analysis (SPL Assistant, F10). Track time analysis will not work properly outside of playlist viewer.

##### Playlist snapshots

While planning a show, it is sometimes helpful to get a glimpse of your currently loaded playlist to find out the current longest track, number of hour markers and so on. If you have a long playlist that spans hours, it becomes tedious to write down information for each track and calculate various statistics such as average duration of all tracks.

NVDA can do this task when you tell it to do so. Pressing SPL Assistant, F8 while focused on any track in the playlist will allow NVDA to "take a snapshot" of your current playlist and present various statistics on a window. Alternatively, if you wish to take a partial playlist snapshot, move to the starting track and mark it as analysis marker, then move to the last track and the press SPL Assistant, F8.

By default, the following playlist information will be shown:

* Number of items (including tracks, hour markers, break notes and so on) in the playlist.
* Total duration of the playlist.
* Name and duration of the longest and shortest tracks.
* Average duration of all tracks in the playlist.
* Top categories.
* Top artists by track count.
* Music genres represented.)

You can configure snapshot information from add-on settings via playlist snapshots category. This screen houses checkboxes and several number edit fields to specify what information will be gathered when taking a playlist snapshot.

Note: For category, artist, genre and album count, you can ask NVDA to show you up to top ten results, or show all results by setting show count setting to zero (0). After reviewing snapshot information, press escape to close the snapshots window.

##### Playlist transcripts

If you wish to view playlist data in a variety of formats (such as an HTML table) or store this information to a file, you can do so with playlist transcripts. In this context, a "transcript" is record of the loaded playlist - either a part of it or the entire playlist.

To request a playlist transcript, press SPL Assistant, Shift+F8. NVDA will then ask for playlist range, transcript format, as well as other options for specific formats, including copying data to the clipboard. After selecting a transcript range and format, select OK, and NVDA will generate a playlist transcript so you can either view it (on a separate screen), paste it somewhere (if copied to the clipboard), or open the transcript file.

The available transcript ranges include:

* Entire playlist.
* To and from current track: from start of the playlist to the current track, or from current track to the end.
* Current hour.

The available transcript formats include:

* Plain text: a record of the playlist in a form announced by NVDA.
* HTML table: the playlist is shown as a table.
* HTML list: similar to plain text option except each track is a list item.
* Markdown table: each column data is surrounded by vertical bars (|) and is formatted for viewing or converting to other formats.
* Comma-separated values (CSV): a popular tabular data exchange format, suitable for opening the CSV file in programs such as Excel for further processing.

All formats listed above will let you view transcripts in a browse mode window or save it to a file. In addition, transcripts in plain text, Markdown table, and CSV formats can be copied to the clipboard.

In addition to viewing transcripts in a variety of formats, you can customize which columns are included and in which order. This can be done via Playlist Transcripts category found in add-on settings. From there, select columns to be included by checking various checkboxes and/or rearrange the presentation order. By default, all columns are included (except status column) and is shown according to default column presentation order as seen by NVDA.

Note: if NVDA is running in secure mode, you cannot copy transcripts to the clipboard or save it to a file.

#### Status announcements

Sometimes, you might find that NVDA might be too verbose when announcing status information such as toggling automation from the main playlist window. You can ask NVDA to play beeps instead of announcing status for these options while toggling them.

To change this (which will become permanent), open SPL add-on settings, go to General Add-on Settings dialog, then select Beep for status announcements checkbox. When you change status announcements to beeps, NVDA will play beeps to indicate events such as toggling microphone, end of track announcements and so on. These settings will also work if you are using SPL Controller to toggle Studio options (see below).

#### Message verbosity

When status such as automation changes, you may not wish to hear the complete announcement. If you would like to hear just enough information, you can change message verbosity from add-on settings dialog under General Add-on Settings.

There are two verbosity levels to choose from:

* Beginner: Gives you more verbose information such as which status has changed. For example, when you press A from playlist viewer, you will hear "Automation On/Automation Off".
* Advanced: Announces just enough information to let you know something has changed. For example, press A from playlist viewer to hear NVDA say "On" or "Off". In this case, you'll know that you've changed automation status.

Note: If you set status announcement to beeps, you'll hear a longer tone when verbosity is set to beginner, and a short tone will be played otherwise (exceptions include microphone alarm). Also, cart edit/insert mode toggle isn't affected.

#### Track and microphone alarms

You can ask NVDA to alert you when a track is ending, end of track intro is approaching, or when microphone is on. The first two are collectively known as "track alarms" and the third is microphone alarm.

You can ask NVDA to either play a beep, announce a warning or do both when end of track (outro) or intro is approaching. By default, NVDA will play a beep when five seconds are left on the outro and intro. In contrast, microphone alarm is useful when you wish to know if a microphone is active. you can ask NVDA to play a beep once when the microphone is turned on, or play a periodic reminder as long as microphone is active, with NVDA set to never do this by default.

To configure these three alarms, press Alt+NVDA+1 to open Alarms settings category in SPL add-on settings screen. From here you can configure:

* Track outro alarm toggle and alarm value in seconds: by default NVDA will notify you five seconds prior to end of a track. You can configure this value between 1 and 59 seconds, or turn this off by unchecking "notify end of track alarm" checkbox.
* Track intro alarm toggle and alarm value in seconds: by default, five seconds before end of track intros, NVDA will play a beep to let you know of this fact. You can configure this value between 1 and 9 seconds, or turn this off by unchecking "notify song ramp alarm" checkbox.
* Microphone alarm: this option will let NVDA play a beep when microphone is turned on. By default, NVDA will not do this (value is 0). You can configure this between 0 (off) and 60 seconds.
* Microphone alarm interval: in addition to playing microphone alarm, NVDA can notify you periodically if microphone is active. You can configure this between 0 (off by default) and 7200 seconds (two hours). If microphone alarm is off, alarm interval will be disabled.
* Alarm notification (beep by default): NVDA can announce end of track and song intro alarms using beeps, a message, or both.

Note: alarm settings are saved to the active broadcast profile. See broadcast profiles section for details.

#### Braille Timer

If you are using a braille display, you can ask NVDA to display remaining time for the track and/or its intro on a braille display. Press Control+Shift+X to step through braille timer options. Alternatively, select the desired option from the add-on configuration's braille timer combo box. You can choose from braille timer off (default), braille track endings, braille intro times or braille both track endings and intro times. Note that you need to be in Studio window in order to see time on a braille display, and NVDA will remember this setting even when it restarts.

#### Time range finder

If you need to fill an hour slot with a track, you can find one by using time range finder. To use this, first assign a command to open this dialog, which consists of two groups of edit spin boxes (minimum and maximum duration, respectively), with each group composed of two spin controls for minute and second. Once you define the duration range, press ENTER and NVDA will either place you on a track or tell you if there aren't any tracks with duration within the just defined range.

#### Track finder

If you are focused on the track list and wish to find a track (by artist name or by song title), you can use track finder to locate the desired track. To find tracks, press Control+NVDA+F (or SPL Assistant, F), then type the part of the name of the track into the editable combo box that appears. NVDA will locate the track with the given name, or if it cannot find it, will alert you that it cannot do so.

If you have searched for a track before, press NVDA+F3 to find forward or NVDA+Shift+F3 to find backward. You can also choose to search a previously entered term from Track Finder dialog's text entry combo box.

Note: Track search terms are case-sensitive.

#### Column Search

Track Finder is not limited to searching for artist or title. You can ask NVDA to find certain information from columns. To activate this, first assign a command to open column search, then press the newly assigned command to open Column Search dialog.

This dialog includes the following:

* Search field: enter the information you wish to find in a column or choose a term you've searched before.
* Columns: This combo box allows you to specify which column you wish to search for the entered information.

Note: Pressing NVDA+F3 or NVDA+Shift+F3 will continue to search artist and title.

#### Place marker track

There are times when you need to mark a track to return to after editing a playlist. NVDA allows you to define a track as a place marker track so you can return to it later.

To define a place marker track, press SPL Assistant, Control+K. NVDA will say, "place marker set". To return to the marked track, press SPL Assistant, K.

Note: You cannot set a breaknote or hour marker as place marker track, and if you delete the place marker track, place marker will be gone. Place marker commands will not work outside of playlist viewer.

#### Cart Explorer

SPL Studio allows you to assign up to 96 carts, or jingle machines. When the cart command is pressed, Studio plays the assigned jingle. You can also edit jingle assignments while cart edit mode is active.

The cart commands are:

* F1 through F12 either by themselves, or in combination with Shift, Control or Alt (e.g. F2, Shift+F11, Control+F5, Alt+F12).
* Number row from 1 through 9, 0, hyphen (-) and equals (=) either by themselves or in combination with Shift, Control or Alt (e.g. 5, Shift+-, Control+=, Alt+0). This set is unavailable in Studio Standard.

Hint: because Alt+F4 is a cart command, press Control+Alt+X to quit SPL Studio.

Note: The modifier assigns carts to "banks". There are four cart banks included with SPL Studio: main (without modifier), and one each for shift, control (CTRL) and alt. You can access each cart bank from the menu bar.

To help you learn what jingle will play when a given cart key is pressed, NVDA allows you to explore cart assignments. Press Alt+NVDA+3 to enter Cart Explorer. When you press the cart key once, NVDA will tell you which jingle is assigned to that cart key. When pressed twice, the jingle associated with the cart command will be played. Once you've explored the cart assignments, press Alt+NVDA+3 to leave Cart Explorer.

Hint: If you toggle cart edit mode or use cart insert mode, NVDA will remind you that Cart Explorer is active if this is such a case. Also, if you are using Studio Standard and press number row keys (with or without modifiers) while cart explorer is active, NVDA will alert you that the cart command is unavailable.

Note: Cart explorer will not operate properly if:

1. Either you have custom names for your carts or saved your cart with a different name, or loaded other cart banks besides your own. Cart explorer will not pick up cart names for additional cart banks you insert into a cart bank (main, shift, control, alt). For example, if you have cart assignments for main cart bank and add cart entries from another user's main cart bank, cart explorer will not announce cart assignments from the added cart bank. For best results, do not load another cart bank apart from your own, or if you are the only user, do not add any other banks besides default user's cart banks.
2. If one or more cart banks doesn't exist or your user name starts or ends with whitespace (" "). If this is the case, NVDA will report that some cart banks were not found and will not enter cart explorer.

#### Music Library scan

As your music collection grows, you might wish to teach Studio where it can find tracks for your shows. To help you with this, Studio has an option to remember where you've stored your music files. This can be access from Studio's options dialog under folder name section. Then, you can start a library scan right away or open insert tracks dialog to start a scan.

If using Options dialog method, once you've selected your music directory, Studio will scan the folder location for available tracks once you close the Options dialog. If using Insert Tracks dialog (Control+I) method, once the dialog opens, press Control+Shift+R to start a fresh library scan. You can then close insert tracks dialog so Studio can scan the library in the background. In either case, depending on library scan announcement setting (see below), NVDA will be silent while Studio is scanning the library, or NVDA may announce scan progress periodically.

To toggle library scan announcement options while scanning the library from inser tracks window or in the background, press Shift+NVDA+R (R for rescan) from Studio window. This command will cycle through the options listed below. Alternatively, from the add-on configuration dialog, open general add-on settings, then select an option from the library scan announcement combo box.

The available options are:

* Do not announce ("off"): by default, NVDA will not announce that a library scan is happening.
* Announce start and end of a scan ("start and end only"): NVDA will notify you when a library scan starts and ends.
* Announce progress of a scan ("scan progress"): In addition to start and end announcement, NVDA will say "scanning" periodically to tell you that a library scan is in progress.
* Announce progress and number of items scanned ("scan count"): NVDA will announce number of items scanned so far as the scan takes place.

Note: words in parentheses are the options from the scan announcement combo box.

Hint: If you set status announcement to beeps, NVDA will play a high and low tone when the scan starts and completes, respectivley. Also, NVDA will play a middle tone during a scan to alert you that a scan is happening.

Note: to monitor the progress of a library scan from insert tracks window, do not move away from Insert Tracks dialog until the scan is complete. This does not apply if you start library scan monitoring via Studio Options dialog method, as NVDA will announce scan progress from any program including from within Studio. Also, if library scan progress is set to scan count, you may hear repeats. Don't worry - this is the case when it takes a long time to perform library scans.

#### Weather and temperature

You can ask Studio to show you temperature and weather information for your local area. Once this is configured, from SPL Assistant, press W. Alternatively, assign a command to announce weather and temperature without invoking SPL Assistant.

#### Metadata streaming

You can ask Studio to use up to five streams to stream track metadata. These include the DSP encoder address and up to four additional URL's, and NVDA can be told to announce if metadata streaming is enabled and connect to predefined servers if any.

To configure when NVDA should announce metadata streaming status and connect to these servers, open add-on settings, select metadata streaming category, and select an option from metadata streaming notification and connection combo box. You can choose between off (not announced and connected), startup (connected and announced when Studio starts) and when switching to an instant switch profile (see instant switch profile section for more details).

To configure which streams should be enabled, go to manage metadata streaming, then check the boxes for streams you wish to connect.

To quickly enable or disable metadata streaming on the fly, press the command you assigned to open metadata streaming options dialog. Check the stream box to enable or uncheck to disable metadata streaming and click OK.

Note: When toggling metadata streaming on the fly, you can check "Apply to selected profile" checkbox to let NVDA store toggle values to the selected profile to be used next time Studio starts. This checkbox is disabled if NVDA is running in secure mode.

#### Using touchscreen commands

If you have NVDA installed on a touchscreen computer, you can use touchscreen gestures to perform some add-on commands. These commands are grouped under a touch mode called "SPL mode". While Studio is focused, perform three finger single tap until you switch to SPL mode.

The commands in SPL mode are as follows:

* Two finger flick left: open alarms settings.
* Two finger flick up: announces broadcaster time.
* Two finger flick down: announces remaining time for the currently playing track.

Note: When you switch away from Studio, you'll be placed in object touch mode.

### Other programs in SPL suite

In addition to StationPlaylist Studio, SPL suite includes Track Tool, Creator, and Remote VT client. Track Tool is typically used to set intros, define cue positions and so on for a track. Creator is useful if you wish to create advanced playlists such as rotations and more interesting track categories. Remote VT client is used by broadcasters to manage a station's playlist remotely.

#### Track Tool

To use Track Tool, highlight a track from within Studio's track list, then press Control+K. Alternatively, press Control+K without selecting any track, then from within Track Tool window, press Control+O to load a track into Track Tool. As you move through the tracks list, you'll hear a beep if intro has been set on a track. NVDA will also tell you the values for cue, overlap and so on if they are set.

From within Track Tool, press Control+NVDA+number to hear various information about the selected track. For example, press Control+NVDA+3 to obtain track duration. Alternatively, use table navigation commands to review column information (Control+Alt+left/right to move between columns, for example).

Following are the information you can query regarding a track in Track Tool:

* Control+NVDA+1: Artist.
* Control+NVDA+2: Track title.
* Control+NVDA+3: Duration of the selected track.
* Control+NVDA+4: Cue time.
* Control+NVDA+5: Overlap duration.
* Control+NVDA+6: Length of the intro.
* Control+NVDA+7: Segue.
* Control+NVDA+8: Path to the file.
* Control+NVDA+9: Album
* Control+NVDA+0: CD code for this track.

#### StationPlaylist Creator

Similar to Track Tool, after loading a playlist or tracks with a given category, you can use table navigation commands (Control+Alt+left arrow/right arrow/up arrow/down arrow/Home/End keys) to review items in a track, or use Columns Explorer to review data from a specific column.

Following are the information you can query regarding a track in SPL Creator:

* Control+NVDA+1: Artist.
* Control+NVDA+2: Track title.
* Control+NVDA+3: Track position.
* Control+NVDA+4: Cue time.
* Control+NVDA+5: Length of the intro.
* Control+NVDA+6: Length of the outro.
* Control+NVDA+7: Segue.
* Control+NVDA+8: Duration of the selected track.
* Control+NVDA+9: Last scheduled date and time.
* Control+NVDA+0: How many times the track was played in the last 7 days.

#### Creator Playlist Editor and Remote VT client

Both Creator's playlist editor and Remote VT client lets you manage playlists for a station. The differences are where the station is hosted (local for Creator, remote for VT client), along with ability to record voice tracks for a remote playlist in Remote VT client which affects the length of a playlist.

Track information shown differs across SPL Creator's Playlist Editor and Remote VT client versions. Following are track information shown in Creator's Playlist Editor and Remote VT client once a remote playlist is loaded:

Versions 5.50 and 6.0x:

* Control+NVDA+1: Artist.
* Control+NVDA+2: Track title.
* Control+NVDA+3: Duration of the selected track.
* Control+NVDA+4: Length of the intro.
* Control+NVDA+5: Length of the outro.
* Control+NVDA+6: Category.
* Control+NVDA+7: Year.
* Control+NVDA+8: Album.
* Control+NVDA+9: Genre.
* Control+NVDA+0: Mood.

Version 6.1x:

* Control+NVDA+1: Scheduled time.
* Control+NVDA+2: Artist.
* Control+NVDA+3: Track title.
* Control+NVDA+4: Duration of the selected track.
* Control+NVDA+5: Length of the intro.
* Control+NVDA+6: Length of the outro.
* Control+NVDA+7: Category.
* Control+NVDA+8: Year.
* Control+NVDA+9: Album.
* Control+NVDA+0: Genre.

In addition, Playlist Editor in creator and Remote VT client includes the following commands:

* Alt+NVDA+1: Date and time for the playlist.
* Alt+NVDA+2: Duration of the playlist.
* Alt+NVDA+3: Date and time for when the selected track is scheduled to play.
]* Alt+NVDA+4: Playlist category and rotation.

## Studio add-on preferences

One of the strengths of NVDA is that it contains gateways for configuring various settings, such as voice, browse mode and so on, all housed in the multi-page Settings screen located in preferences menu. Just like any other settings, SPL add-on comes with its own settings dialog. As long as you are running Studio, you can open this dialog by going to NVDA's preferences menu and selecting "SPL add-on settings" item or pressing Alt+NVDA+0 (zero) from Studio window.

When add-on settings opens, a list of settings categories will be shown on the left, with settings for the selected category on the right. Select a category from list of categories, or to move between categories, press Control+Tab or Control+Shift+Tab. After configuring settings, select OK to save settings and close the dialog, or select Apply button to save settings and keep the dialog open. To discard changes, select Cancel.

Most of the settings in this dialog were discussed throughout the add-on guide. Here is a complete list of available settings and their options (some settings are unavailable if NVDA is running in secure mode):

* General add-on settings: home to a number of general options, including:
	* Beep for status announcements (unchecked by default): See status announcement section. Status messages can be announced as beeps or words when this option is checked or unchecked, respectively.
	* Message verbosity (beginner by default): See message verbosity section for more details and an entry in frequently asked questions for a complete list of messages that'll be affected by this setting.
	* Braille timer (off by default): select the desired braille timer option from this combo box. See braille timer section for more details.
	* Library scan announcement (off by default): select the announcement option from this combo box. See library scan section for more details.
	* Announce hour values when announcing track or playlist duration (on by default): If duration of the track or a playlist exceeds one hour, NVDA will announce minutes and seconds or hours, minutes and seconds when this option is disabled or enabled, respectively.
	* Vertical column navigation announcement (currently reviewing column by default): When you move through columns vertically, you can ask NVDA to keep you on the column you are currently reviewing or announce a specific column. Choose the option or the column you want from this combo box.
	* Beep for different track categories (disabled by default): Enabling this option allows NVDA to play different beeps for different track categories when moving between tracks in playlist viewer. See playlist viewer section for details.
	* Track comment announcement (off by default): Select how NVDA will notify you of track comments if it exists. You can choose from off, message, beep or both. See track comments section for details.
	* Notify when located at top or bottom of playlist viewer (enabled by default): If this is turned on, a beep will be heard when you are at the top or bottom of the playlist.
	* Play a sound when listener requests arrive (enabled by default): if checked, NVDA will play a beep to indicate request arrival. See listener requests section for details.
* Alarms: This category allows you to configure various alarm options, including:
	* Track outro, intro alarms and notification toggle, microphone alarm and interval. See track and microphone alarms section for details.
	* Alarm notification (beep by default): Selects alarm notification type. You can select from beep only, message only or both. See alarms section for more details.
* Playlist snapshots: select this category to configure information to be gathered when you issue playlist snapshots command. See playlist snapshots section for details.
* Metadata streaming: includes options for metadata streaming such as:
	* Metadata streaming notification and connection (off by default): controls when Studio will connect to and announce metadata streaming status. You can silence this (off), have Studio connect to streams and announce this when it starts, or whenever you switch to and from instant switch profiles.
	* Metadata streams list: a list of five checkboxes used to toggle metadata streaming for DSP encoder and up to four additional streams. See metadata streaming section for details.
* Column announcement: handles column announcements such as column order. Settings in this category include:
	* Announce columns in the order shown on screen (enabled by default): if checked, NVDA will use column order as shown on screen when announcing track columns (applicable to Studio's playlist viewer only). To use custom column order and/or exclude certain columns from being announced, uncheck this checkbox.
	* Column inclusion and/or order: check or uncheck columns to be announced and/or customize the announcement order. See column announcements section for details.
* Columns explorer: The three buttons in this category opens dialogs where you can configure columns explorer slots when you use Studio, Track Tool, or SPL Creator. See Columns Explorer section for details.
* Playlist Transcripts: you can configure various settings related to Playlist Transcripts feature, including which columns to include and column order. See Playlist Transcripts section for details.
* Status announcement: this category contains four checkboxes to configure announcement of certain status information. These include announcing scheduled time for the selected track, listener count, name of the currently playing cart and position of the player used for playing the current and the next track.
* Advanced (unavailable in secure mode): This category allows you to configure various advanced options. These include:
	* Use SPl Controller to invoke SPL Assistant (disabled by default): If you check this box after assigning a command to invoke SPL Controller layer (see below), you can use SPl Controller command you assigned to invoke SPl Assistant layer. This is useful for people used to other screen readers where a single layer is used to access functions normally performed by both Controller and Assistant layers in NVDA.
	* Assistant layer layout (NVDA by default): By default, NVDA will use the Assistant layer commands described throughout this user guide. You can choose between this default command set and JAWS for Windows, with layer commands used by these screen reader scripts replacing commands in the SPL Assistant layer. For example, with JAWS for Windows layout active, pressing SPL Assistant, R will announce playlist duration (default is SPL Assistant, D). See the list below for SPL Assistant command changes between layouts.

After configuring the above settings, select OK from main settings dialog to save your changes, Cancel to discard them, or Apply to apply changes without closing the settings dialog.

Notes:

* You can use this dialog to reset add-on settings and other data to default values (applied to all profiles). To do this, ggo to Reset category, select Reset settings button, check the checkboxes for various data items (instant switch flag, encoder settings and track comments), then answer yes when prompted. If no checkboxes are checked, only add-on settings will be returned to defaults. The add-on configuration dialog will close automatically once default settings are applied. Reset category is unavailable if NVDA is running in secure mode.
* If you attempt to reset settings while an instant switch profile is active, you'll be asked to confirm once more. If you say "no", settings won't return to defaults.

## Broadcast profiles

Note: the following section isn't applicable if broadcast profiles are disabled via command-line switches (see FAQ's), and you cannot create, copy, rename, delete, or configure instant switch status for profiles if NVDA is running in secure mode.

You can customize NVDA settings to be applied while using a program or during say all. This is called "configuration profiles". By default, you would use normal configuration, and you can create new profiles to be used anywhere or when using an app. Consult NVDA's user guide on configuration profiles.

StationPlaylist add-on takes this one step further. If you host multiple shows, you can ask NVDA to honor your Studio add-on preferences while broadcasting a particular show. This is achieved via broadcast profiles, a collection of settings to be applied in a given moment upon request.

So far, we've dealt with only one profile: normal profile. By default, NVDA uses default broadcast profile when adjusting settings. You can then use this profile to create new profiles based on this profile, or create a new profile with default settings applied.

As of add-on 21.04, the following settings can be stored in profiles:

* End of track notification toggle.
* End of track alarm.
* Intro notification toggle.
* Intro alarm.
* Microphone alarm.
* Microphone alarm interval.
* Announce columns in the order shown on screen.
* Column announcement order and included columns.
* Metadata streaming URL's.

Broadcast profiles are managed from SPL broadcast profiles dialog, accessed by pressing Alt+NVDA+P. Profile-related controls are as follows:

* Broadcast profile: Lists currently loaded profiles. By default, normal profile is in use (top of the list), with the active profile selected by default. For each profile, a flag will be shown alongside the profile name denoting current profile status, such as whether this profile is the currently active profile. See the next list for more information.
* Activate: activates the selected profile. Alternatively, pressing Enter from broadcast profile list will activate this button. This button will show up if the selected profile is different from the active profile.
* New (disabled in secure mode): Allows you to create a brand new broadcast profile with default profile-specific settings applied. Profiles are saved into a folder in the add-on folder.
* Copy (disabled in secure mode): Allows you to create a new profile using settings from an existing profile.
* Rename (disabled in secure mode): Lets you rename a profile (not available for normal profile).
* Delete (disabled in secure mode): Deletes a profile (say "OK" when prompted; you cannot delete the normal profile).
* Triggers (disabled in secure mode): Configure profile activation and other settings. See the triggers dialog section for details.

The possible profile flags are:

* Active: The selected profile is the active profile. This is set regardless of whether this profile became active when instant profile switching was invoked (see below).
* Instant switch: The selected profile is set as the instant switch profile (see instant switch profile for details).

Note: Multiple flags can be set on certain profiles.

### Creating a broadcast profile

Note: you cannot create or copy profiles in secure mode.

There are two ways of creating a broadcast profile: brand new or as a copy. Select the desired option and answer the following questions when the new/copy profile dialog appears:

* Profile name: Enter the profile name, such as the name of a show you are hosting. You cannot enter a name that is already in use.
* Base profile (when copying a profile): Select the profile that'll become basis for the new profile. Settings from the selected base profile will be copied to the new profile. For brand new profiles, settings from normal configuration minus profile-specific settings will be applied.

### Renaming and deleting broadcast profiles

Note: you cannot rename or delete profiles in secure mode.

To rename a profile, select "rename" button, then enter the new name for the profile. Just like new profiles, you cannot enter a name that is already used.

To delete a profile, select "delete" button, then say "OK" when prompted. You'll be returned to add-on settings with the normal profile activated.

Note: You cannot rename or delete the normal profile.

### Triggers dialog

Note: triggers dialog is disabled in secure mode.

The triggers dialog is used to configure profile switching settings. The following controls are available:

* This is an instant switch profile (checked if this is the case): If you need to use a profile during a show (especially when you don't know the duration of this show), it is best to define the show profile as instant switch profile. Once defined, you can press SPL Assistant, F12 to switch between current and show profile.

Note: if you rename the switch profile, the switch profile setting will carry over to the just renamed profile. If you delete the selected profile, instant switching setting will become undefined.

## SPL Controller

Note: SPL Controller is disabled if NVDA is running in secure mode such as in secure screens.

The SPL Controller is a set of commands used everywhere (except Studio itself) to control various aspects of Studio's functionality. For example, you can use this to start playing the next track right after a Skype call, or disable automation for the time being while conducting a live interview or tweeting.

To use these commands, enter SPL Controller layer. NVDA says, "SPL Controller." Then press the keys for the desired function from the list below.

### SPL Controller commands

after entering SPL Controller, press one of the following commands:

* A: Turn automation on.
* Shift+A: Turn automation off.
* M: Turn on microphone.
* Shift+M: Turn off microphone.
* N: Turn on microphone without fade.
* L: Turn on line-in.
* Shift+L: Turn off line-in.
* P: Play the next track.
* U: Pause or continue playing.
* S: Stop with fade out.
* T: Instant stop.
* Function keys and number row keys (with or without modifiers): play assigned carts (carts without borders).

Notice that the commands are same as SPL control commands available while SPL Studio is used. Also, the toggle commands by themselves enables a particular option, while pressing shift with the toggle key disables it (except when playing carts via SPL Controller).

Additional SPL Controller commands include:

* R: Announce remaining time for the currently playing track in seconds.
* Shift+R: announce number of tracks in the library or library scan progress (if this is happening) along with number of items scanned.)
* E: Announce connection status for active encoders if any.
* I: Announce listener count.
* Q: Announce various Studio status info. These include track playback status, automation, microphone, line-in, record to file, and cart edit/insert mode toggle.
* C: Name and duration of the currently playing track (if any).
* Shift+C: Name and duration of the upcoming track (if any).
* H: Shows a dialog listing available Controller commands.

Note: SPL Controller, E and Q can be assigned to a different command from Input Gestures dialog.

###Carts without borders

In addition to playing carts when focused on Studio and learning about their assignments (see Cart Explorer section for details), you can play cart keys after entering SPL Controller. To do this, enter SPL Controller layer, then press the cart key.

## Quickly switch to SPL Studio

There are times when you might wish to switch quickly to SPL Studio from other programs (for example, if you wish to search a song from the playlist). To switch to SPL Studio from another program, press the command you assigned for this command (for 2.0 and above; for 1.2 and earlier, press NVDA+Shift+grave accent).

Note: you cannot switch to Studio window from other programs if NVDA is running in secure mode such as in secure screens.

## Broadcasting with stream encoders

Now that you know about how to use Studio, it's time to make your presence known on the internet. You can broadcast your show online using Studio, a stream encoder and a streaming server.

StationPlaylist add-on supports various stream encoders, including SAM Encoder from Spatial Audio, SPL Encoders which ships with Studio, and AltaCast, a free stream encoder. SAM and AltaCast Encoders are Winamp plug-ins that encodes your show to a format ready for broadcasting. A popular streaming protocol/server is SHOUTcast, and you can use SHOUTcast servers from various websites to stream your show (you can try it out by installing SHOUTcast server on your local computer). Consult the documentation for Studio, SAM Encoders, AltaCast and other websites to learn more about how to stream your show online.

When you use stream encoders with NVDA, the following commands can be used from the encoder window:

* F9: Connect to a streaming server (for example, SHOUTcast). NVDA announces "connecting", followed by either a beep when connected or error messages (if any). If you tell NVDA to switch to Studio or play the first selected track after connecting, NVDA will switch to Studio window or play the first track when connected to the streaming server, respectively.
* F10 (SAM encoder only): Disconnect from a streaming server (NVDA will announce, "disconnecting"). If you are using SPL or AltaCast encoders, from the encoders list, press Shift+TAB until you reach "disconnect" button and press ENTER.
* Control+F9: Connect all encoders at once.
* Control+F10 (SAM encoder only): Disconnect all encoders.
* Control+Shift+F11: Sets whether NVDA will switch to Studio window when the selected encoder is connected.
* Shift+F11: Sets whether Studio will play the first selected track when the selected encoder is connected.
* Control+F11: allows you to monitor the selected encoder in the background for connection changes. To disable background monitoring of all encoders (of any type), press Control+F11 twice quickly.
* Control+F12: Select the encoder position you have deleted and let NVDA realign stream labels and encoder settings.
* Alt+NVDA+0 and F12: Opens encoder settings dialog. See encoder settings section for details.

Notes:

* There might be a delay when a connection is established; during this time, NVDA may appear to freeze (but it isn't; NVDA is keeping an eye on status changes).
* You can still perform NVDA commands such as announcing current time while encoders are trying to connect to an encoding server. You can also switch to Studio window and perform add-on commands.
* Settings such as focusing to Studio is saved across sessions.
* In addition to status column commands listed below, you can use table navigation commands (Control+Alt+arrow keys) to review column information.

### Encoder status columns

You can use Control+NVDA+number commands to review encoder status. The following columns can be reviewed:

* Control+NVDA+1: Encoder position.
* Control+NVDA+2: Stream label.

For SAM Encoders:

* Control+NVDA+3: Encoder format.
* Control+NVDA+4: Encoder status.
* Control+NVDA+5: Status description.

For SPL and AltaCast Encoders:

* Control+NVDA+3: Encoder settings.
* Control+NVDA+4: Connection status/transfer rate.

### Encoder settings

The encoder settings dialog is used to bring together various commands used to configure encoder preferences. The available settings are as follows:

* Encoder label: Enter the label for this encoder. If blank, the label associated with the encoder will be removed.
* Focus to Studio when connected (off by default): if enabled, Studio window will be focused when the selected encoder is connected.
* Play first track when connected (off by default): if enabled, NVDA will play the first selected track from Studio when the selected encoder connects.
* Background monitor (off by default): if enabled, NVDA will monitor connection status changes for the selected encoder from anywhere.
* Play connection tone (on by default): if enabled, NVDA will play connection tone until the selected encoder connects.
* Announce connection status until encoder connects (on by default): if enabled, NVDA will announce connection attempt messages until the selected encoder actually connects. If disabled, NVDA will stop when an error is encountered while connecting to a streaming server.

These settings will be saved across sessions.

## Frequently asked questions

Here is a list of frequently asked questions when using NVDA with SPL suite of applications:

Q. Is Studio accessible without using the add-on?

Yes. The benefits of using the add-on are for announcing status information and to make broadcasting more efficient through status messages, alarms and so forth.

Q. When I try to perform SPL Controller or Assistant layer commands, NVDA says, "SPL Studio is not running."

You need to run SPL Studio in order for these commands to work.

Q. Some add-on commands do not have keyboard shortcuts.

You can assign your own commands to the following commands from Input Gestures dialog (see NVDA User Guide for details on Input Gestures dialog):

* Entering SPL Controller layer.
* Entering SPL Assistant layer.
* Switching to SPL Studio from any program.
* Obtaining Studio status information from any program.
* Announcing time in hours, minutes and seconds.
* Column Search.
* Time range finder.
* Announcing weather and temperature information.
* Announcing title and duration of the next track if any.
* Announcing title and length of the currently playing track.
* Announcing metadata streaming status.
* Opening a dialog to quickly toggle metadata streaming.
* Obtaining playlist snapshots.

Q. Does the add-on support speech on demand mode?

Speech on demand mode allows NVDA to speak selected commands such as informational messages while staying silent. The following add-on commands support speech on demand mode:

* Entering SPL Controller layer.
* Entering SPL Assistant layer.
* Obtaining Studio and/or encoder status information from any program.
* Elapsed and remaining time for a currently playing track.
* Announcing time in hours, minutes and seconds.
* Announcing broadcaster time.
* Announcing weather and temperature information.
* Announcing title and duration of the next track if any.
* Announcing title and length of the currently playing track.
* Obtaining playlist snapshots and playlist duration analysis.
* Announcing columns and comments for the selected track in Studio.
* Announcing information on the selected encoder such as encoder label.

Q. Can I use SPL Assistant commands from Studio windows other than playlist viewer?

Yes with one exception: you can use various SPL Assistant layer commands outside of playlist viewer (say, from within insert tracks window) except jumping to place marker track (K). Also, when pressing SPL Assistant, D (remaining time for the entire playlist), sometimes you'll be asked to move back to playlist viewer, and from then on, this command will work regardless of where you are in Studio.

Q. How can I tell NVDA to use a different sound card from the card used for streaming radio shows?

To change sound cards for NVDA, Open NVDA menu, go to Preferences, Settings, then select audio settings category (you can also open this window directly by pressing Control+NVDA+U). Go to output device combo box, select the desired sound card for NVDA, then press ENTER. To switch back to the original sound card, repeat these steps, then choose the original sound card from output device combo box.

Alternatively, you can have different sound cards configured via a manually activated configuration profile that you can switch to while using Studio. First, open Configuration profiles dialog (Control+NVDA+P) and define a new manual profile. With the new profile active, select a sound card. Then switch back to the normal profile.

Q. How can I view latest cart assignments?

When you exit cart edit mode, cart explorer will reflect latest cart assignments so you can view cart assignments right away.

Q. When I try to switch to Studio, NVDA says, "SPL minimized."

You can ask Studio to run from system tray. If this is the case, NVDA will announce that Studio is minimized to system tray. To open Studio, go to system tray, select Studio icon and open pop-up menu. Select "restore" from the menu that appears.

Q. Which status announcements are affected by different verbosity levels?

The following toggle announcements are affected by verbosity levels, particularly advanced level where either a shortened text or a short beep will be heard:

* Automation.
* Microphone.
* Line-in.
* Record to file.
* cart edit/insert (prior to December 2016).)

Q. How can I monitor a lengthy library scan?

Open Insert Tracks dialog (Control+I). If you've selected progress announcement from library scan announcement options (see above), NVDA will announce the progress of a scan. Don't move away from this window until the scan is complete. Alternativley, you can monitor a lengthy scan from anywhere by using the SPL Assistant method described above.

Q. During a library scan, NVDA repeats current scan count.

This is expected if it takes a long time to perform library scans, particularly if scanning an entire drive. Don't worry if you hear repeats.

Q. I did something and NVDA no longer remembers stream labels and end of track alarm setting.

Your configuration files have been deleted from your NVDA user configuration folder, or there was a problem with the configuration file. You can get them back by reentering stream labels and entering the desired setting for end of track alarm.

Q. When I start Studio, I get an error saying add-on configuration has been reset to defaults.

If NVDA determines that there were serious problems with your configuration file, some or all settings will be returned to defaults. Please configure the add-on settings to your liking, and barring further problems with the configuration information, the error dialog will go away next time you restart NVDA or Studio.

Q. When I start Studio, NVDA says, "cannot find instant switch profile".

You might have deleted or renamed the file associated with a previously defined instant switch profile. Please assign another profile as an instant switch profile.

Q. Can I save or reset Studio add-on settings using commands used to save or reset NVDA settings?

Yes. You can perform the following commands or select the appropriate item from NVDA menu while Studio is running:

* Save settings: press Control+NVDA+C to save Studio add-on settings along with NVDA settings.
* Reload saved settings from disk: press Control+NVDA+R once to reload saved settings, including Studio add-on settings.
* Reset settings to defaults: press Control+NVDA+R three times quickly to reset settings to defaults.

Q. Can I save and reset encoder settings by pressing save and reset commands?

Yes as long as an encoder is in use. You can save and reset encoder settings - no reload. Note that when resetting settings, any background monitoring announcements will be stopped.

Q. Besides reloading saved settings versus resetting settings to defaults, what are some things to be aware of when pressing Control+NVDA+R once or three times?

1. If you are using a broadcast profile other than normal profile, reloading saved settings won't change the active profile, whereas resetting settings will switch you to normal profile.
2. Metadata streaming settings won't be affected, but the settings applied may show different values as opposed to what is happening on air.
3. If you are using a different sound card via a manually activated NVDA configuration profile, the default sound card you've configured from normal configuration will become active.
4. If you ask NVDA to monitor connection status for an encoder in the background, pressing Control+NVDA+R three times will stop this process.

Q. Are there times when I should not press Control+NVDA+R three times to reset Studio settings?

You should not reset Studio add-on settings (and in some cases, NVDA settings to defaults along with add-on settings when pressing Control+NVDA+R three times quickly) while broadcasting.

Q. When announcing tracks, which columns can NVDA suppress and reorder?

You can customize announcement and/or order of announcement for the following columns:

* Artist (reorder only)
* Title (reorder only)
* Duration
* Intro
* Category
* Filename
* Outro
* Year
* Album
* Genre
* Mood
* Gender
* Energy
* Rating
* Tempo
* BPM
* Time scheduled

Notice that these are the columns shown in Studio's playlist viewer.

Q. NVDA says "failed to locate Studio window" when trying to perform commands with a playlist loaded.

This is usually caused by a Studio plugin (not the add-on) changing the window class name used to communicate between Studio and external code (including this add-on). To check this, from Studio, open Options/Plugins and see the content of window class name edit field. If it is something other than "SPLStudio", this may indicate that a plugin did change the window class name. To restore various Studio add-on functionality, you need to restore window class name to default (SPLStudio).

Q. When trying to switch profiles by pressing SPL Assistant, F12, NVDA says, "no instant switch profile is defined".

Before switching profiles instantly, you need to define an instant profile. See instant switch profile section for more details.

Q. When I try to switch to another profile, NVDA says, "you are already in the instant switch profile".

You need to be using a profile different from that of the instant switch profile before you can switch profiles.

Q. I created several broadcast profiles. They loaded fine until recently, but are not showing up, although the profile files still exist.

This is likely a result of add-on using only the normal profile via command-line switches. See an entry on command-line switches.

Q. Can I monitor connection attempts from somewhere other than encoder window?

Yes. You can press F9 or Control+F9 from an encoder window to connect to a streaming server, then move to another program. NVDA will monitor for connection attempt status (connected or an error message).

Q. How can I monitor all encoders when connecting all of them at once by pressing Control+F9 from SAM encoder window?

Press Control+F9 to connect all encoders. Note that one of the streams should be set so Studio can start playback once connected.

Q. I wish to designate an encoder as an archive encoder. What encoder settings should I use?

For best experience, configure archiver encoder from NVDA side (via encoder settings dialog or Alt+NVDA+number row 0) as follows:

* Stream label: it should be memorable that allows you to identify it as an archive encoder.
* Focus to Studio when connected: no
* Play first track when connected: no
* Monitor connection status in the background: no
* Play connection tone: no
* Announce connection status until connected: no

Q. Playback volume is lowered in Studio whenever NVDA speaks.

You need to disable audio ducking (NVDA+Shift+D).

Q. NVDA responds slowly when I press V from playlist viewer and Studio opens SPL Recorder.

This is one of the limitations of Studio and/or the add-on. One workaround is to use a dummy encoder for recording a show.

Q. When I press SPL Controller, then number row key to play carts, NVDA just plays beeps.

SPL Studio Standard will not let you assign carts to number row keys (1 through 9, 0, hyphen, equals), thus SPL Controller will honor which Studio edition you're using by preventing you from playing number row carts when using Studio Standard.

Q. What is the best way to suggest new features, send bug reports or connect with other add-on users?

There is a dedicated mailing list for users of NVDA and SPL, which can be found at https://nvda-spl.groups.io/g/nvda-spl.

Q. Can I test the absolute latest version of the add-on for testing purposes?

Yes (called Studio Add-on Test Drive program). Anyone can test latest version for free. First, subscribe to NVDA SPL list, then look for messages regarding Test Drive builds (sometimes called development snapshots). These development snapshots can be obtained from NV Access add-on store if StationPlaylist add-on update channel (from add-on context menu) is set to "dev" or "any". Some snapshot builds are bleeding-edge code and are unstable at times, so don't use these builds in a production environment.

Q. I keep hearing about LTS releases. What are they?

LTS stands for long-term support. This is a special version of a software that will be supported for a very long time for stability reasons.

Usually a version of the StationPlaylist add-on for NVDA receives support until the next version is released (typically several weeks to months). However, because there are broadcasters who would like to use a stable version of the add-on for a long time (either because they have to or they cannot upgrade to the latest version of Studio), a long-term support version of the add-on is released every few years to give people time to upgrade to a future stable version of Studio. In addition to longer support period (up to a year or more), a LTS version of the add-on is the last version to support the oldest stable Studio version, or in some cases, provides compatibility with old NVDA and/or Windows releases. Due to special nature of LTS releases, releases in a LTS series must be instaled manually i.e. they will not be made available on the add-on store.

As of 2025, add-on versions 3.x (September 2014-June 2015), 7.x/15.x (April 2016-April 2018; 15.x since October 2016), and 18.09.x (September 2018-December 2019) were designated as LTS releases, supporting Studio 4.33, 5.01, and 5.1x, respectively. Version 20.09.x (September 2020-April 2021), the most recent LTS release, supports Studio 5.20 and NVDA 2019.3 and later, with upcoming 25.06.x designated as last LTS releases to support Studio 5.x.

Q. Which versions of Studio are supported by which add-on releases?

* Studio versions prior to 5.x: add-on 1.0 to 3.9 (January 2014-June 2015).
* Studio 5.0x: Add-on 1.0 to 7.5, 15.0 to 15.14 (January 2014-April 2018).
* Studio 5.1x: Add-on 3.2 to 18.09.13 (November 2014-December 2019).
* Studio 5.20: Add-on 16.11 to 20.09.7 (November 2016-April 2021).
* Studio 5.3x: Add-on 17.11 to 22.12 (November 2017-December 2022).
* Studio 5.40: Add-on 19.11 to 25.05.4 (November 2019-May 2025).
* Studio 5.50: Add-on 20.11 to 25.06 (November 2020-June 2025).
* Studio 6.0x: Add-on 21.11 to 25.06 (November 2021-June 2025).
* Studio 6.1x: Add-on 24.03 to 25.06 (April 2024-June 2025).

Note: the schedule above is subject to change.

Q. After 2017, can I use the add-on on Windows versions prior to Windows 7 Service Pack 1?

In August 2017, NV Access announced that NVDA 2017.3 is the last version to support Windows releases prior to Windows 7 Service Pack 1. To cater to needs of broadcasters who might be using earlier Windows releases such as Windows XP, add-on 15.x was maintained until April 2018.

Q. From 2023, can I use the add-on on Windows versions prior to Windows 10?

Windows 7 and 8.x are out of support from Microsoft from January 2023. You can use the add-on on these Windows releases but note that support will not be provided. Add-on 23.01 and later will not install on unsupported Windows releases, and version 25.05 no longer supports Windows 7 and 8.

Q. What are update channels?

With the introduction of Test Drive Program (see above), it became possible for you to choose the frequency of updates and where to get updates from. As of 2025, there are three regular and two limited time channels:

* Canary (or source code level; regular channel): This includes development branches other than the ones below and is meant for add-on developers (currently two).
* Try builds (limited distribution): sometimes called "offline try builds", meant to troubleshoot issues with one or more broadcasters.
* Development (formerly Test Drive Slow; regular channel): This designates "main" branch in the source code repository and is used to showcase changes under development, including bleeding-edge changes. Releases from this channel are made available on the NV Access add-on store.
* Stable (regular channel): Designates stable releases ("stable" branch in the source code repository). This is the default release available on the add-on store.

In addition, during LTS maintenance, "Longterm" channel becomes active. This is a separate release that receives updates from a separate branch and is unavailable in the add-on store.

Q. Can I switch between all available update channels?

No. You need to visit NV Access add-on store and download appropriate version.

Q. Are there command-line switches unique to this add-on?

Starting with add-on 17.10, it became possible to specify the behavior of the add-on via command-line switches. You would pass in these switches when you start NVDA from Run dialog (Windows+R).

The switches for this add-on are:

* --spl-normalprofileonly: only loads normal profile.
* --spl-configinmemory: not only this will use normal profile only, but settings will not be loaded from disk nor saved to it.

If any of these switches are used, broadcast profiles functionality will be disabled.

Q. What is NVDA in secure mode?

NVDA can be configured to run in secure screens, and if this is the case, NVDA restricts users from saving settings, installing add-ons, and viewing the log. In addition to not allowing you from interacting with StationPlaylist suite of applications, the following limitations are present in secure screens:

* SPL Controller layer commands cannot be performed.
* You cannot switch to Studio from other programs.
* You cannot obtain Studio and/or encoder status.

In addition, it is possible to run NVDA with secure screen like restrictions while not in secure screens (not recommended). If this happens, the following restrictions will be in place when interacting with SPL suite of applications:

* You cannot create, copy, rename, delete, or configure triggers for broadcast profiles.
* You cannot save add-on settings, including encoder settings for the add-on.
* You cannot copy playlist transcripts to the clipboard or save them to a file.
* You cannot configure advanced add-on settings or reset add-on settings to defaults as these settings categories will be unavailable in add-on settings dialog.

Because of these restrictions, you should not copy StationPlaylist add-on to secure screens, nor run NVDA in secure mode while not in secure screens.

## Credits and contact information

If you have suggestions, bug reports or just want to drop by and say hi, you can contact the author using the following contact information:

* Email: nvda@chrisduffley.com
* Mastodon: ChrisDuffley@chrisduffley.com

There is a dedicated forum for people using StationPlaylist suite, and you can subscribe by sending an email to stationplaylist+subscribe@groups.io. In addition, there is a dedicated mailing list for people using NVDA and Studio, which can be found at https://groups.io/g/nvda-spl.

Lastly, if you'd like to take part in shaping the future of the Studio add-on and help test new features, you can join the Studio Add-on Test Drive program available to NVDA SPL list members. Whenever new features are available, you'll be a part of the first group of users to experiment with a new feature and provide feedback.

Credits: I (Joseph) would like to thank the following people for giving me and others inspirations behind the StationPlaylist add-on for NVDA:

* Geoff Shang: For coding the initial version of the add-on and making it available.
* Jamie Teh from NV access: For providing a workaround for track listings.
* Brian Hartgen: For JAWS for Windows scripts for SPL Studio and the idea behind SPL Controller and Assistant layer commands.
* Jeff Bishop: For Window-Eyes scripts and commands used in SPL Controller and Assistant commands.
* Tyler Spivey: For the actual layer command facility.
* Ross Levis: The head developer of SPL Studio for continued support for screen readers in SPL Studio.
* Roger Stewart: For suggesting this add-on and for continued testing and reports.
* Duyahn Walker: For useful suggestions and bug reports.
* Shaun Oliver: For continued suggestions on encoder support.
* Jerry Mader: For useful suggestions and feature testing.
* Jerry Jicha: For useful feedback and feature testing.
* Christopher Duffley: for maintaining and championing the add-on since 2023.
* And many other supporters and testers.

End of StationPlaylist Add-on Guide
