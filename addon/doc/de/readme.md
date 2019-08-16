# StationPlaylist #

* Autoren: Geoff Shang, Joseph Lee und weitere Mitwirkende
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]
* NVDA-Kompatibilität: 2019.1 bis 2019.2

Diese Erweiterung verbessert die Zugänglichkeit von Station Playlist. Es
stehen außerdem Befehle zur Verfügung, um diese Anwendungvon überall aus zu
bedienen.

Weitere Informationen zur Erweiterung finden Sie in der
[Add-On-Anleitung][4]. Für Entwickler, welche wissen wollen, wie die
Erweiterung  erstellt wurde, siehe buildInstructions.txt im
Quellcodeverzeichnis der Erweiterung auf Github.

WICHTIGE HINWEISE:

* Diese Erweiterung benötigt NVDA 2019.1 oder neuer und StationPlaylist
  Suite 5.20 oder neuer.
* Wenn Sie Windows 8 oder höher verwenden, setzen Sie die Reduzierung der
  Lautstärke anderer Audioquellen auf "nie" im Dialog Sprachausgabe im
  NVDA-Einstellungsmenü.
* Seit 2018 finden Sie [die Änderungen der Veröffentlichungen der
  Erweiterung][5] auf GitHub. Diese Readme für die Erweiterung listet die
  Änderungen gegenüber der Version 8.0/16.10 (seit 2016) auf.
* Bestimmte Funktionen sind nicht mehr verfügbar, z.B. während NVDA im
  abgesicherten Modus ausgeführt wird.
* Aufgrund technischer Einschränkungen können Sie diese Erweiterung nicht
  auf der Windows-Store-Version von NVDA installieren oder verwenden.
* Features, die als "experimentell" gekennzeichnet sind, sollen etwas vor
  einer zukünftigen Version testen, sodass sie nicht in stabilen Versionen
  aktiviert werden.

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
* Alt+NVDA+1 (mit zwei Fingern nach rechts wischen im SPL-Touch-Modus) aus
  dem Studio-Fenster: Öffnet den Dialog zum Einstellen des Titelendes.
* Alt+NVDA+2 (mit zwei Fingern nach links wischen im SPL-Touchmodus) aus dem
  Studio-Fenster: Öffnet den Einstellungsdialog für den Titel-Intro-Alarm.
* Alt+NVDA+3 aus dem Studio-Fenster: legt den Cart-Explorer fest, um die
  Zuordnung von Carts zu lernen.
* Alt+NVDA+4 aus dem Studio-Fenster: Öffnet den Mikrofonalarm-Dialog.
* STRG+NVDA+f aus dem Studio-Fenster: Öffnet einen Dialog, um einen Titel
  basierend auf Künstler oder Titelbezeichnung zu finden. Drücken Sie
  NVDA+F3, um vorwärts zu suchen oder NVDA+Umschalt+F3, um rückwärts zu
  suchen.
* Alt+NVDA+R aus dem Studio-Fenster: Benachrichtigungseinstellungen für
  Bibliothek-Scans.
* Strg+Umschalt+X aus dem Studio-Fenster: Braille-Timer-Einstellungen.
* Strg+Alt+Pfeiltaste nach links/rechts (während Sie sich auf einen Track im
  Studio, Creator und Track Tool befinden): Ankündigung der
  vorherigen/nächsten Track-Spalte.
* Strg+Alt+Pfeiltaste nach oben/unten (während Sie sich nur auf einen Track
  in Studio befinden): Wechseln Sie zum vorherigen oder nächsten Track und
  kündigen Sie bestimmte Spalten an (nicht verfügbar im Add-on 15.x).
* Strg+NVDA+1 bis 0 (während sie sich auf einen Track im Studio, Creator und
  Track Tool befinden): Ankündigung von Spalteninhalten für eine bestimmte
  Spalte. Wenn Sie diesen Befehl zweimal drücken, werden
  Spalteninformationen in einem Fenster des Lesemodus angezeigt.
* Strg+NVDA+Minus (Bindestrich) in Studio): Zeigt Daten für alle Spalten in
  einer Spur in einem Fenster des Lesemodus an.
* Alt+NVDA+C während der Fokus auf einen Track (nur Studio): Meldet
  Track-Kommentare, falls vorhanden.
* Alt+NVDA+0 aus dem Studio-Fenster: Öffnet den Konfigurationsdialog der
  SPL-Erweiterung.
* Alt+NVDA+Minus (Bindestrich) aus dem Studio-Fenster: Senden Sie Feedback
  an den Entwickler der Erweiterung mit der E-Mail-Programm.
* Alt+NVDA+F1: öffnet das Willkommensdialog.

## Nicht zugewiesene Befehle

Die folgenden Befehle sind standardmäßig nicht belegt. Falls Sie diese
Befehle verwenden möchten, weisen Sie  den Befehlen im NVDA-Eingabendialog
eine beliebige Tastenkombination zu.

* Das wechseln zum SPL Studio-Fenster aus einem beliebigen Programm.
* Befehlsschicht des SPL-Controllers.
* Ansage des Studio-Status beim Navigieren in anderen Programmen,
  z.B. Titelwiedergabe.
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

## Zusätzliche Befehle während der Verwendung von Sam- oder SPL-Encoder

Folgende Befehle stehen zur Verfügung, wenn Sie Sam- oder SPL-Encoder
verwenden:

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
* STRG+NVDA+3 aus dem SPL-Encoder: öffnet die Encoder-Einstellungen.
* STRG+NvDA+4 aus dem SAM-Encoder: meldet den Encoder-Verbindungsstatus.
* STRG+NVDA+4 aus dem SPL-Encoder: Übertragungsrate oder Verbindungsstatus
  wird angesagt.
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
* C (Umschalt+C in JAWS- und Window-Eyes-Darstellung): Bezeichnung des
  aktuell abgespielten Titels.
* C (JAWS- und Window-Eyes-Darstellungen): Wechselt die Cart-Übersicht (nur
  im Playlist-Viewer).
* D (R in der JAWS-Darstellung): Restdauer der Playlist (wenn eine
  Fehlermeldung angezeigt wird, wechseln Sie zum Playlist-Viewer und geben
  Sie diesen Befehl ein).
* E (G in Window-Eyes-Darstellung): Status der Metadaten-Streams.
* Umschalt+1 bis 4, Umschalt+0: Status für einzelne Metadaten-Streaming-URLs
  (0 ist für DSP-Encoder).
