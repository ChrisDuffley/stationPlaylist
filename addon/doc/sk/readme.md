# Station Playlist #

* Autori: Geoff Shang, Joseph Lee a ďalší
* Stiahnuť [stabilnú verziu][1]
* Stiahnuť [vývojovú verziu][2]
* Funguje s NVDA 2019.3 až 2020.1

Doplnok zlepšuje prístupnosť Station Playlist Studio a ďalších pridružených
aplikácií a tiež umožňuje ovládať Station Playlist mimo hlavného okna
aplikácie. Podporuje tiež aplikácie Studio, Creator, Track Tool, VT
Recorder, Streamer, a tiež SAM, SPL, a AltaCast enkodéri.

Podrobnosti si môžete prečítať v [dokumentácii (anglicky)][4]. Ak chcete
zostaviť vlastnú verziu, pozrite si inštrukcie v súbore
buildInstructions.txt v hlavnom priečinku repozitára doplnku (anglicky).

Dôležité:

* Doplnok vyžaduje StationPlaylist suite od verzie 5.20.
* Ak používate Systém od verzie Windows 8, odporúčame vám vypnúť funkciu
  automatického stišovania.
* Od roku 2018 je [Zoznam zmien (anglicky)][5] na serveri GitHub. V tomto
  dokumente sú uvedené zmeny od verzie 18.09.
* Niektoré funkcie doplnku nemusia vždy fungovať, napríklad ak sa nachádzate
  na zabezpečenej obrazovke.
* Z technických príčin nie je možné tento doplnok používať na verzii NVDA z
  Windows obchodu.
* Funkcie označené ako experimentálne sú v štádiu testovania a nie sú zatiaľ
  zaradené do stabilnej verzie doplnku.
* Z okna SPL studio je možné uložiť nastavenia skratkou ctrl+nvda+c. Môžete
  tiež načítať uložené nastavenia skratkou ctrl+nvda+r. Takisto je možné
  obnoviť pôvodné nastavenia skratkou nvda+ctrl+r stlačením trikrát rýchlo
  za sebou. Toto sa týka aj nastavení enkodéra. Tieto je však možné len
  uložiť alebo obnoviť.

## Klávesové skratky

Väčšina skratiek je určených pre Studio, ak nie je uvedené inak.

* alt+shift+T v okne  studio: Oznámy čas do konca práve prehrávanej skladby.
* Ctrl+Alt+T v okne studio (švihnutie dvoma prstami v dotykovom režime):
  Oznámy čas do konca práve prehrávanej skladby.
* nvda+shift+F12 (švihnutie dvoma prstami hore v dotykovom režime) v okne
  Studio: oznámi čas vysielania, napríklad 5 minút do celej hodiny. Stlačené
  dvakrát rýchlo za sebou oznamuje minúty aj sekundy.
* alt+NVDA+1 (švihnutie dvoma prstami doprava v dotykovom režime spl) v okne
  Studio: otvorí kategóriu upozornenia v nastaveniach doplnku.
* alt+nvda+1 pri úprave playlistu v okne creator a Remote VT playlist
  editor: Oznámi plánovaný čas spustenia playlistu.
* Alt+NVDA+2 pri úprave playlistu v okne creator a Remote VT playlist
  editor: Oznámi celkový čas skladieb v playliste.
* alt+NVDA+3 v okne Studio : zapína a vypína prehliadač jinglov.
* Alt+NVDA+3 pri úprave playlistu v okne creator a Remote VT playlist
  editor: Oznámi čas odohratia vybratej skladby.
* Alt+NVDA+4 pri úprave playlistu v okne creator a Remote VT playlist
  editor: Oznámi kategóriu a rotáciu pre načítaný playlist.
* Ctrl+NVDA+f v okne Studio: otvorí okno, v ktorom môžete nájsť skladbu
  podľa názvu alebo interpreta. NVDA+F3 hľadá dopredu, NVDA+shift+F3 hľadá
  dozadu.
