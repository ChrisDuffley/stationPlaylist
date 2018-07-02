# StationPlaylist Studio #

* Authors: Geoff Shang, Joseph Lee and other contributors
* Download [stable version][1]
* Download [development version][2]

This add-on package provides improved usage of StationPlaylist Studio, as well as providing utilities to control the Studio from anywhere.

For more information about the add-on, read the [add-on guide][4]. For developers seeking to know how to build the add-on, see buildInstructions.txt located at the root of the add-on source code repository.

IMPORTANT NOTES:

* This add-on requires NVDA 2017.4 or later and StationPlaylist Studio 5.10 or later.
* If using Windows 8 or later, for best experience, disable audio ducking mode.
* add-on 8.0/16.10 requires Studio 5.10 or later.
* Starting from 2018, [changelogs for old add-on releases][5] will be found on GitHub. This add-on readme will list changes from version 5.0 (2015 onwards).
* Certain add-on features (notably add-on updating) won't work under some conditions, including running NVDA in secure mode.
* Due to tecnical limitations, you cannot install or use this add-on on Windows Store version of NVDA.

## Shortcut keys

Most of these will work in Studio only unless otherwise specified.

* Alt+Shift+T from Studio window: announce elapsed time for the currently playing trakc.
* Control+Alt+T (two finger flick down in SPL touch mode) from Studio window: announce remaining time for the currently playing trakc.
* NVDA+Shift+F12 (two finger flick up in SPL touch mode) from Studio window: announces broadcaster time such as 5 minutes to top of the hour. Pressing this command twice will announce minutes and seconds till top of the hour.
* Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens end of track setting dialog.
* Alt+NVDA+2 (two finger flick left in SPL mode) from Studio window: Opens song intro alarm setting dialog.
* Alt+NVDA+3 from Studio window: Toggles cart explorer to learn cart assignments.
* Alt+NVDA+4 from Studio window: Opens microphone alarm dialog.
* Control+NVDA+f from Studio window: Opens a dialog to find a track based on artist or song name. Press NvDA+F3 to find forward or NVDA+Shift+F3 to find backward.
* Alt+NVDA+R from Studio window: Steps through library scan announcement settings.
* Control+Shift+X from Studio window: Steps through braille timer settings.
* Control+Alt+left/right arrow (while focused on a track in Studio, Creator, and Track Tool): Announce previous/next track column.
* Control+Alt+up/down arrow (while focused on a track in Studio only): Move to previous or next track and announce specific columns (unavailable in add-on 15.x).
* Control+NVDA+1 through 0 (while focused on a track in Studio, Creator, and Track Tool): Announce column content for a specified column. Pressing this command twice will display column information on a browse mode window.
* Control+NVDA+- (hyphen in Studio): display data for all columns in a track on a browse mode window.
* Alt+NVDA+C while focused on a track (Studio only): announces track comments if any.
* Alt+NVDA+0 from Studio window: Opens the Studio add-on configuration dialog.
* Alt+NVDA+- (hyphen) from Studio window: Send feedback to add-on developer using the default email client.
* Alt+NVDA+F1: Open welcome dialog.

## Unassigned commands

The following commands are not assigned by default; if you wish to assign them, use Input Gestures dialog to add custom commands.

* Switching to SPL Studio window from any program.
* SPL Controller layer.
* Announcing Studio status such as track playback from other programs.
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

## Additional commands when using Sam or SPL encoders

The following commands are available when using Sam or SPL encoders:

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
* Control+NVDA+3 from SPL Encoder: Encoder settings.
* Control+NvDA+4 from SAM Encoder: Encoder connection status.
* Control+NVDA+4 from SPL Encoder: Transfer rate or connection status.
* Control+NVDA+5 from SAM Encoder: Connection status description.

## SPL Assistant layer

