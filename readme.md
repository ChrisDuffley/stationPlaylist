# Station Playlist Studio #

* Authors: Geoff Shang, Joseph Lee and other contributors
* Download [stable version][1]
* Download [development version][2]

This add-on package provides improved usage of Station Playlist Studio, as well as providing utilities to control the Studio from anywhere.

For more information about the add-on, read the [add-on guide][3].

IMPORTANT: Due to major incompatible changes and key assignments, please remove add-on version 1.2 before installing version 2.0 or later. Also, add-on 2.1 and later requires NVDA 2014.1 or later. Add-on 4.0 requires SPL version 5.00 or later.

## Shortcut keys

* Alt+Shift+T from Studio window: announce elapsed time for the currently playing trakc.
* Control+Alt+T from Studio window: announce remaining time for the currently playing trakc.
* NVDA+Shift+F12 from Studio window: announces broadcaster time such as 5 minutes to top of the hour.
* Control+NVDA+1 from Studio window: toggles announcement of toggle messages (such as automation) between words and beeps.
* Control+NVDA+2 from Studio window: Opens end of track setting dialog.
* Alt+NVDA+2 from Studio window: Opens song intro alarm setting dialog.
* Control+NVDA+3 from Studio window: Toggles cart explorer to learn cart assignments.
* Control+NVDA+4 from Studio window: Opens microphone alarm dialog.
* Control+NVDA+f from Studio window: Opens a dialog to find a track based on artist or song name. Press NvDA+F3 to find forward or NVDA+Shift+F3 to find backward.
* Alt+NVDA+R from Studio window: Steps through library scan announcement settings.
* Control+Shift+X from Studio window: Steps through braille timer settings.

## Unassigned commands

The following commands are not assigned by default; if you wish to assign it, use Input Gestures dialog to add custom commands.

* Switching to SPL Studio window from any program.
* SPL Controller layer.
* SPL Assistant layer from SPL Studio.
* Announce time including seconds from SPL Studio.

Note: Input Gestures dialog is available in 2013.3 or later.

## Additional commands when using Sam or SPL encoders

The following commands are available when using Sam or SPL encoders:

* F9: connect to a streaming server.
* F10 (SAM encoder only): Disconnect from the streaming server.
* F11: Toggles whether NVDA will switch to Studio window for the selected encoder if connected.
* Shift+F11: Toggles whether Studio will play the first selected track when encoder is connected to a streaming server.
* F12: Opens a dialog to enter custom label for the selected encoder or stream.

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
* Shift+P: Pitch of the current track (SPL 5.00 and later).
* R: Record to file enabled/disabled.
* Shift+R: Monitor library scan in progress.
* S: Track starts in (scheduled).
* T: Cart edit mode on/off.
* U: Studio up time.
* W: Weather and temperature if configured.
* Y: Playlist modified status (SPL 5.00 and later).

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
* Press F1 to show a help dialog which lists available commands.

## End of track alarm

Five seconds before the current track ends, NVDA will play a short beep to indicate that the track is about to end. This works anywhere (even within SPL Studio window). Press Control+NVDA+2 to configure this between 1 and 59 seconds.

## Song intro alarm

If you have configured song intro time via Track Tool, NVDA will beep when the vocals are about to begin. From Studio window, press Alt+NVDA+2 to configure song intro alarm between 1 and 9 seconds.

## Track Finder

If you wish to quickly find a song by an artist or by song name, from track lisst, press Control+NVDA+F. Type the name of the artist or the song name. NVDA will either place you at the song if found or will display an error if it cannot find the song you're looking for. To find a previously entered song or artist, press NVDA+F3 or NVDA+Shift+F3 to find forward or backward.

Note: Track Finder is case-sensitive.

## Cart Explorer

Depending on edition, SPL Studio allows up to 96 carts to be assigned for playback. NVDA allows you to hear which cart, or jingle is assigned to these commands.

To learn cart assignments, from SPL Studio, press Control+NVDA+3. Pressing the cart command once will tell you which jingle is assigned to the command. Pressing the cart command twice will play the jingle. Press Control+NvDA+3 to exit cart explorer. See the add-on guide for more information on cart explorer.

## Changes for 4.0/3.x

Version 4.0 supports SPL Studio 5.00 and later, with 3.x released designed to provide some new features from 4.0 for users using earlier versions of Studio.

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
* Fixed an issue when trying to obtain remainig time and elapsed time for a track in later builds of Studio 5.10.
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
