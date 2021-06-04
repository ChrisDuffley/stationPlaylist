# StationPlaylist #

* Autores: Geoff Shang, Joseph Lee e outros colaboradores
* Descargar [versión estable][1]
* Compatibilidade con NVDA: 2020.4 en diante

Este paquete de complementos proporciona unhha utilización mellorada do
Station Playlist Studio e outras apps de Station Playlist, así como
utilidades para controlar o Studio dende calquera lugar. As apps soportadas
inclúen Studio, Creator, Track Tool, VT Recorder, e Streamer, así como os
codificadores SAM, SPLe AltaCast.

Para máis información sobre o complemento, le a [guía do complemento][2].

NOTAS IMPORTANTES:

* Este complemento require o paquete StationPlaylist 5.30 ou posterior.
* Se usas o Windows 8 ou posterior, para unha mellor experiencia,
  deshabilita o modo atenuación de audio.
* A partires de 2018, os [rexistros de cambios para versións vellas][3]
  atoparanse en GitHub. Este readme do complemento listará cambios dende a
  versión 20.09 (2020) en diante.
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
* Control+Alt+inicio/fin (mentres se enfoca nunha pista no Studio, Creator,
  Remote VT e Track Tool): Moverse á primeira/última columna da pista.
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

Os seguintes comandos están sen asignar por defecto; se desexas asignalos,
utiliza o diálogo Xestos de Entrada para engadir ordes persoalizadas. Para
facelo, abre o menú NVDA dende a ventá de Studio, Preferencias, logo Xestos
de Entrada. Expande a categoría StationPlaylist, logo localiza os comandos
sen asignar dende a seguinte lista e selecciona "Engadir", logo escribe o
xesto que queres utilizar.

* Cambia á ventá SPL Studio dende calquera programa.
* Capa SPL Controller.
* Anunciar o estado do Studio como a reproducción de pista dende outros
  programas.
* Anunciar o estado de conexión do codificador dende calquera programa.
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
* Shift+F1: abre a guía do usuario en liña.

## SPL Controller

O SPL Controller é un conxunto de ordes en capas que podes utilizar para
controlar SPL Studio dende calquera lugar. Preme a orde da capa SPL
Controller, e NVDA dirá, "SPL Controller." Preme outra orde para controlar
varias opcións do Studio como o micrófono activado/desactivado ou reproducir
a seguinte pista.

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
para administrar perfís de emisión.

## Diálogo de perfiles de transmisión

Podes gardar as opcións para shows específicos en perfiles de emisión. Estes
perfiles pódense administrar dende o diálogo de perfiles de transmisión, ao
que se pode acceder premendo NVDA+Alt+P dende a ventá de Studio.

## Modo Táctil do SPL

Se estás a usar o Studio nunha computadora con pantalla tactil executando
Windows 8 ou posterior e tes NVDA 2012.3 ou posterior instalado, podes
realizar algunhas ordes do Studio dende a pantalla tactil. Primeiro usa un
toque con tgres dedos para cambiar a modo SPL, logo usa as ordes tactiles
listadas arriba para realizar ordes.

## Versión 21.06

* NVDA xa non fará nada ou non reproducirá un ton de erro ao tentar abrir
  varios diálogos do complemento como o diálogo de axustes do
  codificador. Éste é un arranxo crítico requerido para soportar NVDA
  2021.1.
* NVDA xa non parecerá non facer nada ou non reproducirá tons de erro ao
  anunciar o tempo completo (horas, minutos, segundos) dende Studio (orde
  sen asignar). Isto afecta a NVDA 2021.1 e posteriores.

## Versión 21.04/20.09.7-LTS

* 21.04: Requírese NVDA 2020.4 ou posterior.
* Nos codificadores, NVDA xa non falla ó anunciar a información de data e
  hora ao executar ordes de data/hora (NVDA+F12). Isto afecta a NVDA 2021.1
  ou posterior.

## Versión 21.03/20.09.6-LTS

* O requerimento de versión mínima de Windows está agora ligado ás versións
  de NVDA.
* Eliminado o atallo de correo de comentarios (Alt+NVDA+Guión). Por favor,
  envía comentarios ós desenvolvedores de complementos utilizando a
  información de contacto proporcionada no administrador de complementos.
* 21.03: algunhas partes do código fonte agora inclúen anotacións de tipo.
* 21.03: faise o código do complemento máis robusto coa axuda de Mypy (un
  comprobador de tipo estático de Python). Especificamente, arranxados
  varios erros que viñan de longo como a imposibilidade para NVDA de
  restablecer a configuración do complemento baixo certas circunstancias, ou
  a realización de intentos de gardar as opcións do codificador sen estar
  cargado. algúns arranxos importantes tamén se levaron á 20.09.6-LTS.
* Arranxados numerosos erros no diálogo de benvida do complemento
  (Alt+NVDA+F1 dende a ventá de Studio), incluíndo a mostra de varios
  diálogos de benvida e NVDA aparentando non facer nada ou reproducindo tons
  de erro cando se deixaba aberto o diálogo de benvida despois do peche de
  Studio.
* Arranxados numerosos erros co diálogo de comentarios da pista (NVDA+Alt+C
  tres veces dende unha pista en Studio), incluída a reprodución dun ton de
  erro ao tentar gardar comentarios, e a aparición de de varios diálogos de
  comentarios de pista se se premía NVDA+Alt+C varias veces. Se o diálogo de
  comentarios de pista aínda se mostra despois do peche de Studio, os
  comentarios non se gardarán.
* Varios atallos de columnas como o explorador de columnas
  (control+NVDA+fila de números) en pistas de Studio e anuncios de estado do
  codificador xa non proporcionan un resultado erróneo ao premérense tras un
  reinicio de NVDA enfocando pistas ou codificadores. Isto afecta a NVDA
  2020.4 ou posterior.
* Arranxados numerosos erros coas capturas de listas de reprodución
  (Asistente SPL, F8), incluíndo a imposibilidade de obter datos das
  capturas e o anuncio da pista incorrecta como pista máis curta ou longa.
* NVDA xa non anunciará "0 elementos na biblioteca" tras pechar Studio no
  medio dun escaneado de biblioteca.
* NVDA xa non fallará gardando os cambios nas opcións do codificador despois
  de que se encontren errores cargando as opcións do codificador e por
  conseguinte as opcións se reseteen ós valores predeterminados.

## Versión 21.01/20.09.5-LTS

A versión 21.01 soporta SPL Studio 5.30 e posterior.

* 21.01: Requírese NVDA 2020.3 ou posterior.
* 20.10: a opción de inclusión de encabezados de columna nos axustes do
  complemento eliminouse. O anunciado de encabezados de columna no paquete
  SPL e os codificadores controlarao o axuste do propio NVDA sobre os
  encabezados de columna de táboa.
* Engadida unha orde para alternar entre pantalla vs. configuración de orde
  e inclusión de columnas (NVDA+V). Ten en conta que esta orde só está
  dispoñible cando se enfoca unha pista no visualizador de listas de
  reprodución de Studio.
* A axuda en capa de SPL Assistant e Controller presentaranse como un
  documento en modo exploración no canto dun diálogo.
* NVDA xa non parará de anunciar o progreso de escaneo da biblioteca se se
  configurou para anunciar o proceso de escaneo ao utilizar unha pantalla
  braille.

## Versión 20.11.1/20.09.4-LTS

* Soporte inicial para o paquete StationPlaylist 5.50.
* Melloras para a presentación de varios diálogos do complemento gracias ás
  características do NVDA 2020.3.

## Versión 20.11/20.09.3-LTS

* 20.11: Requírese NVDA 2020.1 ou posterior.
* 20.11: Resoltas máis incidencias de estilo do código e erros potenciais
  con Flake8.
* Arranxadas varias incidencias co diálogo de benvida do complemento
  (Alt+NVDA+F1 dende Studio), incluído o comando errado para comentarios
  sobre o complemento (Alt+NVDA+guión).
* 20.11: O formato de presentación de columna para elementos de pista e
  codificador en todo o paquete StationPlaylist (incluíndo o codificador
  SAM) está agora baseado no formato de elemento de lista SysListView32.
* 20.11: agora NVDA anunciará a información de columna para pistas en todo
  StationPlaylist con independencia da opción "anunciar descrición de
  obxecto" no panel de opcións de presentación de obxectos do NVDA. Para a
  mellor experiencia, deixa esta opción activada.
* 20.11: No visualizador de listas de reprodución de Studio, as opcións de
  orde persoalizada e inclusión das columnas afectará a como se presentan as
  columnas das pistas ao utilizar a navegación de obxectos para moverse
  entre pistas, incluíndo o anunciado do obxecto actual no navegador.
