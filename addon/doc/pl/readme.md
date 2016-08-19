# StationPlaylist Studio #

* Autorzy: Geoff Shang, Joseph Lee i inni
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]

This add-on package provides improved usage of StationPlaylist Studio, as
well as providing utilities to control the Studio from anywhere.

Aby uzyskać więcej informacji o dodatku, przeczytaj [Podręcznik][3].

IMPORTANT: This add-on requires NVDA 2015.3 or later and StationPlaylist
Studio 5.00 or later. If you have installed NVDA 2016.1 or later on Windows
8 and later, disable audio ducking mode.

## Skróty klawiszowe

* Alt+Shift+T w oknie studia: wypowiedz pozostały czas aktualnie odtwarzanej
  ścieżki.
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
* Control+NVDA+3 w oknie studia: przełącza eksplorator koszyka umożliwiający
  naukę przypisań koszyka.
* Control+NVDA+4 w oknie studia: otwiera ustawienie alarmu mikrofonu.
* Control+NVDA+f w oknie studia: otwiera okno wyszukiwania ścieżki po tytule
  lub wykonawcy. Naciśnij NvDA+F3 aby powtórzyć wyszukiwanie w przód, albo
  NVDA+Shift+F3 aby powtórzyć wstecz.
* Alt+NVDA+R w oknie studia: przełącza między różnymi ustawieniami
  oznajmiania skanowania biblioteki.
* Control+Shift+X w oknie studia: przełącza ustawienia timera brajlowskiego.
* Control+Alt+right/left arrow (while focused on a track): Announce
  next/previous track column.
* Control+NVDA+0 or Alt+NVDA+0 from Studio window: Opens the Studio add-on
  configuration dialog.
* Control+NVDA+- (hyphen) from Studio window: Send feedback to add-on
  developer using the default email client.

## Nieprzypisane polecenia

Poniższe polecenia domyślnie nie są przypisane; jeśli chcesz je przypisać,
użyj okna zdarzeń wejścia, aby dodać własne polecenia.

* przejście do okna studia SPL z innego programu.
* Warstwa kontrolera SPL.
* Warstwa asystenta SPL ze studia SPL.
* Oznajmia czas z uwzględnieniem sekund ze studia SPL.
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

## Dodatkowe polecenia podczas używania enkodera Sam lub SPL

Następujące polecenia są dostępne podczas używania enkodera Sam lub SPL:

* F9: podłącz do serwera strumieniowania.
* F10(tylko enkoder SAM): rozłącz z serwerem strumieniowania.
* Control+F9/Control+F10 (SAM encoder only): Connect or disconnect all
  encoders, respectivley.
* F11: przełącza czy NVDA będzie przechodzić do okna studia dla wybranego
  enkodera jeśli podłączony.
* Shift+F11: przełącza czy Studio odtworzy pierwszą zaznaczoną ścieżkę, gdy
  enkoder jest połączony do serwera strumieniowania.
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

## Warstwa asystenta SPL 

This layer command set allows you to obtain various status on SPL Studio,
such as whether a track is playing, total duration of all tracks for the
hour and so on. From any SPL Studio window, press the SPL Assistant layer
command, then press one of the keys from the list below (one or more
commands are exclusive to playlist viewer). You can also configure NvDA to
emulate commands from other screen readers.

The available commands are:

* A: automatyzacja.
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
* H: czas trwania muzyki dla aktualnego slotu godzinowego.
* Shift+H: Remaining track duration for the hour slot.
* I (L in JAWS or Window-Eyes layouts): Listener count.
* K: Move to the marked track (playlist viewer only).
* Control+K: Set the current track as the place marker track (playlist
  viewer only).
* L (Shift+L in JAWS and Window-Eyes layouts): Line in.
* M: mikrofon.
* N: tytuł następnej zaplanowanej ścieżki.
* P: status odtwarzania (odtwarzanie lub wstrzymane).
* Shift+P: Pitch of the current track.
* R (Shift+E in JAWS and Window-Eyes layouts): Record to file
  enabled/disabled.
