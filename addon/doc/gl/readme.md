# StationPlaylist #

* Authors: Christopher Duffley <nvda@chrisduffley.com> (formerly Joseph Lee
  <joseph.lee22590@gmail.com>, originally by Geoff Shang and other
  contributors)

Este paquete de complementos proporciona unhha utilización mellorada do
Station Playlist Studio e outras apps de Station Playlist, así como
utilidades para controlar o Studio dende calquera lugar. As apps soportadas
inclúen Studio, Creator, Track Tool, VT Recorder, e Streamer, así como os
codificadores SAM, SPLe AltaCast.

Para máis información sobre o complemento, le a [guía do complemento][2].

NOTAS IMPORTANTES:

* Este complemento require o paquete StationPlaylist 5.40 ou posterior.
* Algunhas características do complemento desactivaranse ou limitaranse se
  NVDA se está executando en modo seguro, como por exemplo na pantalla de
  inicio de sesión.
* Para unha mellor experiencia, deshabilita o modo atenuación de audio.
* A partir de 2018, os [rexistros de cambios para versións vellas][3]
  atoparanse en GitHub. Este léeme (readme) do complemento listará cambios
  dende a versión 23.02 (2023) en diante.
* Cando Studio está en execución, podes gardar, recargar as opcións
  gardadas, ou restablecer as opcións do complemento ás de fábrica premendo
  Control+NVDA+C, Control+NVDA+R unha vez, ou Control+NVDA+R tres veces,
  respectivamente, Isto tamén se aplica ás opcións dos codificadores - podes
  gardar e restablecer (non recargar) as opcións de codificadores se
  utilizas codificadores.
* Many commands will provide speech output while NVDA is in speak on demand
  mode (NVDA 2024.1 and later).

## Teclas de atallo

Most of these will work in Studio only unless otherwise specified. Unless
noted otherwise, these commands support speak on demand mode.

* Alt+Shift+T from Studio window: announce elapsed time for the currently
  playing track.
* Control+Alt+T (two finger flick down in SPL touch mode) from Studio
  window: announce remaining time for the currently playing track.
* NVDA+Shift+F12 (deslizamento con dous dedos cara arriba no modo tactil
  SPL) dende a ventá Studio: anuncia o tempo de emisión como 5 minutos para
  o comezo da hora.Premendo dúas veces esta orde anunciará os minutos e
  segundos ata a hora.
* Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens
  alarms category in Studio add-on configuration dialog (does not support
  speak on demand).
* Alt+NVDA+1 dende a ventá do Editor de Listas de Reprodución de Creator e o
  editor de listas de reprodución de Remote VT: anuncia o tempo programado
  para a lista cargada.
* Alt+NVDA+2 dende a ventá de Editor de Listas de Reprodución de Creator ou
  o editor de listas de reprodución de Remote VT: Anuncia a duración de toda
  a lista.
* Alt+NVDA+3 from Studio window: Toggles cart explorer to learn cart
  assignments (does not support speak on demand).
* Alt+NVDA+2 dende a ventá de Editor de Listas de Reprodución de Creator ou
  o editor de listas de reprodución de Remote VT: Anuncia cando está a pista
  seleccionada programada para reproducirse.
* Alt+NVDA+2 dende a ventá de Editor de Listas de Reprodución de Creator ou
  o editor de listas de reprodución de Remote VT: Anuncia rotación e e
  categoría asociadas coa lista cargada.
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
* Control+NVDA+1 a 0 (cun track enfocado en Studio, Creator -inclúe o editor
  de listas de reprodución-, Remote VT e Track Tool): Anunciar contido da
  columna para unha columna especificada (primeiras dez columnas por
  defecto). Premer este atallo dúas veces amosará a información de columna
  nunha xanela de modo exploración.
* Control+NVDA+- (hyphen while focused on a track in Studio, Creator, Remote
  VT, and Track Tool): display data for all columns in a track on a browse
  mode window (does not support speak on demand).