* E (Window-Eyes-Darstellung): verstrichene zeit des aktuell abgespielten
  Titels.
* F: Titel suchen (nur im Playlist-Viewer).
* H: Dauer der Titel in dieser Stunde.
* Umschalt+H: Verbleibende Spieldauer für den Stundenplatzhalter.
* I (L in der jaws- und Window-Eyes-Darstellung): Anzahl der Zuhörer.
* K: springt zum Lesezeichentitel (nur im Playlist-Viewer).
* Strg+K: Aktuellen Titel als Lesezeichentitel setzen (nur im
  Playlist-viewer).
* L (Umschalt+L in JAWS- und Window-Eyes-Darstellungen): Line in.
* M: Mikrofon.
* N: Titel der nächst geplante Datei.
* P: Wiedergabestatus (Wiedergabe oder angehalten).
* Umschalt+P: Pitch des aktuellen Titels.
* R (Umschalt+E in der Jaws- und Window-Eyes-Darstellung): in Datei
  aufzeichnen ein- und ausschalten.
* Umschalt+R: Überwachung des Bibliothek-Scans läuft...
* S: Titel beginnt (geplant).
* Umschalt+S: Zeit bis zur Wiedergabe des ausgewählten Titels (Titel startet
  in...).
* T: Cart-Bearbeitungs-/Einfügemodus ein und ausschalten.
* U: Studiozeit.
* W: Wetter und Temperatur, wenn konfiguriert.
* Y: Status der Playlist-Änderungen.
* 1 bis 0 (bis 6 für Studio 5.0x): sagt den Spalteninhalt für eine bestimmte
  Spalte an.
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
* Drücken Sie E, um die Anzahl und die Bezeichnung der aktuell überwachten
  Encoder zu erhalten.
* Drücken Sie I, um die Anzahl der Zuhörer zu ermitteln.
* Drücken Sie Q, um verschiedene Statusinformationen über Studio zu
  erhalten, z. B. ob ein Titel wiedergegeben wird, das Mikrofon
  eingeschaltet ist und mehr.
* Drücken Sie die Cart-Tasten (z.B. F1, STRG+1), um die zugewiesenen Carts
  von überall zu spielen.
* Drücken Sie die Taste H, um einen Hilfe-Dialog anzuzeigen, in dem die
  verfügbaren Befehle aufgelistet sind.

## Titelbenachrichtigungen

Standardmäßig gibt NVDA einen Piepton aus, wenn fünf Sekunden im Titel-Outro
und/oder -Intro verbleiben. Um diesen Wert zu konfigurieren und zu
aktivieren bzw. zu deaktivieren, drücken Sie Alt+NVDA+1 oder
Alt+NVDA+2. Somit öffnen Sie die Dialoge für das Ende des Titels. Darüber
hinaus können Sie im Einstellungsdialog für die SPL-Erweiterung
konfigurieren, ob Sie beim Einschalten des Alarms einen Signalton, eine
Meldung oder beides hören.

## Mikrofon-Alarm

Sie können NVDA mitteilen, einen Ton wiederzugeben, wenn das Mikrofon eine
Weile aktiv war. Drücken Sie Alt+NVDA+4, um die Alarmzeit in Sekunden zu
konfigurieren (0 deaktiviert den Alarm).

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

Durch Drücken von Strg+NVDA+1 bis 0 oder SPL Assistant, 1 bis 0, können Sie
den Inhalt bestimmter Spalten erhalten. Standardmäßig sind dies Künstler,
Titel, Dauer, Intro, Kategorie, Dateiname, Jahr, Album, Genre und
Zeitplanung. Sie können konfigurieren, welche Spalten über den
Spalten-Explorer-Dialog im Einstellungsdialog des Add-ons erkundet werden
sollen.

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

## SPL-Touchmodus

Wenn Sie Studio auf einem Touchscreen-Computer mit Windows 8 oder höher
verwenden und NVDA 2012.3 oder höher installiert haben, können Sie einige
Studio-Befehle über den Touchscreen ausführen. Tippen Sie zunächst einmal
mit drei Fingern, um in den SPL-Touchmodus zu wechseln. Verwenden Sie dann
die oben aufgeführten Touch-Befehle, um Befehle auszuführen.

## Version 19.08.1

* In SAM-Enkodern wurde das Problem behoben, dass NVDA nichts zu tuhn
  scheint oder Fehlertöne abspielt, wenn ein Encoder-Eintrag  gelöscht wird,
  während dieser im Hintergrund beobachtet wird.

## Version 19.08/18.09.11-LTS

* 19.08: NVDA 2019.1 oder höher ist erforderlich.
* 19.08: Das Problem, dass NVDA nichts zu tuhn scheint oder Fehlertöne
  abspielt, wurde behoben, wenn es bei geöffnetem Studio-Einstellungsdialog
  der Erweiterung neu gestartet wird.
* NVDA will remember profile-specific setttings when switching between
  settings panels even after renaming the currently selected broadcast
  profile from add-on settings.
* NVDA will no longer forget to honor changes to time-based profiles when OK
  button is pressed to close add-on settings. This bug has been present
  since migrating to multi-page settings in 2018.

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
* 19.03 Experimentell: In Spaltenansagen und Playlist-Transkriptfeldern
  (Add-On-Einstellungen) werden benutzerdefinierte
  Spalteneinschluss-/Reihenfolgesteuerelemente im Vordergrund sichtbar sein,
  anstatt eine Schaltfläche auswählen zu müssen, um einen Dialog zur
  Konfiguration dieser Einstellungen zu öffnen.

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

## Version 18.08.2

* NVDA wird nicht mehr nach Studio-Erweiterungs-Updates suchen, wenn der
  Zusatz-Updater (Proof of Concept) Add-On installiert ist. Infolgedessen
  beinhalten die Einstellungen in diesem Fall keine
  Erweiterungs-Update-bezogenen Einstellungen mehr. Wenn Sie Zusatz-Updater
  verwenden, sollten Benutzer die Funktionen diese Erweiterungen verwenden,
  um nach Studio-Erweiterungs-Updates zu suchen.

## Version 18.08.1

* Ein weiteres Kompatibilitätsproblem mit wxPython 4 wurde behoben, das beim
  Beenden von Studio auftrat.
* NVDA kündigt eine entsprechende Meldung an, wenn kein Text zur Änderung
  der Wiedergabeliste vorhanden ist, was häufig nach dem Laden einer
  unveränderten Wiedergabeliste oder beim Starten von Studio der Fall ist.
