# StationPlaylist #

* Autori: Geoff Shang, Joseph Lee i drugi doprinositelji
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]
* NVDA compatibility: 2019.3 and beyond
* Download [older version][6] compatible with NVDA 2019.2.1 and earlier

Ovaj paket dodataka omogućava bolje korištenje programa StationPlaylist
Studio i drugih StationPlaylist programa te pruža alate za kontrolu programa
Studio s bilo kojeg mjesta. Podržava sljedeće programe: Studio, Creator,
Track Tool, VT Recorder i Streamer, kao i SAM, SPL i AltaCast dekodere.

Za više informacija o dodatku, pročitaj [priručnik dodatka][4]. Za
programere koji žele saznati kako unaprijediti dodatak, postoji datoteka
buildInstructions.txt, koja se nalazi na najvišoj razini repozitorija
izvornog koda.

VAŽNE NAPOMENE:

* This add-on requires StationPlaylist suite 5.20 or later.
* Korisnicima sustava Windows 8 ili novijeg, preporučamo deaktivirati modus
  stišavanja zvuka.
* Starting from 2018, [changelogs for old add-on releases][5] will be found
  on GitHub. This add-on readme will list changes from version 17.08 (2017
  onwards).
* Određene funkcije dodatka neće raditi pod nekim uvjetima, uključujući
  pokretanje NVDA čitača u sigurnom modusu.
* Zbog tehničkih ograničenja, ovaj se dodatak ne može instalirati ili
  koristiti u Windows Store verziji NVDA čitača.
* Funkcije označene kao „eksperimentalne” služe za testiranje nečega prije
  objavljivanja. One stoga neće biti aktivirane u stabilnim izdanjima.

## Tipkovni prečaci

Većina njih radi samo u programu Studio, ukoliko nešto drugo nije navedeno.

* Alt+Shift+T u prozoru Studija: najavi proteklo vrijeme trake koja
  trenutačno svira.
* Control+Alt+T (klizanje s dva prsta prema dolje u dodirnom modusu SPL-a) u
  prozoru Studija: najavi preostalo vrijeme trake koja trenutačno svira.
* NVDA+Shift+F12 (klizanje s dva prsta prema gore u dodirnom modusu SPL-a) u
  prozoru Studija: najavljuje vrijeme emitiranja kao što je 5 minuta do
  punog sata. Dvostrukim pritiskom ove naredbe objavit će se minute i
  sekunde do punog sata.
* Alt+NVDA+1 (klizanje s dva prsta prema desno u dodirnom modusu SPL-a) u
  prozoru Studija: otvara dijaloški okvir s postavkama za kraj snimke.
* Alt+NVDA+1 from Creator's Playlist Editor window: Announces scheduled time
  for the loaded playlist.
* Alt+NVDA+2 (klizanje s dva prsta prema lijevo u dodirnom modusu SPL-a) u
  prozoru Studija: otvara dijaloški okvir s postavkama alarma za uvodni dio
  pjesme.
* Alt+NVDA+2 from Creator's Playlist Editor window: Announces total playlist
  duration.
* Alt+NVDA+3 u prozoru programa Studio: uključuje i isključuje istraživača
  džinglova za prikaz njima dodijeljenih naredbi.
* Alt+NVDA+3 from Creator's Playlist Editor window: Announces when the
  selected track is scheduled to play.
* Alt+NVDA+4 u prozoru Studija: otvara dijaloški okvir za alarm mikrofona.
* Alt+NVDA+4 from Creator's Playlist Editor window: Announces rotation and
  category associated with the loaded playlist.
* Control+NVDA+f u prozoru Studija: otvara dijaloški okvir za pronalaženje
  snimke na temelju izvođača ili pjesme. Pritisni NVDA+F3 za traženje prema
  naprijed ili NVDA+Shift+F3 za traženje prema natrag.
* Alt+NVDA+R u prozoru Studija: prolazi kroz postavke najave skeniranja
  biblioteke.
* Control+Shift+X u prozoru Studija: prolazi kroz postavke brajeve
  štoperice.
