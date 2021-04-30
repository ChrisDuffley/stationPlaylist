# StationPlaylist #

* Autori: Geoff Shang, Joseph Lee și alți contributori
* Descărcați [versiunea stabilă][1]
* Descărcați [versiunea în dezvoltare][2]
* NVDA compatibility: 2020.3 to 2020.4

This add-on package provides improved usage of StationPlaylist Studio and
other StationPlaylist apps, as well as providing utilities to control Studio
from anywhere. Supported apps include Studio, Creator, Track Tool, VT
Recorder, and Streamer, as well as SAM, SPL, and AltaCast encoders.

For more information about the add-on, read the [add-on guide][4].

NOTE IMPORTANTE:

* This add-on requires StationPlaylist suite 5.30 (5.20 for 20.09.x-LTS) or
  later.
* Dacă utilizați Windows 8 sau o versiune ulterioară, pentru cea mai bună
  experiență, dezactivați modul de atenuare audio.
* Starting from 2018, [changelogs for old add-on releases][5] will be found
  on GitHub. This add-on readme will list changes from version 20.09 (2020)
  onwards.
* While Studio is running, you can save, reload saved settings, or reset
  add-on settings to defaults by pressing Control+NVDA+C, Control+NVDA+R
  once, or Control+NVDA+R three times, respectively. This is also applicable
  to encoder settings - you can save and reset (not reload) encoder settings
  if using encoders.

## Scurtături de taste

Most of these will work in Studio only unless otherwise specified.

* Alt+Shift+T din fereastra Studio: anunță timpul scurs pentru piesa care se
  redă în acel moment.
* Control+Alt+T (glisare în jos cu două degete în modul tactil al SPL-ului)
  din fereastra Studio: anunță timpul rămas pentru piesa care se redă în
  acel moment.
* NVDA+Shift+F12 (glisare în sus cu două degete în modul tactil al SPL-ului)
  din fereastra Studio: anunță timpul difuzării, de exemplu 5 minute până la
  începutul orei. Apăsând comanda de două ori, va anunța minutele și
  secundele până la începutul orei.
* Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens
  alarms category in Studio add-on configuration dialog.
* Alt+NVDA+1 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces scheduled time for the loaded playlist.
* Alt+NVDA+2 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces total playlist duration.
* Alt+NVDA+3 din fereastra Studio: activează sau dezactivează exploratorul
  cart pentru învățarea atribuirilor.
* Alt+NVDA+3 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces when the selected track is scheduled to play.
* Alt+NVDA+4 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces rotation and category associated with the loaded playlist.
* Control+NVDA+f from Studio window: Opens a dialog to find a track based on
  artist or song name. Press NVDA+F3 to find forward or NVDA+Shift+F3 to
  find backward.
* Alt + NVDA + R din fereastra Studio: Mergeți prin setările bibliotecii
  pentru a scana anunțul setărilor.
* Control + Shift + X din fereastra Studio: Mergeți prin intermediul
  setărilor cronometrului braille.
* Control+Alt+left/right arrow (while focused on a track in Studio, Creator,
  Remote VT, and Track Tool): Move to previous/next track column.
* Control+Alt+Home/End (while focused on a track in Studio, Creator, Remote
  VT, and Track Tool): Move to first/last track column.
* Control+Alt+up/down arrow (while focused on a track in Studio, Creator,
  Remote VT, and Track Tool): Move to previous/next track and announce
  specific columns.
* Control+NVDA+1 through 0 (while focused on a track in Studio, Creator
  (including Playlist Editor), Remote VT, and Track Tool): Announce column
  content for a specified column (first ten columns by default). Pressing
  this command twice will display column information on a browse mode
  window.
* Control+NVDA+- (hyphen while focused on a track in Studio, Creator, Remote
  VT, and Track Tool): display data for all columns in a track on a browse
  mode window.
