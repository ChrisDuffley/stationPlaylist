# StationPlaylist #

* Autori: Geoff Shang, Joseph Lee i drugi doprinositelji
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]
* Preuzmi [verziju s dugoročnom podrškom][3] – za korisnike porgrama Studio
  5.20
* NVDA kompatibilnost: 2019.3 do 2020.2

Ovaj paket dodataka omogućava bolje korištenje programa StationPlaylist
Studio i drugih StationPlaylist programa te pruža alate za kontrolu programa
Studio s bilo kojeg mjesta. Podržava sljedeće programe: Studio, Creator,
Track Tool, VT Recorder i Streamer, kao i SAM, SPL i AltaCast kodere.

Za više informacija o dodatku, pročitaj [priručnik dodatka][4].

VAŽNE NAPOMENE:

* Ovaj dodatak zahtijeva StationPlaylist izdanje 5.20 ili noviju verziju.
* Korisnicima sustava Windows 8 ili novijeg, preporučamo deaktivirati modus
  stišavanja zvuka.
* Od 2018. godine pa nadalje, [zapisi o promjenama za stara izdanja][5]
  nalaze se na GitHubu. Readme datoteka dodatka sadrži popis promjena od
  verzije 20.01 (2020.) pa nadalje.
* Dok je Studio pokrenut, moguće je spremiti postavke, ponovo učitati
  spremljene postavke ili resetirati postavke dodatka na standardne
  vrijednosti pritiskom tipki kontrol+NVDA+C, pritiskom tipki kontrol+NVDA+R
  jednom ili pritiskom tipki kontrol+NVDA+R tri puta. Ovo se također
  primijenjuje na postavke kodera – moguće je spremiti i resetirati (ali ne
  ponovo učitati) postavke kodera, ako se koderi koriste.

## Tipkovni prečaci

Većina njih radi samo u programu Studio, ukoliko nešto drugo nije navedeno.

* Alt+Šift+T u prozoru Studija: najavi proteklo vrijeme trake koja
  trenutačno svira.
* Kontrol+Alt+T (klizanje s dva prsta prema dolje u dodirnom modusu SPL-a) u
  prozoru Studija: najavi preostalo vrijeme snimke koja trenutačno svira.
* NVDA+Šift+F12 (klizanje s dva prsta prema gore u dodirnom modusu SPL-a) u
  prozoru Studija: najavljuje vrijeme emitiranja kao što je 5 minuta do
  punog sata. Dvostrukim pritiskom ove naredbe objavit će se minute i
  sekunde do punog sata.
* Alt+NVDA+1 (klizanje s dva prsta prema lijevo u dodirnom modusu SPL-a) u
  prozoru Studija: otvara dijaloški okvir s postavkama alarma za uvodni dio
  pjesme.
* Alt+NVDA+1 u prozoru Playlist Editora Creatora i Remote VT editoru popisa
  snimaka: najavljuje planirano vrijeme za učitani popisa snimaka.
* Alt+NVDA+2 u prozoru Playlist Editora Creatora i Remote VT editoru popisa
  snimaka: najavljuje ukupno trajanje popisa snimaka.
* Alt+NVDA+3 u prozoru programa Studio: uključuje i isključuje istraživača
  džinglova za prikaz njima dodijeljenih naredbi.
* Alt+NVDA+3 u prozoru Playlist Editora Creatora i Remote VT editoru popisa
  snimaka: najavljuje planirano vrijeme sviranja za odabranu snimku.
* Alt+NVDA+4 u prozoru Playlist Editora Creatora i Remote VT editoru popisa
  snimaka: najavljuje rotaciju i povezanu kategoriju s učitanim popisom
  snimaka.
* Kontrol+NVDA+f u prozoru Studija: otvara dijaloški okvir za pronalaženje
  snimke na temelju izvođača ili pjesme. Pritisni NVDA+F3 za traženje prema
  naprijed ili NVDA+Šift+F3 za traženje prema natrag.
* Alt+NVDA+R u prozoru Studija: prolazi kroz postavke najave skeniranja
  biblioteke.
* Kontrol+Šift+X u prozoru Studija: prolazi kroz postavke brajeve štoperice.
* Kontrol+Alt+strelica lijevo ili desno (tijekom fokusiranja jedne snimke u
  programima Studio, Creator, Remote VT i Track Tool): prijeđi na prethodni
  ili sljedeći stupac snimaka.
* Kontrol+Alt+Home/End (tijekom fokusiranja jedne snimke u programima
  Studio, Creator, Remote VT i Track Tool): prijeđi na prvi ili zadnji
  stupac snimaka.
* Kontrol+Alt+strelica gore ili dolje (tijekom fokusiranja na snimku u
  programu Studio, Creator, Remote VT i Track Tool): prijeđi na prethodnu
  ili sljedeću snimku i najavi određene stupce.
* Kontrol+NVDA+1 do 0 (tijekom fokusiranja trake u programima Studio,
  Creator (uključujući Playlist Editor), Remote VT i Track Tool): najavi
  sadržaj stupca za određeni stupac (standardno za prvih deset
  stupaca). Pritisni naredbu dvaput za prikaz podataka stupca u prozoru
  modusa pregledavanja.
* Kontrol+NVDA+- (crtica tijekom fokusiranja jedne snimke u programu Studio,
  Creator, Remote VT i Track Tool): prikaži podatke svih stupaca u snimci na
  prozoru modusa pregledavanja.
* Alt+NVDA+C tijekom fokusiranja na snimku (samo Studio): najavljuje
  komentare snimke, ukoliko ih ima.
* Alt+NVDA+0 u prozoru Studija: otvara dijaloški okvir za konfiguriranje
  dodataka.
* Alt+NVDA+P u prozoru Studija: otvara dijaloški okvir za profile
  emitiranja.
* Alt+NVDA+- (crtica) u prozoru Studija: pošalji povratne informacije
  razvojnom programeru dodatka pomoću zadanog klijenta za e-poštu.
* Alt+NVDA+F1: otvara dijaloški okvir za dobrodošlicu.

## Nedodijeljene naredbe

Sljedeće naredbe standardno nisu dodijeljene; ako ih želiš dodijeliti,
koristi dijaloški okvir „Ulazne geste” za dodavanje prilagođenih naredbi. U
prozoru programa Studio, otvori „Postavke” u NVDA izborniku, a zatim „Ulazne
geste”. Rasklopi kategoriju StationPlaylist. Pronađi nedodijeljene naredbe s
donjeg popisa, odaberi „Dodaj” i upiši gestu koju želiš koristiti.

* Prebacivanje na SPL Studio prozor iz bilo koje aplikacije..
* Sloj SPL Kontroler.
* Najavljivanje stanja porgrama Studio, kao što je sviranje snimaka iz
  drugih programa.
* Najavljivanje stanje veze kodera iz bilo kojeg programa.
* Sloj SPL Asistent iz programa SPL Studio.
* Najavi vrijeme sa sekundama iz programa SPL Studio.
* Najavljivanje temperature.
* Najavljivanje naslova sljedeće snimke ako je planirana.
* Najavljivanje naslova trenutačno svirane snimke.
* Označavanje trenutačne snimke kao početak vremenske analize snimaka.
* Izvršavanje vremenske analize snimaka.
* Sastavi statistiku popisa snimaka.
* Nađi tekst u određenim stupcima.
* Nađi snimke čija trajanja odgovaraju određenom vremenskom rasponu, pomoću
  pronalaženja vremenskog raspona.
* Brzo aktiviraj ili deaktiviraj internetski prijenos metapodataka.

## Dodatne naredbe tijekom korištenja kodera

Tijekom korištenja kodera dostupne su sljedeće naredbe:

* F9: Spoji odabrani koder.
* F10 (samo SAM koder): Odspoji odabrani koder.
* Kontrol+F9: Spoji sve kodere.
* Kontrol+F10 (samo SAM koder): Odspoji sve kodere.
* F11: Prekidač za mijenjanje NVDA čitača na prozor programa Studio za
  odabrani koder, ako je povezan.
* Šift+F11: U programu Studio uključuje i isključuje sviranje prve odabrane
  snimke kad je koder povezan s poslužiteljem za internetski prijenos.
* Kontrol+F11: Uključuje i isključuje praćenje odabranog kodera u pozadini.
* Kontrol+F12: Otvara dijaloški okvir za biranje izbrisanih kodera (kako bi
  se uskladile oznake kodera i postavke).
* Alt+NVDA+0: Otvara dijaloški okvir postavki kodera za konfiguriranje
  opcija kao što je oznaka kodera.

Dodatno tome, dostupne su naredbe za pregled stupaca, uključujući sljedeće:

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

Dostupne naredbe su:

* A: Automatizacija.
* C (Šift+C u JAWS rasporedu): Naslov trenutačno svirane snimke.
* C (JAWS raspored): Uključi ili isključi istraživača džinglova (samo u
  prikazu popisa snimaka).
