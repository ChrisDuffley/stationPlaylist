# StationPlaylist #

* Autores: Geoff Shang, Joseph Lee e outros colaboradores
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]
* Compatibilidade con NVDA: da 2019.3 á 2020.1

Este paquete de complementos proporciona unhha utilización mellorada do
Station Playlist Studio e outras apps de Station Playlist, así como
utilidades para controlar o Studio dende calquera lugar. As apps soportadas
inclúen Studio, Creator, Track Tool, VT Recorder, e Streamer, así como os
codificadores SAM, SPLe AltaCast.

Para máis información acerca do complemento, le a [guía do
complemento][4]. Para os desenvolvedores que queran saber cómo compilar o
complemento, consulta buildInstructions.txt localizado na raíz do
repositorio do código fonte.

NOTAS IMPORTANTES:

* Este complemento require o paquete StationPlaylist 5.20 ou posterior.
* Se usas o Windows 8 ou posterior, para unha mellor experiencia,
  deshabilita o modo atenuación de audio.
* A partires de 2018, os [rexistros de cambios para versións vellas][5]
  atoparanse en GitHub. Este readme do complemento listará cambios dende a
  versión 18.09 (2018 en diante).
* Certas características do complemento non funcionarán baixo algunhas
  condicións, incluindo a execución do NVDA en modo seguro.
* Debido a limitacións técnicas, non podes instalar nin usar este
  complemento na versión de Windows Store do NVDA.
* As características marcadas como "experimental" están concebidas para
  probar algo antes dunha publicación máis ampla, polo que non estarán
  habilitadas en versións estables.
* Cando Studio está en execución, podes gardar, recargar as opcións
  gardadas, ou restablecer as opcións do complemento ás de fábrica premendo
  Control+NVDA+C, Control+NVDA+R unha vez, ou Control+NVDA+R tres veces,
  respectivamente, Isto tamén se aplica ás opcións dos codificadores - podes
  gardar e restablecer (non recargar) as opcións de codificadores se
  utilizas codificadores.
* A característica de perfiles de transmisión baseados en tempo está
  descatalogada e eliminarase nunha versión futura.

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
* Alt+NVDA+1 (deslizamento con dous dedos cara a esquerda no modo tactil
  SPL) dende a ventá do Studio: Abre a categoría alarmas no diálogo de
  configuración no complemento Studio.
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
  Studio, Creator, Remote VT ou TrackTool): anuncia a columna da pista
  seguinte ou anterior.
* Control+Alt+inicio/fin (mentres se enfoca nunha pista no Studio, Creator,
  Remote VT e Track Tool): anuncia a primeira/última columna da pista.
* Control+Alt+frecha arriba/abaixo (mentres se enfoque unha pista só en
  Studio): Moverse á pista seguinte ou anterior e anuncia columnas
  específicas.
* Control+NVDA+1 a 0 (cun track enfocado en Studio, Creator -inclúe o editor
  de listas de reprodución-, Remote VT e Track Tool): Anunciar contido da
  columna para unha columna especificada (primeiras dez columnas por
  defecto). Premer este atallo dúas veces amosará a información de columna
  nunha xanela de modo exploración.
* Control+NVDA+- (guión, mentres se enfoca unha pista en Studio, Creator, e
  Track Tool): amosar datos de todas as columnas dunha pista nunha xanela de
  modo exploración.
* Alt+NVDA+C mentres se enfoca unha pista (só Studio): anuncia os
  comentarios da pista se os hai.
* Alt+NVDA+0 dende a ventá do Studio: Abre o diálogo de configuración do
  complemento.
* Alt+NVDA+P dende a ventá de Studio: Abre o diálogo de perfiles de
  transmisión de Studio.
* Alt+NVDA+- (guión) dende a ventá Studio: envía retroalimentación ao
  desenvolvedor do complemento usando o cliente predeterminado de correo.
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

* F9: conecta a un servidor de streaming.
* F10 (só o codificador SAM):: Desconecta dun servidor de streaming.
* Control+F9/Control+F10 (Só codificador SAM): Conecta ou desconecta todos
  os codificadores respectivamente.
* F11: Conmuta se NVDA cambiará á ventá do Studio para o codificador
  seleccionado se está conectado.
* Shift+F11: conmuta  se Studio reproducirá a primeira pista seleccionada
  cando o codificador estéa conectado a un servidor de streaming.
* Control+F11: Conmuta a monitorización de fondo do codificador
  seleccionado.
