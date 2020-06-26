# StationPlaylist #

* Autoren: Geoff Shang, Joseph Lee und weitere Mitwirkende
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]
* NVDA compatibility: 2019.3 to 2020.2

Dieses Zusatzpaket bietet eine verbesserte Nutzung von StationPlaylist
Studio und anderen StationPlaylist-Anwendungen sowie Dienstprogramme zur
Steuerung von Studio von überall. Zu den unterstützten Anwendungen gehören
Studio, Creator, Track Tool, VT Recorder und Streamer sowie SAM, SPL und
AltaCast Encoder.

Weitere Informationen über die Erweiterungfinden Sie in der [Anleitung der
Erweiterung][4]. Entwickler, die wissen möchten, wie das Add-On gebaut wird,
finden die Datei "buildInstructions.txt", die sich im Hauptverzeichnis des
Repository der Erweiterung befindet.

WICHTIGE HINWEISE:

* Diese Erweiterung benötigt die StationPlaylist-Suite 5.20 oder neuer.
* Wenn Sie Windows 8 oder höher verwenden, setzen Sie die Reduzierung der
  Lautstärke anderer Audioquellen auf "nie" im Dialog Sprachausgabe im
  NVDA-Einstellungsmenü.
* Starting from 2018, [changelogs for old add-on releases][5] will be found
  on GitHub. This add-on readme will list changes from version 18.09 (2018
  onwards).
* Bestimmte Funktionen sind nicht mehr verfügbar, z.B. während NVDA im
  abgesicherten Modus ausgeführt wird.
* Aufgrund technischer Einschränkungen können Sie diese Erweiterung nicht
  auf der Windows-Store-Version von NVDA installieren oder verwenden.
* Features, die als "experimentell" gekennzeichnet sind, sollen etwas vor
  einer zukünftigen Version testen, sodass sie nicht in stabilen Versionen
  aktiviert werden.
* While Studio is running, you can save, reload saved settings, or reset
  add-on settings to defaults by pressing Control+NVDA+C, Control+NVDA+R
  once, or Control+NVDA+R three times, respectively. This is also applicable
  to encoder settings - you can save and reset (not reload) encoder settings
  if using encoders.

## Tastenkürzel

Die meisten davon funktionieren nur in Studio, sofern nicht anders
angegeben.

* Alt+Umschalt+T bei geöffnetem spl-Hauptfenster: zeigt die verstrichene
  Zeit der Wiedergabe für den aktuellen Titel an.
* Strg+Alt+T (nach unten  streichen mit zwei Fingern im SPL Touch-Modus) bei
  aktivem spl-Hauptfenster: zeigt die verbleibende Zeit bei der Wiedergabe
  des aktuellen Titels an.
* NVDA+Umschalt+F12 (mit zwei Fingern nach oben wischen im SPL-Touch-Modus)
  aus dem Studio-Fenster: Zeigt die Sendezeit an z.B. 5 Minuten bis zur
  vollen Stunde. Wenn Sie diesen Befehl zweimal drücken, werden Minuten und
  Sekunden bis zur vollen Stunde angesagt.
* Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens
  alarms category in Studio add-on configuration dialog.
* Alt+NVDA+1 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces scheduled time for the loaded playlist.
* Alt+NVDA+2 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces total playlist duration.
* Alt+NVDA+3 aus dem Studio-Fenster: legt den Cart-Explorer fest, um die
  Zuordnung von Carts zu lernen.
* Alt+NVDA+3 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces when the selected track is scheduled to play.
* Alt+NVDA+4 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces rotation and category associated with the loaded playlist.
* STRG+NVDA+f aus dem Studio-Fenster: Öffnet einen Dialog, um einen Titel
  basierend auf Künstler oder Titelbezeichnung zu finden. Drücken Sie
  NVDA+F3, um vorwärts zu suchen oder NVDA+Umschalt+F3, um rückwärts zu
  suchen.
* Alt+NVDA+R aus dem Studio-Fenster: Benachrichtigungseinstellungen für
  Bibliothek-Scans.
* Strg+Umschalt+X aus dem Studio-Fenster: Braille-Timer-Einstellungen.
* Control+Alt+left/right arrow (while focused on a track in Studio, Creator,
  Remote VT, and Track Tool): Announce previous/next track column.
* Control+Alt+Home/End (while focused on a track in Studio, Creator, Remote
  VT, and Track Tool): Announce first/last track column.
* Strg+Alt+Pfeil nach oben/unten (während der Fokus nur auf einen Titel in
  Studio gerichtet ist): Zur vorherigen oder nächsten Spur wechseln und
  bestimmte Spalten mitteilen.
* Control+NVDA+1 through 0 (while focused on a track in Studio, Creator
  (including Playlist Editor), Remote VT, and Track Tool): Announce column
  content for a specified column (first ten columns by default). Pressing
  this command twice will display column information on a browse mode
  window.
