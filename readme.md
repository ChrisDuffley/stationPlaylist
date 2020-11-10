# StationPlaylist #

* Authors: Geoff Shang, Joseph Lee and other contributors
* Download [stable version][1]
* Download [development version][2]
* Download [long-term support version][3] - for Studio 5.20 users
* NVDA compatibility: 2020.3

This add-on package provides improved usage of StationPlaylist Studio and other StationPlaylist apps, as well as providing utilities to control Studio from anywhere. Supported apps include Studio, Creator, Track Tool, VT Recorder, and Streamer, as well as SAM, SPL, and AltaCast encoders.

For more information about the add-on, read the [add-on guide][4]. For developers seeking to know how to build the add-on, see buildInstructions.txt located at the root of the add-on source code repository.

IMPORTANT NOTES:

* This add-on requires StationPlaylist suite 5.20 or later.
* If using Windows 8 or later, for best experience, disable audio ducking mode.
* Starting from 2018, [changelogs for old add-on releases][5] will be found on GitHub. This add-on readme will list changes from version 20.01 (2020) onwards.
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
* Alt+NVDA+0 and F12: Opens encoder settings dialog to configure options such as encoder label.

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

## Version 21.01

* NVDA 2020.3 or later is required.
* Column header inclusion setting from add-on settings has been removed. NVDA's own table column header setting will control column header announcements across SPL suite and encoders.

## Version 20.11.1/20.09.4-LTS

* Initial support for StationPlaylist suite 5.50.
* Improvements to presentation of various add-on dialogs thanks to NVDA 2020.3 features.

## Version 20.11/20.09.3-LTS

* 20.11: NVDA 2020.1 or later is required.
* 20.11: Resolved more coding style issues and potential bugs with Flake8.
* Fixed various issues with add-on welcome dialog (Alt+NVDA+F1 from Studio), including wrong command shown for add-on feedback (Alt+NVDA+Hyphen).
* 20.11: Column presentation format for track and encoder items across StationPlaylist suite (including SAM encoder) is now based on SysListView32 list item format.
* 20.11: NVDA will now announce column information for tracks throughout SPL suite regardless of "report object description" setting in NVDA's object presentation settings panel. For best experience, leave this setting on.
* 20.11: In Studio's playlist viewer, custom column order and inclusion setting will affect how track columns are presented when using object navigation to move between tracks, including current navigator object announcement.
* If vertical column announcement is set to a value other than "whichever column I'm reviewing", NVDA will no longer announce wrong column data after changing column position on screen via mouse.
* improved playlist transcripts (SPL Assistant, Shift+F8) presentation when viewing the transcript in HTML table or list format.
* 20.11: In encoders, encoder labels will be announced when performing object navigation commands in addition to pressing up or down arrow keys to move between encoders.
* In encoders, in addition to Alt+NVDA+number row 0, pressing F12 will also open encoder settings dialog for the selected encoder.

## Version 20.10/20.09.2-LTS

* Due to changes to encoder settings file format, installing an older version of this add-on after installing this version will cause unpredictable behavior.
* It is no longer necessary to restart NVDA with debug logging mode to read debug messages from log viewer. You can view debug messages if log level is set to "debug" from NVDA's general settings panel.
* In Studio's playlist viewer, NVDA will not include column headers if this setting is disabled from add-on settings and custom column order or inclusion settings are not defined.
* 20.10: column header inclusion setting from add-on settings is deprecated and will be removed in a future release. In the future NVDA's own table column header setting will control column header announcements across SPL suite and encoders.
* When SPL Studio is minimized to the system tray (notification area), NVDA will announce this fact when trying to switch to Studio from other programs either through a dedicated command or as a result of an encoder connecting.

## Version 20.09-LTS

Version 20.09.x is the last release series to support Studio 5.20 and based on old technologies, with future releases supporting Studio 5.30 and more recent NVDA features. Some new features will be backported to 20.09.x if needed.

* Due to changes in NVDA, --spl-configvolatile command line switch is no longer available to make add-on settings read-only. You can emulate this by unchecking "Save configuration when exiting NVDA" checkbox from NVDA's general settings panel.
* Removed pilot features setting from Advanced settings category under add-on settings (Alt+NVDA+0), used to let development snapshot users test bleeding-edge code.
* Column navigation commands in Studio are now available in track lists found in listener requests, insert tracks and other screens.
* Various column navigation commands will behave like NVDA's own table navigation commands. Besides simplifying these commands, it brings benefits such as ease of use by low vision users.
* Vertical column navigation (Control+Alt+up/down arrow) commands are now available for Creator, playlist editor, Remote VT, and Track Tool.
* Track columns viewer command (Control+NVDA+hyphen) is now available in Creator's Playlist Editor and Remote VT.
* Track columns viewer command will respect column order displayed on screen.
* In SAM encoders, improved NVDA's responsiveness when pressing Control+F9 or Control+F10 to connect or disconnect all encoders, respectively. This may result in increased verbosity when announcing the selected encoder information.
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
* Commands used to open separate alarm settings dialogs (Alt+NVDA+1, Alt+NVDA+2, Alt+NVDA+4) has been combined into Alt+NVDA+1 and will now open alarms settings in SPL add-on settings screen where track outro/intro and microphone alarm settings can be found.
* In triggers dialog found in broadcast profiles dialog, removed the user interface associated with time-based broadcast profiles feature such as profile switch day/time/duration fields.
* Profile switch countdown setting found in broadcast profiles dialog has been removed.
* As Window-Eyes is no longer supported by Vispero since 2017, SPL Assistant command layout for Window-Eyes is deprecated and will be removed in a future add-on release. A warning will be shown at startup urging users to change SPL Assistant command layout to NVDA (default) or JAWS.
* When using Columns Explorer slots (Control+NVDA+number row commands) or column navigation commands (Control+Alt+home/end/left arrow/right arrow) in Creator and Remote VT client, NVDA will no longer announce wrong column data after changing column position on screen via mouse.
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
* In encoders, NVDA will play connection tone every half a second while an encoder is connecting.
* In encoders, NVDA will now announce connection attempt messages until an encoder is actually connected. Previously NVDA stopped when an error was encountered.
* A new setting has been added to encoder settings to let NVDA announce connection messages until the selected encoder is connected. This setting is enabled by default.

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

## Older releases

Please see changelog link for release notes for old add-on releases.

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: https://addons.nvda-project.org/files/get.php?file=spl-lts20

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