* F12: abre un diálogo para intropducir etiquetas persoalizadas o cadeas
  para o codificador selecionado.
* Control+F12: Abre un diálogo para seleccionar o codificador que
  eliminaches(para realiñar  as etiquetas de cadea e as opcións do
  codificador).
* Alt+NVDA+0: abre o diálogo de opcións do codificador para configurar
  opcións como etiqueta de cadea.

Ademáis, as ordes de revisión de columna están dispoñibles, incluindo:

* Control+NVDA+1: posición do codificador.
* Control+NVDA+2: etiqueta da cadea.
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
* C (Shift+C nas distribucións JAWS e Window-Eyes): Título para a pista
  actualmente en reprodución.
* C (distribucións JAWS e Window-Eyes): conmuta o explorador de cart (só
  visualizador de lista de reprodución).
* D (R na distribución JAWS): duración restante para a lista de reprodución
  (se se da unha mensaxe de erro, move ao visualizador de lista de
  reproducción e logo aílla esta orden).
* E (G na distribución Window-Eyes): Estado dos metadatos do streaming.
* Shift+1 ata Shift+4, Shift+0: estado para as URLs dos metadatos
  individuais do streaming (0 é para o codificador DSP).
* E (distribución Window-Eyes): tempo transcorrido para a pista actualmente
  en reprodución.
* F: atopar pista (só visualizador de lista de reprodución).
* H: Duración da música para o actual espazo de tempo.
* Shift+H: duración das pistas restantes para o slot horario.
* I (L nas distribucións JAWS ou Window-Eyes): conta de oíntes.
* K: móvese á pista marcada (só no visualizador de lista de reprodución).
* Control+K: pon a pista actual como a pista  marcada (só no visualizador de
  lista de reprodución).
* L (Shift+L nas distribucións JAWS e Window-Eyes): Liña auxiliar.
* M: Micrófono.
* N: Título para a seguinte pista programada.
* P: Estado da reproducción (reproducindo ou detido).
* Shift+P: Ton da pista actual.
* R (Shift+E nas distribucións JAWS e Windows-Eye): Grabar en ficheiro
  activado / desactivado.
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

* Preme P para reproducir a seguinte pista seleccionada.
* Preme U para pausar ou non pausar a reproducción.
* Preme S para deter a pista con desvanecimiento, ou para deter a pista
  instantáneamente, preme T.
* Preme M ou Shift+M para activar ou desactivar o micrófono,
  respectivamente, ou preme N to activar o micrófono sen fade.
* Preme A para permitir a automatización ou Shift+A para desactivala.
* Preme L para permitir a entrada de liña ou shift+L para desactivala.
* Preme R para escoitar o tempo restante para a pista actualmente en
  reprodución.
* Preme Shift+R para obter un informe sobre o progreso do escaneado da
  biblioteca.
* Preme C para permitir ao NVDA anunciar o nome e a duración da pista
  actualmente en reprodución.
* Preme Shift+C para permitir ao NVDA anunciar o nome e a duración da pista
  actualmente en reproducción se a hai.
* Preme E pàra oír que codificadores están conectados.
* Preme I para obter o reconto de oíntes.
* Preme Q para obter información de estado variada acerca do Studio
  incluindo se unha pista se está a reproducir, se o micrófono está aceso e
  outra.
* Preme as teclas de cart (F1, Control+1, por exemplo) para reproducir carts
  asignados dende calquer lado.
* Preme H para amosar un diálogo de axuda que liste as ordes dispoñibles.

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

## Versión 20.05

* Soporte inicial para o cliente Remote VT (Voice Track), incluíndo o editor
  de listas reprodución cos mesmos atallos que o editor de listas de
  reprodución de Creator.
* A orde para abrir os diálogos separados de opcións de alarma (Alt+NVDA+1,
  Alt+NVDA+2 e Alt+NVDA+4) combináronse en Alt+NVDA+1 e agora abriranse as
  opcións das alarmas na pantalla de opcións do complemento SPL onde se
  poden atopar a outro/intro de pista e as opcións de alarma do micrófono.
* No diálogo de disparadores, que se atopa no diálogo de perfiles de
  transmisión, eliminouse a interface de usuario asociada aos perfiles de
  transmisión baseado en tempo como os campos de día/momento/duración do
  cambio de perfil.
* Eliminouse a opción de conta atrás para cambio de perfil situada no
  diálogo de perfiles de transmisión.