* Alt+NVDA+R v okne Studio: Prepína oznamovanie skenovania knižnice.
* Ctrl+Shift+X v okne Studio: Prepína zobrazenie na braillovskom riadku.
* Ctrl+Alt+šípky doľava a doprava (pri zobrazení skladby v oknách Studio,
  Creator, Remote VT, a Track Tool): Oznamuje metadáta vybratej skladby.
* Ctrl+Alt+home a end (pri zobrazení skladby v oknách Studio, Creator,
  Remote VT, a Track Tool): Oznámi prvú a poslednú informáciu o metadátach.
* Ctrl+Alt+šípky hore a dole (pri zobrazení skladby v okne Studio): presunie
  kurzor na nasledujúcu alebo predchádzajúcu skladbu a oznámi vybraté
  metadáta.
* Ctrl+NVDA+1 až 0 (Pri zobrazení skladby v okne Studio, Creator (vrátane
  úpravy playlistu), Remote VT, a Track Tool): Oznámi príslušné metadáta
  (prvých 10). Stlačené dvakrát rýchlo za sebou zobrazí metadáta v režime
  prehliadania.
* Ctrl+NVDA+- (pomlčka pri zobrazení skladby v oknách Studio, Creator, a
  Track Tool): Zobrazí všetky metadáta v režime prehliadania.
* Alt+NVDA+C (pri zobrazení skladby v okne Studio): oznámi komentár k
  skladbe.
* Alt+NVDA+0 z okna studio: Otvorí nastavenia doplnku.
* Alt+NVDA+p z okna studio: Otvorí nastavenia vysielacích profilov.
* Alt+NVDA+- (pomlčka) z okna studio: Otvorí predvoleného e-mailového
  klienta na zaslanie e-mailu vývojárovi doplnku.
* Alt+NVDA+F1: Otvorí uvítací dialóg doplnku.

## Funkcie bez klávesových skratiek

Nasledujúce funkcie nemajú predvolene priradené klávesové skratky. Môžete
ich priradiť, ak z okna Station Playlist otvoríte dialóg klávesové
skratky. Tam hľadajte vetvu Station playlist. Po vybratí príslušnej funkcie
v kontextovej ponuke aktivujte tlačidlo Pridať.

* Zobrazenie okna Studio odkiaľkoľvek.
* Podpríkazy na ovládanie a informácie stavu SPL.
* Oznamovanie stavových informácií, napríklad prehrávanie odkiaľkoľvek.
* Oznamovanie stavu pripojenia k streamu z iných aplikácií.
* Podmnožina informačných príkazov.
* Oznámiť čas vrátane sekúnd z okna Studio.
* Oznámiť teplotu.
* Oznámiť názov nasledujúcej naplánovanej skladby.
* Oznámiť názov aktuálne prehrávanej skladby.
* Označenie aktuálnej skladby ako počiatočnej na časovú analýzu.
* Spustenie časovej analýzy.
* Zobrazenie štatistiky playlistu.
* Vyhľadanie textu v určených metadátach.
* Vyhľadanie skladieb s určitou dĺžkou.
* Zapnutie a vypnutie vysielania metadát.

## Ďalšie príkazy pre enkodéry

Dostupné sú tieto príkazy:

* F9: Pripojiť na vysielací server.
* F10 (len sam Encoder): Odpojiť od vysielacieho servera.
* Ctrl+F9/Ctrl+F10 (len SAM encoder): Pripojí a odpojí všetky pripojené
  enkodéry.
* F11: Aktivuje a deaktivuje automatické prepnutie do okna Studio po
  pripojení.
* Shift+F11: určuje, či sa automaticky prehrá prvá vybratá skladba po
  pripojení na server.
* Ctrl+F11: Zapína a vypína monitorovanie vybratého pripojenia na pozadí.
* F12: Otvorí dialóg, v ktorom môžete zadať vlastný názov vybratého streamu
  alebo enkodéra.