* Shift+R: monitor trwającego skanowania biblioteki.
* S: ścieżka rozpocznie się za (zaplanowane).
* Shift+S: Time until selected track will play.
* T: tryb edycji karty włączony / wyłączony.
* U: czas pracy studia.
* Control+Shift+U: Check for add-on updates.
* W: pogoda i temperatura jeśli skonfigurowane.
* Y: Playlist modified status.
* 1 through 0 (6 for Studio 5.0x): Announce column content for a specified
  column.
* F9: Mark current track for track time analysis (playlist viewer only).
* F10: Perform track time analysis (playlist viewer only).
* F12: Switch between current and a predefined profile.
* F1: Layer help.
* Shift+F1: Opens online user guide.

## Kontroler SPL 

Kontroler SPL jest zestawem komend których możesz użyć, aby kontrolować SPL
Studio z każdego miejsca. Naciśnij klawisz przypisany do polecenia
kontrolera SPL, a NVDA powie , "Kontroler SPL." naciśnij inną komendę, aby
kontrolować różne ustawienia studia takie jak mikrofon włączony/wyłączony,
albo odtworzenie następnej ścieżki.

Dostępne komendy kontrolera SPL to:

* Naciśnij P aby odtworzyć następną zaznaczoną ścieżkę.
* Naciśnij U aby zapauzować lub wyłączyć pauzę odtwarzania.
* Naciśnij S aby zatrzymać ścieżkę z wybrzmieniem, albo aby zatrzymać
  ścieżkę natychmiast, naciśnij T.
* Naciśnij odpowiednio M lub Shift+M aby włączyć lub wyłączyć mikrofon, albo
  naciśnij N włączyć mikrofon bez wyciszania.
* Naciśnij A aby włączyć automatyzację, albo Shift+A aby ją wyłączyć.
* Naciśnij L aby włączyć wejście liniowe albo Shift+L aby je wyłączyć.
* Press R to hear remaining time for the currently playing track.
* Naciśnij Shift+R aby uzyskać informację o postępie skanowania biblioteki.
* Press E to get count and labels for encoders being monitored.
* Press I to obtain listener count.
* Naciśnij F1 aby wyświetlić pomoc, zawierającą listę wszystkich dostępnych
  poleceń.

## Track alarms

By default, NvDA will play a beep if five seconds are left in the track
(outro) and/or intro. To configure this value as well as to enable or
disable them, press Control+NVDA+2 or Alt+NVDA+2 to open end of track and
song ramp dialogs, respectively. In addition, use Studio add-on settings
dialog to configure if you'll hear a beep, a message or both when alarms are
turned on.

## Alarm mikrofonu

Możesz poprosić NVDA o odtworzenie dźwięku, gdy mikrofon był aktywny przez
chwilę. Naciśnij Control+NVDA+4 by skonfigurować czas alarmu w sekundach (0
wyłącza).

## Wyszukiwanie ścieżek

Jeśli chcesz szybko znaleźć piosenkę po tytule lub wykonawcy, na liście
ścieżek, naciśnij Control+NVDA+F. Wpisz nazwę wykonawcy lub tytuł
piosenki. NVDA umieści cię na znalezionej ścieżce, albo wyświetli błąd,
jeśli nie zostanie znaleziona. Aby powtórzyć wcześniejsze wyszukiwanie,
naciśnij NVDA+F3 aby wyszukać w przód, albo NVDA+Shift+F3 aby wyszukać
wstecz.

Uwaga: poszukiwanie ścieżek uwzględnia wielkość liter.

## eksplorator koszyka

Zależnie od wydania, SPL Studio umożliwia posiadanie do 96 koszyków
przypisanych do odtwarzania. NVDA może odczytać, który koszyk lub dżingiel
jest przypisany do tych poleceń.

Aby poznać przypisania koszyków w oknie studia naciśnij
Control+NVDA+3. Naciśnięcie polecenia koszyka jednokrotnie, wypowie jaki
dżingiel jest przypisany do polecenia. Dwukrotne naciśnięcie odtworzy
dżingiel. Naciśnij Control+NvDA+3 aby opuścić eksplorator koszyka. Zajrzyj
do podręcznika dodatku, aby uzyskać więcej informacji o eksploratorze.

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
* Zaktualizowano tłumaczenia.

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
* Zaktualizowano tłumaczenia.

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
* Zaktualizowano tłumaczenia.

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
* Zaktualizowano tłumaczenia.

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
* Zaktualizowano tłumaczenia.

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