* Control+Alt+strelica lijevo ili desno (tijekom fokusiranja trake u
  programima Studio, Creator i Track Tool): najavi prethodni ili sljedeći
  stupac trake.
* Control+Alt+Home/End (while focused on a track in Studio, Creator, and
  Track Tool): Announce first/last track column.
* Control+Alt+up/down arrow (while focused on a track in Studio only): Move
  to previous or next track and announce specific columns.
* Control+NVDA+1 do 0 (tijekom fokusiranja trake u programima Studio,
  Creator i Track Tool): najavi sadržaj stupca za određeni stupac. Pritisni
  naredbu dvaput za prikaz podataka stupca u prozoru modusa pregledavanja.
* Control+NVDA+- (hyphen while focused on a track in Studio, Creator, and
  Track Tool): display data for all columns in a track on a browse mode
  window.
* Alt+NVDA+C tijekom fokusiranja na snimku (samo Studio): najavljuje
  komentare snimke, ukoliko ih ima.
* Alt+NVDA+0 u prozoru Studija: otvara dijaloški okvir za konfiguriranje
  dodataka.
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
* Sloj SPL Controller.
* Najavljivanje stanja porgrama Studio, kao što je sviranje snimaka iz
  drugih programa.
* Najavljivanje stanje veze dekodera iz bilo kojeg programa.
* Sloj SPL Assistant iz programa SPL Studio.
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
* Control+F9/Control+F10 (samo SAM dekoder): Poveži dekodere ili prekini
  njihovu vezu.
* F11: Prekidač za mijenjanje NVDA čitača na prozor programa Studio za
  odabrani dekoder, ako je povezan.
* Shift+F11: U programu Studio uključuje i isključuje sviranje prve odabrane
  snimke kad je dekoder povezan s poslužiteljem za internetski prijenos.
* Control+F11: Uključuje i isključuje praćenje odabranog dekodera u
  pozadini.
* F12: Otvara dijaloški okvir za unos prilagođene oznake za odabrani dekoder
  ili internetski prijenos.
* Control+F12: Otvara dijaloški okvir za biranje dekodera kojeg si
  izbrisao/la (kako bi se uskladile oznake internetskog prijenosa i postavke
  dekodera).
* Alt+NVDA+0: Otvara dijaloški okvir postavki dekodera za konfiguriranje
  opcija kao što je oznaka internetskog prijenosa.

Dodatno tome, dostupne su naredbe za pregled stupaca, uključujući sljedeće:

* Control+NVDA+1: Pozicija dekodera.
* Control+NVDA+2: Oznaka internetskog prijenosa.
* Control+NVDA+3 u SAM dekoderu: Format dekodera.
* Control+NVDA+3 u SPL-u i AltaCast dekoderu: Postavke dekodera.
* Control+NVDA+4 u SAM dekoderu: Stanje veze dekodera.
* Control+NVDA+4 u SPL-u i AltaCast dekoderu: Brzina prijenosa ili stanje
  veze.
* Control+NVDA+5 u SAM dekoderu: Opis stanja veze.

## Sloj SPL Assistant

Ovaj skup naredbi sloja omogućuje dobivanje različitih stanja u programu SPL
Studio, kao što je sviranje snimaka, ukupno trajanje svih snimaka u
određenom satu i tako dalje. U bilo kojem prozoru programa SPL Studio,
pritisni naredbu za sloj SPL Assistant. Zatim pritisni jednu od tipki s
donjeg popisa (jedna ili više naredbi se koriste isključivo u prikazu popisa
snimaka). NVDA čitača možeš konfigurirati i na način, da oponaša naredbe
drugih čitača ekrana.

Dostupne naredbe su:

* A: Automacija.
* C (Shift+C u JAWS i Window-Eyes rasporedima): Naslov trenutačno svirane
  snimke.
* C (JAWS i Window-Eyes rasporedi): Uključi ili isključi istraživača
  džinglova (samo u prikazu popisa snimaka).
* D (R u JAWS rasporedu): Preostalo vrijeme popisa snimaka (ako se pojavi
  greška, premjesti se na prikaz popisa snimaka te zadaj ovu naredbu).
