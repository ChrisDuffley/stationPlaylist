# StationPlaylist #

* Authors: Christopher Duffley <nvda@chrisduffley.com> (formerly Joseph Lee
  <joseph.lee22590@gmail.com>, originally by Geoff Shang and other
  contributors)

Ten pakiet dodatków zapewnia lepsze wykorzystanie StationPlaylist Studio i
innych aplikacji StationPlaylist, a także zapewnia narzędzia do sterowania
Studio z dowolnego miejsca. Obsługiwane aplikacje to Studio, Creator, Track
Tool, VT Recorder i Streamer, a także kodery SAM, SPL i AltaCast.

Aby uzyskać więcej informacji na temat dodatku, przeczytaj [przewodnik po
dodatkach][2].

Ważne uwagi:

* This add-on requires StationPlaylist suite 5.40 or later.
* Niektóre funkcje dodatkowe zostaną wyłączone lub ograniczone, jeśli NVDA
  działa w trybie bezpiecznym, na przykład na ekranie logowania.
* For best experience, disable audio ducking mode.
* Starting from 2018, [changelogs for old add-on releases][3] will be found
  on GitHub. This add-on readme will list changes from version 23.02 (2023)
  onwards.
* Gdy Studio jest uruchomione, możesz zapisać, ponownie załadować zapisane
  ustawienia lub zresetować ustawienia dodatków do ustawień domyślnych,
  naciskając odpowiednio Control+ NVDA + C, Control + NVDA + R raz lub
  Control + NVDA + R trzy razy. Dotyczy to również ustawień kodera - możesz
  zapisać i zresetować (nie przeładować) ustawienia kodera, jeśli używasz
  koderów.
* Many commands will provide speech output while NVDA is in speak on demand
  mode (NVDA 2024.1 and later).

## Skrót klawiaturowy

Most of these will work in Studio only unless otherwise specified. Unless
noted otherwise, these commands support speak on demand mode.

* Alt+Shift+T from Studio window: announce elapsed time for the currently
  playing track.
* Control+Alt+T (two finger flick down in SPL touch mode) from Studio
  window: announce remaining time for the currently playing track.
* NVDA + Shift + F12 (przesunięcie dwoma palcami w górę w trybie dotykowym
  SPL) z okna Studio: ogłasza czas nadawcy, taki jak 5 minut do góry
  godziny. Dwukrotne naciśnięcie tego polecenia spowoduje ogłoszenie minut i
  sekund do góry godziny.
* Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens
  alarms category in Studio add-on configuration dialog (does not support
  speak on demand).
* Alt+NVDA+1 z Creator's Playlist Editor i Remote VT playlist Editor:
  informuje o zaplanowanym czasie załadowania playlisty.
* Alt+NVDA+2 w Edytorze list odtwarzania Creatora i Zdalnym edytorze list
  odtwarzania VT: informuje o całkowitym czasie trwania playlisty.
* Alt+NVDA+3 from Studio window: Toggles cart explorer to learn cart
  assignments (does not support speak on demand).
* Alt+NVDA+3 z Creator's Playlist Editor i Remote VT playlist Editor:
  informuje o zaplanowanym odtwarzaniu wybranego utworu.
* Alt+NVDA+4 z Creator's Playlist Editor i Remote VT playlist Editor:
  Informuje o rotacji i kategorii powiązanej z załadowaną playlistą.
* Control+NVDA+F from Studio window: Opens a dialog to find a track based on
  artist or song name. Press NVDA+F3 to find forward or NVDA+Shift+F3 to
  find backward (does not support speak on demand).
* Alt+NVDA+R from Studio window: Steps through library scan announcement
  settings (does not support speak on demand).
* Control+Shift+X from Studio window: Steps through braille timer settings
  (does not support speak on demand).
* Control+Alt+left/right arrow (while focused on a track in Studio, Creator,
  Remote VT, and Track Tool): Move to previous/next track column (does not
  support speak on demand).
* Control+Alt+up/down arrow (while focused on a track in Studio, Creator,
  Remote VT, and Track Tool): Move to previous/next track and announce
  specific columns (does not support speak on demand).