* ctrl+F12: Otvorí okno na výber odstráneného enkodéra (kde môžete prehodiť
  nastavené enkodéry, názvy a nastavenia).
* Alt+NVDA+0: Otvorí nastavenia enkodéra, kde je možné napríklad nastaviť
  názov.

Dostupné sú tieto príkazy na prezeranie stĺpcov:

* Ctrl+NVDA+1: Pozícia enkodéra.
* Ctrl+NVDA+2: Názov pripojenia.
* Ctrl+nvda+3 z okna Sam Encoder: Formát.
* Ctrl+nvda+3 z aplikácie SPL a AltaCast Encoder: Nastavenia enkodéra.
* Ctrl+nvda+4 z okna SAM Encoder: Stav pripojenia.
* Ctrl+NVDA+4 z aplikácie SPL a AltaCast Encoder: Stav a rýchlosť
  pripojenia.
* Ctrl+NVDA+5 z okna SAM Encoder: stav pripojenia.

## Podmnožina informačných príkazov

Táto podmnožina umožňuje zistiť stav SPL Studio, napríklad prehrávanie
skladby, celkové trvanie skladieb v časovom slote a podobne. Najprv je
potrebné stlačiť skratku podmnožiny príkazov a potom príslušné
písmeno. Väčšina príkazov je určených pre okno Studio a špeciálne pre
zobrazenie playlistu. V nastaveniach doplnku je navyše možné prepnúť skratky
tak, aby simulovali správanie, na ktoré ste zvyknutí z iných čítačov
obrazovky.

Dostupné sú tieto príkazy:

* A: autopylot.
* C (Shift+C in JAWS layout): Title for the currently playing track.
* C (JAWS layout): Toggle cart explorer (playlist viewer only).
* D (R v rozložení pre JAWS): Oznámi ostávajúci čas do konca skladby. (Ak
  nefunguje, zopakujte skratku zo zobrazenia playlistu).
* E: Metadata streaming status.
* Shift+1 až Shift+4: Stav jednotlivých pripojení. Shift+0: Stav pre DSP
  enkodér.
* F: Nájsť skladbu (len zo zoznamu skladieb).
* H: Oznámi Trvanie skladieb v aktuálnom hodinovom slote.
* Shift+H: Oznámi zostávajúci čas skladieb v aktuálnom hodinovom slote.
* I (L in JAWS layout): Listener count.
* K: Prejde na záložku (vyznačenú skladbu v zozname skladieb).
* Ctrl+K: Nastaví aktuálnu skladbu ako záložku (v zobrazení playlistu).
* L (Shift+L in JAWS layout): Line in.
* M: Mikrofón.
* N: Oznámi Názov nasledujúcej skladby.
* P: Oznámi Stav prehrávania (prehrávanie alebo zastavené).
* Shift+P: Oznámi tóninu skladby.
* R (Shift+E in JAWS layout): Record to file enabled/disabled.
* Shift+R: Oznámi stav skenovania knižnice.
* S: Oznámi naplánovaný čas spustenia skladby.
* Shift+S: Oznámi čas do spustenia (začína o).
* T: zapína a vypína editáciu jinglov.
* U: Oznámi čas od spustenia aplikácie Studio.
* W: Oznámi Predpoveď počasia.
* Y: Oznámi stav úpravy playlistu.
* F8: Zobrazí štatistiku playlistu (počet skladieb, trvanie playlistu,
  najkratšia a najdlhšia skladba).
* Shift+F8: Uloží prepis playlistu vo viacerých formátoch.
* F9: Označí skladbu ako počiatočnú pre analýzu (v zobrazení skladieb).
* F10: Analyzuje skladby (zo zobrazenia skladieb).
* F12: Prepína medzi konfiguračnými profilmi.
* F1: Oznámi funkcie a klávesové skratky.
* Shift+F1: Otvorí online používateľskú príručku.

## príkazy na ovládanie SPL

je to množina príkazov, pomocou ktorej môžete SPL ovládať aj ak nemáte
zamerané okno SPL Studio. NVDA Povie "ovládanie". NVDA počká na ďalší
príkaz, ktorým môžete sledovať stav mikrofónu, alebo prehrávanie
nasledujúcej skladby.

Dostupné sú tieto príkazy:

* P: prehrá nasledujúcu skladbu.
* U: pozastaví alebo spustí prehrávanie.
* S: postupne stíši prehrávanie. Klávesom T zastavíte prehrávanie okamžite.
* M zapne mikrofón, shift+M vypne mikrofón. Písmeno n zapne mikrofón bez
  stíšenia skladby.
* A: spustí autopylota, shift+A ho zastaví.
* L: povolí line-in vstup, shift+L: vypne line in vstup.
* r: Oznámy čas do konca práve prehrávanej skladby.
* Shift+R: Oznámi stav skenovania knižnice.
* C: Oznámi názov a trvanie prehrávanej skladby.
* Shift+C: Oznámi názov a trvanie najbližšej skladby.
* E: Oznámi aktívne pripojenia.
* I: Oznámi počet pripojených poslucháčov.
* Q: Oznámi stavové informácie, napríklad aktívne prehrávanie, aktívny
  mikrofón a podobne.
* Jingle môžete odkiaľ koľvek spúšťať skratkami F1, ctrl+1 a podobne.
* H: Oznámi dostupné príkazy a funkcie.

## Upozornenia na zapnutý mikrofón, intro a koniec skladby

Predvolene NVDA zapípa 5 sekúnd pred koncom skladby alebo pred koncom intra
skladby a tiež upozorňuje, keď je zapnutý mikrofón. Toto nastavenie je možné
zapnúť, vypnúť a upraviť hodnoty po stlačení alt+nvda+1. Je možné nastaviť
upozornenie pípaním, rečou alebo oboje.

## Vyhľadávač skladieb

Ak chcete rýchlo nájsť skladbu podľa názvu interpreta alebo názvu skladby,
stlačte ctrl+nvda+f. Zadajte názov skladby alebo interpreta. NVDA vás
presunie na skladbu, ak sa našla, alebo zobrazí chybu, ak sa skladbu
nepodarilo nájsť. Ak chcete zopakovať to isté hľadanie smerom dopredu,
stlačte nvda+F3. Vyhľadávanie opačným smerom spustíte skratkou
nvda+shift+F3.

Pozor: Hľadanie rozlišuje veľké a malé písmená.

## Prehliadač jinglov

Studio umožňuje uložiť a zaradiť až 96 jinglov, v závislosti od edície,
ktorú používate. Pomocou NVDA môžete zistiť pozície jinglov v prehliadači.

Aby ste zistili pozíciu jingla, v okne studio stlačte alt+NVDA+3. Ak príkaz
stlačíte raz, dozviete sa, ktorý efekt je priradený konkrétnej skratke. Po
dvojitom stlačení sa zvuk prehrá. Prehliadač opustíte opäť skratkou
alt+nvda+3. Podrobnosti nájdete v návode k tomuto doplnku.

## Analyzovanie času

Ak chcete analyzovať čas vybratých skladieb, postupujte nasledovne: Nájdite
požadovanú počiatočnú skladbu. Potom stlačte skratku na spl zložený príkaz
nasledovanú klávesom F9. Potom nájdite koncovú skladbu, opätovne stlačte
skratku na spl zložený príkaz nasledovaný klávesom F10.

## Prehliadač metadát

Skratkami Ctrl+NVDA+1 až 0, môžete čítať metadáta k skladbe. Predvolene je
to v okne studio: interpret, názov, dĺžka, intro, outro, kategória, rok,
album, žáner a nálada. V editoroch playlistu Creator a Remote VT závisí
poradie podľa toho, ako je nastavené usporiadanie na obrazovke. Zobrazené
metadáta sa dajú nastavovať v prehliadači metadát v nastaveniach
doplnku. Tieto nastavenia sa zohľadňujú len pre Studio a Tracktool.