* Strg+NVDA+- (Bindestrich bei Fokussierung auf eine Spur in Studio, Creator
  und Titelwerkzeug): Anzeige der Daten für alle Spalten einer Spur im
  Lesemodus.
* Alt+NVDA+C während der Fokus auf einen Track (nur Studio): Meldet
  Track-Kommentare, falls vorhanden.
* Alt+NVDA+0 aus dem Studio-Fenster: Öffnet den Konfigurationsdialog der
  SPL-Erweiterung.
* Alt+NVDA+P from Studio window: Opens the Studio broadcast profiles dialog.
* Alt+NVDA+Minus (Bindestrich) aus dem Studio-Fenster: Senden Sie Feedback
  an den Entwickler der Erweiterung mit der E-Mail-Programm.
* Alt+NVDA+F1: öffnet das Willkommensdialog.

## Nicht zugewiesene Befehle

Die folgenden Befehle sind standardmäßig nicht zugewiesen; wenn Sie sie
zuweisen möchten, verwenden Sie den Dialog Eingabegesten, um
benutzerdefinierte Befehle hinzuzufügen. Öffnen Sie dazu im Studio-Fenster
das NVDA-Menü, Einstellungen und dann Eingaben. Erweitern Sie die Kategorie
StationPlaylist, suchen Sie dann nicht zugewiesene Befehle aus der Liste
unten und wählen Sie "Hinzufügen" aus, geben Sie dann den die Taste oder
Tastenkombination ein, die Sie verwenden möchten.

* Das wechseln zum SPL Studio-Fenster aus einem beliebigen Programm.
* Befehlsschicht des SPL-Controllers.
* Ansage des Studio-Status beim Navigieren in anderen Programmen,
  z.B. Titelwiedergabe.
* Anzeige des Verbindungsstatus des Encoders von jedem Programm aus.
* Befehlsschicht des SPL-Assistenten im SPL-Studio.
* Meldet die Studiozeit einschließlich Sekunden.
* Meldet die Temperatur.
* Meldet die bezeichnung des nächsten geplanten Titels, wenn vorhanden.
* Gibt die Bezeichnung des aktuell abgespielten Titels aus.
* Markiert den aktuellen Titel als Anfand für die Titel-Zeitanalyse.
* Titel-Zeitanalyse durchführen.
* Nimmt Statistiken für eine Wiedergabeliste auf.
* Findet Text in bestimmten Spalten.
* Findet über den Suchdialog für die Zeitspanne  Titel mit einer Dauer, die
  in einem bestimmten Zeitraum liegt.
* Schnelles Aktivieren oder Deaktivieren von Metadaten-Streaming.

## Zusätzliche Befehle bei der Encoder-Verwendung

Folgende Befehle stehen zur Verfügung, wenn Sie Encoder verwenden:

* F9: Mit einem Streaming-Server verbinden.
* F10 (nur SAM-Encoder): Trennt die Verbindung zum Streaming-Server.
* STRG+F9/STRG+F10 (nur beim SAM-Encoder): Alle Encoder verbinden
  bzw. trennen.
* F11: legt fest, ob NVDA zum Studio-Fenster für den ausgewählten Encoder
  wechseln soll, wenn dieser angeschlossen ist.
* Shift+F11: legt fest, ob Studio den ersten ausgewählten Titel abspielen
  soll, wenn der Encoder an einen Streaming-Server angeschlossen ist.
* Control+F11: Schaltet die Hintergrundüberwachnung des ausgewählten
  Encoders ein- und aus.
* F12: Öffnet einen Dialog zur Eingabe einer benutzerdefinierten Bezeichnung
  für den ausgewählten Encoder oder Stream.
* STRG+F12: öffnet einen Dialog zur Auswahl des von Ihnen gelöschten
  Encoders (für das Zurücksetzen von Streambezeichnungen und
  Encodereinstellungen).
* Alt+NVDA+0: Öffnet den Dialog Encoder-Einstellungen, um Optionen wie
  Streambezeichnung zu konfigurieren.

Darüber hinaus stehen folgende Befehle für den Spaltenexplorer zur
Verfügung:

* STRG+NVDA+1: Position des Encoders.
* STRG+NVDA+2: StreamBezeichnung.
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

Folgende Befehle stehen zur Verfügung:

* A: Automatisierung.
* C (Shift+C in JAWS layout): Title for the currently playing track.
* C (JAWS layout): Toggle cart explorer (playlist viewer only).
* D (R in der JAWS-Darstellung): Restdauer der Playlist (wenn eine
  Fehlermeldung angezeigt wird, wechseln Sie zum Playlist-Viewer und geben
  Sie diesen Befehl ein).