* NVDA scheint nichts mehr zu tun oder Fehlertöne abzuspielen, wenn versucht
  wird, den Metadaten-Streaming-Status über den SPL-Assistenten (E) zu
  erhalten.

## Version 18.08

* Der Dialog für zusätzliche Einstellungen basiert nun auf der in NVDA
  2018.2 enthaltenen Schnittstelle für Einstellungen in mehreren
  Kategorien. Daher erfordert diese Version die NVDA 2018.2 oder höher. Die
  alte Erweiterungs-Einstellungsoberfläche ist veraltet und wird später im
  Jahr 2018 entfernt.
* Es wurde ein neuer Abschnitt (Schaltfläche / Steuerung) in den
  Einstellungen der Erweiterung hinzugefügt, um die Optionen für die
  Transkripte der Wiedergabeliste zu konfigurieren, mit dem die
  Spalteneinbindung und -reihenfolge für diese Funktion und andere
  Einstellungen konfiguriert werden können.
* Bei der Erstellung einer tabellenbasierten Wiedergabelistentranskription
  und wenn eine benutzerdefinierte Spaltenreihenfolge bzw. Spaltenentfernung
  in Kraft ist, verwendet NVDA eine benutzerdefinierte Spaltenpräsentation,
  die in den Einstellungen der Erweiterung angegeben ist bzw. keine
  Informationen aus entfernten Spalten enthält.
* Wenn Sie in Studio, Creator und Track Tool Spaltennavigationsbefehle in
  Track-Listen (Strg+Alt+Pos1 / Ende / Pfeiltaste nach links / Pfeiltaste
  nach rechts) verwenden, wird NVDA keine falschen Spaltendaten mehr melden,
  nachdem Sie die Spaltenposition auf dem Bildschirm per Maus geändert
  haben.
* Signifikante Verbesserungen der Reaktionsfähigkeit von NVDA bei der
  Verwendung von Spaltennavigationsbefehlen im Creator und Track
  Tool. Insbesondere bei der Verwendung von Creator reagiert NVDA besser,
  wenn dieser Befehle zur Spaltennavigation verwendet.
* NVDA spielt keine Fehlertöne mehr ab oder scheint nichts zu tun, wenn
  versucht wird, Kommentare zu Tracks in Studio hinzuzufügen oder wenn NVDA
  während der Nutzung von Studio verlassen wird, verursacht durch ein
  Kompatibilitätsproblem mit wxPython 4.

## Version 18.07

* Es wurde ein experimenteller Dialog mit Einstellungskathegorien der
  Erweiterung hinzugefügt. Den neuen Dialog können Sie in den Einstellungen
  der Erweiterung / erweiterte Einstellungen aktivieren. Sie müssen NVDA neu
  starten, nachdem Sie diese Einstellung konfiguriert haben, damit der neue
  Dialog angezeigt wird. Dies gilt für Benutzer von NVDA 2018.2 oder
  höher. Nicht alle Einstellungen der Erweiterung können über diesen neuen
  Bildschirm konfiguriert werden.
* NVDA spielt keine Fehlertöne mehr ab oder scheint nichts zu tun, wenn
  versucht wird, ein Broadcast-Profil aus Add-On-Einstellungen umzubenennen,
  verursacht durch ein Kompatibilitätsproblem mit wxPython 4.
* Wenn Sie NVDA bzw. Studio neu starten, nachdem Sie Änderungen an
  Einstellungen in einem anderen als dem normalen Profil vorgenommen haben,
  kehrt NVDA nicht mehr zu den alten Einstellungen zurück.
* Es ist nun möglich, Transkripte von Playlisten für die aktuelle Stunde zu
  erhalten. Wählen Sie "aktuelle Stunde" aus der Liste der Optionen für den
  Wiedergabelistenbereich im Dialogfeld für Wiedergabelistentranskripte
  (SPL-Assistent, Umschalt+F8).
* Im Dialogfeld "Playlist-Transkripte" wurde eine Option hinzugefügt, mit
  der Transkripte in einer Datei gespeichert (alle Formate) oder in die
  Zwischenablage kopiert werden können (nur Text- und
  Abschriftentabellenformate), zusätzlich zur Anzeige von Transkripten auf
  dem Bildschirm. Beim Speichern von Transkripten werden diese im Ordner
  Documents des Benutzers unter dem Unterordner "nvdasplPlaylistTranscripts"
  gespeichert.
* Die Statusspalte ist bei der Erstellung von Playlist-Transkripten im HTML-
  und Markdown-Tabellenformat nicht mehr enthalten.
* Wenn Sie sich im Creator and Track Tool auf eine Spur konzentrieren,
  drücken Sie zweimal Strg+NVDA+1 bis 0 zweimal, um Spalteninformationen im
  Lesemodus anzuzeigen.
* Im Creator and Track Tool wurden die Tasten Strg+Alt+Pos1/Ende
  hinzugefügt, um den Spaltenavigator zur ersten oder letzten Spalte für die
  fokussierte Spur zu verschieben.

## Version 18.06.1

* Mehrere Kompatibilitätsprobleme mit wxPython 4 behoben, darunter die
  Unfähigkeit, den Track Finder (Strg+NVDA+F) zu öffnen, die Dialoge für
  Spaltensuche und Time Ranger Finder in Studio und den Stream Labeler
  Dialog (F12) im Encoder-Fenster.
* Während des Öffnens eines Suchdialogs aus Studio heraus und ein
  unerwarteter Fehler auftritt, zeigt NVDA angemessenere Meldungen an,
  anstatt zu sagen, dass ein anderer Suchdialog geöffnet ist.
* Im Encoder-Fenster gibt NVDA keine Fehlertöne mehr wieder oder scheint
  nichts zu tun, wenn versucht wird, den Dialog Encoder-Einstellungen zu
  öffnen (Alt+NVDA+0).

## Version 18.06

* In den zusätzlichen Einstellungen wurde die Schaltfläche "Übernehmen"
  hinzugefügt, so dass Änderungen an den Einstellungen auf das aktuell
  ausgewählte und/oder aktive Profil angewendet werden können, ohne den
  Dialog zuerst zu schließen. Diese Funktion ist für Benutzer von NVDA
  2018.2 verfügbar.