## Štatistika playlistu

Zloženým príkazom SPL F8 si môžete z okna studio zo zoznamu skladieb
zobraziť štatistiku playlistu. Tu zistíte počet skladieb, najdlhšiu skladbu,
najhranejšieho interpreta a podobne. Ak si priradíte k tejto funkcii vlastnú
skratku, môžete po jej dvojitom stlačení zobraziť informáciu v režime
prehliadania. Okno so štatistikou zatvoríte klávesom ESC.

## Prepisy playlistu

Zložený príkaz SPL shift+F8 umožní uložiť playlist ako prepis v čistom texte
alebo ako tabuľku HTML.

## Nastavenia doplnku

Z okna Studio môžete skratkou alt+nvda+0 otvoriť nastavenia doplnku. Môžete
tiež použiť ponuku NVDA > možnosti. Tu tiež môžete nastaviť profily.

## Profily

Pre rôzne relácie si môžete vytvoriť rôzne profily. Nastavenia vyvoláte
skratkou alt+nvda+p.

## Dotykový režim

Ak máte k dispozícii dotykovú obrazovku, používate Windows od verzie 8 a
NVDA  od verzie 2012.3, môžete na ovládanie doplnku použiť dotykové
príkazy. Najprv je potrebné dotknúť sa obrazovky tromi prstami. Následne
vykonajte gestá spomenúté vyššie v tomto návode.

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.
* Fixed many instances of encoders support feature messages spoken in
  English despite translated into other languages.
* Time-based broadcast profiles feature has been removed.
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

## verzia 20.05

* Prvotná podpora pre aplikáciu na nahrávanie vstupov Remote VT (voice
  track), a tiež podpora pre remote playlist editor s rovnakými príkazmi ako
  Creator.
* Príkazy na otvorenie nastavení upozornení (alt+nvda+1, alt+nvda+2,
  alt+nvda+4) sú odteraz zlúčené do jedného okna, ktoré otvoríte skratkou
  alt+nvda+1.
* Odstránená možnos nastaviť čas a dĺžku trvania spusteného profilu.
* Odstránená možnosť odpočítavania pri spustení časovaného profilu.
* Keďže čítač obrazovky Window-Eyes už firma Vispero  nevyvíja od roku 2017,
  budú z nasledujúcich verzií doplnku odstránené skratky pre tento čítač
  obrazovky. Ak používate rozloženie pre Window-eyes, NVDA na túto
  skutočnosť upozorní a odporučí nastavenie iného rozloženia (JAWS alebo
  NVDA).
* Ak zmeníte poradie metadát myšou a následne použijete skratky na
  prezeranie metadát, NVDA zohľadní zmenyy
* Ak ukončíte NVDA a nemáte v okne s nastavením enkodéra zameraný zoznam
  pripojení, NVDA viac nehlási chybu a dá sa ukončiť bez nutnosti zamerať
  zoznam pripojení.

## verzia 20.04

* Profily viazané na určitý čas viac nie sú podporované. Doplnok vás na túto
  skutočnosť upozorní, ak používate verziu doplnku 20.04 a máte definované
  profily so spustením v určitom čase.
* Nastavenia profilov boli presunuté do samostatného okna, ktoré je dostupné
  pod skratkou alt+nvda+p.
* Boli odstránené skratky na prezeranie metadát zo spl asistenta, keďže
  dochádzalo ku konfliktom so skratkami nvda+ctrl+čísla.
* Opravené zobrazovanie správ, ak sa pokúšate otvoriť viacero dialógov
  doplnku. Využívame teraz hlásenie integrované v NVDA.
* Po nastavení poradia zobrazovaných metadát a ich uložení NVDA viac nehlási
  chybu.
* Odteraz je možné uložiť nastavenia a názvy enkodéra skratkou
  ctrl+nvda+c. Nastavenia obnovíte skratkou ctrl+nvda+r stlačené trikrát
  rýchlo za sebou.

