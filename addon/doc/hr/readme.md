# StationPlaylist #

* Autori: Geoff Shang, Joseph Lee i drugi doprinositelji
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]
* Preuzmi [verziju s dugoročnom podrškom][3] – za korisnike porgrama Studio
  5.20
* NVDA kompatibilnost: 2020.3 do 2020.4

Ovaj paket dodataka omogućava bolje korištenje programa StationPlaylist
Studio i drugih StationPlaylist programa te pruža alate za kontrolu programa
Studio s bilo kojeg mjesta. Podržava sljedeće programe: Studio, Creator,
Track Tool, VT Recorder i Streamer, kao i SAM, SPL i AltaCast kodere.

Za daljnje informacije o dodatku pročitaj [priručnik za dodatke] [4].

VAŽNE NAPOMENE:

* Ovaj dodatak zahtijeva StationPlaylist izdanje 5.30 (5.20 za 20.09.x-LTS)
  ili noviju verziju.
* Korisnicima sustava Windows 8 ili novijeg, preporučamo deaktivirati modus
  stišavanja zvuka.
* Od 2018. godine pa nadalje, [zapisi o promjenama za stara izdanja][5]
  nalaze se na GitHubu. Readme datoteka dodatka sadrži popis promjena od
  verzije 20.09 (2020.) pa nadalje.
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
* NVDA+V tijekom fokusiranja na snimku (samo u prikazu popisa snimaka za
  Studio): mijenja najavljivanje snimke između ekranskog i prilagođenog
  redoslijeda.
* Alt+NVDA+C tijekom fokusiranja na snimku (samo u prikazu popisa snimaka za
  Studio): najavljuje komentare snimke, ukoliko ih ima.
* Alt+NVDA+0 u prozoru Studija: otvara dijaloški okvir za konfiguriranje
  dodataka.
* Alt+NVDA+P u prozoru Studija: otvara dijaloški okvir za profile
  emitiranja.
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
* Alt+NVDA+0 i F12: Otvara dijaloški okvir postavki kodera za konfiguriranje
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
* C: Naslov i trajanje trenutačno svirane snimke.
* Šift+C: Naslov i trajanje nadolazeće snimke, ako je ima.
* E: Stanje veze kodera.
* I: Broj slušatelja.
* Q: Informacije o stanjima u programu Studio, npr. je li se svira neka
  snimka, je li mikrofon uključen ili nije i drugo.
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

## Track column announcement

You can ask NVDA to announce track columns found in Studio's playlist viewer
in the order it appears on screen or using a custom order and/or exclude
certain columns. Press NVDA+V to toggle this behavior while focused on a
track in Studio's playlist viewer. To customize column inclusion and order,
from column announcement settings panel in add-on settings, uncheck
"Announce columns in the order shown on screen" and then customize included
columns and/or column order.

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

## Version 21.03/20.09.6-LTS

* Minimum Windows release requirement is now tied to NVDA releases.
* Removed feedback email command (Alt+NVDA+Hyphen). Please send feedback to
  add-on developers using the contact information provided from Add-ons
  Manager.
* 21.03: parts of the add-on source code now include type annotations.
* 21.03: made the add-on code more robust with help from Mypy (a Python
  static type checker). In particular, fixed several long-standing bugs such
  as NVDA not being able to reset add-on settings to defaults under some
  circumstances and attempting to save encoder settings when not
  loaded. Some prominent bug fixes were also backported to 20.09.6-LTS.
* Fixed numerous bugs with add-on welcome dialog (Alt+NVDA+F1 from Studio
  window), including multiple welcome dialogs being shown and NVDA appearing
  to do nothing or playing error tones when welcome dialog remains open
  after Studio exits.
* Fixed numerous bugs with track comments dialog (Alt+NVDA+C three times
  from a track in Studio), including an error tone heard when trying to save
  comments and many track comment dialogs appearing if Alt+NVDA+C is pressed
  many times. If track comments dialog is still shown after Studio is
  closed, comments will not be saved.
* Various column commands such as columns explorer (Control+NVDA+number row)
  in Studio tracks and encoder status announcements no longer gives
  erroneous results when performed after NVDA is restarted while focused on
  tracks or encoders. This affects NVDA 2020.4 or later.
* Fixed numerous issues with playlist snapshots (SPL Assistant, F8),
  including inability to obtain snapshot data and reporting wrong tracks as
  shortest or longest tracks.
