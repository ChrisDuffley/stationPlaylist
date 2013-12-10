# Station Playlist Studio #

* Authors: Geoff Shang, Joseph Lee and other contributors
* Version: [0.2-dev][1]

This add-on package provides improved usage of Station Playlist Studio, as well as providing utilities to control the Studio from anywhere.

Note that if the downloaded file's extension is a zip, rename this to nvda-addon.

## Shortcut keys ##

* Control+Alt+T from Studio window: announce remaining time for the currently playing trakc.
* NvDA+Shift+P from Studio window: enter a layer command to find out status of playback such as automation.
* NVDA+Shift+grave from anywhere: switch to SPL Studio window from any program.
* NvDA+Grave from anywhere: the next command will control various aspects of SPL Studio.

## SPL Studio layer ##

This layer command set allows you to obtain various status on SPL Studio, such as whether a track is playing, total duration of all tracks for the hour and so on. To enter this mode, press NVDA+Shift+P (command is subject to change), then press one of the commands from the list below.

The available statu information are:

* A: Automation.
* H: Duration of music for the current hour slot.
* Shift+H: Total duration of selected tracks for this hour slot (from the track list, press SPACE to select or uncheck the track to play).
* L: Line in.
* M: Microphone.
* S: Playback status (playing or stopped).

## SPL Controller ##

The SPL Controller is a set of layered commands you can use anywhere. Press NvDA+Grave, and NVDA will say, "SPL Controller." Press another command to control various Studio settings such as microphone on/off or play the next track.

The available SPL Controller commands are:

* Press P to play the next selected track.
* Press S to stop the track with fade out, or to stop the track instantly, press T.
* Press M or Shift+M to turn on or off the microphone, respectivley.
* Press A to enable automation or Shift+A to disable it.
* Press L to enable line-in input or Shift+L to disable it.

[1]: http://addons.nvda-project.org/files/get.php?file=spl-dev