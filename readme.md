# StationPlaylist Studio #

* Authors: Geoff Shang, Joseph Lee and other contributors
* Download [stable version][1]
* Download [development version][2]
* Download [long-term support version][3] - add-on 7.x for Studio 5.0x users

This add-on package provides improved usage of StationPlaylist Studio, as well as providing utilities to control the Studio from anywhere.

For more information about the add-on, read the [add-on guide][4]. For developers seeking to know how to build the add-on, see buildInstructions.txt located at the root of the add-on source code repository.

IMPORTANT: This add-on requires NVDA 2015.3 or later and StationPlaylist Studio 5.00 or later. If you have installed NVDA 2016.1 or later on Windows 8 and later, disable audio ducking mode. Also, add-on 8.0/16.10 requires Studio 5.10 and later, and for broadcasters using Studio 5.0x, a long-term support version (7.x) is available.

## Shortcut keys

* Alt+Shift+T from Studio window: announce elapsed time for the currently playing trakc.
* Control+Alt+T (two finger flick down in SPL touch mode) from Studio window: announce remaining time for the currently playing trakc.
* NVDA+Shift+F12 (two finger flick up in SPL touch mode) from Studio window: announces broadcaster time such as 5 minutes to top of the hour.
* Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens end of track setting dialog.
* Alt+NVDA+2 (two finger flick left in SPL mode) from Studio window: Opens song intro alarm setting dialog.
* Alt+NVDA+3 from Studio window: Toggles cart explorer to learn cart assignments.
* Alt+NVDA+4 from Studio window: Opens microphone alarm dialog.
* Control+NVDA+f from Studio window: Opens a dialog to find a track based on artist or song name. Press NvDA+F3 to find forward or NVDA+Shift+F3 to find backward.
* Alt+NVDA+R from Studio window: Steps through library scan announcement settings.
* Control+Shift+X from Studio window: Steps through braille timer settings.
* Control+Alt+right/left arrow (while focused on a track): Announce next/previous track column.
* Control+NVDA+1 through 0 (6 for Studio 5.0x): Announce column content for a specified column.
* Alt+NVDA+C while focused on a track: announces track comments if any.
* Alt+NVDA+0 from Studio window: Opens the Studio add-on configuration dialog.
* Control+NVDA+- (hyphen) from Studio window: Send feedback to add-on developer using the default email client.
* Alt+NVDA+F1: Open welcome dialog.

## Unassigned commands

The following commands are not assigned by default; if you wish to assign it, use Input Gestures dialog to add custom commands.