* NVDA+V while focused on a track (Studio's playlist viewer only): toggles
  track column announcement between screen order and custom order (does not
  support speak on demand).
* Alt+NVDA+C mentres se enfoca unha pista (só visualizador de listas de
  reprodución de Studio): anuncia os comentarios da pista se os hai.
* Alt+NVDA+0 from Studio window: Opens the Studio add-on configuration
  dialog (does not support speak on demand).
* Alt+NVDA+P from Studio window: Opens the Studio broadcast profiles dialog
  (does not support speak on demand).
* Alt+NVDA+F1: Open welcome dialog (does not support speak on demand).

## Ordes non asignadas

Os seguintes atallos están sen asignar por defecto; se desexas asignalos,
utiliza o diálogo Xestos de Entrada para engadir ordes persoalizadas. Para
facelo, dende a ventá de Studio, abre o menú NVDA dende a ventá de Studio,
Preferencias, logo Xestos de Entrada. Expande a categoría StationPlaylist,
logo localiza os comandos sen asignar dende a seguinte lista e selecciona
"Engadir", logo escribe o xesto que queres utilizar.

Important: some of these commands will not work if NVDA is running in secure
mode such as from login screen. Not all commands support speak on demand.

* Switching to SPL Studio window from any program (unavailable in secure
  mode, does not support speak on demand).
* Capa SPL Controller (non dispoñible en modo seguro).
* Anunciar o estado do Studio como a reproducción de pista dende outros
  programas (non dispoñible en modo seguro).
* Anunciar o estado de conexión do codificador dende calquera programa (non
  dispoñible en modo seguro).
* Capa SPL Assistant desde SPL Studio.
* Anunciar tempo incluíndo segundos dende o SPL Studio.
* Anunciar temperatura.
* Anunciar o título da seguinte pista se se programou.
* Anunciando título da pista actualmente en reprodución.
* Marcar pista actual para comezo da análise de tempo da pista.
* Realizar análise de tempo da pista.
* Tomar instantáneas da listaxe de reprodución.
* Find text in specific columns (does not support speak on demand).
* Find tracks with duration that falls within a given range via time range
  finder (does not support speak on demand).
* Quickly enable or disable metadata streaming (does not support speak on
  demand).

## Ordes adicionais cando se utilizan os codificadores

The following commands are available when using encoders, and the ones used
for toggling options for on-connection behavior such as focusing to Studio,
playing the first track, and toggling of background monitoring can be
assigned through the Input Gestures dialog in NVDA menu, Preferences, Input
Gestures, under the StationPlaylist category. These commands do not support
speak on demand.

* F9: conecta o codificador seleccionado.
* F10 (só codificador SAM): Desconecta o codificador seleccionado.
* Control+F9: Conectar todos os codificadores.
* Control+F10 (só codificador SAM): Desconecta todos os codificadores.
* Control+Shift+F11: Toggles whether NVDA will switch to Studio window for
  the selected encoder if connected.
* Shift+F11: conmuta  se Studio reproducirá a primeira pista seleccionada
  cando o codificador estéa conectado a un servidor de streaming.
* Control+F11: Conmuta a monitorización de fondo do codificador
  seleccionado.
* Control+F12: Abre un diálogo para seleccionar o codificador que
  eliminaches(para realiñar  as etiquetas e as opcións do codificador).
* Alt+NVDA+0 or F12: Opens encoder settings dialog to configure options such
  as encoder label.

In addition, column review commands are available, including (supports speak
on demand):

* Control+NVDA+1: posición do codificador.
* Control+NVDA+2: etiqueta de codificador.
* Control+NVDA+3 dende o codificador SAM: formato do codificador.
* Control+NVDA+3 dende o codificador SPL ou AltaCast: opcións do
  codificador.
* Control+NVDA+4 dende o codificador SAM: Estado da conexión do codificador.
* Control+NVDA+4 dende o codificador SPL ou AltaCast: velocidade de
  transferencia ou estado da conexión.
* Control+NVDA+5 dende o codificador SAM: descripción do estado da conexión.

## SPL Assistant layer

Este conxunto de comandos en capas de ordes permíteche obter varios estados
no SPL Studio, coma se unha pista se reproduce, duración total de todas as
pistas para a hora e outros. Dende calquera ventá do SPL Studio, preme a
orde da capa SPL Assistant, logo preme una das teclas da lista de abaixo
(una ou máis ordes son exclusivamente para o visualizador de lita de
reprodución). Tamén podes configurar NVDA para emular ordes de outros
lectores de pantalla.

The available commands are (most commands support speak on demand):

* A: Automatización.
* C (Shift+C na distribución JAWS): Título para a pista actualmente en
  reprodución.
* C (JAWS layout): Toggle cart explorer (playlist viewer only, does not
  support speak on demand).
* D (R na distribución JAWS): duración restante para a lista de reprodución
  (se se da unha mensaxe de erro, move ao visualizador de lista de
  reproducción e logo aílla esta orden).
* Control+D (Studio 6.10 and later): Control keys enabled/disabled.
* E: Estado dos metadatos do streaming.
* Shift+1 ata Shift+4, Shift+0: estado para as URLs dos metadatos
  individuais do streaming (0 é para o codificador DSP).
* F: Find track (playlist viewer only, does not support speak on demand).
* H: Duración da música para o actual espazo de tempo.
* Shift+H: duración das pistas restantes para o slot horario.
* I (L na distribución JAWS): conta de oíntes.
* K: móvese á pista marcada (só no visualizador de lista de reprodución).
* Control+K: pon a pista actual como a pista  marcada (só no visualizador de
  lista de reprodución).
* L (Shift+L na distribución JAWS): Liña auxiliar.
* M: Micrófono.
* N: Título para a seguinte pista programada.
* P: Estado da reproducción (reproducindo ou detido).
* Shift+P: Ton da pista actual.
* R (Shift+E na distribución JAWS): Grabar en ficheiro activado /
  desactivado.
* Shift+R: Monitorización  do escaneado da biblioteca en progreso.
* S: Comezos de pistas (programado).
* Shift+S: tempo ata o que se reproducirá a pista selecionada (comezos de
  pista).
* T: modo editar/insertar Cart aceso/apagado.
* U: Studio up time.
* W: Clima e temperatura se se configurou.
* Y: Estado da lista de reprodución modificada.
* F8: toma instantáneas da listaxe de reprodución (número de pistas, pista
  máis longa, etc.).
* Shift+F8: Solicita transcripcións da listaxe de reprodución en varios
  formatos.
* F9: marca a pista actual como inicio da análise de lista de reprodución
  (só no visualizador de lista de reprodución).
* F10: realiza análise de tempo da pista (só no visualizador de lista de
  reprodución).
* F12: cambia entre un perfil actual e un predefinido.
* F1: Capa de axuda.

## SPL Controller

O SPL Controller é un conxunto de ordes en capas que podes utilizar para
controlar SPL Studio dende calquera lugar. Preme a orde da capa SPL
Controller, e NVDA dirá, "SPL Controller." Preme outra orde para controlar
varias opcións do Studio como o micrófono activado/desactivado ou reproducir
a seguinte pista.

Importante: os atallos da capa de SPL Controller están desactivados se NVDA
se está executando en modo seguro.

The available SPL Controller commands are (some commands support speak on
demand):

* P: Reproducir a seguinte pista seleccionada.
* U: Pausar ou despausar a reprodución.
* S: Deter a pista con fundido de saída.
* T: Detención instantánea.
* M: Activar micrófono.
* Shift+M: Apagar micrófono.
* A. Activar automatización.
* Shift+A: Desactivar automatización.
* L: Activar entrada de liña.
* Shift+L: Desactivar entrada de liña.
* R: Tempo restante para a pista actualmente en reproducción.
* Shift+R: Progreso do escaneo da libraría.
* C: Title and duration of the currently playing track (supports speak on
  demand).
* Shift+C: Title and duration of the upcoming track if any (supports speak
  on demand).
* E: Encoder connection status (supports speak on demand).
* I: Listener count (supports speak on demand).
* Q: Studio status information such as whether a track is playing,
  microphone is on and others (supports speak on demand).
* Teclas de cart (F1, Control+1, por exemplo): reproducir carts asignados
  dende calquera lado.
* H: Axuda en capa.

## Alarmas de pista e micrófono

Por omisión, NvDA reproducirá un pitido se quedan cinco segundos da pista
(outro) e/ou intro, así como oirás un pitido se o micrófono estivo activo un
tempo. Para configurar as alarmas de pista e micrófono, preme Alt+NVDA+1
para abrir as opcións de alarmas na pantalla de opcións do complemento
Studio. Tamén podes utilizar esta pantalla para configurar se queres oír un
pitido, unha mensaxe ou ambos cando as alarmas estean activas.

## Track Finder

Se desexas atopar rapidamente unha canción dun artista ou polo nome da
canción, dende a lista de pistas, preme Control+NVDA+F. Teclea o nome do
artista ou o nome da canción. NVDA ponte na canción, de ser atopado ou amosa
un erro se non pode atopar a música que estás a buscar. Para atopar unha
canción ou artista previamente buscados, preme NVDA+Shift+F3 para atopar
cara adiante ou cara atrás.

Nota: o Track Finder é sensible ás maiúsculas.

## Explorador de Cart

Depenndendo da edición, SPL Studio permite ate 96 carts para se asignar para
a reproducción. NVDA permíteche escoitar cal cart, ou jingle se asignou a
estas ordes.

Para deprender as asignacións de cart, dende o SPL Studio, preme
Alt+NVDA+3. Premendo a orden do cart unha vez dirache cal jingle se asignou
á orden. Premendo a orden do cart dúas veces reproduce o jingle. Preme
Alt+NVDA+3 para saír do explorador de cart. Olla a guía do complemento para
máis información sobre o explorador de cart.

## Análise de tempo de pista

Para obter a lonxitude para reproducir as pistas selecionadas, marca a pista
actual para comezo da análise de tempo da pista (SPL Assistant, F9), logo
preme SPL Assistant, F10 ó chegares ó remate da seleción.

## Explorador de Columnas

Premendo Control+NVDA+1 ata 0, podes obter contidos das columnas
especificadas. Por omisión, estas son  as dez primeiras nun elemento de
pista (en Studio: artista, título, duración, intro, "outro",  categoría,
ano, álbume, xénero e mood). Para Creator e Remote VT, os datos das columnas
dependen da orde das columnas como se amosa na pantalla. En Studio, a lista
de pistas principal de Creator e Track Tool, os lotes de columnas están
preestablecidos independentemente da orde das columnas na pantalla e pódense
configurar dende o diálogo de opcións do complemento, baixo a categoría
explorador de columnas.

## Anuncio de columna de pista

Podes facer que NVDA anuncie as columnas da pista do visualizador de listas
de reprodución de estudio na orde en que aparecen na pantalla ou utilizando
unha orde persoalizada e/ou excluír certas columnas. Preme NVDA+V para
cambiar este comportamento mentres enfoques una pista no visualizador de
listas de reprodución de Studio. Para persoalizar a inclusión de columnas e
a súa orde, no panel anuncio de columnas das opciónes do complemento,
desmarca "Anunciar columnas na orde que se amosan na pantalla" e logo
persoaliza as columnas incluídas e/ou a orde de columnas.

## Instantáneas da listaxe de reprodución

Podes premer SPL Assistant, F8 mentres se enfoque sobre unha listaxe de
reprodución no Studio para obter varias estadísticas acerca dunha listaxe de
reprodución, incluindo o número de pistas na listaxe, a pista máis longa,
listaxe de artistas e así. Despois de asignar unha orde persoalizada para
esta característica, premer dúas veces a orde persoalizada fará que o NVDA
presente a información da instantánea da listaxe de reprodución coma unha
páxina web para que podas usar o modo exploración para navegar (preme escape
para pechar).

## Transcripcións da listaxe de reprodución

Premendo en SPL Assistant, Shift+F8 presentará una Caixa de diálogo para
permitirche solicitar transcripcións de listaxe de reproducción en varios
formatos, incluindo nun formato de texto plano, e táboa HTML ou unha
listaxe.

## Diálogo Configuración

Dende a ventá do studio, podes premer Alt+NVDA+0 para abrir o diálogo de
configuración do complemento. Alternativamente, vai ó menú Preferencias do
NVDA e seleciona o elemento Opcions do SPL Studio. Este diálogo tamén se usa
para administrar perfís de emisión. Non todas as opcións están dispoñibles
se NVDA se está executando en modo seguro.

## Diálogo de perfiles de transmisión

Podes gardar as opcións para shows específicos en perfiles de emisión. Estes
perfiles pódense administrar dende o diálogo de perfiles de transmisión, ao
que se pode acceder premendo NVDA+Alt+P dende a ventá de Studio.

## Modo Táctil do SPL

Se estás a usar o Studio nunha computadora con pantalla tactil con NVDA
instalado, podes realizar algunhas ordes do Studio dende a pantalla
tactil. Primeiro usa un toque con tres dedos para cambiar a modo SPL, logo
usa as ordes tactiles listadas arriba para realizar ordes.

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

## Versión 23.02

* Require NVDA 2022.4 ou posterior.
* Requírese Windows 10 21H2 (Actualización de novembro de 2021/compilación
  19044) ou posterior.
* No visualizador de listas de reprodución de Studio, NVDA non anunciará
  encabezados de columnas como artista ou título se a opción de cabeceiras
  de táboas está configurada a "filas e columnas" ou "columnas" no panel de
  opcións de formateado de documentos de NVDA.

## Versións vellas

Please see the [changelog][3] for release notes for old add-on releases.

[[!tag dev stable]]

[2]: https://github.com/chrisDuffley/stationplaylist/wiki/SPLAddonGuide

[3]: https://github.com/ChrisDuffley/stationplaylist/wiki/splchangelog