## verzia 20.03

* Prezeranie metadát oznamuje prvých desať položiek (existujúce staršie
  inštalácie budú používať naďalej staršie sloty metadát).
* Prepracovaná možnosť oznamovania hrajúcej skladby odkiaľkoľvek. Odteraz sa
  používa zložený príkaz. Automatické oznamovanie viac nie je podporované.
* Odstránené nepotrebné nastavenie na automatické oznamovanie hrajúcej
  skladby.
* NVDA oznamuje pripájanie dvakrát za sekundu pípaním.
* NVDA oznamuje chyby pripojenia aj v prípade, že dôjde k chybeale pokus o
  pripájanie pokračuje.
* Do nastavení pridaná možnosť oznamovať stav pripájania až po úspešné
  pripojenie. Predvolene je zapnuté.

## verzia 20.02

* Prvotná podpora pre Station Playlist Creator.
* Pridané skratky alt+nvda+číslice  na zisťovanie stavových informácií pri
  úprave playlistu: Dátum a čas playlistu (1), trvanie playlistu (2),
  plánované odohratie vybratej skladby (3), rotáciu a kategóriu (4).
* Ctrl+nvda+- zobrazí metadáta skladby v režime prehliadania. Funguje pri
  zameraní skladby v oknách Creator, Tracktool (ale nie v okne s úpravou
  playlistu Creator).
* Ak má skladba priradených menej ako 10 metadát, NVDA nebude oznamovať
  neexistujúce metadáta.
* NVDA v okne Creator po stlačení skratiek ctrl+nvda+0-9 neoznamuje
  metadáta, ak nie ste v zozname skladieb.
* NVDA viac netvrdí, že sa nič neprehráva, hoci prehrávanie beží a vy
  zisťujete stav cez zložené príkazy.
* NVDA upozorní, že je otvorený dialóg s upozorneniami, ak sa ho pokúsite
  opätovne otvoriť.
* NVDA upozorní, keď je otvorené okno s nastaveniami a vy sa pokúsite zmeniť
  aktívny profil.
* NVDA po reštarte nezabudne pípať v prípade, že nie je aktívne žiadne
  pripojenie.

## Verzia 20.01

* Vyžadujeme NVDA od verzie 2019.3 nakoľko používame Python3.

## verzia 19.11.1/18.09.13-LTS

* Prvotná podpora pre StationPlaylist suite 5.40.
* Ak používate NVDA od verzie 2019.3, funkcie na generovanie štatistiky
  playllistu a oznamovanie času nehlásia chybu.
* V zozname skladieb v okne Creator je od verzie 5.31 rozpoznaný stĺpec
  jazyk.
* V rôznych zoznamoch v okne creator NVDA pri prezeraní metadát správne
  oznamuje stĺpce pri použití ctrl+nvda+číslice.

## Verzia 19.11

* Z podmnožiny príkazov skratka E oznamuje stav vybratého aktívneho enkodéra
  a nie toho, ktorý je nastavený na monitorovanie na pozadí.
* NVDA pri štarte so zameraním na okno s nastavením enkodéra viac nehlási
  chybu.

## verzia 19.10/18.09.12-LTS

* Skrátené oznamovanie verzie aplikácie Studio po štarte.
* pridané oznamovanie verzie aplikácie Creator po štarte.
* 19.10: Je možné priradiť vlastnú skratku na zistenie stavu enkodéru a tak
  zistiť stav odkiaľkoľvek.
* Prvotná podpora pre AltaCast encoder (Winamp plugin musí byť rozpoznaný v
  Studio). Má rovnaké príkazy ako vstavaný enkodér SPL.

## Verzia 19.08.1

* NVDA viac nehlási chybu, ak odstránite pripojenie, ktoré monitorujete na
  pozadí.

## Verzia 19.08/18.09.11-LTS

* 19.08: Vyžaduje NVDA od verzie 2019.1.
* 19.08: NVDA viac nehlási chybu, ak ho reštartujete a súčasne ponecháte
  otvorené okno s nastaveniami doplnku.