* Xa que Window-Eyes xa non ten soporte Vispero dende 2017, a distribución
  de ordes de SPL para window-Eyes está obsoleta e eliminarase nunha versión
  futura do complemento. Amosarase unha advertencia ao arrancar urxindo aos
  usuarios para que a distribución de ordes do Asistente SPL a NVDA
  (predeterminado) ou JAWS.
* Ao utilizar lotes do explorador de columnas (ordes Control+NvDA+fila de
  números) ou ordes de navegación por columnas (ctrl+alt+inicio/fin/frecha
  esquerda/frecha dereita) en Creator e Remote VT, NVDA non anunciará datos
  de columna incorrectos despois de cambiar a posición de columna vía rato.
* En codificadores e Streamer, NVDA xa non parecerá non facer nada ou
  reproducirá tons de erro ao saír do NVDA mentres se enfoque en algo
  diferente da lista de codificadores sen mover o foco aos codificadores
  primeiro.

## Versión 20.04

* A característica de perfiles de transmisión baseados en tempo está
  descatalogada. Amosarase unha advertencia ao iniciar Studio por primeira
  vez despois de instalar o complemento 20.04 se definiches un ou máis
  perfiles de emisión baseados en tempo.
* A administración de perfiles de transmisión separouse do diálogo de
  opcións do complemento SPL ao seu propio diálogo. Podes acceder ó diálogo
  de perfiles de transmisión premendo Alt+NVDA+P dende a ventá de Studio.
* Debido a duplicación coas ordes Control+NVDA+fila de números para pistas
  en Studio, a orde do explorador de columnas dende o Asistente SPL (fila de
  números) eliminouse.
* Modificada a mensaxe de erro ao tentar abrir un diálogo de opcións do
  complemento Studio (como o diálogo de transmisión de metadatos) mentres
  outro diálogo de opcións (como o diálogo de alarma de fin de pista) está
  activo. A nova mensaxe de erro é a mesma que ao tentar abrir múltiples
  diálogos de opcións de NVDA.
* NVDA xa non reproducirá tons de erro nin aparentará non facer nada ao
  pulsar o botón Aceptar dende o diálogo de Explorador de Columnas tras
  configurar os lotes de columnas.
* Nos codificadores, agora podes gardar e restablecer os axustes do
  codificador (incluídas as etiquetas das emisións) premendo Control+NVDA+C
  ou Control+NVDA+R tres veces, respectivamente.

## Versión 20.03

* O Explorador de Columnas agora anunciará por defecto as primeiras dez
  columnas (as instalacións existentes continuarán utilizando os antigos
  lotes de columnas).
* A habilidade para anunciar o nome da pista en reprodución automaticamente
  dende lugares diferentes de Studio eliminouse. Esta característica,
  introducida no complemento 5.6 como un parche para Studio 5.1x, xa non é
  funcional. Os usuarios agora deberán utilizar SPL Controller e/ou o
  comando en capa do Asistente SPL para escoitar o título da pista
  actualmente en reprodución desde calquera lugar (C).
* Debido á eliminación do anunciado automático do nome da pista en
  reprodución, a opción para configurar esta característica eliminouse das
  opcións do complemento/categoría anuncio de estado.
* Nos Codificadores, NVDA reproducirá o ton de conexión cada medio segundo
  mentres un codificador se estea conectando.
* Nos codificadores, agora NVDA anunciará as mensaxes de tentativas de
  conexión ata que o codificador estea realmente conectado. Anteriormente
  NVDA detíñase cando se atopaba un erro.
* Engadiuse un novo axuste ás opcións do codificador para que NVDA anuncie
  as mensaxes de conexión ata que o codificador seleccionado estea
  conectado. Esta opción está habilitada por defecto.

## Versión 20.02

* Soporte inicial para o Editor de Listas de Reprodución do StationPlaylist
  Creator.
* Engadidas as ordes Alt+NVDA+fila de números para anunciar varias
  informacións de estado no Editor de Listas de Reprodución. Inclúen data e
  hora para a lista (1), duración total da lista (2), cando a pista
  seleccionada está programado para reproducirse (3), e rotación e categoría
  (4).
* Ao enfocar unha pista en Creator e Track tool, agás no Editor de Listas de
  Reprodución de Creator, ao premer Control+NVDA+Guión amosará todas as
  columnas nunha ventá de modo exploración.
* Se NVDA recoñece un elemento da lista de pistas con menos de 10 columnas,
  NVDA xa non anunciará os encabezados de columnas que non existen se se
  preme Control+NVDA+fila de números para columnas fóra de rango.