This layer command set allows you to obtain various status on SPL Studio, such as whether a track is playing, total duration of all tracks for the hour and so on. From any SPL Studio window, press the SPL Assistant layer command, then press one of the keys from the list below (one or more commands are exclusive to playlist viewer). You can also configure NvDA to emulate commands from other screen readers.

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
* Control+Shift+U: Check for add-on updates.
* W: Weather and temperature if configured.
* Y: Playlist modified status.
* 1 through 0 (6 for Studio 5.0x): Announce column content for a specified column.
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
* Press E to get count and labels for encoders being monitored.
* Press I to obtain listener count.
* Press Q to obtain various status information about Studio including whether a track is playing, microphone is on and others.
* Press cart keys (F1, Control+1, for example) to play assigned carts from anywhere.
* Press H to show a help dialog which lists available commands.

## Track alarms

By default, NvDA will play a beep if five seconds are left in the track (outro) and/or intro. To configure this value as well as to enable or disable them, press Alt+NVDA+1 or Alt+NVDA+2 to open end of track and song ramp dialogs, respectively. In addition, use Studio add-on settings dialog to configure if you'll hear a beep, a message or both when alarms are turned on.

## Microphone alarm

You can ask NVDA to play a sound when microphone has been active for a while. Press Alt+NVDA+4 to configure alarm time in seconds (0 disables it).

## Track Finder

If you wish to quickly find a song by an artist or by song name, from track list, press Control+NVDA+F. Type or choose the name of the artist or the song name. NVDA will either place you at the song if found or will display an error if it cannot find the song you're looking for. To find a previously entered song or artist, press NVDA+F3 or NVDA+Shift+F3 to find forward or backward.

Note: Track Finder is case-sensitive.

## Cart Explorer

Depending on edition, SPL Studio allows up to 96 carts to be assigned for playback. NVDA allows you to hear which cart, or jingle is assigned to these commands.

To learn cart assignments, from SPL Studio, press Alt+NVDA+3. Pressing the cart command once will tell you which jingle is assigned to the command. Pressing the cart command twice will play the jingle. Press Alt+NvDA+3 to exit cart explorer. See the add-on guide for more information on cart explorer.

## Track time analysis

To obtain length to play selected tracks, mark current track for start of track time analysis (SPL Assistant, F9), then press SPL Assistant, F10 when reaching end of selection.

## Columns Explorer

By pressing Control+NVDA+1 through 0 or SPL Assistant, 1 through 0, you can obtain contents of specific columns. By default, these are artist, title, duration, intro, category, filename, year, album, genre and time scheduled. You can configure which columns will be explored via columns explorer dialog found in add-on settings dialog.

## Playlist snapshots

You can press SPL Assistant, F8 while focused on a playlist in Studio to obtain various statistics about a playlist, including number of tracks in the playlist, longest track, top artists and so on. After assigning a custom command for this feature, pressing the custom command twice will cause NVDA to present playlist snapshot information as a webpage so you can use browse mode to navigate (press escape to close).

## Playlist Transcripts

Pressing SPL Assistant, Shift+F8 will present a dialog to let you request playlist transcripts in numerous formats, including in a plain text format, an HTML table or a list.

## Configuration dialog

From studio window, you can press Alt+NVDA+0 to open the add-on configuration dialog. Alternatively, go to NVDA's preferences menu and select SPL Studio Settings item. This dialog is also used to manage broadcast profiles.

## SPL touch mode

If you are using Studio on a touchscreen computer running Windows 8 or later and have NVDA 2012.3 or later installed, you can perform some Studio commands from the touchscreen. First use three finger tap to switch to SPL mode, then use the touch commands listed above to perform commands.

## Version 18.08

* Added a new section (button/panel) in add-on settings to configure playlist transcripts options, which is used to configure column inclusion and ordering for this feature and other settings.
* When creating a table-based playlist transcripts and if custom column ordering and/or column removal is in effect, NVDA will use custom column presentation order specified form add-on settings and/or not include information from removed columns.
* When using column navigation commands in track items (Control+Alt+home/end/left arrow/right arrow) in Studio, Creator, and Track Tool, NVDA will no longer announce wrong column data after changing column position on screen via mouse.
* Significant improvements to NVDA's responsiveness when using column navigation commands in Creator and Track Tool. In particular, when using Creator, NVDA will respond better when using column navigation commands.

## Version 18.07

