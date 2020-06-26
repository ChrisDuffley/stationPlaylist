# StationPlaylist #

* Autori: Geoff Shang, Joseph Lee i drugi doprinositelji
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]
* NVDA compatibility: 2019.3 to 2020.2

Ovaj paket dodataka omogućava bolje korištenje programa StationPlaylist
Studio i drugih StationPlaylist programa te pruža alate za kontrolu programa
Studio s bilo kojeg mjesta. Podržava sljedeće programe: Studio, Creator,
Track Tool, VT Recorder i Streamer, kao i SAM, SPL i AltaCast dekodere.

Za više informacija o dodatku, pročitaj [priručnik dodatka][4]. Za
programere koji žele saznati kako unaprijediti dodatak, postoji datoteka
buildInstructions.txt, koja se nalazi na najvišoj razini repozitorija
izvornog koda.

VAŽNE NAPOMENE:

* Za dodatak zahtijeva StationPlaylist suite 5.20 ili noviju verziju.
* Korisnicima sustava Windows 8 ili novijeg, preporučamo deaktivirati modus
  stišavanja zvuka.
* Od 2018. godine pa nadalje, [zapisi o promjenama za stara izdanja][5]
  nalaze se na GitHubu. Readme datoteka dodatka sadrži popis promjena od
  verzije 18.09 (2018. pa nadalje).
* Određene funkcije dodatka neće raditi pod nekim uvjetima, uključujući
  pokretanje NVDA čitača u sigurnom modusu.
* Zbog tehničkih ograničenja, ovaj se dodatak ne može instalirati ili
  koristiti u Windows Store verziji NVDA čitača.
* Funkcije označene kao „eksperimentalne” služe za testiranje nečega prije
  objavljivanja. One stoga neće biti aktivirane u stabilnim izdanjima.
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
  prozoru Studija: najavi preostalo vrijeme trake koja trenutačno svira.
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
* Kontrol+Alt+strelica lijevo ili desno (tijekom fokusiranja trake u
  programima Studio, Creator, Remote VT i Track Tool): najavi prethodni ili
  sljedeći stupac snimaka.
* Kontrol+Alt+Home/End (tijekom fokusiranja trake u programima Studio,
  Creator, Remote VT i Track Tool): najavi prvi ili zadnji stupac snimaka.
* Kontrol+Alt+strelica gore ili dolje (samo tijekom fokusiranja na snimku u
  programu Studio): prijeđi na prethodnu ili sljedeću traku i najavi
  određene stupce.
* Kontrol+NVDA+1 do 0 (tijekom fokusiranja trake u programima Studio,
  Creator (uključujući Playlist Editor), Remote VT i Track Tool): najavi
  sadržaj stupca za određeni stupac (standardno za prvih deset
  stupaca). Pritisni naredbu dvaput za prikaz podataka stupca u prozoru
  modusa pregledavanja.
* Kontrol+NVDA+- (crtica u programu Studio, Creator i Track Tool): prikaži
  podatke svih stupaca u snimci na prozoru modusa pregledavanja.
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
* Najavljivanje stanje veze dekodera iz bilo kojeg programa.
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

## Dodatne naredbe tijekom korištenja dekodera

Tijekom korištenja dekodera su dostupne sljedeće naredbe:

* F9: Poveži se s poslužiteljem za internetski prijenos.
* F10 (samo SAM dekoder): Prekini vezu s poslužiteljem za internetski
  prijenos.
* Kontrol+F9/Kontrol+F10 (samo SAM dekoder): Poveži dekodere ili prekini
  njihovu vezu.
* F11: Prekidač za mijenjanje NVDA čitača na prozor programa Studio za
  odabrani dekoder, ako je povezan.
* Šift+F11: U programu Studio uključuje i isključuje sviranje prve odabrane
  snimke kad je dekoder povezan s poslužiteljem za internetski prijenos.
* Kontrol+F11: Uključuje i isključuje praćenje odabranog dekodera u
  pozadini.
* F12: Otvara dijaloški okvir za unos prilagođene oznake za odabrani dekoder
  ili internetski prijenos.
* Kontrol+F12: Otvara dijaloški okvir za biranje dekodera kojeg si
  izbrisao/la (kako bi se uskladile oznake internetskog prijenosa i postavke
  dekodera).