* Es wurde ein Problem behoben, bei dem NVDA Änderungen an den Einstellungen
  der Spalten-Explorer vornehmen konnte, obwohl im Dialogfeld für die
  Einstellungen der Erweiterung auf die Schaltfläche "Abbrechen" geklickt
  wurde.
* Wenn Sie in Studio die Strg+NVDA+1 bis 0 zweimal drücken, während Sie sich
  auf einen Track befinden, zeigt NVDA Spalteninformationen für eine
  bestimmte Spalte im Lesemodus an.
* Wenn Sie sich in Studio auf einen Track befinden, drücken Sie
  Strg+NVDA+Minus (Bindestrich), um Daten für alle Spalten im Lesemodus
  anzuzeigen.
* Wenn Sie im StationPlaylist Creator auf einen Track sich befinden, drücken
  Sie Strg+NVDA+1 bis 0, um Daten in einer bestimmten Spalte anzuzeigen.
* Eine Schaltfläche in den Einstellungen der Studio-Erweiterung hinzugefügt,
  um den Spalten-Explorer für SPL Creator zu konfigurieren.
* Das Format der Abschriftentabelle wurde als Format für
  Wiedergabelistentranskripte hinzugefügt.
* Der Befehl für die Entwicklerrückmeldung per E-Mail wurde von
  Strg+NVDA+Bindestrich auf Alt+NVDA+Bindestrich geändert.

## Version 18.05

* Es wurde die Möglichkeit hinzugefügt, partielle Playlist-Statistiken
  anzuzeigen (im SPL-Assistenten: F9). Dies kann durch Definieren des
  Analysebereichs am Anfang der Analyse und durch das Navigieren zu einem
  anderen Element und Ausführen des Befehls für die Anzeige der
  Playlist-Statistiken erfolgen.
* Ein neuer Befehl (Umschalt+f8) wurde hinzugefügt. Im SPL-Assistenten kann
  man damit Playlist-Protokolle in verschiedenen Formaten aufrufen. Dazu
  gehören Textformat, eine HTML-Tabelle oder eine HTML-Liste.
* Verschiedene Funktionen der Playlist-Analyse wie z.B. Titel-Zeitanalyse
  und Playlist-Statistiken sind nun unter der Kathegorie "Playlist-Analyzer"
  zusammengefasst.

## Version 18.04.1

* NVDA startet nun problemlos den Countdown-Timer für zeitbasierte
  Sendeprofile, wenn NVDA mit wxPython 4 verwendet wird.

## Version 18.04

* Die Suche nach Updates ist nun zuverlässiger, vor allem wenn automatisch
  nach Updates gesucht wird.
* Wenn im Einstellungsmenü der SPL-Erweiterung die Töne für bestimmte
  Ereignisse aktiviert sind, dann wird NVDA beim Starten des
  Bibliothek-Scans einen Ton abspielen.
* NVDA wird den Bibliothek-Scan im Hintergrund ausführen, wenn der
  Suchdurchlauf im Einstellungsdialog des Studio ausgewählt wird oder wenn
  der Bibliothek-Scan beim Starten des Programms automatisch ausgeführt
  werden soll.
* Der Systemfokus wird nun zum entsprechenden Titel bewegt und der Titel
  wird ausgewählt, wenn ein Doppeltippen auf einem Titel im
  Touch-Screen-Modus ausgeführt wird. Dies gilt auch beim Ausführen des
  Standard-Aktionsbefehls.
* Es wurden einige Probleme behoben, die dazu führten, dass NVDA in manchen
  Fällen beim Drücken von F8 im SPL-Assistenten keine Playlist-Statistiken
  aufnahm. Dies gilt für Playlisten, die nur Stunden-Marker beinhalten.

## Version 18.03/15.14-LTS

* Wenn die Ansage der Statusinformationen des Metadaten-Streamings beim
  Starten des Studio im Einstellungsdialog der Erweiterung aktiviert ist,
  wird NVDA diese Einstellung berücksichtigen und den Streaming-Status beim
  Wechseln zu und von Instant-Switch-Profilen nicht mehr melden.
* NVDA wird Statusinformationen des Metadaten-Streamings nicht mehr
  wiederholt ansagen, wenn Profile schnell gewechselt werden. Dies gilt beim
  Wechseln zu und von einem Instant-Switch-Profil und wenn NVDA so
  konfiguriert ist, dass es den Status des Metadaten-Streamings ansagt.
* NVDA wird auch dann automatisch auf das entsprechende zeitbasierte Profil
  umschalten (falls ein Profil für eine Sendung definiert ist), wenn NVDA
  mehrmals während der Übertragung neu gestartet wurde.
* Wenn ein zeitbasiertes Profil mit eingestellter Profildauer aktiv ist und
  wenn der Einstellungsdialog für die SPL-Erweiterung geöffnet und
  geschlossen wird, schaltet NVDA nach Beendigung des zeitbasierten Profils
  immer noch auf das ursprüngliche Profil zurück.
* Bei aktivem zeitbasierten Profil (insbesondere bei Sendungen) kann das
  Auslösen des Sendeprofils über den Einstellungsdialog der SPL-Erweiterung
  nicht geändert werden.

## Version 18.02/15.13-LTS

* 18.02: Aufgrund interner Änderungen an der Unterstützung von Erweiterten
  Schnittstellen und anderen Features ist NVDA 2017.4 erforderlich.
* Aktualisierungen sind in manchen Fällen nicht möglich. Zu solchen fällen
  gehört die Ausführung von NVDA aus dem Quellcode oder mit eingeschaltetem
  Sicherheitsmodus. Die Prüfung, ob der Sicherheitsmodus aktiv ist, kann
  auch in 15.13-LTS angewendet werden.
* Treten bei der Suche nach Aktualisierungen Fehler auf, werden diese
  protokolliert und NVDA wird empfehlen, das NVDA-Protokoll zu lesen.
* In den Einstellungen der Erweiterung werden verschiedene
  Aktualisierungseinstellungen im Abschnitt "Erweiterte Optionen" (z. B. das
  Update-Intervall), nicht angezeigt, wenn die Erweiterungsaktualisierung
  nicht unterstützt wird.
* NVDA friert nicht mehr ein und reagiert entsprechend, wenn Sie zu einem
  Instant-Switch-Profil oder einem zeitbasierten Profil wechseln. NVDA ist
  so konfiguriert, dass es den Status des Metadaten-Streamings ansagt.

## Version 18.01/15.12-LTS