* Added an experimental multi-category add-on settings screen, accessible by toggling a setting in add-on settings/Advanced dialog (you need to restart NVDA after configuring this setting for the new dialog to show up). This is for NVDA 2018.2 users, and not all add-on settings can be configured from this new screen.
* NVDA will no longer play error tones or appear to do nothing when trying to rename a broadcast profile from add-on settings, caused by wxPython 4 compatibility issue.
* When restarting NvDA and/or Studio after making changes to settings in a broadcast profile other than normal profile, NVDA will no longer revert to old settings.
* It is now possible to obtain playlist transcripts for the current hour. Select "current hour" from list of playlist range options in playlist transcripts dialog (SPL Assistant, Shift+F8).
* Added an option in Playlist Transcripts dialog to have transcripts saved to a file (all formats) or copied to the clipboard (text and Markdown table formats only) in addition to viewing transcripts on screen. When transcripts are saved, they are saved to user's Documents folder under "nvdasplPlaylistTranscripts" subfolder.
* Status column is no longer included when creating playlist transcripts in HTML and Markdown table formats.
* When focused on a track in Creator and Track Tool, pressing Control+NVDA+number row twice will present column information on a browse mode window.
* In Creator and Track Tool, added Control+Alt+Home/End keys to move Column Navigator to first or last column for the focused track.

## Version 18.06.1

* Fixed several compatibility issues with wxPython 4, including inability to open track finder (Control+NVDA+F), column search and time ranger finder dialogs in Studio and stream labeler dialog (F12) from encoders window.
* While opening a find dialog from Studio and an unexpected error occurs, NVDA will present more appropriate message instead of saying that another find dialog is open.
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
* Several add-on features were enhanced with extension points. This allows microphone alarm and metadata streaming feature to respond to changes in broadcast profiles. This requires NvDA 2017.4.
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
* In add-on settings, added a checkbox to let NvDA play a sound when listener requests arrive. To use this fully, requests window must pop up when requests arrive.
* Pressing broadcaster time command (NVDA+Shift+F12) twice will now cause NVDA to announce minutes and seconds remaining in the current hour.
* It is now possible to use Track Finder (Control+NVDA+F) to search for names of tracks you've searched before by selecting a search term from a history of terms.
* When announcing title of current and next track via SPL Assistant, it is now possible to include information about which Studio internal player will play the track (e.g. player 1).
* Added a setting in add-on settings under status announcements to include player information when announcing title of the current and the next track.
* Fixed an issue in temporary cue and other dialogs where NVDA would not announce new values when manipulating time pickers.
* NVDA can suppress announcement of column headers such as Artist and Category when reviewing tracks in playlist viewer. This is a broadcast profile specific setting.
* Added a checkbox in add-on settings dialog to suppress announcement of column headers when reviewing tracks in playlist viewer.
* Added a command in SPL Controller layer to announce name and duration of the currently playing track from anywhere (C).
* When obtaining status information via SPL Controller (Q) while using Studio 5.1x, information such as microphone status, cart edit mode and others will also be announced in addition to playback and automation.

## Version 17.06

* You can now perform Track Finder command (Control+NVDA+F) while a playlist is loaded but the first track isn't focused.
* NVDA will no longer play error tones or do nothing when searching for a track forward from the last track or backward from the first track, respectively.
* Pressing NVDA+Numpad Delete (NVDA+Delete in laptop layout) will now announce track position followed by number of items in a playlist.

## Version 17.05.1

* NVDA will no longer fail to save changes to alarm settings from various alarm dialogs (for example, Alt+NVDA+1 for end of track alarm).

## Version 17.05/15.7-LTS

* Update interval can now be set up to 180 days. For default installations, update check interval will be 30 days.
* Fixed an issue where NVDA may play error tone if Studio exits while a time-based profile is active.

## Version 17.04