* E (G u Window-Eyes rasporedu): stanje internetskog prijenosa metapodataka.
* Shift+1 do Shift+4, Shift+0: Stanje URL adresa pojedinih internetskih
  prijenosa metapodataka (0 je za DSP dekoder).
* E (Window-Eyes layout): Elapsed time for the currently playing track.
* F: Nađi snimku (samo u prikazu popisa snimaka).
* H: Trajanje snimaka trenutačnog jednosatnog slota.
* Shift+H: Preostalo trajanje snimaka jednosatnog slota.
* I (L u JAWS ili Window-Eyes rasporedima): Broj slušatelja.
* K: Premjesti se na označenu snimku (samo u prikazu popisa snimaka).
* Control+K: Postavi trenutačnu snimku kao pozicijsku oznaku (samo u prikazu
  popisa snimaka).
* L (Shift+L u JAWS i Window-Eyes rasporedima): Line in.
* M: Mikrofon.
* N: Naslov sljedeće planirane snimke.
* P: Stanje sviranja (svira ili je zaustavljeno).
* Shift+P: Glasnoća trenutačne snimke.
* R (Shift+E u JAWS i Window-Eyes rasporedima): Snimanje u datoteku
  uključeno ili isključeno.
* Shift+R: Praćenje skeniranja biblioteke u tijeku.
* S: Početak sviranja snimke (planirano).
* Shift+S: Vrijeme do sviranja odabrane snimke (sviranje snimke započinje
  za).
* T: Modus uređivanja ili dodavanja džinglova uključen ili isključen.
* U: Ukupno vrijeme rada programa Studio.
* W: Vremenska prognoza i temperatura, ukoliko je konfigurirano.
* Y: Stanje promjena popisa snimaka.
* 1 do 0: Najavi sadržaj stupaca za određeni stupac.
* F8: Sastavi statistiku popisa snimaka (broj snimaka, najduža snimka,
  itd.).
* Shift+F8: Zatraži prijepis popisa snimaka u raznim formatima.
* F9: Označi trenutačnu snimku kao početak za vremensku analizu snimaka
  (samo u prikazu popisa snimaka).
* F10: Izvrši vremensku analizu snimke (samo u prikazu popisa snimaka).
* F12: Mijenjaj profil između trenutačnog i unaprijed definiranog.
* F1: Pomoć za slojeve.
* Shift+F1: Otvori korisnički priručnik na internetu.

## SPL Controller

SPL Controller je skup naredbi koje se mogu koristiti za upravljanje
programom SPL Studio s bilo kojeg mjesta. Pritisni naredbu sloja SPL
Controller i NVDA će izgovoriti: „SPL Controller.” Pritisni neku drugu
naredbu za upravljanje raznim Studio postavkama, kao što je uključivanje ili
isključivanje mikrofona ili sviranje sljedeće snimke.

Dostupne naredbe za SPL Controller su:

* Pritisni P za sviranje sljedeće odabrane snimke.
* Pritisni U za pauzu ili za nastavljanje sviranja.
* Pritisni S za zaustavljanje snimke sa stišavanjem. Za trenutno
  zaustavljanje, pritisni T.
* Pritisni M ili Shift+M za uključivanje ili isključivanje
  mikrofona. Pritisni N za aktiviranje mikrofona bez stišavanja.
* Pritisni A za aktiviranje automacije ili Shift+A za njeno deaktiviranje.
* Pritisni L za aktiviranje line-in ulaza ili Shift+L za njegovo
  deaktiviranje.
* Pritisni R za slušanje preostalog vremena trenutačno svirane snimke.
* Pritisni Shift+R za dobivanje izvještaja o napretku skeniranja biblioteke.
* Pritisni C kako bi NVDA najavio ime i trajanje trenutačno svirane snimke.
* Pritisni Shift+C kako bi NVDA najavio ime i trajanje nadolazeće snimke,
  ako je ima.
* Pritisni E za slušanje podatka o tome koji su dekoderi povezani.
* Pritisni I za broj slušatelja.
* Pritisni Q za razne informacije o stanjima u programu Studio, npr. je li
  se svira neka snimka, je li mikrofon uključen ili nije i drugo.
