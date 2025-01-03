# StationPlaylist #

* Authors: Christopher Duffley <nvda@chrisduffley.com> (formerly Joseph Lee
  <joseph.lee22590@gmail.com>, originally by Geoff Shang and other
  contributors)

Ovaj paket dodataka omogućava bolje korištenje programa StationPlaylist
Studio i drugih StationPlaylist programa te pruža alate za kontrolu programa
Studio s bilo kojeg mjesta. Podržava sljedeće programe: Studio, Creator,
Track Tool, VT Recorder i Streamer, kao i SAM, SPL i AltaCast kodere.

Za daljnje informacije o dodatku pročitaj [priručnik za dodatke][2].

VAŽNE NAPOMENE:

* Ovaj dodatak zahtijeva StationPlaylist izdanje 5.40 ili noviju verziju.
* Neke funkcije dodatka bit će deaktivirane ili ograničeno raditi, ako NVDA
  radi u sigurnom modusu kao što je prozor prijave.
* Za najbolje iskustvo, deaktiviraj modus stišavanja zvuka.
* Od 2018. godine pa nadalje, [zapisi o promjenama za stara izdanja
  dodatka][3] se nalaze na GitHubu. Readme datoteka dodatka sadrži popis
  promjena od verzije 23.02 (2023.) i nadalje.
* Dok je Studio pokrenut, moguće je spremiti postavke, ponovo učitati
  spremljene postavke ili resetirati postavke dodatka na standardne
  vrijednosti pritiskom tipki kontrol+NVDA+C, pritiskom tipki kontrol+NVDA+R
  jednom ili pritiskom tipki kontrol+NVDA+R tri puta. Ovo se također
  primijenjuje na postavke kodera – moguće je spremiti i resetirati (ali ne
  ponovo učitati) postavke kodera, ako se koderi koriste.
* Many commands will provide speech output while NVDA is in speak on demand
  mode (NVDA 2024.1 and later).

## Tipkovni prečaci

Most of these will work in Studio only unless otherwise specified. Unless
noted otherwise, these commands support speak on demand mode.

* Alt+Shift+T from Studio window: announce elapsed time for the currently
  playing track.
* Control+Alt+T (two finger flick down in SPL touch mode) from Studio
  window: announce remaining time for the currently playing track.
* NVDA+Šift+F12 (klizanje s dva prsta prema gore u dodirnom modusu SPL-a) u
  prozoru Studija: najavljuje vrijeme emitiranja kao što je 5 minuta do
  punog sata. Dvostrukim pritiskom ove naredbe objavit će se minute i
  sekunde do punog sata.
* Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens
  alarms category in Studio add-on configuration dialog (does not support
  speak on demand).
* Alt+NVDA+1 u prozoru Playlist Editora Creatora i Remote VT editoru popisa
  snimaka: najavljuje planirano vrijeme za učitani popisa snimaka.
* Alt+NVDA+2 u prozoru Playlist Editora Creatora i Remote VT editoru popisa
  snimaka: najavljuje ukupno trajanje popisa snimaka.
* Alt+NVDA+3 from Studio window: Toggles cart explorer to learn cart
  assignments (does not support speak on demand).
* Alt+NVDA+3 u prozoru Playlist Editora Creatora i Remote VT editoru popisa
  snimaka: najavljuje planirano vrijeme sviranja za odabranu snimku.
* Alt+NVDA+4 u prozoru Playlist Editora Creatora i Remote VT editoru popisa
  snimaka: najavljuje rotaciju i povezanu kategoriju s učitanim popisom
  snimaka.
* Control+NVDA+f from Studio window: Opens a dialog to find a track based on
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
* Kontrol+NVDA+1 do 0 (tijekom fokusiranja trake u programima Studio,
  Creator (uključujući Playlist Editor), Remote VT i Track Tool): najavi
  sadržaj stupca za određeni stupac (standardno za prvih deset
  stupaca). Pritisni naredbu dvaput za prikaz podataka stupca u prozoru
  modusa pregledavanja.
* Control+NVDA+- (hyphen while focused on a track in Studio, Creator, Remote
  VT, and Track Tool): display data for all columns in a track on a browse
  mode window (does not support speak on demand).