* D (R u JAWS rasporedu): Preostalo vrijeme popisa snimaka (ako se pojavi
  greška, premjesti se na prikaz popisa snimaka te zadaj ovu naredbu).
* E: Stanje internetskog prijenosa metapodataka.
* Šift+1 do Šift+4, Šift+0: Stanje URL adresa pojedinih internetskih
  prijenosa metapodataka (0 je za DSP koder).
* F: Nađi snimku (samo u prikazu popisa snimaka).
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
* Šift+F1: Otvori korisnički priručnik na internetu.

## SPL Kontroler

SPL Kontroler je skup naredbi koje se mogu koristiti za upravljanje
programom SPL Studio s bilo kojeg mjesta. Pritisni naredbu sloja SPL
Kontroler i NVDA će izgovoriti: „SPL Kontroler.” Pritisni neku drugu naredbu
za upravljanje raznim Studio postavkama, kao što je uključivanje ili
isključivanje mikrofona ili sviranje sljedeće snimke.

Dostupne naredbe za SPL Kontroler su:

* Pritisni P za sviranje sljedeće odabrane snimke.
* Pritisni U za pauzu ili za nastavljanje sviranja.
* Pritisni S za zaustavljanje snimke sa stišavanjem. Za trenutno
  zaustavljanje, pritisni T.
* Pritisni M ili Šift+M za uključivanje ili isključivanje
  mikrofona. Pritisni N za aktiviranje mikrofona bez stišavanja.
* Pritisni A za aktiviranje automacije ili Šift+A za njeno deaktiviranje.
* Pritisni L za aktiviranje line-in ulaza ili Šift+L za njegovo
  deaktiviranje.
* Pritisni R za slušanje preostalog vremena trenutačno svirane snimke.
* Pritisni Šift+R za dobivanje izvještaja o napretku skeniranja biblioteke.
* Pritisni C kako bi NVDA najavio ime i trajanje trenutačno svirane snimke.
* Pritisni Šift+C kako bi NVDA najavio ime i trajanje nadolazeće snimke, ako
  je ima.
* Pritisni E za slušanje podatka o tome koji su koderi povezani.
* Pritisni I za broj slušatelja.
* Pritisni Q za razne informacije o stanjima u programu Studio, npr. je li
  se svira neka snimka, je li mikrofon uključen ili nije i drugo.
* Pritisni tipke za džinglove (npr. F1, Kontrol+1) za sviranje dodijeljenih
  džinglova s bilo kojeg mjesta.
* Pritisni H za prikaz dijaloškog okvira za pomoć s popisom dostupnih
  naredbi.

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
izbornik Postavke i odaberi stavku SPL Studio postavke. Ovaj se dijaloški
okvir koristi i za upravljanje profilima za emitiranje.

## Dijaloški okvir profila emitiranja

Postavke za određene emisije mogu se spremiti u profile emitiranja. Tim se
profilima može upravljati putem SPL-ovog dijaloškog okvira profila
emitiranja, kojem se može pristupiti pritiskom na Alt+NVDA+P u prozoru
programa Studio.

## Dodirni modus za SPL

Ako koristiš Studio na računalu s ekranom osjetljivim na dodir s
operacijskim sustavom Windows 8 ili novijim i ako imaš instaliran NVDA
2012.3 ili noviji, možeš izvršiti neke Studio naredbe na ekranu osjetljivim
na dodir. Za prebacivanje na modus SPL-a, dodirni ekran s tri prsta. Zatim
koristi gore navedene dodirne naredbe za njihovo izvršavanje.

## Verzija 20.09-LTS

Verzija 20.09.x posljednja je serija izdanja koja podržava Studio 5.20 i
temelji se na starim tehnologijama, a buduća izdanja podržavaju Studio 5.30
i novije NVDA funkcije. Po potrebi će se neke nove funkcije portirati natrag
na verziju 20.09.x.

* Zbog promjena u NVDA-u, prekidač --spl-configvolatile u naredbenom retku
  više nije dostupan za postavljanje postavki dodatka u stanje
  samo-za-čitanje. To možeš emulirati, ako odznačiš potvrdni okvir „Spremi
  konfiguraciju prilikom isključivanja NVDA” na ploči općih postavki za
  NVDA.
* Uklonjene su postavke probne funkcije iz kategorije „Napredne postavke” u
  postavkama dodataka (Alt+NVDA+0), koje su koristili programeri za
  testiranje najnovijih kodova.
* Naredbe za navigaciju stupaca u programu Studio sada su dostupne u
  popisima snimaka koji se nalaze u ekranima zahtjeva slušatelja, umetanja
  zapisa i drugima.
* Razne naredbe za kretanje po stupcima ponašat će se kao NVDA-ove naredbe
  za kretanje po tablicama. Osim što se time pojednostavljuju same naredbe,
  slabovidnim osobama olakšava njihovu upotrebu.
* Naredbe za okomito kretanje po stupcima (kontrol+Alt+strelica gore/dolje)
  sada su dostupne za Creator, Playlist Editor, Remote VT i Track Tool.
* Naredba za prikaz stupaca snimaka (kontrol+NVDA+crtica) sada je dostupna u
  Playlist Editoru Creatora i Remote VT.
* Naredba za prikaz stupaca snimaka poštivat će redoslijed stupaca prikazan
  na ekranu.
* U SAM koderima, poboljšana je NVDA reakcija pritiskom tipki kontrol+F9 ili
  kontrol+F10 za spajanje odnosno odspajanje svih kodera. To može
  rezultirati u pretjerano opširnom opisu tijekom najave podataka odabranog
  kodera.
* U koderima SPL i AltaCast pritiskom tipke F9 sada će se povezati odabrani
  koder.

## Verzija 20.07

* In Studio's playlist viewer, NVDA will no longer appear to do nothing or
  play error tones when attempting to delete tracks or after clearing the
  loaded playlist while focused on playlist viewer.
* When searching for tracks in Studio's insert tracks dialog, NVDA will
  announce search results if results are found.
* NVDA will no longer appear to do nothing or play error tones when trying
  to switch to a newly created broadcast profile and save add-on settings.
* In encoder settings, "stream label" has been renamed to "encoder label".
* Naredba za označavanje prijenosa (F12) uklonjena je iz kodera. Oznake
  kodera mogu se definirati u dijaloškom okviru postavki kodera
  (Alt+NVDA+0).
* System focus will no longer move to Studio repeatedly or selected track
  will be played when an encoder being monitored in the background
  (Control+F11) connects and disconnects repeatedly.
* In SPL encoders, added Control+F9 command to connect all encoders (same as
  F9 command).

## Verzija 20.06

* Resolved many coding style issues and potential bugs with Flake8.
* Ispravljeni su mnogi slučajevi kodera s govorom poruka na engleskom
  jeziku, iako su prevedene na druge jezike.
* Funkcija vremenski određenih profila emitiranja je uklonjenja.
* Window-Eyes command layout for SPL Assistant has been removed. Window-Eyes
  command layout users will be migrated to NVDA layout.
* Budući da funkcija stišavanja zvuka u NVDA-u ne utječe na prijenos iz
  Studija, osim na specifičnim hardverskim postavama, dijaloški okvir
  podsjetnika za stišavanje zvuka je uklonjen.
* When errors are found in encoder settings, it is no longer necessary to
  switch to Studio window to let NVDA reset settings to defaults. You must
  now switch to an encoder from encoders window to let NVDA reset encoder
  settings.
* The title of encoder settings dialog for SAM encoders now displays encoder
  format rather than encoder position.

## Verzija 20.05

* Initial support for Remote VT (voice track) client, including remote
  playlist editor with same commands as Creator's playlist editor.
* Nardbe koje se upotrebljavaju za otvaranje dijaloškog okvira postavki
  različitih alarma (Alt+NVDA+1, Alt+NVDA+2, Alt+NVDA+4) spojena su u
  Alt+NVDA+1 te će sada otvoriti postavke alarma u postavkama SPL dodatka,
  gdje se mogu pronaći postavke alarma za završni ili uvodni dio snimke i za
  mikrofon.
* In triggers dialog found in broadcast profiles dialog, removed the user
  interface associated with time-based broadcast profiles feature such as
  profile switch day/time/duration fields.
* Profile switch countdown setting found in broadcast profiles dialog has
  been removed.
* As Window-Eyes is no longer supported by Vispero since 2017, SPL Assistant
  command layout for Window-Eyes is deprecated and will be removed in a
  future add-on release. A warning will be shown at startup urging users to
  change SPL Assistant command layout to NVDA (default) or JAWS.
* When using Columns Explorer slots (Control+NVDA+number row commands) or
  column navigation commands (Control+Alt+home/end/left arrow/right arrow)
  in Creator and Remote VT client, NVDA will no longer announce wrong column
  data after changing column position on screen via mouse.
* In encoders and Streamer, NVDA will no longer appear to do nothing or play
  error tones when exiting NVDA while focused on something other than
  encoders list without moving focus to encoders first.

## Verzija 20.04

