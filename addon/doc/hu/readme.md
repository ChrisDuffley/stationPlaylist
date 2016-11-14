# StationPlaylist Studio #

* Készítők: Geoff Shang, Joseph Lee, és további közreműködők
* Letöltés [Stabil verzió][1]
* Letöltés [Fejlesztői verzió][2]
* Download [long-term support version][3] - add-on 15.x for Studio 5.0x
  users

Ez a kiegészítő javítja a Station Playlist Studio nevű online
rádióadás-vezérlő program használhatóságát, egyúttal egy olyan
segédprogramot is nyújt, amivel bárhonnan vezérelhető a szoftver.

For more information about the add-on, read the [add-on guide][4]. For
developers seeking to know how to build the add-on, see
buildInstructions.txt located at the root of the add-on source code
repository.

IMPORTANT: This add-on requires NVDA 2015.3 or later and StationPlaylist
Studio 5.00 or later. If you have installed NVDA 2016.1 or later on Windows
8 and later, disable audio ducking mode. Also, add-on 8.0/16.10 requires
Studio 5.10 and later, and for broadcasters using Studio 5.0x, a long-term
support version (7.x) is available.

## Gyorsbillentyűk

* Alt+Shift+T a Studio ablakában: Bemondja a lejátszás alatt álló dal eltelt
  idejét.
* Ctrl+Alt+T, vagy kétujjas lefelé pöccintés a Studio ablakában: bemondja a
  lejátszás alatt álló dal hátralévő idejét.
* NVDA+Shift+F12, vagy kétujjas felfelé pöccintés a Studio ablakában:
  Bemondja a a broadcaster idejét, pl 5 perc az óra végéig.
* Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens
  end of track setting dialog.
* Alt+NVDA+2, vagy kétujjas balra pöccintés a Studio ablakában: Megnyitja a
  zeneszám intró beállítása párbeszédpanelt.
* Alt+NVDA+3 from Studio window: Toggles cart explorer to learn cart
  assignments.
* Alt+NVDA+4 from Studio window: Opens microphone alarm dialog.
* Control+NVDA+F a Studio ablakában: Megnyit egy párbeszédablakot, ahol
  előadó, és dalnév szerint kereshetőek dalok. Nyomja meg az NVDA+F3
  billentyűparancsokat előre, vagy az NVDA+Shift+F3 billentyűket hátra
  kereséshez.
* Alt+NVDA+R a Studio ablakában: Átugorja a gyűjtemény átvizsgálás
  beállításait.
* Control+Shift+X a Studio ablakában: Átugorja a braille időzítő
  beállításait.
* Control+Alt+right/left arrow (while focused on a track): Announce
  next/previous track column.
* Control+NVDA+1 through 0 (6 for Studio 5.0x): Announce column content for
  a specified column.
* Alt+NVDA+C while focused on a track: announces track comments if any.
* Alt+NVDA+0 from Studio window: Opens the Studio add-on configuration
  dialog.
* Control+NVDA+- (hyphen) from Studio window: Send feedback to add-on
  developer using the default email client.
* Alt+NVDA+F1: Open welcome dialog.

## Nem hozzárendelt parancsok

Az alábbi parancsok nincsenek billentyűparancshoz rendelve. Ha ezt meg
szeretné változtatni, használja a Beviteli Parancsok párbeszédpanelt.

* Bármely programból az SPL Studio ablakára vált.
* SPL Vezérlőréteg
* SPL segédréteg az SPL Studio-ból.
* Másodpercre pontosan bejelenti az időt az SPL Studioból.
* Toggling track dial on or off (works properly while a track is focused; to
  assign a command to this, move to a track in Studio, then open NVDA's
  input gestures dialog.).
* Hőmérséklet bejelentése.
* A következő zeneszám címének bemondása, amennyiben van ilyen.
* Announcing title of the currently playing track.
* Marking current track for start of track time analysis.
* Performing track time analysis.
* Find text in specific columns.
* Find tracks with duration that falls within a given range via time range
  finder.
* Quickly enable or disable metadata streaming.

## Kiegészítő parancsok a Sam és az SPL encoderek használatához

A következő parancsok állnak rendelkezésre a Sam és SPL encoderek
használatához:

* F9: Csatlakozás streaming szerverhez
* F10 (csak SAM encoder): Kapcsolat bontása a streaming szerverrel
* Control+F9/Control+F10 (csak a SAM encoderben): Csatlakozik az összes
  encoderhez, vagy bontja a kapcsolatot velük.
* F11: A kiválasztott encoder számára a Studio ablakára vált, amennyiben
  kapcsolódva van.
* Shift+F11: A Studio elkezdi lejátszani az első kijelölt dalt, amennyiben
  az encoder egy Streaming szerverhez kapcsolódik.
* Control+F11: A kiválasztott encoder ellenőrzése a háttérben.
* F12: Opens a dialog to enter custom label for the selected encoder or
  stream.
* Control+F12: opens a dialog to select the encoder you have deleted (to
  realign stream labels and encoder settings).
* Alt+NVDA+0: Opens encoder settings dialog to configure options such as
  stream label.

In addition, column review commands are available, including:

* Control+NVDA+1: Encoder position.
* Control+NVDA+2: stream label.
* Control+NVDA+3 from SAM Encoder: Encoder format.
* Control+NVDA+3 from SPL Encoder: Encoder settings.
* Control+NvDA+4 from SAM Encoder: Encoder connection status.
* Control+NVDA+4 from SPL Encoder: Transfer rate or connection status.
* Control+NVDA+5 from SAM Encoder: Connection status description.

## SPL segédréteg

This layer command set allows you to obtain various status on SPL Studio,
such as whether a track is playing, total duration of all tracks for the
hour and so on. From any SPL Studio window, press the SPL Assistant layer
command, then press one of the keys from the list below (one or more
commands are exclusive to playlist viewer). You can also configure NvDA to
emulate commands from other screen readers.

The available commands are:

* A: Automatikus lejátszás.
* C (Shift+C in JAWS and Window-Eyes layouts): Title for the currently
  playing track.
* C (JAWS and Window-Eyes layouts): Toggle cart explorer (playlist viewer
  only).
* D (R in JAWS layout): Remaining duration for the playlist (if an error
  message is given, move to playlist viewer and then issue this command).
* E (G in Window-Eyes layout): Metadata streaming status.
* Shift+1 through Shift+4, Shift+0: Status for individual metadata streaming
  URL's (0 is for DSP encoder).
* E (Window-Eyes layout): Elapsed time for the currently playing track.
* F: Find track (playlist viewer only).
* H: A dal hossza az aktuális órában.
* Shift+H: Remaining track duration for the hour slot.
* I (L in JAWS or Window-Eyes layouts): Listener count.
* K: Move to the marked track (playlist viewer only).
* Control+K: Set the current track as the place marker track (playlist
  viewer only).
* L (Shift+L in JAWS and Window-Eyes layouts): Line in.
* M: Mikrofon.
* N: A soron következő dal címe.
* P: A lejátszás állapota, (lejátszás alatt, vagy leállítva).
* Shift+P: Pitch of the current track.
* R (Shift+E in JAWS and Window-Eyes layouts): Record to file
  enabled/disabled.
* Shift+R: A folyamatban lévő gyűjtemény-átvizsgálás követése.
* S: Zeneszám elkezdése (ütemezett idő)
* Shift+S: Time until selected track will play.
* T: Cart szerkesztési mód be-, és kikapcsolása.
* U: A Studio futási ideje.
* Control+Shift+U: Check for add-on updates.
* W: Időjárás és hőmérséklet, amennyiben be van állítva.
* Y: Playlist modified status.
* 1 through 0 (6 for Studio 5.0x): Announce column content for a specified
  column.
* F9: Mark current track for track time analysis (playlist viewer only).
* F10: Perform track time analysis (playlist viewer only).
* F12: Switch between current and a predefined profile.
* F1: Súgó
* Shift+F1: Opens online user guide.

## SPL Vezérlő

Ez a parancsréteg az SPL Studio bárhonnani vezérlését teszi lehetővé. Nyomja
le az SPL vezérlőréteg parancsát, ekkor az NVDA bemondja: "SPL
Vezérlőréteg." Használjon további parancsokat a Studio egyéb beállításainak
megadásához, mint a mikrofon be- és kikapcsolása, vagy a következő dalra
ugrás.

Az elérhető SPL Vezérlőparancsok a következők:

* P: A következő kijelölt dal lejátszása.
* U: A lejátszás szüneteltetése és folytatása.
* S: a zeneszám megállítása elhalkítással, T: a zeneszám megállítása
  azonnal.
* M, Shift+M: A mikrofon be-, és kikapcsolása, N: A mikrofon bekapcsolása
  elhalkulás nélkül.
* A, Shift+A: az automatikus lejátszás be-, és kikapcsolása.
* L, Shift+L: a vonalbemenet engedélyezése, és letiltása.
* Press R to hear remaining time for the currently playing track.
* Használja a Shift+R billentyűparancsot a gyűjtemény átvizsgálás
  folyamatának követéséhez.
* E: Az ellenőrzés alatt álló encoderek száma.
* Press I to obtain listener count.
* Az F1 billentyűvel listáztathatja az elérhető parancsokat.

## Track alarms

By default, NvDA will play a beep if five seconds are left in the track
(outro) and/or intro. To configure this value as well as to enable or
disable them, press Alt+NVDA+1 or Alt+NVDA+2 to open end of track and song
ramp dialogs, respectively. In addition, use Studio add-on settings dialog
to configure if you'll hear a beep, a message or both when alarms are turned
on.

## Mikrofon figyelmeztetés

You can ask NVDA to play a sound when microphone has been active for a
while. Press Alt+NVDA+4 to configure alarm time in seconds (0 disables it).

## Dalkereső

Ha egy dalnévre, vagy dalra szeretne keresni előadó alapján, nyomja meg a
Control+NVDA+F billentyűket a dallistában. Írja be a dal, vagy az előadó
nevét. Az NVDA találat esetén a dalra ugrik, vagy a találat sikertelenségét
hibaüzenettel jelzi. Egy előzőleg begépelt dal vagy előadó ismételt
kereséséhez nyomja meg az NVDA+F3 (előre keresés), vagy az NVDA+Shift+F3
(hátra keresés) billentyűket.

Megjegyzés: a Dalkereső figyelembe veszi a kis- és nagybetűket.

## Cart Explorer

A verzió függvényében az SPL Studio 96 cart hozzárendelését teszi lehetővé a
lejátszáshoz. Az NVDA segítségével hallható hogy milyen cart vagy csengés
van hozzárendelve ezekhez a parancsokhoz.

To learn cart assignments, from SPL Studio, press Alt+NVDA+3. Pressing the
cart command once will tell you which jingle is assigned to the
command. Pressing the cart command twice will play the jingle. Press
Alt+NvDA+3 to exit cart explorer. See the add-on guide for more information
on cart explorer.

## Track Dial

You can use arrow keys to review various information about a track. To turn
Track Dial on, while a track is focused in the main playlist viewer, press
the command you assigned for toggling Track Dial. Then use left and right
arrow keys to review information such as artist, duration and so
on. Alternatively, press Control+Alt+left or right arrows to navigate
between columns without invoking Track Dial.

## Track time analysis

To obtain length to play selected tracks, mark current track for start of
track time analysis (SPL Assistant, F9), then press SPL Assistant, F10 when
reaching end of selection.

## Columns Explorer

By pressing Control+NVDA+1 through 0 (6 for Studio 5.0x) or SPL Assistant, 1
through 0 (6 for Studio 5.01 and earlier), you can obtain contents of
specific columns. By default, these are artist, title, duration, intro,
category and filename (Studio 5.10 adds year, album, genre and time
scheduled). You can configure which columns will be explored via columns
explorer dialog found in add-on settings dialog.

## Beállítások párbeszédpanel

From studio window, you can press Alt+NVDA+0 to open the add-on
configuration dialog. Alternatively, go to NVDA's preferences menu and
select SPL Studio Settings item. This dialog is also used to manage
broadcast profiles.

## SPL érintőmód

Amennyiben érintőképernyős számítógépen használja a Studiot Windows 8, vagy
újabb verzió alatt, NVDA 2012.3 vagy újabb verzióval, bizonyos Studio
parancsokat végrehajthat az érintőképernyőn is. Először 3 ujjas koppintással
váltson SPL módra, és utána már használhatók az alább felsorolt parancsok.

## Version 16.11/15.3-LTS

* Initial support for StationPlaylist Studio 5.20, including improved
  responsiveness when obtaining status information such as automation status
  via SPL Assistant layer.
* Fixed issues related to searching for tracks and interacting with them,
  including inability to check or uncheck place marker track or a track
  found via time range finder dialog.
* Column announcement order will no longer revert to default order after
  changing it.
* 16.11: If broadcast profiles have errors, error dialog will no longer fail
  to show up.

## Version 16.10.1/15.2-LTS

* You can now interact with the track that was found via Track Finder
  (Control+NVDA+F) such as checking it for playback.
* Fordítások frissítése

## Changes for 8.0/16.10/15.0-LTS

Version 8.0 (also known as 16.10) supports SPL Studio 5.10 and later, with
15.0-LTS (formerly 7.x) designed to provide some new features from 8.0 for
users using earlier versions of Studio. Unless otherwise noted, entries
below apply to both 8.0 and 7.x. A warning dialog will be shown the first
time you use add-on 8.0 with Studio 5.0x installed, asking you to use 7.x
LTS version.

* Version scheme has changed to reflect release year.month instead of
  major.minor. During transition period (until mid-2017), version 8.0 is
  synonymous with version 16.10, with 7.x LTS being designated 15.0 due to
  incompatible changes.
* Add-on source code is now hosted on GitHub (repository located at
  https://github.com/josephsl/stationPlaylist).
* Added a welcome dialog that launches when Studio starts after installing
  the add-on. A command (Alt+NvDA+F1) has been added to reopen this dialog
  once dismissed.
* Changes to various add-on commands, including removal of status
  announcement toggle (Control+NvDA+1), reassigned end of track alarm to
  Alt+NVDA+1, Cart Explorer toggle is now Alt+NvDA+3, microphone alarm
  dialog is Alt+NVDA+4 and add-on/encoder settings dialog is
  Alt+NvDA+0. This was done to allow Control+NVDA+number row to be assigned
  to Columns Explorer.
* 8.0: Relaxed Columns Explorer restriction in place in 7.x so numbers 1
  through 6 can be configured to announce Studio 5.1x columns.
* 8.0: Track Dial toggle command and the corresponding setting in add-on
  settings are deprecated and will be removed in 9.0. This command will
  remain available in add-on 7.x.
* Added Control+Alt+Home/End to move Column Navigator to first or last
  column in Playlist Viewer.
* You can now add, view, change or delete track comments (notes). Press
  Alt+NVDA+C from a track in the playlist viewer to hear track comments if
  defined, press twice to copy comment to clipboard or three times to open a
  dialog to edit comments.
* Added ability to notify if a track comment exists, as well as a setting in
  add-on settings to control how this should be done.
* Added a setting in add-on settings dialog to let NVDA notify you if you've
  reached top or bottom of playlist viewer.
* When resetting add-on settings, you can now specify what gets reset. By
  default, add-on settings will be reset, with checkboxes for resetting
  instant switch profile, time-based profile, encoder settings and erasing
  track comments added to reset settings dialog.
* In Track Tool, you can obtain information on album and CD code by pressing
  Control+NVDA+9 and Control+NVDA+0, respectively.
* Performance improvements when obtaining column information for the first
  time in Track Tool.
* 8.0: Added a dialog in add-on settings to configure Columns Explorer slots
  for Track Tool.
* You can now configure microphone alarm interval from microphone alarm
  dialog (Alt+NvDA+4).

## Version 7.5/16.09

* NVDA will no longer pop up update progress dialog if add-on update channel
  has just changed.
* NVDA will honor the selected update channel when downloading updates.
* Fordítások frissítése

## Version 7.4/16.08

Version 7.4 is also known as 16.08 following the year.month version number
for stable releases.

* It is possible to select add-on update channel from add-on
  settings/advanced options, to be removed later in 2017. For 7.4, available
  channels are beta, stable and long-term.
* Added a setting in add-on settings/Advanced options to configure update
  check interval between 1 and 30 days (default is 7 or weekly checks).
* SPL Controller command and the command to focus to Studio will not be
  available from secure screens.
* New and updated translations and added localized documentation in various
  languages.

## Changes for 7.3

* Slight performance improvements when looking up information such as
  automation via some SPL Assistant commands.
* Fordítások frissítése

## Changes for 7.2

* Due to removal of old-style internal configuration format, it is mandatory
  to install add-on 7.2. Once installed, you cannot go back to an earlier
  version of the add-on.
* Added a command in SPL Controller to report listener count (I).
* You can now open SPL add-on settings and encoder settings dialogs by
  pressing Alt+NVDA+0. You can still use Control+NVDA+0 to open these
  dialogs (to be removed in add-on 8.0).
* In Track Tool, you can use Control+Alt+left or right arrow keys to
  navigate between columns.
* Contents of various Studio dialogs such as About dialog in Studio 5.1x are
  now announced.
* In SPL Encoders, NVDA will silence connection tone if auto-connect is
  enabled and then turned off from encoder context menu while the selected
  encoder is connecting.
* Fordítások frissítése

## Changes for 7.1

* Fixed erorrs encountered when upgrading from add-on 5.5 and below to 7.0.
* When answering "no" when resetting add-on settings, you'll be returned to
  add-on settings dialog and NVDA will remember instant switch profile
  setting.
* NVDA will ask you to reconfigure stream labels and other encoder options
  if encoder configuration file becomes corrupted.

## Changes for 7.0

* Added add-on update check feature. This can be done manually (SPL
  Assistant, Control+Shift+U) or automatically (configurable via advanced
  options dialog from add-on settings).
* It is no longer required to stay in the playlist viewer window in order to
  invoke most SPL Assistant layer commands or obtain time announcements such
  as remaining time for the track and broadcaster time.
* Changes to SPL Assistant commands, including playlist duration (D),
  reassignment of hour selection duration from Shift+H to Shift+S and
  Shift+H now used to announce duration of remaining tracks for the current
  hour slot, metadata streaming status command reassigned (1 through 4, 0 is
  now Shift+1 through Shift+4, Shift+0).
* It is now possible to invoke track finder via SPL Assistant (F).
* SPL Assistant, numbers 1 through 0 (6 for Studio 5.01 and earlier) can be
  used to announce specific column information. These column slots can be
  changed under Columns Explorer item in add-on settings dialog.
* Fixed numerous errors reported by users when installing add-on 7.0 for the
  first time when no prior version of this add-on was installed.
* Improvements to Track Dial, including improved responsiveness when moving
  through columns and tracking how columns are presented on screen.
* Added ability to press Control+Alt+left or right arrow keys to move
  between track columns.
* It is now possible to use a different screen reader command layout for SPL
  Assistant commands. Go to advanced options dialog from add-on settings to
  configure this option between NVDA, JAWS and Window-Eyes layouts. See the
  SPL Assistant commands above for details.
* NVDA can be configured to switch to a specific broadcast profile at a
  specific day and time. Use the new triggers dialog in add-on settings to
  configure this.
* NVDA will report name of the profile one is switching to via instant
  switch (SPL Assistant, F12) or as a result of time-based profile becoming
  active.
* Moved instant switch toggle (now a checkbox) to the new triggers dialog.
* Entries in profiles combo box in add-on settings dialog now shows profile
  flags such as active, whether it is an instant switch profile and so on.
* If a serious problem with reading broadcast profile files are found, NVDA
  will present an error dialog and reset settings to defaults instead of
  doing nothing or sounding an error tone.
* Settings will be saved to disk if and only if you change settings. This
  prolongs life of SSD's (solid state drives) by preventing unnecessary
  saves to disk if no settings have changed.
* In add-on settings dialog, the controls used to toggle announcement of
  scheduled time, listener count, cart name and track name has been moved to
  a dedicated status announcements dialog (select status announcement button
  to open this dialog).
* Added a new setting in add-on settings dialog to let NVDA play beep for
  different track categories when moving between tracks in playlist viewer.
* Attempting to open metadata configuration option in add-on settings dialog
  while quick metadata streaming dialog is open will no longer cause NVDA to
  do nothing or play an error tone. NvDA will now ask you to close metadata
  streaming dialog before you can open add-on settings.
* When announcing time such as remaining time for the playing track, hours
  are also announced. Consequently, the hour announcement setting is enabled
  by default.
* Pressing SPL Controller, R now causes NVDA to announce remaining time in
  hours, minutes and seconds (minutes and seconds if this is such a case).
* In encoders, pressing Control+NVDA+0 will present encoder settings dialog
  for configuring various options such as stream label, focusing to Studio
  when connected and so on.
* In encoders, it is now possible to turn off connection progress tone
  (configurable from encoder settings dialog).

## Changes for 6.4

* Fixed a major problem when switching back from an instant switch profile
  and the instant switch profile becomes active again, seen after deleting a
  profile that was positioned right before the previously active
  profile. When attempting to delete a profile, a warning dialog will be
  shown if an instant switch profile is active.

## Changes for 6.3

* Internal security enhancements.
* When add-on 6.3 or later is first launched on a computer running Windows 8
  or later with NVDA 2016.1 or later installed, an alert dialog will be
  shown asking you to disable audio ducking mode (NVDA+Shift+D). Select the
  checkbox to suppress this dialog in the future.
* Added a command to send bug reports, feature suggestions and other
  feedback to add-on developer (Control+NVDA+dash (hyphen, "-")).
* Fordítások frissítése

## Changes for 6.2

* Fixed an issue with playlist remainder command (SPL Assistant, D (R if
  compatibility mode is on)) where the duration for the current hour was
  announced as opposed to the entire playlist (the behavior of this command
  can be configured from advanced settings found in add-on settings dialog).
* NvDA can now announce name of the currently playing track while using
  another program (configurable from add-on settings).
* The setting used to let SPL Controller command invoke SPL Assistant is now
  honored (previously it was enabled at all times).
* In SAM encoders, Control+F9 and Control+F10 commands now works correctly.
* In encoders, when an encoder is first focused and if this encoder is
  configured to be monitored in the background, NVDA will now start the
  background monitor automatically.

## Changes for 6.1

* Column announcement order and inclusion, as well as metadata streaming
  settings are now profile-specific settings.
* When changing profiles, the correct metadata streams will be enabled.
* When opening quick metadata streaming settings dialog (command
  unassigned), the changed settings are now applied to the active profile.
* When starting Studio, changed how the errors are displayed if the only
  corrupt profile is the normal profile.
* When changing certain settings using shortcut keys such as status
  announcements, fixed an issue where the changed settings are not retained
  when switching to and from an instant switch profile.
* When using a SPL Assistant command with a custom gesture defined (such as
  next track command), it is no longer required to stay in the Studio's
  playlist viewer to use these commands (they can be performed from other
  Studio windows).

## Changes for 6.0

* New SPL Assistant commands, including announcing title of the currently
  playing track (C), announcing status of metadata streaming (E, 1 through 4
  and 0) and opening the online user guide (Shift+F1).
* Ability to package favorite settings as broadcast profiles to be used
  during a show and to switch to a predefined profile. See the add-on guide
  for details on broadcast profiles.
* Added a new setting in add-on settings to control message verbosity (some
  messages will be shortened when advanced verbosity is selected).
* Added a new setting in add-on settings to let NVDA announce hours, minutes
  and seconds for track or playlist duration commands (affected features
  include announcing elapsed and remaining time for the currently playing
  track, track time analysis and others).
* You can now ask NVDA to report total length of a range of tracks via track
  time analysis feature. Press SPL Assistant, F9 to mark current track as
  start marker, move to end of track range and press SPL Assistant,
  F10. These commands can be reassigned so one doesn't have to invoke SPL
  Assistant layer to perform track time analysis.
* Added a column search dialog (command unassigned) to find text in specific
  columns such as artist or part of file name.
* Added a time range finder dialog (command unassigned) to find a track with
  duration that falls within a specified range, useful if wishing to find a
  track to fill an hour slot.
* Added ability to reorder track column announcement and to suppress
  announcement of specific columns if "use screen order" is unchecked from
  add-on settings dialog. Use "manage column announcement" dialog to reorder
  columns.
* Added a dialog (command unassigned) to quickly toggle metadata streaming.
* Added a setting in add-on settings dialog to configure when metadata
  streaming status should be announced and to enable metadata streaming.
* Added ability to mark a track as a place marker to return to it later (SPL
  Assistant, Control+K to set, SPL Assistant, K to move to the marked
  track).
* Improved performance when searching for next or previous track text
  containing the searched text.
* Added a setting in add-on settings dialog to configure alarm notification
  (beep, message or both).
* It is now possible to configure microphone alarm between 0 (disabled) and
  two hours (7200 seconds) and to use up and down arrow keys to configure
  this setting.
* Added a setting in add-on settings dialog to allow microphone active
  notification to be given periodically.
* You can now use Track Dial toggle command in Studio to toggle Track Dial
  in Track Tool provided that you didn't assign a command to toggle Track
  Dial in Track Tool.
* Added ability to use SPL Controller layer command to invoke SPL Assistant
  layer (configurable from advanced Settings dialog found in add-on settings
  dialog).
* Added ability for NvDA to use certain SPL Assistant commands used by other
  screen readers. To configure this, go to add-on settings, select Advanced
  Settings and check screen reader compatibility mode checkbox.
* In encoders, settings such as focusing to Studio when connected are now
  remembered.
* It is now possible to view various columns from encoder window (such as
  encoder connection status) via Control+NVDA+number command; consult the
  encoder commands above.
* Fixed a rare bug where switching to Studio or closing an NVDA dialog
  (including Studio add-on dialogs) prevented track commands (such as
  toggling Track Dial) from working as expected.

## Changes for 5.6

* In Studio 5.10 and later, NVDA no longer announces "not selected" when the
  selected track is playing.
* Due to an issue with Studio itself, NVDA will now announce name of the
  currently playing track automatically. An option to toggle this behavior
  has been added in studio add-on settings dialog.

## Changes for 5.5

* Play after connecting setting will be remembered when moving away from the
  encoder window.

## Changes for 5.4

* Performing library scan from Insert Tracks dialog no longer causes NVDA to
  not announce scan status or play error tones if NVDA is configured to
  announce library scan progress or scan count.
* Fordítások frissítése

## A 3.0 verzió változásai

* Az SPL Encoder felhasználók számára is elérhető az a hibajavítás, mely azt
  orvosolja, hogy a SAM Encoder nem indította el a következő zeneszámot,
  amikor egy másik lejátszás alatt volt, és az encoder kapcsolódott.
* Az NVDA már nem ad hibajelző hangot, és nem viselkedik abnormálisan, ha az
  SPL Segédrétegnél lenyomja az F1 billentyűt, mely a kapcsolódó súgó
  párbeszédpanelt nyitja meg.

## Az 5.2 verzió változásai

* Az NVDA már nem engedi egyszerre megnyitni a beállítási és Riasztási
  párbeszédpaneleket. Egy figyelmeztetés fog megjelenni, mely megkér a
  korábban megnyitott párbeszédpanelek bezárására, mielőtt a kívánt
  párbeszédpanelt megnyitná.
* Egy vagy több encoder ellenőrzése közben az SPL vezérlőpult képes
  bejelenteni az encoderek számát, azonosítóját, és stream címkéit,
  amennyiben rendelkeznek vele.
* Az NVDA támogatja a kapcsolódás/Szétkapcsolódás minden parancsát
  (Control+F9/Control+F10) a SAM encoderekben.
* Az NVDA már nem indítja el a következő zeneszámot abban az esetben, ha a
  Studio épp lejátszik egy dalt, és olyankor kapcsolódik egy encoderhez,
  miközben a zeneszám lejátszása kapcsolódás után opció be van kapcsolva.
* Fordítások frissítése

## Az 5.1 verzió változásai

* A Track Tool egyéni oszlopai áttekinthetők a track dial használatával
  (nincs billentyűparancs hozzárendelve). Fontos, hogy ehhez a Studionak
  aktívnak kell lennie.
* Hozzáadtak egy jelölőnégyzettel állítható opciót a kiegészítő beállítási
  párbeszédpanelén, amellyel a lejátszás alatt álló cart nevének bemondása
  szabályozható.
* A mikrofon be- és kikapcsolása az SPL Vezérlőpultról már nem okoz
  hibajelző hangot a be- és kikapcsolás hangja helyett.
* Amennyiben egy SPL segédréteg billentyűparancs egy másik funkcióhoz is
  hozzá van rendelve, akkor amint lenyomja ezt a billentyűkombinációt az SPL
  segédréteg megnyitása után, az NVDA haladéktalanul bezárja a segédréteget.

## Az 5.0 verzió változásai

* Saját beállítási párbeszédpanelt adtak az SPL kiegészítőhöz, ami elérhető
  az NVDA Beállítások menüjében, vagy aktiválható a Control+NVDA+0
  billentyűparanccsal az SPL ablakában.
* A kiegészítő beállításainak párbeszédpanelén már visszaállíthatók a
  beállítások az alapértelmezett értékekre.
* Ha néhány beállítás hibát tartalmaz, akkor csak az érintett beállítások
  lesznek visszaállítva az alapértelmezett értékekre.
* Hozzáadtak egy saját SPL érintőmódot, amely bizonyos Studio parancsokat
  elérhetővé tesz érintőképernyőről is.
* Változások az SPL segédrétegben: F1 réteg súgó parancs hozzáadva,
  ill. eltávolítva a hallgatók számának bejelentése (Shift+I) és az
  ütemezett idő bejelentése (Shift+S) parancsok. Ezeket beállíthatja a
  kiegészítő beállítási párbeszédpanelén.
* A ki/bekapcsolás jelzése átnevezve állapotjelzésre, mivel más
  állapotinformációkat is jelezhet hangjelzés, pl. a gyűjtemény átvizsgálás
  befejezését.
* Az állapotjelzés beállítása megmarad a munkafolyamatokon keresztül,
  korábban ezt mindig manuálisan be kellett állítani a Studio indulásakor.
* A Track Dial funkció használatával áttekintheti a fő lejátszásilistában a
  zeneszámokhoz tartozó bejegyzések oszlopait. A funkció bekapcsolásához
  használja a hozzárendelt billentyűparancsot.
* Saját billentyűparancsok rendelhetők hőmérsékleti információk és a
  következő zeneszámok címének lekérdezéséhez.
* Hozzáadtak egy, a riasztás be- és kikapcsolására szolgáló jelölőnégyzetet
  a zeneszám végi, és a zeneszám intro beállítása párbeszédpanelhez. A
  jelölőnégyzet bejelölt állapotában van bekapcsolva az opció. Ez a
  kiegészítő beállítási párbeszédpanelén is beállítható.
* Hibajavítás: Korábban, ha egy riasztás, vagy keresés párbeszédpanel
  parancs olyankor lett kiadva, amikor másik riasztás, vagy keresés
  párbeszédpanel is nyitva volt, az az épp aktív párbeszédpanel újabb
  példányának a megnyitásához vezethetett. Az NVDA most már egy üzenettel
  figyelmeztet, hogy a korábban megnyitott párbeszédpanelt előbb be kell
  zárni.
* Cart explorer változások és javítások: Korábban rossz cart sorozatok
  böngészése, amikor a fókusz nincs a lejátszási listán. Innentől a Cart
  Explorer már ellenőrzi, hogy a lejátszási lista van-e fókuszban.
* Lehetőség, hogy egy SPL vezérlőréteg paranccsal elő lehessen hívni az SPL
  segédréteget. (kísérleti fázisban van). A részleteket keresse a kiegészítő
  útmutatójában.
* Az encoder ablakokban az NVDA idő és dátum lekérdezésére szolgáló parancsa
  (NVDA+F12) az időt másodperces pontossággal mondja be.
* Most már az egyes encodereket is ellenőrizheti, lekérdezheti a
  kapcsolódási állapotot, és egyéb üzeneteket, miközben az ellenőrizni
  kívánt encoder fókuszban van. SAM encoderek esetében jobban működik.
* Új parancs az SPL vezérlő rétegben az ellenőrzés alatt álló encoderek
  számának bejelentéséhez (E).
* megoldható az a hiba, hogy az NVDA nem a megfelelő encoderekhez társította
  a stream címkéket, ez főként encoderek törlése után jelentkezett. Nyomja
  meg a Control+F12 billentyűkombinációt, és jelölje ki a törölt encoder
  pozícióját.

## A 4.4/3.9 verzió változásai

* A gyűjtemény vizsgálat már működik a Studio 5.10 verziójának legújab
  kiadásában.

## A 4.3/3.8 verzió változásai

* Amennyiben a Cart Explorer aktív, és a fókuszt áthelyezzük a Studio más
  részére, pl.: A Zeneszám kiválasztása párbeszédpanelhez, az NVDA már nem
  mond be Cart üzeneteket, amennyiben cart kezelésére szolgáló
  billentyűparancsokat használunk. (Pl.: Zeneszám kijelölése a Zeneszám
  kiválasztása ablakban).
* Új SPL segédparancsok, többek közt váltás ütemezett idő és hallgatók száma
  közt (Shift+S és Shift+I)
* Amennyiben a Studiot úgy zárja be, hogy bizonyos figyelmeztetéseket
  beállító ablakok nyitva vannak, az NVDA érzékeli, hogy már bezárult a
  program, és nem fogja menteni a legutóbbi változásokat.
* Fordítások frissítése

## A 4.2/3.7 verzió változásai

* Az NVDA már megőrzi az új, és módosított encoder címkéket akkor is, ha a
  felhasználó kijelentkezik, vagy újraindítja a számítógépet.
* Ha a kiegészítő beállításai megsérülnek az NVDA indítása során , az NVDA
  visszaállítja a gyári beállításokat, és hibaüzenetben informálja a
  felhasználót.
* A kiegészítő 3.7 verziójában, a Studio 4.33 kiadásban a zeneszámok
  törlésénél fellépő fókusszal kapcsolatos hiba javítva lett. (ugyanaz a
  javítás történt a Studio 5.0x felhasználói számára is a kiegészítő 4.1
  verziójában).

## A 4.1 verzió változásai

* A Studio 5.0x verzióban, egy zeneszám törlése után a fő lejátszási lista
  ablakában az NVDA már nem a ténylegesen fókuszban lévő elem alatt
  található zeneszámot jelenti be. (Jobban észrevehető volt ez az utolsó
  előtti zeneszám törlése esetén, amikor az NVDA az "ismeretlen" bejelentést
  tette).
* Javítva számos gyűjtemény vizsgálattal kapcsolatos hiba a Studio 5.10
  verziótól, többek között: a gyűjteményben lévő  összes elem számának
  bejelentése a Zeneszám beillesztésére szolgáló párbeszédpanelen, valamint
  "A vizsgálat folyamatban van" bejelentése, amikor a vizsgálat folyamatát
  követni akarjuk SPL segédparanccsal.
* Braille kijelző használata esetén a Studio 5.10 verziójától, amennyiben
  egy zeneszám ki van jelölve, az alatta lévő zeneszám szóköz gombbal
  történő kijelölésekor a braille kijelzőn már megjelenik az újonnan
  kijelölt állapot.

## A 4.0/3.6 verzió változásai

A kiegészítő 4.0 verziója a Studio 5.00 és későbbi kiadásait támogatja. A
3.x verziókkal a Studio régebbi kiadásainak felhasználói is hozzájuthatnak a
4.0 verzió néhány újdonságához.

* Új SPL Segédparancsok, többek közt a zeneszám ütemezett ideje (S), a
  lejátszási lista hátralévő ideje (D), és hőmérséklet (W már amennyiben be
  van állítva). Ezen felül a Studio 5.x verzióban lejátszási lista
  módosítása (Y) és zeneszám magassága (Shift+P).
* Új SPL Vezérlőpult parancsok, többek közt gyűjtemény vizsgálat állapota
  (Shift+R) és mikrofon bekapcsolása halkítás nélkül (N). Az F1 billentyű
  lenyomására felugrik egy párbeszédpanel az elérhető parancsok listájával.
* A mikrofon SPL vezérlőpulton történő ki- és bekapcsolása esetén hangjelzés
  jelzi a ki- és a bekapcsolt állapotot.
* A beállítások, mint a dal végi idő már egy meghatározott konfigurációs
  fájlba kerülnek mentésre a felhasználó konfigurációs könyvtárában. Ez a
  kiegészítő 4.0 verziójától kezdve működik.
* Új parancs hozzáadva a zeneszám intro figyelmeztetés 1 és 9 másodperc
  közti beállítására (Alt+NVDA+2).
* A zeneszám végi, és az intro figyelmeztetés beállítására szolgáló
  párbeszédpanelen már a fel- és lenyíl segítségével is módosíthatók az
  értékek. helytelen érték megadása esetén a program a maximum értéket
  állítja be.
* Új parancs hozzáadva (Control+NVDA+4): Beállítható vele figyelmeztető
  jelzés, ha a mikrofon bizonyos ideig bekapcsolva marad.
* Új lehetőség: az idő órában, percben, és másodpercben történő bejelentése
  (nincs hozzárendelve parancs).
* Már lehetséges a gyűjtemény vizsgálata a zeneszámok beillesztése
  párbeszédpanelről, vagy akárhonnan. A vizsgálat állapotáról az Alt+NVDA+R
  billentyűparancs segítségével beállítható módon kaphatunk információkat.
* A Track Tool támogatása, beleértve hangjelzés, ha egy zeneszám beállított
  intróval rendelkezik, és parancsok zeneszámok bizonyos információinak
  lekérdezésére, mint játékidő, vagy jelölő pozíció.
* A StationPlaylist Encoder támogatása (Studio 5.00 és újabb verziói),
  hasonló mértékű támogatás, mint a SAM Encoder esetében.
* Az Encoder ablakokban az NVDA már nem ad hibát jelző hangot olyan esetben,
  amikor Streaming szerverre való kapcsolódás közben akarunk a minimalizált
  állapotban lévő Studio ablakára váltani.
* Már nincs hibajelzés címkével ellátott stream törlése esetén.
* Az intró, és a zeneszám végi riasztás állapota már Braille-kijelzőn is
  megjeleníthető, a Braille időzítő beállításával (Control+Shift+X).
* Javítva egy hiba, mely akkor lépett fel, ha minden ablak minimalizált
  állapota esetén akart valaki egy másik programból a Studio ablakára
  váltani.
* A Studio 5.01, vagy korábbi verzióinak használata esetén az NVDA már nem
  mond be egymás után többször bizonyos állapotinformációkat, mint pl a
  tervezett idő.

## A 3.5 verzió változásai

* Ha az NVDA olyankor van elindítva, vagy újraindítva, amikor a Studio 5.10
  verziójának fő lejátszási lista ablaka van fókuszban, az NVDA már nem ad
  hibajelzést, és/vagy nem jelenti be a következő és előző zeneszámot a
  listában történő navigálás során.
* Az SPL Studio 5.10 utáni kiadásaiban javítva a zeneszámok hátralévő és
  eltelt idejének kinyerése közben fellépő  hiba.
* Fordítások frissítése

## A 3.4 verzió változásai

* A Cart Explorerben a cart kezelő parancsok, (pl.: Control+F1) már jól
  működnek.
* Fordítások frissítése

## A 3.3 verzió változásai

* Streaming szerverhez való kapcsolódás esetén a z SAM encoderrel, már nem
  szükséges az encoder ablakában maradni a kapcsolat létrejöttéig.
* Javítva az a hiba, mely az encoder parancsok (pl.: stream címkéző)
  működését akadályozta olyankor, mikor más programoktól átkerült a fókusz
  az SAM ablakára.

## A 3.2 verzió változásai

* Új parancs hozzáadva az SPL vezérlőhöz a lejátszás alatt álló dal
  hátralévő idejének lekérdezésére (R).
* A SAM encoder ablakában a Shift+F11 billentyűparancs beviteli súgója
  javítva lett.
* A Cart Explorerben, amennyiben a Studio Standard van használatban, az NVDA
  figyelmeztet, hogy a cart hozzárendelési parancsok nem elérhetők.
* A Studio 5.10-es verziójában a dalkereső már nem ad hibát jelző hangot
  dalok keresése közben.
* Új és frissített fordítások.

## A 3.1 verzió változásai

* A SAM encoder ablakában hozzáadták a Shift+F11 parancsot, amivel
  beállítható, hogy kapcsolódás esetén a program elindítsa az első dalt.
* Számos, streaming szerverhez kapcsolódás közben jelentkező hiba javításra
  került: nem végrehajtott NVDA parancsok, az NVDA nem jelezte, hogy
  létrejött a kapcsolat, a kapcsolódást jelző hang helyett hibát jelző
  hangot játszott le sikeres kapcsolódás esetén.

## A 3.0 verzió változásai

* Hozzáadták a Cart Explorert a hozzárendelések megtekintéséhez, összesen 96
  hozzárendelés lehetséges.
* Új billentyűparancsok: broadcaster idő (NVDA+Shift+F12), új SPL kisegítő
  parancsok: hallgatók száma (I), a soron következő dal címe (N).
* A pprogram üzenetei, mint az automatikus lejátszás, már braille-ben is
  megjelennek függetlenül a parancsok bejelentési beállításától.
* Ha a StationPlaylist ablaka minimalizálva a tálca értesítési területén
  található, az NVDA jelzi ezt a tényt, amikor más programokból megkísérli
  az SPL ablakába lépést.
* Már nem hangzik el hibát jelző hang hangjelzésre állított visszajelzés
  esetén az állapotüzenetek változásaikor a ki és be kivételével. Pl. cartok
  lejátszása.
* Hibát jelző hang már nem hallható amikor megkísérel információkat
  lekérdezni, mint pl hátralévő idő, olyan esetben amikor a Studio egy másik
  ablaka (nem a dallista) van fókuszban, pl a Beállítások
  párbeszédpanel. Amennyiben a kívánt információk nem elérhetők, az NVDA
  közli ezt a tényt.
* Most már lehetségessé vált előadó alapján keresni dalokat, korábban csak
  cím alapján lehetett.
* Támogatás az SAM encoderhez, lehetőség az encoderek címkézésére, ill. a
  Studiora váltásra, amennyiben a kiválasztott encoder kapcsolódik. 
* A kiegészítő súgója már elérhető a bővítmények kezelése párbeszédpanelen.

## A 2.1 verzió változásai

* Javítva egy hiba, ami az SPL 5.x első NVDA futása melletti indításainál
  megakadályozta, hogy a felhasználók bizonyos állapotinformációkhoz
  hozzáférjenek, mint pl. az automatikus lejátszás.

## A 2.0 verzió változásai

* Néhány mindenütt elérhető és alkalmazáshoz kötött billentyűparancs el lett
  távolítva. Egyéni billentyűparancs hozzárendelésre a Beviteli Parancsok
  párbeszédpanelen van lehetőség. A kiegészítő 2.0 verziója NVDA 2013.3 vagy
  újabb verziót igényel.
* Több SPL segédparancsot hozzáadtak, köztük a cart szerkesztési módjának
  állapotát.
* Mostantól átválthat az SPL Studio-ra ha minden ablak kis méretben van
  (előfordulhat, hogy nem minden esetben működik).
* Kiterjesztették a dal végét előrejelző riasztás teljes idejét 59
  másodpercre.
* Lehetőség van dalra keresni egy lejátszási listában (Control+NVDA+F
  keresés, NVDA+F3 vagy NVDA+Shift+F3 előre és hátra keresés).
* A kombinált listamezők nevei helyesen hangzanak el (pl. a Beállítások
  párbeszédpanelen és a kezdeti SPL beállítási képernyőkön).
* Javítva egy hiba, ami az SPL Studio 5-ben azt eredményezte, hogy az NVDA
  helytelen információt közölt, mikor megkísérelte kinyerni egy dal
  hátralévő idejét.

## Az 1.2 verzió változásai

* Windows 8/8.1 rendszerek alá telepített Station Playlist 4.x verzió esetén
  ismét hallhatóvá vált az egyes zeneszámok eltelt, és hátralévő ideje.
* Fordítások frissítése

## Az 1.1 verzió változásai

* Új parancs hozzáadva a dalvégi figyelmeztetés beállítására
  (Control+NvDA+2).
* Hibajavítás: bizonyos szerkesztőmezők, különösen a Beállítások
  párbeszédpanelen nem voltak megfelelően bejelentve.
* Különböző fordítások hozzáadva.


## Az 1.0 verzió változásai

* Első kiadás

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=spl

[2]: http://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: http://spl.nvda-kr.org/files/get.php?file=spl-lts16

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide
