# StationPlaylist #

* Autoren: Geoff Shang, Joseph Lee und weitere Mitwirkende
* [Stabile Version herunterladen][1]
* NVDA-Kompatibilität: 2021.2 und neuer

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
* Starting from 2018, [changelogs for old add-on releases][3] will be found
  on GitHub. This add-on readme will list changes from version 21.10 (2021)
  onwards.
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
unten und wählen Sie "Hinzufügen" aus, geben Sie dann die Taste oder
Tastenkombination ein, welche Sie verwenden möchten.

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

## Version 22.01

* If add-on specific command-line switches such as "--spl-configinmemory" is
  specified when starting NVDA, NVDA will no longer add the specified
  parameter each time NVDA and/or Studio runs. Restart NVDA to restore
  normal functionality (without command-line switches).

## Version 21.11

* Initial support for StationPlaylist suite 6.0.

## Version 21.10

* NVDA 2021.2 oder neuer ist erforderlich, da die Änderungen diese
  Erweiterung betreffen.

## Ältere Versionen

Für weitere Änderungsnotizen beachten Sie den Link zu den Änderungsnotizen
älterer Erweiterungsversionen.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[3]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
