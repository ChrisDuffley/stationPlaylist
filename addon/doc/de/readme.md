# StationPlaylist #

* Autoren: Geoff Shang, Joseph Lee und weitere Mitwirkende
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]
* NVDA-Kompatibilität: 2019.3 bis 2020.2

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
* Seit 2018 werden [Änderungen für alte Versionen der Erweiterung][5] auf
  GitHub zu finden sein. Diese Readme-Datei für die Änderungen der
  Erweiterung ab Version 18.09 (ab 2018) auflisten.
* Bestimmte Funktionen sind nicht mehr verfügbar, z.B. während NVDA im
  abgesicherten Modus ausgeführt wird.
* Aufgrund technischer Einschränkungen können Sie diese Erweiterung nicht
  auf der Windows-Store-Version von NVDA installieren oder verwenden.
* Features, die als "experimentell" gekennzeichnet sind, sollen etwas vor
  einer zukünftigen Version testen, sodass sie nicht in stabilen Versionen
  aktiviert werden.
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
* Strg+Alt+Pfeil nach links/rechts (während der Fokus auf einer Spur in
  Studio, Creator, Remote VT und Track Tool liegt): Vorherige bzw. nächste
  Track-Spalte ansagen.
* Strg+Alt+Pos1/Ende (während der Fokus auf einem Track in Studio, Creator,
  Remote-VT und Track Tool liegt): Erste und letzte Track-Spalte ansagen.
* Strg+Alt+Pfeil nach oben/unten (während der Fokus nur auf einen Titel in
  Studio gerichtet ist): Zur vorherigen oder nächsten Spur wechseln und
  bestimmte Spalten mitteilen.
* Strg+NVDA+1 bis 0 (während der Fokus auf einem Track in Studio, Creator
  (einschließlich im Playlist-Editor), Remote-VT und Track Tool liegt):
  Spalteninhalt für eine bestimmte Spalte ankündigen (standardmäßig die
  ersten zehn Spalten). Wenn Sie diesen Befehl zweimal drücken, werden die
  Spalteninformationen in einem Fenster im Blätternmodus angezeigt.
* Strg+NVDA+- (Bindestrich bei Fokussierung auf eine Spur in Studio, Creator
  und Titelwerkzeug): Anzeige der Daten für alle Spalten einer Spur im
  Lesemodus.
* Alt+NVDA+C während der Fokus auf einen Track (nur Studio): Meldet
  Track-Kommentare, falls vorhanden.
* Alt+NVDA+0 aus dem Studio-Fenster: Öffnet den Konfigurationsdialog der
  SPL-Erweiterung.
* Alt+NVDA+P aus dem Studio-Fenster: Öffnet die Studio-Sendeprofile.
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
* Alt+NVDA+0: Öffnet das Dialogfeld der Encoder-Einstellungen, um Optionen
  wie z. B. die Encoder-Beschreibung zu konfigurieren.

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

## Version 20.07

* Im Wiedergabelisten-Viewer von Studio scheint NVDA nicht mehr nichts zu
  tun oder Fehlertöne abzuspielen, wenn versucht wird, Titel zu löschen oder
  nachdem die geladene Wiedergabeliste gelöscht wurde, während der
  Wiedergabelisten-Viewer fokussiert war.
* Bei der Suche nach Tracks im Dialogfeld Tracks einfügen von Studio meldet
  NVDA die Suchergebnisse, wenn Ergebnisse gefunden werden.
* NVDA scheint nicht mehr nichts zu tun oder Fehlertöne wiederzugeben, wenn
  versucht wird, zu einem neu erstellten Sendeprofil zu wechseln und
  Zusatz-Einstellungen zu speichern.
* In den Encoder-Einstellungen wurde die Stream-Beschreibung in
  Encoder-Beschreibung" umbenann.
* Der dedizierter Befehl zur Stream-Beschreibung (F12) wurde aus den
  Encodern entfernt. Encoder-Beschreibungen können in den
  Encoder-Einstellungen definiert werden (Alt+NVDA+0).
* Der Systemfokus bewegt sich nicht mehr wiederholt zu Studio oder die
  ausgewählte Spur wird abgespielt, wenn ein im Hintergrund (Strg+F11)
  überwachter Encoder wiederholt ein- und ausgeschaltet wird.
* Bei SPL-Encodern wurde der Befehl Strg+F9 hinzugefügt, um alle Encoder zu
  verbinden (wie F9).

## Version 20.06

* Mit Flake8 wurden viele Probleme im Code und potenzielle Fehler behoben.
* Viele Fälle, in denen Meldungen der Encoder Features trotz Übersetzung in
  andere Sprachen auf Englisch unterstützt wurden, wurden behoben.
* Die Funktion der zeitbasierten Sendeprofile wurde entfernt.
* Das Befehlslayout von Window-Eyes für den SPL-Assistenten wurde
  entfernt. Benutzer des Befehlslayouts von Window-Eyes werden zum
  NVDA-Layout migriert.
* Da die Funktion zum Reduzieren anderer Audio-Quellen in NVDA das Streaming
  aus Studio nicht beeinflusst, außer bei bestimmten
  Hardware-Konfigurationen, wurde der entsprechende Erinnerungsdialog
  entfernt.
* Wenn Fehler in den Encoder-Einstellungen gefunden werden, ist es nicht
  mehr notwendig, zum Studio-Fenster zu wechseln, damit NVDA die
  Einstellungen auf die Standardwerte zurücksetzen kann. Sie müssen nun vom
  Encoder-Fenster zu einem Encoder wechseln, um NVDA-Encoder-Einstellungen
  zurücksetzen zu lassen.
