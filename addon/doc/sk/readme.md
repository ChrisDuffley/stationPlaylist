# Station Playlist #

* Authors: Christopher Duffley <nvda@chrisduffley.com> (formerly Joseph Lee
  <joseph.lee22590@gmail.com>, originally by Geoff Shang and other
  contributors)

Doplnok zlepšuje prístupnosť Station Playlist Studio a ďalších pridružených
aplikácií a tiež umožňuje ovládať Station Playlist mimo hlavného okna
aplikácie. Podporuje tiež aplikácie Studio, Creator, Track Tool, VT
Recorder, Streamer, a tiež SAM, SPL, a AltaCast enkodéri.

For more information about the add-on, read the [add-on guide][1].

Dôležité:

* This add-on requires StationPlaylist suite 6.0 or later.
* Some add-on features will be disabled or limited if NVDA is running in
  secure mode such as in logon screen.
* For best experience, disable audio ducking mode.
* Starting from 2018, [changelogs for old add-on releases][2] will be found
  on GitHub. This add-on readme will list changes from version 25.01 (2025)
  onwards.
* Z okna SPL studio je možné uložiť nastavenia skratkou ctrl+nvda+c. Môžete
  tiež načítať uložené nastavenia skratkou ctrl+nvda+r. Takisto je možné
  obnoviť pôvodné nastavenia skratkou nvda+ctrl+r stlačením trikrát rýchlo
  za sebou. Toto sa týka aj nastavení enkodéra. Tieto je však možné len
  uložiť alebo obnoviť.
* Many commands will provide speech output while NVDA is in speak on demand
  mode (NVDA 2024.1 and later).

## Klávesové skratky

Most of these will work in Studio only unless otherwise specified. Unless
noted otherwise, these commands support speak on demand mode.

* Alt+Shift+T from Studio window: announce elapsed time for the currently
  playing track.
* Control+Alt+T (two finger flick down in SPL touch mode) from Studio
  window: announce remaining time for the currently playing track.
* nvda+shift+F12 (švihnutie dvoma prstami hore v dotykovom režime) v okne
  Studio: oznámi čas vysielania, napríklad 5 minút do celej hodiny. Stlačené
  dvakrát rýchlo za sebou oznamuje minúty aj sekundy.
* Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens
  alarms category in Studio add-on configuration dialog (does not support
  speak on demand).
* alt+nvda+1 pri úprave playlistu v okne creator a Remote VT playlist
  editor: Oznámi plánovaný čas spustenia playlistu.
* Alt+NVDA+2 pri úprave playlistu v okne creator a Remote VT playlist
  editor: Oznámi celkový čas skladieb v playliste.
* Alt+NVDA+3 from Studio window: Toggles cart explorer to learn cart
  assignments (does not support speak on demand).
* Alt+NVDA+3 pri úprave playlistu v okne creator a Remote VT playlist
  editor: Oznámi čas odohratia vybratej skladby.
* Alt+NVDA+4 pri úprave playlistu v okne creator a Remote VT playlist
  editor: Oznámi kategóriu a rotáciu pre načítaný playlist.
* Control+NVDA+F from Studio window: Opens a dialog to find a track based on
  artist or song name. Press NVDA+F3 to find forward or NVDA+Shift+F3 to
  find backward (does not support speak on demand).
* Shift+NVDA+R from Studio window: Steps through library scan announcement
  settings (does not support speak on demand).
* Control+Shift+X from Studio window: Steps through braille timer settings
  (does not support speak on demand).
* Control+Alt+left/right arrow (while focused on a track in Studio, Creator,
  Remote VT, and Track Tool): Move to previous/next track column (does not
  support speak on demand).
* Control+Alt+up/down arrow (while focused on a track in Studio, Creator,
  Remote VT, and Track Tool): Move to previous/next track and announce
  specific columns (does not support speak on demand).
* Ctrl+NVDA+1 až 0 (Pri zobrazení skladby v okne Studio, Creator (vrátane
  úpravy playlistu), Remote VT, a Track Tool): Oznámi príslušné metadáta
  (prvých 10). Stlačené dvakrát rýchlo za sebou zobrazí metadáta v režime
  prehliadania.
* Control+NVDA+- (hyphen while focused on a track in Studio, Creator, Remote
  VT, and Track Tool): display data for all columns in a track on a browse
  mode window (does not support speak on demand).