* En Creator, NVDA xa non anunciará información de columna se se premen as
  teclas Control+NVDA+fila de números enfocando lugares diferentes da lista
  de pistas.
* Cando unha pista se está reproducindo, NVDA xa non anunciará "Sen pista en
  reprodución" ao abrir a información sobre a pista actual e seguinte a
  través de SPL Assistant ou SPL controller.
* Se está aberto un diálogo de opcións de alarma (intro, outro, micrófono),
  NVDA xa non parecerá non facer nada ou non reproducirá tons de erro ao
  tentar abrir unha segunda instancia de calquera diálogo de alarma.
* Ao tentar cambiar entre o perfil activo e un perfil instantáneo a través
  de SPL Assitant (F12), NVDA presentará unha mensaxe se se intenta facer
  cando a pantalla de opcións do complemento estea aberta.
* Nos codificadores, NVDA xa non esquecerá aplicar o axuste de sen ton de
  conexión para os codificadores ao reiniciarse NVDA.

## Versión 20.01

* Requírese NVDA 2019.3 ou posterior debido ao uso extensivo de Python 3.

## Versión 19.11.1/18.09.13-LTS

* Soporte inicial para o paquete StationPlaylist 5.40.
* En Studio, a de capturas de lista de reprodución (Asistente SPL, F8) e
  varias ordes de anunciado de hora como a de tempo restante (Control+Alt+T)
  xa non causarán que NVDA reproduza tons de erro ou non faga nada ao
  utilizar NVDA 2019.3 ou posterior.
* Nos elementos da lista de pistas de Creator, xa se recoñece correctamente
  a columna "Idioma" engadida en Creator 5.31 e posterior.
* En varias listas en Creator aparte da lista de pistas, NVDA xa non
  anunciará información de columna aleatoria se se preme a orde
  Control+NVDA+fila de números.

## Versión 19.11

* O comando Estado de codificador dende o SPL controller (E) anunciará o
  estado de conexión para o codificador activo, establecido no canto de
  monitorizar os codificadores en segundo plano.
* 19.08: NVDA xa non parecerá non facer nada ou non reproducirá tons de erro
  ao arrincar mentres se enfoque unha ventá de codificador.

## Versión 19.10/18.09.12-LTS

* Encurtado a mensaxe de anuncio de versión cando Studio se inicia.
* Anunciarase información de versión de Creator ao iniciar.
* 19.10: poden asignarse ordes persoalizadas para o estado do codificador
  dende o SPL Controller (E) de maneira que se poida usar dende calquera
  sitio.
* Soporte inicial para codificador altaCast (plugin de Winamp e debe ser
  recoñecido por Studio). Os comandos son os mesmos que os de SPL Encoder.

## Versión 19.08.1

* En codificadores SAM, NVDA xa non parecerá non facer nada nin reproducirá
  tons de erro se unha entrada de codificador se elimina mentres se está a
  monitorizar en segundo plano.

## Versión 19.08/18.09.11-LTS

* 19.08: Requírese NVDA 2019.1 ou posterior.
* 19.08: NVDA xa non parecerá non facer nada ou non reproducirá tons de erro
  ao reinicialo mentres o diálogo de opcións do complemento Studio estea
  aberto.
* NVDA lembrará axustes específicos de perfil ao cambiar entre paneles de
  opcións mesmo despois de renomear o perfil de transmisión actualmente
  seleccionado dende as opcións do complemento.
* NVDA xa non esquecerá respectar cambios en perfís basados en tempo cando
  se prema o botón Aceptar para pechar as opcións do complemento. Este bug
  estivo presente dende a migración a opcións multipáxina en 2018.

## Versión 19.07/18.09.10-LTS

* Complemento renomeado de "StationPlaylist Studio" a "StationPlaylist" para
  describir mellor as aplicacións e características soportadas por este
  complemento.
* Melloras de seguridade interna.
* Se os axustes de alarma de micrófono ou de transmisión de metadatos se
  cambian dende as opcións do complemento, NVDA xa non fallará aplicando os
  axustes modificados. Isto resolve un problema polo que a alarma de
  micrófono non comezaba ou se detía apropiadamente tras cambiar os axustes
  mediante as opcións do complemento.

## Versión 19.06/18.09.9-LTS

A versión 19.06 soporta SPL Studio 5.20 e posterior.

