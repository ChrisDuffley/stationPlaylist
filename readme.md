# Station Playlist Studio #

* Authors: Geoff Shang, Joseph Lee and other contributors
* Download [stable version][1]
* Download [development version][2]

This add-on package provides improved usage of Station Playlist Studio, as well as providing utilities to control the Studio from anywhere.

For more information about the add-on, read the [add-on guide][3].

IMPORTANT: Due to major incompatible changes and key assignments, please remove add-on version 1.2 before installing version 2.0 or later. Also, add-on 2.1 and later requires NVDA 2014.1 or later.

## Shortcut keys

* Alt+Shift+T from Studio window: announce elapsed time for the currently playing trakc.
* Control+Alt+T from Studio window: announce remaining time for the currently playing trakc.
* NVDA+Shift+F12 from Studio window: announces broadcaster time such as 5 minutes to top of the hour.
* Control+NVDA+1 from Studio window: toggles announcement of toggle messages (such as automation) between words and beeps.
* Control+NVDA+2 from Studio window: Opens end of track setting dialog.
* Control+NVDA+3 from Studio window: Toggles cart explorer to learn cart assignments.
* Control+NVDA+f from Studio window: Opens a dialog to find a track based on artist or song name. Press NvDA+F3 to find forward or NVDA+Shift+F3 to find backward.

## Unassigned commands

The following commands are not assigned by default; if you wish to assign it, use Input Gestures dialog to add custom commands.

* Switching to SPL Studio window from any program.
* SPL Controller layer.
* SPL Assistant layer from SPL Studio.

Note: Input Gestures dialog is available in 2013.3 or later.

## SPL Assistant layer

This layer command set allows you to obtain various status on SPL Studio, such as whether a track is playing, total duration of all tracks for the hour and so on. From SPL Studio window, press the SPL Assistant layer command, then press one of the keys from the list below.

The available status information are:

* A: Automation.
* H: Duration of music for the current hour slot.
* Shift+H: Total duration of selected tracks for this hour slot (from the track list, press SPACE to select or uncheck the track to play).
* I: Listener count.
* L: Line in.
* M: Microphone.
* N: Title for the next scheduled track.
* P: Playback status (playing or stopped).
* R: Record to file enabled/disabled.
* T: Cart edit mode on/off.
* U: Studio up time.

## SPL Controller

The SPL Controller is a set of layered commands you can use to control SPL Studio anywhere. Press the SPL Controller layer command, and NVDA will say, "SPL Controller." Press another command to control various Studio settings such as microphone on/off or play the next track.

The available SPL Controller commands are:

* Press P to play the next selected track.
* Press U to pause or unpause playback.
* Press S to stop the track with fade out, or to stop the track instantly, press T.
* Press M or Shift+M to turn on or off the microphone, respectively.
* Press A to enable automation or Shift+A to disable it.
* Press L to enable line-in input or Shift+L to disable it.

## End of track alarm

Five seconds before the current track ends, NVDA will play a short beep to indicate that the track is about to end. This works anywhere (even within SPL Studio window). Press Control+NVDA+2 to configure this between 1 and 59 seconds.

## Track Finder

If you wish to quickly find a song by an artist or by song name, from track lisst, press Control+NVDA+F. Type the name of the artist or the song name. NVDA will either place you at the song if found or will display an error if it cannot find the song you're looking for. To find a previously entered song or artist, press NVDA+F3 or NVDA+Shift+F3 to find forward or backward.

Note: Track Finder is case-sensitive.

## Cart Explorer

Depending on edition, SPL Studio allows up to 96 carts to be assigned for playback. NVDA allows you to hear which cart, or jingle is assigned to these commands.

To learn cart assignments, from SPL Studio, press Control+NVDA+3. Pressing the cart command once will tell you which jingle is assigned to the command. Pressing the cart command twice will play the jingle. Press Control+NvDA+3 to exit cart explorer. See the add-on guide for more information on cart explorer.

## Changes for 3.0-dev

* Added Cart Explorer to learn cart assignments (up to 96 carts can be assigned).
* Added new commands, including broadcaster time (NVDA+Shift+F12) and listener count (i) and next track title (n) in SPL Assistant.
* Toggle messages such as automation are now displayed in braille regardless of toggle announcement setting.
* When StationPlaylist window is minimized to the system tray (notification area), NVDA will announce this fact when trying to switch to SPL from other programs.
* Error tones are no longer heard when toggle announcement is set to beeps and status messages other than on/off toggle are announced (example: playing carts).
* Error tones are no longer heard when trying to obtain information such as remaining time while other Studio window other than track list (such as Options dialog) is focused. If the needed information is not found, NVDA will announce this fact.
* It is now possible to search a track by artist name. Previously you could search by track title.

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