* E: Metadata streaming status.
* Umschalt+1 bis 4, Umschalt+0: Status für einzelne Metadaten-Streaming-URLs
  (0 ist für DSP-Encoder).
* F: Titel suchen (nur im Playlist-Viewer).
* H: Dauer der Titel in dieser Stunde.
* Umschalt+H: Verbleibende Spieldauer für den Stundenplatzhalter.
* I (L in JAWS layout): Listener count.
* K: springt zum Lesezeichentitel (nur im Playlist-Viewer).
* Strg+K: Aktuellen Titel als Lesezeichentitel setzen (nur im
  Playlist-viewer).
* L (Shift+L in JAWS layout): Line in.
* M: Mikrofon.
* N: Titel der nächst geplante Datei.
* P: Wiedergabestatus (Wiedergabe oder angehalten).
* Umschalt+P: Pitch des aktuellen Titels.
* R (Shift+E in JAWS layout): Record to file enabled/disabled.
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
* Umschalt+F1: Öffnet das Online-Benutzerhandbuch.

## SPL-Controller

Der SPL-Controller bietet eine Befehlsschicht, mit der Sie SPL-Studio von
überall steuern können. Drücken Sie den Befehl für die SPL-Controller
-Befehlsschicht und NVDA wird "SPL-Controller." ansagen. Drücken Sie einen
anderen Befehl, um verschiedene Studio-Funktionen auszuführen (z.B. Mikrofon
ein/aus oder nächsten Titel abspielen).

Die verfügbaren Befehle für den SPL-Controller sind:

* Drücken Sie P, um den nächsten ausgewählten Titel zu spielen.
* Drücken Sie U, um die Wiedergabe zu Pausieren oder um die Wiedergabe
  fortzusetzen.
* Drücken Sie S, um den Titel mit Ausblendung zu stoppen, oder drücken Sie
  T, um den Titel sofort zu stoppen.
* Drücken Sie M oder Umschalt+M, um das Mikrofon ein- bzw. auszuschalten,
  oder drücken Sie N, um das Mikrofon ohne Überblendung zu aktivieren.
* A drücken, um die Automatisierung zu aktivieren, oder Umschalt   A, um es
  auszuschalten.
* Drücken Sie L, um Line-In-Eingang zu aktivieren oder Umschalt  +L, um ihn
  zu deaktivieren.
* Drücken Sie R, um die verbleibende Zeit für den aktuell abgespielten Titel
  zu hören.
* Drücken Sie Umschalt+R, um einen Bericht über den Fortschritt des
  Bibliothek-Scans zu erhalten.
* Drücken Sie C, um den Namen und die Dauer des aktuell abgespielten Titels
  zu hören.
* Drücken Sie Umschalt+C, um den Namen und die Dauer des nächsten Titels,
  falls vorhanden, zu erhalten.
* Drücken Sie E, um zu hören, welche Encoder verbunden sind.
* Drücken Sie I, um die Anzahl der Zuhörer zu ermitteln.
* Drücken Sie Q, um verschiedene Statusinformationen über Studio zu
  erhalten, z. B. ob ein Titel wiedergegeben wird, das Mikrofon
  eingeschaltet ist und mehr.
* Drücken Sie die Cart-Tasten (z.B. F1, STRG+1), um die zugewiesenen Carts
  von überall zu spielen.
* Drücken Sie die Taste H, um einen Hilfe-Dialog anzuzeigen, in dem die
  verfügbaren Befehle aufgelistet sind.

## Track and microphone alarms

By default, NVDA will play a beep if five seconds are left in the track
(outro) and/or intro, as well as to hear a beep if microphone has been
active for a while. To configure track and microphone alarms, press
Alt+NVDA+1 to open alarms settings in Studio add-on settings screen. You can
also use this screen to configure if you'll hear a beep, a message or both
when alarms are turned on.

## Titelfinder

Wenn Sie schnell einen Song nach Interpreten oder Titelbezeichnung aus der
Titelliste finden möchten, drücken Sie STRG+NVDA+F. Geben Sie den Namen des
Interpreten oder den Namen des Titels ein oder wählen Sie ihn aus. NVDA wird
den Cursor entweder beim gefundenen Titel platzieren oder einen Fehler
anzeigen, wenn der gesuchte Titel nicht gefunden wurde. Um einen zuvor
eingegebenen Titel oder Interpreten zu finden, drücken Sie NVDA+F3 oder
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

By pressing Control+NVDA+1 through 0, you can obtain contents of specific
columns. By default, these are first ten columns for a track item (in
Studio: artist, title, duration, intro, outro, category, year, album, genre,
mood). For playlist editor in Creator and Remote VT client, column data
depends on column order as shown on screen. In Studio, Creator's main track
list, and Track Tool, column slots are preset regardless of column order on
screen and can be configured from add-on settings dialog under columns
explorer category.