* Pritisni tipke za džinglove (npr. F1, Control+1) za sviranje dodijeljenih
  džinglova s bilo kojeg mjesta.
* Pritisni H za prikaz dijaloškog okvira za pomoć s popisom dostupnih
  naredbi.

## Alarmi za snimke

NVDA je standardno tako postavljen, da svira zvučni signal pri ostatku od
pet sekundi u završnom i-ili uvodnom dijelu snimke. Za konfiguriranje ovu
vrijednosti te za aktiviranje ili deaktiviranje sviranja zvučnog signala,
pritisni Alt+NVDA+1. Ili pritisni Alt+NVDA+2 za otvaranje kraja
snimke. Pored toga, koristi dijaloški okvir postavki Studio dodatka, gdje
možeš odlučiti, želiš li čuti zvučni signal, poruku ili oboje, kad su alarmi
uključeni.

## Alarmi za mikrofon

NVDA može svirati zvuk kad je mikrofon neko vrijeme aktivan. Pritisni
Alt+NVDA+4 i konfiguriraj vrijeme alarma u sekundama (0 ga deaktivira).

## Pronalaženje snimaka

Ako s popisa snimaka želi brzo pronaći pjesmu na osnovi izvođača ili imena
pjesme, pritisni Control+NVDA+F. Upiši ili odaberi ime izvođača ili naslov
pjesme. Ako se pronađe, NVDA će te premjestiti na pjesmu. Ako ne može
pronaći pjesmu koju tražiš, prikazat će grešku. Za traženje prethodno
upisane pjesme ili izvođača, pritisni NVDA+F3 ili NVDA+Shift+F3 za traženje
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
vremenske analize (SPL Assistant, F9), a zatim pritisni SPL Assistant, F10
kad dođeš do kraja odabira.

## Istraživač stupaca

Pritiskom na Control+NVDA+1 do 0 ili SPL Assistant, od 1 do 0, dobiva se
sadržaj određenih stupaca. Standardno su to sljedeći podaci: izvođač,
naslov, trajanje, uvod, kategorija, naziv datoteke, godina, album, žanr i
planirano vrijeme. Moguće je konfigurirati koji će se stupci istraživati
putem dijaloškog okvira istraživača stupaca, koji se nalazi u dijaloškom
okviru za postavke dodatka.

## Statistika popisa snimaka

Pritisni SPL Assistant, F8 tijekom fokusa na popis snimaka u programu Studio
za dobivanje raznih statistika o popisu snimaka, uključujući broj snimaka u
popisu snimaka, najdulju snimku, top izvođače i tako dalje. Nakon što
dodijeliš prilagođenu naredbu za ovu funkciju, pritisni prilagođenu naredbu
dvaput, kako bi NVDA prikazao statističke informacije popisa snimkama kao
web stranicu. Na taj način možeš koristiti modus čitanja za kretanje
(pritisni escape za zatvaranje).

## Prijepisi popisa snimaka

Pritiskom na SPL Assistant, Shift+F8 će prikazati dijaloški okvir koji
omogućava zatražiti prijepis popisa snimaka u raznim formatima, uključujući
format običnog teksta, HTML tablice ili popisa.

## Dijaloški okvir konfiguracije

U prozoru programa Studio možeš pritisnuti Alt+NVDA+0 za otvaranje
dijaloškog okvira za konfiguraciju dodatka. Alternativno, idi na NVDA
izbornik Postavke i odaberi stavku SPL Studio postavke. Ovaj se dijaloški
okvir koristi i za upravljanje profilima za emitiranje.

## Dodirni modus za SPL

Ako koristiš Studio na računalu s ekranom osjetljivim na dodir s
operacijskim sustavom Windows 8 ili novijim i ako imaš instaliran NVDA
2012.3 ili noviji, možeš izvršiti neke Studio naredbe na ekranu osjetljivim
na dodir. Za prebacivanje na modus SPL-a, dodirni ekran s tri prsta. Zatim
koristi gore navedene dodirne naredbe za njihovo izvršavanje.

## Version 20.02

