# StationPlaylist #

* Authors: Geoff Shang, Joseph Lee and other contributors
* Download [stable version][1]
* Download [development version][2]
* NVDA compatibility: 2019.3

This add-on package provides improved usage of StationPlaylist Studio and other StationPlaylist apps, as well as providing utilities to control Studio from anywhere. Supported apps include Studio, Creator, Track Tool, VT Recorder, and Streamer, as well as SAM, SPL, and AltaCast encoders.

For more information about the add-on, read the [add-on guide][4]. For developers seeking to know how to build the add-on, see buildInstructions.txt located at the root of the add-on source code repository.

IMPORTANT NOTES:

* This add-on requires StationPlaylist suite 5.20 or later.
* If using Windows 8 or later, for best experience, disable audio ducking mode.
* Starting from 2018, [changelogs for old add-on releases][5] will be found on GitHub. This add-on readme will list changes from version 17.08 (2017 onwards).
* Certain add-on features won't work under some conditions, including running NVDA in secure mode.
* Due to tecnical limitations, you cannot install or use this add-on on Windows Store version of NVDA.
* Features marked as "experimental" are meant to test something before a wider release, so they will not be enabled in stable releases.

## Shortcut keys

Most of these will work in Studio only unless otherwise specified.

* Alt+Shift+T from Studio window: announce elapsed time for the currently playing trakc.
* Control+Alt+T (two finger flick down in SPL touch mode) from Studio window: announce remaining time for the currently playing trakc.
* NVDA+Shift+F12 (two finger flick up in SPL touch mode) from Studio window: announces broadcaster time such as 5 minutes to top of the hour. Pressing this command twice will announce minutes and seconds till top of the hour.
* Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens end of track setting dialog.
* Alt+NVDA+1 from Creator's Playlist Editor window: Announces scheduled time for the loaded playlist.
* Alt+NVDA+2 (two finger flick left in SPL mode) from Studio window: Opens song intro alarm setting dialog.
* Alt+NVDA+2 from Creator's Playlist Editor window: Announces total playlist duration.
* Alt+NVDA+3 from Studio window: Toggles cart explorer to learn cart assignments.
* Alt+NVDA+3 from Creator's Playlist Editor window: Announces when the selected track is scheduled to play.
* Alt+NVDA+4 from Studio window: Opens microphone alarm dialog.
* Alt+NVDA+4 from Creator's Playlist Editor window: Announces rotation and category associated with the loaded playlist.
* Control+NVDA+f from Studio window: Opens a dialog to find a track based on artist or song name. Press NVDA+F3 to find forward or NVDA+Shift+F3 to find backward.
* Alt+NVDA+R from Studio window: Steps through library scan announcement settings.
* Control+Shift+X from Studio window: Steps through braille timer settings.
* Control+Alt+left/right arrow (while focused on a track in Studio, Creator, and Track Tool): Announce previous/next track column.
* Control+Alt+Home/End (while focused on a track in Studio, Creator, and Track Tool): Announce first/last track column.
* Control+Alt+up/down arrow (while focused on a track in Studio only): Move to previous or next track and announce specific columns.
* Control+NVDA+1 through 0 (while focused on a track in Studio, Creator (including Playlist Editor), and Track Tool): Announce column content for a specified column (first ten columns by default). Pressing this command twice will display column information on a browse mode window.
* Control+NVDA+- (hyphen while focused on a track in Studio, Creator, and Track Tool): display data for all columns in a track on a browse mode window.
* Alt+NVDA+C while focused on a track (Studio only): announces track comments if any.
* Alt+NVDA+0 from Studio window: Opens the Studio add-on configuration dialog.
* Alt+NVDA+- (hyphen) from Studio window: Send feedback to add-on developer using the default email client.
* Alt+NVDA+F1: Open welcome dialog.

## Unassigned commands

The following commands are not assigned by default; if you wish to assign them, use Input Gestures dialog to add custom commands. To do so, from Studio window, open NVDA menu, Preferences, then Input Gestures. Expand StationPlaylist category, then locate unassigned commands from the list below and select "Add", then type the gesutre you wish to use.

* Switching to SPL Studio window from any program.
* SPL Controller layer.
* Announcing Studio status such as track playback from other programs.
* Announcing encoder connection status from any program.
* SPL Assistant layer from SPL Studio.
* Announce time including seconds from SPL Studio.
* Announcing temperature.
* Announcing title of next track if scheduled.
* Announcing title of the currently playing track.
* Marking current track for start of track time analysis.
* Performing track time analysis.
* Take playlist snapshots.
* Find text in specific columns.
* Find tracks with duration that falls within a given range via time range finder.
* Quickly enable or disable metadata streaming.