## Playlist-Statistiken

Sie können im SPL-Assistenten F8 drücken, während Sie sich auf eine
Wiedergabeliste in Studio konzentrieren, um verschiedene Statistiken über
eine Wiedergabeliste zu erhalten. Die Statistik beinhaltet beispielsweise
die Anzahl der Titel, der längste Titel, der beste Interpret und so
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

Aus dem Studio-Fenster können Sie Alt+NVDA+0 drücken, um den
Konfigurationsdialog der NVDA-Erweiterung zu öffnen. Alternativ können Sie
auch das Einstellungsmenü von NVDA aufrufen und den Punkt Einstellungen für
SPL-Studio auswählen. Dieser Dialog dient auch zur Verwaltung von
Broadcast-Profilen.

## Broadcast profiles dialog

You can save settings for specific shows into broadcast profiles. These
profiles can be managed via SPL broadcast profiles dialog which can be
accessed by pressing Alt+NVDA+P from Studio window.

## SPL-Touchmodus

Wenn Sie Studio auf einem Touchscreen-Computer mit Windows 8 oder höher
verwenden und NVDA 2012.3 oder höher installiert haben, können Sie einige
Studio-Befehle über den Touchscreen ausführen. Tippen Sie zunächst einmal
mit drei Fingern, um in den SPL-Touchmodus zu wechseln. Verwenden Sie dann
die oben aufgeführten Touch-Befehle, um Befehle auszuführen.

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.
* Fixed many instances of encoders support feature messages spoken in
  English despite translated into other languages.
* Time-based broadcast profiles feature has been removed.
* Window-Eyes command layout for SPL Assistant has been removed. Window-Eyes
  command layout users will be migrated to NVDA layout.
* As audio ducking feature in NVDA does not impact streaming from Studio
  except for specific hardware setups, audio ducking reminder dialog has
  been removed.
* When errors are found in encoder settings, it is no longer necessary to
  switch to Studio window to let NVDA reset settings to defaults. You must
  now switch to an encoder from encoders window to let NVDA reset encoder
  settings.
* The title of encoder settings dialog for SAM encoders now displays encoder
  format rather than encoder position.

## Version 20.05

* Initial support for Remote VT (voice track) client, including remote
  playlist editor with same commands as Creator's playlist editor.
* Commands used to open separate alarm settings dialogs (Alt+NVDA+1,
  Alt+NVDA+2, Alt+NVDA+4) has been combined into Alt+NvDA+1 and will now
  open alarms settings in SPL add-on settings screen where track outro/intro
  and microphone alarm settings can be found.
* In triggers dialog found in broadcast profiles dialog, removed the user
  interface associated with time-based broadcast profiles feature such as
  profile switch day/time/duration fields.
* Profile switch countdown setting found in broadcast profiles dialog has
  been removed.
* As Window-Eyes is no longer supported by Vispero since 2017, SPL Assistant
  command layout for Window-Eyes is deprecated and will be removed in a
  future add-on release. A warning will be shown at startup urging users to
  change SPL Assistant command layout to NVDA (default) or JAWS.
* When using Columns Explorer slots (Control+NvDA+number row commands) or
  column navigation commands (Control+Alt+home/end/left arrow/right arrow)
  in Creator and Remote VT client, NVDA will no longer announce wrong column
  data after changing column position on screen via mouse.
* In encoders and Streamer, NVDA will no longer appear to do nothing or play
  error tones when exiting NVDA while focused on something other than
  encoders list without moving focus to encoders first.

## Version 20.04

* Time-based broadcast profiles feature is deprecated. A warning message
  will be shown when first starting Studio after installing add-on 20.04 if
  you have defined one or more time-based broadcast profiles.
* Broadcast profiles management has been split from SPL add-on settings
  dialog into its own dialog. You can access broadcast profiles dialog by
  pressing Alt+NVDA+P from Studio window.
* Due to duplication with Control+NVDA+number row commands for Studio
  tracks, columns explorer commands from SPL Assistant (number row) has been
  removed.
* Changed error message shown when trying to open a Studio add-on settings
  dialog (such as metadata streaming dialog) while another settings dialog
  (such as end of track alarm dialog) is active. The new error message is
  same as the message shown when trying to open multiple NVDA settings
  dialogs.
* NVDA will no longer play error tones or appear to do nothing when clicking
  OK button from Columns Explorer dialog after configuring column slots.
* In encoders, you can now save and reset encoder settings (including stream
  labels) by pressing Control+NVDA+C or Control+NVDA+R three times,
  respectively.

## Version 20.03

* Der Spalten-Explorer liest standardmäßig die ersten zehn Spalten vor
  (bestehende Installationen werden weiterhin die alten Spalten verwenden).