* Funkcija vremenski određenih profila emitiranja je zastarjela. Prilikom
  prvog pokretanja Studija, prikazat će se poruka upozorenja nakon
  instaliranja dodatka 20.04, ako postoji jedan ili više vremenski određenih
  profila emitiranja.
* Upravljanje profilima emitiranja odvojeno je iz dijaloškog okvira postavki
  SPL dodatka u vlastiti dijaloški okvir. Dijaloškom okviru profila
  emitiranja moguće je pristupiti pritiskom na Alt+NVDA+P u prozoru programa
  Studio.
* Zbog dupliciranja s naredbama za Studio zapise kao što su
  kontrol+NVDA+brojčani redak tipkovnice, naredbe istrživača stupaca
  uklonjene su iz SPL Assistant-a (brojčani redak tipkovnice).
* Izmijenjena je poruka o grešci, koja se prikazuje prilikom pokušaja
  otvaranja dijaloškog okvira postavki Studio-dodatka (kao što je dijaloški
  okvir za prijenos metapodataka) dok je jedan drugi dijaloški okvir
  postavki aktivan (poput dijaloškog okvira alarma za kraj snimke). Nova
  poruka o grešci jednaka je poruci koja se prikazuje prilikom pokušaja
  otvaranja višestrukih dijaloških okvira NVDA postavki.
* NVDA više neće svirati tonove greške niti izgledati kao da se ništa ne
  radi, kad se u dijaloškom okviru „Istraživača stupaca” pritisne gumb „U
  redu”, nakon konfiguriranja slotova stupaca.
* U koderima je sada moguće spremiti i resetirati postavke kodera
  (uključujući oznake prijenosa) pritiskom tipki kontrol+NVDA+C ili
  pritiskom tipki kontrol+NVDA+R tri puta.

## Version 20.03

* Istraživač stupaca sada će standardno najaviti prvih deset stupaca
  (postojeće instalacije nastavit će koristiti stare slotove stupaca).
* The ability to announce name of the playing track automatically from
  places other than Studio has been removed. This feature, introduced in
  add-on 5.6 as a workaround for Studio 5.1x, is no longer functional. Users
  must now use SPL Controller and/or Assistant layer command to hear title
  of the currently playing track from everywhere (C).
* Zbog uklanjanja automatske najave naslova snimke, postavka za
  konfiguriranje ove funkcije uklonjena je iz postavki dodatka/kategorija
  najave stanja.
* In encoders, NVDA will play connection tone every half a second while an
  encoder is connecting.
* In encoders, NVDA will now announce connection attempt messages until an
  encoder is actually connected. Previously NVDA stopped when an error was
  encountered.
* Dodana je nova postavka kodera kako bi se omogućilo da NvDA najavi vezu
  sve dok se odabrani koder ne spoji. Ova je postavka standardno aktivirana.

## Version 20.02

* Prva podrška za Playlist Editora StationPlaylist Creatora.
* Dodane su naredbe Alt+NVDA+brojčani redak tipkovnice, za najavu raznih
  informacija o stanju u Playlist Editoru. To uključuje datum i vrijeme za
  popis snimaka (1), ukupno trajanje popisa snimaka (2), planirano vrijeme
  sviranja (3) te rotaciju i kategoriju (4).
* Dok je fokusiran na zapis u alatu Creator i Track Tool (osim u Playlist
  Editoru Creatora), pritiskom na Kontrol+NVDA+crtica prikazat će se podaci
  za sve stupce u prozoru načina pregledavanja.
* If NVDA Recognizes a track list item with less than 10 columns, NVDA will
  no longer announce headers for nonexistent columns if Control+NVDA+number
  row for out of range column is pressed.
* In creator, NVDA will no longer announce column information if
  Control+NVDA+number row keys are pressed while focused on places other
  than track list.
* When a track is playing, NVDA will no longer announce "no track is
  playing" if obtaining information about current and next tracks via SPL
  Assistant or SPL Controller.
* If an alarm options dialog (intro, outro, microphone) is open, NVDA will
  no longer appear to do nothing or play error tone if attempting to open a
  second instance of any alarm dialog.
* When trying to switch between active profile and an instant profile via
  SPL Assistant (F12), NVDA will present a message if attempting to do so
  while add-on settings screen is open.
* In encoders, NVDA will no longer forget to apply no connection tone
  setting for encoders when NVDA is restarted.

## Version 20.01

* NVDA 2019.3 or later is required due to extensive use of Python 3.

## Older releases

Please see changelog link for release notes for old add-on releases.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: https://addons.nvda-project.org/files/get.php?file=spl-lts20

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
