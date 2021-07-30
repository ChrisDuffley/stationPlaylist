# StationPlaylist #

* Autoren: Geoff Shang, Joseph Lee und weitere Mitwirkende
* [Stabile Version herunterladen][1]
* NVDA-Kompatibilität: 2020.4 und neuer

Dieses Zusatzpaket bietet eine verbesserte Nutzung von StationPlaylist
Studio und anderen StationPlaylist-Anwendungen sowie Dienstprogramme zur
Steuerung von Studio von überall. Zu den unterstützten Anwendungen gehören
Studio, Creator, Track Tool, VT Recorder und Streamer sowie SAM, SPL und
AltaCast Encoder.

Weitere Informationen zur Erweiterung finden Sie in der
[Add-On-Anleitung][2].

WICHTIGE HINWEISE:

* Diese Erweiterung unterstützt die StationPlaylist Suite 5.30 oder neuer.
* Wenn Sie Windows 8 oder höher verwenden, setzen Sie die Reduzierung der
  Lautstärke anderer Audioquellen auf "nie" im Dialog Sprachausgabe im
  NVDA-Einstellungsmenü.
* Seit 2018 sind [Änderungsprotokolle für alte Releases der Erweiterung][3]
  auf GitHub zu finden. Die Readme der Erweiterung listet Änderungen ab
  Version 20.09 (2020) auf.
* Während die Studio-Software läuft, können Sie gespeicherte Einstellungen
  speichern, wieder laden oder Zusatzeinstellungen auf die Standardwerte
  zurücksetzen, indem Sie Strg+NVDA+C, Strg+NVDA+R einmal bzw. Strg+NVDA+R
  dreimal drücken. Dies gilt auch für die Encoder-Einstellungen - Sie können
  Encoder-Einstellungen speichern und zurücksetzen (nicht neu laden), wenn
  Sie Encoder verwenden.

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
* Alt+NVDA+1 (im SPL-Modus mit zwei Fingern nach rechts wischen) aus dem
  Studio-Fenster: Öffnet die Kategorie Alarm-Einstellungen im
  Studio-Zusatzkonfigurationsfenster.
* Alt+NVDA+1 aus dem Playlist-Editor des Creators und dem
  Remote-VT-Playlist-Editor: Meldet die geplante Zeit für die
  Wiedergabeliste.
* Alt+NVDA+2 aus dem Playlist-Editor des Creators und dem
  Remote-VT-Playlist-Editor: Meldet die Gesamtdauer der Wiedergabeliste.
* Alt+NVDA+3 aus dem Studio-Fenster: legt den Cart-Explorer fest, um die
  Zuordnung von Carts zu lernen.
* Alt+NVDA+3 aus dem Playlist-Editor des Creators und dem
  Remote-VT-Playlist-Editor: Zeigt an, wann die Wiedergabe des ausgewählten
  Titels geplant ist.
* Alt+NVDA+4 aus dem Playlist-Editor des Creators und dem
  Remote-VT-Playlist-Editor: Meldet die Rotation und die Kategorie, die mit
  der die Wiedergabeliste verbunden ist.
* STRG+NVDA+f aus dem Studio-Fenster: Öffnet einen Dialog, um einen Titel
  basierend auf Künstler oder Titelbezeichnung zu finden. Drücken Sie
  NVDA+F3, um vorwärts zu suchen oder NVDA+Umschalt+F3, um rückwärts zu
  suchen.
* Alt+NVDA+R aus dem Studio-Fenster: Benachrichtigungseinstellungen für
  Bibliothek-Scans.
* Strg+Umschalt+X aus dem Studio-Fenster: Braille-Timer-Einstellungen.
* Strg+Alt+Pfeil links/rechts (während der Fokus auf einer Spur in Studio,
  Creator, Remote-Voice-Tracking und Track-Tool liegt): Zur
  vorherigen/nächsten Track-Spalte wechseln.
* Strg+Alt+Pos1/Ende (während der Fokus auf einem Track in Studio, Creator,
  Remote-Voice-Tracking und Track-Tool liegt): Zur ersten/letzten
  Track-Spalte wechseln.