* Die Möglichkeit, den Namen des abspielenden Titels automatisch von anderen
  Orten als Studio aus anzukündigen, wurde entfernt. Diese Funktion, die in
  5.6 als Workaround für Studio 5.1x eingeführt wurde, ist nicht mehr
  funktionsfähig. Benutzer müssen nun den SPL-Controller und/oder den Befehl
  für den Assistenten verwenden, um den Titel des gerade abgespielten Titels
  von überall her zu hören (C).
* Auf Grund der Entfernung der automatischen Ansage des abspielenden Titels
  wurde die Einstellung zur Konfiguration dieser Funktion aus der Kategorie
  Zusatzeinstellungen bzw. Status-Ankündigung entfernt.
* In encoders, NvDA will play connection tone every half a second while an
  encoder is connecting.
* Bei Encodern meldet NVDA nun Meldungen über Verbindungsversuche, bis ein
  Encoder tatsächlich angeschlossen ist. Zuvor stoppte NVDA, wenn ein Fehler
  auftrat.
* A new setting has been added to encoder settings to let NvDA announce
  connection messages until the selected encoder is connected. This setting
  is enabled by default.

## Version 20.02

* Anfängliche Unterstützung für den Playlist-Editor des StationPlaylist
  Creators.
* Es wurden Befehle mit Alt+NVDA+Zahlenreihen hinzugefügt, um verschiedene
  Status-Informationen im Playlist-Editor mitzuteilen. Dazu gehören Datum
  und Uhrzeit für die Wiedergabeliste (1), die Gesamtdauer der
  Wiedergabeliste (2), wann der ausgewählte Titel abgespielt wird (3) sowie
  Rotation und Kategorie (4).
* Während Sie sich im Creator und im Titelwerkzeug auf einen Titel
  konzentrieren (außer im Playlist-Editor des Creators), können Sie durch
  Drücken von Strg+NVDA+Barcode Daten für alle Spalten im Lesemodus anzeigen
  lassen.
* Wenn NVDA ein Titellistenelement mit weniger als zehn Spalten erkennt,
  kündigt NVDA keine Überschriften für nicht vorhandene Spalten mehr an,
  wenn Steuerung+NVDA+Zahlenzeile für Spalte außerhalb des Bereichs gedrückt
  werden.
* Im Creator wird NVDA keine Spalteninformationen mehr ankündigen, wenn die
  Tasten Strg+NVDA+Zahlenreihe gedrückt werden, während man sich auf andere
  Stellen als die Titelliste konzentriert.
* Wenn ein Titel abgespielt wird, meldet NVDA nicht mehr "Kein Titel wird
  abgespielt", wenn Informationen über den aktuellen und nächsten Titel über
  den SPL-Assistenten oder SPL-Controller eingeholt werden.
* Wenn eine Option der Alarm-Meldung (Intro, Outro, Mikrofon) geöffnet ist,
  erscheint NVDA nicht mehr, um nichts zu tun oder einen Fehlerton
  abzuspielen, wenn versucht wird, eine zweite Instanz einer Alarm-Meldung
  zu öffnen.
* Wenn Sie versuchen, über den SPL-Assistenten (F12) zwischen einem aktiven
  Profil und einem Sofortprofil zu wechseln, zeigt NVDA eine Meldung an,
  wenn Sie versuchen, dies zu tun, während der Bildschirm mit den
  Zusatzeinstellungen geöffnet ist.
* Beim Neustarten von NVDA werden keine Verbindungston-Einstellung für
  Enkoder mehr vergessen vorzunehmen.

## Version 20.01

* NVDA 2019.3 oder neuer ist auf Grund der umfangreichen Nutzung von Python
  3 erforderlich.

## Version 19.11.1/18.09.13-LTS

* Erste Unterstützung für die StationPlaylist Suite 5.40.
* In Studio führen Wiedergabelistenschnappschüsse (SPL-Assistent, F8) und
  verschiedene Befehle der Zeitansage wie Restzeit (Strg+Alt+T) nicht mehr
  dazu, dass NVDA bei Verwendung von NVDA 2019.3 oder neuer Fehlertöne
  wiedergibt oder verstummt.
* In den Titellistenelementen von Creator wird die Spalte "Sprache", die in
  Creator 5.31 und neuer hinzugefügt wurde, richtig erkannt.
* In verschiedenen Listen im Creator, abgesehen von der Titelliste, wird
  NVDA keine ungeraden Spalteninformationen mehr melden, wenn die
  Tastenkombination Strg+NVDA+Zahlenreihe gedrückt wird.

## Version 19.11

* Der Encoder-Statusbefehl der SPL-Steuerung (E) meldet den
  Verbindungsstatus für den aktiven Encodersatz, anstatt dass Encoder im
  Hintergrund überwacht werden.
* NVDA gibt beim Start keine Fehlertöne mehr wieder, während ein
  Encoder-Fenster im Vordergrund sich befindet.

## Version 19.10/18.09.12-LTS

* Die Versionsankündigungsnachricht für Studio wurde beim Starten gekürzt.
* Versionsinformationen für Creator werden beim Start ausgegeben.
* 19.10: Eine benutzerdefinierte Tastenkombination kann für den
  Encoder-Status vom SPL-Steuerung (E) zugewiesen werden, so dass er von
  überall her verwendet werden kann.
* Erste Unterstützung für AltaCast Encoder (Winamp Plugin und muss vom
  Studio erkannt werden). Die Befehle sind identisch mit dem SPL Encoder.

## Version 19.08.1

* In SAM-Enkodern wurde das Problem behoben, dass NVDA nichts zu tuhn
  scheint oder Fehlertöne abspielt, wenn ein Encoder-Eintrag  gelöscht wird,
  während dieser im Hintergrund beobachtet wird.

## Version 19.08/18.09.11-LTS

* 19.08: NVDA 2019.1 oder höher ist erforderlich.
* 19.08: Das Problem, dass NVDA nichts zu tuhn scheint oder Fehlertöne
  abspielt, wurde behoben, wenn es bei geöffnetem Studio-Einstellungsdialog
  der Erweiterung neu gestartet wird.
* NVDA merkt sich profilspezifische Einstellungen beim Wechseln zwischen den
  Einstellungsbereichen, auch nachdem das aktuell ausgewählte
  Broadcast-Profil aus den Add-On-Einstellungen umbenannt wurde.
* NVDA wird nicht mehr vergessen, Änderungen an zeitbasierten Profilen zu
  berücksichtigen, wenn die Schaltfläche OK gedrückt wird, um die
  Erweiterungs-Einstellungen zu schließen. Dieser Fehler ist seit der
  Migration zu mehrseitigen Einstellungen im Jahr 2018 vorhanden.

## Version 19.07/18.09.10-LTS

* Die Erweiterung wurde von "StationPlaylist Studio" in "StationPlaylist"
  umbenannt, um die unterstützten Anwendungen und Funktionen besser zu
  beschreiben.
* Verbesserungen der internen Sicherheit.
* Wenn die Einstellungen für Mikrofon-Alarm oder Metadaten-Streaming von den
  Einstellungen der Erweiterung geändert werden, kann NVDA die geänderten
  Einstellungen nicht mehr übernehmen. Dies behebt ein Problem, bei dem der
  Mikrofon-Alarm nicht richtig gestartet oder gestoppt werden konnte, nach
  dem die Einstellungen über die Zusatz-Einstellungen geändert wurden.

## Version 19.06/18.09.9-LTS

Version 19.06 unterstützt SPL 5.20 und neuer.

* Erstmalige Unterstützung für StationPlaylist.
* Wenn beim Ausführen verschiedener Studio-Anwendungen wie Titelwerkzeug und
  Studio eine zweite Instanz der Anwendung gestartet und dann beendet wird,
  führt NVDA nicht mehr dazu, dass Studio-Konfigurationsroutinen der
  Erweiterung Fehler verursachen und nicht mehr ordnungsgemäß funktionieren.
* Bezeichnungen für verschiedene Optionen im Konfigurationsdialog des
  SPL-Encoders hinzugefügt.

## Version 19.04.1

* Mehrere Probleme mit neu gestalteten Spaltenansagen und
  Playlist-Transkripten in den Einstellungen der Erweiterung behoben,
  einschließlich Änderungen an der benutzerdefinierten Spaltenreihenfolge
  und inklusiv, die beim Speichern und/oder Umschalten zwischen den Panels
  nicht berücksichtigt wurden.

## Version 19.04/18.09.8-LTS

* Verschiedene globale Befehle wie die Eingabe des SPL-Steuerung und die
  Umschaltung auf das Studio-Fenster werden deaktiviert, wenn NVDA im
  sicheren Modus oder als Windows Store-Anwendung ausgeführt wird.
* 19.04: In Spaltenansagen und Playlist-Transkriptfeldern (Einstellungen der
  ERweiterung) werden benutzerdefinierte
  Spalteneinschluss-/Reihenfolgesteuerelemente im Vordergrund sichtbar sein,
  anstatt eine Schaltfläche auswählen zu müssen, um einen Dialog zum
  Konfigurieren dieser Einstellungen zu öffnen.
* Im Creator spielt NVDA keinen Fehlerton mehr ab oder scheint nichts zu
  passieren, wenn man sich auf bestimmte Listen konzentriert.

## Version 19.03/18.09.7-LTS

* Wenn Sie Strg+NVDA+R drücken, um gespeicherte Einstellungen neu zu laden,
  werden nun auch die Einstellungen der SPL-Erweiterung neu geladen, und
  wenn Sie diesen Befehl dreimal drücken, werden auch diese Einstellungen
  auf die Standard-Einstellungen zusammen mit den NVDA-Einstellungen
  zurückgesetzt.
