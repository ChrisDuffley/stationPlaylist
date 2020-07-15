# StationPlaylist #

* Authors: Geoff Shang, Joseph Lee and other contributors
* Download [stable version][1]
* Download [development version][2]
* NVDA compatibility: 2019.3 to 2020.2

This add-on package provides improved usage of StationPlaylist Studio and other StationPlaylist apps, as well as providing utilities to control Studio from anywhere. Supported apps include Studio, Creator, Track Tool, VT Recorder, and Streamer, as well as SAM, SPL, and AltaCast encoders.

For more information about the add-on, read the [add-on guide][4]. For developers seeking to know how to build the add-on, see buildInstructions.txt located at the root of the add-on source code repository.

IMPORTANT NOTES:

* This add-on requires StationPlaylist suite 5.20 or later.
* If using Windows 8 or later, for best experience, disable audio ducking mode.
* Starting from 2018, [changelogs for old add-on releases][5] will be found on GitHub. This add-on readme will list changes from version 18.09 (2018 onwards).
* Certain add-on features won't work under some conditions, including running NVDA in secure mode.
* Due to tecnical limitations, you cannot install or use this add-on on Windows Store version of NVDA.
* Features marked as "experimental" are meant to test something before a wider release, so they will not be enabled in stable releases.
* While Studio is running, you can save, reload saved settings, or reset add-on settings to defaults by pressing Control+NVDA+C, Control+NVDA+R once, or Control+NVDA+R three times, respectively. This is also applicable to encoder settings - you can save and reset (not reload) encoder settings if using encoders.

## Shortcut keys

Most of these will work in Studio only unless otherwise specified.

* Alt+Shift+T from Studio window: announce elapsed time for the currently playing trakc.
* Control+Alt+T (two finger flick down in SPL touch mode) from Studio window: announce remaining time for the currently playing trakc.
* NVDA+Shift+F12 (two finger flick up in SPL touch mode) from Studio window: announces broadcaster time such as 5 minutes to top of the hour. Pressing this command twice will announce minutes and seconds till top of the hour.
* Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens alarms category in Studio add-on configuration dialog.
* Alt+NVDA+1 from Creator's Playlist Editor and Remote VT playlist editor: Announces scheduled time for the loaded playlist.
* Alt+NVDA+2 from Creator's Playlist Editor and Remote VT playlist editor: Announces total playlist duration.
* Alt+NVDA+3 from Studio window: Toggles cart explorer to learn cart assignments.
* Alt+NVDA+3 from Creator's Playlist Editor and Remote VT playlist editor: Announces when the selected track is scheduled to play.
* Alt+NVDA+4 from Creator's Playlist Editor and Remote VT playlist editor: Announces rotation and category associated with the loaded playlist.
* Control+NVDA+f from Studio window: Opens a dialog to find a track based on artist or song name. Press NVDA+F3 to find forward or NVDA+Shift+F3 to find backward.
* Alt+NVDA+R from Studio window: Steps through library scan announcement settings.
* Control+Shift+X from Studio window: Steps through braille timer settings.
* Control+Alt+left/right arrow (while focused on a track in Studio, Creator, Remote VT, and Track Tool): Move to previous/next track column.
* Control+Alt+Home/End (while focused on a track in Studio, Creator, Remote VT, and Track Tool): Move to first/last track column.
* Control+Alt+up/down arrow (while focused on a track in Studio, Creator, Remote VT, and Track Tool): Move to previous/next track and announce specific columns.
* Control+NVDA+1 through 0 (while focused on a track in Studio, Creator (including Playlist Editor), Remote VT, and Track Tool): Announce column content for a specified column (first ten columns by default). Pressing this command twice will display column information on a browse mode window.
* Control+NVDA+- (hyphen while focused on a track in Studio, Creator, Remote VT, and Track Tool): display data for all columns in a track on a browse mode window.
* Alt+NVDA+C while focused on a track (Studio only): announces track comments if any.
* Alt+NVDA+0 from Studio window: Opens the Studio add-on configuration dialog.
* Alt+NVDA+P from Studio window: Opens the Studio broadcast profiles dialog.
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

* F9: connect the selected encoder.
* F10 (SAM encoder only): Disconnect the selected encoder.
* Control+F9: Connect all encoders.
* Control+F10 (SAM encoder only): Disconnect all encoders.
* F11: Toggles whether NVDA will switch to Studio window for the selected encoder if connected.
* Shift+F11: Toggles whether Studio will play the first selected track when encoder is connected to a streaming server.
* Control+F11: Toggles background monitoring of the selected encoder.
* Control+F12: opens a dialog to select the encoder you have deleted (to realign encoder labels and settings).
* Alt+NVDA+0: Opens encoder settings dialog to configure options such as encoder label.

In addition, column review commands are available, including:

* Control+NVDA+1: Encoder position.
* Control+NVDA+2: encoder label.
* Control+NVDA+3 from SAM Encoder: Encoder format.
* Control+NVDA+3 from SPL and AltaCast Encoder: Encoder settings.
* Control+NVDA+4 from SAM Encoder: Encoder connection status.
* Control+NVDA+4 from SPL and AltaCast Encoder: Transfer rate or connection status.
* Control+NVDA+5 from SAM Encoder: Connection status description.

