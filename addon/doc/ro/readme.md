# StationPlaylist #
* Authors: Christopher Duffley <nvda@chrisduffley.com> (formerly Joseph Lee
  <joseph.lee22590@gmail.com>, originally by Geoff Shang and other
  contributors)
* Descărcați [versiunea stabilă][1]
* NVDA compatibility: 2022.4 and later

This add-on package provides improved usage of StationPlaylist Studio and
other StationPlaylist apps, as well as providing utilities to control Studio
from anywhere. Supported apps include Studio, Creator, Track Tool, VT
Recorder, and Streamer, as well as SAM, SPL, and AltaCast encoders.

For more information about the add-on, read the [add-on guide][2].

NOTE IMPORTANTE:

* This add-on requires StationPlaylist suite 5.40 or later.
* Some add-on features will be disabled or limited if NVDA is running in
  secure mode such as in logon screen.
* For best experience, disable audio ducking mode.
* Starting from 2018, [changelogs for old add-on releases][3] will be found
  on GitHub. This add-on readme will list changes from version 23.02 (2023)
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
below and select "Add", then type the gesture you wish to use.

Important: some of these commands will not work if NVDA is running in secure
mode such as from login screen.

* Switching to SPL Studio window from any program (unavailable in secure
  mode).
* SPL Controller layer (unavailable in secure mode).
* Announcing Studio status such as track playback from other programs
  (unavailable in secure mode).
* Announcing encoder connection status from any program (unavailable in
  secure mode).
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
* Control+Shift+F11: Toggles whether NVDA will switch to Studio window for
  the selected encoder if connected.
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

## SPL Controller

SPL Controler este un set de comenzi stratificate pe care le puteți utiliza
pentru a controla SPL Studio oriunde. Apăsați comanda stratului SPL
Controller, iar NVDA va spune: "Controller SPL". Apăsați o altă comandă
pentru a controla diferite setări Studio, cum ar fi microfonul pornit /
oprit sau pentru a reda piesa următoare.

Important: SPL Controller layer commands are disabled if NVDA is running in
secure mode.

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

From studio window, you can press Alt+NVDA+0 to open the add-on
configuration dialog. Alternatively, go to NVDA's preferences menu and
select SPL Studio Settings item. Not all settings are available if NVDA is
running in secure mode.

## Broadcast profiles dialog

You can save settings for specific shows into broadcast profiles. These
profiles can be managed via SPL broadcast profiles dialog which can be
accessed by pressing Alt+NVDA+P from Studio window.

## Modul de atingere SPL

If you are using Studio on a touchscreen computer with NVDA installed, you
can perform some Studio commands from the touchscreen. First use three
finger tap to switch to SPL mode, then use the touch commands listed above
to perform commands.

## Version 24.01

* The commands for the Encoder Settings dialog for use with the SPL and SAM
  Encoders are now assignable, meaning that you can change them from their
  defaults under the StationPlaylist category in NVDA Menu > Preferences >
  Input Gestures. The ones that are not assignable are the connect and
  disconnect commands. Also, to prevent command conflicts and make much
  easier use of this command on remote servers, the default gesture for
  switching to Studio after connecting is now Control+Shift+F11 (previously
  just F11). All of these can of course still be toggled from the Encoder
  Settings dialog (NVDA+Alt+0 or F12).

## Version 23.05

* To reflect the maintainer change, the manifest has been updated to
  indicate as such.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.
* In Studio's playlist viewer, NVDA will not announce column headers such as
  artist and title if table headers setting is set to either "rows and
  columns" or "columns" in NVDA's document formatting settings panel.

## Distribuții mai vechi

Please see the [changelog][3] for release notes for old add-on releases.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=stationPlaylist

[2]: https://github.com/chrisDuffley/stationplaylist/wiki/SPLAddonGuide

[3]: https://github.com/ChrisDuffley/stationplaylist/wiki/splchangelog