* Der Befehl  STRG+Umschalt+U für das Suchen nach Aktualisierungen
  funktioniert nun richtig, wenn Sie die JAWS-Darstellung für den
  SPL-Assistenten verwenden.
* Mikrofonalarmeinstellungen wie z.B. die Aktivierung des Alarms und die
  Änderung des Mikrofonalarmintervalls über den Alarmdialog (Alt+NVDA+4)
  werden beim Schließen des Dialogs übernommen.

## Version 17.12

* Windows 7 Service Pack 1 oder höher ist erforderlich.
* Mehrere Zusatzfunktionen wurden erweitert. Dadurch können
  Mikrofonbenachrichtigung und Metadaten-Streaming auf Änderungen in
  Broadcast-Konfigurationsprofilen reagieren. Dies erfordert NVDA 2017.4.
* Beim Beenden des Studio schließen sich verschiedene Erweiterungsdialoge
  wie Einstellungen, Benachrichtigungsdialoge und andere automatisch. Dies
  erfordert NVDA 2017.4.
* Es wurde ein neuer Befehl in der Befehlsschicht für den SPL-Controller
  hinzugefügt, um den Namen des nächsten Titels anzukündigen (Umschalt+C).
* Sie können nun nach dem Öffnen der SPl-Controller-Ebene die Cart-Tasten
  (z.B. F1) drücken, um die zugewiesenen Carts von überall her abzuspielen.
* Aufgrund von Änderungen, die im wxPython 4 GUI Toolkit eingeführt wurden,
  ist der Dialog zum Löschen von Streambezeichnungen nun ein
  Kombinationsfeld anstelle eines Zahleneingabefeldes.

## Version 17.11.2

Dies ist die letzte stabile Version, die Windows XP, Vista und 7 ohne
Service Pack 1 unterstützt. Die nächste stabile Version für diese
Windows-Versionen wird eine 15.x LTS-Version sein.

* Sie können nicht zu Entwicklungskanälen wechseln, wenn Sie
  Windows-Versionen vor Windows 7 Service Pack 1 verwenden.

## Version 17.11.1/15.11-LTS

* NVDA spielt keine Fehlertöne mehr ab und reagiert entsprechend, wenn Sie
  mit den Tasten STRG+Alt+Links oder Rechtspfeil im Studio 5.20 zwischen
  Spalten mit geladenem Titel navigieren. Aus diesem Grund ist bei der
  Verwendung von Studio 5.20 die Build 48 oder höher erforderlich.

## Version 17.11/15.10-LTS

* Erstmalige Unterstützung für StationPlaylist Studio 5.30.
* Wenn die Mikrofonbenachrichtigung und/oder der Intervalltimer
  eingeschaltet ist und wenn Studio beendet wird, während das Mikrofon
  eingeschaltet ist, gibt NVDA den Ton für die Mikrofonbenachrichtigung
  nicht mehr von überall her wieder.
* Die Instant-Switch-Flag wird nicht aus dem Switch-Profil entfernt, wenn
  Sende-Profile gelöscht werden und wenn ein anderes Profil ein
  Instant-Switch-Profil ist.
* Wenn Sie ein aktives Profil löschen, das kein Instant-Switch-  oder wenn
  das profil ein temporäres Profil ist, fragt NVDA noch einmal nach einer
  Bestätigung, bevor Sie fortfahren.
* NVDA wendet die korrekten Einstellungen für die Einstellungen der
  Mikrofonbenachrichtigung an, wenn Profile über den Dialog für die
  Einstellungen der Studio-Erweiterung gewechselt werden.
* Sie können nun die Taste für den SPL-Controller (H) drücken, um Hilfe für
  die SPL-Controller-Befehlsschicht zu erhalten.

## Version 17.10

* Wenn Sie Windows-Versionen älter als Windows 7 Service Pack 1 verwenden,
  können Sie nicht auf den Aktualisierungskanal Test Drive Fast
  umschalten. Ein zukünftiges Release dieser Erweiterung wird Benutzer
  veralteter Windows-Versionen in einen dedizierten Support-Kanal
  verschieben.
* Einige allgemeine Einstellungen wie z.B. Signaltöne für die Statusansage,
  Benachrichtigung über den Anfang und Ende einer Playlist und mehr,
  befinden sich jetzt im neuen Dialogfeld für die allgemeinen Einstellungen
  (über eine neue Schaltfläche in den Einstellungen zur Studio-Erweiterung).
* Es ist nun möglich, Optionen der Erweiterung schreibgeschützt zu machen,
  nur das normale Profil zu verwenden oder die Einstellungen beim Start von
  Studio nicht von der Festplatte zu laden. Diese werden von neuen
  Kommandozeilenbefehlen gesteuert, die speziell für diese Erweiterung
  entwickelt wurden.
* Beim Ausführen von NVDA aus dem Dialogfeld "Ausführen" (Windows+R) können
  Sie nun zusätzliche Kommandozeilenbefehle eingeben, um die Funktionsweise
  der Erweiterung zu ändern. Dazu gehören "--spl-configvolatile"
  (schreibgeschützte Einstellungen), "--spl-configinmemory" (Einstellungen
  nicht von der Festplatte laden) und "--spl-normalprofileonly" (nur
  normales Profil verwenden).
* Wenn Sie Studio (nicht NVDA) verlassen, während ein Instant-Switch-Profil
  aktiv ist, gibt NVDA beim Wechseln zu einem Instant-Switch-Profil keine
  irreführende Ansage mehr aus. Dies gilt, wenn Sie Studio wieder öffnen.

## Version 17.09.1

* Als Ergebnis der Ankündigung von NV Access, dass NVDA 2017.3 die letzte
  Version mit Unterstützung für Windows-Versionen vor Windows 7 Service Pack
  1 sein wird, wird die Studio-Erweiterung in älteren Windows-Versionen eine
  entsprechende Erinnerungsmeldung anzeigen. Das Ende des Supports für alte
  Windows-Versionen aus dieser Erweiterung (über Langzeit-Support-Version)
  ist für April 2018 geplant.
* NVDA zeigt keine Startdialoge und/oder kündigt die Studio-Version nicht
  mehr an, wenn sie mit minimalem Flag (nvda -rm) gestartet wird. Die
  einzige Ausnahme ist der alte Windows-Release-Erinnerungsdialog.

## Version 17.09

