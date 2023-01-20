# StationPlaylist #

* Autorzy: Geoff Shang, Joseph Lee i inni współpracownicy
* Pobierz [Wersja stabilna][1]
* NVDA compatibility: 2022.4 and later

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
  on GitHub. This add-on readme will list changes from version 23.01 (2023)
  onwards.
* Gdy Studio jest uruchomione, możesz zapisać, ponownie załadować zapisane
  ustawienia lub zresetować ustawienia dodatków do ustawień domyślnych,
  naciskając odpowiednio Control+ NVDA + C, Control + NVDA + R raz lub
  Control + NVDA + R trzy razy. Dotyczy to również ustawień kodera - możesz
  zapisać i zresetować (nie przeładować) ustawienia kodera, jeśli używasz
  koderów.

## Skrót klawiaturowy

Większość z nich będzie działać tylko w Studio, chyba że określono inaczej.

* Alt+Shift+T z okna Studio: ogłasza czas, jaki upłynął dla aktualnie
  odtwarzanego trakcu.
* Control+Alt+T (przesunięcie dwoma palcami w dół w trybie dotykowym SPL) z
  okna Studio: poinformuj o czasie pozostałym do aktualnie odtwarzanego
  trakcu.
* NVDA + Shift + F12 (przesunięcie dwoma palcami w górę w trybie dotykowym
  SPL) z okna Studio: ogłasza czas nadawcy, taki jak 5 minut do góry
  godziny. Dwukrotne naciśnięcie tego polecenia spowoduje ogłoszenie minut i
  sekund do góry godziny.
* Alt+NVDA+1 (przesunięcie dwoma palcami w prawo w trybie SPL) z okna
  Studio: Otwiera kategorię alarmów w oknie dialogowym konfiguracji dodatku
  Studio.
* Alt+NVDA+1 z Creator's Playlist Editor i Remote VT playlist Editor:
  informuje o zaplanowanym czasie załadowania playlisty.
* Alt+NVDA+2 w Edytorze list odtwarzania Creatora i Zdalnym edytorze list
  odtwarzania VT: informuje o całkowitym czasie trwania playlisty.
* Alt + NVDA + 3 z okna Studio: Przełącz eksplorator wózka, aby nauczyć się
  przydziałów koszyka.
* Alt+NVDA+3 z Creator's Playlist Editor i Remote VT playlist Editor:
  informuje o zaplanowanym odtwarzaniu wybranego utworu.
* Alt+NVDA+4 z Creator's Playlist Editor i Remote VT playlist Editor:
  Informuje o rotacji i kategorii powiązanej z załadowaną playlistą.
* Control+NVDA+f z okna Studio: Otwiera okno dialogowe, w którym można
  znaleźć utwór na podstawie nazwy wykonawcy lub utworu. Naciśnij NVDA+F3,
  aby znaleźć do przodu, lub NVDA+Shift+F3, aby znaleźć do tyłu.
* Alt+NVDA+R z okna Studio: Kroki przez ustawienia anonsu skanowania
  biblioteki.
* Control+Shift+X z okna Studio: Kroki przez ustawienia czasomierza
  Braille'a.
* Control+Alt+strzałka w lewo/w prawo (podczas gdy skupiasz się na ścieżce w
  Studio, Creator, Remote VT i Track Tool): Przejdź do poprzedniej/następnej
  kolumny ścieżki.
* Control+Alt+strzałka w górę/w dół (podczas gdy skupiasz się na ścieżce w
  Studio, Creator, Remote VT i Track Tool): Przejdź do
  poprzedniego/następnego utworu i ogłoś określone kolumny.
* Control+NVDA+1 do 0 (podczas gdy skupiasz się na ścieżce w Studio, Creator
  (w tym Edytorze playlist), Remote VT i Track Tool): Ogłaszaj zawartość
  kolumny dla określonej kolumny (domyślnie pierwsze dziesięć
  kolumn). Dwukrotne naciśnięcie tego polecenia spowoduje wyświetlenie
  informacji o kolumnie w oknie trybu przeglądania.
* Control+NVDA+- (łącznik podczas skupiania się na ścieżce w Studio,
  Creator, Remote VT i Track Tool): wyświetla dane dla wszystkich kolumn w
  ścieżce w oknie trybu przeglądania.
* NVDA+V podczas skupiania się na utworze (tylko przeglądarka list
  odtwarzania Studio): przełącza zapowiedzi kolumn ścieżek między
  kolejnością ekranu a kolejnością niestandardową.
