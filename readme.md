# StationPlaylist Studio #

* Authors: Geoff Shang, Joseph Lee and other contributors
* Download [stable version][1]
* Download [development version][2]

This add-on package provides improved usage of StationPlaylist Studio, as well as providing utilities to control the Studio from anywhere.

For more information about the add-on, read the [add-on guide][3].

IMPORTANT: This add-on requires NVDA 2014.3 or later and StationPlaylist Studio 5.00 or later.

## Shortcut keys

* Alt+Shift+T from Studio window: announce elapsed time for the currently playing trakc.
* Control+Alt+T (two finger flick down in SPL touch mode) from Studio window: announce remaining time for the currently playing trakc.
* NVDA+Shift+F12 (two finger flick up in SPL touch mode) from Studio window: announces broadcaster time such as 5 minutes to top of the hour.
* Control+NVDA+1 from Studio window: toggles announcement of status messages (such as automation and end of library scan) between words and beeps.
* Control+NVDA+2 (two finger flick right in SPL mode) from Studio window: Opens end of track setting dialog.
* Alt+NVDA+2 (two finger flick left in SPL mode) from Studio window: Opens song intro alarm setting dialog.
* Control+NVDA+3 from Studio window: Toggles cart explorer to learn cart assignments.
* Control+NVDA+4 from Studio window: Opens microphone alarm dialog.
* Control+NVDA+f from Studio window: Opens a dialog to find a track based on artist or song name. Press NvDA+F3 to find forward or NVDA+Shift+F3 to find backward.
* Alt+NVDA+R from Studio window: Steps through library scan announcement settings.
* Control+Shift+X from Studio window: Steps through braille timer settings.
* Control+NVDA+0 from Studio window: Opens the Studio add-on configuration dialog.

## Unassigned commands

The following commands are not assigned by default; if you wish to assign it, use Input Gestures dialog to add custom commands.

* Switching to SPL Studio window from any program.
* SPL Controller layer.
* SPL Assistant layer from SPL Studio.
* Announce time including seconds from SPL Studio.
* Toggling track dial on or off (works properly while a track is focused; to assign a command to this, select a track, then open NVDA's input gestures dialog.).
* Announcing temperature.
* Announcing title of next track if scheduled.

Note: Input Gestures dialog is available in 2013.3 or later.

## Additional commands when using Sam or SPL encoders

The following commands are available when using Sam or SPL encoders:

* F9: connect to a streaming server.
* F10 (SAM encoder only): Disconnect from the streaming server.
* Control+F9/Control+F10 (SAM encoder only): Connect or disconnect all encoders, respectivley.
* F11: Toggles whether NVDA will switch to Studio window for the selected encoder if connected.
* Shift+F11: Toggles whether Studio will play the first selected track when encoder is connected to a streaming server.
* Control+F11: Toggles background monitoring of the selected encoder.
* F12: Opens a dialog to enter custom label for the selected encoder or stream.
* Control+F12: opens a dialog to select the encoder you have deleted (to realign stream labels).

## SPL Assistant layer

This layer command set allows you to obtain various status on SPL Studio, such as whether a track is playing, total duration of all tracks for the hour and so on. From SPL Studio window, press the SPL Assistant layer command, then press one of the keys from the list below.

The available status information are:

* A: Automation.
* D: Remaining duration for the playlist.
* H: Duration of music for the current hour slot.
* Shift+H: Total duration of selected tracks for this hour slot (from the track list, press SPACE to select or uncheck the track to play).
* I: Listener count.
* L: Line in.
* M: Microphone.
* N: Title for the next scheduled track.
* P: Playback status (playing or stopped).
* Shift+P: Pitch of the current track.
* R: Record to file enabled/disabled.
* Shift+R: Monitor library scan in progress.
* S: Track starts in (scheduled).
* T: Cart edit mode on/off.
* U: Studio up time.
* W: Weather and temperature if configured.
* Y: Playlist modified status.
* F1: Layer help.

## SPL Controller

The SPL Controller is a set of layered commands you can use to control SPL Studio anywhere. Press the SPL Controller layer command, and NVDA will say, "SPL Controller." Press another command to control various Studio settings such as microphone on/off or play the next track.

The available SPL Controller commands are:

* Press P to play the next selected track.
* Press U to pause or unpause playback.
* Press S to stop the track with fade out, or to stop the track instantly, press T.
* Press M or Shift+M to turn on or off the microphone, respectively, or press N to enable microphone without fade.
* Press A to enable automation or Shift+A to disable it.
* Press L to enable line-in input or Shift+L to disable it.
* Press R to hear remaining time for the currently playing track in seconds.
* Press Shift+R to get a report on library scan progress.
* Press E to get count and labels for encoders being monitored.
* Press F1 to show a help dialog which lists available commands.

## End of track alarm

Five seconds before the current track ends, NVDA will play a short beep to indicate that the track is about to end. This works anywhere (even within SPL Studio window). Press Control+NVDA+2 to configure this between 1 and 59 seconds.

## Song intro alarm

If you have configured song intro time via Track Tool, NVDA will beep when the vocals are about to begin. From Studio window, press Alt+NVDA+2 to configure song intro alarm between 1 and 9 seconds.

## Microphone alarm

You can ask NVDA to play a sound when microphone has been active for a while. Press Control+NVDA+4 to configure alarm time in seconds (0 disables it).

## Track Finder

If you wish to quickly find a song by an artist or by song name, from track list, press Control+NVDA+F. Type the name of the artist or the song name. NVDA will either place you at the song if found or will display an error if it cannot find the song you're looking for. To find a previously entered song or artist, press NVDA+F3 or NVDA+Shift+F3 to find forward or backward.

Note: Track Finder is case-sensitive.

## Cart Explorer

Depending on edition, SPL Studio allows up to 96 carts to be assigned for playback. NVDA allows you to hear which cart, or jingle is assigned to these commands.

To learn cart assignments, from SPL Studio, press Control+NVDA+3. Pressing the cart command once will tell you which jingle is assigned to the command. Pressing the cart command twice will play the jingle. Press Control+NvDA+3 to exit cart explorer. See the add-on guide for more information on cart explorer.

## Track Dial

You can use arrow keys to review various information about a track. To turn Track Dial on, while a track is focused in the main playlist viewer, press the command you assigned for toggling Track Dial. Then use left and right arrow keys to review information such as artist, duration and so on.

## Configuration dialog

From studio window, you can press Control+NVDA+0 to open the add-on configuration dialog. Alternatively, go to NVDA's preferences menu and select SPL Studio Settings item.

## SPL touch mode

If you are using Studio on a touchscreen computer running Windows 8 or later and have NVDA 2012.3 or later installed, you can perform some Studio commands from the touchscreen. First use three finger tap to switch to SPL mode, then use the touch commands listed above to perform commands.

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

[3]: https://bitbucket.org/nvdaaddonteam/stationplaylist/wiki/SPLAddonGuide

[4]: https://bitbucket.org/nvdaaddonteam/stationplaylist/wiki/DownloadLegacy
