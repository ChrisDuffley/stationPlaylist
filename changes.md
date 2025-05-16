# StationPlaylist Add-on Changelog

This page lists the complete changelog for StationPlaylist add-on releases.

## Version 25.06-LTS

Version 25.06.x is the last release series to support Studio 5.x with future releases requiring Studio 6.x. Some new features will be backported to 25.06.x if needed.

* NVDA will no longer forget to transfer broadcast profiles while updating the add-on (fixing a regression introduced in 25.05).
* Added a new command in SPL Assistant to announce playlist hour over/under by in minutes and seconds (O).
* In Studio, the command to step through library scan announcement settings has changed from Alt+NVDA+R to Shift+NVDA+R as the former command toggles remote access feature in NVDA 2025.1.
* NVDA will no longer play error tones or appear to do nothing when performing some SPL Assistant commands after resizing Studio window.
* The user interface for confirmation dialog shown when deleting broadcast profiles now resembles NVDA's configuration profile deletion interface.
* NVDA will recognize track column changes introduced in Creator and Track Tool 6.11.
* In columns explorer for Creator, "Date Restriction" column is now "Restrictions".
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

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer supported by Microsoft as of January 2023.
* Removed first and last track column commands (Control+Alt+Home/End) as NVDA includes these commands.
* Removed Streamer app module and buffer size edit field workaround as Streamer has become an alias module for SPL Engine.

## Version 22.03

This is the last stable version to support Studio 5.30 as wel as Windows 7 Service Pack 1, 8, and 8.1.

* NVDA 2021.3 or later is required.
* A warning message will be displayed when attempting to install the add-on on Windows 7, 8, and 8.1.
* It is no longer possible to perform the following commands if NVDA is running in secure mode: all SPL Controller layer commands, switching to Studio from other programs, obtaining Studio status and encoder status from other programs.
* It is no longer possible to copy track comments to the clipboard or add or change comments if NVDA is running in secure mode.
* It is no longer possible to copy playlist transcripts to clipboard or save it to a file if NVDA is running in secure mode. Only viewing transcripts will be allowed in secure mode.
* To improve security, online user guide command from SPL Assistant (Shift+F1) has been removed.
* It is no longer possible to create, copy, rename, delete, or configure instant switch status for broadcast profiles if NVDA is running in secure mode.
* It is no longer possible to configure advanced add-on settings or reset settings to defaults from add-on settings screen if NVDA is running in secure mode.
* In Studio, NVDA will no longer do nothing or play error tones if attempting to obtain playlist snapshots (SPL Assistant, F8) if the loaded playlist consists only of hour markers.
* In Creator 6.0, NVDA will no longer appear to do nothing when one of the columns explorer column is "Date Restriction" as the column has been renamed to "Restrictions".

## Version 22.01

* If add-on specific command-line switches such as "--spl-configinmemory" is specified when starting NVDA, NVDA will no longer add the specified parameter each time NVDA and/or Studio runs. Restart NVDA to restore normal functionality (without command-line switches).

## Version 21.11

* Initial support for StationPlaylist suite 6.0.

## Version 21.10

* NVDA 2021.2 or later is required due to changes to NVDA that affects this add-on.

## Version 21.08

* In SAM encoders, NVDA will no longer play a tone if the selected encoder becomes idle as this tone is really meant to help when debugging the add-on.

## Version 21.06

* NVDA will no longer do nothing or play error tones when trying to open various add-on dialogs such as encoder settings dialog. This is a critical fix required to support NVDA 2021.1.
* NVDA will no longer appear to do nothing or play error tones when trying to announce complete time (hours, minutes, seconds) from Studio (command unassigned). This affects NVDA 2021.1 or later.

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

## Version 19.11.1/18.09.13-LTS

* Initial support for StationPlaylist suite 5.40.
* In Studio, playlist snapshots (SPL Assistant, F8) and various time announcement commands such as remaining time (Control+Alt+T) will no longer cause NVDA to play error tones or do nothing if using NVDA 2019.3 or later.
* In Creator's track list items, "Language" column added in Creator 5.31 and later is properly recognized.
* In various lists in Creator apart from track list, NVDA will no longer announce odd column information if Control+NVDA+number row command is pressed.

## Version 19.11

* Encoder status command from SPL Controller (E) will announce connection status for the active encoder set instead of encoders being monitored in the background.
* NVDA will no longer appear to do nothing or play error tones when it starts while an encoder window is focused.

## Version 19.10/18.09.12-LTS

* Shortened the version announcement message for Studio when it starts.
* Version information for Creator will be announced when it starts.
* 19.10: custom command can be assigned for encoder status command from SPL Controller (E) so it can be used from everywhere.
* Initial support for AltaCast encoder (Winamp plugin and must be recognized by Studio). Commands are same as SPL Encoder.

