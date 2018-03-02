# StationPlaylist Studio #

* Authoren: Geoff Shang, Joseph Lee und andere Entwickler
* lade [stable version][1] herunter
* lade [development version][2] herunter

Dieses Erweiterungspaket verbessert die Zugänglichkeit von Station Playlist
Studio. Es stehen außerdem Befehle zur Verfügung, um Station Playlist von
überall aus zu bedienen.

Weitere Informationen zur Erweiterung finden Sie in der
[Add-On-Anleitung][4]. Für Entwickler, welche wissen wollen, wie die
Erweiterung  erstellt wurde, siehe buildInstructions.txt im
Quellcodeverzeichnis der Erweiterung auf Github.

WICHTIGE HINWEISE:

* This add-on requires NVDA 2017.4 or later and StationPlaylist Studio 5.10
  or later.
* Wenn Sie Windows 8 oder höher verwenden, setzen Sie die Reduzierung der
  Lautstärke anderer Audioquellen auf "nie" im Dialog Sprachausgabe im
  NVDA-Einstellungsmenü.
* add-on 8.0/16.10 requires Studio 5.10 or later. For broadcasters using
  Studio 5.0x and/or Windows XP, Vista or 7 without Service Pack 1, a
  [long-term support version][3] (15.x) is available. The last stable
  version to support Windows releases prior to 7 Service Pack 1 is 17.11.2.
* Starting from 2018, [changelogs for old add-on releases][5] will be found
  on GitHub. This add-on readme will list changes from version 5.0 (2015
  onwards).
* Certain add-on features (notably add-on updating) won't work under some
  conditions, including running NVDA in secure mode.
* Due to tecnical limitations, you cannot install or use this add-on on
  Windows Store version of NVDA.

## Tastenkürzel

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
* Alt+NVDA+2 (two finger flick left in SPL mode) from Studio window: Opens
  song intro alarm setting dialog.
* Alt+NVDA+3 from Studio window: Toggles cart explorer to learn cart
  assignments.
* Alt+NVDA+4 from Studio window: Opens microphone alarm dialog.
* Control+NVDA+f from Studio window: Opens a dialog to find a track based on
  artist or song name. Press NvDA+F3 to find forward or NVDA+Shift+F3 to
  find backward.
* Alt+NVDA+R from Studio window: Steps through library scan announcement
  settings.
* Control+Shift+X from Studio window: Steps through braille timer settings.
* Strg+Alt+Links/Rechtspfeil (während der Fokus auf einen Titel gerichtet
  ist): Ansage der vorherigen/nächsten Titelspalte.
* STRG+Alt+Pfeil nach oben/unten (während der Fokus auf einen Titel
  gerichtet ist): Bewegt den Cursor zum vorherigen oder nächsten Titel und
  sagt bestimmte Spalten an (nicht verfügbar in der Version 15.x).
* STRG+NVDA+1 bis 0 (bis 6 für Studio 5.0x): Spalteninhalt für eine
  bestimmte Spalte ankündigen.
* Alt+NVDA+C, während der Fokus auf einen Titel gerichtet ist: Gibt
  Titelkommentare aus, falls vorhanden.
* Alt+NVDA+0 from Studio window: Opens the Studio add-on configuration
  dialog.
* Control+NVDA+- (hyphen) from Studio window: Send feedback to add-on
  developer using the default email client.
* Alt+NVDA+F1: öffnet das Willkommensdialog.

## nicht zugewiesene Befehle

The following commands are not assigned by default; if you wish to assign
them, use Input Gestures dialog to add custom commands.

* Das wechseln zum SPL Studio-Fenster aus einem beliebigen Programm.
* SPL Controller layer.
* Ansage des Studio-Status beim Navigieren in anderen Programmen,
  z.B. Titelwiedergabe.
* SPL Assistant layer from SPL Studio.
* Announce time including seconds from SPL Studio.
* Announcing temperature.
* Announcing title of next track if scheduled.
* Announcing title of the currently playing track.
* Marking current track for start of track time analysis.
* Performing track time analysis.
* nimmt Schnappschüsse aus der Playlist auf.
* Find text in specific columns.
* Find tracks with duration that falls within a given range via time range
  finder.
* Quickly enable or disable metadata streaming.

## Additional commands when using Sam or SPL encoders

The following commands are available when using Sam or SPL encoders:

* F9: Mit einem Streaming-Server verbinden.
* F10 (SAM encoder only): Disconnect from the streaming server.
* Control+F9/Control+F10 (SAM encoder only): Connect or disconnect all
  encoders, respectivley.
* F11: Toggles whether NVDA will switch to Studio window for the selected
  encoder if connected.
* Shift+F11: Toggles whether Studio will play the first selected track when
  encoder is connected to a streaming server.
* Control+F11: Toggles background monitoring of the selected encoder.
* F12: Opens a dialog to enter custom label for the selected encoder or
  stream.
* Control+F12: opens a dialog to select the encoder you have deleted (to
  realign stream labels and encoder settings).
* Alt+NVDA+0: Öffnet den Dialog Encoder-Einstellungen, um Optionen wie
  Streambezeichnung zu konfigurieren.

In addition, column review commands are available, including:

* Control+NVDA+1: Encoder position.
* Control+NVDA+2: stream label.
* Control+NVDA+3 from SAM Encoder: Encoder format.
* Control+NVDA+3 from SPL Encoder: Encoder settings.
* Control+NvDA+4 from SAM Encoder: Encoder connection status.
* Control+NVDA+4 from SPL Encoder: Transfer rate or connection status.
* Control+NVDA+5 from SAM Encoder: Connection status description.

## SPL Assistant layer

This layer command set allows you to obtain various status on SPL Studio,
such as whether a track is playing, total duration of all tracks for the
hour and so on. From any SPL Studio window, press the SPL Assistant layer
command, then press one of the keys from the list below (one or more
commands are exclusive to playlist viewer). You can also configure NvDA to
emulate commands from other screen readers.

The available commands are:

* A: Automatisierung.
* C (Shift+C in JAWS and Window-Eyes layouts): Title for the currently
  playing track.
* C (JAWS- und Window-Eyes-Darstellungen): Wechselt die Cart-Übersicht (nur
  im Playlist-Viewer).
* D (R in der JAWS-Darstellung): Restdauer der Playlist (wenn eine
  Fehlermeldung angezeigt wird, wechseln Sie zum Playlist-Viewer und geben
  Sie diesen Befehl ein).
* E (G in Window-Eyes layout): Metadata streaming status.
* Umschalt+1 bis 4, Umschalt+0: Status für einzelne Metadaten-Streaming-URLs
  (0 ist für DSP-Encoder).
* E (Window-Eyes layout): Elapsed time for the currently playing track.
* F: Titel suchen (nur im Playlist-Viewer).
* H: Duration of music for the current hour slot.
* Umschalt+H: Verbleibende Spieldauer für den Stundenplatzhalter.
* I (L in JAWS or Window-Eyes layouts): Listener count.
* K: Move to the marked track (playlist viewer only).
* Control+K: Set the current track as the place marker track (playlist
  viewer only).
* L (Umschalt+L in JAWS- und Window-Eyes-Darstellungen): Line in.
* M: Mikrofon.
* N: Titel der nächst geplante Datei.
* P: Wiedergabestatus (Wiedergabe oder angehalten).
* Shift+P: Pitch of the current track.
* R (Shift+E in JAWS and Window-Eyes layouts): Record to file
  enabled/disabled.
* Shift+R: Monitor library scan in progress.
* S: Track starts (scheduled).
* Umschalt+S: Zeit bis zur Wiedergabe des ausgewählten Titels (Titel startet
  in...).
* T: Cart edit/insert mode on/off.
* U: Studio up time.
* STRG+Umschalt+U: überprüft, ob Aktualisierungen für die Erweiterung
  vorhanden sind.
* W: Wetter und Temperatur, wenn konfiguriert.
* Y: Playlist modified status.
* 1 bis 0 (bis 6 für Studio 5.0x): sagt den Spalteninhalt für eine bestimmte
  Spalte an.
* F8: nimmt Schnappschüsse von Playlisten auf (Anzahl der Titel, längster
  Titel, etc.).
* F9: Mark current track for track time analysis (playlist viewer only).
* F10: Perform track time analysis (playlist viewer only).
* F12: Switch between current and a predefined profile.
* F1: Layer help.
* Shift+F1: Opens online user guide.

## SPL-Steuerung

The SPL Controller is a set of layered commands you can use to control SPL
Studio anywhere. Press the SPL Controller layer command, and NVDA will say,
"SPL Controller." Press another command to control various Studio settings
such as microphone on/off or play the next track.

The available SPL Controller commands are:

* Drücken Sie P, um den nächsten ausgewählten Titel zu spielen.
* Drücken Sie U, um die Wiedergabe zu Pausieren oder um die Wiedergabe
  fortzusetzen.
* Press S to stop the track with fade out, or to stop the track instantly,
  press T.
* Press M or Shift+M to turn on or off the microphone, respectively, or
  press N to enable microphone without fade.
* Press A to enable automation or Shift+A to disable it.
* Press L to enable line-in input or Shift+L to disable it.
* Press R to hear remaining time for the currently playing track.
* Press Shift+R to get a report on library scan progress.
* Press C to let NVDA announce name and duration of the currently playing
  track.
* Press Shift+C to let NVDA announce name and duration of the upcoming track
  if any.
* Press E to get count and labels for encoders being monitored.
* Drücken Sie I, um die Anzahl der Zuhörer zu ermitteln.
* Drücken Sie Q, um verschiedene Statusinformationen über Studio zu
  erhalten, z. B. ob ein Titel wiedergegeben wird, das Mikrofon
  eingeschaltet ist und mehr.
* Drücken Sie die Cart-Tasten (z.B. F1, STRG+1), um die zugewiesenen Carts
  von überall zu spielen.
* Press H to show a help dialog which lists available commands.

## Track alarms

By default, NvDA will play a beep if five seconds are left in the track
(outro) and/or intro. To configure this value as well as to enable or
disable them, press Alt+NVDA+1 or Alt+NVDA+2 to open end of track and song
ramp dialogs, respectively. In addition, use Studio add-on settings dialog
to configure if you'll hear a beep, a message or both when alarms are turned
on.

## Mikrofon-Alarm