## Zmiany dla wersji 4.4/3.9

* Funkcja skanowania biblioteki działa teraz w Studio 5.10 (wymaga
  najnowszej kompilacji Studio 5.10).

## Zmiany dla wersji 4.3/3.8

* Przy przełączeniu do innej części Studia takiej jak wstawianie ścieżek
  podczas aktywnej eksploracji koszyka, NVDA nie będzie dłużej oznajmiać
  powiadomień koszyka, gdy odpowiednie klawisze zostały naciśnięte
  (np. lokalizowanie ścieżki z okna wstawiania ścieżek).
* Nowe klawisze asystenta SPL, włączając w to przełączanie oznajmiania
  zaplanowanego czasu i liczby słuchaczy(odpowiednio Shift+S i Shift+I, nie
  zapisywane między sesjami).
* Po wyjściu ze Studia przy otwartych oknach ustawiania różnych alarmów,
  NVDA wykrywa, że Studio zostało zamknięte i nie zapisze
  nowozmodyfikowanych wartości alarmów.
* Zaktualizowano tłumaczenia.

## Zmiany dla wersji 4.2/3.7

* NVDA nie gubi nowych i zmienionych etykiet enkodera, gdy użytkownik
  wyloguje się, albo zrestartuje komputer.
* Jeśli konfiguracja dodatku okaże się uszkodzona przy starcie NVDA,
  przywrócona zostanie konfiguracja domyślna, oraz pojawi się informacja o
  tym fakcie.
* W dodatku 3.7, naprawiono problem punktu uwagi podczas kasowania ścieżek w
  Studio 4.33 (ta sama poprawka dostępna dla użytkowników Studio 5.0x w
  wersji dodatku 4.1).

## Zmiany dla wersji 4.1

* W Studio 5.0x, kasowanie ścieżki z głównej przeglądarki listy odtwarzania
  nie powoduje dłużej, że NVDA zgłasza ścieżkę pod nowopodświetloną
  (zauważalne bardziej, gdy usunięta ścieżka druga od końca, co powodowało,
  że NVDA wypowiada "nieznane").
* Poprawiono kilka błędów skanowania biblioteki w Studio 5.10, w tym
  oznajmianie łącznej liczby elementów w bibliotece podczas przechodzenia
  tabulatorem między elementami w oknie wstawiania ścieżek i wypowiadanie
  "skanowanie w toku" przy próbie monitorowania skanowania biblioteki w
  asystencie SPL.
* Używając monitora brajlowskiego w Studio 5.10 , gdy ścieżka jest
  zaznaczona, naciśnięcie spacji aby zaznaczyć ścieżkę poniżej, nie powoduje
  od teraz że nowy stan zaznaczenia nie był odzwierciedlany na monitorze.

## Zmiany dla wersji 4.0/3.6

Wersja 4.0 obsługuje SPL Studio 5.00 i nowsze, wersja 3.x dostarcza
niektórych nowych funkcji wersji 4.0 dla użytkowników korzystających z
wcześniejszych wersji Studio.

* Nowe klawisze asystenta SPL, w tym zaplanuj czas dla ścieżki (S),
  pozostały czas listy odtwarzania (D) i temperatura (W jeśli
  skonfigurowana). Ponadto, dla Studio 5.x, dodana modyfikacja listy
  odtwarzania (Y) i wysokość ścieżki (Shift+P).
* Nowe polecenia kontrolera SPL  a w tym postęp skanowania biblioteki
  (Shift+R) i włączanie mikrofonu bez wyciszenia (N). Naciśnięcie F1
  wyświetla okno zawierające dostępne polecenia.
* Przy włączaniu i wyłączaniu mikrofonu przez kontroler SPL, będą odtwarzane
  dźwięki określające stan przełącznika.
* Ustawienia takie jak czas końca ścieżki, są zapisywane w specjalnym pliku
  konfiguracyjnym w folderze konfiguracji użytkownika i są zachowywane
  podczas aktualizacji dodatku (wersja 4.0 i nowsze).