* Strg+Alt+Pfeil nach oben/unten (während der Fokus auf einem Track in
  Studio, Creator, Remote-Voice-Tracking und Track-Tool liegt): Zum
  vorherigen/nächsten Track gehen und bestimmte Spalten ansagen.
* Strg+NVDA+1 bis 0 (während der Fokus auf einem Track in Studio, Creator
  (einschließlich im Playlist-Editor), Remote-VT und Track Tool liegt):
  Spalteninhalt für eine bestimmte Spalte ankündigen (standardmäßig die
  ersten zehn Spalten). Wenn Sie diesen Befehl zweimal drücken, werden die
  Spalteninformationen in einem Fenster im Blätternmodus angezeigt.
* Strg+NVDA+- (Bindestrich bei Fokussierung auf eine Spur in Studio,
  Creator, Remote-Voice-Tracking und Track-Tool): Anzeige der Daten für alle
  Spalten einer Spur im Lesemodus.
* NVDA+V bei Fokussierung auf einen Titel (nur für den
  Wiedergabelisten-Betrachter von Studio): Schaltet die Ansage der
  Titelspalte zwischen Bildschirmreihenfolge und benutzerdefinierter
  Reihenfolge um.
* Alt+NVDA+C während der Fokus auf einem Titel steht, (nur
  Studio-Playlistenbetrachter): werden Titel-Kommentare falls vorhanden
  gemeldet.
* Alt+NVDA+0 aus dem Studio-Fenster: Öffnet den Konfigurationsdialog der
  SPL-Erweiterung.
* Alt+NVDA+P aus dem Studio-Fenster: Öffnet die Studio-Sendeprofile.
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

* F9: Den ausgewählten Encoder verbinden.
* F10 (nur gleicher Encoder): Trennt den ausgewählten Encoder.
* Strg+F9: Verbindet alle Encoder.
* Strg+F10 (nur SAM-Encoder): Alle Encoder trennen.
* F11: legt fest, ob NVDA zum Studio-Fenster für den ausgewählten Encoder
  wechseln soll, wenn dieser angeschlossen ist.
* Shift+F11: legt fest, ob Studio den ersten ausgewählten Titel abspielen
  soll, wenn der Encoder an einen Streaming-Server angeschlossen ist.
* Control+F11: Schaltet die Hintergrundüberwachnung des ausgewählten
  Encoders ein- und aus.
* Strg+F12: Öffnet ein Dialogfeld zur Auswahl des ausgelöschten Encoders
  (zur Neuausrichtung der Encoder-Beschreibung und Einstellungen).
* Alt+NVDA+0 und F12: Öffnet das Dialogfeld für Encodereinstellungen zur
  Konfiguration von Optionen wie z. B. Encoder-Beschreibungen.

Darüber hinaus stehen folgende Befehle für den Spaltenexplorer zur
Verfügung:

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

Folgende Befehle stehen zur Verfügung:

* A: Automatisierung.
* C (Umschalt+C im JAWS-Layout): Name des aktuell abgespielten Titels.
* C (JAWS-Layout): Cart-Explorer umschalten (nur in der Ansicht der
  Wiedergabelisten).
* D (R in der JAWS-Darstellung): Restdauer der Playlist (wenn eine
  Fehlermeldung angezeigt wird, wechseln Sie zum Playlist-Viewer und geben
  Sie diesen Befehl ein).
* E: Metadaten-Streaming-Status.
* Umschalt+1 bis 4, Umschalt+0: Status für einzelne Metadaten-Streaming-URLs
  (0 ist für DSP-Encoder).
* F: Titel suchen (nur im Playlist-Viewer).
* H: Dauer der Titel in dieser Stunde.
* Umschalt+H: Verbleibende Spieldauer für den Stundenplatzhalter.
* I (L im JAWS-Layout): Anzahl der Zuhörer.
* K: springt zum Lesezeichentitel (nur im Playlist-Viewer).
* Strg+K: Aktuellen Titel als Lesezeichentitel setzen (nur im
  Playlist-viewer).
* L (Umschalt+L im JAWS-Layout): Line-In.
* M: Mikrofon.
* N: Titel der nächst geplante Datei.
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
* Umschalt+F1: Öffnet das Online-Benutzerhandbuch.

## SPL-Controller

Der SPL-Controller bietet eine Befehlsschicht, mit der Sie SPL-Studio von
überall steuern können. Drücken Sie den Befehl für die SPL-Controller
-Befehlsschicht und NVDA wird "SPL-Controller." ansagen. Drücken Sie einen
anderen Befehl, um verschiedene Studio-Funktionen auszuführen (z.B. Mikrofon
ein/aus oder nächsten Titel abspielen).

Die verfügbaren Befehle für den SPL-Controller sind:

* P: Nächsten ausgewählten Titel abspielen.
* U: Wiedergabe anhalten oder fortsetzen.
* S: Titel anhalten mit Ausblenden.
* T: Sofort anhalten.
* M: Mikrofon einschalten.
* Umschalt+M: Mikrofon ausschalten.
* A: Automatisierung einschalten.
* Umschalt+A: Automatisierung ausschalten.
* L: Line-In-Eingang einschalten.
* Umschalt+L: Line-In-Eingang ausschalten.
* R: Restzeit für den aktuell wiedergegebenen Titel.
* Umschalt+R: Fortschritt des Bibliotheksscans.
* C: Titel und Dauer des aktuell wiedergegebenen Titels.
* Umschalt+C: Titel und Dauer des nachfolgenden Titels, falls vorhanden.
* E: Verbindungsstatus des Encoders.
* I: Zuhörer zählen.
* F: Studio-Statusinformationen, z. B. ob ein Titel abgespielt wird, das
  Mikrofon eingeschaltet ist und weitere.
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

Aus dem Studio-Fenster können Sie Alt+NVDA+0 drücken, um den
Konfigurationsdialog der NVDA-Erweiterung zu öffnen. Alternativ können Sie
auch das Einstellungsmenü von NVDA aufrufen und den Punkt Einstellungen für
SPL-Studio auswählen. Dieser Dialog dient auch zur Verwaltung von
Broadcast-Profilen.

## Dialogfeld der Sendeprofile

Sie können Einstellungen für bestimmte Sendungen in Sendeprofilen
speichern. Diese Profile können über das Dialogfeld SPL-Sendeprofile
verwaltet werden, auf das durch Drücken von Alt+NVDA+P im Studio-Fenster
zugegriffen werden kann.

## SPL-Touchmodus

Wenn Sie Studio auf einem Touchscreen-Computer mit Windows 8 oder höher
verwenden und NVDA 2012.3 oder höher installiert haben, können Sie einige
Studio-Befehle über den Touchscreen ausführen. Tippen Sie zunächst einmal
mit drei Fingern, um in den SPL-Touchmodus zu wechseln. Verwenden Sie dann
die oben aufgeführten Touch-Befehle, um Befehle auszuführen.

## Version 21.08

* In SAM encoders, NVDA will no longer play a tone if the selected encoder
  becomes idle as this tone is really meant to help when debugging the
  add-on.

## Version 21.06

* NVDA wird beim Versuch, verschiedene Dialogfelder der Erweiterung wie den
  Encoder-Einstellungsdialog zu öffnen, nichts mehr tun oder Fehlertöne
  abspielen. Dies ist ein kritischer Fix, der für die Unterstützung von NVDA
  2021.1 erforderlich ist.
* NVDA scheint nichts mehr zu unternehmen oder Fehlertöne abzuspielen, wenn
  versucht wird, die vollständige Zeit (Stunden, Minuten, Sekunden) von
  Studio aus anzukündigen (Befehl nicht zugewiesen). Dies betrifft NVDA
  2021.1 oder neuer.

## Version 21.04/20.09.7-LTS