## SPL Assistant layer

This layer command set allows you to obtain various status on SPL Studio, such as whether a track is playing, total duration of all tracks for the hour and so on. From any SPL Studio window, press the SPL Assistant layer command, then press one of the keys from the list below (one or more commands are exclusive to playlist viewer). You can also configure NVDA to emulate commands from other screen readers.

The available commands are:

* A: Automation.
* C (Shift+C  in JAWS layout): Title for the currently playing track.
* C (JAWS layout): Toggle cart explorer (playlist viewer only).
* D (R in JAWS layout): Remaining duration for the playlist (if an error message is given, move to playlist viewer and then issue this command).
* E: Metadata streaming status.
* Shift+1 through Shift+4, Shift+0: Status for individual metadata streaming URL's (0 is for DSP encoder).
* F: Find track (playlist viewer only).
* H: Duration of music for the current hour slot.
* Shift+H: Remaining track duration for the hour slot.
* I (L in JAWS layout): Listener count.
* K: Move to the marked track (playlist viewer only).
* Control+K: Set the current track as the place marker track (playlist viewer only).
* L (Shift+L in JAWS layout): Line in.
* M: Microphone.
* N: Title for the next scheduled track.
* P: Playback status (playing or stopped).
* Shift+P: Pitch of the current track.
* R (Shift+E in JAWS layout): Record to file enabled/disabled.
* Shift+R: Monitor library scan in progress.
* S: Track starts (scheduled).
* Shift+S: Time until selected track will play (track starts in).
* T: Cart edit/insert mode on/off.
* U: Studio up time.
* W: Weather and temperature if configured.
* Y: Playlist modified status.
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

## Track and microphone alarms

By default, NVDA will play a beep if five seconds are left in the track (outro) and/or intro, as well as to hear a beep if microphone has been active for a while. To configure track and microphone alarms, press Alt+NVDA+1 to open alarms settings in Studio add-on settings screen. You can also use this screen to configure if you'll hear a beep, a message or both when alarms are turned on.

## Track Finder

If you wish to quickly find a song by an artist or by song name, from track list, press Control+NVDA+F. Type or choose the name of the artist or the song name. NVDA will either place you at the song if found or will display an error if it cannot find the song you're looking for. To find a previously entered song or artist, press NVDA+F3 or NVDA+Shift+F3 to find forward or backward.

Note: Track Finder is case-sensitive.

## Cart Explorer

Depending on edition, SPL Studio allows up to 96 carts to be assigned for playback. NVDA allows you to hear which cart, or jingle is assigned to these commands.

To learn cart assignments, from SPL Studio, press Alt+NVDA+3. Pressing the cart command once will tell you which jingle is assigned to the command. Pressing the cart command twice will play the jingle. Press Alt+NVDA+3 to exit cart explorer. See the add-on guide for more information on cart explorer.

## Track time analysis

To obtain length to play selected tracks, mark current track for start of track time analysis (SPL Assistant, F9), then press SPL Assistant, F10 when reaching end of selection.

## Columns Explorer

By pressing Control+NVDA+1 through 0, you can obtain contents of specific columns. By default, these are first ten columns for a track item (in Studio: artist, title, duration, intro, outro, category, year, album, genre, mood). For playlist editor in Creator and Remote VT client, column data depends on column order as shown on screen. In Studio, Creator's main track list, and Track Tool, column slots are preset regardless of column order on screen and can be configured from add-on settings dialog under columns explorer category.

## Playlist snapshots

You can press SPL Assistant, F8 while focused on a playlist in Studio to obtain various statistics about a playlist, including number of tracks in the playlist, longest track, top artists and so on. After assigning a custom command for this feature, pressing the custom command twice will cause NVDA to present playlist snapshot information as a webpage so you can use browse mode to navigate (press escape to close).

## Playlist Transcripts

Pressing SPL Assistant, Shift+F8 will present a dialog to let you request playlist transcripts in numerous formats, including in a plain text format, an HTML table or a list.

## Configuration dialog

From studio window, you can press Alt+NVDA+0 to open the add-on configuration dialog. Alternatively, go to NVDA's preferences menu and select SPL Studio Settings item. This dialog is also used to manage broadcast profiles.

## Broadcast profiles dialog

You can save settings for specific shows into broadcast profiles. These profiles can be managed via SPL broadcast profiles dialog which can be accessed by pressing Alt+NVDA+P from Studio window.

## SPL touch mode

If you are using Studio on a touchscreen computer running Windows 8 or later and have NVDA 2012.3 or later installed, you can perform some Studio commands from the touchscreen. First use three finger tap to switch to SPL mode, then use the touch commands listed above to perform commands.

## Version 20.09