* Dodano polecenie (Alt+NvDA+2) ustawiające alarm intra ścieżki między 1 i 9
  sekund.
* W oknach alarmu końca ścieżki i intra, można użyć klawiszy strzałek by
  zmienić ustawienie alarmu. Jeśli wprowadzona zostanie nieprawidłowa
  wartość, czas alarmu jest ustawiany na maksimum.
* Dodane polecenie (Control+NVDA+4) ustawienia czasu, po którym NVDA
  odtworzy dźwięk jeśli mikrofon był aktywny.
* Dodana funkcja oznajmiania czasu w godzinach, minutach i sekundach
  (polecenie nieprzypisane).
* Możliwe jest teraz śledzenie skanowania biblioteki w oknie wstawiania
  ścieżek lub gdziekolwiek, oraz dedykowane polecenie (Alt+NVDA+R) do
  przełączania opcji oznajmiania skanowania biblioteki.
* Obsługa narzędzia ścieżki, a w tym odtwarzanie dźwięku jeśli ścieżka ma
  zdefiniowane intro oraz polecenia oznajmiania informacji o ścieżce, takich
  jak czas trwania i pozycja cue.
* Obsługa enkodera StationPlaylist (Studio 5.00 i nowsze), dostarczająca ten
  sam poziom obsługi co obsługa enkodera SAM.
* W oknach enkodera, NvDA nie odtwarza dźwięku błędów, gdy NVDA ma się
  przełączyć do studia po podłączeniu do serwera strumieniowania, a okno
  studia jest zminimalizowane.
* Błędy nie pojawiają się po usunięciu strumienia z ustawioną etykietą.
* Możliwe jest monitorowanie czasu intra i końca ścieżki w brajlu przy
  użyciu opcji timera brajlowskiego (Control+Shift+X).
* Poprawiono błąd, że próba przejścia do okna Studia z innego programu, gdy
  wszystkie okna były zminimalizowane, powodowała pojawienie się czegoś
  innego.
* W Studio 5.01 i starszych, NVDA nie będzie oznajmiać wielokrotnie
  niektórych informacji statusu takich jak zaplanowany czas.

## Zmiany dla wersji 3.5

* Jeżeli NVDA jest uruchomiony lub zrestartowany, podczas gdy główne okno
  playlisty Studio 5.10 posiada punkt uwagi, NVDA nie spowoduje to
  odgrywania dźwięków błędu NVDA, albo braku informacji o następnej i
  poprzedniej ścieżce przy przechodzeniu strzałkami po ścieżkach.
* Poprawiony błąd pobierania czasu który pozostał i czasu, który upłynął dla
  ścieżki w późniejszych kompilacjach Studio 5.10.
* Zaktualizowano tłumaczenia.

## Zmiany dla wersji 3.4

* W eksploratorze koszyka, koszyki z klawiszem Control (takie jak Ctrl+F1)
  są teraz prawidłowo obsługiwane.
* Zaktualizowano tłumaczenia.

## Zmiany dla wersji 3.3

* Przy połączeniu z serwerem strumienia z użyciem enkodera SAM, nie trzeba
  pozostawać w oknie enkodera do chwili ustanowienia połączenia.
* Poprawiono problem, że komendy enkodera (np. nazywanie strumieni) nie
  działały po przełączeniu do okna SAM z innych programów.

## Zmiany dla wersji 3.2

* Dodane polecenie w kontrolerze SPL  wypowiadania pozostałego czasu
  aktualnie odtwarzanej ścieżki (R).
* W oknie enkodera SAM, wiadomość pomocy klawiatury dla Shift+F11 została
  poprawiona
* W eksploratorze koszyka, jeśli używane jest Studio Standard, NVDA
  ostrzeże, że polecenia numerów wierszy są niedostępne dla przypisywania
  koszyków.
* W Studio 5.10, poszukiwanie ścieżek nie generuje dźwięków błędu, podczas
  przeszukiwania.
* Nowe i zaktualizowane tłumaczenia.

## Zmiany dla wersji 3.1

* W oknie enkodera SAM, dodana komenda (Shift+F11) nakazująca studiu odegrać
  pierwszą ścieżkę, gdy połączone.
