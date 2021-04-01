# StationPlaylist #

* Authors: Geoff Shang, Joseph Lee and other contributors
* Download [stable version][1]
* Download [development version][2]
* Download [long-term support version][3] - for Studio 5.20 users
* NVDA compatibility: 2020.4

This add-on package provides improved usage of StationPlaylist Studio and other StationPlaylist apps, as well as providing utilities to control Studio from anywhere. Supported apps include Studio, Creator, Track Tool, VT Recorder, and Streamer, as well as SAM, SPL, and AltaCast encoders.

For more information about the add-on, read the [add-on guide][4].

IMPORTANT NOTES:

* This add-on requires StationPlaylist suite 5.30 (5.20 for 20.09.x-LTS) or later.
* If using Windows 8 or later, for best experience, disable audio ducking mode.
* Starting from 2018, [changelogs for old add-on releases][5] will be found on GitHub. This add-on readme will list changes from version 20.09 (2020) onwards.
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
* NVDA+V while focused on a track (Studio's playlist viewer only): toggles track column announcement between screen order and custom order.
* Alt+NVDA+C while focused on a track (Studio's playlist viewer only): announces track comments if any.
* Alt+NVDA+0 from Studio window: Opens the Studio add-on configuration dialog.
* Alt+NVDA+P from Studio window: Opens the Studio broadcast profiles dialog.
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

* P: Play the next selected track.
* U: Pause or unpause playback.
* S: Stop the track with fade out.
* T: Instant stop.
* M: Turn on microphone.
* Shift+M: Turn off microphone.
* A: Turn on automation.
* Shift+A: Turn off automation.
* L: Turn on line-in input.
* Shift+L: Turn off line-in input.
* R: Remaining time for the currently playing track.
* Shift+R: Library scan progress.
* C: Title and duration of the currently playing track.
* Shift+C: Title and duration of the upcoming track if any.
* E: Encoder connection status.
* I: Listener count.
* Q: Studio status information such as whether a track is playing, microphone is on and others.
* Cart keys (F1, Control+1, for example): Play assigned carts from anywhere.
* H: Layer help.

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

## Track column announcement

You can ask NVDA to announce track columns found in Studio's playlist viewer in the order it appears on screen or using a custom order and/or exclude certain columns. Press NVDA+V to toggle this behavior while focused on a track in Studio's playlist viewer. To customize column inclusion and order, from column announcement settings panel in add-on settings, uncheck "Announce columns in the order shown on screen" and then customize included columns and/or column order.

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

## Version 21.04/20.09.7-LTS

* 21.04: NVDA 2020.4 or later is required.
* In encoders, NVDA no longer fails to announce date and time information when performing date/time command (NVDA+F12). This affects NVDA 2021.1 or later.

## Version 21.03/20.09.6-LTS

* Minimum Windows release requirement is now tied to NVDA releases.
* Removed feedback email command (Alt+NVDA+Hyphen). Please send feedback to add-on developers using the contact information provided from Add-ons Manager.
* 21.03: parts of the add-on source code now include type annotations.
* 21.03: made the add-on code more robust with help from Mypy (a Python static type checker). In particular, fixed several long-standing bugs such as NVDA not being able to reset add-on settings to defaults under some circumstances and attempting to save encoder settings when not loaded. Some prominent bug fixes were also backported to 20.09.6-LTS.
* Fixed numerous bugs with add-on welcome dialog (Alt+NVDA+F1 from Studio window), including multiple welcome dialogs being shown and NVDA appearing to do nothing or playing error tones when welcome dialog remains open after Studio exits.
* Fixed numerous bugs with track comments dialog (Alt+NVDA+C three times from a track in Studio), including an error tone heard when trying to save comments and many track comment dialogs appearing if Alt+NVDA+C is pressed many times. If track comments dialog is still shown after Studio is closed, comments will not be saved.
* Various column commands such as columns explorer (Control+NVDA+number row) in Studio tracks and encoder status announcements no longer gives erroneous results when performed after NVDA is restarted while focused on tracks or encoders. This affects NVDA 2020.4 or later.
* Fixed numerous issues with playlist snapshots (SPL Assistant, F8), including inability to obtain snapshot data and reporting wrong tracks as shortest or longest tracks.
* NVDA will no longer announce "0 items in the library" when Studio exits in the middle of a library scan.
* NVDA will no longer fail to save changes to encoder settings after errors are encountered when loading encoder settings and subsequently settings are reset to defaults.

## Version 21.01/20.09.5-LTS

Version 21.01 supports SPL Studio 5.30 and later.

* 21.01: NVDA 2020.3 or later is required.
* 21.01: column header inclusion setting from add-on settings has been removed. NVDA's own table column header setting will control column header announcements across SPL suite and encoders.
* Added a command to toggle screen versus custom column inclusion and order setting (NVDA+V). Note that this command is available only when focused on a track in Studio's playlist viewer.
* SPL Assistant and Controller layer help will be presented as a browse mode document instead of a dialog.
* NVDA will no longer stop announcing library scan progress if configured to announce scan progress while using a braille display.

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

## Older releases

Please see changelog link for release notes for old add-on releases.

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: https://addons.nvda-project.org/files/get.php?file=spl-lts20

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