* NVDA zeigt beim Verlassen des Einstellungsdialogs nicht mehr die Kanal-
  und/oder Intervallwarnung an, wenn ein Benutzer den Dialog Erweiterte
  Optionen unter den Einstellungen zur Studio-Erweiterung aufruft. Dies gilt
  während der Update-Kanal und das Intervall auf Test Drive Fast und/oder 0
  Tage eingestellt wurde.
* Die Befehle zur Analyse der Restdauer der Playlist und der Titeldauer
  erfordern nun, dass eine Playlist geladen wird. Andernfalls wird eine
  genauere Fehlermeldung angezeigt.

## Version 17.08.1

* NVDA wird nicht mehr verusachen, dass Studio den ersten Titel abspielt,
  wenn ein Encoder angeschlossen ist.

## Version 17.08

* Änderungen bei der Aktualisierung der Kanalbezeichnungen: try build ist
  jetzt Test Drive Fast, der Entwicklungskanal ist Test Drive Slow. Die
  wahren "try"-Builds werden für tatsächliche Try-Builds reserviert sein,
  bei denen die Benutzer eine Testversion manuell installieren müssen.
* Das Aktualisierungsintervall kann jetzt auf 0 (null) Tage eingestellt
  werden. Dies ermöglicht es der Erweiterung beim Start von NVDA und/oder
  SPL Studio nach Updates zu suchen. Eine Bestätigung ist erforderlich, um
  das Aktualisierungsintervall auf Null Tage zu ändern.
* NVDA wird nicht mehr bei der Suche von Aktualisierungen für diese
  Erweiterung fehlschlagen, wenn das Aktualisierungsintervall auf 25 Tage
  oder länger eingestellt ist.
* In den Einstellungenzur Erweiterung  wurde ein Kontrollkästchen
  hinzugefügt, mit dem NVDA einen Sound abspielen kann, wenn Anfragen von
  Zuhörern eintreffen. Um dies vollständig nutzen zu können, muss das
  Anfragenfenster beim Eintreffen von Anfragen geöffnet sein.
* Zweimaliges Drücken des Befehls für die Sendezeit (NVDA+Umschalt+F12)
  bewirkt nun, dass NVDA die verbleibenden Minuten und Sekunden in der
  aktuellen Stunde ansagt.
* Es ist jetzt möglich, mit dem Titelfinder (STRG+NVDA+F) nach zuletzt
  gesuchten Bezeichnungen von Titeln zu suchen, indem Sie einen Suchbegriff
  aus einer Liste auswählen.
* Bei der Ansage der Bezeichnung des aktuellen und des nächsten Titels über
  den SPL-Assistenten ist es nun möglich, Informationen über die Zuordnung
  des Titels zu einem bestimmten Studio-internen Player einzugeben. Der
  Titel wird in dem ausgewählten Player abgespielt, z.B. Player 1.
* Es wurde eine Einstellung in den Einstellungsdialog unter Statusmeldungen
  hinzugefügt, um Player-Informationen bei der Ansage der Bezeichnung des
  aktuellen und des nächsten Titels zu berücksichtigen.
* Es wurde ein Problem in temporären Cue-Dialogen und anderen Dialogen
  behoben, bei dem NVDA keine neuen Werte bei der Manipulation von
  Zeitschaltern ansagte.
* NVDA kann die Ankündigung von Spaltenüberschriften wie Interpret und
  Kathegorie unterdrücken, wenn Titelim Playlist-Viewer betrachtet
  werden. Dies ist eine Sende-Profil-spezifische Einstellung.
* Es wurde ein Kontrollkästchen im Einstellungsdialog der SPL-Erweiterung
  hinzugefügt, um die Ansage von Spaltenüberschriften beim Betrachten von
  Titeln im Playlist-Viewer zu unterdrücken.
* In der Befehlsschicht für den SPL-Controller wurde ein Befehl hinzugefügt,
  um den Namen und die Dauer des aktuell abgespielten Titels von überall zu
  melden (C).
* Wenn Sie mit Studio 5.1x Statusinformationen über den SPL Controller (Q)
  abrufen, werden neben der Wiedergabe und Automatisierung auch
  Informationen wie Mikrofonstatus, Cart-Bearbeitungsmodus und mehr
  angesagt.

## Version 17.06

* Sie können nun den Titelfinder-Befehl (STRG+NVDA+F) ausführen, während
  eine Playlist geladen ist. Dies gilt, auch wenn der erste Titel nicht
  fokussiert ist.
* NVDA wird keine Fehlertöne mehr abspielen und entsprechend reagieren, wenn
  vorwärts vom letzten Titel bzw. rückwärts vom ersten Titel nach einem
  bestimmten Titel gesucht wird.
* Drücken von NVDA+Nummernblock-Entfernen (NVDA+Entfernen im Laptop-Layout)
  wird nun die Titelposition und die Anzahl der Elemente in einer Playlist
  ausgeben.

## Version 17.05.1

* NVDA wird beim Speichern von Änderungen an den Alarmeinstellungen aus
  verschiedenen Alarmdialogen nicht mehr fehlschlagen (z.B. Alt+NVDA+1 für
  Benachrichtigungen zum Ende eines Titels).

## Version 17.05/15.7-LTS

* Das Aktualisierungsintervall kann jetzt auf 180 Tage eingestellt
  werden. Bei Standardinstallationen beträgt das Prüfintervall für
  Aktualisierungen 30 Tage.
* Es wurde ein Problem behoben, bei dem NVDA manchmal einen Fehlerton
  ausgab, wenn Studio beendet wurde. Dies trat auf, wenn ein temporäres
  Profil aktiv war.

## Version 17.04

* Es wurde eine grundlegende Unterstützung für Debugging hinzugefügt, indem
  verschiedene Informationen protokolliert werden, während die Erweiterung
  aktiv ist und NVDA auf Debug-Protokollierungsstufe eingestellt ist
  (erfordert NVDA 2017.1 und höher). Wählen Sie nach der Installation von
  NVDA 2017.1 im Dialogfeld "Protokollierungsstufe" die Option "Debug", um
  diese Funktion zu verwenden.
* Verbesserte Darstellung verschiedener Dialoge dank der Funktionen von NVDA
  2016.4.
* NVDA lädt Aktualisierungen für diese Erweiterung  im Hintergrund herunter,
  wenn Sie im Bestätigungsdialog bei der Aktualisierung auf "Ja"
  klicken. Infolgedessen werden Benachrichtigungen über Datei-Downloads von
  Webbrowsern nicht mehr angesagt.
