# Station Playlist Studio #

* Authors: Geoff Shang, Joseph Lee and other contributors
* Release version: [1.1][1]
* Development version: [2.0-dev][2]

This add-on package provides improved usage of Station Playlist Studio, as well as providing utilities to control the Studio from anywhere.

For more information about the add-on, read the [add-on guide][3].

## Shortcut keys ##

* Alt+Shift+T from Studio window: announce elapsed time for the currently playing trakc.
* Control+Alt+T from Studio window: announce remaining time for the currently playing trakc.
* Control+NVDA+` (grave accent) from Studio window: enter a layer command to find out status of playback such as automation.
* Control+NVDA+1 from Studio window: toggles announcement of toggle messages (such as automation) between words and beeps.
* Control+NVDA+2 from Studio window: Opens end of track setting dialog.
* Control+NVDA+f from Studio window: Opens a dialog to find a track based on artist or song name.
* NVDA+Shift+grave from anywhere: switch to SPL Studio window from any program.
* NVDA+Grave from anywhere: the next command will control various aspects of SPL Studio.

## SPL Assistant layer

This layer command set allows you to obtain various status on SPL Studio, such as whether a track is playing, total duration of all tracks for the hour and so on. To enter this mode, press Control+NVDA+` (grave accent) from SPL Studio window, then press one of the commands from the list below.

The available status information are:

* A: Automation.
* H: Duration of music for the current hour slot.
* Shift+H: Total duration of selected tracks for this hour slot (from the track list, press SPACE to select or uncheck the track to play).
* L: Line in.
* M: Microphone.
* P: Playback status (playing or stopped).
* R: Record to file enabled/disabled.
* T: Cart edit mode on/off.
* U: Studio up time.

## SPL Controller ##

The SPL Controller is a set of layered commands you can use to control SPL Studio anywhere. Press NVDA+Grave, and NVDA will say, "SPL Controller." Press another command to control various Studio settings such as microphone on/off or play the next track.

The available SPL Controller commands are:

* Press P to play the next selected track.
* Press U to pause or unpause playback.
* Press S to stop the track with fade out, or to stop the track instantly, press T.
* Press M or Shift+M to turn on or off the microphone, respectivley.
* Press A to enable automation or Shift+A to disable it.
* Press L to enable line-in input or Shift+L to disable it.

## End of track alarm ##

Five seconds before the current track ends, NVDA will play a short beep to indicate that the track is about to end. This works anywhere (even within SPL Studio window). Press Control+NVDA+2 to configure this between 1 and 59 seconds.

## Changes for 2.0-dev

* Added more SPL Assistant commands such as cart edit mode status.
* You can now switch to SPL Studio even with all windows minimized (may not work in some cases).
* Extended the end of track alarm range to 59 seconds.

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