* NVDA+V while focused on a track (Studio's playlist viewer only): toggles
  track column announcement between screen order and custom order (does not
  support speak on demand).
* Alt+NVDA+C tijekom fokusiranja na snimku (samo u prikazu popisa snimaka
  programa Studio): najavljuje komentare snimke, ukoliko ih ima.
* Alt+NVDA+0 from Studio window: Opens the Studio add-on configuration
  dialog (does not support speak on demand).
* Alt+NVDA+P from Studio window: Opens the Studio broadcast profiles dialog
  (does not support speak on demand).
* Alt+NVDA+F1: Open welcome dialog (does not support speak on demand).

## Nedodijeljene naredbe

Sljedeće naredbe standardno nisu dodijeljene; ako ih želiš dodijeliti,
koristi dijaloški okvir „Ulazne geste” za dodavanje prilagođenih naredbi. U
prozoru programa Studio, otvori „Postavke” u NVDA izborniku, a zatim „Ulazne
geste”. Rasklopi kategoriju StationPlaylist. Pronađi nedodijeljene naredbe s
donjeg popisa, odaberi „Dodaj” i upiši gestu koju želiš koristiti.

Important: some of these commands will not work if NVDA is running in secure
mode such as from login screen. Not all commands support speak on demand.

* Switching to SPL Studio window from any program (unavailable in secure
  mode, does not support speak on demand).
* Sloj SPL Kontrolera (nedostupno u sigurnom modusu).
* Najavljivanje stanja porgrama Studio, kao što je sviranje snimaka iz
  drugih programa (nedostupno u sigurnom modusu).
* Najavljivanje stanje veze kodera iz bilo kojeg programa (nedostupno u
  sigurnom modusu).
* Sloj SPL Asistent iz programa SPL Studio.
* Najavi vrijeme sa sekundama iz programa SPL Studio.
* Najavljivanje temperature.
* Najavljivanje naslova sljedeće snimke ako je planirana.
* Najavljivanje naslova trenutačno svirane snimke.
* Označavanje trenutačne snimke kao početak vremenske analize snimaka.
* Izvršavanje vremenske analize snimaka.
* Sastavi statistiku popisa snimaka.
* Find text in specific columns (does not support speak on demand).
* Find tracks with duration that falls within a given range via time range
  finder (does not support speak on demand).
* Quickly enable or disable metadata streaming (does not support speak on
  demand).

## Dodatne naredbe tijekom korištenja kodera

The following commands are available when using encoders, and the ones used
for toggling options for on-connection behavior such as focusing to Studio,
playing the first track, and toggling of background monitoring can be
assigned through the Input Gestures dialog in NVDA menu, Preferences, Input
Gestures, under the StationPlaylist category. These commands do not support
speak on demand.

* F9: Spoji odabrani koder.
* F10 (samo SAM koder): Odspoji odabrani koder.
* Kontrol+F9: Spoji sve kodere.
* Kontrol+F10 (samo SAM koder): Odspoji sve kodere.
* Control+Shift+F11: Toggles whether NVDA will switch to Studio window for
  the selected encoder if connected.
* Šift+F11: U programu Studio uključuje i isključuje sviranje prve odabrane
  snimke kad je koder povezan s poslužiteljem za internetski prijenos.
* Kontrol+F11: Uključuje i isključuje praćenje odabranog kodera u pozadini.
* Kontrol+F12: Otvara dijaloški okvir za biranje izbrisanih kodera (kako bi
  se uskladile oznake kodera i postavke).
* Alt+NVDA+0 or F12: Opens encoder settings dialog to configure options such
  as encoder label.

In addition, column review commands are available, including (supports speak
on demand):

* Kontrol+NVDA+1: Pozicija kodera.
* Kontrol+NVDA+2: Oznaka kodera.
* Kontrol+NVDA+3 u SAM koderu: Format kodera.
* Kontrol+NVDA+3 u SPL-u i AltaCast koderu: Postavke kodera.
* Kontrol+NVDA+4 u SAM koderu: Stanje veze kodera.
* Kontrol+NVDA+4 u SPL-u i AltaCast koderu: Brzina prijenosa ili stanje
  veze.
* Kontrol+NVDA+5 u SAM koderu: Opis stanja veze.

## Sloj SPL Asistent

Ovaj skup naredbi sloja omogućuje dobivanje različitih stanja u programu SPL
Studio, kao što je sviranje snimaka, ukupno trajanje svih snimaka u
određenom satu i tako dalje. U bilo kojem prozoru programa SPL Studio,
pritisni naredbu za sloj SPL Asistent. Zatim pritisni jednu od tipki s
donjeg popisa (jedna ili više naredbi se koriste isključivo u prikazu popisa
snimaka). NVDA čitača možeš konfigurirati i na način, da oponaša naredbe
drugih čitača ekrana.

The available commands are (most commands support speak on demand):

* A: Automatizacija.
* C (Šift+C u JAWS rasporedu): Naslov trenutačno svirane snimke.
* C (JAWS layout): Toggle cart explorer (playlist viewer only, does not
  support speak on demand).
* D (R u JAWS rasporedu): Preostalo vrijeme popisa snimaka (ako se pojavi
  greška, premjesti se na prikaz popisa snimaka te zadaj ovu naredbu).
* Control+D (Studio 6.10 and later): Control keys enabled/disabled.
* E: Stanje internetskog prijenosa metapodataka.
* Šift+1 do Šift+4, Šift+0: Stanje URL adresa pojedinih internetskih
  prijenosa metapodataka (0 je za DSP koder).
* F: Find track (playlist viewer only, does not support speak on demand).
* H: Trajanje snimaka trenutačnog jednosatnog slota.
* Šift+H: Preostalo trajanje snimaka jednosatnog slota.
* I (L u JAWS rasporedu): Broj slušatelja.
* K: Premjesti se na označenu snimku (samo u prikazu popisa snimaka).
* Kontrol+K: Postavi trenutačnu snimku kao pozicijsku oznaku (samo u prikazu
  popisa snimaka).
* L (Šift+L u JAWS rasporedu): Line in.
* M: Mikrofon.
* N: Naslov sljedeće planirane snimke.
* P: Stanje sviranja (svira ili je zaustavljeno).
* Šift+P: Glasnoća trenutačne snimke.
* R (Šift+E u JAWS rasporedu): Snimanje u datoteku uključeno ili isključeno.
* Šift+R: Praćenje skeniranja biblioteke u tijeku.
* S: Početak sviranja snimke (planirano).
* Šift+S: Vrijeme do sviranja odabrane snimke (sviranje snimke započinje
  za).
* T: Modus uređivanja ili dodavanja džinglova uključen ili isključen.
* U: Ukupno vrijeme rada programa Studio.
* W: Vremenska prognoza i temperatura, ukoliko je konfigurirano.
* Y: Stanje promjena popisa snimaka.
* F8: Sastavi statistiku popisa snimaka (broj snimaka, najduža snimka,
  itd.).
* Šift+F8: Zatraži prijepis popisa snimaka u raznim formatima.
* F9: Označi trenutačnu snimku kao početak za vremensku analizu snimaka
  (samo u prikazu popisa snimaka).
* F10: Izvrši vremensku analizu snimke (samo u prikazu popisa snimaka).
* F12: Mijenjaj profil između trenutačnog i unaprijed definiranog.
* F1: Pomoć za slojeve.

## SPL Kontroler

SPL Kontroler je skup naredbi koje se mogu koristiti za upravljanje
programom SPL Studio s bilo kojeg mjesta. Pritisni naredbu sloja SPL
Kontroler i NVDA će izgovoriti: „SPL Kontroler.” Pritisni neku drugu naredbu
za upravljanje raznim Studio postavkama, kao što je uključivanje ili
isključivanje mikrofona ili sviranje sljedeće snimke.

Važno: Naredbe sloja SPL Kontrolera su deaktivirane ako NVDA čitač radi u
sigurnom modusu.

The available SPL Controller commands are (some commands support speak on
demand):

* P: Sviraj sljedeće odabrane snimke.
* U: Pauza ili nastavljanje sviranja.
* S: Prekini svirati snimku sa stišavanjem.
* T: Trenutan prekid.
* M: Uključi mikrofon.
* Shift+M: Isključi mikrofon.
* A: Uključi automatizaciju.
* Shift+A: Isključi automatizaciju.
* L: Uključi line-in unos.
* Shift+L: Isključi line-in unos.
* R: Preostalo vrijeme trenutačno svirane snimke.
* Šift+R: Napredovanje skeniranja biblioteke.
* C: Title and duration of the currently playing track (supports speak on
  demand).
* Shift+C: Title and duration of the upcoming track if any (supports speak
  on demand).
* E: Encoder connection status (supports speak on demand).
* I: Listener count (supports speak on demand).
* Q: Studio status information such as whether a track is playing,
  microphone is on and others (supports speak on demand).
* Tipke za džinglove (npr. F1, Kontrol+1): Sviraj dodijeljene džinglove s
  bilo kojeg mjesta.
* H: Pomoć za slojeve.

## Alarmi za snimke i mikrofon

NVDA je standardno tako postavljen, da svira zvučni signal pri ostatku od
pet sekundi u završnom i-ili uvodnom dijelu snimke, kao i zvučni signal kad
je mikrofon već neko vrijeme aktivan. Za konfiguriranje alarma za snimke i
mikrofon, pritisni Alt+NVDA+1 za otvaranje ostavki alarma u prozoru postavki
Studio dodatka. U tom prozoru možeš i odlučiti, želiš li čuti zvučni signal,
poruku ili oboje, kad su alarmi uključeni.

## Pronalaženje snimaka

Ako s popisa snimaka želi brzo pronaći pjesmu na osnovi izvođača ili imena
pjesme, pritisni Kontrol+NVDA+F. Upiši ili odaberi ime izvođača ili naslov
pjesme. Ako se pronađe, NVDA će te premjestiti na pjesmu. Ako ne može
pronaći pjesmu koju tražiš, prikazat će grešku. Za traženje prethodno
upisane pjesme ili izvođača, pritisni NVDA+F3 ili NVDA+Šift+F3 za traženje
prema naprijed ili natrag.

Napomena: Pronalaženje snimaka razlikuje pisanje velikim i malim slovima.

## Istraživač džìnglova

Ovisno o izdanju, SPL Studio omogućuje dodjeliivanje do 96 džinglova. NVDA
omogućuje čuti koji je džingl dodijeljen ovim naredbama.

Za javljanje dodijeljenih džinglova, u programu SPL Studio pritisni
Alt+NVDA+3. Jednostrukim pritiskom naredbe za džinglove, javit će džingl
koji je dodijeljen naredbi. Dvostrukim pritiskom naredbe, odsvirat će
džingl. Pritisni Alt+NVDA+3 za izlaz iz istraživača džinglova. Pogledaj
priručnik dodatka za daljnje informacije o istraživaču džinglova.

## Vremenska analiza snimaka

Za dobivanje trjanja odabranih snimaka, označi trenutačnu snimku za početak
vremenske analize (SPL Asistent, F9), a zatim pritisni SPL Asistent, F10 kad
dođeš do kraja odabira.

## Istraživač stupaca

Pritiskom na Kontrol+NVDA+1 do 0, dobiva se sadržaj određenih
stupaca. Standardno je to prvih deset stupaca za snimku (u Studio programu:
izvođač, naslov, trajanje, uvodni dio, završni dio, kategorija, godina,
album, žanr i ugođaj). Za uređivača popisa snimaka u Creatoru i Remote VT
klijentu, podaci stupaca ovise o redoslijedu stupaca kako se prikazuju na
ekranu. U programu Studio, u glavnom popisu pjesama Creatora i u Track Tool,
mjesta u stupcima se prikazuju bez obzira na redoslijed stupaca na ekranu i
mogu se konfigurirati u dijaloškom okviru postavki dodataka u kategoriji
istraživača stupaca.

## Najavljivanje stupca snimaka

Možeš zatražiti da NVDA najavi stupce snimaka koje se nalaze u pregledniku
popisa za reprodukciju programa Studio redoslijedom kojim se pojavljuju na
ekranu ili pomoću prilagođenog redoslijeda. Također mođeš isključi određene
stupce. Pritisni NVDA+V za mijenjanje ovog ponašanja dok je fokusirana jedna
snimka u pregledniku popisa za reprodukciju Studija. Za prilagođavanje
uključivanja stupaca i njihov redoslijed, na ploči postavki najava stupaca u
postavkama dodatka, deaktiviraj „Najavi stupce redoslijedom prikazanim na
ekranuu”, a zatim prilagodi uključene stupce i/ili redoslijed stupaca.

## Statistika popisa snimaka

Pritisni SPL Asistent, F8 tijekom fokusa na popis snimaka u programu Studio
za dobivanje raznih statistika o popisu snimaka, uključujući broj snimaka u
popisu snimaka, najdulju snimku, top izvođače i tako dalje. Nakon što
dodijeliš prilagođenu naredbu za ovu funkciju, pritisni prilagođenu naredbu
dvaput, kako bi NVDA prikazao statističke informacije popisa snimkama kao
web stranicu. Na taj način možeš koristiti modus čitanja za kretanje
(pritisni escape za zatvaranje).

## Prijepisi popisa snimaka

Pritiskom na SPL Asistent, Šift+F8 će prikazati dijaloški okvir koji
omogućava zatražiti prijepis popisa snimaka u raznim formatima, uključujući
format običnog teksta, HTML tablice ili popisa.

## Dijaloški okvir konfiguracije

U prozoru programa Studio možeš pritisnuti Alt+NVDA+0 za otvaranje
dijaloškog okvira za konfiguraciju dodatka. Alternativno, idi na NVDA
izbornik Postavke i odaberi stavku SPL Studio postavke. Neke postavke nisu
dostupne ako NVDA radi u sigurnom modusu.

## Dijaloški okvir profila emitiranja

Postavke za određene emisije mogu se spremiti u profile emitiranja. Tim se
profilima može upravljati putem SPL-ovog dijaloškog okvira profila
emitiranja, kojem se može pristupiti pritiskom na Alt+NVDA+P u prozoru
programa Studio.

## Dodirni modus za SPL

Ako koristiš Studio na računalu s ekranom osjetljivim na dodir i
instaliranim NVDA čitačem, neke Studio naredbe možeš izvršiti na ekranu
osjetljivim na dodir. Za prebacivanje na modus SPL-a, dodirni ekran s tri
prsta. Zatim koristi gore navedene dodirne naredbe za njihovo izvršavanje.

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

## Verzija 24.03

* Compatible with NVDA 2024.1.
* Zahtijeva NVDA 2023.3.3 ili noviju verziju.
* Podrška za StationPlaylist izdanje 6.10.
* Most commands support speak on demand (NVDA 2024.1) so announcements can
  be spoken in this mode.

## Verzija 24.01

* The commands for the Encoder Settings dialog for use with the SPL and SAM
  Encoders are now assignable, meaning that you can change them from their
  defaults under the StationPlaylist category in NVDA Menu > Preferences >
  Input Gestures. The ones that are not assignable are the connect and
  disconnect commands. Also, to prevent command conflicts and make much
  easier use of this command on remote servers, the default gesture for
  switching to Studio after connecting is now Control+Shift+F11 (previously
  just F11). All of these can of course still be toggled from the Encoder
  Settings dialog (NVDA+Alt+0 or F12).

## Verzija 23.05

* To reflect the maintainer change, the manifest has been updated to
  indicate as such.

## Verzija 23.02

* Potrebna je NVDA verzija 2022.4 ili novija.
* Potreban je sustav Windows 10 21H2 (aktualizirana verzija iz studenog
  2021./izgradnja 19044) ili novija verzija.
* U pregledniku popisa snimaka programa Studio, NVDA neće najavljivati
  zaglavlja stupaca kao što su izvođač i naslov ako je postavka zaglavlja
  tablice postavljena na „Redci i stupci” ili „Stupci” u NVDA ploči postavki
  formatiranja dokumenta.

## Starija izdanja

Pogledaj poveznicu [zapisnika promjena][3] za bilješke o starim izdanjima
dodatka.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=stationPlaylist

[2]: https://github.com/chrisDuffley/stationplaylist/wiki/SPLAddonGuide

[3]: https://github.com/ChrisDuffley/stationplaylist/wiki/splchangelog