You can ask NVDA to play a sound when microphone has been active for a
while. Press Alt+NVDA+4 to configure alarm time in seconds (0 disables it).

## Track Finder

If you wish to quickly find a song by an artist or by song name, from track
list, press Control+NVDA+F. Type or choose the name of the artist or the
song name. NVDA will either place you at the song if found or will display
an error if it cannot find the song you're looking for. To find a previously
entered song or artist, press NVDA+F3 or NVDA+Shift+F3 to find forward or
backward.

Note: Track Finder is case-sensitive.

## Cart Explorer

Depending on edition, SPL Studio allows up to 96 carts to be assigned for
playback. NVDA allows you to hear which cart, or jingle is assigned to these
commands.

To learn cart assignments, from SPL Studio, press Alt+NVDA+3. Pressing the
cart command once will tell you which jingle is assigned to the
command. Pressing the cart command twice will play the jingle. Press
Alt+NvDA+3 to exit cart explorer. See the add-on guide for more information
on cart explorer.

## Track time analysis

To obtain length to play selected tracks, mark current track for start of
track time analysis (SPL Assistant, F9), then press SPL Assistant, F10 when
reaching end of selection.

## Columns Explorer

STRG+NVDA+1 bis 0 (bis 6 für Studio 5.0x) oder im SPL-Assistenten, 1 bis 0
(bis 6 für Studio 5.01 und früher): Ansage der Inhalte bestimmter
Spalten. Standardmäßig sind dies Künstler, Titel, Dauer, Intro, Kategorie
und Dateiname (Studio 5.10 fügt Jahr, Album, Genre und Zeitplan hinzu). Sie
können konfigurieren, welche Spalten durchsucht werden sollen, indem Sie den
Spalten-Explorer-Dialog verwenden. Sie finden diesen Dialog im Dialogfeld
"Einstellungen für die Studio-Erweiterung".

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

## Configuration dialog

From studio window, you can press Alt+NVDA+0 to open the add-on
configuration dialog. Alternatively, go to NVDA's preferences menu and
select SPL Studio Settings item. This dialog is also used to manage
broadcast profiles.

## SPL touch mode

If you are using Studio on a touchscreen computer running Windows 8 or later
and have NVDA 2012.3 or later installed, you can perform some Studio
commands from the touchscreen. First use three finger tap to switch to SPL
mode, then use the touch commands listed above to perform commands.

## Version 18.03/15.14-LTS

* If NVDA is configured to announce metadata streaming status when Studio
  starts, NVDA will honor this setting and no longer announce streaming
  status when switching to and from instant switch profiles.
* If switching to and from an instant switch profile and NVDA is configured
  to announce metadata streaming status whenever this happens, NVDA will no
  longer announce this information multiple times when switching profiles
  quickly.
* NVDA will remember to switch to the appropriate time-based profile (if
  defined for a show) after NVDA restarts multiple times during broadcasts.
* If a time-based profile with profile duration set is active and when
  add-on settings dialog is opened and closed, NVDA will still switch back
  to the original profile once the time-based profile is finished.
* If a time-based profile is active (particularly during broadcasts),
  changing broadcast profile triggers via add-on settings dialog will not be
  possible.

## Version 18.02/15.13-LTS

* 18.02: Due to internal changes made to support extension points and other
  features, NVDA 2017.4 is required.
* Add-on updating won't be possible under some cases. These include running
  NVDA from source code or with secure mode turned on. Secure mode check is
  applicable to 15.13-LTS as well.
* If errors occur while checking for updates, these will be logged and NVDA
  will advise you to read the NVDA log for details.
* In add-on settings, various update settings in advanced settings section
  such as update interval will not be displayed if add-on updating is not
  supported.
* NVDA will no longer appear to freeze or do nothing when switching to an
  instant switch profile or a time-based profile and NVDA is configured to
  announce metadata streaming status.

## Version 18.01/15.12-LTS

* When using JAWS layout for SPL Assistant, update check command
  (Control+Shift+U) now works correctly.
* When changing microphone alarm settings via the alarm dialog (Alt+NVDA+4),
  changes such as enabling alarm and changes to microphone alarm interval
  are applied when closing the dialog.

## Version 17.12

* Windows 7 Service Pack 1 oder höher ist erforderlich.
* Mehrere Zusatzfunktionen wurden erweitert. Dadurch können
  Mikrofonbenachrichtigung und Metadaten-Streaming auf Änderungen in
  Broadcast-Konfigurationsprofilen reagieren. Dies erfordert NVDA 2017.4.
* Beim Beenden des Studio schließen sich verschiedene Erweiterungsdialoge
  wie Einstellungen, Benachrichtigungsdialoge und andere automatisch. Dies
  erfordert NVDA 2017.4.
* Added a new command in SPL Controller layer to announce name of the
  upcoming track if any (Shift+C).
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
  den SPL-Controller-Layer zu erhalten.

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

* NVDA will no longer fail to cause Studio to play the first track when an
  encoder is connected.

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
  Anfragenfenster beim Eintreffen von Anfragen geöffnet werden.
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
* Added a checkbox in add-on settings dialog to suppress announcement of
  column headers when reviewing tracks in playlist viewer.