* Alt+NVDA+C podczas skupiania się na utworze (tylko przeglądarka list
  odtwarzania Studio): ogłasza ewentualne komentarze do utworów.
* Alt+NVDA+0 z okna Studio: Otwiera okno dialogowe konfiguracji dodatku
  Studio.
* Alt+NVDA+P z okna Studio: Otwiera okno dialogowe Profile emisji Studio.
* Alt+NVDA+F1: Otwórz okno dialogowe powitania.

## Nieprzypisane polecenia

Następujące polecenia nie są domyślnie przypisywane; Jeśli chcesz je
przypisać, użyj okna dialogowego Gesty wprowadzania, aby dodać
niestandardowe polecenia. Aby to zrobić, w oknie Studio otwórz menu NVDA,
Preferencje, a następnie Gesty wprowadzania. Rozwiń kategorię
StationPlaylist, a następnie znajdź nieprzypisane polecenia z poniższej
listy i wybierz "Dodaj", a następnie wpisz gest, którego chcesz użyć.

Ważne: niektóre z tych poleceń nie będą działać, jeśli NVDA działa w trybie
bezpiecznym, na przykład z ekranu logowania.

* Przełączanie do okna SPL Studio z dowolnego programu (niedostępne w trybie
  bezpiecznym).
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
* Znajdowanie tekstu w określonych kolumnach.
* Znajdź ścieżki z czasem trwania, który mieści się w danym zakresie za
  pomocą wyszukiwarki zakresów czasu.
* Szybko włączaj lub wyłączaj przesyłanie strumieniowe metadanych.

## Dodatkowe polecenia podczas korzystania z koderów

Następujące polecenia są dostępne podczas korzystania z koderów:

* F9: podłącz wybrany koder.
* F10 (tylko koder SAM): Odłącz wybrany koder.
* Control+F9: Podłącz wszystkie enkodery.
* Control+F10 (tylko koder SAM): Odłącz wszystkie enkodery.
* F11: Przełącza, czy NVDA przełączy się do okna Studio dla wybranego
  kodera, jeśli jest podłączony.
* Shift+F11: Przełącza, czy Studio będzie odtwarzać pierwszy wybrany utwór,
  gdy koder jest podłączony do serwera przesyłania strumieniowego.
* Control+F11: Przełącza monitorowanie w tle wybranego kodera.
* Control+F12: otwiera okno dialogowe z wyborem usuniętego kodera (w celu
  wyrównania etykiet i ustawień kodera).
* Alt+NVDA+0 i F12: Otwiera okno dialogowe ustawień kodera, aby
  skonfigurować opcje, takie jak etykieta kodera.

Ponadto dostępne są polecenia przeglądu kolumn, w tym:

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

Dostępne polecenia to:

* O: Automatyzacja.
* C (Shift+C w układzie JAWS): Tytuł aktualnie odtwarzanego utworu.
* C (układ JAWS): Przełącz eksplorator wózka (tylko przeglądarka list
  odtwarzania).
* D (R w układzie JAWS): Pozostały czas trwania listy odtwarzania (jeśli
  zostanie wyświetlony komunikat o błędzie, przejdź do przeglądarki list
  odtwarzania, a następnie wydaj to polecenie).
* E: Stan przesyłania strumieniowego metadanych.
* Shift+1 do Shift+4, Shift+0: Stan dla poszczególnych adresów URL
  przesyłania strumieniowego metadanych (0 oznacza koder DSP).
* F: Znajdź utwór (tylko przeglądarka list odtwarzania).
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

Dostępne polecenia kontrolera SPL to:

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
* C: Tytuł i czas trwania aktualnie odtwarzanego utworu.
* Shift+C: Tytuł i czas trwania nadchodzącego utworu, jeśli taki istnieje.
* E: Stan połączenia enkodera.
* I: Liczba słuchaczy.
* P: Informacje o stanie studia, takie jak to, czy utwór jest odtwarzany,
  mikrofon jest włączony i inne.
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

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer
  supported by Microsoft as of January 2023.
* Removed first and last track column commands (Control+Alt+Home/End) as
  NVDA includes these commands.
* Removed Streamer app module and buffer size edit field workaround as
  Streamer has become an alias module for SPL Engine.

## Starsze wersje

Zobacz link do dziennika zmian, aby uzyskać informacje o wersji dla starych
wydań dodatków.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[3]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