* NVDA si zapamätá nastavenia profilu aj vtedy, ak sa prepínate medzi
  panelmi nastavení a premenujete profil v nastaveniach doplnku.
* NVDA Zohľadňuje časovú aktiváciu profilov po aktivovaní tlačidla OK v
  nastaveniach. Problém nastal po migrovaní do stromu nastavení.

## Verzia 19.07/18.09.10-LTS

* Doplnok premenovaný zo "Station playlist studio" na "Station playlist",
  keďže teraz podporuje viacero aplikácií z ponuky Station playlist.
* Opravené mierne bezpečnostné chyby.
* Opravená chyba s ukladaním nastavení streamovania metadát a upozornenia na
  zapnutý mikrofón.

## Verzia 19.06/18.09.9-LTS

Verzia 19.06 podporuje SPL Studio od verzie 5.20.

* Prvotná podpora pre Station Playlist Streamer.
* Ak je spustený Tracktool alebo Studio a spustíte nové okno aplikácie,
  ktoré neskôr zatvoríte, doplnok sa naďalej bude správať korektne.
* Pridané popisky prvkov v nastavení enkodéra.

## Verzia 19.04.1

* Opravené problémy s ukladaním nastavení, upravenými stĺpcami metadát a
  prepisom playlistu.

## Verzia 19.04/18.09.8-LTS

* Množina príkazov SPL nebude fungovať, ak ste na zabezpečenej obrazovke,
  alebo spúšťate verziu NVDA z Windows obchodu.
* 19.04: Pri prepise playlistu a nastavovaní zobrazeného poradia metadát nie
  je viac potrebné otvoriť nové okno. Všetko nastavíte priamo v aktívnom
  okne.
* V niektorých zoznamoch v okne Creator NVDA viac nehlási chybu.

## verzia 19.03/18.09.7-LTS

* Skratka Ctrl+NVDA+R načíta uložené nastavenia aj pre tento
  doplnok. Rovnako trojité stlačenie vynuluje aj nastavenia doplnku.
* Premenované pokročilé nastavenia len na pokročilé.
* 19.03 experimentálne: Pri prepise playlistu a nastavovaní zobrazeného
  poradia metadát nie je viac potrebné otvoriť nové okno. Všetko nastavíte
  priamo v aktívnom okne.

## Verzia 19.02

* Odstránená kontrola aktualizácie doplnku. Doplnok aktualizujte cez
  aktualizačný nástroj pre doplnky.
* NVDA viac nehlási chybu po nastavení intervalu upozornenia na zapnutý
  mikrofón.
* NVDA pri pokuse obnoviť nastavenia doplnku upozorní, ak je aktívny iný
  profil.
* NVDA po obnove nastavení vypne upozornenie na zapnutý mikrofón a
  upozornenie na streamovanie metadát.

## Verzia 19.01.1

* NVDA po zatvorení okna Studio viac nehlási skenovanie knižnice.

## Verzia 19.01/18.09.6-LTS

* Vyžaduje sa NVDA od verzie 2018.4.
* Upravený kód pre Python 3.
* 19.01: Namiesto vlastných prekladov v niektorých situáciách používame
  priamo správy integrované v NVDA.
* 19.01: Odstránená podpora pre aktualizáciu doplnku. Aktualizujte pomocou
  aktualizačného nástroja pre doplnky NVDA.
* Upravená odozva pri nahrávaní vstupov a súčasnom použití aplikácie Voice
  Track Recorder. Stále je ale zhoršená odozva pri súčasnom použití Studio a
  Voice Track Recorder.
* NVDA zobrazí chybu pri pokuse otvoriť novú inštanciu okna s nastavením
  enkodéru.

## Verzia 18.12

* Úpravy pre budúce verzie NVDA.
* Opravené oznamovanie správ doplnku v Angličtine v situáciách, keď bol
  dostupný preklad.