* Naprawiono liczne błędy podczas połączenia z serwerem w enkoderze SAM,
  włączając niemożność wykonania poleceń NVDA, NVDA nie informujący o
  nawiązaniu połączenia i odtwarzanie dźwięków błędów zamiast dźwięków
  połączenia.

## Zmiany dla wersji 3.0

* Dodany eksplorator koszyka umożliwiający nauczenie się przypisań koszyków
  (do 96 koszyków może być przypisanych).
* Dodane nowe polecenia asystenta SPL w tym czas nadawcy (NVDA+Shift+F12) i
  ilość słuchaczy (i) oraz tytuł następnej ścieżki (n).
* Przełączalne wiadomości takie jak automatyzacja, są teraz wyświetlane w
  brajlu niezależnie od ustawienia przełącznika oznajmiania.
* Gdy okno StationPlaylist jest zminimalizowane do szuflady systemu (obszaru
  powiadomień), NVDA oznajmi ten stan podczas próby przełączenia się do SPL
  z innych programów.
* Dźwięki błędów nie są słyszalne, gdy przełączanie oznajmiania jest
  ustawione na dźwięki i oznajmiane są wiadomości statusu inne niż
  przełącznik włączony/wyłączony. (np.: odtwarzanie koszyków).
* Dźwięki błędów nie są słyszalne, podczas próby uzyskania informacji takich
  jak pozostały czas, jeśli punkt uwagi znajduje się w oknie Studia innym
  niż lista ścieżek (np. w oknie opcji). Jeśli potrzebna informacja nie
  zostanie znaleziona, NVDA poinformuje o tym fakcie.
* Można wyszukiwać ścieżek po nazwie artysty. Poprzednio można było szukać
  po tytule ścieżki.
* Wsparcie dla enkodera SAM, w tym możliwość etykietowania enkodera i
  przełącznik przejścia do studia, gdy wybrany enkoder jest podłączony.
* Pomoc dodatku dostępna w managerze dodatków.

## Zmiany dla wersji 2.1

* Poprawiono błąd, że użytkownik nie mógł uzyskać informacji o statusie
  takich jak stan automatyzacji, gdy SPL 5.x był po raz pierwszy uruchomiony
  podczas pracy NVDA.

## Zmiany dla wersji 2.0

* Niektóre globalne lub specyficzne dla aplikacji klawisze skrótów zostały
  usunięte, aby możliwe było przypisanie własnych skrótów z okna zdarzeń
  wejścia (dodatek w wersji 2.0 wymaga NVDA 2013.3 lub nowszej).
* Dodano więcej komend asystenta SPL takich jak tryb edycji karty, status.
* Możesz teraz przełączyć się do studia SPL nawet przy zminimalizowanych
  wszystkich oknach (może nie działać w niektórych przypadkach).
* Zakres alarmu końca ścieżki rozszerzony do 59 sekund.
* Możesz wyszukiwać ścieżki w liście odtwarzania (Control+NVDA+F aby
  znaleźć, NvDA+F3 lub NvDA+Shift+F3 by powtórzyć wyszukiwanie odpowiednio w
  przód lub wstecz).
* Prawidłowe nazwy list rozwijanych są teraz odczytywane przez NVDA
  (np. okna opcji i wstępnej konfiguracji SPL).
* Poprawiony błąd, że NVDA ogłaszał nieprawidłową informację zamiast
  pozostałego czasu ścieżki w SPL Studio 5.

## Zmiany dla wersji 1.2

* Gdy Station Playlist 4.x jest zainstalowane na niektórych komputerach z
  Windows 8/8.1, możliwe jest ponownie uzyskanie informacji o czasie, który
  upłynął i pozostał dla ścieżki.
* Zaktualizowano tłumaczenia.

## Zmiany dla wersji 1.1

* Dodano polecenie (Control+NvDA+2) ustawiające alarm końca ścieżki.
* Poprawiono błąd, że nazwy niektórych pól edycyjnych nie były odczytywane
  (szczególnie pola edycyjne w okienku opcji).
* Dodano różne tłumaczenia.


## Zmiany dla wersji 1.0

* Wstępne wydanie.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=spl

[2]: http://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: https://bitbucket.org/nvdaaddonteam/stationplaylist/wiki/SPLAddonGuide