* Initial support for StationPlaylist Creator's Playlist Editor.
* Added Alt+NVDA+number row commands to announce various status information
  in Playlist Editor. These include date and time for the playlist (1),
  total playlist duration (2), when the selected track is scheduled to play
  (3), and rotation and category (4).
* While focused on a track in Creator and Track Tool (except in Creator's
  Playlist Editor), pressing Control+NVDA+Dash will display data for all
  columns on a browse mode window.
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
* 19.03 Experimental: in column announcements and playlist transcripts
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

## Version 18.08.2

* NVDA will no longer check for Studio add-on updates if Add-on Updater
  (proof of concept) add-on is installed. Consequently, add-on settings will
  no longer include add-on update related settings if this is the case. If
  using Add-on Updater, users should use features provided by this add-on to
  check for Studio add-on updates.

## Version 18.08.1

* Fixed yet another wxPython 4 compatibility issue seen when Studio exits.
* NVDA will announce an appropriate message when playlist modification text
  isn't present, commonly seen after loading an unmodified playlist or when
  Studio starts.
* NVDA will no longer appear to do nothing or play error tones when trying
  to obtain metadata streaming status via SPL Assistant (E).

## Version 18.08

* Add-on settings dialog is now based on multi-category settings interface
  found in NVDA 2018.2. Consequently, this release requires NVDA 2018.2 or
  later. The old add-on settings interface is deprecated and will be removed
  later in 2018.
* Added a new section (button/panel) in add-on settings to configure
  playlist transcripts options, which is used to configure column inclusion
  and ordering for this feature and other settings.
* When creating a table-based playlist transcripts and if custom column
  ordering and/or column removal is in effect, NVDA will use custom column
  presentation order specified from add-on settings and/or not include
  information from removed columns.
* When using column navigation commands in track items
  (Control+Alt+home/end/left arrow/right arrow) in Studio, Creator, and
  Track Tool, NVDA will no longer announce wrong column data after changing
  column position on screen via mouse.
* Significant improvements to NVDA's responsiveness when using column
  navigation commands in Creator and Track Tool. In particular, when using
  Creator, NVDA will respond better when using column navigation commands.
* NVDA will no longer play error tones or appear to do nothing when
  attempting to add comments to tracks in Studio or when exiting NVDA while
  using Studio, caused by wxPython 4 compatibility issue.

## Version 18.07

* Added an experimental multi-category add-on settings screen, accessible by
  toggling a setting in add-on settings/Advanced dialog (you need to restart
  NVDA after configuring this setting for the new dialog to show up). This
  is for NVDA 2018.2 users, and not all add-on settings can be configured
  from this new screen.
* NVDA will no longer play error tones or appear to do nothing when trying
  to rename a broadcast profile from add-on settings, caused by wxPython 4
  compatibility issue.
* When restarting NVDA and/or Studio after making changes to settings in a
  broadcast profile other than normal profile, NVDA will no longer revert to
  old settings.
* It is now possible to obtain playlist transcripts for the current
  hour. Select "current hour" from list of playlist range options in
  playlist transcripts dialog (SPL Assistant, Shift+F8).
* Added an option in Playlist Transcripts dialog to have transcripts saved
  to a file (all formats) or copied to the clipboard (text and Markdown
  table formats only) in addition to viewing transcripts on screen. When
  transcripts are saved, they are saved to user's Documents folder under
  "nvdasplPlaylistTranscripts" subfolder.
* Status column is no longer included when creating playlist transcripts in
  HTML and Markdown table formats.
* When focused on a track in Creator and Track Tool, pressing
  Control+NVDA+number row twice will present column information on a browse
  mode window.
* In Creator and Track Tool, added Control+Alt+Home/End keys to move Column
  Navigator to first or last column for the focused track.

## Version 18.06.1

* Fixed several compatibility issues with wxPython 4, including inability to
  open track finder (Control+NVDA+F), column search and time ranger finder
  dialogs in Studio and stream labeler dialog (F12) from encoders window.
* While opening a find dialog from Studio and an unexpected error occurs,
  NVDA will present more appropriate messages instead of saying that another
  find dialog is open.