* Alt+NVDA+0: Otvara dijaloški okvir postavki dekodera za konfiguriranje
  opcija kao što je oznaka internetskog prijenosa.

Dodatno tome, dostupne su naredbe za pregled stupaca, uključujući sljedeće:

* Kontrol+NVDA+1: Pozicija dekodera.
* Kontrol+NVDA+2: Oznaka internetskog prijenosa.
* Kontrol+NVDA+3 u SAM dekoderu: Format dekodera.
* Kontrol+NVDA+3 u SPL-u i AltaCast dekoderu: Postavke dekodera.
* Kontrol+NVDA+4 u SAM dekoderu: Stanje veze dekodera.
* Kontrol+NVDA+4 u SPL-u i AltaCast dekoderu: Brzina prijenosa ili stanje
  veze.
* Kontrol+NVDA+5 u SAM dekoderu: Opis stanja veze.

## Sloj SPL Asistent

Ovaj skup naredbi sloja omogućuje dobivanje različitih stanja u programu SPL
Studio, kao što je sviranje snimaka, ukupno trajanje svih snimaka u
određenom satu i tako dalje. U bilo kojem prozoru programa SPL Studio,
pritisni naredbu za sloj SPL Asistent. Zatim pritisni jednu od tipki s
donjeg popisa (jedna ili više naredbi se koriste isključivo u prikazu popisa
snimaka). NVDA čitača možeš konfigurirati i na način, da oponaša naredbe
drugih čitača ekrana.

Dostupne naredbe su:

* A: Automacija.
* C (Šift+C u JAWS rasporedu): Naslov trenutačno svirane snimke.
* C (JAWS raspored): Uključi ili isključi istraživača džinglova (samo u
  prikazu popisa snimaka).
* D (R u JAWS rasporedu): Preostalo vrijeme popisa snimaka (ako se pojavi
  greška, premjesti se na prikaz popisa snimaka te zadaj ovu naredbu).
* E: Stanje internetskog prijenosa metapodataka.
* Šift+1 do Šift+4, Šift+0: Stanje URL adresa pojedinih internetskih
  prijenosa metapodataka (0 je za DSP dekoder).
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
* Pritisni E za slušanje podatka o tome koji su dekoderi povezani.
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

## Verzija 20.06

* Resolved many coding style issues and potential bugs with Flake8.
* Fixed many instances of encoders support feature messages spoken in
  English despite translated into other languages.
* Funkcija vremenski određenih profila emitiranja je uklonjenja.
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

## Verzija 20.05

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

* Columns Explorer will now announce first ten columns by default (existing
  installations will continue to use old column slots).
* The ability to announce name of the playing track automatically from
  places other than Studio has been removed. This feature, introduced in
  add-on 5.6 as a workaround for Studio 5.1x, is no longer functional. Users
  must now use SPL Controller and/or Assistant layer command to hear title
  of the currently playing track from everywhere (C).
* Due to removal of automatic announcement of playing track title, the
  setting to configure this feature has been removed from add-on
  settings/status announcement category.
* In encoders, NvDA will play connection tone every half a second while an
  encoder is connecting.
* In encoders, NVDA will now announce connection attempt messages until an
  encoder is actually connected. Previously NVDA stopped when an error was
  encountered.
* A new setting has been added to encoder settings to let NvDA announce
  connection messages until the selected encoder is connected. This setting
  is enabled by default.

## Version 20.02

* Initial support for StationPlaylist Creator's Playlist Editor.
* Added Alt+NVDA+number row commands to announce various status information
  in Playlist Editor. These include date and time for the playlist (1),
  total playlist duration (2), when the selected track is scheduled to play
  (3), and rotation and category (4).
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

## Version 19.11.1/18.09.13-LTS

* Initial support for StationPlaylist suite 5.40.
* In Studio, playlist snapshots (SPL Assistant, F8) and various time
  announcement commands such as remaining time (Control+Alt+T) will no
  longer cause NVDA to play error tones or do nothing if using NVDA 2019.3
  or later.
* In Creator's track list items, "Language" column added in Creator 5.31 and
  later is properly recognized.
* In various lists in Creator apart from track list, NVDA will no longer
  announce odd column information if Control+NVDA+number row command is
  pressed.