* 21.04: NVDA 2020.4 oder neuer ist erforderlich.
* In Encodern schlägt die Ansage von Datum und Uhrzeit beim drücken von
  NVDA+F12 nicht mehr fehl. Dies betrifft NVDA 2020.1 und neuer.

## Version 21.03/20.09.6-LTS

* Die Mindestanforderungen für Windows-Versionen sind jetzt an
  NVDA-Versionen gebunden.
* Der Befehl für Feedback per E-Mail (Alt+NVDA+Bindestrich) wurde
  entfernt. Bitte senden Sie Feedback an Add-On-Entwickler unter Verwendung
  der Kontaktinformationen, die in der Verwaltung der Erweiterungen
  bereitgestellt werden.
* 21.03: Teile des Quellcodes der Erweiterung enthalten nun Typ-Anmerkungen.
* 21.03: Der Code der Erweiterung wurde mit Hilfe von Mypy (einem statischen
  Python-Typ-Prüfer) robuster. Insbesondere wurden einige langjährige Fehler
  behoben, z. B., dass NVDA unter bestimmten Umständen die Einstellungen der
  Erweiterung nicht auf die Standardeinstellungen zurücksetzen konnte und
  versuchte, die Encodereinstellungen zu speichern, wenn sie nicht geladen
  waren. Einige bekannte Fehlerkorrekturen wurden ebenfalls auf 20.09.6-LTS
  zurückportiert.
* Es wurden zahlreiche Fehler mit dem Begrüßungsdialog hinzugefügt
  (Alt+NVDA+F1 aus dem Studio-Fenster heraus), einschließlich der Anzeige
  mehrerer Begrüßungsdialoge und der Tatsache, dass NVDA scheinbar nichts
  macht oder Fehlertöne ausgibt, wenn der Begrüßungsdialog nach dem Beenden
  von Studio geöffnet bleibt.
* Es wurden zahlreiche Fehler im Dialogfeld "Titelkommentare" behoben
  (Alt+NVDA+C dreimal von einem Titel in Studio), einschließlich eines
  Fehlertons beim Speichern von Kommentaren und vieler Dialogfelder für
  Titelkommentare, die angezeigt werden, wenn Alt+NVDA+C mehrmals gedrückt
  wird. Wenn das Dialogfeld "Kommentare verfolgen" nach dem Schließen von
  Studio weiterhin angezeigt wird, werden Kommentare nicht gespeichert.
* Verschiedene Spaltenbefehle wie der Spalten-Explorer
  (Strg+NVDA+Zahlenreihe) in Studio-Spuren und Ankündigungen des
  Encoder-Status führen nicht mehr zu fehlerhaften Ergebnissen, wenn sie
  nach dem Neustart von NVDA ausgeführt werden, während sie sich auf Spuren
  oder Encoder konzentrieren. Dies betrifft NVDA 2020.4 oder höher.
* Es wurden zahlreiche Probleme mit Wiedergabelisten-Snapshots
  (SPL-Assistent, F8) behoben, einschließlich der Umstand, Snapshot-Daten
  abzurufen und falsche Tracks als kürzeste oder längste Tracks zu melden.
* NVDA meldet nun nicht mehr "0 Elemente in der Bibliothek", wenn Studio
  mitten in einem Scan-Vorgan der Bibliothek beendet wird.
* NVDA konnte Änderungen an den Encoder-Einstellungen nicht mehr speichern,
  nachdem beim Laden selbiger Fehler aufgetreten sind und die Einstellungen
  anschließend auf die Standardeinstellungen zurückgesetzt werden.

## Version 21.01 / 20.09.5-LTS

Version 21.01 unterstützt SPL Studio 5.30 und neuer.

* 21.01: NVDA 2020.3 oder neuer ist erforderlich.
* 21.01: Die Einstellung für die Einbeziehung von Spaltenüberschriften aus
  den Einstellungen der Erweiterung wurde entfernt. Die NVDA-eigene
  Einstellung für Tabellenspaltenüberschriften steuert die Ankündigungen von
  Spaltenüberschriften für SPL-Suite und Encoder.