* Added a basic add-on debugging support by logging various information while the add-on is active with NVDA set to debug logging (requires NVDA 2017.1 and later). To use this, after installing NVDA 2017.1, from Exit NVDA dialog, choose "restart with debug logging enabled" option.
* Improvements to presentation of various add-on dialogs thanks to NVDA 2016.4 features.
* NVDA will download add-on updates in the background if you say "yes" when asked to update the add-on. Consequently, file download notifications from web browsers will no longer be shown.
* NVDA will no longer appear to freeze when checking for update at startup due to add-on update channel change.
* Added ability to press Control+Alt+up or down arrow keys to move between tracks (specifically, track columns) vertically just as one is moving to next or previous row in a table.
* Added a combo box in add-on settings dialog to set which column should be announced when moving through columns vertically.
* Moved end of track , intro and microphone alarm controls from add-on settings to the new Alarms Center.
* In Alarms Center, end of track and track intro edit fields are always shown regardless of state of alarm notification checkboxes.
* Added a command in SPL Assistant to obtain playlist snapshots such as number of tracks, longest track, top artists and so on (F8). You can also add a custom command for this feature.
* Pressing the custom gesture for playlist snapshots command once will let NVDA speak and braile a short snapshot information. Pressing the command twice will cause NVDA to open a webpage containing a fuller playlist snapshot information. Press escape to close this webpage.
* Removed Track Dial (NVDA's version of enhanced arrow keys), replaced by Columns explorer and Column Navigator/table navigation commands). This affects Studio and Track Tool.
* After closing Insert Tracks dialog while a library scan is in progress, it is no longer required to press SPL Assistant, Shift+R to monitor scan progress.
* Improved accuracy of detecting and reporting completion of library scans in Studio 5.10 and later. This fixes a problem where library scan monitor will end prematurely when there are more tracks to be scanned, necessitating restarting library scan monitor.
* Improved library scan status reporting via SPL Controller (Shift+R) by announcing scan count if scan is indeed happening.
* In studio Demo, when registration screen appears when starting Studio, commands such as remaining time for a track will no longer cause NVDA to do nothing, play error tones, or give wrong information. An error message will be announced instead. Commands such as these will require Studio's main window handle to be present.
* Initial support for StationPlaylist Creator.
* Added a new command in SPL Controller layer to announce Studio status such as track playback and microphone status (Q).

## Version 17.03

* NVDA will no longer appear to do anything or play an error tone when switching to a time-based broadcast profile.
* Updated translations.

## Version 17.01/15.5-LTS

Note: 17.01.1/15.5A-LTS replaces 17.01 due to changes to location of new add-on files.

* 17.01.1/15.5A-LTS: Changed where updates are downloaded from for long-term support releases. Installing this version is mandatory.
* Improved responsiveness and reliability when using the add-on to switch to Studio, either using focus to Studio command from other programs or when an encoder is connected and NVDA is told to switch to Studio when this happens. If Studio is minimized, Studio window will be shown as unavailable. If so, restore Studio window from system tray.
* If editing carts while Cart Explorer is active, it is no longer necessary to reenter Cart Explorer to view updated cart assignments when Cart Edit mode is turned off. Consequently, Cart Explorer reentry message is no longer announced.
* In add-on 15.5-LTS, corrected user interface presentation for SPL add-on settings dialog.

## Version 16.12.1

* Corrected user interface presentation for SPL add-on settings dialog.
* Updated translations.

## Version 16.12/15.4-LTS

* More work on supporting Studio 5.20, including announcing cart insert mode status (if turned on) from SPL Assistant layer (T).
* Cart edit/insert mode toggle is no longer affected by message verbosity nor status announcement type settings (this status will always be announced via speech and/or braille).
* It is no longer possible to add comments to timed break notes.
* Support for Track Tool 5.20, including fixed an issue where wrong information is announced when using Columns Explorer commands to announce column information.

## Version 16.11/15.3-LTS

* Initial support for StationPlaylist Studio 5.20, including improved responsiveness when obtaining status information such as automation status via SPL Assistant layer.
* Fixed issues related to searching for tracks and interacting with them, including inability to check or uncheck place marker track or a track found via time range finder dialog.
* Column announcement order will no longer revert to default order after changing it.
* 16.11: If broadcast profiles have errors, error dialog will no longer fail to show up.

## Version 16.10.1/15.2-LTS

* You can now interact with the track that was found via Track Finder (Control+NVDA+F) such as checking it for playback.
* Updated translations.

## Version 8.0/16.10/15.0-LTS

Version 8.0 (also known as 16.10) supports SPL Studio 5.10 and later, with 15.0-LTS (formerly 7.x) designed to provide some new features from 8.0 for users using earlier versions of Studio. Unless otherwise noted, entries below apply to both 8.0 and 7.x. A warning dialog will be shown the first time you use add-on 8.0 with Studio 5.0x installed, asking you to use 15.x LTS version.

* Version scheme has changed to reflect release year.month instead of major.minor. During transition period (until mid-2017), version 8.0 is synonymous with version 16.10, with 7.x LTS being designated 15.0 due to incompatible changes.
* Add-on source code is now hosted on GitHub (repository located at https://github.com/josephsl/stationPlaylist).
* Added a welcome dialog that launches when Studio starts after installing the add-on. A command (Alt+NvDA+F1) has been added to reopen this dialog once dismissed.
* Changes to various add-on commands, including removal of status announcement toggle (Control+NvDA+1), reassigned end of track alarm to Alt+NVDA+1, Cart Explorer toggle is now Alt+NvDA+3, microphone alarm dialog is Alt+NVDA+4 and add-on/encoder settings dialog is Alt+NvDA+0. This was done to allow Control+NVDA+number row to be assigned to Columns Explorer.
* 8.0: Relaxed Columns Explorer restriction in place in 7.x so numbers 1 through 6 can be configured to announce Studio 5.1x columns.
* 8.0: Track Dial toggle command and the corresponding setting in add-on settings are deprecated and will be removed in 9.0. This command will remain available in add-on 7.x.
* Added Control+Alt+Home/End to move Column Navigator to first or last column in Playlist Viewer.
* You can now add, view, change or delete track comments (notes). Press Alt+NVDA+C from a track in the playlist viewer to hear track comments if defined, press twice to copy comment to clipboard or three times to open a dialog to edit comments.
* Added ability to notify if a track comment exists, as well as a setting in add-on settings to control how this should be done.
* Added a setting in add-on settings dialog to let NVDA notify you if you've reached top or bottom of playlist viewer.
* When resetting add-on settings, you can now specify what gets reset. By default, add-on settings will be reset, with checkboxes for resetting instant switch profile, time-based profile, encoder settings and erasing track comments added to reset settings dialog.
* In Track Tool, you can obtain information on album and CD code by pressing Control+NVDA+9 and Control+NVDA+0, respectively.
* Performance improvements when obtaining column information for the first time in Track Tool.
* 8.0: Added a dialog in add-on settings to configure Columns Explorer slots for Track Tool.
* You can now configure microphone alarm interval from microphone alarm dialog (Alt+NvDA+4).

## Version 7.5/16.09

* NVDA will no longer pop up update progress dialog if add-on update channel has just changed.
* NVDA will honor the selected update channel when downloading updates.
* Updated translations.

## Version 7.4/16.08

Version 7.4 is also known as 16.08 following the year.month version number for stable releases.

* It is possible to select add-on update channel from add-on settings/advanced options, to be removed later in 2017. For 7.4, available channels are beta, stable and long-term.
* Added a setting in add-on settings/Advanced options to configure update check interval between 1 and 30 days (default is 7 or weekly checks).
* SPL Controller command and the command to focus to Studio will not be available from secure screens.
* New and updated translations and added localized documentation in various languages.

## Changes for 7.3

* Slight performance improvements when looking up information such as automation via some SPL Assistant commands.
* Updated translations.

## Changes for 7.2

* Due to removal of old-style internal configuration format, it is mandatory to install add-on 7.2. Once installed, you cannot go back to an earlier version of the add-on.
* Added a command in SPL Controller to report listener count (I).
* You can now open SPL add-on settings and encoder settings dialogs by pressing Alt+NVDA+0. You can still use Control+NVDA+0 to open these dialogs (to be removed in add-on 8.0).
* In Track Tool, you can use Control+Alt+left or right arrow keys to navigate between columns.
* Contents of various Studio dialogs such as About dialog in Studio 5.1x are now announced.
* In SPL Encoders, NVDA will silence connection tone if auto-connect is enabled and then turned off from encoder context menu while the selected encoder is connecting.
* Updated translations.

## Changes for 7.1

* Fixed erorrs encountered when upgrading from add-on 5.5 and below to 7.0.
* When answering "no" when resetting add-on settings, you'll be returned to add-on settings dialog and NVDA will remember instant switch profile setting.
* NVDA will ask you to reconfigure stream labels and other encoder options if encoder configuration file becomes corrupted.

## Changes for 7.0

* Added add-on update check feature. This can be done manually (SPL Assistant, Control+Shift+U) or automatically (configurable via advanced options dialog from add-on settings).
* It is no longer required to stay in the playlist viewer window in order to invoke most SPL Assistant layer commands or obtain time announcements such as remaining time for the track and broadcaster time.
* Changes to SPL Assistant commands, including playlist duration (D), reassignment of hour selection duration from Shift+H to Shift+S and Shift+H now used to announce duration of remaining tracks for the current hour slot, metadata streaming status command reassigned (1 through 4, 0 is now Shift+1 through Shift+4, Shift+0).
* It is now possible to invoke track finder via SPL Assistant (F).
* SPL Assistant, numbers 1 through 0 (6 for Studio 5.01 and earlier) can be used to announce specific column information. These column slots can be changed under Columns Explorer item in add-on settings dialog.
* Fixed numerous errors reported by users when installing add-on 7.0 for the first time when no prior version of this add-on was installed.
* Improvements to Track Dial, including improved responsiveness when moving through columns and tracking how columns are presented on screen.
* Added ability to press Control+Alt+left or right arrow keys to move between track columns.
* It is now possible to use a different screen reader command layout for SPL Assistant commands. Go to advanced options dialog from add-on settings to configure this option between NVDA, JAWS and Window-Eyes layouts. See the SPL Assistant commands above for details.
* NVDA can be configured to switch to a specific broadcast profile at a specific day and time. Use the new triggers dialog in add-on settings to configure this.
* NVDA will report name of the profile one is switching to via instant switch (SPL Assistant, F12) or as a result of time-based profile becoming active.
* Moved instant switch toggle (now a checkbox) to the new triggers dialog.
* Entries in profiles combo box in add-on settings dialog now shows profile flags such as active, whether it is an instant switch profile and so on.
* If a serious problem with reading broadcast profile files are found, NVDA will present an error dialog and reset settings to defaults instead of doing nothing or sounding an error tone.
* Settings will be saved to disk if and only if you change settings. This prolongs life of SSD's (solid state drives) by preventing unnecessary saves to disk if no settings have changed.
* In add-on settings dialog, the controls used to toggle announcement of scheduled time, listener count, cart name and track name has been moved to a dedicated status announcements dialog (select status announcement button to open this dialog).
* Added a new setting in add-on settings dialog to let NVDA play beep for different track categories when moving between tracks in playlist viewer.
* Attempting to open metadata configuration option in add-on settings dialog while quick metadata streaming dialog is open will no longer cause NVDA to do nothing or play an error tone. NvDA will now ask you to close metadata streaming dialog before you can open add-on settings.
* When announcing time such as remaining time for the playing track, hours are also announced. Consequently, the hour announcement setting is enabled by default.
* Pressing SPL Controller, R now causes NVDA to announce remaining time in hours, minutes and seconds (minutes and seconds if this is such a case).
* In encoders, pressing Control+NVDA+0 will present encoder settings dialog for configuring various options such as stream label, focusing to Studio when connected and so on.
* In encoders, it is now possible to turn off connection progress tone (configurable from encoder settings dialog).

## Changes for 6.4

* Fixed a major problem when switching back from an instant switch profile and the instant switch profile becomes active again, seen after deleting a profile that was positioned right before the previously active profile. When attempting to delete a profile, a warning dialog will be shown if an instant switch profile is active.

## Changes for 6.3

* Internal security enhancements.
* When add-on 6.3 or later is first launched on a computer running Windows 8 or later with NVDA 2016.1 or later installed, an alert dialog will be shown asking you to disable audio ducking mode (NVDA+Shift+D). Select the checkbox to suppress this dialog in the future.
* Added a command to send bug reports, feature suggestions and other feedback to add-on developer (Control+NVDA+dash (hyphen, "-")).
* Updated translations.

## Changes for 6.2

* Fixed an issue with playlist remainder command (SPL Assistant, D (R if compatibility mode is on)) where the duration for the current hour was announced as opposed to the entire playlist (the behavior of this command can be configured from advanced settings found in add-on settings dialog).
* NvDA can now announce name of the currently playing track while using another program (configurable from add-on settings).
* The setting used to let SPL Controller command invoke SPL Assistant is now honored (previously it was enabled at all times).
* In SAM encoders, Control+F9 and Control+F10 commands now works correctly.
* In encoders, when an encoder is first focused and if this encoder is configured to be monitored in the background, NVDA will now start the background monitor automatically.

## Changes for 6.1

* Column announcement order and inclusion, as well as metadata streaming settings are now profile-specific settings.
* When changing profiles, the correct metadata streams will be enabled.
* When opening quick metadata streaming settings dialog (command unassigned), the changed settings are now applied to the active profile.
* When starting Studio, changed how the errors are displayed if the only corrupt profile is the normal profile.
* When changing certain settings using shortcut keys such as status announcements, fixed an issue where the changed settings are not retained when switching to and from an instant switch profile.
* When using a SPL Assistant command with a custom gesture defined (such as next track command), it is no longer required to stay in the Studio's playlist viewer to use these commands (they can be performed from other Studio windows).

## Changes for 6.0

* New SPL Assistant commands, including announcing title of the currently playing track (C), announcing status of metadata streaming (E, 1 through 4 and 0) and opening the online user guide (Shift+F1).
* Ability to package favorite settings as broadcast profiles to be used during a show and to switch to a predefined profile. See the add-on guide for details on broadcast profiles.
* Added a new setting in add-on settings to control message verbosity (some messages will be shortened when advanced verbosity is selected).
* Added a new setting in add-on settings to let NVDA announce hours, minutes and seconds for track or playlist duration commands (affected features include announcing elapsed and remaining time for the currently playing track, track time analysis and others).
* You can now ask NVDA to report total length of a range of tracks via track time analysis feature. Press SPL Assistant, F9 to mark current track as start marker, move to end of track range and press SPL Assistant, F10. These commands can be reassigned so one doesn't have to invoke SPL Assistant layer to perform track time analysis.
* Added a column search dialog (command unassigned) to find text in specific columns such as artist or part of file name.
* Added a time range finder dialog (command unassigned) to find a track with duration that falls within a specified range, useful if wishing to find a track to fill an hour slot.
* Added ability to reorder track column announcement and to suppress announcement of specific columns if "use screen order" is unchecked from add-on settings dialog. Use "manage column announcement" dialog to reorder columns.
* Added a dialog (command unassigned) to quickly toggle metadata streaming.
* Added a setting in add-on settings dialog to configure when metadata streaming status should be announced and to enable metadata streaming.
* Added ability to mark a track as a place marker to return to it later (SPL Assistant, Control+K to set, SPL Assistant, K to move to the marked track).
* Improved performance when searching for next or previous track text containing the searched text.
* Added a setting in add-on settings dialog to configure alarm notification (beep, message or both).
* It is now possible to configure microphone alarm between 0 (disabled) and two hours (7200 seconds) and to use up and down arrow keys to configure this setting.
* Added a setting in add-on settings dialog to allow microphone active notification to be given periodically.
* You can now use Track Dial toggle command in Studio to toggle Track Dial in Track Tool provided that you didn't assign a command to toggle Track Dial in Track Tool.
* Added ability to use SPL Controller layer command to invoke SPL Assistant layer (configurable from advanced Settings dialog found in add-on settings dialog).
* Added ability for NvDA to use certain SPL Assistant commands used by other screen readers. To configure this, go to add-on settings, select Advanced Settings and check screen reader compatibility mode checkbox.
* In encoders, settings such as focusing to Studio when connected are now remembered.
* It is now possible to view various columns from encoder window (such as encoder connection status) via Control+NVDA+number command; consult the encoder commands above.
* Fixed a rare bug where switching to Studio or closing an NVDA dialog (including Studio add-on dialogs) prevented track commands (such as toggling Track Dial) from working as expected.

## Changes for 5.6

* In Studio 5.10 and later, NVDA no longer announces "not selected" when the selected track is playing.
* Due to an issue with Studio itself, NVDA will now announce name of the currently playing track automatically. An option to toggle this behavior has been added in studio add-on settings dialog.

## Changes for 5.5

* Play after connecting setting will be remembered when moving away from the encoder window.

## Changes for 5.4

* Performing library scan from Insert Tracks dialog no longer causes NVDA to not announce scan status or play error tones if NVDA is configured to announce library scan progress or scan count.
* Updated translations.

## Changes for 5.3

* The fix for SAM Encoder (not playing the next track if a track is playing and when the encoder connects) is now available for SPL Encoder users.
* NVDA no longer plays errors or does not do anything when SPL Assistant, F1 (Assistant help dialog) is pressed.

## Changes for 5.2

* NVDA will no longer allow both settings and alarm dialogs to be opened. A warning will be shown asking you to close the previously opened dialog before opening another dialog.
* When monitoring one or more encoders, pressing SPL Controller, E will now announce encoder count, encoder ID and stream label(s) if any.
* NVDA supports connect/disconnect all commands (Control+F9/Control+F10) in SAM encoders.
* NVDA will no longer play the next track if an encoder connects while Studio is playing a track and Studio is told to play tracks when an encoder is connected.
* Updated translations.

## Changes for 5.1

* It is now possible to review individual columns in Track Tool via Track Dial (toggle key unassigned). Note that Studio must be active before using this mode.
* Added a check box in Studio add-on settings dialog to toggle announcement of name of the currently playing cart.
* Toggling microphone on and off via SPL Controller no longer causes error tones to be played or toggle sound to not be played.
* If a custom command is assigned for an SPL Assistant layer command and this command is pressed right after entering SPL Assistant, NvDA will now promptly exit SPL Assistant.

## Changes for 5.0

* A dedicated settings dialog for SPL add-on has been added, accessible from NVDA's preferences menu or by pressing Control+NVDA+0 from SPL window.
* Added ability to reset all settings to defaults via configuration dialog.
* If some of the settings have errors, only the affected settings will be reset to factory defaults.
* Added a dedicated SPL touchscreen mode and touch commands to perform various Studio commands.
* Changes to SPL Assistant layer include addition of layer help command (F1) and removal of commands to toggle listener count (Shift+I) and scheduled time announcement (Shift+S). You can configure these settings in add-on settings dialog.
* Renamed "toggle announcement" to "status announcement" as beeps are used for announcing other status information such as completion of library scans.
* Status announcement setting is now retained across sessions. Previously you had to configure this setting manually when Studio starts.
* You can now use Track Dial feature to review columns in a track entry in Studio's main playlist viewer (to toggle this feature, press the command you assigned for this feature).
* You can now assign custom commands to hear temperature information or to announce title for the upcoming track if scheduled.
* Added a checkbox in end of track and song intro alarm dialogs to enable or disable these alarms (check to enable). These can also be "configured" from add-on settings.
* Fixed an issue where pressing alarm dialog or track finder commands while another alarm  or find dialog is opened would cause another instance of the same dialog to appear. NVDA will pop up a message asking you to close the previously opened dialog first.
* Cart explorer changes and fixes, including exploring wrong cart banks when user is not focused on playlist viewer. Cart explorer will now check to make sure that you are in playlist viewer.
* Added ability to use SPL Controller layer command to invoke SPL Assistant (experimental; consult the add-on guide on how to enable this).
* In encoder windows, NVDA's time and date announcement command (NVDA+F12 by default) will announce time including seconds.
* You can now monitor individual encoders for connection status and for other messages by pressing Control+F11 while the encoder you wish to monitor is focused (works better when using SAM encoders).
* Added a command in SPL Controller layer to announce status of encoders being monitored (E).
* A workaround is now available to fix an issue where NvDA was announcing stream labels for the wrong encoders, especially after deleting an encoder (to realign stream labels, press Control+F12, then select the position of the encoder you have removed).

## Older releases

Please see changelog link for release notes for old add-on releases.

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