* Due to changes in NVDA, --spl-configvolatile command line switch is no longer availible to make add-on settings read-only. You can emulate this by unchecking "Save configuration when exiting NVDA" checkbox from NVDA's general settings panel.
* Removed pilot features setting from Advanced settings category under add-on settings (Alt+NvDA+0), used to let development snapshot users test bleeding-ege code.
* Column navigation commands in Studio are now availible in track lists found in listener requests, insert tracks and other screens.
* Various column navigation commands will behave like NVDA's own table navigation commands. Besides simplifying these commands, it brings benefits such as ease of use by low vision users.
* Vertical column navigation (Control+Alt+up/down arrow) commands are now availible for Creator, playlist editor, Remote VT, and Track Tool.
* Track columns viewer command (Control+NVDA+hyphen) is now availible in Creator's Playlist Editor and Remote VT.
* Track columns viewer command will respect column order displayed on screen.
* In SAM encoders, improved NVDA's responsivness when pressing Control+F9 or Control+F10 to connect or disconnect all encoders, respectively. This may result in increased verbosity when announcing the selected encoder information.
* In SPL and AltaCast encoders, pressing F9 will now connect the selected encoder.

## Version 20.07

* In Studio's playlist viewer, NVDA will no longer appear to do nothing or play error tones when attempting to delete tracks or after clearing the loaded playlist while focused on playlist viewer.
* When searching for tracks in Studio's insert tracks dialog, NVDA will announce search results if results are found.
* NVDA will no longer appear to do nothing or play error tones when trying to switch to a newly created broadcast profile and save add-on settings.
* In encoder settings, "stream label" has been renamed to "encoder label".
* Dedicated stream labeler command (F12) has been removed from encoders. Encoder labels can be defined from encoder settings dialog (Alt+NVDA+0).
* System focus will no longer move to Studio repeatedly or selected track will be played when an encoder being monitored in the background (Control+F11) connects and disconnects repeatedly.
* In SPL encoders, added Control+F9 command to connect all encoders (same as F9 command).

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.
* Fixed many instances of encoders support feature messages spoken in English despite translated into other languages.
* Time-based broadcast profiles feature has been removed.
* Window-Eyes command layout for SPL Assistant has been removed. Window-Eyes command layout users will be migrated to NVDA layout.
* As audio ducking feature in NVDA does not impact streaming from Studio except for specific hardware setups, audio ducking reminder dialog has been removed.
* When errors are found in encoder settings, it is no longer necessary to switch to Studio window to let NVDA reset settings to defaults. You must now switch to an encoder from encoders window to let NVDA reset encoder settings.
* The title of encoder settings dialog for SAM encoders now displays encoder format rather than encoder position.

## Version 20.05

* Initial support for Remote VT (voice track) client, including remote playlist editor with same commands as Creator's playlist editor.
* Commands used to open separate alarm settings dialogs (Alt+NVDA+1, Alt+NVDA+2, Alt+NVDA+4) has been combined into Alt+NvDA+1 and will now open alarms settings in SPL add-on settings screen where track outro/intro and microphone alarm settings can be found.
* In triggers dialog found in broadcast profiles dialog, removed the user interface associated with time-based broadcast profiles feature such as profile switch day/time/duration fields.
* Profile switch countdown setting found in broadcast profiles dialog has been removed.
* As Window-Eyes is no longer supported by Vispero since 2017, SPL Assistant command layout for Window-Eyes is deprecated and will be removed in a future add-on release. A warning will be shown at startup urging users to change SPL Assistant command layout to NVDA (default) or JAWS.
* When using Columns Explorer slots (Control+NvDA+number row commands) or column navigation commands (Control+Alt+home/end/left arrow/right arrow) in Creator and Remote VT client, NVDA will no longer announce wrong column data after changing column position on screen via mouse.
* In encoders and Streamer, NVDA will no longer appear to do nothing or play error tones when exiting NVDA while focused on something other than encoders list without moving focus to encoders first.

## Version 20.04

* Time-based broadcast profiles feature is deprecated. A warning message will be shown when first starting Studio after installing add-on 20.04 if you have defined one or more time-based broadcast profiles.
* Broadcast profiles management has been split from SPL add-on settings dialog into its own dialog. You can access broadcast profiles dialog by pressing Alt+NVDA+P from Studio window.
* Due to duplication with Control+NVDA+number row commands for Studio tracks, columns explorer commands from SPL Assistant (number row) has been removed.
* Changed error message shown when trying to open a Studio add-on settings dialog (such as metadata streaming dialog) while another settings dialog (such as end of track alarm dialog) is active. The new error message is same as the message shown when trying to open multiple NVDA settings dialogs.
* NVDA will no longer play error tones or appear to do nothing when clicking OK button from Columns Explorer dialog after configuring column slots.
* In encoders, you can now save and reset encoder settings (including stream labels) by pressing Control+NVDA+C or Control+NVDA+R three times, respectively.

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
* 19.03 experimental: in column announcements and playlist transcripts panels (add-on settings), custom column inclusion/order controls will be visible up front instead of having to select a button to open a dialog to configure these settings.

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

## Older releases

Please see changelog link for release notes for old add-on releases.

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
