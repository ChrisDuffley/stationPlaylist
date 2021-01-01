# Station Playlist #

* Autori: Geoff Shang, Joseph Lee a ďalší
* Stiahnuť [stabilnú verziu][1]
* Stiahnuť [vývojovú verziu][2]
* Download [long-term support version][3] - for Studio 5.20 users
* NVDA compatibility: 2019.3 to 2020.2

Doplnok zlepšuje prístupnosť Station Playlist Studio a ďalších pridružených
aplikácií a tiež umožňuje ovládať Station Playlist mimo hlavného okna
aplikácie. Podporuje tiež aplikácie Studio, Creator, Track Tool, VT
Recorder, Streamer, a tiež SAM, SPL, a AltaCast enkodéri.

Podrobnosti si môžete prečítať v [dokumentácii (anglicky)][4].

Dôležité:

* Doplnok vyžaduje StationPlaylist suite od verzie 5.20.
* Ak používate Systém od verzie Windows 8, odporúčame vám vypnúť funkciu
  automatického stišovania.
* Starting from 2018, [changelogs for old add-on releases][5] will be found
  on GitHub. This add-on readme will list changes from version 20.01 (2020)
  onwards.
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
* Control+Alt+left/right arrow (while focused on a track in Studio, Creator,
  Remote VT, and Track Tool): Move to previous/next track column.
* Control+Alt+Home/End (while focused on a track in Studio, Creator, Remote
  VT, and Track Tool): Move to first/last track column.
* Control+Alt+up/down arrow (while focused on a track in Studio, Creator,
  Remote VT, and Track Tool): Move to previous/next track and announce
  specific columns.
* Ctrl+NVDA+1 až 0 (Pri zobrazení skladby v okne Studio, Creator (vrátane
  úpravy playlistu), Remote VT, a Track Tool): Oznámi príslušné metadáta
  (prvých 10). Stlačené dvakrát rýchlo za sebou zobrazí metadáta v režime
  prehliadania.
* Control+NVDA+- (hyphen while focused on a track in Studio, Creator, Remote
  VT, and Track Tool): display data for all columns in a track on a browse
  mode window.
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

* F9: connect the selected encoder.
* F10 (SAM encoder only): Disconnect the selected encoder.
* Control+F9: Connect all encoders.
* Control+F10 (SAM encoder only): Disconnect all encoders.
* F11: Aktivuje a deaktivuje automatické prepnutie do okna Studio po
  pripojení.
* Shift+F11: určuje, či sa automaticky prehrá prvá vybratá skladba po
  pripojení na server.
* Ctrl+F11: Zapína a vypína monitorovanie vybratého pripojenia na pozadí.
* Control+F12: opens a dialog to select the encoder you have deleted (to
  realign encoder labels and settings).
* Alt+NVDA+0: Opens encoder settings dialog to configure options such as
  encoder label.

Dostupné sú tieto príkazy na prezeranie stĺpcov:

* Ctrl+NVDA+1: Pozícia enkodéra.
* Control+NVDA+2: encoder label.
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
* C (Shift+C v rozložení pre JAWS): Oznámi názov prehrávanej skladby.
* C (Rozloženie JAWS): Zobraziť jingle (len z playlistu).
* D (R v rozložení pre JAWS): Oznámi ostávajúci čas do konca skladby. (Ak
  nefunguje, zopakujte skratku zo zobrazenia playlistu).
* E: Oznámi Stav streamovania metadát.
* Shift+1 až Shift+4: Stav jednotlivých pripojení. Shift+0: Stav pre DSP
  enkodér.
* F: Nájsť skladbu (len zo zoznamu skladieb).
* H: Oznámi Trvanie skladieb v aktuálnom hodinovom slote.
* Shift+H: Oznámi zostávajúci čas skladieb v aktuálnom hodinovom slote.
* I (L v rozložení pre JAWS): Oznámi počet pripojených poslucháčov.
* K: Prejde na záložku (vyznačenú skladbu v zozname skladieb).
* Ctrl+K: Nastaví aktuálnu skladbu ako záložku (v zobrazení playlistu).
* L (Shift+L v rozložení JAWS): Line in.
* M: Mikrofón.
* N: Oznámi Názov nasledujúcej skladby.
* P: Oznámi Stav prehrávania (prehrávanie alebo zastavené).
* Shift+P: Oznámi tóninu skladby.
* R (Shift+E v rozložení JAWS): zapína a vypína nahrávanie do súboru.
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

## Version 20.09-LTS

Version 20.09.x is the last release series to support Studio 5.20 and based
on old technologies, with future releases supporting Studio 5.30 and more
recent NVDA features. Some new features will be backported to 20.09.x if
needed.