* Soporte inicial para StationPlaylist Streams.
* Cando se executen varias apps do Studio como Track tool ou Studio, se se
  inicia unha segunda instancia da app e logo se sae dela, NVDA xa non
  causará que as rutinas de configuración do complemento Studio produzan
  erros e deixen de traballar correctamente.
* Engadidas etiquetas para varias opcións no diálogo de configuración de SPL
  Encoder.

## Versión 19.04.1

* Arranxados problemas diversos cos paneis redeseñados de anuncios de
  columna e transcricións de listas de reprodución nas opcións do
  complemento, incluíndo cambios a orde persoalizada de columnas e a
  inclusión que non se reflectía ao gardar e/ou cambiar entre paneis.

## Versión 19.04/18.09.8-LTS

* Varios comandos globais como acceder a SPL Controller e saltar á xanela de
  Studio desactivaranse se NVDA se está a executar en modo seguro ou como
  aplicación da Windows Store.
* 19.04: nos paneis de anunciado de columnas e transcricións de listas de
  reprodución (opcións do complemento), os controis de inclusión/orde de
  columnas persoalizada estarán en primeiro plano en lugar de ter que
  seleccionar un botón para abrir un diálogo onde configurar estes axustes.
* En Creator, NVDA xa non reproducirá tons de erro nin aparentará non facer
  nada ao enfocar certas listaxes.

## Versión 19.03/18.09.7-LTS

* Ao priemer Control+NVDA+R para recargar as configuracións gardadas tamén
  se recargarán as opcións do complemento Studio, e ao premer este comando
  tres veces tamén se restablecerán as opcións do complemento Studio ás de
  fábrica xunto cos axustes do NVDA.
* Renomeado o diálogo do complemento Studio panel "Opcións avanzadas" a
  "Avanzado".
* 19.03 Experimental: nos paneis de anunciado de columnas e transcricións de
  listas de reprodución (opcións do complemento), os controis de
  inclusión/orde de columnas persoalizada estarán en primeiro plano en lugar
  de ter que seleccionar un botón para abrir un diálogo onde configurar
  estes axustes.

## Versión 19.02

* Eliminada a característica de verificación de actualizacións, incluído o
  comando de verificar actualizacións do Asistente SPL (Control+Shift+U) e
  as opcións de actualización do complemento das preferencias. A
  verificación de actualizacións para o complemento faise agora mediante
  Add-on Updater.
* NVDA xa non parecerá non facer nada ou non reproducirá un ton de erro
  cando o intervalo de micrófono activo estea configurado, utilizado para
  lembrar aos emisores que o micrófono está activo con pitidos periódicos.
* Ao restablecer os axustes do complemento dende o diálogo de preferencias
  do complemento/panel restablecer, NVDA preguntará unha vez máis en caso de
  que un perfil de cambio automático ou basado en tempo estea activo.
* Tras restablecer os axustes do complemento Studio, NvDA desactivará o
  temporizador de alarma de micrófono e anunciará o estado de emisión de
  metadatos, similar a cando se cambia de perfil de transmisión.

## Versión 19.01.1

* NVDA xa non anunciará "Monitorizando escaneado de biblioteca" tras pechar
  Studio nalgunhas situacións.

## Versión 19.01/18.09.6-LTS

* Requírese do NVDA 2018.4 ou posterior.
* Máis trocos internos para facer o complemento compatible con Python 3.
* 19.01: algunhas traducións de mensaxes deste complemento asemellaranse a
  mensaxes do NVDA.
* 19.01: a característica de verificación de actualizacións deste
  complemento xa non existe. Presentarase unha mensaxe de erro ao tentar
  utilizar asistente SPL, Control+Shift+U para verificar
  actualizacións. Para actualizacións futuras, por favor usa o complemento
  Add-on Updater.
* Lixeiras melloras de rendemento ao usar aplicacións diferentes de Studio
  mentres a Grabación de Pista de Voz está activada. NVDA aínda continuará a
  amosar fallos de rendemento cando se use o propio Studio coa Grabación de
  Pista de Voz activa.
* En codificadores, se un diálogo de axustes de codificador está aberto
  (Alt+NVDA+0), NVDA presentará unha mensaxe de erro ao tentar abrir outro
  diálogo de axustes de codificador.

## Versión 18.12

* Trocos internos para facer o complemento máis compatible con versións
  futuras de NVDA.
* Arranxadas varias instancias de mensaxes do complemento faladas en inglés
  aínda que estivesen traducidas noutros idiomas.
