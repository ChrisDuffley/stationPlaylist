# StationPlaylist #

* Authors: Christopher Duffley <nvda@chrisduffley.com> (formerly Joseph Lee
  <joseph.lee22590@gmail.com>, originally by Geoff Shang and other
  contributors)

Dieses Zusatzpaket bietet eine verbesserte Nutzung von StationPlaylist
Studio und anderen StationPlaylist-Anwendungen sowie Dienstprogramme zur
Steuerung von Studio von überall. Zu den unterstützten Anwendungen gehören
Studio, Creator, Track Tool, VT Recorder und Streamer sowie SAM, SPL und
AltaCast Encoder.

For more information about the add-on, read the [add-on guide][1].

WICHTIGE HINWEISE:

* This add-on requires StationPlaylist suite 5.50 or later.
* Einige Funktionen der Erweiterung werden deaktiviert oder eingeschränkt,
  sobald NVDA im Abgesicherten Modus ausgeführt wird, z. B. während der
  Windows-Anmeldung.
* Für ein optimales Sound-Erlebnis sollten Sie den Modus für die
  Verringerung der Audio-Quellen deaktivieren.
* Starting from 2018, [changelogs for old add-on releases][2] will be found
  on GitHub. This add-on readme will list changes from version 23.02 (2023)
  onwards.
* Während die Studio-Software läuft, können Sie gespeicherte Einstellungen
  speichern, wieder laden oder Zusatzeinstellungen auf die Standardwerte
  zurücksetzen, indem Sie Strg+NVDA+C, Strg+NVDA+R einmal bzw. Strg+NVDA+R
  dreimal drücken. Dies gilt auch für die Encoder-Einstellungen - Sie können
  Encoder-Einstellungen speichern und zurücksetzen (nicht neu laden), wenn
  Sie Encoder verwenden.
* Many commands will provide speech output while NVDA is in speak on demand
  mode (NVDA 2024.1 and later).

## Tastenkürzel

Most of these will work in Studio only unless otherwise specified. Unless
noted otherwise, these commands support speak on demand mode.

* Alt+Shift+T from Studio window: announce elapsed time for the currently
  playing track.
* Control+Alt+T (two finger flick down in SPL touch mode) from Studio
  window: announce remaining time for the currently playing track.
* NVDA+Umschalt+F12 (mit zwei Fingern nach oben wischen im SPL-Touch-Modus)
  aus dem Studio-Fenster: Zeigt die Sendezeit an z.B. 5 Minuten bis zur
  vollen Stunde. Wenn Sie diesen Befehl zweimal drücken, werden Minuten und
  Sekunden bis zur vollen Stunde angesagt.
* Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens
  alarms category in Studio add-on configuration dialog (does not support
  speak on demand).
* Alt+NVDA+1 aus dem Playlist-Editor des Creators und dem
  Remote-VT-Playlist-Editor: Meldet die geplante Zeit für die
  Wiedergabeliste.
* Alt+NVDA+2 aus dem Playlist-Editor des Creators und dem
  Remote-VT-Playlist-Editor: Meldet die Gesamtdauer der Wiedergabeliste.
* Alt+NVDA+3 from Studio window: Toggles cart explorer to learn cart
  assignments (does not support speak on demand).
* Alt+NVDA+3 aus dem Playlist-Editor des Creators und dem
  Remote-VT-Playlist-Editor: Zeigt an, wann die Wiedergabe des ausgewählten
  Titels geplant ist.
* Alt+NVDA+4 aus dem Playlist-Editor des Creators und dem
  Remote-VT-Playlist-Editor: Meldet die Rotation und die Kategorie, die mit
  der die Wiedergabeliste verbunden ist.
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
* Strg+NVDA+1 bis 0 (während der Fokus auf einem Track in Studio, Creator
  (einschließlich im Playlist-Editor), Remote-VT und Track Tool liegt):
  Spalteninhalt für eine bestimmte Spalte ankündigen (standardmäßig die
  ersten zehn Spalten). Wenn Sie diesen Befehl zweimal drücken, werden die
  Spalteninformationen in einem Fenster im Blätternmodus angezeigt.
* Control+NVDA+- (hyphen while focused on a track in Studio, Creator, Remote
  VT, and Track Tool): display data for all columns in a track on a browse
  mode window (does not support speak on demand).