* Due to changes in NVDA, --spl-configvolatile command line switch is no
  longer available to make add-on settings read-only. You can emulate this
  by unchecking "Save configuration when exiting NVDA" checkbox from NVDA's
  general settings panel.
* Removed pilot features setting from Advanced settings category under
  add-on settings (Alt+NVDA+0), used to let development snapshot users test
  bleeding-edge code.
* Column navigation commands in Studio are now available in track lists
  found in listener requests, insert tracks and other screens.
* Various column navigation commands will behave like NVDA's own table
  navigation commands. Besides simplifying these commands, it brings
  benefits such as ease of use by low vision users.
* Vertical column navigation (Control+Alt+up/down arrow) commands are now
  available for Creator, playlist editor, Remote VT, and Track Tool.
* Track columns viewer command (Control+NVDA+hyphen) is now available in
  Creator's Playlist Editor and Remote VT.
* Track columns viewer command will respect column order displayed on
  screen.
* In SAM encoders, improved NVDA's responsiveness when pressing Control+F9
  or Control+F10 to connect or disconnect all encoders, respectively. This
  may result in increased verbosity when announcing the selected encoder
  information.
* In SPL and AltaCast encoders, pressing F9 will now connect the selected
  encoder.

## Version 20.07

* In Studio's playlist viewer, NVDA will no longer appear to do nothing or
  play error tones when attempting to delete tracks or after clearing the
  loaded playlist while focused on playlist viewer.
* When searching for tracks in Studio's insert tracks dialog, NVDA will
  announce search results if results are found.
* NVDA will no longer appear to do nothing or play error tones when trying
  to switch to a newly created broadcast profile and save add-on settings.
* In encoder settings, "stream label" has been renamed to "encoder label".
* Dedicated stream labeler command (F12) has been removed from
  encoders. Encoder labels can be defined from encoder settings dialog
  (Alt+NVDA+0).
* System focus will no longer move to Studio repeatedly or selected track
  will be played when an encoder being monitored in the background
  (Control+F11) connects and disconnects repeatedly.
* In SPL encoders, added Control+F9 command to connect all encoders (same as
  F9 command).

## verzia 20.06

* Opravené drobné chyby v kóde.
* Opravené oznamovanie správ doplnku v Angličtine v situáciách, keď bol
  dostupný preklad.
* Časovo aktivované profily nie sú viac podporované.
* Odstránené rozloženie klávesovách skratiek pre Window-eyes. Ak ste mali
  nastavené toto rozloženie, bude sa odteraz používať rozloženie NVDA.
* Odstránené upozornenie na stišovanie audia, nakoľko toto v skutočnosti
  zasahuje len málo používateľou so špecifickým nastavením.
* Ak pri nastavovaní enkodéra dôjde k chybe, nie je potrebné vracať sa do
  okna studio. Nastavenia sa vynulujú pri prechode do okna enkodéra.
* V názve okna SAM enkodéra sa zobrazuje formát streamu a nie pozícia.

## verzia 20.05

* Prvotná podpora pre aplikáciu na nahrávanie vstupov Remote VT (voice
  track), a tiež podpora pre remote playlist editor s rovnakými príkazmi ako
  Creator.
* Commands used to open separate alarm settings dialogs (Alt+NVDA+1,
  Alt+NVDA+2, Alt+NVDA+4) has been combined into Alt+NVDA+1 and will now
  open alarms settings in SPL add-on settings screen where track outro/intro
  and microphone alarm settings can be found.
* Odstránená možnos nastaviť čas a dĺžku trvania spusteného profilu.
* Odstránená možnosť odpočítavania pri spustení časovaného profilu.
* Keďže čítač obrazovky Window-Eyes už firma Vispero  nevyvíja od roku 2017,
  budú z nasledujúcich verzií doplnku odstránené skratky pre tento čítač
  obrazovky. Ak používate rozloženie pre Window-eyes, NVDA na túto
  skutočnosť upozorní a odporučí nastavenie iného rozloženia (JAWS alebo
  NVDA).
* When using Columns Explorer slots (Control+NVDA+number row commands) or
  column navigation commands (Control+Alt+home/end/left arrow/right arrow)
  in Creator and Remote VT client, NVDA will no longer announce wrong column
  data after changing column position on screen via mouse.
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
* In encoders, NVDA will play connection tone every half a second while an
  encoder is connecting.
* NVDA oznamuje chyby pripojenia aj v prípade, že dôjde k chybeale pokus o
  pripájanie pokračuje.
* A new setting has been added to encoder settings to let NVDA announce
  connection messages until the selected encoder is connected. This setting
  is enabled by default.

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

## Staršie verzie

Výpis zmien pre staršie verzie doplnku nájdete na samostatnej stránke
(anglicky).

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: https://addons.nvda-project.org/files/get.php?file=spl-lts20

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
