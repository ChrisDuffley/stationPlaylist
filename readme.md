# StationPlaylist #

* Authors: Christopher Duffley <nvda@chrisduffley.com> (formerly Joseph Lee <joseph.lee22590@gmail.com>, originally by Geoff Shang and other contributors)

This add-on package provides improved usage of StationPlaylist Studio and other StationPlaylist apps, as well as providing utilities to control Studio from anywhere. Supported apps include Studio, Creator, Track Tool, VT Recorder, and Streamer, as well as SAM, SPL, and AltaCast encoders.

For more information about the add-on, read the [add-on guide][1].

IMPORTANT NOTES:

* This add-on requires StationPlaylist suite 5.50 or later.
* Some add-on features will be disabled or limited if NVDA is running in secure mode such as in logon screen.
* For best experience, disable audio ducking mode.
* Starting from 2018, [changelogs for old add-on releases][2] will be found on GitHub. This add-on readme will list changes from version 23.02 (2023) onwards.
* While Studio is running, you can save, reload saved settings, or reset add-on settings to defaults by pressing Control+NVDA+C, Control+NVDA+R once, or Control+NVDA+R three times, respectively. This is also applicable to encoder settings - you can save and reset (not reload) encoder settings if using encoders.
* Many commands will provide speech output while NVDA is in speak on demand mode (NVDA 2024.1 and later).

## Shortcut keys

Most of these will work in Studio only unless otherwise specified. Unless noted otherwise, these commands support speak on demand mode.