* Added a command in SPL Controller layer to announce name and duration of
  the currently playing track from anywhere (C).
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
* Added a combo box in add-on settings dialog to set which column should be
  announced when moving through columns vertically.
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
* Added a new command in SPL Controller layer to announce Studio status such
  as track playback and microphone status (Q).

## Version 17.03

* NVDA wird keine irreführenden Aktionen  mehr ausführen und auch keine
  Fehlerton mehr abspielen, wenn auf  ein temporäres Sendeprofil gewechselt
  wird.
* Übersetzungen aktualisiert

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
* Übersetzungen aktualisiert

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
* Übersetzungen aktualisiert

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
  Alt+NvDA+0. Dies wurde geändert, damit STRG+NVDA+Zajlenreihe dem
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
* Added a setting in add-on settings dialog to let NVDA notify you if you've
  reached top or bottom of playlist viewer.
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
* 8.0: Added a dialog in add-on settings to configure Columns Explorer slots
  for Track Tool.
* Sie können nun das Intervall der Mikrofonbenachrichtigung im Dialog
  Mikrofonbenachrichtigung konfigurieren (Alt+NVDA+4).

## Version 7.5/16.09

* NVDA öffnet den Fortschrittsdialog nicht mehr, wenn sich der Update-Kanal
  der Erweiterung gerade geändert hat.
* NVDA berücksichtigt den ausgewählten Update-Kanal beim Herunterladen von
  Updates.
* Übersetzungen aktualisiert

## Version 7.4/16.08

Version 7.4 ist auch bekannt als 16.08 nach der Jahr/Monat-Versionsnummer
für stabile Versionen.

* Es ist jetzt möglich, aus den Einstellungen zur
  Studio-Erweiterung/Erweiterte Optionen einen Aktualisierungskanal für die
  Erweiterung auszuwählen, der später im Jahr 2017 entfernt werden soll. Für
  7.4 verfügbare Kanäle sind Beta, stabil und langfristig.
* Es wurde eine Einstellung in dem Einstellungsdialog für die
  Studio-Erweiterung/Erweiterte Optionen hinzugefügt, um das Prüfintervall
  für Aktualisierungen zwischen 1 und 30 Tagen zu konfigurieren (Standard
  ist 7 oder wöchentliche Prüfungen).
* Der Befehl SPL-Controller und der Befehl zum Fokussieren auf Studio stehen
  auf geschützten Bildschirmen nicht zur Verfügung.
* Neue und aktualisierte Übersetzungen und lokalisierte Dokumentation in
  verschiedenen Sprachen.

## Änderungen in7.3

* Leichte Performance-Verbesserungen beim Nachschlagen von Informationen
  über einige Befehle des SPL-Assistenten wie z.B. Automatisierung.
* Übersetzungen aktualisiert

## Änderungen in7.2

* Aufgrund der Entfernung des alten internen Konfigurationsformats ist es
  zwingend erforderlich das Add-on 7.2 zu installieren. Nach der
  Installation können Sie nicht mehr auf eine frühere Version des Add-ons
  zurückgreifen.
* Added a command in SPL Controller to report listener count (I).
* Mit Alt+NVDA+0 können Sie nun die Einstellungen zur Studio-Erweiterung und
  die Dialoge für die Encoder-Einstellungen öffnen. Sie können diese Dialoge
  auch weiterhin mit Control+NVDA+0 öffnen (in der Version 8.0 nur noch
  Alt+NVDA+0 verfügbar).
* Im Track Tool können Sie mit Strg+Alt+Links oder Rechtspfeil zwischen den
  Spalten navigieren.
* Inhalte verschiedener Studio-Dialoge, wie z.B. Info-Dialog in Studio 5.1x,
  werden nun angesagt.
* Bei SPL-Encodern schaltet NVDA den Verbindungston aus, wenn Auto-Connect
  aktiviert ist und während dem Verbindungsaufbau diese Option aus dem
  Encoder-Kontextmenü ausgeschaltet wird.
* Übersetzungen aktualisiert

## Änderungen in7.1

* Fehler behoben, die beim Upgrade von Version 5.5 und älter auf 7.0
  aufgetreten sind.
* Wenn Sie beim Zurücksetzen der Einstellungen mit "nein" antworten, werden
  Sie zum Dialogfeld "Einstellungen zur Studio-Erweiterung" zurückgeleitet
  und NVDA merkt sich die Einstellungen des Instant-Switch-Profils.
* NVDA wird Sie auffordern Streambezeichnungen und andere Encoder-Optionen
  neu zu konfigurieren, wenn die Encoder-Konfigurationsdatei beschädigt ist.

## Änderungen in7.0

* Added add-on update check feature. This can be done manually (SPL
  Assistant, Control+Shift+U) or automatically (configurable via advanced
  options dialog from add-on settings).
* Es ist nicht mehr erforderlich, im Fenster für den Playlist-Viewer zu
  bleiben, um die meisten Hilfsbefehle des SPL-Assistenten aufzurufen oder
  Zeitansagen wie die verbleibende Zeit für den Titel und die Sendezeit zu
  erhalten.