## Additional commands when using encoders

The following commands are available when using encoders:

* F9: connect to a streaming server.
* F10 (SAM encoder only): Disconnect from the streaming server.
* Control+F9/Control+F10 (SAM encoder only): Connect or disconnect all encoders, respectivley.
* F11: Toggles whether NVDA will switch to Studio window for the selected encoder if connected.
* Shift+F11: Toggles whether Studio will play the first selected track when encoder is connected to a streaming server.
* Control+F11: Toggles background monitoring of the selected encoder.
* F12: Opens a dialog to enter custom label for the selected encoder or stream.
* Control+F12: opens a dialog to select the encoder you have deleted (to realign stream labels and encoder settings).
* Alt+NVDA+0: Opens encoder settings dialog to configure options such as stream label.

In addition, column review commands are available, including:

* Control+NVDA+1: Encoder position.
* Control+NVDA+2: stream label.
* Control+NVDA+3 from SAM Encoder: Encoder format.
* Control+NVDA+3 from SPL and AltaCast Encoder: Encoder settings.
* Control+NVDA+4 from SAM Encoder: Encoder connection status.
* Control+NVDA+4 from SPL and AltaCast Encoder: Transfer rate or connection status.
* Control+NVDA+5 from SAM Encoder: Connection status description.

## SPL Assistant layer

This layer command set allows you to obtain various status on SPL Studio, such as whether a track is playing, total duration of all tracks for the hour and so on. From any SPL Studio window, press the SPL Assistant layer command, then press one of the keys from the list below (one or more commands are exclusive to playlist viewer). You can also configure NVDA to emulate commands from other screen readers.

The available commands are:

* A: Automation.
* C (Shift+C  in JAWS and Window-Eyes layouts): Title for the currently playing track.
* C (JAWS and Window-Eyes layouts): Toggle cart explorer (playlist viewer only).
* D (R in JAWS layout): Remaining duration for the playlist (if an error message is given, move to playlist viewer and then issue this command).
* E (G in Window-Eyes layout): Metadata streaming status.
* Shift+1 through Shift+4, Shift+0: Status for individual metadata streaming URL's (0 is for DSP encoder).
* E (Window-Eyes layout): Elapsed time for the currently playing track.
* F: Find track (playlist viewer only).
* H: Duration of music for the current hour slot.
* Shift+H: Remaining track duration for the hour slot.
* I (L in JAWS or Window-Eyes layouts): Listener count.
* K: Move to the marked track (playlist viewer only).
* Control+K: Set the current track as the place marker track (playlist viewer only).
* L (Shift+L in JAWS and Window-Eyes layouts): Line in.
* M: Microphone.
* N: Title for the next scheduled track.
* P: Playback status (playing or stopped).
* Shift+P: Pitch of the current track.
* R (Shift+E in JAWS and Window-Eyes layouts): Record to file enabled/disabled.
* Shift+R: Monitor library scan in progress.
* S: Track starts (scheduled).
* Shift+S: Time until selected track will play (track starts in).
* T: Cart edit/insert mode on/off.
* U: Studio up time.
* W: Weather and temperature if configured.
* Y: Playlist modified status.
* 1 through 0: Announce column content for a specified column.
* F8: Take playlist snapshots (number of tracks, longest track, etc.).
* Shift+F8: Request playlist transcripts in numerous formats.
* F9: Mark current track for start of playlist analysis (playlist viewer only).
* F10: Perform track time analysis (playlist viewer only).
* F12: Switch between current and a predefined profile.
* F1: Layer help.
* Shift+F1: Opens online user guide.

## SPL Controller

The SPL Controller is a set of layered commands you can use to control SPL Studio anywhere. Press the SPL Controller layer command, and NVDA will say, "SPL Controller." Press another command to control various Studio settings such as microphone on/off or play the next track.

The available SPL Controller commands are:

* Press P to play the next selected track.
* Press U to pause or unpause playback.
* Press S to stop the track with fade out, or to stop the track instantly, press T.
* Press M or Shift+M to turn on or off the microphone, respectively, or press N to enable microphone without fade.
* Press A to enable automation or Shift+A to disable it.
* Press L to enable line-in input or Shift+L to disable it.
* Press R to hear remaining time for the currently playing track.
* Press Shift+R to get a report on library scan progress.
* Press C to let NVDA announce name and duration of the currently playing track.
* Press Shift+C to let NVDA announce name and duration of the upcoming track if any.
* Press E to hear which encoders are connected.
* Press I to obtain listener count.
* Press Q to obtain various status information about Studio including whether a track is playing, microphone is on and others.
* Press cart keys (F1, Control+1, for example) to play assigned carts from anywhere.
* Press H to show a help dialog which lists available commands.

## Track alarms

By default, NVDA will play a beep if five seconds are left in the track (outro) and/or intro. To configure this value as well as to enable or disable them, press Alt+NVDA+1 or Alt+NVDA+2 to open end of track and song ramp dialogs, respectively. In addition, use Studio add-on settings dialog to configure if you'll hear a beep, a message or both when alarms are turned on.

## Microphone alarm

You can ask NVDA to play a sound when microphone has been active for a while. Press Alt+NVDA+4 to configure alarm time in seconds (0 disables it).

## Track Finder

If you wish to quickly find a song by an artist or by song name, from track list, press Control+NVDA+F. Type or choose the name of the artist or the song name. NVDA will either place you at the song if found or will display an error if it cannot find the song you're looking for. To find a previously entered song or artist, press NVDA+F3 or NVDA+Shift+F3 to find forward or backward.

Note: Track Finder is case-sensitive.

## Cart Explorer

Depending on edition, SPL Studio allows up to 96 carts to be assigned for playback. NVDA allows you to hear which cart, or jingle is assigned to these commands.

To learn cart assignments, from SPL Studio, press Alt+NVDA+3. Pressing the cart command once will tell you which jingle is assigned to the command. Pressing the cart command twice will play the jingle. Press Alt+NVDA+3 to exit cart explorer. See the add-on guide for more information on cart explorer.

## Track time analysis

To obtain length to play selected tracks, mark current track for start of track time analysis (SPL Assistant, F9), then press SPL Assistant, F10 when reaching end of selection.

## Columns Explorer

By pressing Control+NVDA+1 through 0 or SPL Assistant, 1 through 0, you can obtain contents of specific columns. By default, these are artist, title, duration, intro, outro, category, year, album, genre and mood. You can configure which columns will be explored via columns explorer dialog found in add-on settings dialog.

## Playlist snapshots

You can press SPL Assistant, F8 while focused on a playlist in Studio to obtain various statistics about a playlist, including number of tracks in the playlist, longest track, top artists and so on. After assigning a custom command for this feature, pressing the custom command twice will cause NVDA to present playlist snapshot information as a webpage so you can use browse mode to navigate (press escape to close).

## Playlist Transcripts

Pressing SPL Assistant, Shift+F8 will present a dialog to let you request playlist transcripts in numerous formats, including in a plain text format, an HTML table or a list.

## Configuration dialog

From studio window, you can press Alt+NVDA+0 to open the add-on configuration dialog. Alternatively, go to NVDA's preferences menu and select SPL Studio Settings item. This dialog is also used to manage broadcast profiles.

## SPL touch mode

If you are using Studio on a touchscreen computer running Windows 8 or later and have NVDA 2012.3 or later installed, you can perform some Studio commands from the touchscreen. First use three finger tap to switch to SPL mode, then use the touch commands listed above to perform commands.

## Version 20.03

* Columns Explorer will now announce first ten columns by default (existing installations will continue to use old column slots).
* The ability to announce name of the playing track automatically from places other than Studio has been removed. This feature, introduced in add-on 5.6 as a workaround for Studio 5.1x, is no longer functional. Users must now use SPL Controller and/or Assistant layer command to hear title of the currently playing track from everywhere (C).
* Due to removal of automatic announcement of playing track title, the setting to configure this feature has been removed from add-on settings/status announcement category.
* In encoders, NvDA will play connection tone every half a second while an encoder is connecting.
* In encoders, NVDA will now announce connection attempt messages until an encoder is actually connected. Previously NVDA stopped when an error was encountered.
* A new setting has been added to encoder settings to let NvDA announce connection messages until the selected encoder is connected. This setting is enabled by default.

## Version 20.02