## Version 19.08.1

* In SAM encoders, NVDA will no longer appear to do nothing or play error tones if an encoder entry is deleted while being monitored in the background.

## Version 19.08/18.09.11-LTS

* 19.08: NVDA 2019.1 or later is required.
* 19.08: NVDA will no longer appear to do nothing or play error tones when restarting it while Studio add-on settings dialog is open.
* NVDA will remember profile-specific setttings when switching between settings panels even after renaming the currently selected broadcast profile from add-on settings.
* NVDA will no longer forget to honor changes to time-based profiles when OK button is pressed to close add-on settings. This bug has been present since migrating to multi-page settings in 2018.

## Version 19.07/18.09.10-LTS

* Renamed the add-on from "StationPlaylist Studio" to "StationPlaylist" to better describe apps and features supported by this add-on.
* Internal security enhancements.
* If microphone alarm or metadata streaming settings are changed from add-on settings, NVDA will no longer fail to apply changed settings. This resolves an issue where microphone alarm did not start or stop properly after changing settings via add-on settings.

## Version 19.06/18.09.9-LTS

Version 19.06 supports SPL Studio 5.20 and later.

* Initial support for StationPlaylist Streamer.
* While running various Studio apps such as Track Tool and Studio, if a second instance of the app is started and then exits, NVDA will no longer cause Studio add-on configuration routines to produce errors and stop working correctly.
* Added labels for various options in SPL Encoder configuration dialog.

## Version 19.04.1

* Fixed several issues with redesigned column announcements and playlist transcripts panels in add-on settings, including changes to custom column order and inclusion not being reflected when saving and/or switching between panels.

## Version 19.04/18.09.8-LTS

* Various global commands such as entering SPL Controller and switching to Studio window will be turned off if NVDA is running in secure mode or as a Windows Store application.
* 19.04: in column announcements and playlist transcripts panels (add-on settings), custom column inclusion/order controls will be visible up front instead of having to select a button to open a dialog to configure these settings.
* In Creator, NVDA will no longer play error tones or appear to do nothing when focused on certain lists.

## Version 19.03/18.09.7-LTS

* Pressing Control+NVDA+R to reload saved settings will now also reload Studio add-on settings, and pressing this command three times will also reset Studio add-on settings to defaults along with NVDA settings.
* Renamed Studio add-on settings dialog's "Advanced options" panel to "Advanced".
* 19.03 experimental: in column announcements and playlist transcripts panels (add-on settings), custom column inclusion/order controls will be visible up front instead of having to select a button to open a dialog to configure these settings.

## Version 19.02

* Removed standalone add-on update check feature, including update check command from SPL Assistant (Control+Shift+U) and add-on update check options from add-on settings. Add-on update check is now performed by Add-on Updater.
* NVDA will no longer appear to do nothing or play error tones when microphone active interval is set, used to remind broadcasters that microphone is active with periodic beeps.
* When resetting add-on settings from add-on settings dialog/reset panel, NVDA will ask once more if an instant switch profile or a time-based profile is active.
* After resetting Studio add-on settings, NVDA will turn off microphone alarm timer and announce metadata streaming status, similar to after switching between broadcast profiles.

## Version 19.01.1

* NVDA will no longer announce "monitoring library scan" after closing Studio in some situations.

## Version 19.01/18.09.6-LTS

* NVDA 2018.4 or later is required.
* More code changes to make the add-on compatible with Python 3.
* 19.01: some message translations from this add-on will resemble NVDA messages.
* 19.01: add-on update check feature from this add-on is no more. An error message will be presented when trying to use SPL Assistant, Control+Shift+U to check for updates. For future updates, please use Add-on Updater add-on.
* Slight performance improvements when using NVDA with apps other than Studio while Voice Track Recorder is active. NVDA will still show performance issues when using Studio itself with Voice Track Recorder active.
* In encoders, if an encoder settings dialog is open (Alt+NVDA+0), NVDA will present an error message if trying to open another encoder settings dialog.

## Version 18.12

* Internal changes to make the add-on compatible with future NVDA releases.
* Fixed many instances of add-on messages spoken in English despite translated into other languages.
* If using SPL Assistant to check for add-on updates (SPL Assistant, Control+Shift+U), NVDA will not install new add-on releases if they require a newer version of NVDA.
* Some SPL Assistant commands will now require that the playlist viewer is visible and populated with a playlist, and in some cases, a track is focused. Commands affected include remaining duration (D), playlist snapshots (F8), and playlist transcripts (Shift+F8).
* Playlist remaining duration command (SPL Assistant, D) will now require a track from playlist viewer be focused.
* In SAM Encoders, you can now use table navigation commands (Control+Alt+arrow keys) to review various encoder status information.