* Änderungen an den Befehlen des SPL-Assistenten, einschließlich der
  Playlist-Dauer (D), Neuzuweisung der Auswahl der Stundendauer von
  Umschalt+H zu Umschalt+S. Umschalt+H wird nun verwendet, um die Dauer der
  verbleibenden Titel für den aktuellen Stundenplatzhalter anzusagen. Neuer
  Statusbefehl für Metadaten-Streaming (1 bis 4, 0 ist jetzt Umschalt+1 bis
  Shift+4 bzw. Umschalt+0).
* Es ist nun möglich, den Titelfinder über den SPL-Assistenten (F)
  aufzurufen.
* Im SPL-Assistenten können die Zahlen 1 bis 0 (bis 6 für Studio 5.01 und
  früher) verwendet werden, um bestimmte Spalteninformationen
  anzukündigen. Diese Spaltenslots können unter dem Eintrag Spaltenexplorer
  im Einstellungsdialog zur Studio-Erweiterung geändert werden.
* Es wurden zahlreiche Fehler behoben, die von Benutzern bei der
  Erstinstallation von Add-on 7.0 gemeldet wurden, wenn keine
  Vorgängerversion dieser Erweiterung installiert war.
* Verbesserungen bei der Titeleingabe, einschließlich verbesserter
  Reaktionsfähigkeit beim Bewegen durch Spalten und Verfolgen der
  Darstellung von Spalten auf dem Bildschirm.
* Mit Strg+Alt+Links oder Rechtspfeil können Sie nun  zwischen den Spalten
  der Titel wechseln.
* Es ist nun möglich, für die Befehle des SPL-Assistenten ein anderes
  Screenreader-Befehlslayout zu verwenden. Wechseln Sie in den Dialog
  Erweiterte Optionen aus den Einstellungen zur Studio-Erweiterung, um
  zwischen NVDA-, JAWS- und Window-Eyes-Darstellungen zu wechseln. Für
  weitere Informationen siehe die Befehle des SPL-Assistenten weiter oben.
* NVDA kann so konfiguriert werden, dass es zu einem bestimmten Sendeprofil
  an einem bestimmten Tag und zu einer bestimmten Uhrzeit
  wechselt. Verwenden Sie den neuen Triggerdialog in den Einstellungen zur
  Studio-Erweiterung, um dies einzustellen.
* NVDA meldet den Namen des Profils, zu dem über den Instant-Switch-Schalter
  (F12 im SPL-Assistenten) gewechselt wurde, oder auch beim Aktivieren des
  temporären Profils.
* Der Schalter für den Instant-Switch (jetzt ein Kontrollkästchen) wurde in
  den neuen Triggerdialog verschoben.
* Einträge in der Ausklappliste für die Profile in den Einstellungen zur
  Erweiterung beinhalten nun Profil-Flags, wie z.B. aktiv, ob es sich um ein
  Instant-Switch-Profil handelt und so weiter.
* Wenn ein ernsthaftes Problem mit dem Lesen von Sendeprofildateien gefunden
  wird, zeigt NVDA einen Fehlerdialog an, setzt die Einstellungen auf die
  Standardwerte zurück und spielt keinen Fehlerton mehr ab.
* Einstellungen werden nur dann auf der Festplatte gespeichert, wenn Sie die
  Einstellungen ändern. Dies verlängert die Lebensdauer von SSDs (Solid
  State Drives), indem unnötige Sicherungen auf der Festplatte vermieden
  werden, wenn keine Einstellungen geändert wurden.
* Im Einstellungsdialog zur Studio-Erweiterung wurden die Steuerelemente zum
  Umschalten der Ansage der geplanten Zeit, der Anzahl der Zuhörer, des
  Cart-Namens und der Titelbezeichnung in einen dedizierten Dialog für
  Statusansagen verschoben (wählen Sie die Schaltfläche für Statusansagen,
  um diesen Dialog zu öffnen).
* Es wurde eine neue Einstellung im Dialogfeld "Einstellungen zur
  Studio-Erweiterung" hinzugefügt, mit der NVDA beim Wechseln zwischen
  Titeln im Playlist-Viewer für verschiedene Titelkategorien einen Piepton
  abspielen kann.
* Der Versuch, die Metadaten-Konfigurationseinstellung im Einstellungsdialog
  zur Erweiterung zu öffnen, während der schnelle Metadaten-Streaming-Dialog
  geöffnet ist, führt nicht mehr zu einem Fehlerton. NVDA fordert Sie nun
  auf, den Dialog Metadaten-Streaming zu schließen, bevor Sie die
  Einstellungen öffnen können.
* Bei der Ansage der Zeit, wie z.B. der Restdauer für den laufenden Titel,
  werden auch die Stunden angesagt. Daher ist die Einstellung der
  Stundenansagen standardmäßig aktiviert.
* Wenn Sie R im SPL-Controller drücken, sagt NVDA nun die verbleibende Zeit
  in Stunden, Minuten und Sekunden an.
* In Encodern wird durch Drücken von STRG+NVDA+0 ein Dialogfeld für die
  Encoder-Einstellungen angezeigt, in dem verschiedene Optionen wie
  Streambezeichnung, Fokussierung auf Studio bei Verbindungsaufbau
  usw. konfiguriert werden können.