## Version 19.11

* Encoder status command from SPL Controller (E) will announce connection
  status for the active encoder set instead of encoders being monitored in
  the background.
* NVDA will no longer appear to do nothing or play error tones when it
  starts while an encoder window is focused.

## Version 19.10/18.09.12-LTS

* Shortened the version announcement message for Studio when it starts.
* Version information for Creator will be announced when it starts.
* 19.10: custom command can be assigned for encoder status command from SPL
  Controller (E) so it can be used from everywhere.
* Initial support for AltaCast encoder (Winamp plugin and must be recognized
  by Studio). Commands are same as SPL Encoder.

## Version 19.08.1

* In SAM encoders, NVDA will no longer appear to do nothing or play error
  tones if an encoder entry is deleted while being monitored in the
  background.

## Version 19.08/18.09.11-LTS

* 19.08: NVDA 2019.1 or later is required.
* 19.08: NVDA will no longer appear to do nothing or play error tones when
  restarting it while Studio add-on settings dialog is open.
* NVDA will remember profile-specific setttings when switching between
  settings panels even after renaming the currently selected broadcast
  profile from add-on settings.
* NVDA will no longer forget to honor changes to time-based profiles when OK
  button is pressed to close add-on settings. This bug has been present
  since migrating to multi-page settings in 2018.

## Version 19.07/18.09.10-LTS

* Renamed the add-on from "StationPlaylist Studio" to "StationPlaylist" to
  better describe apps and features supported by this add-on.
* Internal security enhancements.
* If microphone alarm or metadata streaming settings are changed from add-on
  settings, NVDA will no longer fail to apply changed settings. This
  resolves an issue where microphone alarm did not start or stop properly
  after changing settings via add-on settings.

## Version 19.06/18.09.9-LTS

Version 19.06 supports SPL Studio 5.20 and later.

* Initial support for StationPlaylist Streamer.
* While running various Studio apps such as Track Tool and Studio, if a
  second instance of the app is started and then exits, NVDA will no longer
  cause Studio add-on configuration routines to produce errors and stop
  working correctly.
* Added labels for various options in SPL Encoder configuration dialog.

## Version 19.04.1

* Fixed several issues with redesigned column announcements and playlist
  transcripts panels in add-on settings, including changes to custom column
  order and inclusion not being reflected when saving and/or switching
  between panels.

## Version 19.04/18.09.8-LTS

* Various global commands such as entering SPL Controller and switching to
  Studio window will be turned off if NVDA is running in secure mode or as a
  Windows Store application.
* 19.04: in column announcements and playlist transcripts panels (add-on
  settings), custom column inclusion/order controls will be visible up front
  instead of having to select a button to open a dialog to configure these
  settings.
* In Creator, NVDA will no longer play error tones or appear to do nothing
  when focused on certain lists.

## Version 19.03/18.09.7-LTS

* Pressing Control+NVDA+R to reload saved settings will now also reload
  Studio add-on settings, and pressing this command three times will also
  reset Studio add-on settings to defaults along with NVDA settings.
* Renamed Studio add-on settings dialog's "Advanced options" panel to
  "Advanced".
* 19.03 experimental: in column announcements and playlist transcripts
  panels (add-on settings), custom column inclusion/order controls will be
  visible up front instead of having to select a button to open a dialog to
  configure these settings.

## Version 19.02

* Removed standalone add-on update check feature, including update check
  command from SPL Assistant (Control+Shift+U) and add-on update check
  options from add-on settings. Add-on update check is now performed by
  Add-on Updater.
* NVDA will no longer appear to do nothing or play error tones when
  microphone active interval is set, used to remind broadcasters that
  microphone is active with periodic beeps.
* When resetting add-on settings from add-on settings dialog/reset panel,
  NVDA will ask once more if an instant switch profile or a time-based
  profile is active.
* After resetting Studio add-on settings, NVDA will turn off microphone
  alarm timer and announce metadata streaming status, similar to after
  switching between broadcast profiles.

## Version 19.01.1

* NVDA will no longer announce "monitoring library scan" after closing
  Studio in some situations.

## Version 19.01/18.09.6-LTS