## Version 18.11/18.09.5-LTS

Note: 18.11.1 replaces 18.11 in order to provide better support for Studio 5.31.

* Initial support for StationPlaylist Studio 5.31.
* You can now obtain playlist snapshots (SPL Assistant, F8) and transcripts (SPL Assistant, Shift+F8) while a playlist is loaded but the first track isn't focused.
* NVDA will no longer appear to do nothing or play error tones when trying to announce metadata streaming status when Studio starts if configured to do so.
* If configured to announce metadata streaming status at startup, metadata streaming status announcement will no longer cut off announcements about status bar changes and vice versa.

## Version 18.10.2/18.09.4-LTS

* Fixed inability to close the add-on settings screen if Apply button was pressed and subsequently OK or Cancel buttons were pressed.

## Version 18.10.1/18.09.3-LTS

* Resolved several issues related to encoder connection announcement feature, including not announcing status messages, failing to play the first selected track, or not switching to Studio window when connected. These bugs are caused by wxPython 4 (NVDA 2018.3 or later).

## Version 18.10

* NVDA 2018.3 or later is required.
* Internal changes to make the add-on more compatible with Python 3.

## Version 18.09.1-LTS

* When obtaining playlist transcripts in HTML table format, column headers are no longer rendered as a Python list string.

## Version 18.09-LTS

Version 18.09.x is the last release series to support Studio 5.10 and based on old technologies, with 18.10 and later supporting Studio 5.11/5.20 and new features. Some new features will be backported to 18.09.x if needed.

* NVDA 2018.3 or later is recommended due to introduction of wxPython 4.
* Add-on settings screen is now fully based on multi-page interface derived from NVDA 2018.2 and later.
* Test Drive Fast and Slow rings have been combined into "development" channel, with an option for development snapshot users to test pilot features by checking the new pilot features checkbox found in Advanced add-on settings panel. Users formerly on Test Drive Fast ring will continue to test pilot features.
* The ability to select different add-on update channel from add-on settings has been removed. Users wishing to switch to a different release channel should visit NVDA community add-ons website (addons.nvda-project.org), select StationPlaylist Studio, then download the appropriate release.
* Column inclusion checkboxes for column announcement and playlist transcripts, as well as metadata streams checkboxes have been converted to checkable list controls.
* When switching between settings panels, NVDA will remember current settings for profile-specific settings (alarms, column announcements, metadata streaming settings).
* Added CSV (comma-separated values) format as a playlist transcripts format.
* Pressing Control+NVDA+C to save settings will now also save Studio add-on settings (requires NVDA 2018.3).

## Version 18.08.2

* NVDA will no longer check for Studio add-on updates if Add-on Updater (proof of concept) add-on is installed. Consequently, add-on settings will no longer include add-on update related settings if this is the case. If using Add-on Updater, users should use features provided by this add-on to check for Studio add-on updates.

## Version 18.08.1

* Fixed yet another wxPython 4 compatibility issue seen when Studio exits.
* NVDA will announce an appropriate message when playlist modification text isn't present, commonly seen after loading an unmodified playlist or when Studio starts.
* NVDA will no longer appear to do nothing or play error tones when trying to obtain metadata streaming status via SPL Assistant (E).

## Version 18.08

* Add-on settings dialog is now based on multi-category settings interface found in NVDA 2018.2. Consequently, this release requires NVDA 2018.2 or later. The old add-on settings interface is deprecated and will be removed later in 2018.
* Added a new section (button/panel) in add-on settings to configure playlist transcripts options, which is used to configure column inclusion and ordering for this feature and other settings.
* When creating a table-based playlist transcripts and if custom column ordering and/or column removal is in effect, NVDA will use custom column presentation order specified from add-on settings and/or not include information from removed columns.
* When using column navigation commands in track items (Control+Alt+home/end/left arrow/right arrow) in Studio, Creator, and Track Tool, NVDA will no longer announce wrong column data after changing column position on screen via mouse.
* Significant improvements to NVDA's responsiveness when using column navigation commands in Creator and Track Tool. In particular, when using Creator, NVDA will respond better when using column navigation commands.
* NVDA will no longer play error tones or appear to do nothing when attempting to add comments to tracks in Studio or when exiting NVDA while using Studio, caused by wxPython 4 compatibility issue.

## Version 18.07

* Added an experimental multi-category add-on settings screen, accessible by toggling a setting in add-on settings/Advanced dialog (you need to restart NVDA after configuring this setting for the new dialog to show up). This is for NVDA 2018.2 users, and not all add-on settings can be configured from this new screen.
* NVDA will no longer play error tones or appear to do nothing when trying to rename a broadcast profile from add-on settings, caused by wxPython 4 compatibility issue.
* When restarting NVDA and/or Studio after making changes to settings in a broadcast profile other than normal profile, NVDA will no longer revert to old settings.
* It is now possible to obtain playlist transcripts for the current hour. Select "current hour" from list of playlist range options in playlist transcripts dialog (SPL Assistant, Shift+F8).
* Added an option in Playlist Transcripts dialog to have transcripts saved to a file (all formats) or copied to the clipboard (text and Markdown table formats only) in addition to viewing transcripts on screen. When transcripts are saved, they are saved to user's Documents folder under "nvdasplPlaylistTranscripts" subfolder.
* Status column is no longer included when creating playlist transcripts in HTML and Markdown table formats.
* When focused on a track in Creator and Track Tool, pressing Control+NVDA+number row twice will present column information on a browse mode window.
* In Creator and Track Tool, added Control+Alt+Home/End keys to move Column Navigator to first or last column for the focused track.

## Version 18.06.1

* Fixed several compatibility issues with wxPython 4, including inability to open track finder (Control+NVDA+F), column search and time ranger finder dialogs in Studio and stream labeler dialog (F12) from encoders window.
* While opening a find dialog from Studio and an unexpected error occurs, NVDA will present more appropriate messages instead of saying that another find dialog is open.
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
* Several add-on features were enhanced with extension points. This allows microphone alarm and metadata streaming feature to respond to changes in broadcast profiles. This requires NVDA 2017.4.
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
* In add-on settings, added a checkbox to let NVDA play a sound when listener requests arrive. To use this fully, requests window must pop up when requests arrive.
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
* Added a welcome dialog that launches when Studio starts after installing the add-on. A command (Alt+NVDA+F1) has been added to reopen this dialog once dismissed.
* Changes to various add-on commands, including removal of status announcement toggle (Control+NVDA+1), reassigned end of track alarm to Alt+NVDA+1, Cart Explorer toggle is now Alt+NVDA+3, microphone alarm dialog is Alt+NVDA+4 and add-on/encoder settings dialog is Alt+NVDA+0. This was done to allow Control+NVDA+number row to be assigned to Columns Explorer.
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
* You can now configure microphone alarm interval from microphone alarm dialog (Alt+NVDA+4).

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
* Attempting to open metadata configuration option in add-on settings dialog while quick metadata streaming dialog is open will no longer cause NVDA to do nothing or play an error tone. NVDA will now ask you to close metadata streaming dialog before you can open add-on settings.
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
* NVDA can now announce name of the currently playing track while using another program (configurable from add-on settings).
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
* Added ability for NVDA to use certain SPL Assistant commands used by other screen readers. To configure this, go to add-on settings, select Advanced Settings and check screen reader compatibility mode checkbox.
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
* If a custom command is assigned for an SPL Assistant layer command and this command is pressed right after entering SPL Assistant, NVDA will now promptly exit SPL Assistant.

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
* A workaround is now available to fix an issue where NVDA was announcing stream labels for the wrong encoders, especially after deleting an encoder (to realign stream labels, press Control+F12, then select the position of the encoder you have removed).

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
* Added a command (Alt+NVDA+2) to set song intro alarm time between 1 and 9 seconds.
* In end of track and intro alarm dialogs, you can use up and down arrows to change alarm settings. If a wrong value is entered, alarm value is set to maximum value.
* Added a command (Control+NVDA+4) to set a time when NVDA will play a sound when microphone has been active for a while.
* Added a feature to announce time in hours, minutes and seconds (command unassigned).
* It is now possible to track library scans from Insert Tracks dialog or from anywhere, and a dedicated command (Alt+NVDA+R) to toggle library scan announcement options.
* Support for Track Tool, including playing a beep if a track has intro defined and commands to announce information on a track such as duration and cue position.
* Support for StationPlaylist Encoder (Studio 5.00 and later), providing same level of support as found in SAM Encoder support.
* In encoder windows, NVDA no longer plays error tones when NVDA is told to switch to Studio upon connecting to a streaming server while Studio window is minimized.
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
* You can now search for a track in a playlist (Control+NVDA+F to find, NVDA+F3 or NVDA+Shift+F3 to find forward or backward, respectively).
* Correct names of combo boxes are now announced by NVDA (e.g. Options dialog and initial SPL setup screens).
* Fixed an issue where NVDA was announcing wrong information when trying to get remaining time for a track in SPL Studio 5.

## Changes for 1.2

* When Station Playlist 4.x is installed on certain Windows 8/8.1 computers, it is again possible to hear elapsed and remaining times for a track.
* Updated translations.

## Changes for 1.1

* Added a command (Control+NVDA+2) to set end of track alarm time.
* Fixed a bug in which field names for certain edit fields were not announced (particularly edit fields in Options dialog).
* Added various translations.

## Changes for 1.0

* Initial release.