* Der Dialog "Erweiterungseinstellungen für Studio" im Bereich "Erweiterte
  Optionen" wurde in "Erweitert" umbenannt.
* 19.03 experimental: in column announcements and playlist transcripts
  panels (add-on settings), custom column inclusion/order controls will be
  visible up front instead of having to select a button to open a dialog to
  configure these settings.

## Version 19.02

* Die eigenständige Aktualisierungsprüfung wurde entfernt, einschließlich
  des Update-Check-Befehls aus dem SPL-Assistenten (STRG+Umschalt+U). Auch
  die aktualisierungsprüfung aus den Einstellungen der Erweiterung wurde
  entfernt. Die Überprüfung nach Aktualisierungen wird nun vom Updater für
  Erweiterungen durchgeführt.
* NVDA scheint nichts mehr zu unternehmen oder einen Fehlerton abzuspielen,
  wenn das aktive Intervall des Mikrofons eingestellt ist, um die Sender
  daran zu erinnern, dass das Mikrofon aktiv ist und dabei periodische
  Pieptöne sendet.
* Beim Zurücksetzen von den Einstellungen der Erweiterung aus dem Dialogfeld
  Zurücksetzen von den Einstellungen der Erweiterung fragt NVDA erneut, ob
  ein Sofortwechselprofil oder ein zeitbasiertes Profil aktiv ist.
* Nach dem Zurücksetzen der Einstellund der Studio-Erweiterung schaltet NVDA
  das Mikrofonalarm aus und meldet den Metadaten-Streaming-Status, ähnlich
  wie nach dem Umschalten zwischen den Broadcast-Profilen.

## Version 19.01.1

* NVDA wird nach dem Schließen von Studio "Bibliotheks-Scan wird überwacht"
  nicht mehr ankündigen.

## Version 19.01/18.09.6-LTS

* NVDA 2018.4 oder höher ist erforderlich.
* Weitere Code-Änderungen, um die Erweiterung mit Python 3 kompatibel zu
  machen.
* 19.01: Einige Meldungs-Übersetzungen aus dieser Erweiterung werden
  NVDA-Meldungen ähneln.
* 19.01: Die Prüfung auf  Updates für diese Erweiterung ist nicht mehr
  verfügbar. Eine Fehlermeldung wird angezeigt, wenn Sie versuchen,
  Steuerung+Umschalt +u zu verwenden, um nach Updates zu suchen. Für
  zukünftige Updates verwenden Sie bitte die Erweiterung Addon-Updater.
* Leichte Leistungsverbesserungen bei der Verwendung von NVDA mit anderen
  Anwendungen als Studio, während der Aufnahmerekorder aktiv ist. NVDA zeigt
  immer noch Performance-Probleme, wenn man Studio selbst mit Voice Track
  Recorder aktiv nutzt.
* In Encodern wird NVDA, wenn ein Encoder-Einstellungsdialog geöffnet ist
  (Alt+NVDA+0), eine Fehlermeldung ausgeben, wenn versucht wird, einen
  anderen Encoder-Einstellungsdialog zu öffnen.

## Version 18.12

* Interne Änderungen, um die Erweiterung besser mit zukünftigen
  NVDA-Versionen kompatibel zu machen.
* Viele Beispiele von Meldungen der Erweiterung wurden auf englisch
  ausgesprochen, obwohl sie in andere Sprachen übersetzt wurden. Dieses
  Problem ist nun gelöst.
* Bei der Suche nach Aktualisierungen für die Erweiterung über den
  SPL-Assistenten (SPL-Assistent, Steuerung+Umschalt+U) wird NVDA keine
  neuen Erweiterungsversionen installieren, wenn diese eine neuere Version
  von NVDA erfordern.
* Einige Tastaturbefehle im SPL-Assistenten erfordern nun, dass der
  Playlistviewer sichtbar ist und mit mindestens einer Wiedergabeliste
  gefüllt ist. In einigen Fällen wird ein Titel fokussiert. Zu den
  betroffenen Tastaturbefehlen gehören die Ansage der verbleibende Dauer
  (D), Playlist-Statistiken (F8) und Transkripte von Wiedergabelisten
  (Umschalt+F8).
* Der Befehl für die Ansage der Restlaufzeit der Wiedergabeliste
  (SPL-Assistent, D) erfordert nun, dass ein Titel aus dem Playlistviewer
  fokussiert wird.
* In SAM Encodern können Sie nun mit Hilfe von Tabellen-Navigationsbefehlen
  (Steuerung+Alt+Pfeiltasten) verschiedene Statusinformationen zum Encoder
  einsehen.