* Der Titel des Dialogfelds für Enkodereinstellungen für SAM-Enkoder zeigt
  jetzt das Enkoderformat und nicht mehr die Enkoderposition an.

## Version 20.05

* Anfängliche Unterstützung für den Remote-VT-Client (Voice Tracking),
  einschließlich Remote-Playlist-Editor mit denselben Befehlen wie der
  Playlist-Editor des Creators.
* Befehle, die zum Öffnen separater Alarmeinstellungsdialoge (Alt+NVDA+1,
  Alt+NVDA+2, Alt+NVDA+4) verwendet werden, wurden zu Alt+NVDA+1
  zusammengefasst und öffnen nun die Alarm-Einstellungen im
  SPL-Zusatz-Einstellungsbildschirm, wo die Einstellungen für das Intro
  bzw. Abspann des Tracks und Mikrofonalarm gefunden werden können.
* Die Trigger, der in den Sendeprofile gefunden wurde, wurde die
  Benutzeroberfläche entfernt, die mit zeitbasierten Sendeprofilen verbunden
  ist, wie z. B. die Felder für die Profilumschaltung Tag/Uhrzeit/Dauer.
* Die im Dialogfeld für Sendeprofile gefundene Countdown-Einstellung für den
  Profilwechsel wurde entfernt.
* Da Window-Eyes seit 2017 nicht mehr von Vispero unterstützt wird, ist das
  Befehlslayout des SPL-Assistenten für Window-Eyes veraltet und wird in
  einem zukünftigen Release der Erweiterung entfernt werden. Beim Start wird
  eine Warnung angezeigt, indem der Benutzer aufgefordert wird, das
  Befehlslayout des SPL-Assistenten auf NVDA (Standard) oder auf JAWS zu
  ändern.
* Bei der Verwendung des Spalten-Explorers (Strg+NVDA+Ziffernreihe) oder
  Spaltennavigationsbefehlen (Strg+Alt+Pos1/Ende/Pfeil nach links/rechts) im
  Creator und Remote-VT-Client meldet NVDA nach Änderung der Spaltenposition
  auf dem Bildschirm per Maus keine falschen Spaltendaten mehr.
* In Encodern und Streamern scheint NVDA beim Beenden von NVDA nicht mehr
  nichts zu tun oder Fehlertöne abzuspielen, während man sich auf etwas
  anderes als die Encoder-Liste konzentriert, ohne den Fokus zuerst auf die
  Encoder zu richten.

## Version 20.04

* Die Funktion der zeitbasierten Sendeprofile ist veraltet. Wenn Sie ein
  oder mehrere zeitbasierte Sendeprofile definiert haben, wird beim ersten
  Start von Studio nach der Installation der Version 20.04 eine Warnmeldung
  angezeigt.
* Die Verwaltung der Sendeprofile wurde vom SPL-Zusatzeinstellungsdialog in
  einen eigenen Dialog aufgeteilt. Sie können auf die Sendeprofile
  zugreifen, indem Sie Alt+NVDA+P im Studio-Fenster drücken.
* Auf Grund der Duplizierung mit Strg+NVDA+Ziffernreihe für Studio-Spuren
  wurden die Spaltenexplorer-Befehle aus dem SPL-Assistenten entfernt.
* Geänderte Fehlermeldung, die angezeigt wird, wenn versucht wird, ein
  Studio-Zusatzeinstellungsdialogfeld (z. B. Metadaten-Streaming-Dialogfeld)
  zu öffnen, während ein anderes Einstellungsdialogfeld
  (z. B. Alarmdialogfeld für das Ende der Spur) aktiv ist. Die neue
  Fehlermeldung entspricht der Meldung, die angezeigt wird, wenn versucht
  wird, mehrere NVDA-Einstellungsdialoge zu öffnen.
* NVDA verursacht keine Fehlertöne mehr oder scheint nichts zu tun, wenn
  nach der Konfiguration der Spalten in dem Spalten-Explorer auf die
  Schaltfläche "OK" geklickt wird.
* In den Encodern können Sie nun Encoder-Einstellungen (einschließlich
  Stream-Bezeichnungen) durch dreimaliges Drücken von Strg+NVDA+C
  bzw. Strg+NVDA+R speichern und zurücksetzen.

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
* Bei Encodern spielt NVDA jede halbe Sekunde einen Verbindungston ab,
  während ein Encoder verbunden ist.
* Bei Encodern meldet NVDA nun Meldungen über Verbindungsversuche, bis ein
  Encoder tatsächlich angeschlossen ist. Zuvor stoppte NVDA, wenn ein Fehler
  auftrat.
* Eine neue Einstellung zu den Encoder-Einstellungen wurde hinzugefügt,
  damit NVDA über Verbindungsmeldungen informiert, bis der ausgewählte
  Encoder verbunden ist. Diese Einstellung ist standardmäßig aktiviert.

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
* 19.03 Experimentell: In den Panels für Spaltenankündigungen und
  Playlist-Transkriptionen (Zusatz-Einstellungen) werden benutzerdefinierte
  Spalteneinschluss- bzw. Kontrollen im Vordergrund sichtbar sein, anstatt
  eine Schaltfläche auswählen zu müssen, um einen Dialog zur Konfiguration
  dieser Einstellungen zu öffnen.

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