* NVDA will no longer announce "0 items in the library" when Studio exits in
  the middle of a library scan.
* NVDA will no longer fail to save changes to encoder settings after errors
  are encountered when loading encoder settings and subsequently settings
  are reset to defaults.

## Verzija 21.01/20.09.5-LTS

Verzija 21.01 podržava SPL Studio 5.30 i novije.

* 21.01: Potrebna je verzija NVDA čitača 2020.3 ili novija.
* 21.01: Postavka uključivanja zaglavlja stupca uklonjena je iz postavki
  dodatka. NVDA postavke zaglavlja stupaca tablice upravljat će
  najavljivanjem zaglavlja stupaca u SPL paketu i koderima.
* Dodana je naredba za prebacivanje ekrana u odnosu na prilagođeno
  uključivanje stupaca i postavljanje redoslijeda (NVDA + V). Imaj na umu da
  je ova naredba dostupna samo kad je fokusirana snimka u pregledniku popisa
  snimaka Studija.
* SPL Assistant and Controller layer help will be presented as a browse mode
  document instead of a dialog.
* NVDA will no longer stop announcing library scan progress if configured to
  announce scan progress while using a braille display.

## Verzija 20.11.1/20.09.4-LTS

* Prva podrška za StationPlaylist paket 5.50.
* Poboljšanja u prezentaciji raznih dijaloških okvira dodataka zahvaljujući
  funkcijama čitača NVDA 2020.3.

## Verzija 20.11/20.09.3-LTS

* 20.11: Potrebna je verzija NVDA čitača 2020.1 ili novija.
* 20.11: Riješeni su daljnji problemi sa stilom kodiranja kao i potencijalne
  greške s Flake8.
* Ispravljeni su razni problemi s dijaloškim okvirom dobrodošlice dodataka
  (Alt+NVDA+F1 iz Studija), uključujući pogrešnu naredbu koja se prikazuje
  za povratne informacije o dodatku (Alt+NVDA+crtica).
* 20.11: Column presentation format for track and encoder items across
  StationPlaylist suite (including SAM encoder) is now based on
  SysListView32 list item format.
* 20.11: NVDA will now announce column information for tracks throughout SPL
  suite regardless of "report object description" setting in NVDA's object
  presentation settings panel. For best experience, leave this setting on.
* 20.11: In Studio's playlist viewer, custom column order and inclusion
  setting will affect how track columns are presented when using object
  navigation to move between tracks, including current navigator object
  announcement.
* If vertical column announcement is set to a value other than "whichever
  column I'm reviewing", NVDA will no longer announce wrong column data
  after changing column position on screen via mouse.
* improved playlist transcripts (SPL Assistant, Shift+F8) presentation when
  viewing the transcript in HTML table or list format.
* 20.11: In encoders, encoder labels will be announced when performing
  object navigation commands in addition to pressing up or down arrow keys
  to move between encoders.
* In encoders, in addition to Alt+NVDA+number row 0, pressing F12 will also
  open encoder settings dialog for the selected encoder.

## Version 20.10/20.09.2-LTS

* Zbog promjena u datotečnom formatu postavki kodera, instaliranje starije
  verzije ovog dodatka će nakon instaliranja ove verzije prouzročiti
  nepredvidivo ponašanje.
* Više nije potrebno ponovo pokrenuti NVDA u modusu zapisivanja otklanjanje
  grešaka, da bi se čitale poruke za otklanjanje grešaka iz preglednika
  dnevnika. Poruke za otklanjanje grešaka možeš pregledati, ako je razina
  dnevnika postavljena na „Otklanjanje grešaka” u NVDA-ovoj ploči općih
  postavki.
* In Studio's playlist viewer, NVDA will not include column headers if this
  setting is disabled from add-on settings and custom column order or
  inclusion settings are not defined.
* 20.10: column header inclusion setting from add-on settings is deprecated
  and will be removed in a future release. In the future NVDA's own table
  column header setting will control column header announcements across SPL
  suite and encoders.
* When SPL Studio is minimized to the system tray (notification area), NVDA
  will announce this fact when trying to switch to Studio from other
  programs either through a dedicated command or as a result of an encoder
  connecting.

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

## Older releases

Please see changelog link for release notes for old add-on releases.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: https://addons.nvda-project.org/files/get.php?file=spl-lts20

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