* Switching to SPL Studio window from any program.
* SPL Controller layer.
* SPL Assistant layer from SPL Studio.
* Announce time including seconds from SPL Studio.
* Toggling track dial on or off (works properly while a track is focused; to assign a command to this, move to a track in Studio, then open NVDA's input gestures dialog.).
* Announcing temperature.
* Announcing title of next track if scheduled.
* Announcing title of the currently playing track.
* Marking current track for start of track time analysis.
* Performing track time analysis.
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
* S: Track starts in (scheduled).
* Shift+S: Time until selected track will play.
* T: Cart edit mode on/off.
* U: Studio up time.
* Control+Shift+U: Check for add-on updates.
* W: Weather and temperature if configured.
* Y: Playlist modified status.
* 1 through 0 (6 for Studio 5.0x): Announce column content for a specified column.
* F9: Mark current track for track time analysis (playlist viewer only).
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
* Press E to get count and labels for encoders being monitored.
* Press I to obtain listener count.
* Press F1 to show a help dialog which lists available commands.

## Track alarms

By default, NvDA will play a beep if five seconds are left in the track (outro) and/or intro. To configure this value as well as to enable or disable them, press Alt+NVDA+1 or Alt+NVDA+2 to open end of track and song ramp dialogs, respectively. In addition, use Studio add-on settings dialog to configure if you'll hear a beep, a message or both when alarms are turned on.

## Microphone alarm

You can ask NVDA to play a sound when microphone has been active for a while. Press Alt+NVDA+4 to configure alarm time in seconds (0 disables it).

## Track Finder

If you wish to quickly find a song by an artist or by song name, from track list, press Control+NVDA+F. Type the name of the artist or the song name. NVDA will either place you at the song if found or will display an error if it cannot find the song you're looking for. To find a previously entered song or artist, press NVDA+F3 or NVDA+Shift+F3 to find forward or backward.

Note: Track Finder is case-sensitive.

## Cart Explorer

Depending on edition, SPL Studio allows up to 96 carts to be assigned for playback. NVDA allows you to hear which cart, or jingle is assigned to these commands.

To learn cart assignments, from SPL Studio, press Alt+NVDA+3. Pressing the cart command once will tell you which jingle is assigned to the command. Pressing the cart command twice will play the jingle. Press Alt+NvDA+3 to exit cart explorer. See the add-on guide for more information on cart explorer.

## Track Dial

You can use arrow keys to review various information about a track. To turn Track Dial on, while a track is focused in the main playlist viewer, press the command you assigned for toggling Track Dial. Then use left and right arrow keys to review information such as artist, duration and so on. Alternatively, press Control+Alt+left or right arrows to navigate between columns without invoking Track Dial.

## Track time analysis

To obtain length to play selected tracks, mark current track for start of track time analysis (SPL Assistant, F9), then press SPL Assistant, F10 when reaching end of selection.

## Columns Explorer

By pressing Control+NVDA+1 through 0 (6 for Studio 5.0x) or SPL Assistant, 1 through 0 (6 for Studio 5.01 and earlier), you can obtain contents of specific columns. By default, these are artist, title, duration, intro, category and filename (Studio 5.10 adds year, album, genre and time scheduled). You can configure which columns will be explored via columns explorer dialog found in add-on settings dialog.

## Configuration dialog

From studio window, you can press Alt+NVDA+0 to open the add-on configuration dialog. Alternatively, go to NVDA's preferences menu and select SPL Studio Settings item. This dialog is also used to manage broadcast profiles.

## SPL touch mode

If you are using Studio on a touchscreen computer running Windows 8 or later and have NVDA 2012.3 or later installed, you can perform some Studio commands from the touchscreen. First use three finger tap to switch to SPL mode, then use the touch commands listed above to perform commands.

## Changes for 8.0/16.10-dev/15.0-LTS

Version 8.0 (also known as 16.10) supports SPL Studio 5.10 and later, with 15.0-LTS (formerly 7.x) designed to provide some new features from 8.0 for users using earlier versions of Studio. Unless otherwise noted, entries below apply to both 8.0 and 7.x. A warning dialog will be shown the first time you use add-on 8.0 with Studio 5.0x installed, asking you to use 7.x LTS version.

* Version scheme has changed to reflect release year.month instead of major.minor. During transition period (until mid-2017), version 8.0 is synonymous with version 16.10, with 7.x LTS being designated 15.0 due to incompatible changes.
* Add-on source code is now hosted on GitHub (repository located at https://github.com/josephsl/stationPlaylist).
* Added a welcome dialog that launches when Studio starts after installing the add-on. A command (Alt+NvDA+F1) has been added to reopen this dialog once dismissed.
* Changes to various add-on commands, including removal of status announcement toggle (Control+NvDA+1), reassigned end of track alarm to Alt+NVDA+1, Cart Explorer toggle is now Alt+NvDA+3, microphone alarm dialog is Alt+NVDA+4 and add-on/encoder settings dialog is Alt+NvDA+0. This was done to allow Control+NVDA+number row to be assigned to Columns Explorer.
* 8.0: Relaxed Columns Explorer restriction in place in 7.x so numbers 1 through 6 can be configured to announce Studio 5.1x columns.
* 8.0: Track Dial toggle command and the corresponding setting in add-on settings are deprecated and will be removed in 9.0. This command will remain available in add-on 7.x.
* You can now add, view, change or delete track comments (notes). Press Alt+NVDA+C from a track in the playlist viewer to hear track comments if defined, press twice to copy comment to clipboard or three times to open a dialog to edit comments.
* Added ability to notify if a track comment exists, as well as a setting in add-on settings to control how this should be done.
* Added a setting in add-on settings dialog to let NVDA notify you if you've reached top or bottom of playlist viewer.
* When resetting add-on settings, you can now specify what gets reset. By default, add-on settings will be reset, with checkboxes for resetting instant switch profile, time-based profile, encoder settings and erasing track comments added to reset settings dialog.
* In Track Tool, you can obtain information on album and CD code by pressing Control+NVDA+9 and Control+NVDA+0, respectively.
* Performance improvements when obtaining column information for the first time in Track Tool.
* 8.0: Added a dialog in add-on settings to configure Columns Explorer slots for Track Tool.
* You can now configure microphone alarm interval from microphone alarm dialog (Alt+NvDA+4).

## Version 7.4/16.08

Version 7.4 is also known as 16.08 following the year.month version number for stable releases. 7.4 is the last version in the 7.x series and the entire major.minor version numbers.

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

## Changes for 4.4/3.9

* Library scan function now works in Studio 5.10 (requires latest Studio 5.10 build).

## Changes for 4.3/3.8

* When switching to another part of Studio such as insert tracks dialog while cart explorer is active, NVDA will no longer announce cart messages when cart keys are pressed (for example, locating a track from insert tracks dialog).
* New SPL Assistant keys, including toggling announcement of scheduled time and listener count (Shift+S and Shift+I, respectively, not saved across sessions).
* When exiting Studio while various alarm dialogs are opened, NVDA will detect that Studio has been exited and will not save newly modified alarm values.
* Updated translations.

## Changes for 4.2/3.7

* NVDA will no longer forget to retain new and changed encoder labels when a user logs off or restarts a computer.
* When the add-on configuration becomes corrupted when NVDA starts, NVDA will restore default configuration and will display a message to inform the user of this fact.
* In add-on 3.7, focus issue seen when deleting tracks in Studio 4.33 has been corrected (same fix is available for Studio 5.0x users in add-on 4.1).

## Changes for 4.1

* In Studio 5.0x, deleting a track from the main playlist viewer will no longer cause NVDA to announce the track below the newly focused track (more noticeable if the second to last track was deleted, in which case NVDA said "unknown").
* Fixed several library scan issues in Studio 5.10, including announcing total number of items in the library while tabbing around in the insert tracks dialog and saying "scan is in progress" when attempting to monitor library scans via SPL Assistant.
* When using a braille display with Studio 5.10 and if a track is checked, pressing SPACE to check a track below no longer causes braille to not reflect the newly checked state.

## Changes for 4.0/3.6

Version 4.0 supports SPL Studio 5.00 and later, with 3.x designed to provide some new features from 4.0 for users using earlier versions of Studio.

* New SPL Assistant keys, including schedule time for the track (S), remaining duration for the playlist (D) and temperature (W if configured). In addition, for Studio 5.x, added playlist modification (Y) and track pitch (Shift+P).
* New SPL Controller commands, including progress of library scans (Shift+R) and enabling microphone without fade (N). Also, pressing F1 pops up a dialog showing available commands.
* When enabling or disabling microphone via SPL Controller, beeps will be played to indicate on/off status.
* Settings such as end of track time are saved to a dedicated configuration file in your user configuration directory and are preserved during add-on upgrades (version 4.0 and later).
* Added a command (Alt+NvDA+2) to set song intro alarm time between 1 and 9 seconds.
* In end of track and intro alarm dialogs, you can use up and down arrows to change alarm settings. If a wrong value is entered, alarm value is set to maximum value.
* Added a command (Control+NVDA+4) to set a time when NVDA will play a sound when microphone has been active for a while.
* Added a feature to announce time in hours, minutes and seconds (command unassigned).
* It is now possible to track library scans from Insert Tracks dialog or from anywhere, and a dedicated command (Alt+NVDA+R) to toggle library scan announcement options.
* Support for Track Tool, including playing a beep if a track has intro defined and commands to announce information on a track such as duration and cue position.
* Support for StationPlaylist Encoder (Studio 5.00 and later), providing same level of support as found in SAM Encoder support.
* In encoder windows, NvDA no longer plays error tones when NVDA is told to switch to Studio upon connecting to a streaming server while Studio window is minimized.
* Errors are no longer heard after deleting a stream with a stream label set on it.
* It is now possible to monitor introduction and end of track via braille using the braille timer options (Control+Shift+X).
* Fixed an issue where attempting to switch to Studio window from any program after all windows were minimized caused something else to appear.
* When using Studio 5.01 and earlier, NVDA will no longer announce certain status information such as scheduled time multiple times.

## Changes for 3.5

* When NVDA is started or restarted while Studio 5.10's main playlist window is focused, NVDA will no longer play error tones and/or not announce next and previous tracks when arrowing through tracks.
* Fixed an issue when trying to obtain remaining time and elapsed time for a track in later builds of Studio 5.10.
* Updated translations.

## Changes for 3.4

* In cart explorer, carts involving control key (such as Ctrl+F1) are now handled correctly.
* Updated translations.

## Changes for 3.3

* When connecting to a streaming server using SAM encoder, it is no longer required to stay in the encoder window until connection is established.
* Fixed an issue where encoder commands (for example, stream labeler) would no longer work when switching to SAM window from other programs.

## Changes for 3.2

* Added a command in SPL Controller to report remaining time for the currently playing track (R).
* In SAM encoder window, input help mode message for Shift+F11 command has been corrected
* In cart explorer, if Studio Standard is in use, NVDA will alert that number row commands are unavailable for cart assignments.
* In Studio 5.10, track finder no longer plays error tones when searching through tracks.
* New and updated translations.

## Changes for 3.1

* In SAM Encoder window, added a command (Shift+F11) to tell Studio to play the first track when connected.
* Fixed numerous bugs when connecting to a server in SAM Encoder, including inability to perform NVDA commands, NVDA not announcing when connection has been established and error tones instead of connection beep being played when connected.

## Changes for 3.0

* Added Cart Explorer to learn cart assignments (up to 96 carts can be assigned).
* Added new commands, including broadcaster time (NVDA+Shift+F12) and listener count (i) and next track title (n) in SPL Assistant.
* Toggle messages such as automation are now displayed in braille regardless of toggle announcement setting.
* When StationPlaylist window is minimized to the system tray (notification area), NVDA will announce this fact when trying to switch to SPL from other programs.
* Error tones are no longer heard when toggle announcement is set to beeps and status messages other than on/off toggle are announced (example: playing carts).
* Error tones are no longer heard when trying to obtain information such as remaining time while other Studio window other than track list (such as Options dialog) is focused. If the needed information is not found, NVDA will announce this fact.
* It is now possible to search a track by artist name. Previously you could search by track title.
* Support for SAM Encoder, including ability to label the encoder and a toggle command to switch to Studio when the selected encoder is connected.
* Add-on help is available from the Add-ons Manager.

## Changes for 2.1

* Fixed an issue where user was unable to obtain status information such as automation status when SPL 5.x was first launched while NVDA was running.

## Changes for 2.0

* Some global and app-specific hotkeys were removed so you can assign a custom command from Input Gestures dialog (add-on version 2.0 requires NVDA 2013.3 or later).
* Added more SPL Assistant commands such as cart edit mode status.
* You can now switch to SPL Studio even with all windows minimized (may not work in some cases).
* Increased the end of track alarm range to 59 seconds.
* You can now search for a track in a playlist (Control+NVDA+F to find, NvDA+F3 or NvDA+Shift+F3 to find forward or backward, respectively).
* Correct names of combo boxes are now announced by NVDA (e.g. Options dialog and initial SPL setup screens).
* Fixed an issue where NVDA was announcing wrong information when trying to get remaining time for a track in SPL Studio 5.

## Changes for 1.2

* When Station Playlist 4.x is installed on certain Windows 8/8.1 computers, it is again possible to hear elapsed and remaining times for a track.
* Updated translations.

## Changes for 1.1

* Added a command (Control+NvDA+2) to set end of track alarm time.
* Fixed a bug in which field names for certain edit fields were not announced (particularly edit fields in Options dialog).
* Added various translations.


## Changes for 1.0

* Initial release.

[1]: http://addons.nvda-project.org/files/get.php?file=spl

[2]: http://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: http://spl.nvda-kr.org/files/get.php?file=spl-lts7

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide
