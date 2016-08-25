# StationPlaylist Studio #

* Автори: Geoff Shang, Joseph Lee и други сътрудници
* Изтегляне [стабилна версия][1]
* Изтегляне [работна версия][2]

This add-on package provides improved usage of StationPlaylist Studio, as
well as providing utilities to control the Studio from anywhere.

За повече информация относно добавката прочетете [ръководството за
добавката][3].

IMPORTANT: This add-on requires NVDA 2015.3 or later and StationPlaylist
Studio 5.00 or later. If you have installed NVDA 2016.1 or later on Windows
8 and later, disable audio ducking mode.

## Бързи клавиши

* Alt+Shift+T, докато сте в прозореца на програмата: съобщава изминало време
  за текущо просвирвания запис.
* Control+Alt+T (two finger flick down in SPL touch mode) from Studio
  window: announce remaining time for the currently playing trakc.
* NVDA+Shift+F12 (two finger flick up in SPL touch mode) from Studio window:
  announces broadcaster time such as 5 minutes to top of the hour.
* Control+NVDA+1 from Studio window: toggles announcement of status messages
  (such as automation and end of library scan) between words and beeps.
* Control+NVDA+2 (two finger flick right in SPL mode) from Studio window:
  Opens end of track setting dialog.
* Alt+NVDA+2 (two finger flick left in SPL mode) from Studio window: Opens
  song intro alarm setting dialog.
* Control+NVDA+3 докато сте в прозореца на програмата: Превключва прегледа
  на джингъли за изследване на назначенията на джингълите.
* Control+NVDA+4 от прозореца на Studio: Отваря диалоговия прозорец за
  предупреждението за микрофона.
* Control+NVDA+F докато сте в прозореца на програмата: Отваря прозорец за
  търсене на базата на името на изпълнител или песен. Натиснете NVDA+F3 за
  търсене напред или NVDA+Shift+F3 за търсене назад.
* Alt+NVDA+R от прозореца на Studio: Преминава през настройките за
  съобщаването на сканирането на библиотеката.
* Control+Shift+X от прозореца на Studio: Преминава през настройките за
  брайловия таймер.
* Control+Alt+right/left arrow (while focused on a track): Announce
  next/previous track column.
* Control+NVDA+0 or Alt+NVDA+0 from Studio window: Opens the Studio add-on
  configuration dialog.
* Control+NVDA+- (hyphen) from Studio window: Send feedback to add-on
  developer using the default email client.

## Неприсвоени команди

Следните команди не са присвоени по подразбиране; Ако искате да ги
присвоите, използвайте диалоговия прозорец за жестове на въвеждане, за да
добавите команди по избор.

* Превключване към прозореца на SPL Studio от всяка програма.
* Слой за контролера на SPL
* Помощен слой на SPL от SPL Studio.
* Съобщаване на времето, включително и секундите от SPL Studio.
* Toggling track dial on or off (works properly while a track is focused; to
  assign a command to this, move to a track in Studio, then open NVDA's
  input gestures dialog.).
* Announcing temperature.
* Announcing title of next track if scheduled.
* Announcing title of the currently playing track.
* Marking current track for start of track time analysis.
* Performing track time analysis.
* Find text in specific columns.
* Find tracks with duration that falls within a given range via time range
  finder.
* Quickly enable or disable metadata streaming.

## Допълнителни команди при използването на Sam или SPL енкодерите

Следните команди са налични при използването на Sam или SPL енкодерите:

* F9: Свързване с излъчващ сървър.
* F10 (само за SAM енкодера): Прекъсване на връзката с излъчващия сървър.
* Control+F9/Control+F10 (SAM encoder only): Connect or disconnect all
  encoders, respectivley.
* F11: Определя дали NVDA ще превключва към прозореца на програмата ако
  избрания енкодер е свързан.
* Shift+F11: Определя дали ще се просвирва първият избран запис когато
  енкодера е свързан към излъчващ сървър.
* Control+F11: Toggles background monitoring of the selected encoder.
* F12: Opens a dialog to enter custom label for the selected encoder or
  stream.
* Control+F12: opens a dialog to select the encoder you have deleted (to
  realign stream labels and encoder settings).
* Control+NVDA+0 or Alt+NVDA+0: Opens encoder settings dialog to configure
  options such as stream label.

In addition, column review commands are available, including:

* Control+NVDA+1: Encoder position.
* Control+NVDA+2: stream label.
* Control+NVDA+3 from SAM Encoder: Encoder format.
* Control+NVDA+3 from SPL Encoder: Encoder settings.
* Control+NvDA+4 from SAM Encoder: Encoder connection status.
* Control+NVDA+4 from SPL Encoder: Transfer rate or connection status.
* Control+NVDA+5 from SAM Encoder: Connection status description.

## Помощен слой на SPL

This layer command set allows you to obtain various status on SPL Studio,
such as whether a track is playing, total duration of all tracks for the
hour and so on. From any SPL Studio window, press the SPL Assistant layer
command, then press one of the keys from the list below (one or more
commands are exclusive to playlist viewer). You can also configure NvDA to
emulate commands from other screen readers.

The available commands are:

* A: Автоматизация.
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
* H: продължителност на записите от текущия час.
* Shift+H: Remaining track duration for the hour slot.
* I (L in JAWS or Window-Eyes layouts): Listener count.
* K: Move to the marked track (playlist viewer only).
* Control+K: Set the current track as the place marker track (playlist
  viewer only).
* L (Shift+L in JAWS and Window-Eyes layouts): Line in.
* M: микрофон.
* N: заглавието на следващия запис на опашката.
* P: състояние на възпроизвеждането (активно или спряно).
* Shift+P: Pitch of the current track.
* R (Shift+E in JAWS and Window-Eyes layouts): Record to file
  enabled/disabled.
* Shift+R: Наблюдаване на напредъка при сканирането на библиотеката.
* S: Записът ще се възпроизведе в (планирано).
* Shift+S: Time until selected track will play.
* T: Включване/изключване на Cart режима на редактиране.
* U: Изминало време в Studio.
* Control+Shift+U: Check for add-on updates.
* W: Време и температура, ако са конфигурирани.
* Y: Playlist modified status.
* 1 through 0 (6 for Studio 5.0x): Announce column content for a specified
  column.
* F9: Mark current track for track time analysis (playlist viewer only).
* F10: Perform track time analysis (playlist viewer only).
* F12: Switch between current and a predefined profile.
* F1: Layer help.
* Shift+F1: Opens online user guide.

## Контролер на SPL

Контролерът на SPL е набор от команди за слоя, които може да използвате, за
да управлявате SPL Studio от всякъде. Натиснете командата за слоя на
контролера за SPL и NVDA ще съобщи, "Контролер на SPL." Натиснете клавиш,
отговарящ на някоя от командите по-долу, за да управлявате някоя от многото
настройки, например заглушаване или активиране на микрофона или просвирване
на следващия запис.

Наличните команди на контролера на SPL са:

* Натиснете P, за да просвирите следващия маркиран запис.
* Натиснете U, за да поставите на пауза текущия запис или да възобновите
  възпроизвеждането.
* Натиснете S, за да спрете записа със затихване, или натиснете T, за да
  спрете записа незабавно.
* Натиснете M или Shift+M за да включите или съответно изключите микрофона,
  или натиснете N за да задействате микрофона без засилване.
* Натиснете A, за да разрешите автоматизацията или Shift+A, за да я
  забраните.
* Натиснете L, за да разрешите линейния вход или Shift+L, за да го
  забраните.
* Press R to hear remaining time for the currently playing track.
* Натиснете Shift+R за да получите доклад за напредъка по сканирането на
  библиотеката.
* Press E to get count and labels for encoders being monitored.
* Press I to obtain listener count.
* Натиснете F1 за да изведете помощен прозорец, който изброява наличните
  команди.

## Track alarms

By default, NvDA will play a beep if five seconds are left in the track
(outro) and/or intro. To configure this value as well as to enable or
disable them, press Control+NVDA+2 or Alt+NVDA+2 to open end of track and
song ramp dialogs, respectively. In addition, use Studio add-on settings
dialog to configure if you'll hear a beep, a message or both when alarms are
turned on.

## Предупреждение за микрофона

Можете да укажете на NVDA да възпроизвежда звук, когато микрофонът е бил
активен от известно време. Натиснете Control+NVDA+4 за да конфигурирате
времето за предупреждението в секунди (0 го забранява).

## Търсене на записи

Ако желаете бързо да намерите запис от изпълнител или по името на записа, от
списъка за изпълнение, натиснете Control+NVDA+F. Въведете името на
изпълнителя или името на песента. NVDA ще ви позиционира върху записа Ако е
намерен или ще изведе грешка, ако не може да се намери записа, който
търсите. За да намерите предходно търсен запис или изпълнител, натиснете
NVDA+F3 или NVDA+Shift+F3, за да търсите съответно напред или назад.

Забележка: Търсенето на записи взема предвид малките и главните букви.

## Разглеждане на джингъли

В зависимост от изданието, SPL Studio позволява да бъдат определени до 96
джингъли за използване по време на предаване. NVDA ви позволява да чуете кой
джингъл е назначен за коя от тези команди.

За да изследвате джингълите, от SPL Studio, натиснете
Control+NVDA+3. Натискането на командата за джингъла ви казва кой е
асоциирания джингъл. Двукратно натискане просвирва джингъла. Натиснете
Control+NvDA+3 за да излезете от този режим. За повече информация се
обърнете към ръководството на добавката.

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

By pressing SPL Assistant, 1 through 0 (6 for Studio 5.01 and earlier), you
can obtain contents of specific columns. By default, these are artist,
title, duration, intro, category and filename (Studio 5.10 adds year, album,
genre and time scheduled). You can configure which columns will be explored
via columns explorer dialog found in add-on settings dialog.

## Configuration dialog

From studio window, you can press Control+NVDA+0 or Alt+NVDA+0 to open the
add-on configuration dialog. Alternatively, go to NVDA's preferences menu
and select SPL Studio Settings item. This dialog is also used to manage
broadcast profiles.

## SPL touch mode

If you are using Studio on a touchscreen computer running Windows 8 or later
and have NVDA 2012.3 or later installed, you can perform some Studio
commands from the touchscreen. First use three finger tap to switch to SPL
mode, then use the touch commands listed above to perform commands.

## Version 7.4/16.08

Version 7.4 is also known as 16.08 following the year.month version number
for stable releases. 7.4 is the last version in the 7.x series and the
entire major.minor version numbers.

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
* Обновени преводи.

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
* Обновени преводи.

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
* Обновени преводи.

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
* Обновени преводи.

## Changes for 5.3

* The fix for SAM Encoder (not playing the next track if a track is playing
  and when the encoder connects) is now available for SPL Encoder users.
* NVDA no longer plays errors or does not do anything when SPL Assistant, F1
  (Assistant help dialog) is pressed.

## Changes for 5.2

* NVDA will no longer allow both settings and alarm dialogs to be opened. A
  warning will be shown asking you to close the previously opened dialog
  before opening another dialog.
* When monitoring one or more encoders, pressing SPL Controller, E will now
  announce encoder count, encoder ID and stream label(s) if any.
* NVDA supports connect/disconnect all commands (Control+F9/Control+F10) in
  SAM encoders.
* NVDA will no longer play the next track if an encoder connects while
  Studio is playing a track and Studio is told to play tracks when an
  encoder is connected.
* Обновени преводи.

## Changes for 5.1

* It is now possible to review individual columns in Track Tool via Track
  Dial (toggle key unassigned). Note that Studio must be active before using
  this mode.
* Added a check box in Studio add-on settings dialog to toggle announcement
  of name of the currently playing cart.
* Toggling microphone on and off via SPL Controller no longer causes error
  tones to be played or toggle sound to not be played.
* If a custom command is assigned for an SPL Assistant layer command and
  this command is pressed right after entering SPL Assistant, NvDA will now
  promptly exit SPL Assistant.

## Changes for 5.0

* A dedicated settings dialog for SPL add-on has been added, accessible from
  NVDA's preferences menu or by pressing Control+NVDA+0 from SPL window.
* Added ability to reset all settings to defaults via configuration dialog.
* If some of the settings have errors, only the affected settings will be
  reset to factory defaults.
* Added a dedicated SPL touchscreen mode and touch commands to perform
  various Studio commands.
* Changes to SPL Assistant layer include addition of layer help command (F1)
  and removal of commands to toggle listener count (Shift+I) and scheduled
  time announcement (Shift+S). You can configure these settings in add-on
  settings dialog.
* Renamed "toggle announcement" to "status announcement" as beeps are used
  for announcing other status information such as completion of library
  scans.
* Status announcement setting is now retained across sessions. Previously
  you had to configure this setting manually when Studio starts.
* You can now use Track Dial feature to review columns in a track entry in
  Studio's main playlist viewer (to toggle this feature, press the command
  you assigned for this feature).
* You can now assign custom commands to hear temperature information or to
  announce title for the upcoming track if scheduled.
* Added a checkbox in end of track and song intro alarm dialogs to enable or
  disable these alarms (check to enable). These can also be "configured"
  from add-on settings.
* Fixed an issue where pressing alarm dialog or track finder commands while
  another alarm or find dialog is opened would cause another instance of the
  same dialog to appear. NVDA will pop up a message asking you to close the
  previously opened dialog first.
* Cart explorer changes and fixes, including exploring wrong cart banks when
  user is not focused on playlist viewer. Cart explorer will now check to
  make sure that you are in playlist viewer.
* Added ability to use SPL Controller layer command to invoke SPL Assistant
  (experimental; consult the add-on guide on how to enable this).
* In encoder windows, NVDA's time and date announcement command (NVDA+F12 by
  default) will announce time including seconds.
* You can now monitor individual encoders for connection status and for
  other messages by pressing Control+F11 while the encoder you wish to
  monitor is focused (works better when using SAM encoders).
* Added a command in SPL Controller layer to announce status of encoders
  being monitored (E).
* A workaround is now available to fix an issue where NvDA was announcing
  stream labels for the wrong encoders, especially after deleting an encoder
  (to realign stream labels, press Control+F12, then select the position of
  the encoder you have removed).

## Промени във версии 4.4/3.9

* Функцията за сканиране на библиотеката вече работи в Studio 5.10 (изисква
  най-новата компилация на Studio 5.10).

## Промени във версии 4.3/3.8

* При преминаване към друга част на Studio, като например прозореца за
  вмъкване на записи, докато е активен прегледът на джингъли, NVDA няма да
  съобщава известията за джингълите при натискане на клавишите за джингълите
  (например, при намиране на запис в прозореца за вмъкване на записи).
* Нови клавишни команди за Помощника на SPL, включително за превключване на
  обявяването на планираното време и броя на слушателите (съответно Shift+S
  и Shift+I, които не се запазват между сесиите).
* При изход от Studio при отворени диалогови прозорци за аларми, NVDA ще
  засече, че Studio е била затворена и няма да запише новите променени
  стойности за алармите.
* Обновени преводи.

## Промени във версии 4.2/3.7

* NVDA вече няма да забравя да запазва новите и променените етикети за
  енкодера когато потребителят излиза от системата или рестартира компютъра.
* Когато конфигурацията на добавката се повреди при стартиране на NVDA,
  екранният четец ще възстанови конфигурацията по подразбиране и ще изведе
  съобщение, с което ще информира потребителя за този факт.
* Във версия 3.7 на добавката бе отстранен проблем с фокуса забелязан при
  изтриване на записи в Studio 4.33 (същата корекция е налична за
  потребителите на Studio 5.0 x във версия 4.1 на добавката).

## Промени във версия 4.1

* В Studio 5.0 x, изтриване на запис от основния списъчен изглед вече няма
  да предизвиква NVDA да прочита записа под последно фокусирания запис
  (по-забележимо ако е бил изтрит предпоследният запис, в който случай NVDA
  съобщаваше "непознат").
* Поправени са няколко проблема със сканирането на библиотеката в Studio
  5.10, включително съобщаването на общият брой на елементите в библиотеката
  при обхождане с табулатора в диалоговия прозорец за вмъкване на записи и
  съобщаване на "извършва се сканиране" при опит за наблюдаване на
  сканирането на библиотеката чрез SPL помощника.
* Когато се използва брайлов дисплей със Studio 5.10 и ако даден запис е
  отметнат, натискането на интервал за отмятане на запис по-долу, вече не
  предизвиква брайловия дисплей да не отразява новото състояние на елемента.

## Промени във версии 4.0/3.6

Версия 4.0 поддържа SPL Studio 5.00 и по-нови, а 3.x е предназначена да
предоставят някои нови функции от 4.0 за потребителите използващи по-стари
версии на Studio.

* Нови клавиши за SPL Помощника, включително за планираното време за записа
  (S), оставащото времетраене на списъка за изпълнение (D) и температурата
  (W, ако е конфигурирано). В допълнение, за Studio 5.x е добавено промяна
  на списъка за изпълнение (Y) и височина на записа (Shift+P).
* Нови команди за контролния панел на SPL, включително за напредъка на
  сканиранията на библиотеката (Shift+R) и за разрешаването на микрофона без
  засилване (N). Също така, натискането на F1 извежда диалогов прозорец с
  наличните команди.
* При разрешаването или забраняването на микрофона през контролния панел на
  SPL, ще се възпроизвежда сигнал, посочващ дали микрофонът е включен или
  изключен.
* Настройки като времето за края на записа се записват в специален
  конфигурационен файл във вашата потребителска конфигурационна директория и
  се запазват при обновяване на добавката (версия 4.0 и по-нови).
* Добавена е команда (Alt+NVDA+2) за задаване на време за предупреждение за
  въведение в мелодията (между 1 и 9 секунди).
* В диалоговите прозорци за предупреждението за края на записа и за
  въведението можете да използвате стрелките за нагоре и надолу за да
  промените настройките за предупреждението. Ако бъде въведена неправилна
  стойност, стойността за предупреждението се задава на максималната
  стойност.
* Добавена е команда (Control+NVDA+4) за задаване на време след което NVDA
  ще възпроизвежда звук когато микрофонът е бил активен от известно време.
* Добавена е възможност за съобщаване на времето в часове, минути и секунди
  (командата не е назначена).
* Вече е възможно да се следи сканирането на библиотеката от диалоговия
  прозорец за вмъкване на записи или от което и да е друго място и
  специалната команда (Alt+NVDA+R) за превключване на опциите за
  наблюдаването на сканирането на библиотеката.
* Поддръжка за Инструмента за записа (Track Tool), включително за
  възпроизвеждане на сигнал, ако даден запис има зададено въведение и
  команди за съобщаване на информация за записа, като продължителност и
  позицията на маркера.
* Поддръжка за StationPlaylist Encoder (Studio 5.00 и по-нови),
  предоставяйки същото ниво на поддръжка, като това в SAM Encoder.
* В прозорците на енкодера, NVDA вече не възпроизвежда сигнала си за грешка,
  когато на NVDA е указано да премине към Studio при свързване към излъчващ
  сървър докато прозорецът на Studio е намален.
* Вече няма грешки след изтриването на поток със зададен към него етикет за
  потока.
* Вече е възможно да се наблюдават въведението и края на записа чрез брайл с
  помощта на опциите за брайловия таймер (Control+Shift+X).
* Поправен проблем, при който при опит за превключване към прозореца на
  Studio, след като всички прозорци са били намалени, предизвиква появата на
  нещо друго.
* При използване на Studio 5.01 и по-стари, NVDA вече няма да съобщава по
  няколко пъти дадена информация за състоянието, като например планираното
  време.

## Промени във версия 3.5

* Когато NVDA бъде стартиран или рестартиран докато фокусът е върху
  прозореца с основния списък за изпълнение на Studio 5.10, NVDA няма да
  възпроизвежда звуци при грешка и/или да съобщава следващата и предишната
  песни, когато се преглеждат песните чрез стрелките.
* Отстранен е проблем, възникващ при опит да се получат оставащото и
  изминалото време за песен в по-нови компилации на Studio 5.10.
* Обновени преводи.

## Промени във версия 3.4

* В разглеждането на джингъли, джингълите включващи клавиша Control (като
  Ctrl+F1) сега се обработват коректно.
* Обновени преводи.

## Промени във версия 3.3

* При свързване към излъчващ сървър с използване на SAM encoder, вече не се
  налага да останете в прозореца на енкодера докато връзката бъде
  осъществена.
* Отстранен е проблем, при който командите за енкодера (например за
  етикетиране на потока) преставаха да работят при превключване към
  прозореца на SAM от други програми.

## Промени във версия 3.2

* Добавена е команда в контролера на SPL за докладване на оставащо време за
  текущо просвирвания запис (R).
* В прозореца на SAM encoder, съобщението в помощен режим за командата
  Shift+F11 беше поправено.
* В прегледа на джингъли, ако се използва Studio Standard, NVDA ще ви
  уведоми, че командите за номер на ред са недостъпни за назначенията на
  джингъли.
* В Studio 5.10, търсачката за записи вече не просвирва сигнали за грешка
  при търсене в записите.
* Нови и обновени преводи.

## Промени във версия 3.1

* В прозореца на SAM Encoder беше добавена команда (Shift+F11) за указване
  на Studio да просвири първият запис при свързване.
* Отстранени са множество грешки при свързване към сървър със SAM Encoder,
  включително невъзможността за изпълнение на командите на NVDA, пропуска за
  съобщаване на успешно свързване и сигнали за грешка вместо за успешно
  свързване.

## Промени във версия 3.0

* Добавен е преглед на джингъли, където може да изследвате назначенията на
  джингълите (до 96 джингъла могат да бъдат назначени).
* Добавени са нови команди, включително време на излъчване (NVDA+Shift+F12)
  и брой на слушателите (i) и заглавие на следващ запис (n) в помощника на
  SPL.
* Съобщенията за превключване на настройките като автоматизацията вече се
  изобразяват на брайл без значение от настройката за известяване на
  превключването.
* NVDA ще ви съобщи когато се опитва да превключи към SPL от други програми,
  но в същото време прозореца на StationPlaylist е минимизиран в системния
  жлеб (областта за уведомяване).
* Вече не се чуват сигнали за грешка когато съобщаването на превключванията
  е зададено на бибипкане и се изговарят съобщения за състоянието, различни
  от включено и превключване (например: просвирване на джингъли).
* Вече не се чуват сигнали за грешка когато се опитваме да получим
  информация като оставащо време докато друг прозорец на Studio различен от
  списъка със записи (например прозореца за настройка) е на фокус. Ако
  нужната информация не е намерена, NVDA ще ви съобщи този факт.
* Вече е възможно да търсите запис по име на изпълнител. Преди можеше да се
  извърши търсене само по име на запис.
* Поддръжка за SAM Encoder, включително възможност за етикетиране на
  енкодера и команда за превключване към Studio когато избраният енкодер е
  свързан.
* Помощ за добавката е налична от мениджъра на добавки.

## Промени във версия 2.1

* Отстранен е проблем, при който беше невъзможно да се получи информация за
  състоянието, например това на автоматизацията, когато SPL 5.x се стартира
  за първи път след като NVDA вече е бил стартиран.

## Промени във версия 2.0

* Някои глобални и локални клавишни комбинации са премахнати, така че да
  можете да зададете команда по избор от прозореца за жестове на въвеждане
  (версия 2.0 на добавката изисква NVDA 2013.3 или по-нова).
* Добавени са още команди за SPL помощника, като например за състоянието на
  режима за редактиране cart.
* Сега можете да преминете към SPL Studio дори ако всички прозорци са
  намалени (може да не работи в някои случаи).
* Разширен е диапазона на алармата за край на записа до 59 секунди.
* Вече можете да търсите за даден запис в списъка за изпълнение
  (Control+NVDA+F за търсене, NVDA+F3 или NVDA+Shift+F3 за търсене съответно
  напред и назад).
* NVDA вече съобщава правилните имена на Разгъващите се списъци (например
  диалоговия прозорец с опциите и екраните за първоначалната настройка на
  SPL).
* Отстранен е проблем, при който NVDA съобщаваше грешна информация при опит
  за получаване на оставащото време за запис в SPL Studio 5.

## Промени във версия 1.2

* Когато използвате Station Playlist 4.x под Windows 8/8.1, отново е
  възможно да получите информация за изминало и оставащо време за текущия
  запис.
* Обновени преводи.

## Промени във версия 1.1

* Добавена е команда (Control+NvDA+2) за задаване на време за
  предупреждението за край на записа.
* Отстранен е проблем, при който имената на определени полета за писане не
  бяха съобщавани (например някои полета за писане в диалога за настройка на
  програмата).
* Добавени са множество преводи.


## Промени във версия 1.0

* Първоначално издание

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=spl

[2]: http://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: https://bitbucket.org/nvdaaddonteam/stationplaylist/wiki/SPLAddonGuide