* NVDA hängt sich bei der Suche nach Aktualisierungen für diese Erweiterung
  nicht mehr auf, da der Kanalwechsel beim Update erfolgt.
* Es wurde die Möglichkeit zugefügt, mit Strg+Alt+aufwärts oder abwärtspfeil
  vertikal zwischen den Titeln (insbesondere den Titelspalten) zu wechseln,
  während man sich in einer Tabelle zur nächsten oder vorherigen Zeile
  bewegt.
* Es wurde ein Kombinationsfeld im Einstellungsdialog der SPL-Erweiterung
  hinzugefügt, um festzulegen, welche Spalte beim vertikalen Durchlaufen von
  Spalten angesagt werden soll.
* Das Ende des Titels, Intro- und Mikrofon-Alarmsteuerungen wurden von den
  Einstellungen der Erweiterung im neuen Benachrichtigungscenter verschoben.
* Im Benachrichtigungscenter werden die Eingabefelder für das Ende und das
  Intro des Titels immer angesagt, unabhängig vom Status der
  Alarmbenachrichtigung.
* Im SPL-Assistenten wurde der Befehl F8 hinzugefügt, um Schnappschüsse von
  Wiedergabelisten zu erhalten (z.B. Anzahl der Titel, längster Titel, Top
  Interpreten usw.). Sie können auch einen benutzerdefinierten Befehl für
  diese Funktion hinzufügen.
* Durch einmaliges Drücken des benutzerdefinierten Befehls für die Funktion
  "Playlist-Schnappschüsse" kann NVDA eine kurze Statistik-Information
  ausgeben und in Braille anzeigen. Wenn Sie den Befehl zweimal drücken,
  öffnet NVDA eine Webseite, die eine umfangreichere Playlist-Statistik
  enthält. Drücken Sie Escape, um diese Webseite zu schließen.
* Titeleingabe (Die Art der erweiterten Pfeiltasten in NVDA) wurde entfernt
  und durch Spaltenexplorer und Spaltennavigator/Befehele der
  Tabellennavigation ersetzt. Dies betrifft Studio und Tracktool.
* Nach dem Schließen des Dialogs "Titel einfügen" während eines
  Suchduurchlaufs in der Bibliothek ist es nicht mehr erforderlich, im
  SPL-Assistenten Umschalt+R zu drücken, um den Scanfortschritt zu
  überwachen.
* Verbesserte Genauigkeit bei der Erkennung und Meldung der Fertigstellung
  von Suchdurchläufen in Bibliotheken in Studio 5.10 und höher. Dies behebt
  ein Problem, bei dem der Bibliothek-Scan-Monitor vorzeitig beendet wird,
  wenn mehr Titel durchsucht werden müssen. Dies macht einen Neustart des
  Bibliotheks-Scan-Monitors erforderlich.
* Verbesserte Statusmeldung des Bibliotheksscans über den SPL-Controller
  (Umschalt+R) durch Ankündigung des Scan-Zählers, wenn der Scan tatsächlich
  stattfindet.
* In der Studio-Demo, wenn der Registrierungsbildschirm beim Starten von
  Studio erscheint, führen Befehle wie die verbleibende Zeit für einen Titel
  nicht mehr zur Ausgabe von Fehlertönen oder falscher Informationsangaben
  durch NVDA. Stattdessen wird eine Fehlermeldung ausgegeben. Für solche
  Befehle ist es erforderlich, dass das Hauptfenster von Studio maximiert
  ist.
* Erstmalige  Unterstützung für StationPlaylist-Creator.
* Es wurde ein neuer Befehl in der Befehlsschicht für den SPL-Controller
  hinzugefügt, um den Studio-Status wie Titelwiedergabe und Mikrofon-Status
  (Q) zu melden.

## Version 17.03

* NVDA wird keine irreführenden Aktionen  mehr ausführen und auch keine
  Fehlerton mehr abspielen, wenn auf  ein temporäres Sendeprofil gewechselt
  wird.
* Übersetzungen aktualisiert.

## Version 17.01/15.5-LTS

Hinweis: 17.01.1/15.5A-LTS ersetzt 17.01 aufgrund von Änderungen am
Speicherort neuer Erweiterungsdateien.

* 17.01.1/15.5A-LTS: Bei Langzeit-Support-Versionen wurden die Quellen der
  Downloads der Aktualisierungen geändert. Die Installation dieser Version
  ist obligatorisch.
* Verbesserte Reaktionsfähigkeit und Zuverlässigkeit bei der Verwendung der
  Erweiterung zum Umschalten auf Studio, entweder mit dem Befehl "Fokus zum
  Studio" aus anderen Programmen oder wenn ein Encoder angeschlossen ist und
  NVDA aufgefordert wird, in diesem Fall auf Studio umzuschalten. Wenn
  Studio minimiert ist, wird das Studio-Fenster als nicht verfügbar
  angezeigt. Bitte stellen Sie in diesem Fall das Studio-Fenster aus der
  Taskleiste wieder her.
* Beim Bearbeiten von Carts während die Cart-Übersicht aktiv ist, ist es
  nicht mehr notwendig die Cart-Übersicht erneut zu öffnen, um aktualisierte
  Cart-Zuweisungen anzuzeigen. Dies gilt, wenn der Cart-Bearbeitungsmodus
  deaktiviert ist. Folglich, die Meldung "Cart-Explorer reentry" wird nicht
  mehr angezeigt.
* In der Version 15.5-LTS wurde die Darstellung der Benutzeroberfläche für
  den SPL-Einstellungsdialog korrigiert.

## Version 16.12.1

* Die Darstellung der Benutzeroberfläche für den Einstellungsdialog für die
  Studio-Erweiterung wurde verbessert.
* Übersetzungen aktualisiert.

## Version 16.12/15.4-LTS

* Weitere Arbeiten an der Unterstützung von Studio 5.20, einschließlich der
  Ansage des Status des Einfügemodus mit der Taste t (falls aktiviert) von
  der Ebene SPL-Assistenten.
* Die Umschaltung zwischen dem Bearbeitungs- und Einfügemodus der Carts wird
  nicht mehr durch die Einstellungen für die Sprachausführlichkeit und die
  Art der Statusansage beeinflusst (dieser Status wird immer über Sprache
  und/oder Braille angezeigt).
* Das Hinzufügen von Kommentaren zu zeitgesteuerten Pausen ist nicht mehr
  möglich.