* Es wurde ein Befehl zum Umschalten des Bildschirms gegenüber der
  benutzerdefinierten Spalteneinbeziehung und Reihenfolgeeinstellung
  (NVDA+V) hinzugefügt. Beachten Sie, dass dieser Befehl nur verfügbar ist,
  wenn Sie sich auf einen Titel im Wiedergabelisten-Betrachter von Studio
  befinden.
* Die Hilfe zur SPL-Assistenten- und Controller-Layer wird anstelle eines
  Dialogfelds als Dokument im Suchmodus angezeigt.
* NVDA unterbricht die Ansage des Scan-Fortschritts der Bibliothek nicht
  mehr, wenn es so konfiguriert ist, dass der Scan-Fortschritt bei
  Verwendung einer Braillezeile ausgegeben wird.

## Version 20.11.1/20.09.4-LTS

* Erste Unterstützung für die StationPlaylist Suite 5.50.
* Verbesserungen bei der Darstellung verschiedener Dialogfelder der
  Erweiterung dank der Funktionen von NVDA 2020.3.

## Version 20.11/20.09.3-LTS

* 20.11: NVDA 2020.1 oder neuer ist erforderlich.
* 20.11: Mit Flake8 wurden weitere Probleme im Code und potenzielle Fehler
  behoben.
* Verschiedene Probleme mit dem Begrüßungsdialogfeld der Erweiterung
  (Alt+NVDA+F1 aus Studio) wurden behoben, einschließlich des falschen
  Befehls, der für das Add-On-Feedback angezeigt wurde (Alt+NVDA+Hyphen).
* 20.11: Das Spaltenpräsentationsformat für Track- und Encoder-Elemente in
  der gesamten StationPlaylist-Suite (einschließlich SAM-Encoder) basiert
  jetzt auf dem SysListView32-Listenelementformat.
* 20.11: NVDA wird nun Spalteninformationen für Spuren in der gesamten
  SPL-Suite mitteilen, unabhängig von der Einstellung "Objektbeschreibung
  melden" im Einstellungsfenster für die Objektpräsentation von
  NVDA. Behalten Sie nach Möglichkeit diese Einstellung bei.
* 20.11: Im Playlist-Viewer von Studio beeinflussen die benutzerdefinierte
  Spaltenreihenfolge und die Einschlusseinstellung die Art und Weise, wie
  die Trackspalten dargestellt werden, wenn die Objekt-Navigation verwendet
  wird, um sich zwischen den einzlnen titeln zu bewegen, einschließlich der
  Ansage des aktuellen Navigator-Objekts.
* Wenn vertikale Spalten auf einen anderen Wert als die, die gerade geprüft
  wird, eingestellt ist, kündigt NVDA keine falschen Spaltendaten mehr an,
  nachdem die Spaltenposition auf dem Bildschirm mit der Maus geändert
  wurde.
* Verbesserte Darstellung von Wiedergabelisten-Transkripten (SPL-Assistent,
  Umschalt+F8) beim Betrachten des Transkripte im HTML-Tabellen- oder
  Listenformat.
* 20.11: In Encodern werden Encoder-Beschreibungen mitgeteilt, wenn
  Objekt-Navigationsbefehle ausgeführt werden, zusätzlich zum Drücken der
  Auf- oder Ab-Pfeiltasten, um sich zwischen den Encodern zu bewegen.
* Beim Encodern wird durch Drücken von F12 zusätzlich zu
  Alt+NVDA+Zahlenreihe 0 auch das Dialogfeld zur Encoder-Einstellungen für
  den ausgewählten Encoder geöffnet.

## Version 20.10/20.09.2-LTS

* Auf Grund von Änderungen am Datei-Format der Encoder-Einstellungen führt
  die Installation einer älteren Version dieser Erweiterung nach der
  Installation dieser Version zu unvorhersehbarem Verhalten.