* NVDA+V while focused on a track (Studio's playlist viewer only): toggles
  track column announcement between screen order and custom order.
* Alt+NVDA+C while focused on a track (Studio's playlist viewer only):
  announces track comments if any.
* Alt+NVDA+0 din fereastra Studio:Deschide dialogul de configurare al
  add-on-ului.
* Alt+NVDA+P from Studio window: Opens the Studio broadcast profiles dialog.
* Alt+NVDA+F1: Deschide dialogul de bun venit.

## Comenzi neatribuite

The following commands are not assigned by default; if you wish to assign
them, use Input Gestures dialog to add custom commands. To do so, from
Studio window, open NVDA menu, Preferences, then Input Gestures. Expand
StationPlaylist category, then locate unassigned commands from the list
below and select "Add", then type the gesutre you wish to use.

* Comutare la fereastra SPL din orice program.
* Layer SPL controler
* Anunțarea stării Studio, cum ar fi piesa în curs de redare de la alte
  programe.
* Announcing encoder connection status from any program.
* Asistent Layer SPL din SPL Studio.
* Anunță timpul incluzând secundele din SPL Studio.
* Anunțarea temperaturii.
* Anunțarea titlului următoarei piese dacă este programată.
* Anunțarea titlului piesei care se redă în acel moment.
* Marcarea piesei curente pentru începerea analizării duratei melodiei.
* Efectuarea analizării duratei melodiei.
* Ia lista de redare instantanee
* Găsiți text în coloane specifice.
* Găsiți piese cu o durată care se încadrează într-un anumit interval de
  timp, prin interval de căutare.
* Activați și dezactivați rapid metadata emisiei.

## Additional commands when using encoders

The following commands are available when using encoders:

* F9: connect the selected encoder.
* F10 (SAM encoder only): Disconnect the selected encoder.
* Control+F9: Connect all encoders.
* Control+F10 (SAM encoder only): Disconnect all encoders.
* F11: activează sau dezactivează dacă NVDA va comuta la fereastra Studio
  pentru encoderul selectat dacă este conectat.
* Shift+F11: Activează sau dezactivează dacă Studio va reda prima piesă
  selectată atunci când encoderul este conectat la un server stream.
* Control+F11: Activează sau dezactivează monitorizarea fundalului la
  encoderul selectat.
* Control+F12: opens a dialog to select the encoder you have deleted (to
  realign encoder labels and settings).
* Alt+NVDA+0 and F12: Opens encoder settings dialog to configure options
  such as encoder label.

În plus, revizuirea coloanei de comenzi este disponibilă, incluzând:

* Control+NVDA+1: Poziția encoderului.
* Control+NVDA+2: encoder label.
* Control+NVDA+3 de la Encoderul SAM: Format encoder.
* Control+NVDA+3 from SPL and AltaCast Encoder: Encoder settings.
* Control+NVDA+4 from SAM Encoder: Encoder connection status.
* Control+NVDA+4 from SPL and AltaCast Encoder: Transfer rate or connection
  status.
* Control+NVDA+5 de la encoderul SAM: Descrie starea conexiunii.

## Asistent Layer SPL

This layer command set allows you to obtain various status on SPL Studio,
such as whether a track is playing, total duration of all tracks for the
hour and so on. From any SPL Studio window, press the SPL Assistant layer
command, then press one of the keys from the list below (one or more
commands are exclusive to playlist viewer). You can also configure NVDA to
emulate commands from other screen readers.

Comenzile disponibile sunt:

* A: Automatizare.
* C (Shift+C in JAWS layout): Title for the currently playing track.
* C (JAWS layout): Toggle cart explorer (playlist viewer only).
* D (R în aspectul JAWS): durata rămasă pentru lista de redare (dacă un
  mesaj de eroare este dat, deplasați-vă la vizualizatorul listei de redare,
  apoi emiteți această comandă).
* E: Metadata streaming status.
* Shift+1 până la Shift+4, Shift+0: Stare pentru metadata individuală a
  URL-ului emisiei (0 este pentru encoderul DSP).
* F: Găsire piesă (doar vizualizatorul listei de redare).
* H: durata muzicii pentru spațiul orei curente.
* Shift+H: Durata rămasă a piesei pentru spațiul orei.
* I (L in JAWS layout): Listener count.
* K: Deplasare la piesa marcată (doar vizualizatorul listei de redare).
* Control+K: Setează piesa curentă ca o piesă a locului de marcare (doar
  vizualizatorul listei de redare).
* L (Shift+L in JAWS layout): Line in.
* M: Microfon.
* N: Titlul următoarei piese programate.
* P: Starea redării (în redare sau oprit).
* Shift+P: Tonalitatea piesei curente.
* R (Shift+E in JAWS layout): Record to file enabled/disabled.
* Shift+R: Scanarea librăriei monitorului în curs.
* S: Piesa începe (programată).
* Shift+S: Timp până la redarea piesei (piesa începe în).
* T: modul editare/inserare cart activat/dezactivat.
* U: Studio up time.
* W: Vremea și temperatura dacă sunt configurate.
* Y: stare playlist modificat.
* F8: Ia lista de redare instantanee (numărul pieselor, cea mai lungă piesă,
  etc.).
* Shift+F8: Request playlist transcripts in numerous formats.
* F9: Mark current track for start of playlist analysis (playlist viewer
  only).
* F10: Efectuează analizarea timpului piesei )(doar vizualizatorul listei de
  redare).
* F12: Comută între un profil curent și unul predefinit.
* F1: Ajutor layer.
* Shift+F1: Deschide ghidul online al utilizatorului.

## SPL Controller

SPL Controler este un set de comenzi stratificate pe care le puteți utiliza
pentru a controla SPL Studio oriunde. Apăsați comanda stratului SPL
Controller, iar NVDA va spune: "Controller SPL". Apăsați o altă comandă
pentru a controla diferite setări Studio, cum ar fi microfonul pornit /
oprit sau pentru a reda piesa următoare.

Comenzile disponibile SPL Controller sunt:

* P: Play the next selected track.
* U: Pause or unpause playback.
* S: Stop the track with fade out.
* T: Instant stop.
* M: Turn on microphone.
* Shift+M: Turn off microphone.
* A: Turn on automation.
* Shift+A: Turn off automation.
* L: Turn on line-in input.
* Shift+L: Turn off line-in input.
* R: Remaining time for the currently playing track.
* Shift+R: Library scan progress.
* C: Title and duration of the currently playing track.
* Shift+C: Title and duration of the upcoming track if any.
* E: Encoder connection status.
* I: Listener count.
* Q: Studio status information such as whether a track is playing,
  microphone is on and others.
* Cart keys (F1, Control+1, for example): Play assigned carts from anywhere.
* H: Layer help.

## Track and microphone alarms

By default, NVDA will play a beep if five seconds are left in the track
(outro) and/or intro, as well as to hear a beep if microphone has been
active for a while. To configure track and microphone alarms, press
Alt+NVDA+1 to open alarms settings in Studio add-on settings screen. You can
also use this screen to configure if you'll hear a beep, a message or both
when alarms are turned on.

## Căutătorul de piese

Dacă doriți să căutați rapid un cântec după artist sau după numele acestuia
în lista de piese, apăsați Control+NVDA+F. Tastați sau alegeți numele
artistului sau al cântecului. NVDA vă va plasa fie la piesă dacă e găsită,
fie va afișa o eroare dacă n-a putut găsi piesa care vă interesa. Pentru a
găsi o melodie introdusă anterior sau un artist, apăsați NVDA+F3 sau
NVDA+Shift+F3 pentru a căuta înainte sau înapoi.

Notă: Căutătorul de piese e sensibil la majuscule.

## Exploratorul Cart

În funcție de ediție, SPL Studio permite atribuirea a până la 96 de carturi
pentru redare. NVDA vă permite să auziți care cart sau jingle este atribuit
acestor comenzi.

To learn cart assignments, from SPL Studio, press Alt+NVDA+3. Pressing the
cart command once will tell you which jingle is assigned to the
command. Pressing the cart command twice will play the jingle. Press
Alt+NVDA+3 to exit cart explorer. See the add-on guide for more information
on cart explorer.

## Analiză de timp a pistei

Pentru a obține lungimea pentru redare a pistei selectate, marcați pista
curentă pentru începerea analizei de timp (SPL Assistant, F9), apoi apăsați
SPL Assistant, F10 când ajungeți la finalul selecției.

## Exploratorul de coloane

By pressing Control+NVDA+1 through 0, you can obtain contents of specific
columns. By default, these are first ten columns for a track item (in
Studio: artist, title, duration, intro, outro, category, year, album, genre,
mood). For playlist editor in Creator and Remote VT client, column data
depends on column order as shown on screen. In Studio, Creator's main track
list, and Track Tool, column slots are preset regardless of column order on
screen and can be configured from add-on settings dialog under columns
explorer category.

## Track column announcement

You can ask NVDA to announce track columns found in Studio's playlist viewer
in the order it appears on screen or using a custom order and/or exclude
certain columns. Press NVDA+V to toggle this behavior while focused on a
track in Studio's playlist viewer. To customize column inclusion and order,
from column announcement settings panel in add-on settings, uncheck
"Announce columns in the order shown on screen" and then customize included
columns and/or column order.

## Instantaneu(snapshot) listă de redare

Puteți apăsa SPL Assistant, în timp ce vă focalizați pe o listă de redare în
Studio pentru a obține statistici diferite despre o listă de redare,
inclusiv numărul de melodii din lista de redare, cea mai lungă melodie,
artiștii de top și așa mai departe. După atribuirea unei comenzi
personalizate pentru această caracteristică, apăsarea de două ori a comenzii
personalizate va determina NVDA să prezinte informații instantanee de redare
ca pagină web pentru a putea utiliza modul de navigare pentru a naviga
(apăsați pe Escape pentru a închide).

## Playlist Transcripts

Pressing SPL Assistant, Shift+F8 will present a dialog to let you request
playlist transcripts in numerous formats, including in a plain text format,
an HTML table or a list.

## Dialog de configurare

Din fereastra studio, puteți apăsa Alt+NVDA+0 pentru a deschide dialogul de
configurare pentru supliment. Alternativ, accesați meniul preferințelor NVDA
și selectați elementul SPL Studio Settings. Acest dialog este, de asemenea,
utilizat pentru a gestiona profilurile de difuzare.

## Broadcast profiles dialog

You can save settings for specific shows into broadcast profiles. These
profiles can be managed via SPL broadcast profiles dialog which can be
accessed by pressing Alt+NVDA+P from Studio window.

## Modul de atingere SPL

Dacă utilizați Studio pe un computer cu ecran tactil care rulează Windows 8
sau o versiune ulterioară și aveți NVDA 2012.3 sau mai recent instalat,
puteți efectua unele comenzi Studio de pe ecranul tactil. Utilizați mai
întâi trei atingeri cu degetul pentru a comuta la modul SPL, apoi utilizați
comenzile de atingere listate mai sus pentru a efectua comenzi.

## Version 21.04/20.09.7-LTS

* 21.04: NVDA 2020.4 or later is required.
* In encoders, NVDA no longer fails to announce date and time information
  when performing date/time command (NVDA+F12). This affects NVDA 2021.1 or
  later.

## Version 21.03/20.09.6-LTS

* Minimum Windows release requirement is now tied to NVDA releases.
* Removed feedback email command (Alt+NVDA+Hyphen). Please send feedback to
  add-on developers using the contact information provided from Add-ons
  Manager.
* 21.03: parts of the add-on source code now include type annotations.
* 21.03: made the add-on code more robust with help from Mypy (a Python
  static type checker). In particular, fixed several long-standing bugs such
  as NVDA not being able to reset add-on settings to defaults under some
  circumstances and attempting to save encoder settings when not
  loaded. Some prominent bug fixes were also backported to 20.09.6-LTS.
* Fixed numerous bugs with add-on welcome dialog (Alt+NVDA+F1 from Studio
  window), including multiple welcome dialogs being shown and NVDA appearing
  to do nothing or playing error tones when welcome dialog remains open
  after Studio exits.
* Fixed numerous bugs with track comments dialog (Alt+NVDA+C three times
  from a track in Studio), including an error tone heard when trying to save
  comments and many track comment dialogs appearing if Alt+NVDA+C is pressed
  many times. If track comments dialog is still shown after Studio is
  closed, comments will not be saved.
* Various column commands such as columns explorer (Control+NVDA+number row)
  in Studio tracks and encoder status announcements no longer gives
  erroneous results when performed after NVDA is restarted while focused on
  tracks or encoders. This affects NVDA 2020.4 or later.
* Fixed numerous issues with playlist snapshots (SPL Assistant, F8),
  including inability to obtain snapshot data and reporting wrong tracks as
  shortest or longest tracks.
* NVDA will no longer announce "0 items in the library" when Studio exits in
  the middle of a library scan.
* NVDA will no longer fail to save changes to encoder settings after errors
  are encountered when loading encoder settings and subsequently settings
  are reset to defaults.

## Version 21.01/20.09.5-LTS

Version 21.01 supports SPL Studio 5.30 and later.

* 21.01: NVDA 2020.3 or later is required.
* 21.01: column header inclusion setting from add-on settings has been
  removed. NVDA's own table column header setting will control column header
  announcements across SPL suite and encoders.
* Added a command to toggle screen versus custom column inclusion and order
  setting (NVDA+V). Note that this command is available only when focused on
  a track in Studio's playlist viewer.
* SPL Assistant and Controller layer help will be presented as a browse mode
  document instead of a dialog.
* NVDA will no longer stop announcing library scan progress if configured to
  announce scan progress while using a braille display.

## Version 20.11.1/20.09.4-LTS

* Initial support for StationPlaylist suite 5.50.
* Improvements to presentation of various add-on dialogs thanks to NVDA
  2020.3 features.

## Version 20.11/20.09.3-LTS

* 20.11: NVDA 2020.1 or later is required.
* 20.11: Resolved more coding style issues and potential bugs with Flake8.
* Fixed various issues with add-on welcome dialog (Alt+NVDA+F1 from Studio),
  including wrong command shown for add-on feedback (Alt+NVDA+Hyphen).
* 20.11: Column presentation format for track and encoder items across
  StationPlaylist suite (including SAM encoder) is now based on
  SysListView32 list item format.
* 20.11: NVDA will now announce column information for tracks throughout SPL
  suite regardless of "report object description" setting in NVDA's object
  presentation settings panel. For best experience, leave this setting on.
* 20.11: In Studio's playlist viewer, custom column order and inclusion
  setting will affect how track columns are presented when using object
  navigation to move between tracks, including current navigator object
  announcement.
* If vertical column announcement is set to a value other than "whichever
  column I'm reviewing", NVDA will no longer announce wrong column data
  after changing column position on screen via mouse.
* improved playlist transcripts (SPL Assistant, Shift+F8) presentation when
  viewing the transcript in HTML table or list format.
* 20.11: In encoders, encoder labels will be announced when performing
  object navigation commands in addition to pressing up or down arrow keys
  to move between encoders.
* In encoders, in addition to Alt+NVDA+number row 0, pressing F12 will also
  open encoder settings dialog for the selected encoder.

## Version 20.10/20.09.2-LTS

* Due to changes to encoder settings file format, installing an older
  version of this add-on after installing this version will cause
  unpredictable behavior.
* It is no longer necessary to restart NVDA with debug logging mode to read
  debug messages from log viewer. You can view debug messages if log level
  is set to "debug" from NVDA's general settings panel.
* In Studio's playlist viewer, NVDA will not include column headers if this
  setting is disabled from add-on settings and custom column order or
  inclusion settings are not defined.
* 20.10: column header inclusion setting from add-on settings is deprecated
  and will be removed in a future release. In the future NVDA's own table
  column header setting will control column header announcements across SPL
  suite and encoders.
* When SPL Studio is minimized to the system tray (notification area), NVDA
  will announce this fact when trying to switch to Studio from other
  programs either through a dedicated command or as a result of an encoder
  connecting.

## Version 20.09-LTS

Version 20.09.x is the last release series to support Studio 5.20 and based
on old technologies, with future releases supporting Studio 5.30 and more
recent NVDA features. Some new features will be backported to 20.09.x if
needed.

* Due to changes in NVDA, --spl-configvolatile command line switch is no
  longer available to make add-on settings read-only. You can emulate this
  by unchecking "Save configuration when exiting NVDA" checkbox from NVDA's
  general settings panel.
* Removed pilot features setting from Advanced settings category under
  add-on settings (Alt+NVDA+0), used to let development snapshot users test
  bleeding-edge code.
* Column navigation commands in Studio are now available in track lists
  found in listener requests, insert tracks and other screens.
* Various column navigation commands will behave like NVDA's own table
  navigation commands. Besides simplifying these commands, it brings
  benefits such as ease of use by low vision users.
* Vertical column navigation (Control+Alt+up/down arrow) commands are now
  available for Creator, playlist editor, Remote VT, and Track Tool.
* Track columns viewer command (Control+NVDA+hyphen) is now available in
  Creator's Playlist Editor and Remote VT.
* Track columns viewer command will respect column order displayed on
  screen.
* In SAM encoders, improved NVDA's responsiveness when pressing Control+F9
  or Control+F10 to connect or disconnect all encoders, respectively. This
  may result in increased verbosity when announcing the selected encoder
  information.
* In SPL and AltaCast encoders, pressing F9 will now connect the selected
  encoder.

## Distribuții mai vechi

Consultați legătura cu logul de modificări pentru versiuni mai vechi ale
suplimentului.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