* Unterstützung für Track Tool 5.20. Ein Problem wurde behoben, bei dem
  falsche Informationen angesagt werden, wenn mit den Befehlen des
  Spaltenexplorers Spalteninformationen abgerufen werden.

## Version 16.11/15.3-LTS

* Erstmalige Unterstützung für StationPlaylist Studio 5.20, einschließlich
  verbesserter Reaktionsfähigkeit beim Abrufen von Statusinformationen wie
  z.B. Automatisierungsstatus über die Ebene des SPL-Assistenten.
* Probleme bei der Suche nach Titel und der Interaktion mit ihnen wurden
  behoben. Auch fehler beim Aktivieren und Deaktivieren der Titel als
  Markierungszeichen oder eines Titels, der über den Suchdialog für den
  Zeitbereich gefunden wurde, wurden beseitigt.
* Die Reihenfolge der Spaltenansage wird nicht mehr auf die
  Standardreihenfolge zurückgesetzt, nachdem sie geändert wurde.
* 16.11: der  Fehlerdialog wird nun immer angezeigt, Wenn Sendeprofile
  Fehler aufweisen.

## Version 16.10.1/15.2-LTS

* Sie können nun mit dem Titel interagieren, der über den Titelfinder
  (STRG+NVDA+F) gefunden wurde, Beispielsweise, um ihn für die Wiedergabe zu
  aktivieren.
* Übersetzungen aktualisiert.

## Version 8.0/16.10/15.0-LTS

Version 8.0 (auch bekannt als 16.10) unterstützt SPL Studio 5.10 und
höher. Version 15.0-LTS (früher 7.x) stellt einige neue Funktionen von 8.0
für Benutzer früherer Studio-Versionen bereit. Sofern nicht anders vermerkt,
gelten die folgenden Einträge sowohl für 8.0 als auch für 7.x. Bei der
ersten Verwendung des Add-ons 8.0 mit installiertem Studio 5.0x erscheint
ein Warndialog, in dem Sie aufgefordert werden, die 15.x LTS-Version zu
verwenden.

* Das Versionsschema  wurde von major.minor zu Version Jahr.Monat
  geändert. Während der Übergangszeit (bis Mitte 2017) ist Version 8.0
  gleichbedeutend mit Version 16.10, wobei 7.x LTS aufgrund inkompatibler
  Änderungen als 15.0 bezeichnet wird.
* Der Quellcode der Erweiterung wird nun auf GitHub gehostet (Repository
  unter https://github.com/josephsl/stationPlaylist).
* Es wurde ein Willkommensdialog hinzugefügt, der beim Start von Studio nach
  der Installation der Erweiterung angezeigt wird. Ein Befehl (Alt+NVDA+F1)
  wurde hinzugefügt, um diesen Dialog nach dem Schließen wieder zu öffnen.
* Änderungen an verschiedenen Tastaturbefehlen. Dazu gehören die Entfernung
  des Wechselns der Statusansage (STRG+NvDA+1), die Zuweisung der
  Benachrichtigung zum Ende des Titels an Alt+NVDA+1, der Schalter für die
  Cart-Übersicht ist jetzt Alt+NvDA+3, der Mikrofon-Alarm-Dialog ist
  Alt+NVDA+4 und der Einstellundsdialog der Erweiterung / des Encoders ist
  Alt+NVDA+0. Dies wurde geändert, damit STRG+NVDA+Zajlenreihe dem
  Spaltenexplorer zugewiesen werden kann.
* 8.0: leichte Beschränkung des Spaltenexplorers in 7.x, so dass die Zahlen
  1 bis 6 so konfiguriert werden können, dass sie die Spalten in Studio 5.1x
  ankündigen.
* 8.0: Der Wechsel-Befehl Titeleingabe und die entsprechende Einstellung in
  den Einstellungen zur Studio-Erweiterung sind veraltet und werden in 9.0
  entfernt. Dieser Befehl bleibt in der Version 7.x verfügbar.
* STRG+Alt+Pos1/Ende hinzugefügt, um den Spaltennavigator auf die erste oder
  letzte Spalte im Playlist-Viewer zu verschieben.
* Sie können nun Titelkommentare (Notizen) hinzufügen, anzeigen, ändern oder
  löschen. Drücken Sie Alt+NVDA+C von einem Titel im Playlist-Viewer, um
  Titelkommentare zu hören. Falls der Befehl benutzerdefiniert ist, drücken
  Sie zweimal, um den Kommentar in die Zwischenablage zu kopieren oder
  dreimal, um einen Dialog zum Bearbeiten von Kommentaren zu öffnen.
* Benachrichtigung bei vorhandenen Titelkommentaren wurde hinzugefügt. Eine
  Einstellung in den Einstellungen für die Studio-Erweiterung wurde
  eingefügt, um die Benachrichtigungsparameter zu steuern.
* Es wurde eine Einstellung im Einstellungsdialog der SPL-Erweiterung
  hinzugefügt, mit der NVDA Sie benachrichtigen kann, wenn Sie ganz oben
  oder ganz unten im Playlist-Viewer angelangt sind.
* Beim Zurücksetzen der Einstellungen für die Studio-Erweiterung können Sie
  nun festlegen, was zurückgesetzt werden soll. Standardmäßig werden die
  Einstellungen der Erweiterung zurückgesetzt, wobei die Kontrollkästchen
  für das Zurücksetzen des Instant-Switch-Profils, des temporären Profils,
  der Encoder-Einstellungen und des Löschens von Titelkommentaren im
  Einstellungsdialog hinzugefügt wurden.
* Im Track Tool können Sie Informationen über Album und CD-Code erhalten,
  indem Sie STRG+NVDA+9 bzw. STRG+NVDA+0 drücken.
* Performance-Verbesserungen beim erstmaligen Abrufen von
  Spalteninformationen in Track Tool.
* 8.0: Es wurde ein Dialog in den Einstellungen für die SPL-Erweiterung
  hinzugefügt, um Platzhalter für den Spaltenexplorer für das Track-Tool zu
  konfigurieren.
* Sie können nun das Intervall der Mikrofonbenachrichtigung im Dialog
  Mikrofonbenachrichtigung konfigurieren (Alt+NVDA+4).

## Ältere Versionen

Für weitere Änderungsnotizen beachten Sie den Link zu den Änderungsnotizen
älterer Erweiterungsversionen.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: https://addons.nvda-project.org/files/get.php?file=spl-lts18

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