* In Encodern ist es nun möglich, den Ton für den Verbindungsfortschritt
  abzuschalten (konfigurierbar über den Dialog Encoder-Einstellungen).

## Änderungen in6.4

* Es wurde ein signifikantes Problem behoben, das beim Zurückschalten von
  einem Instant-Switch-Profil auftrat und das Instant-Switch-Profil nach dem
  Löschen eines Profils an der vorherigen Position wieder aktiv wurde. Beim
  Versuch ein Profil zu löschen wird bei aktivem Instant-Switch-Profil ein
  Warndialog angezeigt.

## Änderungen in6.3

* Verbesserungen der internen Sicherheit.
* Wenn Version 6.3 oder höher auf einem Computer mit Windows 8 oder höher
  mit NVDA 2016.1 oder höher gestartet wird, wird ein Warndialog angezeigt,
  in dem Sie aufgefordert werden die Reduzierung der Lautstärke anderer
  Anwendungen (NVDA+Umschalt+D) zu deaktivieren. Markieren Sie das
  Kontrollkästchen, um diesen Dialog in Zukunft zu unterdrücken.
* Es wurde ein Befehl hinzugefügt, um Fehlerberichte, Funktionsvorschläge
  und anderes Feedback an die Entwickler der Erweiterung zu senden
  (STRG+NVDA+Bindestrich) "-".
* Übersetzungen aktualisiert

## Änderungen in6.2

* Im SPL-Assistenten wurde ein Problem mit dem Befehl "Playlist Restdauer"
  (D) (R, wenn Kompatibilitätsmodus eingeschaltet ist) behoben, bei dem die
  Dauer für die aktuelle Stunde statt der gesamten Playlist angesagt
  wurde. Das Verhalten dieses Befehls kann über die erweiterten
  Einstellungen im Dialogfeld "Einstellungen zur Studio-Erweiterung"
  konfiguriert werden.
* NVDA kann nun den Namen des aktuell abgespielten Titels bekannt geben,
  während ein anderes Programm verwendet wird (konfigurierbar über
  Einstellungen zur Studio-Erweiterung).
* Die Einstellung, mit der der Befehl für den SPL-Controller den
  SPL-Assistenten aufrufen kann, wird nun berücksichtigt (vorher war er
  immer aktiviert).
* Bei SAM-Encodern funktionieren die Befehle STRG+F9 und STRG+F10 nun
  korrekt.
* Bei Encodern startet NVDA nun automatisch den Hintergrund-Monitor, wenn
  ein Encoder zuerst fokussiert wird und wenn dieser Encoder so konfiguriert
  ist, dass er im Hintergrund überwacht wird.

## Änderungen in6.1

* Die Reihenfolde der Spaltenansagen und -einbindung sowie
  Metadaten-Streaming-Einstellungen sind nun profilspezifische
  Einstellungen.
* Beim Ändern von Profilen werden die korrekten Metadatenströme aktiviert.
* Beim Öffnen des Einstellungsdialogs für das schnelle Metadaten-Streaming
  (Befehl nicht zugewiesen) werden die geänderten Einstellungen nun auf das
  aktive Profil angewendet.
* Beim Start von Studio wurde die Anzeige der Fehler geändert, wenn das
  einzige beschädigte Profil das normale Profil ist.
* Beim Ändern bestimmter Einstellungen mit Hilfe von Tastenkombinationen,
  wie z.B. Statusmeldungen, wurde ein Problem behoben, wo die geänderten
  Einstellungen beim Wechseln zu und von einem Instant-Switch-Profil nicht
  beibehalten wurden.
* Wenn Sie einen SPL-Assistenten-Befehl mit einer benutzerdefinierten
  Tastaturkombination verwenden (z. B. Befehl für den nächsten Titel), ist
  es nicht mehr erforderlich, im Playlist-Viewer des Studios zu bleiben. Die
  Befehle können nun aus anderen Studio-Fenstern ausgeführt werden.

## Änderungen in6.0

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
* Die Ansage von Titelspalten kann jetzt neu angeordnet und die Ansage
  bestimmter Spalten kann nun unterdrückt werden. Dies gilt nur, wenn das
  Kontrollkästchen "Bildschirmreihenfolge verwenden" im Dialogfeld
  "Einstellungen zur Erweiterung" deaktiviert ist. Verwenden Sie den Dialog
  "Spaltenansagen verwalten", um Spalten neu anzuordnen.
* Es wurde ein Dialog hinzugefügt, um schnell und einfach
  Metadaten-Streaming umzuschalten. Ein Tastaturbefehl wurde noch nicht
  zugewiesen.
* Im Dialogfeld "Einstellungen zur Erweiterung" kann jetzt konfiguriert
  werden, wann der Status des Metadaten-Streaming angekündigt werden
  soll. Das Streaming von Metadaten kann in diesem Dialog auch aktiviert
  werden.
* Es wurde die Möglichkeit hinzugefügt, einen Titel im SPL-Assistenten als
  Lesezeichen zu setzen, um später zu ihm zurückzukehren. STRG+K zum
  Einstellen, K zum Bewegen zum markierten Titel.
* Die Performance bei der Suche nach dem nächsten oder vorherigen Titeltext,
  der den gesuchten Text enthält, wurde verbessert.