* Alt+Shift+T from Studio window: announce elapsed time for the currently playing track.
* Control+Alt+T (two finger flick down in SPL touch mode) from Studio window: announce remaining time for the currently playing track.
* NVDA+Shift+F12 (two finger flick up in SPL touch mode) from Studio window: announces broadcaster time such as 5 minutes to top of the hour. Pressing this command twice will announce minutes and seconds till top of the hour.
* Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens alarms category in Studio add-on configuration dialog (does not support speak on demand).
* Alt+NVDA+1 from Creator's Playlist Editor and Remote VT playlist editor: Announces scheduled time for the loaded playlist.
* Alt+NVDA+2 from Creator's Playlist Editor and Remote VT playlist editor: Announces total playlist duration.
* Alt+NVDA+3 from Studio window: Toggles cart explorer to learn cart assignments (does not support speak on demand).
* Alt+NVDA+3 from Creator's Playlist Editor and Remote VT playlist editor: Announces when the selected track is scheduled to play.
* Alt+NVDA+4 from Creator's Playlist Editor and Remote VT playlist editor: Announces rotation and category associated with the loaded playlist.
* Control+NVDA+F from Studio window: Opens a dialog to find a track based on artist or song name. Press NVDA+F3 to find forward or NVDA+Shift+F3 to find backward (does not support speak on demand).
* Alt+NVDA+R from Studio window: Steps through library scan announcement settings (does not support speak on demand).
* Control+Shift+X from Studio window: Steps through braille timer settings (does not support speak on demand).
* Control+Alt+left/right arrow (while focused on a track in Studio, Creator, Remote VT, and Track Tool): Move to previous/next track column (does not support speak on demand).
* Control+Alt+up/down arrow (while focused on a track in Studio, Creator, Remote VT, and Track Tool): Move to previous/next track and announce specific columns (does not support speak on demand).
* Control+NVDA+1 through 0 (while focused on a track in Studio, Creator (including Playlist Editor), Remote VT, and Track Tool): Announce column content for a specified column (first ten columns by default). Pressing this command twice will display column information on a browse mode window.
* Control+NVDA+- (hyphen while focused on a track in Studio, Creator, Remote VT, and Track Tool): display data for all columns in a track on a browse mode window (does not support speak on demand).
* NVDA+V while focused on a track (Studio's playlist viewer only): toggles track column announcement between screen order and custom order (does not support speak on demand).
* Alt+NVDA+C while focused on a track (Studio's playlist viewer only): announces track comments if any.
* Alt+NVDA+0 from Studio window: Opens the Studio add-on configuration dialog (does not support speak on demand).
* Alt+NVDA+P from Studio window: Opens the Studio broadcast profiles dialog (does not support speak on demand).
* Alt+NVDA+F1: Open welcome dialog (does not support speak on demand).

## Unassigned commands

The following commands are not assigned by default; if you wish to assign them, use Input Gestures dialog to add custom commands. To do so, from Studio window, open NVDA menu, Preferences, then Input Gestures. Expand StationPlaylist category, then locate unassigned commands from the list below and select "Add", then type the gesture you wish to use.

Important: some of these commands will not work if NVDA is running in secure mode such as from login screen. Not all commands support speak on demand.

* Switching to SPL Studio window from any program (unavailable in secure mode, does not support speak on demand).
* SPL Controller layer (unavailable in secure mode).
* Announcing Studio status such as track playback from other programs (unavailable in secure mode).
* Announcing encoder connection status from any program (unavailable in secure mode).
* SPL Assistant layer from SPL Studio.
* Announce time including seconds from SPL Studio.
* Announcing temperature.
* Announcing title of next track if scheduled.
* Announcing title of the currently playing track.
* Marking current track for start of track time analysis.
* Performing track time analysis.
* Take playlist snapshots.
* Find text in specific columns (does not support speak on demand).
* Find tracks with duration that falls within a given range via time range finder (does not support speak on demand).
* Quickly enable or disable metadata streaming (does not support speak on demand).

## Additional commands when using encoders

The following commands are available when using encoders, and the ones used for toggling options for on-connection behavior such as focusing to Studio, playing the first track, and toggling of background monitoring can be assigned through the Input Gestures dialog in NVDA menu, Preferences, Input Gestures, under the StationPlaylist category. These commands do not support speak on demand.

* F9: connect the selected encoder.
* F10 (SAM encoder only): Disconnect the selected encoder.
* Control+F9: Connect all encoders.
* Control+F10 (SAM encoder only): Disconnect all encoders.
* Control+Shift+F11: Toggles whether NVDA will switch to Studio window for the selected encoder if connected.
* Shift+F11: Toggles whether Studio will play the first selected track when encoder is connected to a streaming server.
* Control+F11: Toggles background monitoring of the selected encoder.
* Control+F12: opens a dialog to select the encoder you have deleted (to realign encoder labels and settings).
* Alt+NVDA+0 or F12: Opens encoder settings dialog to configure options such as encoder label.

In addition, column review commands are available, including (supports speak on demand):

* Control+NVDA+1: Encoder position.
* Control+NVDA+2: encoder label.
* Control+NVDA+3 from SAM Encoder: Encoder format.
* Control+NVDA+3 from SPL and AltaCast Encoder: Encoder settings.
* Control+NVDA+4 from SAM Encoder: Encoder connection status.
* Control+NVDA+4 from SPL and AltaCast Encoder: Transfer rate or connection status.
* Control+NVDA+5 from SAM Encoder: Connection status description.

## SPL Assistant layer

This layer command set allows you to obtain various status on SPL Studio, such as whether a track is playing, total duration of all tracks for the hour and so on. From any SPL Studio window, press the SPL Assistant layer command, then press one of the keys from the list below (one or more commands are exclusive to playlist viewer). You can also configure NVDA to emulate commands from other screen readers.

The available commands are (most commands support speak on demand):

* A: Automation.
* C (Shift+C  in JAWS layout): Title for the currently playing track.
* C (JAWS layout): Toggle cart explorer (playlist viewer only, does not support speak on demand).
* D (R in JAWS layout): Remaining duration for the playlist (if an error message is given, move to playlist viewer and then issue this command).
* Control+D (Studio 6.10 and later): Control keys enabled/disabled.
* E: Metadata streaming status.
* Shift+1 through Shift+4, Shift+0: Status for individual metadata streaming URL's (0 is for DSP encoder).
* F: Find track (playlist viewer only, does not support speak on demand).
* H: Duration of music for the current hour slot.
* Shift+H: Remaining track duration for the hour slot.
* I (L in JAWS layout): Listener count.
* K: Move to the marked track (playlist viewer only).
* Control+K: Set the current track as the place marker track (playlist viewer only).
* L (Shift+L in JAWS layout): Line in.
* M: Microphone.
* N: Title for the next scheduled track.
* O: Playlist hour over/under by.
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

## SPL Controller

The SPL Controller is a set of layered commands you can use to control SPL Studio anywhere. Press the SPL Controller layer command, and NVDA will say, "SPL Controller." Press another command to control various Studio settings such as microphone on/off or play the next track.

Important: SPL Controller layer commands are disabled if NVDA is running in secure mode.

The available SPL Controller commands are (some commands support speak on demand):

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
* C: Title and duration of the currently playing track (supports speak on demand).
* Shift+C: Title and duration of the upcoming track if any (supports speak on demand).
* E: Encoder connection status (supports speak on demand).
* I: Listener count (supports speak on demand).
* Q: Studio status information such as whether a track is playing, microphone is on and others (supports speak on demand).
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

From studio window, you can press Alt+NVDA+0 to open the add-on configuration dialog. Alternatively, go to NVDA's preferences menu and select SPL Studio Settings item. Not all settings are available if NVDA is running in secure mode.

## Broadcast profiles dialog

You can save settings for specific shows into broadcast profiles. These profiles can be managed via SPL broadcast profiles dialog which can be accessed by pressing Alt+NVDA+P from Studio window.

## SPL touch mode

If you are using Studio on a touchscreen computer with NVDA installed, you can perform some Studio commands from the touchscreen. First use three finger tap to switch to SPL mode, then use the touch commands listed above to perform commands.

## Version 25.06-LTS

Version 25.06.x is the last release series to support Studio 5.x with future releases requiring Studio 6.x. Some new features will be backported to 25.06.x if needed.

* Added a new command in SPL Assistant to announce playlist hour over/under by in minutes and seconds (O).
* NVDA will no longer play wrong carts when playing them via SPL Controller layer.

## Version 25.05

* NVDA 2024.1 or later is required due to Python 3.11 upgrade.
* Restored limited support for Windows 8.1.
* Moved ad-on wiki documents such as add-on changelog to the main code repository.
* Added close button to playlist snapshots, playlist transcripts, and SPL Assistant and Controller layer help screens (NVDA 2025.1 and later).
* NVDA will no longer do nothing or play error tones when announcing weather and temperature information in Studio 6.x (SPL Assistant, W).

## Version 25.01

* 64-bit Windows 10 21H2 (build 19044) or later is required.
* Download links for add-on releases are no longer included in add-on documentation. You can download the add-on from NV Access add-on store.
* Switched linting tool from Flake8 to Ruff and reformatted add-on modules to better align with NVDA coding standards.
* Removed support for automatic add-on updates feature from Add-on Updater add-on.
* In Studio 6.10 and later, added a new command in SPL Assistant to announce control keys enabled/disabled status (Control+D).

## Version 24.03

* Compatible with NVDA 2024.1.
* NVDA 2023.3.3 or later is required.
* Support for StationPlaylist suite 6.10.
* Most commands support speak on demand (NVDA 2024.1) so announcements can be spoken in this mode.

## Version 24.01

* The commands for the Encoder Settings dialog for use with the SPL and SAM Encoders are now assignable, meaning that you can change them from their defaults under the StationPlaylist category in NVDA Menu > Preferences > Input Gestures. The ones that are not assignable are the connect and disconnect commands. Also, to prevent command conflicts and make much easier use of this command on remote servers, the default gesture for switching to Studio after connecting is now Control+Shift+F11 (previously just F11). All of these can of course still be toggled from the Encoder Settings dialog (NVDA+Alt+0 or F12).

## Version 23.05

* To reflect the maintainer change, the manifest has been updated to indicate as such.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.
* In Studio's playlist viewer, NVDA will not announce column headers such as artist and title if table headers setting is set to either "rows and columns" or "columns" in NVDA's document formatting settings panel.

## Older releases

Please see the [changelog][2] for release notes for old add-on releases.

[1]: https://github.com/ChrisDuffley/stationPlaylist/blob/main/addonuserguide.md

[2]: https://github.com/ChrisDuffley/stationPlaylist/blob/main/changes.md