* Initial support for StationPlaylist Creator's Playlist Editor.
* Added Alt+NVDA+number row commands to announce various status information in Playlist Editor. These include date and time for the playlist (1), total playlist duration (2), when the selected track is scheduled to play (3), and rotation and category (4).
* While focused on a track in Creator and Track Tool (except in Creator's Playlist Editor), pressing Control+NVDA+Dash will display data for all columns on a browse mode window.
* If NVDA Recognizes a track list item with less than 10 columns, NVDA will no longer announce headers for nonexistent columns if Control+NVDA+number row for out of range column is pressed.
* In creator, NVDA will no longer announce column information if Control+NVDA+number row keys are pressed while focused on places other than track list.
* When a track is playing, NVDA will no longer announce "no track is playing" if obtaining information about current and next tracks via SPL Assistant or SPL Controller.
* If an alarm options dialog (intro, outro, microphone) is open, NVDA will no longer appear to do nothing or play error tone if attempting to open a second instance of any alarm dialog.
* When trying to switch between active profile and an instant profile via SPL Assistant (F12), NVDA will present a message if attempting to do so while add-on settings screen is open.
* In encoders, NVDA will no longer forget to apply no connection tone setting for encoders when NVDA is restarted.

## Version 20.01

* NVDA 2019.3 or later is required due to extensive use of Python 3.

## Version 19.11.1/18.09.13-LTS

* Initial support for StationPlaylist suite 5.40.
* In Studio, playlist snapshots (SPL Assistant, F8) and various time announcement commands such as remaining time (Control+Alt+T) will no longer cause NVDA to play error tones or do nothing if using NVDA 2019.3 or later.
* In Creator's track list items, "Language" column added in Creator 5.31 and later is properly recognized.
* In various lists in Creator apart from track list, NVDA will no longer announce odd column information if Control+NVDA+number row command is pressed.

## Version 19.11

* Encoder status command from SPL Controller (E) will announce connection status for the active encoder set instead of encoders being monitored in the background.
* NVDA will no longer appear to do nothing or play error tones when it starts while an encoder window is focused.

## Version 19.10/18.09.12-LTS

* Shortened the version announcement message for Studio when it starts.
* Version information for Creator will be announced when it starts.
* 19.10: custom command can be assigned for encoder status command from SPL Controller (E) so it can be used from everywhere.
* Initial support for AltaCast encoder (Winamp plugin and must be recognized by Studio). Commands are same as SPL Encoder.

## Version 19.08.1

* In SAM encoders, NVDA will no longer appear to do nothing or play error tones if an encoder entry is deleted while being monitored in the background.

## Version 19.08/18.09.11-LTS

* 19.08: NVDA 2019.1 or later is required.
* 19.08: NVDA will no longer appear to do nothing or play error tones when restarting it while Studio add-on settings dialog is open.
* NVDA will remember profile-specific setttings when switching between settings panels even after renaming the currently selected broadcast profile from add-on settings.
* NVDA will no longer forget to honor changes to time-based profiles when OK button is pressed to close add-on settings. This bug has been present since migrating to multi-page settings in 2018.

## Version 19.07/18.09.10-LTS

* Renamed the add-on from "StationPlaylist Studio" to "StationPlaylist" to better describe apps and features supported by this add-on.
* Internal security enhancements.
* If microphone alarm or metadata streaming settings are changed from add-on settings, NVDA will no longer fail to apply changed settings. This resolves an issue where microphone alarm did not start or stop properly after changing settings via add-on settings.

## Version 19.06/18.09.9-LTS

Version 19.06 supports SPL Studio 5.20 and later.

* Initial support for StationPlaylist Streamer.
* While running various Studio apps such as Track Tool and Studio, if a second instance of the app is started and then exits, NVDA will no longer cause Studio add-on configuration routines to produce errors and stop working correctly.
* Added labels for various options in SPL Encoder configuration dialog.

## Version 19.04.1

* Fixed several issues with redesigned column announcements and playlist transcripts panels in add-on settings, including changes to custom column order and inclusion not being reflected when saving and/or switching between panels.

## Version 19.04/18.09.8-LTS

* Various global commands such as entering SPL Controller and switching to Studio window will be turned off if NVDA is running in secure mode or as a Windows Store application.
* 19.04: in column announcements and playlist transcripts panels (add-on settings), custom column inclusion/order controls will be visible up front instead of having to select a button to open a dialog to configure these settings.
* In Creator, NVDA will no longer play error tones or appear to do nothing when focused on certain lists.

## Version 19.03/18.09.7-LTS

* Pressing Control+NVDA+R to reload saved settings will now also reload Studio add-on settings, and pressing this command three times will also reset Studio add-on settings to defaults along with NVDA settings.
* Renamed Studio add-on settings dialog's "Advanced options" panel to "Advanced".
* 19.03 Experimental: in column announcements and playlist transcripts panels (add-on settings), custom column inclusion/order controls will be visible up front instead of having to select a button to open a dialog to configure these settings.

## Version 19.02

* Removed standalone add-on update check feature, including update check command from SPL Assistant (Control+Shift+U) and add-on update check options from add-on settings. Add-on update check is now performed by Add-on Updater.
* NVDA will no longer appear to do nothing or play error tones when microphone active interval is set, used to remind broadcasters that microphone is active with periodic beeps.
* When resetting add-on settings from add-on settings dialog/reset panel, NVDA will ask once more if an instant switch profile or a time-based profile is active.
* After resetting Studio add-on settings, NVDA will turn off microphone alarm timer and announce metadata streaming status, similar to after switching between broadcast profiles.

## Version 19.01.1

* NVDA will no longer announce "monitoring library scan" after closing Studio in some situations.

## Version 19.01/18.09.6-LTS

* NVDA 2018.4 or later is required.
* More code changes to make the add-on compatible with Python 3.
* 19.01: some message translations from this add-on will resemble NVDA messages.
* 19.01: add-on update check feature from this add-on is no more. An error message will be presented when trying to use SPL Assistant, Control+Shift+U to check for updates. For future updates, please use Add-on Updater add-on.
* Slight performance improvements when using NVDA with apps other than Studio while Voice Track Recorder is active. NVDA will still show performance issues when using Studio itself with Voice Track Recorder active.
* In encoders, if an encoder settings dialog is open (Alt+NVDA+0), NVDA will present an error message if trying to open another encoder settings dialog.

## Version 18.12

* Internal changes to make the add-on compatible with future NVDA releases.
* Fixed many instances of add-on messages spoken in English despite translated into other languages.
* If using SPL Assistant to check for add-on updates (SPL Assistant, Control+Shift+U), NVDA will not install new add-on releases if they require a newer version of NVDA.
* Some SPL Assistant commands will now require that the playlist viewer is visible and populated with a playlist, and in some cases, a track is focused. Commands affected include remaining duration (D), playlist snapshots (F8), and playlist transcripts (Shift+F8).
* Playlist remaining duration command (SPL Assistant, D) will now require a track from playlist viewer be focused.
* In SAM Encoders, you can now use table navigation commands (Control+Alt+arrow keys) to review various encoder status information.

## Version 18.11/18.09.5-LTS

Note: 18.11.1 replaces 18.11 in order to provide better support for Studio 5.31.

* Initial support for StationPlaylist Studio 5.31.
* You can now obtain playlist snapshots (SPL Assistant, F8) and transcripts (SPL Assistant, Shift+F8) while a playlist is loaded but the first track isn't focused.
* NVDA will no longer appear to do nothing or play error tones when trying to announce metadata streaming status when Studio starts if configured to do so.
* If configured to announce metadata streaming status at startup, metadata streaming status announcement will no longer cut off announcements about status bar changes and vice versa.

## Version 18.10.2/18.09.4-LTS

* Fixed inability to close the add-on settings screen if Apply button was pressed and subsequently OK or Cancel buttons were pressed.

## Version 18.10.1/18.09.3-LTS

* Resolved several issues related to encoder connection announcement feature, including not announcing status messages, failing to play the first selected track, or not switching to Studio window when connected. These bugs are caused by wxPython 4 (NVDA 2018.3 or later).

## Version 18.10

* NVDA 2018.3 or later is required.
* Internal changes to make the add-on more compatible with Python 3.

## Version 18.09.1-LTS

* When obtaining playlist transcripts in HTML table format, column headers are no longer rendered as a Python list string.

## Version 18.09-LTS

Version 18.09.x is the last release series to support Studio 5.10 and based on old technologies, with 18.10 and later supporting Studio 5.11/5.20 and new features. Some new features will be backported to 18.09.x if needed.

* NVDA 2018.3 or later is recommended due to introduction of wxPython 4.
* Add-on settings screen is now fully based on multi-page interface derived from NVDA 2018.2 and later.
* Test Drive Fast and Slow rings have been combined into "development" channel, with an option for development snapshot users to test pilot features by checking the new pilot features checkbox found in Advanced add-on settings panel. Users formerly on Test Drive Fast ring will continue to test pilot features.
* The ability to select different add-on update channel from add-on settings has been removed. Users wishing to switch to a different release channel should visit NVDA community add-ons website (addons.nvda-project.org), select StationPlaylist Studio, then download the appropriate release.
* Column inclusion checkboxes for column announcement and playlist transcripts, as well as metadata streams checkboxes have been converted to checkable list controls.
* When switching between settings panels, NVDA will remember current settings for profile-specific settings (alarms, column announcements, metadata streaming settings).
* Added CSV (comma-separated values) format as a playlist transcripts format.
* Pressing Control+NVDA+C to save settings will now also save Studio add-on settings (requires NVDA 2018.3).

## Version 18.08.2

* NVDA will no longer check for Studio add-on updates if Add-on Updater (proof of concept) add-on is installed. Consequently, add-on settings will no longer include add-on update related settings if this is the case. If using Add-on Updater, users should use features provided by this add-on to check for Studio add-on updates.

## Version 18.08.1

* Fixed yet another wxPython 4 compatibility issue seen when Studio exits.
* NVDA will announce an appropriate message when playlist modification text isn't present, commonly seen after loading an unmodified playlist or when Studio starts.
* NVDA will no longer appear to do nothing or play error tones when trying to obtain metadata streaming status via SPL Assistant (E).

## Version 18.08

* Add-on settings dialog is now based on multi-category settings interface found in NVDA 2018.2. Consequently, this release requires NVDA 2018.2 or later. The old add-on settings interface is deprecated and will be removed later in 2018.
* Added a new section (button/panel) in add-on settings to configure playlist transcripts options, which is used to configure column inclusion and ordering for this feature and other settings.
* When creating a table-based playlist transcripts and if custom column ordering and/or column removal is in effect, NVDA will use custom column presentation order specified from add-on settings and/or not include information from removed columns.
* When using column navigation commands in track items (Control+Alt+home/end/left arrow/right arrow) in Studio, Creator, and Track Tool, NVDA will no longer announce wrong column data after changing column position on screen via mouse.
* Significant improvements to NVDA's responsiveness when using column navigation commands in Creator and Track Tool. In particular, when using Creator, NVDA will respond better when using column navigation commands.
* NVDA will no longer play error tones or appear to do nothing when attempting to add comments to tracks in Studio or when exiting NVDA while using Studio, caused by wxPython 4 compatibility issue.

## Version 18.07

* Added an experimental multi-category add-on settings screen, accessible by toggling a setting in add-on settings/Advanced dialog (you need to restart NVDA after configuring this setting for the new dialog to show up). This is for NVDA 2018.2 users, and not all add-on settings can be configured from this new screen.
* NVDA will no longer play error tones or appear to do nothing when trying to rename a broadcast profile from add-on settings, caused by wxPython 4 compatibility issue.
* When restarting NVDA and/or Studio after making changes to settings in a broadcast profile other than normal profile, NVDA will no longer revert to old settings.
* It is now possible to obtain playlist transcripts for the current hour. Select "current hour" from list of playlist range options in playlist transcripts dialog (SPL Assistant, Shift+F8).
* Added an option in Playlist Transcripts dialog to have transcripts saved to a file (all formats) or copied to the clipboard (text and Markdown table formats only) in addition to viewing transcripts on screen. When transcripts are saved, they are saved to user's Documents folder under "nvdasplPlaylistTranscripts" subfolder.
* Status column is no longer included when creating playlist transcripts in HTML and Markdown table formats.
* When focused on a track in Creator and Track Tool, pressing Control+NVDA+number row twice will present column information on a browse mode window.
* In Creator and Track Tool, added Control+Alt+Home/End keys to move Column Navigator to first or last column for the focused track.

## Version 18.06.1

* Fixed several compatibility issues with wxPython 4, including inability to open track finder (Control+NVDA+F), column search and time ranger finder dialogs in Studio and stream labeler dialog (F12) from encoders window.
* While opening a find dialog from Studio and an unexpected error occurs, NVDA will present more appropriate messages instead of saying that another find dialog is open.
* In encoders window, NVDA will no longer play error tones or appear to do nothing when attempting to open encoder settings dialog (Alt+NVDA+0).

## Version 18.06

* In add-on settings, added "Apply" button so changes to settings can be applied to the currently selected and/or active profile without closing the dialog first. This feature is available for NVDA 2018.2 users.
* Resolved an issue where NVDA would apply changes to Columns Explorer settings despite pressing Cancel button from add-on settings dialog.
* In Studio, when pressing Control+NVDA+number row twice while focused on a track, NVDA will display column information for a specific column on a browse mode window.
* While focused on a track in Studio, pressing Control+NVDA+Dash will display data for all columns on a browse mode window.
* In StationPlaylist Creator, when focused on a track, pressing Control+NVDA+number row will announce data in specific column.
* Added a button in Studio add-on settings to configure Columns Explorer for SPL Creator.
* Added Markdown table format as a playlist transcripts format.
* The developer feedback email command has changed from Control+NVDA+dash to Alt+NVDA+dash.

## Version 18.05

* Added ability to take partial playlist snapshots. This can be done by defining analysis range (SPL Assistant, F9 at the start of the analysis range) and moving to another item and performing playlist snapshots command.
* Added a new command in SPL Assistant to request playlist transcripts in a number of formats (Shift+F8). These include plain text, an HTML table, or an HTML list.
* Various playlist analysis features such as track time analysis and playlist snapshots are now grouped under the theme of "Playlist Analyzer".

## Version 18.04.1

* NVDA will no longer fail to start countdown timer for time-based broadcast profiles if NVDA with wxPython 4 toolkit installed is in use.

## Version 18.04

* Changes were made to make add-on update check feature more reliable, particularly if automatic add-on update check is enabled.
* NVDA will play a tone to indicate start of library scan when it is configured to play beeps for various announcements.
* NVDA will start library scan in the background if library scan is started from Studio's Options dialog or at startup.
* Double-tapping on a track on a touchscreen computer or performing default action command will now select the track and move system focus to it.
* When taking playlist snapshots (SPL Assistant, F8), if a playlist consists of hour markers only, resolves several issues where NVDA appeared to not take snapshots.

## Version 18.03/15.14-LTS

* If NVDA is configured to announce metadata streaming status when Studio starts, NVDA will honor this setting and no longer announce streaming status when switching to and from instant switch profiles.
* If switching to and from an instant switch profile and NVDA is configured to announce metadata streaming status whenever this happens, NVDA will no longer announce this information multiple times when switching profiles quickly.
* NVDA will remember to switch to the appropriate time-based profile (if defined for a show) after NVDA restarts multiple times during broadcasts.
* If a time-based profile with profile duration set is active and when add-on settings dialog is opened and closed, NVDA will still switch back to the original profile once the time-based profile is finished.
* If a time-based profile is active (particularly during broadcasts), changing broadcast profile triggers via add-on settings dialog will not be possible.

## Version 18.02/15.13-LTS

* 18.02: Due to internal changes made to support extension points and other features, NVDA 2017.4 is required.
* Add-on updating won't be possible under some cases. These include running NVDA from source code or with secure mode turned on. Secure mode check is applicable to 15.13-LTS as well.
* If errors occur while checking for updates, these will be logged and NVDA will advise you to read the NVDA log for details.
* In add-on settings, various update settings in advanced settings section such as update interval will not be displayed if add-on updating is not supported.
* NVDA will no longer appear to freeze or do nothing when switching to an instant switch profile or a time-based profile and NVDA is configured to announce metadata streaming status.

## Version 18.01/15.12-LTS

* When using JAWS layout for SPL Assistant, update check command (Control+Shift+U) now works correctly.
* When changing microphone alarm settings via the alarm dialog (Alt+NVDA+4), changes such as enabling alarm and changes to microphone alarm interval are applied when closing the dialog.

## Version 17.12

* Windows 7 Service Pack 1 or later is required.
* Several add-on features were enhanced with extension points. This allows microphone alarm and metadata streaming feature to respond to changes in broadcast profiles. This requires NVDA 2017.4.
* When Studio exits, various add-on dialogs such as add-on settings, alarm dialogs and others will close automatically. This requires NVDA 2017.4.
* Added a new command in SPL Controller layer to announce name of the upcoming track if any (Shift+C).
* You can now press cart keys (F1, for example) after entering SPl Controller layer to play assigned carts from anywhere.
* Due to changes introduced in wxPython 4 GUI toolkit, stream label eraser dialog is now a combo box instead of a number entry field.

## Version 17.11.2

This is the last stable version to support Windows XP, Vista and 7 without Service Pack 1. The next stable version for these Windows releases will be a 15.x LTS release.

* If using Windows releases prior to Windows 7 Service Pack 1, you cannot switch to development channels.

## Version 17.11.1/15.11-LTS

* NVDA will no longer play error tones or appear to do nothing when using Control+Alt+left or right arrow keys to navigate columns in Track Tool 5.20 with a track loaded. Because of this change, when using Studio 5.20, build 48 or later is required.

## Version 17.11/15.10-LTS

* Initial support for StationPlaylist Studio 5.30.
* If microphone alarm and/or interval timer is turned on and if Studio exits while microphone is on, NVDA will no longer play microphone alarm tone from everywhere.
* When deleting broadcast profiles and if another profile happens to be an instant switch profile, instant switch flag won't be removed from the switch profile.
* If deleting an active profile that is not an instant switch or a time-based profile, NVDA will ask once more for confirmation before proceeding.
* NVDA will apply correct settings for microphone alarm settings when switching profiles via add-on settings dialog.
* You can now press SPL Controller, H to obtain help for SPL Controller layer.

## Version 17.10

* If using Windows releases prior to Windows 7 Service Pack 1, you cannot switch to Test Drive Fast update channel. A future release of this add-on will move users of old Windows versions to a dedicated support channel.
* Several general settings such as status announcement beeps, top and bottom of playlist notification and others are now located in the new general add-on settings dialog (accessed from a new button in add-on settings).
* It is now possible to make add-on options read-only, use only the normal profile, or not load settings from disk when Studio starts. These are controlled by new command-line switches specific to this add-on.
* When running NVDA from Run dialog (Windows+R), you can now pass in additional command-line switches to change how the add-on works. These include "--spl-configvolatile" (read-only settings), "--spl-configinmemory" (do not load settings from disk), and "--spl-normalprofileonly" (only use normal profile).
* If exitting Studio (not NVDA) while an instant switch profile is active, NVDA will no longer give misleading announcement when switching to an instant switch profile when using Studio again.

## Version 17.09.1

* As a result of announcement from NV Access that NVDA 2017.3 will be the last version to support Windows versions prior to windows 7 Service Pack 1, Studio add-on will present a reminder message about this if running from old Windows releases. End of support for old Windows releases from this add-on (via long-term support release) is scheduled for April 2018.
* NVDA will no longer display startup dialogs and/or announce Studio version if started with minimal (nvda -rm) flag set. The sole exception is the old Windows release reminder dialog.

## Version 17.09

* If a user enters advanced options dialog under add-on settings while the update channel and interval was set to Test Drive Fast and/or zero days, NVDA will no longer present the channel and/or interval warning message when exitting this dialog.
* Playlist remainder and trakc time analysis commands will now require that a playlist be loaded, and a more accurate error message will be presented otherwise.

## Version 17.08.1

* NVDA will no longer fail to cause Studio to play the first track when an encoder is connected.

## Version 17.08

* Changes to update channel labels: try build is now Test Drive Fast, development channel is Test Drive Slow. The true "try" builds will be reserved for actual try builds that require users to manually install a test version.
* Update interval can now be set to 0 (zero) days. This allows the add-on to check for updates when NVDA and/or SPL Studio starts. A confirmation will be required to change update interval to zero days.
* NVDA will no longer fail to check for add-on updates if update interval is set to 25 days or longer.
* In add-on settings, added a checkbox to let NVDA play a sound when listener requests arrive. To use this fully, requests window must pop up when requests arrive.
* Pressing broadcaster time command (NVDA+Shift+F12) twice will now cause NVDA to announce minutes and seconds remaining in the current hour.
* It is now possible to use Track Finder (Control+NVDA+F) to search for names of tracks you've searched before by selecting a search term from a history of terms.
* When announcing title of current and next track via SPL Assistant, it is now possible to include information about which Studio internal player will play the track (e.g. player 1).
* Added a setting in add-on settings under status announcements to include player information when announcing title of the current and the next track.
* Fixed an issue in temporary cue and other dialogs where NVDA would not announce new values when manipulating time pickers.
* NVDA can suppress announcement of column headers such as Artist and Category when reviewing tracks in playlist viewer. This is a broadcast profile specific setting.
* Added a checkbox in add-on settings dialog to suppress announcement of column headers when reviewing tracks in playlist viewer.
* Added a command in SPL Controller layer to announce name and duration of the currently playing track from anywhere (C).
* When obtaining status information via SPL Controller (Q) while using Studio 5.1x, information such as microphone status, cart edit mode and others will also be announced in addition to playback and automation.

## Older releases

Please see changelog link for release notes for old add-on releases.

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: https://addons.nvda-project.org/files/get.php?file=spl-lts18

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