* Se o anuncio vertical de columnas se configura nun valor diferente de "A
  columna que estea explorando", NVDA non anunciará datos de columna
  incorrectos despois de cambiar a posición da columna na pantalla vía rato.
* mellora na presentación das transcricións de listas de reprodución
  (Asistente SPL, Shift+F8) ao visualizar a transcrición en táboa HTML ou
  formato lista.
* 20.11: Nos codificadores, as etiquetas anunciaranse ao navegar por
  obxectos ademais de ao premer frecha arriba e abaixo para moverse entre
  codificadores.
* Nos codificadores, ademáis de alt+NVDA+0 da fila de números, pulsar F12
  tamén abrirá oo diálogo de axustes do codificador para aquel que se
  seleccionara.

## Versión 20.10/20.09.2-LTS

* Debido a trocos no formato do archivo de opcións dos codificadores,
  instalar unha versión antiga deste complemento tras instalar ésta causará
  un comportamento impredecible.
* Xa non é necesario reiniciar NVDA en modo de rexistro de depuración para
  ler as mensaxes de depuración dende o visualizador de rexistro. Podes ver
  as mensaxes de depuración se o nivel de rexistro está establecido en
  "depuración" dende o panel xeral das opcións do NVDA.
* No visualizador de listas de reprodución de Studio, NVDA non incluirá
  encabezados de columnas se esta opción está deshabilitada dende as opcións
  do complemento e a orde persoalizada de columnas ou os axustes de
  inclusión non están definidos.
* 20.10: a opción de inclusión de encabezados de columna nos axustes do
  complemento está obsoleta e eliminarase nunha versión futura. No futuro o
  anunciado de encabezados de columna no paquete SPL e os codificadores
  controlarao o axuste do propio NVDA sobre os encabezados de columna de
  táboa.
* Cando SPL Studio estea minimizado na bandexa do sistema (área de
  notificacións), NVDA anunciará esta circunstancia ao tentar saltar a
  Studio dende outros programas, xa sexa mediante un atallo dedicado ou como
  resultado da conexión dun codificador.

## Versión 20.09-LTS

A versión 20.09.x é a última serie de publicacións en soportar Studio 5.20 e
basados en tecnoloxías vellas, soportando versións futuras Studio 5.30 e
novas características do NVDA. Algunhas características retroportaranse á
20.09.x de ser necesario.

* Debido a cambios en NVDA, a opción de liña de comandos
  --spl-configvolatile xa non está dispoñible para facer as opcións do
  complemento de só lectura. Podes emular isto desmarcando a caixa de
  verificación "Gardar configuración ao saír do NVDA" dende o panel xeral
  das opcións de NVDA.
* Eliminada a opción características piloto da categoría de Opcións
  avanzadas nas opcións do complemento (Alt+NvDA+0), utilizada para permitir
  aos usuarios de versións de desenvolvemento probar código ó bordo do
  precipicio.
* As ordes de navegación por columnas en Studio están agora dispoñibles na
  lista de pistas localizada en peticións dos oíntes, insertar pistas e
  outras pantallas.
* Varias ordes de navegación por columnas comportaranse como as ordes de
  navegación por tablas do propio NVDA. Ademais de simplificar estas ordes,
  trae beneficios como maior facilidad de uso para usuarios con baixa
  visión.
* As ordes de navegación vertical por columnas (Control+Alt+frecha
  arriba/abaixo) están agora dispoñibles para Creator, o editor de listas de
  reprodución, Remote VT e Track Tool.
* A orde do visualizador de columnas de pista (Control+NVDA+guión) está
  agora dispoñible no editor de listas de reprodución de Creator e en Remote
  VT.
* A orde do visualizador de columnas de pista respectará a orde de columnas
  mostrada na pantalla.
* En codificadores SAM, mellorada a responsividade do NVDA ao premer
  Control+F9 e Control+F10 para conectar ou desconectar tódolos
  codificadores, respectivamente. Isto podería resultar nun incremento da
  verbosidade ao anunciar a información do codificador seleccionado.
* En codificadores SPL e AltaCast, agora premer F9 conectará o codificador
  seleccionado.

## Versións vellas

Por favor consulta a liga changelog para notas da versión para versións
vellas do complemento.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[3]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