* Ao utilizar o Asistente SPL para verificar actualizacións do complemento
  (Asistente SPL; Control+Shift+U), NVDA non instalará versións novas do
  complemento se requiren unha versión máis actualizada do NVDA.
* Algúns comandos do Asistente SPL requerirán agora que o visualizador de
  lista de reprodución estea visible e enchido cunha lista de reprodución, e
  nalgúns casos que unha pista estea enfocada. Os comandos afectados inclúen
  duración restante (D), capturas de lista de reprodución (F8), e
  transcricións de lista de reprodución (Shift+F8).
* O comando de duración restante da lista de reprodución (asistente SPL, D)
  requerirá agora que se enfoque unha pista no visualizador de listas de
  reprodución.
* Agora, en codificadores SAM, podes utilizar comandos de navegación por
  táboas (Control+Alt+teclas de frecha) para consultar certa información de
  estado do codificador.

## Versión 18.11/18.09.5-LTS

Nota: a 18.11.1 remplaza á 18.11 co fin de fornecer mellor soporte do studio
5.31.

* Soporte inicial para StationPlaylist Studio 5.31.
* Agora pódense obter capturas de lista de reprodución (Asistente SPL, F8) e
  transcricións (Asistente SPL, Shift+F8) mentres se carga unha lista de
  reproducción pero a primeira pista non se enfoca.
* NVDA xa non parecerá non facer nada ou non reproducirá un ton de erro ao
  anunciar o estado de transmisión de metadatos ao arrancar Studio se se
  configurou para facelo.
* Se NVDA está configurado para anunciar o estado de emisión de metadatos
  cando Studio se inicia, o anuncio do estado de transmisión de metadatos xa
  non curtará o anuncio de cambios na barra de estado e viceversa.

## Versión 18.10.2/18.09.4-LTS

* Solucionada a imposibilidade de pechar a pantalla de axustes do
  complemento se ao premerse o botón Aplicar e a continuación Aceptar ou
  Cancelar.

## Versión 18.10.1/18.09.3-LTS

* Resoltos certos erros na característica de anunciado da conexión do
  codificador, incluíndo a ausencia do anunciado de mensaxes de estado, os
  fallos ao reproducir a primeira pista ou non saltar a Studio ao
  conectarse. Estes erros son a causa de WxPython 4 (NVDA 2018.3 ou
  posterior).

## Versión 18.10

* Requírese do NVDA 2018.3 ou posterior.
* Trocos internos para facer o complemento máis compatible con Python 3.

## Versión 18.09.1-LTS

* Ao obter transcricións de listas de reprodución no formato táboa HTML, as
  cabeceiras de columna xa non se presentan coma unha cadea de lista Python.

## Versión 18.09-LTS

A versión 18.09.x e a última serie de publicacións en soportar Studio 5.10 e
basados en tecnoloxías vellas, soportando a versión 18.10 Studio 5.11/5.20 e
novas características. Algunhas características retroportaranse á 18.09.x de
ser necesario.

* Recoméndase NVDA 2018.3 ou superior debido á introdución de wxPython 4.
* A pantalla de axustes do complemento está agora completamente baseada na
  interface multipáxina derivada do NVDA 2018.2 e posteriores.
* Combináronse os aneis de probas Drive Fast e Slow no canal
  "desenvolvemento", coa opción para os usuarios de publicacións de
  desenvolvemento de probar características piloto verificando a nova caixa
  características piloto no panel de axustes avanzados do complemento.
* Eliminouse a característica de escoller un canal de actualización do
  complemento diferente. Os usuarios que desexen cambiar a outro canal de
  publicación deben visitar o sitio web de complementos da comunidade do
  NVDA (addons.nvda-project.org), seleccionar StationPlaylist Studio e
  descargar logo a versión axeitada.
* Convertéronse a controis de listas de verificación as caixas de
  verificación de inclusión de columnas para anunciado de columnas e
  transcricións de listaxes de reprodución, así como as caixas de
  verificación de transmisións de metadatos.
* Ao saltar entre paneis de axustes, NVDA lembrará as preferencias actuais
  de axustes específicos do perfil (alarmas, anuncios de columnas, axustes
  da retransmisión de metadatos).
* Engadido o formato CSV (valores separados por comas) aos formatos de
  transcricións de listas de reprodución.
* Ao pulsar Control+NVDA+C para gardar a configuración agora gardaranse
  tamén os axustes do complemento Studio (require NVDA 2018.3).

## Versións vellas

Por favor consulta a liga changelog para notas da versión para versións
vellas do complemento.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