* Die Alarmbenachrichtigung kann jetzt als Piepton, Nachricht oder beides
  konfiguriert werden.
* Die periodische Mikrofonbenachrichtigung kann jeztt  zwischen 0
  (deaktiviert) und zwei Stunden (7200 Sekunden) konfiguriert werden. Diese
  Einstellung kann mit den Pfeiltasten nach oben und unten angepasst werden.
* Es wurde eine Einstellung im Dialogfeld "Einstellungen zur Erweiterung"
  hinzugefügt, die eine periodische Benachrichtigung über aktive Mikrofone
  erlaubt.
* Sie können jetzt die Befehlsschicht für das Umschalten der Titelnavigation
  im Studio verwenden, um die Titelnavigation auch in Tracktool
  umzuschalten, sofern Sie keinen Befehl zum Umschalten der Titelnavigation
  im Tracktootl bereits zugewiesen haben.
* Es wurde die Möglichkeit zugefügt, die Befehlsschicht für den
  SPL-Controller zum Aufrufen der Ebene des SPL-Assistenten zu verwenden
  (konfigurierbar über den Dialog "Erweiterte Einstellungen" im Dialogfeld
  "Einstellungen zur Erweiterung").
* NVDA kann nun bestimmte Befehle für den SPL-Assistenten von anderen
  Screenreadern verarbeiten. Um dies zu konfigurieren, gehen Sie zu den
  Einstellungen zur Erweiterung, wählen Sie Erweiterte Einstellungen und
  aktivieren Sie das Kontrollkästchen  Kompatilibilitätsmodus mit anderen
  Screenreadern.
* Einstellungen wie Fokus auf Studio, wenn Encoder verbunden ist, werden
  jetzt dauerhaft gespeichert.
* Es ist nun möglich verschiedene Spalten aus Encoder-Fenstern
  (z.B. Verbindungsstatus) über STRG+NVDA+Zahlen aus der Zahlenreihe
  abzulesen. Siehe die Befehle für den Encoder weiter oben.
* Ein seltener Fehler wurde behoben, bei dem bestimmte Titelbefehle
  (z.B. hinsichtlich der Titelnavigation) nicht wie erwartet
  funktionierten. Dies trat auf, wenn zum Studio-Fenster umgeschaltet oder
  ein NVDA Dialog (einschließlich der Erweiterungsdialoge) geschlossen
  wurde.

## Änderungen in 5.6

* In Studio 5.10 und höher sagt NVDA nicht mehr "nicht ausgewählt", wenn der
  ausgewählte Titel abgespielt wird.
* Aufgrund eines Problems mit Studio selbst wird NVDA den Namen des aktuell
  abgespielten Titels jetzt automatisch ankündigen. Eine Option, um dieses
  Verhalten zu ändern, wurde im Dialog für die Einstellungen der
  Studio-Erweiterung hinzugefügt.

## Änderungen in 5.5

* Die Einstellung für die automatische Wiedergabe nach dem Verbindungsaufbau
  eines Encoders wird gespeichert, auch wenn das Encoder-Fenster verlassen
  wird.

## Änderungen in 5.4

* Beim Durchführen von  Bibliothek-Scans Aus dem Dialog Titelfinder zeigt
  NVDA keine Fehler mehr an. NVDA sagt nun den Scan-Status an, wenn NVDA so
  konfiguriert ist, dass der Scanfortschritt oder Anzahl der Suchläufe
  angekündigt werden sollen.
* Übersetzungen aktualisiert

## Änderungen in 5.3

* Die Fehlerbehebung für SAM Encoder steht jetzt für Benutzer von
  SPL-Encodern zur Verfügung.
* Beim Drücken von f1 für die Hilfe im SPL-Assistenten zeigt NVDA keine
  Fehler mehr an und reagiert entsprechend.

## Änderungen in 5.2

* NVDA erlaubt nicht mehr das Einstellungs- und Benachrichtigungsdialog
  gleichzeitig zu öffnen. Eine Warnung wird angezeigt, welche das Schließen
  des zuvor geöffneten Dialogs vor dem Öffnen eines weiteren Dialogs
  fordert.
* Bei der Überwachung einer oder mehrerer Encoder wird nun durch Drücken von
  e in der SPL-Steuerung die Anzahl der Encoder, Encoder-ID und
  Streambezeichnungen angesagt, falls vorhanden.
* NVDA unterstützt die Befehle Strg   F9 / Strg   F10 zum Verbinden /
  Trennen aller Befehle in SAM-Encodern.
* NVDA wird den nächsten Titel während dem Verbindungsaufbau mit einem
  Encoder nicht mehr abspielen, während Studio einen Titel abspielt. Dies
  gilt, wenn Studio so eingestellt wird, dass Titel nur bei verbundenem
  Encoder abgespielt werden sollen.
* Übersetzungen aktualisiert

## Änderungen in 5.1

* Es ist nun möglich, einzelne Spalten im Tracktool durch Titelnavigation
  abzulesen (Befehl noch nicht zugewiesen). Beachten Sie: das Studio-Fenster
  muss vor der Verwendung dieser Funktion aktiv sein.
* Ein Kontrollkästchen wurde im Einstellungsdialog der Studio-Erweiterung
  hinzugefügt, welches die Ansage des Namens des aktuell aktiven Carts
  ermöglicht.