* NVDA+V while focused on a track (Studio's playlist viewer only): toggles
  track column announcement between screen order and custom order (does not
  support speak on demand).
* Alt+NVDA+C while focused on a track (Studio's playlist viewer only):
  announces track comments if any.
* Alt+NVDA+0 (two finger flick left in SPL mode) from Studio window: Opens
  the Studio add-on configuration dialog (does not support speak on demand).
* Alt+NVDA+P from Studio window: Opens the Studio broadcast profiles dialog
  (does not support speak on demand).
* Alt+NVDA+F1: Open welcome dialog (does not support speak on demand).

## Funkcie bez klávesových skratiek

The following commands are not assigned by default; if you wish to assign
them, use Input Gestures dialog to add custom commands. To do so, from
Studio window, open NVDA menu, Preferences, then Input Gestures. Expand
StationPlaylist category, then locate unassigned commands from the list
below and select "Add", then type the gesture you wish to use.

Important: some of these commands will not work if NVDA is running in secure
mode such as from login screen. Not all commands support speak on demand.

* Switching to SPL Studio window from any program (unavailable in secure
  mode, does not support speak on demand).
* SPL Controller layer (unavailable in secure mode).
* Announcing Studio status such as track playback from other programs
  (unavailable in secure mode).
* Announcing encoder connection status from any program (unavailable in
  secure mode).
* Podmnožina informačných príkazov.
* Oznámiť čas vrátane sekúnd z okna Studio.
* Oznámiť teplotu.
* Oznámiť názov nasledujúcej naplánovanej skladby.
* Oznámiť názov aktuálne prehrávanej skladby.
* Označenie aktuálnej skladby ako počiatočnej na časovú analýzu.
* Spustenie časovej analýzy.
* Zobrazenie štatistiky playlistu.
* Find text in specific columns (does not support speak on demand).
* Find tracks with duration that falls within a given range via time range
  finder (does not support speak on demand).
* Quickly enable or disable metadata streaming (does not support speak on
  demand).

## Ďalšie príkazy pre enkodéry

The following commands are available when using encoders, and the ones used
for toggling options for on-connection behavior such as focusing to Studio,
playing the first track, and toggling of background monitoring can be
assigned through the Input Gestures dialog in NVDA menu, Preferences, Input
Gestures, under the StationPlaylist category. These commands do not support
speak on demand.

* F9: Pripojiť zvolený stream.
* F10 (SAM encoder): Odpojí zvolený stream.
* Ctrl+F9: Pripojiť všetky streami.
* Ctrl+F10 (len SAM encoder): odpojí všetky streami.
* Control+Shift+F11: Toggles whether NVDA will switch to Studio window for
  the selected encoder if connected.
* Shift+F11: určuje, či sa automaticky prehrá prvá vybratá skladba po
  pripojení na server.
* Ctrl+F11: Zapína a vypína monitorovanie vybratého pripojenia na pozadí.
* ctrl+F12: Otvorí okno na výber odstráneného streamu (kde môžete zmeniť
  názvy a nastavenia).
* Alt+NVDA+0 or F12: Opens encoder settings dialog to configure options such
  as encoder label.

In addition, column review commands are available, including (supports speak
on demand):

* Ctrl+NVDA+1: Pozícia enkodéra.
* Ctrl+NVDA+2: Názov pripojenia.
* Ctrl+nvda+3 z okna Sam Encoder: Formát.
* Ctrl+nvda+3 z aplikácie SPL a AltaCast Encoder: Nastavenia enkodéra.
* Ctrl+nvda+4 z okna SAM Encoder: Stav pripojenia.
* Ctrl+NVDA+4 z aplikácie SPL a AltaCast Encoder: Stav a rýchlosť
  pripojenia.
* Ctrl+NVDA+5 z okna SAM Encoder: stav pripojenia.

## Podmnožina informačných príkazov

Táto podmnožina umožňuje zistiť stav SPL Studio, napríklad prehrávanie
skladby, celkové trvanie skladieb v časovom slote a podobne. Najprv je
potrebné stlačiť skratku podmnožiny príkazov a potom príslušné
písmeno. Väčšina príkazov je určených pre okno Studio a špeciálne pre
zobrazenie playlistu. V nastaveniach doplnku je navyše možné prepnúť skratky
tak, aby simulovali správanie, na ktoré ste zvyknutí z iných čítačov
obrazovky.

The available commands are (most commands support speak on demand):

* A: autopylot.
* C (Shift+C v rozložení pre JAWS): Oznámi názov prehrávanej skladby.
* C (JAWS layout): Toggle cart explorer (playlist viewer only, does not
  support speak on demand).
* D (R v rozložení pre JAWS): Oznámi ostávajúci čas do konca skladby. (Ak
  nefunguje, zopakujte skratku zo zobrazenia playlistu).
* Control+D (Studio 6.10 and later): Control keys enabled/disabled.
* E: Oznámi Stav streamovania metadát.
* Shift+1 až Shift+4: Stav jednotlivých pripojení. Shift+0: Stav pre DSP
  enkodér.
* F: Find track (playlist viewer only, does not support speak on demand).
* H: Oznámi Trvanie skladieb v aktuálnom hodinovom slote.
* Shift+H: Oznámi zostávajúci čas skladieb v aktuálnom hodinovom slote.
* I (L v rozložení pre JAWS): Oznámi počet pripojených poslucháčov.
* K: Prejde na záložku (vyznačenú skladbu v zozname skladieb).
* Ctrl+K: Nastaví aktuálnu skladbu ako záložku (v zobrazení playlistu).
* L (Shift+L v rozložení JAWS): Line in.
* M: Mikrofón.
* N: Oznámi Názov nasledujúcej skladby.
* O: Playlist hour over/under by.
* P: Oznámi Stav prehrávania (prehrávanie alebo zastavené).
* Shift+P: Oznámi tóninu skladby.
* R (Shift+E v rozložení JAWS): zapína a vypína nahrávanie do súboru.
* Shift+R: Oznámi stav skenovania knižnice.
* S: Oznámi naplánovaný čas spustenia skladby.
* Shift+S: Oznámi čas do spustenia (začína o).
* T: zapína a vypína editáciu jinglov.
* U: Oznámi čas od spustenia aplikácie Studio.
* W: Oznámi Predpoveď počasia.
* Y: Oznámi stav úpravy playlistu.
* F8: Zobrazí štatistiku playlistu (počet skladieb, trvanie playlistu,
  najkratšia a najdlhšia skladba).
* Shift+F8: Uloží prepis playlistu vo viacerých formátoch.
* F9: Označí skladbu ako počiatočnú pre analýzu (v zobrazení skladieb).
* F10: Analyzuje skladby (zo zobrazenia skladieb).
* F12: Prepína medzi konfiguračnými profilmi.
* F1: Oznámi funkcie a klávesové skratky.

## príkazy na ovládanie SPL

je to množina príkazov, pomocou ktorej môžete SPL ovládať aj ak nemáte
zamerané okno SPL Studio. NVDA Povie "ovládanie". NVDA počká na ďalší
príkaz, ktorým môžete sledovať stav mikrofónu, alebo prehrávanie
nasledujúcej skladby.

Important: SPL Controller layer commands are disabled if NVDA is running in
secure mode.

The available SPL Controller commands are (some commands support speak on
demand):

* P: Play the next selected track.
* U: Pause or unpause playback.
* S: Stop the track with fade out.
* T: Instant stop.
* M: Turn on microphone.
* Shift+M: Turn off microphone.
* N: Turn microphone on without fade.
* A: Turn on automation.
* Shift+A: Turn off automation.
* L: Turn on line-in input.
* Shift+L: Turn off line-in input.
* R: Remaining time for the currently playing track.
* Shift+R: Library scan progress.
* C: Title and duration of the currently playing track (supports speak on
  demand).
* Shift+C: Title and duration of the upcoming track if any (supports speak
  on demand).
* E: Encoder connection status (supports speak on demand).
* I: Listener count (supports speak on demand).
* Q: Studio status information such as whether a track is playing,
  microphone is on and others (supports speak on demand).
* Cart keys (F1, Control+1, for example): Play assigned carts from anywhere.
* H: Layer help.

## Upozornenia na zapnutý mikrofón, intro a koniec skladby

Predvolene NVDA zapípa 5 sekúnd pred koncom skladby alebo pred koncom intra
skladby a tiež upozorňuje, keď je zapnutý mikrofón. Toto nastavenie je možné
zapnúť, vypnúť a upraviť hodnoty po stlačení alt+nvda+1. Je možné nastaviť
upozornenie pípaním, rečou alebo oboje.

## Vyhľadávač skladieb

Ak chcete rýchlo nájsť skladbu podľa názvu interpreta alebo názvu skladby,
stlačte ctrl+nvda+f. Zadajte názov skladby alebo interpreta. NVDA vás
presunie na skladbu, ak sa našla, alebo zobrazí chybu, ak sa skladbu
nepodarilo nájsť. Ak chcete zopakovať to isté hľadanie smerom dopredu,
stlačte nvda+F3. Vyhľadávanie opačným smerom spustíte skratkou
nvda+shift+F3.

Pozor: Hľadanie rozlišuje veľké a malé písmená.

## Prehliadač jinglov

Studio umožňuje uložiť a zaradiť až 96 jinglov, v závislosti od edície,
ktorú používate. Pomocou NVDA môžete zistiť pozície jinglov v prehliadači.

Aby ste zistili pozíciu jingla, v okne studio stlačte alt+NVDA+3. Ak príkaz
stlačíte raz, dozviete sa, ktorý efekt je priradený konkrétnej skratke. Po
dvojitom stlačení sa zvuk prehrá. Prehliadač opustíte opäť skratkou
alt+nvda+3. Podrobnosti nájdete v návode k tomuto doplnku.

## Analyzovanie času

Ak chcete analyzovať čas vybratých skladieb, postupujte nasledovne: Nájdite
požadovanú počiatočnú skladbu. Potom stlačte skratku na spl zložený príkaz
nasledovanú klávesom F9. Potom nájdite koncovú skladbu, opätovne stlačte
skratku na spl zložený príkaz nasledovaný klávesom F10.

## Prehliadač metadát

By pressing Control+NVDA+1 through 0, you can obtain contents of specific
columns. By default, these are first ten columns for a track item (in
Studio: artist, title, duration, intro, outro, category, year, album, genre,
mood). In Studio, Creator's main track list and playlist editor, Track Tool,
and Remote VT, column slots are preset regardless of column order on screen
and can be configured from add-on settings dialog under columns explorer
category.

## Track column announcement

You can ask NVDA to announce track columns found in Studio's playlist viewer
in the order it appears on screen or using a custom order and/or exclude
certain columns. Press NVDA+V to toggle this behavior while focused on a
track in Studio's playlist viewer. To customize column inclusion and order,
from column announcement settings panel in add-on settings, uncheck
"Announce columns in the order shown on screen" and then customize included
columns and/or column order.

## Štatistika playlistu

Zloženým príkazom SPL F8 si môžete z okna studio zo zoznamu skladieb
zobraziť štatistiku playlistu. Tu zistíte počet skladieb, najdlhšiu skladbu,
najhranejšieho interpreta a podobne. Ak si priradíte k tejto funkcii vlastnú
skratku, môžete po jej dvojitom stlačení zobraziť informáciu v režime
prehliadania. Okno so štatistikou zatvoríte klávesom ESC.

## Prepisy playlistu

Zložený príkaz SPL shift+F8 umožní uložiť playlist ako prepis v čistom texte
alebo ako tabuľku HTML.

## Nastavenia doplnku

From studio window, you can press Alt+NVDA+0 to open the add-on
configuration dialog. Alternatively, go to NVDA's preferences menu and
select SPL Studio Settings item. Not all settings are available if NVDA is
running in secure mode.

## Profily

Pre rôzne relácie si môžete vytvoriť rôzne profily. Nastavenia vyvoláte
skratkou alt+nvda+p.

## Dotykový režim

If you are using Studio on a touchscreen computer with NVDA installed, you
can perform some Studio commands from the touchscreen. First use three
finger tap to switch to SPL mode, then use the touch commands listed above
to perform commands.

## Version 25.08/25.06.5-LTS

* 25.08: removed unmaintained localizations (add-on messages and
  documentation).
* In Studio, added two-finger flick left gesture in SPL touch mode to open
  SPL add-on settings.
* Removed "Status" from vertical column navigation options.
* In columns explorer (Studio, Track Tool, Creator, Remote VT), NVDA will no
  longer announce "blank" for empty column content (only column header will
  be announced).
* In Studio, Track Tool, Creator, and Remote VT, NVDA will announce track
  position and count when location command is performed (NVDA+Numpad Delete
  (desktop)/NVDA+Delete (laptop) and adding Shift for review cursor
  version).

## Version 25.07.2/25.06.4-LTS

* Restored missing localized messages including track comment announcement
  in Studio's playlist viewer.
* NVDA will present an error dialog when running Studio releases earlier
  than the version required for the add-on.
* In Studio, pressing NVDA+Shift+F3 the first time without opening find
  dialog will cause NVDA to search backwards.
* In Track Tool, NVDA will no longer play a beep when moving through tracks,
  especially for tracks without an intro set.

## Version 25.07.1/25.06.3-LTS

* In Studio's playlist viewer, NVDA will no longer appear to do nothing or
  play error tones when reporting column contents if vertical column
  navigation is set to values other than "whichever column I am reviewing".
* Setting vertical column navigation to "Status" column is deprecated and
  will be removed in a future add-on release.

## Version 25.07/25.06.2-LTS

Version 25.07 supports SPL Studio 6.0 and later.

* 25.07: code was refactored, including through use of Pyright (a Python
  static type checker). Some prominent code changes were also backported to
  25.06.2-LTS.
* Columns explorer (Control+NVDA+number row) is now configurable for Creator
  and Remote VT's playlist editor. A new button, "columns explorer for
  playlist editor" is available from columns explorer add-on settings
  screen.
* In columns explorer add-on settings, renamed "columns explorer" to
  "columns explorer for SPL Studio".
* Added JSON (JavaScript Object Notation) format as a playlist transcripts
  format.
* In encoders, NVDA will remove encoder settings if pressing Control+F12 to
  remove settings for encoder 10 and above if more than ten encoders are
  present.

## Version 25.06-LTS

Version 25.06.x is the last release series to support Studio 5.x with future
releases requiring Studio 6.x. Some new features will be backported to
25.06.x if needed.

* Internal changes to make the add-on more compatible with upcoming 64-bit
  NVDA.
* NVDA will no longer forget to transfer broadcast profiles while updating
  the add-on (fixing a regression introduced in 25.05).
* Added a new command in SPL Assistant to announce playlist hour over/under
  by in minutes and seconds (O).
* In Studio, the command to step through library scan announcement settings
  has changed from Alt+NVDA+R to Shift+NVDA+R as the former command toggles
  remote access feature in NVDA 2025.1.
* NVDA will no longer play error tones or appear to do nothing when
  performing some SPL Assistant commands after resizing Studio window.
* The user interface for confirmation dialog shown when deleting broadcast
  profiles now resembles NVDA's configuration profile deletion interface.
* In add-on settings, NVDA will no longer move keyboard focus to OK button
  after closing columns explorer and reset dialogs.
* NVDA will recognize track column changes introduced in Creator and Track
  Tool 6.11.
* In columns explorer for Creator, "Date Restriction" column is now
  "Restrictions".
* NVDA will no longer play wrong carts when playing them via SPL Controller
  layer.

## Version 25.05

* NVDA 2024.1 or later is required due to Python 3.11 upgrade.
* Restored limited support for Windows 8.1.
* Moved ad-on wiki documents such as add-on changelog to the main code
  repository.
* Added close button to playlist snapshots, playlist transcripts, and SPL
  Assistant and Controller layer help screens (NVDA 2025.1 and later).
* NVDA will no longer do nothing or play error tones when announcing weather
  and temperature information in Studio 6.1x (SPL Assistant, W).

## Version 25.01

* 64-bit Windows 10 21H2 (build 19044) or later is required.
* Download links for add-on releases are no longer included in add-on
  documentation. You can download the add-on from NV Access add-on store.
* Switched linting tool from Flake8 to Ruff and reformatted add-on modules
  to better align with NVDA coding standards.
* Removed support for automatic add-on updates feature from Add-on Updater
  add-on.
* In Studio 6.10 and later, added a new command in SPL Assistant to announce
  control keys enabled/disabled status (Control+D).

## Staršie verzie

Please see the [changelog][2] for release notes for old add-on releases.

[1]:
https://github.com/ChrisDuffley/stationPlaylist/blob/main/addonuserguide.md

[2]: https://github.com/ChrisDuffley/stationPlaylist/blob/main/changes.md