* Es ist nicht mehr notwendig, NVDA im Debug-Modus neu zu starten, um
  Debug-Meldungen aus dem Protokoll-Betrachter zu lesen. Sie können
  Debug-Meldungen einsehen, wenn der Log-Level in den allgemeinen
  Einstellungen von NVDA auf "Debug-Meldungen" gesetzt ist.
* Im Playlist-Betrachter von Studio schließt NVDA keine Spaltenüberschriften
  ein, wenn diese Einstellung in den Zusatzeinstellungen deaktiviert ist und
  keine benutzerdefinierten Spaltenreihenfolge- oder Einschlusseinstellungen
  definiert sind.
* 20.10: Die Einstellung zur Aufnahme von Spaltenüberschriften aus den
  Einstellungen der Einstellung ist veraltet und wird in einer zukünftigen
  Version entfernt werden. In Zukunft wird die NVDA-eigene Einstellung der
  Tabellenspaltenüberschriften die Ankündigungen der Spaltenüberschriften in
  der SPL-Suite und den Kodierern steuern.
* Wenn SPL Studio in die Taskleiste (Benachrichtigungsbereich) minimiert
  wird, meldet NVDA diese Tatsache, wenn versucht wird, von anderen
  Programmen entweder über einen dedizierten Befehl oder als Ergebnis einer
  Encoder-Verbindung zum Studio zu wechseln.

## Version 20.09-LTS

Version 20.09.x ist die letzte Version, die Studio 5.20 unterstützt und auf
alten Technologien basiert. Zukünftige Versionen unterstützen Studio 5.30
und neuere NVDA-Funktionen. Einige neue Funktionen werden bei Bedarf auf
20.09.x zurückportiert.

* Auf Grund von Änderungen in NVDA steht der Befehlszeilenparameter
  "--spl-configvolatile" nicht mehr zur Verfügung, um Einstellungen der
  Erweiterung nicht mehr überschreiben zu können. Dies können Sie emulieren,
  indem Sie das Kontrollkästchen "Konfiguration beim Beenden von NVDA
  speichern" in den allgemeinen Einstellungen von NVDA deaktivieren.
* Die Einstellung für Pilotfunktionen wurde aus der Kategorie der Erweiterte
  Einstellungen in den Einstellungen der ERweiterung (Alt+NVDA+0) entfernt,
  damit Benutzer von Entwicklungs-Snapshots den Bleeding-Edge-Code testen
  können.
* Die Befehle für die Spaltennavigation in Studio sind jetzt in Titellisten
  verfügbar, die sich in Höreranfragen, Einfügen von Titeln und anderen
  Bildschirmen befinden.
* Verschiedene Befehle zur Spaltennavigation werden sich wie die
  NVDA-eigenen Befehle zur Tabellennavigation verhalten. Neben der
  Vereinfachung dieser Befehle bringt sie Vorteile wie die
  Benutzerfreundlichkeit für Sehbehinderte mit sich.
* Die Befehle für die vertikale Spaltennavigation (Strg+Alt+Pfeil nach
  oben/unten) stehen jetzt für Creator, Playlist-Editor,
  Remote-Voice-Tracking und im Track-Tool zur Verfügung.
* Der Befehl zum Betrachten von Titelspalten (Strg+NVDA+Hilfsstrich) ist
  jetzt im Playlisten-Editor des Erstellers und in Remote-Voice-Tracking
  verfügbar.
* Der Befehl für den Betrachter der Track-Spalten berücksichtigt nun die auf
  dem Bildschirm angezeigte Spaltenreihenfolge.
* Bei SAM-Encodern wurde das Ansprechverhalten von NVDA beim Drücken von
  Strg+F9 oder Strg+F10 zum Verbinden bzw. Trennen aller Encoder
  verbessert. Dies kann zu einer Verbesserung der Rückmeldungen in den
  ausgewählten Encoder-Informationen führen.
* Bei SPL- und AltaCast-Encodern wird nun durch Drücken von F9 der
  ausgewählte Encoder verbunden.

## Ältere Versionen

Für weitere Änderungsnotizen beachten Sie den Link zu den Änderungsnotizen
älterer Erweiterungsversionen.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[3]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