* In encoders window, NVDA will no longer play error tones or appear to do
  nothing when attempting to open encoder settings dialog (Alt+NVDA+0).

## Version 18.06

* In add-on settings, added "Apply" button so changes to settings can be
  applied to the currently selected and/or active profile without closing
  the dialog first. This feature is available for NVDA 2018.2 users.
* Resolved an issue where NVDA would apply changes to Columns Explorer
  settings despite pressing Cancel button from add-on settings dialog.
* In Studio, when pressing Control+NVDA+number row twice while focused on a
  track, NVDA will display column information for a specific column on a
  browse mode window.
* While focused on a track in Studio, pressing Control+NVDA+Dash will
  display data for all columns on a browse mode window.
* In StationPlaylist Creator, when focused on a track, pressing
  Control+NVDA+number row will announce data in specific column.
* Added a button in Studio add-on settings to configure Columns Explorer for
  SPL Creator.
* Added Markdown table format as a playlist transcripts format.
* The developer feedback email command has changed from Control+NVDA+dash to
  Alt+NVDA+dash.

## Version 18.05

* Added ability to take partial playlist snapshots. This can be done by
  defining analysis range (SPL Assistant, F9 at the start of the analysis
  range) and moving to another item and performing playlist snapshots
  command.
* Added a new command in SPL Assistant to request playlist transcripts in a
  number of formats (Shift+F8). These include plain text, an HTML table, or
  an HTML list.
* Various playlist analysis features such as track time analysis and
  playlist snapshots are now grouped under the theme of "Playlist Analyzer".

## Version 18.04.1

* NVDA will no longer fail to start countdown timer for time-based broadcast
  profiles if NVDA with wxPython 4 toolkit installed is in use.

## Version 18.04

* Changes were made to make add-on update check feature more reliable,
  particularly if automatic add-on update check is enabled.
* NVDA will play a tone to indicate start of library scan when it is
  configured to play beeps for various announcements.
* NVDA will start library scan in the background if library scan is started
  from Studio's Options dialog or at startup.
* Double-tapping on a track on a touchscreen computer or performing default
  action command will now select the track and move system focus to it.
* When taking playlist snapshots (SPL Assistant, F8), if a playlist consists
  of hour markers only, resolves several issues where NVDA appeared to not
  take snapshots.

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

* Windows 7 Service Pack 1 or later is required.
* Several add-on features were enhanced with extension points. This allows
  microphone alarm and metadata streaming feature to respond to changes in
  broadcast profiles. This requires NVDA 2017.4.
* When Studio exits, various add-on dialogs such as add-on settings, alarm
  dialogs and others will close automatically. This requires NVDA 2017.4.
* Added a new command in SPL Controller layer to announce name of the
  upcoming track if any (Shift+C).
* You can now press cart keys (F1, for example) after entering SPl
  Controller layer to play assigned carts from anywhere.
* Due to changes introduced in wxPython 4 GUI toolkit, stream label eraser
  dialog is now a combo box instead of a number entry field.

## Version 17.11.2

This is the last stable version to support Windows XP, Vista and 7 without
Service Pack 1. The next stable version for these Windows releases will be a
15.x LTS release.

* If using Windows releases prior to Windows 7 Service Pack 1, you cannot
  switch to development channels.

## Version 17.11.1/15.11-LTS

* NVDA will no longer play error tones or appear to do nothing when using
  Control+Alt+left or right arrow keys to navigate columns in Track Tool
  5.20 with a track loaded. Because of this change, when using Studio 5.20,
  build 48 or later is required.

## Version 17.11/15.10-LTS

* Initial support for StationPlaylist Studio 5.30.
* If microphone alarm and/or interval timer is turned on and if Studio exits
  while microphone is on, NVDA will no longer play microphone alarm tone
  from everywhere.
* When deleting broadcast profiles and if another profile happens to be an
  instant switch profile, instant switch flag won't be removed from the
  switch profile.
* If deleting an active profile that is not an instant switch or a
  time-based profile, NVDA will ask once more for confirmation before
  proceeding.