* Po kontrole aktualizácie doplnku sa táto nenainštaluje, ak vyžaduje novú
  verziu NVDA.
* Pri použití niektorých funkcií je potrebné najprv zamerať playlist a
  vybrať konkrétnu skladbu. Týka sa zisťovania času (d), štatistiky
  playlistu (F8), a prepisu playlistu (shift+F8).
* Pre zobrazenie ostávajúceho času do konca odohratia playlistu (zložený
  príkaz nasledovaný písmenom D) je potrebné byť v zozname skladieb a mať
  vybratú skladbu.
* V okne SAM Encoder je možné prezerať stav pripojenia pomocou príkazov na
  navigáciu v tabuľke (ctrl+alt+šípky).

## Verzia 18.11/18.09.5-LTS

Verzia 18.11.1 nahrádza 18.11 ktorá má lepšiu podporu pre Studio 5.31.

* Prvotná podpora pre StationPlaylist Studio 5.31.
* Odteraz je možné získať štatistiku a prepis playlistu aj v prípade, že je
  zameraný zoznam skladieb a nie je vybratá prvá skladba.
* NVDA viac nehlási chybu ak sa pokúšate zistiť stav streamovania metadát
  pri spúšťaní okna Studio.
* Oznamovanie streamovania metadát a iné stavové informácie sú oznamované v
  celku a navzájom sa neprerušujú.

## verzia 18.10.2/18.09.4-LTS

* Odteraz je možné zatvoriť nastavenia doplnku po stlačení tlačidla použiť a
  následnom stlačení tlačidla OK alebo zrušiť.

## verzia 18.10.1/18.09.3-LTS

* Opravené viaceré problémy s enkodérmi, konkrétne napríklad neoznamovanie
  stavu pripojenia, nespustenie prvej skladby z playlistu po pripojení,
  alebo nefunkčné automatické zameranie okna Studio po pripojení. Všetko
  bolo spôsobené prechodom na wxPython 4 (NVDA od verzie 2018.3).

## Verzia 18.10

* Kompatibilné s NVDA od verzie 2018.3.
* Upravený kód pre Python 3.

## verzia 18.09.1-LTS

* Pri prepise playlistu do html tabuľky sa viac na generovanie hlavičiek
  nepoužívajú Python list string.

## verzia 18.09-LTS

Verzia 18.09.x je posledná, ktorá podporuje Studio 5.10 so staršou
technológiou. Od verzie 18.10 podporujeme Studio 5.11/5.20. Niektoré nové
funkcie môžu byť časom portované aj do verzie 18.09.

* Vyžadujeme NVDA od verzie 2018.3 lebo prechádzame na wxPython 4.
* Nastavenia doplnku sú prispôsobené pre strom s nastaveniami predstavený v
  NVDA od verzie 2018.2.
* Testovacie verzie boli skombinované do jednej vývojovej verzie. Vývojové
  verzie budete dostávať po začiarknutí príslušného políčka v pokročilých
  nastaveniach.
* Odteraz nie je možné nastaviť aktualizačný kanál. Ak chcete prejsť na
  vývojovú verziu doplnku, z tejto stránky si stiahnite vývojovú verziu.
* Začiarkávacie políčka pre vybratie metadát na prepis a oznamovanie, ako aj
  začiarkávacie polia pre pripojenia boli zmenené na zoznamso začiarkávacími
  poliami.
* NVDA si zapamätá špecifické nastavenia pre konkrétny profil pri zmene
  panela s nastaveniami. Jedná sa o upozornenia, oznamovanie metadát a
  streamovanie metadát.
* Prepis playlistu je možné uložiť vo formáte CSV (zoznam oddelený
  čiarkami\v).
* Skratka na uloženie nastavení ctrl+nvda+c uloží aj nastavenia
  doplnku. Vyžaduje sa NVDA od verzie 2018.3.

## Staršie verzie

Výpis zmien pre staršie verzie doplnku nájdete na samostatnej stránke
(anglicky).

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