* NVDA+V while focused on a track (Studio's playlist viewer only): toggles
  track column announcement between screen order and custom order (does not
  support speak on demand).
* Alt+NVDA+C während der Fokus auf einem Titel steht, (nur
  Studio-Playlistenbetrachter): werden Titel-Kommentare falls vorhanden
  gemeldet.
* Alt+NVDA+0 from Studio window: Opens the Studio add-on configuration
  dialog (does not support speak on demand).
* Alt+NVDA+P from Studio window: Opens the Studio broadcast profiles dialog
  (does not support speak on demand).
* Alt+NVDA+F1: Open welcome dialog (does not support speak on demand).

## Nicht zugewiesene Befehle

Die folgenden Befehle sind standardmäßig nicht zugewiesen; wenn Sie sie
zuweisen möchten, verwenden Sie den Dialog Eingabegesten, um
benutzerdefinierte Befehle hinzuzufügen. Öffnen Sie dazu im Studio-Fenster
das NVDA-Menü, Einstellungen und dann Eingaben. Erweitern Sie die Kategorie
StationPlaylist, suchen Sie dann nicht zugewiesene Befehle aus der Liste
unten und wählen Sie "Hinzufügen" aus, geben Sie dann die Taste oder
Tastenkombination ein, welche Sie verwenden möchten.

Important: some of these commands will not work if NVDA is running in secure
mode such as from login screen. Not all commands support speak on demand.

* Switching to SPL Studio window from any program (unavailable in secure
  mode, does not support speak on demand).
* Die SPL-Steuerung ist (im Abgesicherten Modus) nicht verfügbar.
* Die Mitteilungen des Studio-Status, wie z. B. die Wiedergabe von Titeln
  aus anderen Anwendungen ist (im Abgesicherten Modus) nicht verfügbar.
* Ansage des Encoder-Verbindungsstatus aus einer beliebigen Anwendung heraus
  ist (im Abgesicherten Modus nicht verfügbar.
* Befehlsschicht des SPL-Assistenten im SPL-Studio.
* Meldet die Studiozeit einschließlich Sekunden.
* Meldet die Temperatur.
* Meldet die bezeichnung des nächsten geplanten Titels, wenn vorhanden.
* Gibt die Bezeichnung des aktuell abgespielten Titels aus.
* Markiert den aktuellen Titel als Anfand für die Titel-Zeitanalyse.
* Titel-Zeitanalyse durchführen.
* Nimmt Statistiken für eine Wiedergabeliste auf.
* Find text in specific columns (does not support speak on demand).
* Find tracks with duration that falls within a given range via time range
  finder (does not support speak on demand).
* Quickly enable or disable metadata streaming (does not support speak on
  demand).

## Zusätzliche Befehle bei der Encoder-Verwendung

The following commands are available when using encoders, and the ones used
for toggling options for on-connection behavior such as focusing to Studio,
playing the first track, and toggling of background monitoring can be
assigned through the Input Gestures dialog in NVDA menu, Preferences, Input
Gestures, under the StationPlaylist category. These commands do not support
speak on demand.

* F9: Den ausgewählten Encoder verbinden.
* F10 (nur gleicher Encoder): Trennt den ausgewählten Encoder.
* Strg+F9: Verbindet alle Encoder.
* Strg+F10 (nur SAM-Encoder): Alle Encoder trennen.
* Control+Shift+F11: Toggles whether NVDA will switch to Studio window for
  the selected encoder if connected.
* Shift+F11: legt fest, ob Studio den ersten ausgewählten Titel abspielen
  soll, wenn der Encoder an einen Streaming-Server angeschlossen ist.
* Control+F11: Schaltet die Hintergrundüberwachnung des ausgewählten
  Encoders ein- und aus.
* Strg+F12: Öffnet ein Dialogfeld zur Auswahl des ausgelöschten Encoders
  (zur Neuausrichtung der Encoder-Beschreibung und Einstellungen).
* Alt+NVDA+0 or F12: Opens encoder settings dialog to configure options such
  as encoder label.

In addition, column review commands are available, including (supports speak
on demand):

* STRG+NVDA+1: Position des Encoders.
* Strg+NVDA+2: Encoder-Beschreibung.
* STRG+NVDA+3 aus dem SAM-Encoder: Encoder-Format.
* Strg+NVDA+3 aus SPL und AltaCast Encoder: Encoder-Einstellungen.
* STRG+NvDA+4 aus dem SAM-Encoder: meldet den Encoder-Verbindungsstatus.
* Strg+NVDA+4 aus SPL und AltaCast Encoder: Übertragungsgeschwindigkeit oder
  Verbindungsstatus.
* STRG+NVDA+5 aus dem SAM-Encoder: Beschreibt den Verbindungsstatus.

## Befehlsschicht für den SPL-Assistenten

Mit dieser Befehlsschicht können Sie verschiedene Statusmeldungen in SPL
Studio erhalten, wie z.B. ob ein Titel gerade abgespielt wird, die
Gesamtdauer aller Titel für die aktuelle Stunde und so weiter. Verwenden Sie
in einem beliebigen SPL-Studio-Fenster die Befehlsschicht des
SPL-Assistenten und drücken Sie dann eine der Tasten aus der untenstehenden
Liste (ein oder mehrere Befehle sind exklusiv für den Playlist-Viewer
bestimmt). Sie können NVDA auch so konfigurieren, dass es Befehle von
anderen Screenreadern simuliert.

The available commands are (most commands support speak on demand):

* A: Automatisierung.
* C (Umschalt+C im JAWS-Layout): Name des aktuell abgespielten Titels.
* C (JAWS layout): Toggle cart explorer (playlist viewer only, does not
  support speak on demand).
* D (R in der JAWS-Darstellung): Restdauer der Playlist (wenn eine
  Fehlermeldung angezeigt wird, wechseln Sie zum Playlist-Viewer und geben
  Sie diesen Befehl ein).
* Control+D (Studio 6.10 and later): Control keys enabled/disabled.
* E: Metadaten-Streaming-Status.
* Umschalt+1 bis 4, Umschalt+0: Status für einzelne Metadaten-Streaming-URLs
  (0 ist für DSP-Encoder).
* F: Find track (playlist viewer only, does not support speak on demand).
* H: Dauer der Titel in dieser Stunde.
* Umschalt+H: Verbleibende Spieldauer für den Stundenplatzhalter.
* I (L im JAWS-Layout): Anzahl der Zuhörer.
* K: springt zum Lesezeichentitel (nur im Playlist-Viewer).
* Strg+K: Aktuellen Titel als Lesezeichentitel setzen (nur im
  Playlist-viewer).
* L (Umschalt+L im JAWS-Layout): Line-In.
* M: Mikrofon.
* N: Titel der nächst geplante Datei.
* O: Playlist hour over/under by.
* P: Wiedergabestatus (Wiedergabe oder angehalten).
* Umschalt+P: Pitch des aktuellen Titels.
* R (Umschalt+E im JAWS-Layout): Datensatz in Datei aktiviert/deaktiviert.
* Umschalt+R: Überwachung des Bibliothek-Scans läuft...
* S: Titel beginnt (geplant).
* Umschalt+S: Zeit bis zur Wiedergabe des ausgewählten Titels (Titel startet
  in...).
* T: Cart-Bearbeitungs-/Einfügemodus ein und ausschalten.
* U: Studiozeit.
* W: Wetter und Temperatur, wenn konfiguriert.
* Y: Status der Playlist-Änderungen.
* F8: nimmt Schnappschüsse von Playlisten auf (Anzahl der Titel, längster
  Titel, etc.).
* Umschalt+F8: Playlist-Protokolle in verschiednen Formaten anfordern.
* F9: markiert den aktuellen Titel als Beginn der Playlist-Analyse (nur im
  Playlist-Viewer).
* F10: führt die Titel-zeitanalyse durch (nur im Playlist-Viewer).
* F12: schaltet zwischen aktuellen und einem vordefinierten Profil um.
* F1: Hilfe für die Befehlsschicht.

## SPL-Controller

Der SPL-Controller bietet eine Befehlsschicht, mit der Sie SPL-Studio von
überall steuern können. Drücken Sie den Befehl für die SPL-Controller
-Befehlsschicht und NVDA wird "SPL-Controller." ansagen. Drücken Sie einen
anderen Befehl, um verschiedene Studio-Funktionen auszuführen (z.B. Mikrofon
ein/aus oder nächsten Titel abspielen).

Wichtig: Die Befehle in der SPL-Steuerung sind deaktiviert, sobald NVDA im
Abgesicherten Modus ausgeführt wird.

The available SPL Controller commands are (some commands support speak on
demand):

* P: Nächsten ausgewählten Titel abspielen.
* U: Wiedergabe anhalten oder fortsetzen.
* S: Titel anhalten mit Ausblenden.
* T: Sofort anhalten.
* M: Mikrofon einschalten.
* Umschalt+M: Mikrofon ausschalten.
* N: Turn microphone on without fade.
* A: Automatisierung einschalten.
* Umschalt+A: Automatisierung ausschalten.
* L: Line-In-Eingang einschalten.
* Umschalt+L: Line-In-Eingang ausschalten.
* R: Restzeit für den aktuell wiedergegebenen Titel.
* Umschalt+R: Fortschritt des Bibliotheksscans.
* C: Title and duration of the currently playing track (supports speak on
  demand).
* Shift+C: Title and duration of the upcoming track if any (supports speak
  on demand).
* E: Encoder connection status (supports speak on demand).
* I: Listener count (supports speak on demand).
* Q: Studio status information such as whether a track is playing,
  microphone is on and others (supports speak on demand).
* Cart-Tasten (z. B. F1, Strg+1): Spielen Sie zugewiesene Cart von überall
  aus.
* H: Layer-Hilfe.

## Track- und Mikrofon-Alarm

Standardmäßig gibt NVDA einen Piepton ab, wenn noch fünf Sekunden im Track
(Outro) und/oder Intro verbleiben, sowie einen Piepton, wenn das Mikrofon
eine Zeit lang aktiv war. Um Track- und Mikrofon-Alarme zu konfigurieren,
drücken Sie Alt+NVDA+1, um die Alarm-Einstellungen in den
Zusatz-Einstellungen zu öffnen. Sie können ihn auch verwenden, um zu
konfigurieren, ob Sie einen Piepton, eine Nachricht oder beides hören, wenn
die Alarme eingeschaltet werden.

## Titelfinder

Wenn Sie schnell einen Song nach Künstler oder Titelbezeichnung aus der
Titelliste finden möchten, drücken Sie STRG+NVDA+F. Geben Sie den Namen des
Künstlers oder den Namen des Titels ein oder wählen Sie ihn aus. NVDA wird
den Cursor entweder beim gefundenen Titel platzieren oder einen Fehler
anzeigen, wenn der gesuchte Titel nicht gefunden wurde. Um einen zuvor
eingegebenen Titel oder Künstler zu finden, drücken Sie NVDA+F3 oder
NVDA+Umschalt+F3. Somit such NVDA vorwärts oder rückwärts.

Hinweis: Im Titelfinder wird zwischen Groß- und Kleinschreibung
unterschieden.

## Cart-Explorer

Je nach Version erlaubt SPL-Studio die Zuweisung von bis zu 96 Carts für die
Wiedergabe. Mit NVDA können Sie hören, welches Cart oder Ton diesen Befehlen
zugeordnet ist.

Um die Zuordnung von Carts zu lernen, drücken Sie im SPL-Studio
Alt+NVDA+3. Durch einmaliges Drücken des Cart-Befehls erfahren Sie, welcher
Ton dem Befehl zugeordnet ist. Durch zweimaliges Drücken des Cart-Befehls
wird der Ton abgespielt. Drücken Sie Alt+NVDA+3, um den Cart-Explorer zu
verlassen. Weitere Informationen zum Cart-Explorer finden Sie in der
Erweiterungsanleitung.

## Titel-Zeitanalyse

Um die Dauer bis zur Wiedergabe der ausgewählten Titel herauszufinden,
markieren Sie den aktuellen Titel als Anfang der Titel-Zeitanalyse (F9 im
SPL-Assistenten) und drücken Sie dann F10, wenn Sie das Ende der Auswahl
erreicht haben.

## Spaltenexplorer

Durch Drücken von Strg+NVDA+1 bis 0 oder SPL-Assistent, 1 bis 0, können Sie
den Inhalt bestimmter Spalten erhalten. Standardmäßig sind dies Künstler,
Titel, Dauer, Intro, Outro, Kategorie, Jahr, Album, Genre und Stimmung. Sie
können konfigurieren, welche Spalten über den Spalten-Explorer-Dialog, der
sich in den Einstellungen der Erweiterung befindet, erkundet werden sollen.

## Spaltenansage verfolgen

Sie können NVDA anweisen, die im Wiedergabelisten-Betrachter von Studio
gefundenen Titelspalten in der Reihenfolge anzukündigen, in der sie auf dem
Bildschirm angezeigt werden, oder eine benutzerdefinierte Reihenfolge zu
verwenden und / oder bestimmte Spalten auszuschließen. Drücken Sie NVDA+V,
um dieses Verhalten umzuschalten, während Sie sich auf einen Titel im
Wiedergabelisten-Betrachter von Studio befinden. Deaktivieren Sie zum
Anpassen der Spalteneinbeziehung und -reihenfolge im Bereich
"Spaltenansagen" in den Einstellungen der Erweiterung das Kontrollkästchen
"Spalten in der auf dem Bildschirm angezeigten Reihenfolge ankündigen" und
passen Sie dann die enthaltenen Spalten und / oder die Spaltenreihenfolge
an.

## Playlist-Statistiken

Sie können im SPL-Assistenten F8 drücken, während Sie sich auf eine
Wiedergabeliste in Studio konzentrieren, um verschiedene Statistiken über
eine Wiedergabeliste zu erhalten. Die Statistik beinhaltet beispielsweise
die Anzahl der Titel, der längste Titel, der beste Künstler und so
weiter. Nach der Zuweisung eines benutzerdefinierten Befehls für diese
Funktion führt ein zweimaliges Drücken des benutzerdefinierten Befehls dazu,
dass NVDA die Schnappschuss-Informationen der Wiedergabeliste als Webseite
anzeigt, so dass Sie den Lesemodus zum Navigieren verwenden können. Drücken
Sie die Escape-Taste zum Schließen.

## Playlist-Protokolle

Umschalt+F8 im SPL-Assistenten ruft ein Dialogfeld auf, in dem Sie
Playlist-Protokolle in verschiedenen Formaten öffnen können (z.B. einfaches
Textformat, eine HTML-Tabelle oder eine Liste).

## Konfigurationsdialog

Im Studio-Fenster können Sie Alt+NVDA+0 drücken, um das Dialogfeld für die
Konfiguration der Erweiterung zu öffnen oder  auch das Einstellungsmenü von
NVDA aufrufen und dort den Eintrag für die Einstellung des SPL-Studios
auswählen. Nicht alle Einstellungen sind verfügbar, sobald NVDA im
Abgesicherten Modus läuft.

## Dialogfeld der Sendeprofile

Sie können Einstellungen für bestimmte Sendungen in Sendeprofilen
speichern. Diese Profile können über das Dialogfeld SPL-Sendeprofile
verwaltet werden, auf das durch Drücken von Alt+NVDA+P im Studio-Fenster
zugegriffen werden kann.

## SPL-Touchmodus

Wenn Sie Studio auf einem Computer mit Touchscreen und installiertem NVDA
verwenden, können Sie einige Studio-Befehle über den Touchscreen
ausführen. Wechseln Sie zunächst mit drei Fingern in den SPL-Modus und
verwenden Sie dann die oben aufgeführten Touch-Befehle, um Befehle
auszuführen.

## Version 25.06-LTS

Version 25.06.x is the last release series to support Studio 5.x with future
releases requiring Studio 6.x. Some new features will be backported to
25.06.x if needed.

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
  and temperature information in Studio 6.x (SPL Assistant, W).

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

## Version 24.03

* Compatible with NVDA 2024.1.
* NVDA 2023.3.3 or later is required.
* Support for StationPlaylist suite 6.10.
* Most commands support speak on demand (NVDA 2024.1) so announcements can
  be spoken in this mode.

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

* NVDA 2022.4 oder neuer wird benötigt.
* Windows 10 Version 21H2 (November 2021 Update bzw. Build 19044) oder neuer
  wird benötigt.
* In der Ansicht für die Wiedergabelisten im Studio zeigt NVDA keine
  Spaltenüberschriften wie Interpret und Titel an, wenn die Einstellung für
  Tabellenüberschriften in den Einstellungen für die Dokument-Formatierungen
  in NVDA entweder auf "Zeilen und Spalten" oder "Spalten" gesetzt ist.

## Ältere Versionen

Please see the [changelog][2] for release notes for old add-on releases.

[1]:
https://github.com/ChrisDuffley/stationPlaylist/blob/main/addonuserguide.md

[2]: https://github.com/ChrisDuffley/stationPlaylist/blob/main/changes.md