* NVDA will apply correct settings for microphone alarm settings when
  switching profiles via add-on settings dialog.
* You can now press SPL Controller, H to obtain help for SPL Controller
  layer.

## Version 17.10

* If using Windows releases prior to Windows 7 Service Pack 1, you cannot
  switch to Test Drive Fast update channel. A future release of this add-on
  will move users of old Windows versions to a dedicated support channel.
* Several general settings such as status announcement beeps, top and bottom
  of playlist notification and others are now located in the new general
  add-on settings dialog (accessed from a new button in add-on settings).
* It is now possible to make add-on options read-only, use only the normal
  profile, or not load settings from disk when Studio starts. These are
  controlled by new command-line switches specific to this add-on.
* When running NVDA from Run dialog (Windows+R), you can now pass in
  additional command-line switches to change how the add-on works. These
  include "--spl-configvolatile" (read-only settings),
  "--spl-configinmemory" (do not load settings from disk), and
  "--spl-normalprofileonly" (only use normal profile).
* If exitting Studio (not NVDA) while an instant switch profile is active,
  NVDA will no longer give misleading announcement when switching to an
  instant switch profile when using Studio again.

## Version 17.09.1

* As a result of announcement from NV Access that NVDA 2017.3 will be the
  last version to support Windows versions prior to windows 7 Service Pack
  1, Studio add-on will present a reminder message about this if running
  from old Windows releases. End of support for old Windows releases from
  this add-on (via long-term support release) is scheduled for April 2018.
* NVDA will no longer display startup dialogs and/or announce Studio version
  if started with minimal (nvda -rm) flag set. The sole exception is the old
  Windows release reminder dialog.

## Version 17.09

* If a user enters advanced options dialog under add-on settings while the
  update channel and interval was set to Test Drive Fast and/or zero days,
  NVDA will no longer present the channel and/or interval warning message
  when exitting this dialog.
* Playlist remainder and trakc time analysis commands will now require that
  a playlist be loaded, and a more accurate error message will be presented
  otherwise.

## Version 17.08.1

* NVDA will no longer fail to cause Studio to play the first track when an
  encoder is connected.

## Version 17.08

* Changes to update channel labels: try build is now Test Drive Fast,
  development channel is Test Drive Slow. The true "try" builds will be
  reserved for actual try builds that require users to manually install a
  test version.
* Update interval can now be set to 0 (zero) days. This allows the add-on to
  check for updates when NVDA and/or SPL Studio starts. A confirmation will
  be required to change update interval to zero days.
* NVDA will no longer fail to check for add-on updates if update interval is
  set to 25 days or longer.
* In add-on settings, added a checkbox to let NVDA play a sound when
  listener requests arrive. To use this fully, requests window must pop up
  when requests arrive.
* Pressing broadcaster time command (NVDA+Shift+F12) twice will now cause
  NVDA to announce minutes and seconds remaining in the current hour.
* It is now possible to use Track Finder (Control+NVDA+F) to search for
  names of tracks you've searched before by selecting a search term from a
  history of terms.
* When announcing title of current and next track via SPL Assistant, it is
  now possible to include information about which Studio internal player
  will play the track (e.g. player 1).
* Added a setting in add-on settings under status announcements to include
  player information when announcing title of the current and the next
  track.
* Fixed an issue in temporary cue and other dialogs where NVDA would not
  announce new values when manipulating time pickers.
* NVDA can suppress announcement of column headers such as Artist and
  Category when reviewing tracks in playlist viewer. This is a broadcast
  profile specific setting.
* Added a checkbox in add-on settings dialog to suppress announcement of
  column headers when reviewing tracks in playlist viewer.
* Added a command in SPL Controller layer to announce name and duration of
  the currently playing track from anywhere (C).
* When obtaining status information via SPL Controller (Q) while using
  Studio 5.1x, information such as microphone status, cart edit mode and
  others will also be announced in addition to playback and automation.

## Older releases

Please see changelog link for release notes for old add-on releases.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: https://addons.nvda-project.org/files/get.php?file=spl-lts18

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog

[6]: https://addons.nvda-project.org/files/get.php?file=spl-2019