* Control+NVDA+1 do 0 (podczas gdy skupiasz się na ścieżce w Studio, Creator
  (w tym Edytorze playlist), Remote VT i Track Tool): Ogłaszaj zawartość
  kolumny dla określonej kolumny (domyślnie pierwsze dziesięć
  kolumn). Dwukrotne naciśnięcie tego polecenia spowoduje wyświetlenie
  informacji o kolumnie w oknie trybu przeglądania.
* Control+NVDA+- (hyphen while focused on a track in Studio, Creator, Remote
  VT, and Track Tool): display data for all columns in a track on a browse
  mode window (does not support speak on demand).
* NVDA+V while focused on a track (Studio's playlist viewer only): toggles
  track column announcement between screen order and custom order (does not
  support speak on demand).
* Alt+NVDA+C podczas skupiania się na utworze (tylko przeglądarka list
  odtwarzania Studio): ogłasza ewentualne komentarze do utworów.
* Alt+NVDA+0 from Studio window: Opens the Studio add-on configuration
  dialog (does not support speak on demand).
* Alt+NVDA+P from Studio window: Opens the Studio broadcast profiles dialog
  (does not support speak on demand).
* Alt+NVDA+F1: Open welcome dialog (does not support speak on demand).

## Nieprzypisane polecenia

Następujące polecenia nie są domyślnie przypisywane; Jeśli chcesz je
przypisać, użyj okna dialogowego Gesty wprowadzania, aby dodać
niestandardowe polecenia. Aby to zrobić, w oknie Studio otwórz menu NVDA,
Preferencje, a następnie Gesty wprowadzania. Rozwiń kategorię
StationPlaylist, a następnie znajdź nieprzypisane polecenia z poniższej
listy i wybierz "Dodaj", a następnie wpisz gest, którego chcesz użyć.

Important: some of these commands will not work if NVDA is running in secure
mode such as from login screen. Not all commands support speak on demand.

* Switching to SPL Studio window from any program (unavailable in secure
  mode, does not support speak on demand).
* Warstwa kontrolera SPL (niedostępna w trybie bezpiecznym).
* Ogłaszanie stanu Studio, takiego jak odtwarzanie utworów z innych
  programów (niedostępne w trybie bezpiecznym).
* Ogłaszanie stanu połączenia kodera z dowolnego programu (niedostępne w
  trybie bezpiecznym).
* Warstwa SPL Assistant od SPL Studio.
* Ogłaszaj czas, w tym sekundy z SPL Studio.
* Ogłaszanie temperatury.
* Ogłoszenie tytułu następnego utworu, jeśli jest zaplanowany.
* Zapowiedź tytułu aktualnie odtwarzanego utworu.
* Oznaczanie bieżącego toru w celu rozpoczęcia analizy czasu śledzenia.
* Wykonywanie analizy czasu śledzenia.
* Rób migawki list odtwarzania.
* Find text in specific columns (does not support speak on demand).
* Find tracks with duration that falls within a given range via time range
  finder (does not support speak on demand).
* Quickly enable or disable metadata streaming (does not support speak on
  demand).

## Dodatkowe polecenia podczas korzystania z koderów

The following commands are available when using encoders, and the ones used
for toggling options for on-connection behavior such as focusing to Studio,
playing the first track, and toggling of background monitoring can be
assigned through the Input Gestures dialog in NVDA menu, Preferences, Input
Gestures, under the StationPlaylist category. These commands do not support
speak on demand.

* F9: podłącz wybrany koder.
* F10 (tylko koder SAM): Odłącz wybrany koder.
* Control+F9: Podłącz wszystkie enkodery.
* Control+F10 (tylko koder SAM): Odłącz wszystkie enkodery.
* Control+Shift+F11: Toggles whether NVDA will switch to Studio window for
  the selected encoder if connected.
* Shift+F11: Przełącza, czy Studio będzie odtwarzać pierwszy wybrany utwór,
  gdy koder jest podłączony do serwera przesyłania strumieniowego.
* Control+F11: Przełącza monitorowanie w tle wybranego kodera.
* Control+F12: otwiera okno dialogowe z wyborem usuniętego kodera (w celu
  wyrównania etykiet i ustawień kodera).
* Alt+NVDA+0 or F12: Opens encoder settings dialog to configure options such
  as encoder label.

In addition, column review commands are available, including (supports speak
on demand):

* Control+NVDA+1: Pozycja enkodera.
* Control+NVDA+2: etykieta enkodera.
* Control+NVDA+3 z SAM Encoder: Format enkodera.
* Control+NVDA+3 z SPL i AltaCast Encoder: Ustawienia enkodera.
* Control+NVDA+4 z SAM Encoder: Stan połączenia enkodera.
* Control+NVDA+4 z SPL i AltaCast Encoder: Szybkość transferu lub stan
  połączenia.
* Control+NVDA+5 z SAM Encoder: Opis stanu połączenia.

## Warstwa SPL Assistant

Ten zestaw poleceń warstwy umożliwia uzyskanie różnych statusów w SPL
Studio, takich jak to, czy utwór jest odtwarzany, całkowity czas trwania
wszystkich ścieżek przez godzinę i tak dalej. W dowolnym oknie SPL Studio
naciśnij polecenie warstwy Asystenta SPL, a następnie naciśnij jeden z z
poniższej listy (jedno lub więcej poleceń jest dostępnych wyłącznie w
przeglądarce list odtwarzania). Można również skonfigurować NVDA do emulacji
poleceń z innych czytników ekranu.

The available commands are (most commands support speak on demand):

* O: Automatyzacja.
* C (Shift+C w układzie JAWS): Tytuł aktualnie odtwarzanego utworu.
* C (JAWS layout): Toggle cart explorer (playlist viewer only, does not
  support speak on demand).
* D (R w układzie JAWS): Pozostały czas trwania listy odtwarzania (jeśli
  zostanie wyświetlony komunikat o błędzie, przejdź do przeglądarki list
  odtwarzania, a następnie wydaj to polecenie).
* Control+D (Studio 6.10 and later): Control keys enabled/disabled.
* E: Stan przesyłania strumieniowego metadanych.
* Shift+1 do Shift+4, Shift+0: Stan dla poszczególnych adresów URL
  przesyłania strumieniowego metadanych (0 oznacza koder DSP).
* F: Find track (playlist viewer only, does not support speak on demand).
* H: Czas trwania muzyki dla bieżącego przedziału godzinowego.
* Shift+H: Pozostały czas trwania ścieżki dla szczeliny godzinowej.
* I (L w układzie JAWS): Liczba słuchaczy.
* K: Przejdź do zaznaczonego utworu (tylko przeglądarka playlist).
* Control+K: Ustaw bieżący utwór jako ścieżkę znacznika miejsca (tylko
  przeglądarka list odtwarzania).
* L (Shift+L w układzie JAWS): Wejście liniowe.
* M: Mikrofon.
* N: Tytuł następnego zaplanowanego utworu.
* P: Stan odtwarzania (odtwarzanie lub zatrzymanie).
* Shift+P: Skok bieżącego toru.
* R (Shift+E w układzie JAWS): Zapis do pliku włączony/wyłączony.
* Shift+R: Monitoruj trwające skanowanie biblioteki.
* S: Rozpoczęcie toru (zaplanowane).
* Shift+S: Czas do momentu, w którym wybrana ścieżka zostanie odtworzona
  (ścieżka rozpocznie się w).
* T: Tryb edycji / wstawiania koszyka włączony / wyłączony.
* U: Czas pracy studyjnej.
* W: Pogoda i temperatura, jeśli są skonfigurowane.
* Y: Status zmodyfikowanej playlisty.
* F8: Zrób migawki listy odtwarzania (liczba utworów, najdłuższy utwór
  itp.).
* Shift+F8: Żądaj transkrypcji list odtwarzania w wielu formatach.
* F9: Zaznacz bieżący utwór do rozpoczęcia analizy listy odtwarzania (tylko
  przeglądarka list odtwarzania).
* F10: Przeprowadź analizę czasu utworu (tylko przeglądarka list
  odtwarzania).
* F12: Przełączanie między bieżącym a wstępnie zdefiniowanym profilem.
* F1: Pomoc dotycząca warstwy.

## Kontroler SPL

Kontroler SPL to zestaw warstwowych poleceń, których można używać do
sterowania SPL Studio w dowolnym miejscu. Naciśnij polecenie warstwy
kontrolera SPL, a NVDA powie "Kontroler SPL". Naciśnij inne polecenie, aby
sterować różnymi ustawieniami Studia, takimi jak włączanie/ wyłączanie
mikrofonu lub odtwarzanie następnego utworu.

Ważne: Polecenia warstwy kontrolera SPL są wyłączone, jeśli NVDA działa w
trybie bezpiecznym.

The available SPL Controller commands are (some commands support speak on
demand):

* P: Odtwórz następny wybrany utwór.
* U: Wstrzymaj lub cofnij odtwarzanie.
* S: Zatrzymaj utwór z zanikaniem.
* T: Natychmiastowe zatrzymanie.
* M: Włącz mikrofon.
* Shift+M: Wyłącz mikrofon.
* O: Włącz automatyzację.
* Shift+A: Wyłącz automatyzację.
* L: Włącz wejście liniowe.
* Shift+L: Wyłącz wejście liniowe.
* R: Pozostały czas na aktualnie odtwarzany utwór.
* Shift+R: postęp skanowania biblioteki.
* C: Title and duration of the currently playing track (supports speak on
  demand).
* Shift+C: Title and duration of the upcoming track if any (supports speak
  on demand).
* E: Encoder connection status (supports speak on demand).
* I: Listener count (supports speak on demand).
* Q: Studio status information such as whether a track is playing,
  microphone is on and others (supports speak on demand).
* Koszyka (na przykład F1, Control+1): Odtwarzaj przypisane koszyki z
  dowolnego miejsca.
* H: Pomoc warstwy.

## Śledzenie i alarmy mikrofonowe

Domyślnie NVDA odtwarza sygnał dźwiękowy, jeśli w utworze (outro) i/lub
intro pozostało pięć sekund, a także słyszy sygnał dźwiękowy, jeśli mikrofon
jest aktywny przez jakiś czas. Aby skonfigurować alarmy ścieżek i
mikrofonów, naciśnij Alt+NVDA+1, aby otworzyć ustawienia alarmów na ekranie
ustawień dodatku Studio. Możesz również użyć tego ekranu, aby skonfigurować,
czy po włączeniu alarmów usłyszysz sygnał dźwiękowy, komunikat lub oba te
elementy.

## Wyszukiwarka śladów

Jeśli chcesz szybko znaleźć utwór wykonawcy lub nazwę utworu, z listy
utworów naciśnij Control+NVDA+F. Wpisz lub wybierz nazwę wykonawcy lub nazwę
utworu. NVDA umieści Cię przy utworze, jeśli zostanie znaleziony, lub
wyświetli błąd, jeśli nie może znaleźć utworu, którego szukasz. Aby znaleźć
wcześniej wprowadzony utwór lub wykonawcę, naciśnij NVDA+F3 lub
NVDA+Shift+F3, aby znaleźć do przodu lub do tyłu.

Uwaga: w Wyszukiwarce śladów rozróżniana jest wielkość liter.

## Eksplorator koszyków

W zależności od edycji, SPL Studio pozwala na przypisanie do 96 wózków do
odtwarzania. NVDA pozwala usłyszeć, który wózek lub jingle jest przypisany
do tych poleceń.

Aby nauczyć się przydzielania koszyków, w SPL Studio naciśnij
Alt+NVDA+3. Jednokrotne naciśnięcie polecenia wózka powie Ci, który jingle
jest przypisany do polecenia. Dwukrotne naciśnięcie polecenia wózka
spowoduje odtworzenie dżingla. Naciśnij Alt+NVDA+3, aby wyjść z eksploratora
koszyków. Zobacz przewodnik po dodatkach, aby uzyskać więcej informacji na
temat eksploratora koszyka.

## Śledzenie analizy czasu

Aby uzyskać długość odtwarzania wybranych ścieżek, zaznacz bieżący utwór do
analizy czasu rozpoczęcia ścieżki (SPL Assistant, F9), a następnie naciśnij
SPL Assistant, F10 po osiągnięciu końca wyboru.

## Eksplorator kolumn

Naciskając Control+NVDA+1 do 0, można uzyskać zawartość określonych
kolumn. Domyślnie są to pierwsze dziesięć kolumn dla elementu utworu (w
Studio: wykonawca, tytuł, czas trwania, intro, outro, kategoria, rok, album,
gatunek, nastrój). W przypadku edytora list odtwarzania w creator i remote
VT client dane kolumn zależą od kolejności kolumn wyświetlanej na ekranie. W
Studio, głównej liście utworów Creatora i Narzędziu Śledzenie, gniazda
kolumn są wstępnie ustawione niezależnie od kolejności kolumn na ekranie i
można je skonfigurować w oknie dialogowym ustawień dodatków w kategorii
eksploratora kolumn.

## Śledzenie ogłoszenia kolumn

Możesz poprosić NVDA o ogłoszenie kolumn utworów znalezionych w przeglądarce
list odtwarzania Studio w kolejności, w jakiej pojawiają się na ekranie lub
przy użyciu niestandardowej kolejności i / lub wykluczyć niektóre
kolumny. Naciśnij NVDA+V, aby przełączyć to zachowanie, koncentrując się na
utworze w przeglądarce list odtwarzania Studio. Aby dostosować dołączanie
kolumn i kolejność, w panelu ustawień anonsów kolumn w ustawieniach dodatków
odznacz "Ogłaszaj kolumny w kolejności wyświetlanej na ekranie", a następnie
dostosuj dołączone kolumny i/lub kolejność kolumn.

## Migawki list odtwarzania

Możesz nacisnąć SPL Assistant, F8, koncentrując się na liście odtwarzania w
Studio, aby uzyskać różne statystyki dotyczące listy odtwarzania, w tym
liczbę utworów na liście odtwarzania, najdłuższy utwór, najlepszych
wykonawców i tak dalej. Po przypisaniu niestandardowego polecenia dla tej
funkcji dwukrotne naciśnięcie polecenia niestandardowego spowoduje, że NVDA
wyświetli informacje o migawce listy odtwarzania jako stronę internetową,
dzięki czemu można użyć trybu przeglądania do nawigacji (naciśnij escape,
aby zamknąć).

## Transkrypcje list odtwarzania

Naciskając SPL Assistant, Shift + F8 wyświetli okno dialogowe, które pozwoli
Ci zażądać transkrypcji list odtwarzania w wielu formatach, w tym w formacie
zwykłego tekstu, tabeli HTML lub listy.

## Okno dialogowe konfiguracji

W oknie studio możesz nacisnąć Alt + NVDA + 0, aby otworzyć okno dialogowe
konfiguracji dodatku. Alternatywnie przejdź do menu preferencji NVDA i
wybierz element Ustawienia SPL Studio. Nie wszystkie ustawienia są dostępne,
jeśli NVDA działa w trybie bezpiecznym.

## Okno dialogowe Profile emisji

Ustawienia określonych programów można zapisywać w profilach emisji. Profile
te można zarządzać za pomocą okna dialogowego profili emisji SPL, do którego
można uzyskać dostęp, naciskając Alt + NVDA + P w oknie Studio.

## Tryb dotykowy SPL

If you are using Studio on a touchscreen computer with NVDA installed, you
can perform some Studio commands from the touchscreen. First use three
finger tap to switch to SPL mode, then use the touch commands listed above
to perform commands.

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

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.
* In Studio's playlist viewer, NVDA will not announce column headers such as
  artist and title if table headers setting is set to either "rows and
  columns" or "columns" in NVDA's document formatting settings panel.

## Starsze wersje

Please see the [changelog][3] for release notes for old add-on releases.

[[!tag dev stable]]

[2]: https://github.com/chrisDuffley/stationplaylist/wiki/SPLAddonGuide

[3]: https://github.com/ChrisDuffley/stationplaylist/wiki/splchangelog
