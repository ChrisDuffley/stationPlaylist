# StationPlaylist #

* Autores: Geoff Shang, Joseph Lee e outros colaboradores
* Descargar [versión estable][1]
* Compatibilidade con NVDA: 2022.2 en diante

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
* A partires de 2018, os [rexistros de cambios para versións vellas][3]
  atoparanse en GitHub. Este readme do complemento listará cambios dende a
  versión 22.03 (2022) en diante.
* Cando Studio está en execución, podes gardar, recargar as opcións
  gardadas, ou restablecer as opcións do complemento ás de fábrica premendo
  Control+NVDA+C, Control+NVDA+R unha vez, ou Control+NVDA+R tres veces,
  respectivamente, Isto tamén se aplica ás opcións dos codificadores - podes
  gardar e restablecer (non recargar) as opcións de codificadores se
  utilizas codificadores.

## Teclas de atallo

A maioría destes funcionarán só en Studio a menos que se especifique o
contrario.

* Alt+Shift+T dende a ventá do Studio: anuncia o tempo transcorrido para a
  pista actual en reproducción.
* Control+Alt+T (deslizamento con dous dedos cara abaixo no modo tactil SPL)
  dende a ventá do Studio: anuncia o tempo restante para a pista que se
  estea a reproducir.
* NVDA+Shift+F12 (deslizamento con dous dedos cara arriba no modo tactil
  SPL) dende a ventá Studio: anuncia o tempo de emisión como 5 minutos para
  o comezo da hora.Premendo dúas veces esta orde anunciará os minutos e
  segundos ata a hora.
* Alt+NVDA+1 (deslizamento con dous dedos cara á dereita no modo SPL) dende
  a ventá do Studio: Abre a categoría alarmas no diálogo de configuración no
  complemento Studio.
* Alt+NVDA+1 dende a ventá do Editor de Listas de Reprodución de Creator e o
  editor de listas de reprodución de Remote VT: anuncia o tempo programado
  para a lista cargada.
* Alt+NVDA+2 dende a ventá de Editor de Listas de Reprodución de Creator ou
  o editor de listas de reprodución de Remote VT: Anuncia a duración de toda
  a lista.
* Alt+NVDA+3 dende a ventá Studio:  conmuta o explorador de cart para
  deprender  as asignacións das cart.
* Alt+NVDA+2 dende a ventá de Editor de Listas de Reprodución de Creator ou
  o editor de listas de reprodución de Remote VT: Anuncia cando está a pista
  seleccionada programada para reproducirse.
* Alt+NVDA+2 dende a ventá de Editor de Listas de Reprodución de Creator ou
  o editor de listas de reprodución de Remote VT: Anuncia rotación e e
  categoría asociadas coa lista cargada.
* Control+NVDA+f dende a ventá do Studio: Abre un diálogo para procurar unha
  pista baseada no artista ou no nome da canción. Preme NVDA+F3 para
  procurar cara adiante ou NVDA+Shift+F3 para procurar cara atrás.
* Alt+NVDA+R dende a ventá do Studio: Pasos para as opcións de anunciado do
  escaneado da biblioteca.
* Control+Shift+X dende a ventá do Studio: Pasos para as opcións do
  temporizador braille.
* Control+Alt+frechas dereita e esquerda (mentres se enfoca nunha pista no
  Studio, Creator, Remote VT ou TrackTool): Moverse á columna
  anterior/seguinte da pista.
* Control+Alt+frecha arriba/abaixo (mentres se enfoque unha pista en Studio,
  Creator, Remote VT e Track Tool): Moverse á pista seguinte ou anterior e
  anunciar columnas específicas.
* Control+NVDA+1 a 0 (cun track enfocado en Studio, Creator -inclúe o editor
  de listas de reprodución-, Remote VT e Track Tool): Anunciar contido da
  columna para unha columna especificada (primeiras dez columnas por
  defecto). Premer este atallo dúas veces amosará a información de columna
  nunha xanela de modo exploración.
* Control+NVDA+- (guión, mentres se enfoca unha pista en Studio, Creator,
  Remote VT e Track Tool): amosar datos de todas as columnas dunha pista
  nunha xanela de modo exploración.
* NVDA+V mentres se enfoca unha pista (só visualizador de listas de
  reprodución de Studio): alterna o anunciado de columnas de pista entre
  orde de pantalla e orde persoalizada.
* Alt+NVDA+C mentres se enfoca unha pista (só visualizador de listas de
  reprodución de Studio): anuncia os comentarios da pista se os hai.
* Alt+NVDA+0 dende a ventá do Studio: Abre o diálogo de configuración do
  complemento.
* Alt+NVDA+P dende a ventá de Studio: Abre o diálogo de perfiles de
  transmisión de Studio.
* Alt+NVDA+F1: abre o diálogo de benvida.

## Ordes non asignadas

Os seguintes atallos están sen asignar por defecto; se desexas asignalos,
utiliza o diálogo Xestos de Entrada para engadir ordes persoalizadas. Para
facelo, dende a ventá de Studio, abre o menú NVDA dende a ventá de Studio,
Preferencias, logo Xestos de Entrada. Expande a categoría StationPlaylist,
logo localiza os comandos sen asignar dende a seguinte lista e selecciona
"Engadir", logo escribe o xesto que queres utilizar.

Importante: algúns destes atallos non funcionarán cando NVDA estea
funcionando en modo seguro, como por exemplo na pantalla de inicio de
sesión.

* Cambia á ventá SPL Studio dende calquera programa (non dispoñible en modo
  seguro).
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
* Atopar texto en columnas específicas.
* Atopar pistas ca duración que caia dentro dun rango dado a través do
  buscador de rango de tempo.
* Habilitar ou deshabilitar cíclicamente metadatos do streaming.

## Ordes adicionais cando se utilizan os codificadores

As seguintes ordes están dispoñibles cando se utilizan os codificadores:

* F9: conecta o codificador seleccionado.
* F10 (só codificador SAM): Desconecta o codificador seleccionado.
* Control+F9: Conectar todos os codificadores.
* Control+F10 (só codificador SAM): Desconecta todos os codificadores.
* F11: Conmuta se NVDA cambiará á ventá do Studio para o codificador
  seleccionado se está conectado.
* Shift+F11: conmuta  se Studio reproducirá a primeira pista seleccionada
  cando o codificador estéa conectado a un servidor de streaming.
* Control+F11: Conmuta a monitorización de fondo do codificador
  seleccionado.
* Control+F12: Abre un diálogo para seleccionar o codificador que
  eliminaches(para realiñar  as etiquetas e as opcións do codificador).
* Alt+NVDA+0 e F12: abre o diálogo de opcións do codificador para configurar
  opcións como a etiqueta de codificador.

Ademáis, as ordes de revisión de columna están dispoñibles, incluindo:

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

As ordes dispoñibles son:

* A: Automatización.
* C (Shift+C na distribución JAWS): Título para a pista actualmente en
  reprodución.
* C (distribución JAWS): conmuta o explorador de cart (só visualizador de
  lista de reprodución).
* D (R na distribución JAWS): duración restante para a lista de reprodución
  (se se da unha mensaxe de erro, move ao visualizador de lista de
  reproducción e logo aílla esta orden).
* E: Estado dos metadatos do streaming.
* Shift+1 ata Shift+4, Shift+0: estado para as URLs dos metadatos
  individuais do streaming (0 é para o codificador DSP).
* F: atopar pista (só visualizador de lista de reprodución).
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

As ordes dispoñibles para o SPL Controller son:

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
* C: Título e duración da pista en reproducción.
* Shift+C: Título e duración da pista próxima se a hai.
* E: Estado de conexión do codificador.
* I: Contador de oíntes.
* Q: Informadión de estado de Studio como se se está reproducindo unha
  pista, se o micrófono está acendido e outros.
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

## Versión 23.01

* Require NVDA 2022.3 ou posterior.
* Requírese Windows 10 ou posterior xa que Windows 7, 8, e 8.1 xa non se
  soportan dende Microsoft dende xaneiro do 2023.
* Eliminadas as ordes de primeira e última columna de pista
  (Control+Alt+Inicio/Final) xa que NVDA inclúe eses comandos.
* Eliminados o módulo de aplicación para Streamer e o método para superar o
  problema coa caixa de edición de tamaño do búfer, xa que Streamer se
  convertiu nun módulo alias para SPL Engine.

## Versión 22.03

Ésta é a derradeira versión estable que soporta Studio 5.3x así como Windows
7 Service Pack 1, 8, e 8.1.

* Requírese NVDA 2021.3 ou posterior.
* Amosarase unha mensaxe de advertencia ao tentar instalar o complemento en
  Windows 7, 8, e 8.1.
* Xa non é posible realizar os seguintes xestos se NVDA se está executando
  en modo seguro: todos os atallos da capa de SPL Controller, cambiar a
  Studio dende outros programas, obter estado de Studio e estado do
  codificador dende outros programas.
* Xa non é posible copiar os comentarios da pista ó portapapeis ou engadir
  ou cambiar os comentarios se NVDA se está executando en modo seguro.
* Xa non é posible copiar as transcricións de listas de reprodución ou
  gardalas nun arquivo se NVDA se está executando en modo seguro. Só se
  permitirá ver as transcricións en modo seguro.
* Para mellorar a seguridade, as ordes da guía de usuario en liña do SPL
  Assistant (Shift+F1) elimináronse.
* Xa non é posible crear, copiar, renomear, eliminar, ou configurar o estado
  de cambio instantáneo para perfiles de emisión se NVDA está en modo
  seguro.
* Xa non é posible configurar as opcións avanzadas do complemento ou
  restablecer as opcións por defecto dende a pantalla de opcións do
  complemento se NVDA se está executando en modo seguro.
* En Studio, NVDA xa non fará nada nin reproducirá tons de erro ao tentar
  obter capturas de lista de reprodución (SPL Assistant, F8) se a lista de
  reprodución cargada consiste soamente de marcadores de hora.
* En Creator 6.0, NVDA xa non parecerá non facer nada cando unha das
  columnas do explorador de columnas sexa "Date restriction" (restrición de
  data) xa que a columna se renomeou a "Restricións".

## Versións vellas

Por favor consulta a liga changelog para notas da versión para versións
vellas do complemento.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[3]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