* NVDA 2018.4 or later is required.
* More code changes to make the add-on compatible with Python 3.
* 19.01: some message translations from this add-on will resemble NVDA
  messages.
* 19.01: add-on update check feature from this add-on is no more. An error
  message will be presented when trying to use SPL Assistant,
  Control+Shift+U to check for updates. For future updates, please use
  Add-on Updater add-on.
* Slight performance improvements when using NVDA with apps other than
  Studio while Voice Track Recorder is active. NVDA will still show
  performance issues when using Studio itself with Voice Track Recorder
  active.
* In encoders, if an encoder settings dialog is open (Alt+NVDA+0), NVDA will
  present an error message if trying to open another encoder settings
  dialog.

## Version 18.12

* Internal changes to make the add-on compatible with future NVDA releases.
* Fixed many instances of add-on messages spoken in English despite
  translated into other languages.
* If using SPL Assistant to check for add-on updates (SPL Assistant,
  Control+Shift+U), NVDA will not install new add-on releases if they
  require a newer version of NVDA.
* Some SPL Assistant commands will now require that the playlist viewer is
  visible and populated with a playlist, and in some cases, a track is
  focused. Commands affected include remaining duration (D), playlist
  snapshots (F8), and playlist transcripts (Shift+F8).
* Playlist remaining duration command (SPL Assistant, D) will now require a
  track from playlist viewer be focused.
* In SAM Encoders, you can now use table navigation commands
  (Control+Alt+arrow keys) to review various encoder status information.

## Version 18.11/18.09.5-LTS

Note: 18.11.1 replaces 18.11 in order to provide better support for Studio
5.31.

* Initial support for StationPlaylist Studio 5.31.
* You can now obtain playlist snapshots (SPL Assistant, F8) and transcripts
  (SPL Assistant, Shift+F8) while a playlist is loaded but the first track
  isn't focused.
* NVDA will no longer appear to do nothing or play error tones when trying
  to announce metadata streaming status when Studio starts if configured to
  do so.
* If configured to announce metadata streaming status at startup, metadata
  streaming status announcement will no longer cut off announcements about
  status bar changes and vice versa.

## Version 18.10.2/18.09.4-LTS

* Fixed inability to close the add-on settings screen if Apply button was
  pressed and subsequently OK or Cancel buttons were pressed.

## Version 18.10.1/18.09.3-LTS

* Resolved several issues related to encoder connection announcement
  feature, including not announcing status messages, failing to play the
  first selected track, or not switching to Studio window when
  connected. These bugs are caused by wxPython 4 (NVDA 2018.3 or later).

## Version 18.10

* NVDA 2018.3 or later is required.
* Internal changes to make the add-on more compatible with Python 3.

## Version 18.09.1-LTS

* When obtaining playlist transcripts in HTML table format, column headers
  are no longer rendered as a Python list string.

## Version 18.09-LTS

Version 18.09.x is the last release series to support Studio 5.10 and based
on old technologies, with 18.10 and later supporting Studio 5.11/5.20 and
new features. Some new features will be backported to 18.09.x if needed.

* NVDA 2018.3 or later is recommended due to introduction of wxPython 4.
* Add-on settings screen is now fully based on multi-page interface derived
  from NVDA 2018.2 and later.
* Test Drive Fast and Slow rings have been combined into "development"
  channel, with an option for development snapshot users to test pilot
  features by checking the new pilot features checkbox found in Advanced
  add-on settings panel. Users formerly on Test Drive Fast ring will
  continue to test pilot features.
* The ability to select different add-on update channel from add-on settings
  has been removed. Users wishing to switch to a different release channel
  should visit NVDA community add-ons website (addons.nvda-project.org),
  select StationPlaylist Studio, then download the appropriate release.
* Column inclusion checkboxes for column announcement and playlist
  transcripts, as well as metadata streams checkboxes have been converted to
  checkable list controls.
* When switching between settings panels, NVDA will remember current
  settings for profile-specific settings (alarms, column announcements,
  metadata streaming settings).
* Added CSV (comma-separated values) format as a playlist transcripts
  format.
* Pressing Control+NVDA+C to save settings will now also save Studio add-on
  settings (requires NVDA 2018.3).

## Older releases

Please see changelog link for release notes for old add-on releases.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