## Version 18.11 / 18.09.5-LTS

Hinweis: Version 18.11.1 ersetzt 18.11, um eine solidere Studio
5.31-Unterstützung zu bieten.

* Erstmalige Unterstützung für StationPlaylist Studio 5.31.
* Sie können nun Playlist-Statistiken (SPL-Assistent: f8) und
  Playlist-Transkripte (SPL-Assistent: Umschalt+f8) erstellen, während eine
  Playlist geladen ist, auch wenn der erste Titel nicht fokussiert ist.
* NVDA ist aktiv und spielt keine Fehlertöne mehr ab, wenn versucht wird den
  Metadaten-Streaming-Status beim starten von Studio zu erhalten. Dies gilt
  nur bei entsprechender Einstellung.
* Wenn die Ansage der Statusinformationen des Metadaten-Streamings beim
  Starten des Studio im Einstellungsdialog der Erweiterung aktiviert ist,
  kommen sich diese Ansage und die Ansage anderer Änderungen in der
  Statusleiste nicht mehr in die Quere.

## Version 18.10.2 / 18.09.4-LTS

* Es wurde ein Fehler behoben, dass der Bildschirm mit den Einstellungen der
  Erweiterung nicht geschlossen werden konnte, wenn auf den Schalter
  "Übernehmen" gedrückt und anschließend auf "OK" oder "Abbrechen" gedrückt
  wurde.

## Version 18.10.1 / 18.09.3-LTS

* Mehrere Probleme im Zusammenhang mit der Ansage-Funktion für die
  Encoderverbindung wurden behoben, darunter das Verzichten auf
  Statusmeldungen, das Nichtwiedergeben des ersten ausgewählten Tracks oder
  das Wechseln zum Studio-Fenster, wenn eine Verbindung besteht. Diese
  Fehler werden durch wxPython 4 (NVDA 2018.3 oder höher) verursacht.

## Version 18.10

* NVDA 2018.3 oder höher ist erforderlich.
* Interne Änderungen, um die Erweiterung besser mit Python 3 kompatibel zu
  machen.

## Version 18.09.1-LTS

* Wenn Sie Playlist-Transkripte im HTML-Tabellenformat erhalten, werden
  Spaltenüberschriften nicht mehr als Python-Listenzeichenfolge dargestellt.

## Version 18.09-LTS

Version 18.09.x ist die letzte Release-Reihe, die Studio 5.10 unterstützt
und auf alten Technologien basiert, mit 18.10 und später Studio 5.11/5.20
und neuen Features. Einige neue Features werden bei Bedarf auf 18.09.x
zurückportiert.

* NVDA 2018.3 oder höher wird auf Grund der Einführung von wxPython 4
  empfohlen.
* Der Bildschirm für die zusätzlichen Einstellungen basiert nun vollständig
  auf einer mehrseitigen Schnittstelle, die von NVDA 2018.2 und höher
  abgeleitet wurde.
* Die schnellen und langsamen Ringe der Testkanäle wurden zum Kanal
  "Entwicklung" kombiniert, mit einer Option für Benutzer von
  Entwicklungs-Snapshots zum Testen von Pilotfunktionen, indem das
  Kontrollkästchen für neue Pilotfunktionen aktiviert wird, das sich im
  Fenster Erweiterte Zusatzeinstellungen befindet. Benutzer, die zuvor am
  Testkanal Schneller Ring waren, werden weiterhin Pilotfunktionen testen.
* Die Möglichkeit, verschiedene Update-Kanäle der Erweiterungen aus den
  Einstellungen der Erweiterung auszuwählen, wurde entfernt. Benutzer, die
  auf einen anderen Release-Kanal wechseln möchten, sollten die
  Community-Website für NVDA-Erweiterungen besuchen
  (addons.nvda-project.org), StationPlaylist Studio auswählen und dann die
  entsprechende Version herunterladen.
* Die Kontrollkästchen für die Spaltenansage und die Transkription von
  Wiedergabelisten sowie die Kontrollkästchen für Metadatenströme wurden in
  überprüfbare Listensteuerelemente umgewandelt.
* Beim Umschalten zwischen den Einstellungsfeldern speichert NVDA die
  aktuellen Einstellungen für profilspezifische Einstellungen (Alarm-,
  Spaltenansagen, Metadaten-Streaming-Einstellungen, etc.).
* CSV-Format (kommagetrennte Werte) als Format für
  Wiedergabelistentranskripte hinzugefügt.
* Wenn Sie zum Speichern der Einstellungen Strg+NVDA+C drücken, werden nun
  auch die Einstellungen der Erweiterung gespeichert (erfordert NVDA
  2018.4).

## Ältere Versionen

Für weitere Änderungsnotizen beachten Sie den Link zu den Änderungsnotizen
älterer Erweiterungsversionen.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