* Beim Ein- und Ausschalten des Mikrofons werden nun keine Fehlertöne mehr
  abgespielt. Die richtigen Töne werden stattdessen ausgegeben.
* NVDA wird den SPL-Assistenten beenden, wenn ein benutzerdefinierter Befehl
  für einen SPL-Assistent-Layer zugewiesen und dieser Befehl direkt nach dem
  Start des SPL Assistenten gedrückt wird.

## Änderungen in 5.0

* Ein dediziertes Einstellungsdialog für die SPL-Erweiterung wurde
  hinzugefügt. Das Dialog kann aus  dem NVDA-Einstellungsmenü oder durch
  Drücken von STRG+NVDA+0 aus dem SPL-Fenster aufgerufen werden.
* Möglichkeit hinzugefüt, um alle Einstellungen auf die Standardwerte über
  den Konfigurationsdialog zurückzusetzen.
* Wenn einige der Einstellungen Fehler aufweisen, dann werden nur die
  betroffenen Einstellungen auf die Werkseinstellungen zurückgesetzt.
* Eine dedizierte SPL Touchscreen-Unterstützung wurde hinzugefügt, um
  Touch-Befehle für verschiedene Studio-Funktionen nutzen zu können.
* Zu den Änderungen in der Ebene des SPL-Assistenten gehören der neue Befehl
  für die Befehlshilfe (F1) und das Entfernen von Befehlen zum Umschalten
  der Anzahl der Zuhörer (Umschalt+I) sowie die geplante Zeitansage
  (Umschalt+S). Diese Einstellungen können Sie im Dialog Einstellungen für
  die Studio-Erweiterung vornehmen.
* "Umschalt-Benachrichtigung" wurde in "Statusansage" umbenannt, da Pieptöne
  für die Ankündigung anderer Statusinformationen, wie z.B. die
  Fertigstellung von Bibliotheks-Scans, verwendet werden.
* Die Einstellung der Statusansage bleibt nun über alle Sitzungen hinweg
  erhalten. Bisher musste diese Einstellung beim Start von Studio manuell
  konfiguriert werden.
* Sie können nun die Titeleingabe-Funktion verwenden, um Spalten in einem
  Titeleintrag im Playlist-Viewer von Studio zu überprüfen. Zum Umschalten
  dieser Funktion drücken Sie den Befehl, den Sie für diese Funktion
  zugewiesen haben.
* Sie können nun benutzerdefinierte Befehle zuweisen, um
  Temperaturinformationen zu hören oder Bezeichnung des nächsten Titels
  abzurufen.
* Ein Kontrollkästchen für Ende des Titels und Song-Intro wurde in den
  Dialog für Benachrichtigungen eingefügt. Das Kontrollkästchen ermöglicht
  das Aktivieren oder Deaktivieren dieser Benachrichtigungen. Diese können
  auch über die Einstellungen für die Studio-Erweiterung konfiguriert
  werden.
* Es wurde ein Problem behoben, bei dem das Ausführen von Befehlen für den
  Benachrichtigungsdialog oder den Titelfinder eine andere Instanz desselben
  Dialogs anzeigte, während ein anderer Benachrichtigungs- oder Suchdialog
  geöffnet wurde. NVDA öffnet nun eine Meldung, in der Sie aufgefordert
  werden, den zuvor geöffneten Dialog zu schließen.
* Änderungen und Korrekturen für die Cart-Übersicht, einschließlich beim
  Blättern durch fehlerhafte Cart-Stapel, wenn der Benutzer nicht den
  Playlist-Viewer fokussiert. Die Cart-Übersicht überprüft nun, ob der
  Nutzer sich im Playlist-Viewer befindet.
* Es wurde die Möglichkeit hinzugefügt, den Befehl für den Layer des
  SPL-Controllers zu verwenden, um den SPL-Assistenten aufzurufen
  (experimentell; für die Aktivierung siehe Entwicklungshandbuch für
  Erweiterungen).
* In Encoder-Fenstern wird der NVDA-Befehl für die Zeit- und Datumsanzeige
  (standardmäßig NVDA+F12) die Zeit einschließlich Sekunden anzeigen.
* Sie können nun einzelne Encoder auf Verbindungsstatus und andere Meldungen
  überwachen. Drücken Sie dazu STRG+F11, während der zu überwachende Encoder
  fokussiert ist (funktioniert besser bei Verwendung von SAM-Encodern).
* Es wurde ein Befehl in der Befehlsstruktur von SPL-Controller hinzugefügt,
  um den Status der überwachten Encoder anzukündigen (E).
* Eine alternative Lösung für das Zuordnen der Streambezeichnungen zum
  richtigen Encoder von NVDA ist nun verfügbar. NVDA sagte die falsche
  Streambezeichnung insbesondere nach dem Löschen eines Encoders an. Um
  Streabezeichnungen neu zuzuordnen, drücken Sie STRG+F12 und wählen Sie
  dann die Position des Encoders, den Sie entfernt haben.

## Ältere Versionen

Please see changelog link for release notes for old add-on releases.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: http://www.josephsl.net/files/nvdaaddons/getupdate.php?file=spl-lts16

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
