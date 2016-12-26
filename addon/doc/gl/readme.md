# StationPlaylist Studio #

* Autores: Geoff Shang, Joseph Lee e outros colaboradores
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]
* Descargar [long-term support version][3] - complemento 15.x para usuarios
  do Studio 5.0x

Este paquete de complementos proporciona unhha utilización mellorada do
Station Playlist Studio, así como utilidades para controlar o Studio dende
calquera lugar.

Para máis información acerca do complemento, le a [guía do
complemento][4]. Para os desenvolvedores que queran saber cómo compilar o
complemento, consulta buildInstructions.txt localizado na raíz do
repositorio do código fonte.

IMPORTANTE: este complemento require do NVDA 2015.3 ou posterior e
StationPlaylist Studio 5.00 ou posterior. Se instalaches NVDA 2016.1 ou
posterior en Windows 8 e posterior, deshabilita o modo atenuación de
audio. Tamén, o complemento 8.0/16.10 require do Studio 5.10 e posterior, e
para emisores que usen o Studio 5.0x, está disponible unha versión long-term
support (15.x).

## Teclas de atallo

* Alt+Shift+T dende a ventá do Studio: anuncia o tempo transcorrido para a
  pista actual en reproducción.
* Control+Alt+T (deslizamento con dous dedos cara abaixo no modo tactil SPL)
  dende a ventá do Studio: anuncia o tempo restante para a pista que se
  estea a reproducir.
* NVDA+Shift+F12 (deslizamento con dous dedos cara arriba no modo tactil
  SPL) dende a ventá Studio: anuncia o tempo de emisión como 5 minutos para
  o comezo da hora.
* Alt+NVDA+1 (deslizamento con dous dedos cara a dereita no modo tactil SPL)
  dende a ventá do Studio: Abre o diálogo de opcións do remate da pista.
* Alt+NVDA+2 (deslizamento con dous dedos cara a esquerda no modo tactil
  SPL) dende a ventá do Studio: Abre o diálogo de configuración da alarma de
  intro da canción.
* Alt+NVDA+3 dende a ventá Studio:  conmuta o explorador de cart para
  deprender  as asignacións das cart. 
* Alt+NVDA+4 dende a ventá do Studio: Abre o diálogo de alarma do micrófono.
* Control+NVDA+f dende a ventá do Studio: Abre un diálogo para procurar unha
  pista baseada no artista ou no nome da canción. Preme NVDA+F3 para
  procurar cara adiante ou NVDA+Shift+F3 para procurar cara atrás.
* Alt+NVDA+R dende a ventá do Studio: Pasos para as opcións de anunciado do
  escaneado da biblioteca.
* Control+Shift+X dende a ventá do Studio: Pasos para as opcións do
  temporizador braille.
* Control+Alt+frechas dereita e esquerda (mentres se enfoca nunha pista):
  anuncia a columna da pista seguinte ou anterior.
* Control+NVDA+1 ata 0 (6 para Studio 5.0x): anuncia contidos de columna
  para una columna especificada.
* Alt+NVDA+C mentres se enfoca unha pista: anuncia os comentarios da pista
  se os hai.
* Alt+NVDA+0 dende a ventá do Studio: Abre o diálogo de configuración do
  complemento.
* Control+NVDA+- (guión) dende a ventá Studio: envía retroalimentación ao
  desenvolvedor do complemento usando o cliente predeterminado de correo.
* Alt+NVDA+F1: abre o diálogo de benvida.

## Ordes non asignadas

As seguintes ordes non son asignadas por defecto; se desexas asignalas, usa
o diálogo Xestos de Entrada para engadir ordes persoalizadas.

* Cambia á ventá SPL Studio dende calquera programa.
* Capa SPL Controller.
* capa SPL Assistant desde SPL Studio.
* Anunciar tempo incluíndo segundos dende o SPL Studio.
* Ó se activar ou desactivar o dial de pista (funciona apropiadamente
  mentras unha pista estea enfocada; para assignar unha orde a esta, móvete
  cara unha pista no Studio, logo abre o diálogo de entrada de xestos do
  NVDA.).
* Anunciar temperatura.
* Anunciar o título da seguinte pista se se programou.
* Anunciando título da pista actualmente en reprodución.
* Marcar pista actual para comezo da análise de tempo da pista.
* Realizar análise de tempo da pista.
* Atopar texto en columnas específicas.
* Atopar pistas ca duración que caia dentro dun rango dado a través do
  buscador de rango de tempo.
* Habilitar ou deshabilitar cíclicamente metadatos do streaming.

## Ordes adicionais cando se utilizan os codificadores Sam ou SPL

As seguintes ordes están dispoñibles cando se utilizan os codificadores Sam
ou SPL:

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
* Control+NVDA+3 dende o codificador SPL: opcións do codificador.
* Control+NVDA+4 dende o codificador SAM: estado da conexión do codificador.
* Control+NVDA+4 dende o codificador SPL: velocidade de transferencia ou
  estado da conexión.
* Control+NVDA+5 dende o codificador SAM: descripción do estado da conexión.

## SPL Assistant layer

Este conxunto de capas de ordes permíteche to obter varios estados no SPL
Studio, coma se unha pista se reproduce, duración total de todas as pistas
para a hora e outros. Dende calquera ventá do SPL Studio, preme a orde da
capa SPL Assistant, logo preme una das teclas da lista de abaixo (una ou
máis ordes son exclusivamente para o visualizador de lita de
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
* Control+Shift+U: procurar actualizacións do complemento.
* W: Clima e temperatura se se configurou.
* Y: Estado da lista de reprodución modificada.
* 1 ata 0 (6 para Studio 5.0x): anuncia contidos de columna para una columna
  especificada.
* F9: marca a pista actual para a análise de tempo da pista (só no
  visualizador de lista de reprodución).
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
* Preme E pàra obter contas e etiquetas de codificadores a ser
  monitorizados.
* Preme I para obter o reconto de oíntes.
* Preme F1 para amosar un diálogo de axuda que liste as ordes dispoñibles.

## Alarmas de pista

Por omisión, NvDA reproducirá un pitido se quedan cinco segundos á esquerda
na pista (outro) e/ou intro. Para configurar este valor así como para
habilitalos ou deshabilitalos, preme Alt+NVDA+1 ou Alt+NVDA+2 para abrir os
diálogos remate da pista e rampa de canción, respectivamente. Ademáis, usa o
diálogo opcións do complemento Studio para configurar se escoitarás un
pitido, unha mensaxe ou ambos cando as alarmas estean acesas.

## Alarma do micrófono

Podes preguntar ó NVDA para reproducir unha canción cando o micrófono sexa
activado por un tempo. Preme Alt+NVDA+4 para configurar o tempo da alarma en
segundos (0 deshabilítao).

## Track Finder

Se desexas atopar rapidamente unha canción dun artista ou polo nome da
canción, dende a lista de pistas, preme Control+NVDA+F. Teclea o nome do
artista ou o nome da canción. NVDA ponte na canción, de ser atopado ou amosa
un erro se non pode atopar a música que estás a buscar. Para atopar unha
canción ou artista previamente buscados, preme NVDA+F3 ou NVDA+Shift+F3 para
atopar cara adiante ou cara atrás.

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

## Dial de Pista

Podes utilizar as frechas para revisar varias informacións sobre unha
pista. Para activar o Dial de pista, mentres unha pista estea enfocada no
visor de lista principal, preme a orde asignada para cambiar o Dial de
pista. A continuación, utiliza as teclas de frecha dereita e esquerda para
revisar a información, como artista, duración e demáis. Alternativamente,
preme Control+Alt+frechas esquerda ou dereita para navegar entre columnas
sen invocar ao Dial de pistas.

## Análise de tempo de pista

Para obter a lonxitude para reproducir as pistas selecionadas, marca a pista
actual para comezo da análise de tempo da pista (SPL Assistant, F9), logo
preme SPL Assistant, F10 ó chegares ó remate da seleción.

## Explorador de Columnas

Premendo Control+NVDA+1 ata 0 (6 para Studio 5.0x) ou SPL Assistant, 1 ata 0
(6 para Studio 5.01 e anteriores), podes obter contidos das columnas
especificadas. Por omisión, estas son  artista, título, duración, intro,
categoría e nome de ficheiro (Studio 5.10 engade ano, álbum, xénero e tempo
programado). Podes configurar que columnas se explorarán a través do diálogo
explorador de columnas atopado no diálogo opcións do complemento.

## Diálogo Configuración

Dende a ventá do studio, podes premer Alt+NVDA+0 para abrir o diálogo de
configuración do complemento. Alternativamente, vai ó menú Preferencias do
NVDA e seleciona o elemento Opcions do SPL Studio. Este diálogo tamén se usa
para administrar perfís de emisión.

## Modo Táctil do SPL

Se estás a usar o Studio nunha computadora con pantalla tactil executando
Windows 8 ou posterior e tes NVDA 2012.3 ou posterior instalado, podes
realizar algunhas ordes do Studio dende a pantalla tactil. Primeiro usa un
toque con tgres dedos para cambiar a modo SPL, logo usa as ordes tactiles
listadas arriba para realizar ordes.

## Version 16.12.1

* Corrected user interface presentation for SPL add-on settings dialog.
* Traducións actualizadas.

## Versión 16.12/15.4-LTS

* Máis traballo no soporte do Studio 5.20, incluindo o anunciado do estado
  do modo insertar de cart (se está aceso) dende SPL Assistant layer (T).
* Conmutar o modo editar/insertar xa non está afectado pola verbosidade das
  mensaxes nin as opción de anunciado de tipo de estado (este estado
  anunciarase sempre a través de voz e/ou braille).
* Xa non é posible engadir comentarios ás notas partidas.
* Soporte para Track Tool 5.20, incluindo corrección dun problema where onde
  se anunciaba información errónea ao se usar ordes ddo Explorador de
  Columnas para anunciar información da columna.

## Versión 16.11/15.3-LTS

* Soporte inicial para StationPlaylist Studio 5.20, incluindo melloras de
  sensibilidade ao se opter información de estado coma estado de
  automatización a través do SPL Assistant layer.
* Correxidos fallos relativos á procura para pistas e interactuación con
  eles, incluindo a incapacidade para marcar ou desmarcar marcadores de
  pista ou unha pista atopada a través do diálogo atopar rango de tempo.
* A orde de anunciado de columnas xa non se reverterá á orde por defecto
  despois de cambiala.
* 16.11: Se o perfil transmisión ten erros, o diálogo erro xa non fallará ao
  despregarse.

## Versión 16.10.1/15.2-LTS

* Agora podes interactuar coa pista que se atopou a través Do Buscador de
  Pistas (Control+NVDA+F) según a procuras para reproducir.
* Traducións actualizadas.

## Versión 8.0/16.10/15.0-LTS

Versión 8.0 (tamén coñecida coma 16.10) soporta SPL Studio 5.10 e
posteriores, con 15.0-LTS (anteriormente 7.x) deseñado para proporcionar
algunas características novas dende 8.0 para usuarios que usen versión
anteriores do Studio. Ao menos que se sinale doutro xeito, as entradas máis
abaixo aplícanse a ambas versión 8.0 e 7.x. Amosarase un diálogo de aviso a
primeira vez que uses o complemento 8.0 co Studio 5.0x instalado,
preguntándoche se usas a versión 15.x LTS.

* O esquema da versión cambiou para reflectir o ano.mes da versión en lugar
  de maior.menor. Durante o período de transición (ata mitade  do 2017),
  versión 8.0 é sinónimo de versión 16.10, co 7.x LTS sendo designado coma
  15.0 debido a cambios incompatibles.
* O códigop fonte do complemento agora está hospedado en GitHub (repositorio
  localizado en https://github.com/josephsl/stationPlaylist).
* Engadido un diálogo de benvida que se lanza cando o Studio arranca despois
  de instalar o complemento. Engadiuse una orde (Alt+NVDA+F1) para reabrir
  este diálogo una vez pechado.
* Cambios para varias ordes do complemento, incluindo o borrado do conmutado
  do anunciado de estado (Control+NVDA+1), reasignada alarma de final da
  pista a Alt+NVDA+1, conmutar Esplorador de Cart agora é Alt+NVDA+3, o
  diálogo de alarma de micrófono é Alt+NVDA+4 e o diálogo das preferencias
  do complemento/codificador é Alt+NVDA+0. Esto fíxose para permitir que
  Control+NVDA+fila de números sexa asignada ao Explorador de Columnas.
* 8.0: Relaxouse a restrición do Explorador de Columnas en lugar en 7.x así
  os números 1 ata 6 poden configurarse para anunciar columnas no Studio
  5.1x.
* 8.0: a orde conmutar Dial de Pista e the a opción correspondente nas
  opción do complemento están en desuso e eliminaranse na 9.0. Esta orde
  permanecerá disponible no complemento 7.x.
* Engadida Control+Alt+Inicio/Fin para mover o navegador de Columnas á
  primeira ou á última columna no Visualizador de Lista de Reprodución.
* Agora podes engadir, ver, cambiar ou borrar comentarios de pista
  (notas). Preme Alt+NVDA+C dende unha pista no Visualizador de lista de
  Reprodución para escoitar comentarios de pista se se definiron, preme dúas
  veces para copiar o comentario ao portapapeis ou tres veces para abrir un
  diálogo para editar comentarios.
* Engadida a capacidade para notificar se existe un comentario de pista, así
  como una opción nas opción do complemento para controlar cómo se debería
  facer esto.
* Engadido un axuste no diálogo opción do complemento para permitir ao NVDA
  notificarche se acadaches a parte superior ou a inferior do visualizador
  de lista de reprodución.
* Ao reiniciar as opcións do complemento, agora podes especificar qué se
  reinicia. Por omisión, reiniciaranse as opción do complemento, cas caixas
  de verificación para reiniciar o perfil de cambio instantáneo, perfil
  baseado no tempo, opción do codificador e borrado dos comentarios de pista
  engadidos ao diálogo reiniciar opcións.
* Na Ferramenta de Pista, podes obter información do álbum e código do CD
  premendo Control+NVDA+9 e Control+NVDA+0, respectivamente.
* Mellórase o rendemento ao obter información da columna para a primeira vez
  na Ferramenta de Pista.
* 8.0: engadido un diálogo nas opcións do complemento para configurar os
  slots no Explorador de Columnas para a Ferramenta de Pista.
* Agora podes configurar o intervalo da alarma do micrófono dende o diálogo
  Alarma do micrófono (Alt+NvDA+4).

## Versión 7.5/16.09

* NVDA xa non despregará o diálogo de progreso da actualización se a canle
  de actualización do complemento cambiou.
* NVDA respectará a canle de actualización selecionada cando se descarguen
  actualizacións.
* Traducións actualizadas.

## Versión 7.4/16.08

A versión 7.4 tamén se coñece coma 16.08 seguido do ano.mes número da
versión para versións estables.

* É posible selecionar a canle de actualización do complemento dende
  opcións/opción avanzadas do complemento, para se borrar máis tarde na
  2017. Para a 7.4, as canles disponibles son beta, stable e long-term.
* Engadida unha opción nas opción do complemento/Opcións avanzadas para
  configurar o intervalo da procura da actualización entre 1 e 30 días (o
  predeterminado é 7 ou procuras semanais).
* A orde SPL Controller e a orde enfocar ao Studio non estará disponible
  dende pantallas seguras.
* Novas traduccións e actualizacións e engadida a localización da
  documentación en varias linguas.

## Cambios para 7.3

* Lixeiras melloras de rendemento ao procurar información como a
  automatización a través dalgunhas ordes do SPL Assistant.
* Traducións actualizadas.

## Cambios para 7.2

* Debido ao borrado do vello estilo do formato interno da configuración, é
  obrigatorio instalar o complemento 7.2. Unha vez instalado, non podes
  voltar a una versión anterior do complemento.
* Engadida unha orde no SPL Controller para informar do reconto de oíntes
  (I).
* Agora podes abrir os diálogos opción do complemento e opción do
  codificador premendo Alt+NVDA+0. Aínda podes usar Control+NVDA+0 para
  abrir estes diálogos (será eliminado no complemento 8.0).
* Na Ferramenta Pista, podes usar Control+Alt+Frechas esquerda ou dereita
  para navegar entre columnas.
* Agora anúncianse varios contidos en diálogos do Studio coma o diálogo
  Acerca en Studio 5.1x.
* Nos Codificadores SPL, NVDA silenciará o ton de conexión se auto-conectar
  está habilitado e logo apágase dende o menú de contexto do codificador
  mentres o codificador seleccionado se está a conectar.
* Traducións actualizadas.

## Cambios para 7.1

* Correxidos erros atopados ao actualizar dende o complemento 5.5 e
  anteriores ao 7.0.
* Ao respostar "non" cando se reinicia as opción do complemento, voltarás ao
  diálogo de opción do complemento e NVDA lembrará a opción perfil de cambio
  instantáneo.
* NVDA preguntarache para refonfigurar as etiquetas de cadea e outras opción
  de codificador se o ficheiro de configuración do codificador chega a
  coromperse.

## Cambios para 7.0

* Engadida a característica buscar actualización do complemento. Esto pode
  facerse manualmente (SPL Assistant, Control+Shift+U) ou automáticamente
  (configurable a través do diálogo Opcións avanzadas dende as opción do
  complemento).
* Xa non se require estar na ventá do visualizador de lista de reproducción
  para invocar a mayoría das ordes do SPL Assistant ou obter anunciados de
  tempo como tempo restante para a pista e tempo de retransmisión.
* Cambios para ordes do SPL Assistant, incluíndo a duración da lista de
  reprodución (D), reasignación da selección da duración da hora dende
  Shift+H a Shift+S e Shift+H agora utilízase para anunciar a duración das
  pistas restantes para o actual slot horario, reasignada a orden de estado
  dos metadatos do streaming (1 ata 4, 0 agora é Shift+1 ata Shift+4,
  Shift+0).
* Agora é posible invocar o buscador de pistas a través de SPL Assistant
  (F).
* SPL Assistant, números 1 ata 0 (6 para Studio 5.01 e anteriores) poden
  utilizarse para anunciar información da columna especificada. Estes slots
  de columna poden cambiarse no elemento Explorador de Columnas No diálogo
  opcións do complemento.
* Correxidos varios erros informados polos usuarios ao instalar o
  complemento 7.0 por primeira vez cando non estaba instalada una versión
  anterior deste complemento.
* Melloras para o Dial de Pista, incluindo a mellora da resposta ao se mover
  entre columnas e o seguemento de cómo as columnas se presentan na
  pantalla.
* Engadida a capacidade para premer Control+Alt+teclas de frecha esquerda ou
  dereita para moverse entre columnas de pista.
* Agora é posible usar unha distribución de ordes dun lector de pantalla
  diferente para as ordes do SPL Assistant. Vaite ao diálogo opción
  avanzadas das opcións do complemento para configurar esta opción entre as
  distribucións de NVDA, JAWS e Window-Eyes. Consulta as ordes do SPL
  Assistant máis abaixo para detalles.
* NVDA pode configurarse para cambiar a un perfil de retransmisión
  específico nun día e hora especificados. Usa o novo diálogo disparadores
  nas opcións do complemento para configurar esto.
* NVDA anunciará o nome do perfil unha vez que cambie a través de cambio
  instantáneo (SPL Assistant, F12) ou como o resultado do perfil baseado en
  tempo que quede activo.
* Movido o conmutado de cambio instantáneo (agora unha Caixa de
  verificación) cara o novo diálogo disparadores.
* As entradas na Caixa combinada perfís no diálogo opción do complemento
  agora amosa bandeiras de perfil como activo, se é un perfil de cambio
  instantáneo e outros.
* Se se atopa un problema serio ca lectura dos ficheiros do perfil de
  retransmisión, NVDA presentará un diálogo de erro e reiniciará as opción
  ás predeterminadas en lugar de non facer nada ou de reproducir un ton de
  erro.
* As opcións gardaranse no disco se e só se cambias opcións. Esto alonga a
  vida dos SSDs (disdos de estado sólido) para previr gardados innecesarios
  no disco se non cambiaron as opcións.
* No diálogo de opcións do complemento, os controis usados para conmutar o
  anunciado do tempo programado, conta de oíntes, nome do cart e nome da
  pista movéronse a un diálogo estado dedicado de anunciado (seleciona o
  botón estado do anunciado para abrir este diálogo).
* Engadida una nova opción no diálogo opción do complemento para permitir ao
  NVDA reproducir pitidos para diferentes categorías cando te movas entre
  pistas no visualizador de lista de reprodución.
* Téntase abrir a configuración da opción metadatos  no diálogo de opción do
  complemento mentres o diálogo rápido de metadatos do streaming está aberto
  xa non causará que NVDA non faga nada ou que reproduza un ton de
  erro. NvDA agora preguntarache para pechar o diálogo dos metadatos do
  streaming antes de que podas abrir as opcións do complemento.
* Ao anunciar tempo como o tempo restante para a pista en reprodución, as
  horas tamén se anuncian. Consecuentemente, a opción anunciado da hora está
  habilitado por omisión.
* Premendo SPL Controller, R agora causas que NVDA anuncie o tempo restante
  en horas, minutos e segundos (minutos e segundos se este é o caso).
* Nos codificadores, o premer Control+NVDA+0 presentará o diálogo opción do
  codificador para configurar varias opcións como etiqueta da cadea, enfocar
  ao Studio cando se conecte e outras.
* Nos codificadores, agora é posible apagar os tons do progreso da conexión
  (configurable dende o diálogo opción do codificador).

## Cambios para 6.4

* Correxiuse un problema importante cando se volta dende un perfil de cambio
  instantáneo e o perfil de cambio instantáneo actívase de novo, visto
  despois de eliminar un perfil que se colocou xusto antes do perfil activo
  anteriormente. Ao tentar eliminar un perfil, amosarase un diálogo de aviso
  se está activo un perfil de cambio instantáneo.

## Cambios para 6.3

* Melloras de seguridade interna.
* Cando o complemento 6.3 ou posterior se lanza primeiro nunha computadora
  executando Windows 8 ou posterior con NVDA 2016.1 ou posterior instalado,
  amosarase un diálogo de alerta pedíndoche deshabilitar o modo de
  atenuación de audio (NVDA+Shift+D). Seleciona a caixa de verificación para
  pechar este diálogo no futuro.
* Engadida unha orde para enviar informes de fallos, suxerencias de
  características e outra retroalimentación ao desenvolvedor do complemento
  (Control+NVDA+- (guión, "-")).
* Traducións actualizadas.

## Cambios para 6.2

* Correxido un erro ca orde restante da lista de reprodución (SPL Assistant,
  D (R se o modo de compatibilidade está aceso)) onde a duración ou a hora
  actual foi anunciada coma oposta a lista de reprodución enteira (O
  comportamento desta orde pódese configurar dende as opcións avanzadas que
  se atopan no diálogo de opcións do complemento).
* NVDA agora pode anunciar o nome da pista actualmente en reprodución
  mentras se utiliza outro programa (configurable dende as opcións do
  complemento).
* A configuración usada para permitir á orde do SPL Controller invocar SPL
  Assistant agora aténdese (anteriormente habilitábase en todas as
  ocasións).
* Nos codificadores SAM, as ordes Control+F9 e Control+F10 agora funcionan
  correctamente.
* Nos codificadores, cando un codificador se enfoca primeiro e se este
  codificador se configura para seren monitorizado de fondo, NVDA agora
  comezará o monitorizado de fondo automáticamente.

## Cambios para 6.1

* Orden de anunciamento da columna e inclusión, así como as opcións de
  metadatos do streaming agora son opcións do perfil específico.
* Ó se cambiar os perfís, os metadatos corectos da cadea habilitaranse.
* Ó se abrir o diálogo opcións rápidas de metadatos do streaming (orden non
  asignada), as opcións cambiadas agora aplícanse ó perfil activo.
* Ó se arrancar Studio, cambiou cómo os erros se amosan se só o perfil
  corrupto é o perfil normal.
* Cando se cambian certas opcións usando atallos de teclado como
  anunciamentos de estado, correxiuse un fallo onde as opcións cambiadas non
  se retiñan ó se cambiar e dende un perfil de cambio instantáneo.
* Ó se usar unha orde SPL Assistant cun xexto personalizado predefinido (tal
  como a orde seguinte pista), xa non se require estar no visualizador de
  lista de reprodución do Studio para usar estas ordes (poden realizarse
  dende outras ventás do Studio).

## Cambios para 6.0

* Novas ordes SPL Assistant, incluindo o anunciado do título da pista
  actualmente en reprodución (C), o anunciado do estado dos metadatos do
  streaming (E, 1 ate 4 e 0) e apertura da guía do usuario en liña
  (Shift+F1).
* A capacidade para empaquetar as opcións favoritas como perfís de emisión
  para se usar durante un show e para cambiár a un perfilñ predefinido. Olla
  a guía do complemento para detalles sobre perfís de emisión.
* Engadida unha nova opción nas opciòns do complemento para controlar a
  verbosidade das mensaxes (algunhas mensaxes acurtaranse cando a
  verbosidade avanzada estea selecionada).
* Engadida unha nova opción nas opcións do complemento para permitir ó NVDA
  anunciar horas, minutos e segundos para as ordes de duración da pista ou
  da lista de reprodución (as características afectadas inclúen o anunciado
  de tempo transcorrido e restante para a pista actualmente en reprodución,
  análise de tempo da pista e oujtros).
* Agora podes pedir ó NVDA que anuncie a lonxitude total dun rango de pistas
  a través da característica análise de tempo da pista. Preme SPL Assistant,
  F9 para marcar a pista actual como o marcador de comezo, móvete ó remate
  do rango de pista e preme SPL Assistant, F10. estas ordes poden
  reasignarse así unha non invoca ó SPL Assistant layer para realizar a
  análise de tempo da pista.
* Engadido un diálogo procurar columna (orde non asignada) para atopar texto
  nas columnas especificadas como artista ou parte do nome de ficheiro.
* Engadido un diálogo atopar rango de tempo (orden non asignada) para atopar
  unha pista ca duración que caia dentro dun rango especificado, util se se
  desexa atopar unha pista a rechear unha hora slot.
* Engadida a capacidade para reordear o anunciamento de colujmnas de pista e
  para suprimir o anunciamento de columnas específicas se "usar orden de
  pantalla" está desmarcado dende o diálogo opcións do complemento. Usa o
  diálogo "administrar anunciado de columna" para reordear columnas.
* Engadido un diálogo (orde non asignada) para conmutar cíclicamente os
  metadatos do streaming.
* Engadida unha opción no diálogo de opcións do complemento para configurar
  cando o estado dos metadatos do streaming deberíase de anunciar e para
  habilitar metadatos do streaming.
* Engadida a capacidade de marcar unha pista como un marcador para voltar a
  el máis tarde (SPL Assistant, Control+K para poñer, SPL Assistant, K para
  moverse á pista marcada).
* Mellorado o desempeño cando se procura o texto na pista seguinte o ou
  anterior contendo o texto procurado.
* Engadida unha opción no diálogo opcións do complemento para configurar a
  alarma de notificación  (pitar, mensaxe ou ambos).
* Agora é posible configurar alarma de micrófono entre 0 (deshabilitada) e
  dúas horas (7200 segundos) e utilizar as teclas de frecha arriba e abaixo
  para configurar esta opción.
* Engadida unha opción no diálogo opcións do complemento para permitir no
  micrófono activo notificacións dadas piriódicamente.
* Agora podes usar a orde conmutar Dial da pista no Studio para conmutar
  Dial de Pista na Ferramenta de Pista proporcionada que non se asignóu unha
  orde para conmutar Dial de Pista na Ferramenta de Pista.
* Engadida a capacidade para usar a orde de capa do SPL Controller para
  chamar o SPL Assistant (configurable dende o diálogo opcións avanzadas
  atopado nas opcións do complemento).
* Engadida a capacidade para NVDA para usar certas ordes do SPL Assistant
  utilizadas por outros lectores de pantalla. Para configurar esto, vai ás
  opcións do complemento, seleciona Opcións Avanzadas e marca a caixa de
  verificación modo de compatibilidade de lectores de pantalla.
* Nos codificadores, opcións como enfocar Studio cando se estea conectado
  ahora lémbranse.
* Agora é posible ver varias columnas dende a ventá do codificador (como o
  estado da conexión do codificador) a través da orde Control+NVDA+número;
  consulta as ordes do codificador arriba.
* Correxido un fallo raro onde ó cambiar a Studio ou ó pechar un diálogo do
  NVDA (incluindo os diálogos do complemento Studio) impedía as ordes de
  pista (como conmutar Dial de pista) de traballar coma se esperabha.

## Cambios para 5.6

* En Studio 5.10 e posterior, NVDA xa non anuncia "non selecionado" cando a
  pista selecionada se estea a reproducir.
* Debido a un problema co Studio mesmo, NVDA agora anunciará o nome da pista
  actualmente en reprodución automáticamente. Foi engadida unha opción para
  conmutar este comportamento no diálogo de opcións do complemento studio.

## Cambios para 5.5

* A opción Reproducir despois de conectarse recordarase ó se mover a través
  da ventá do codificador.

## Cambios para 5.4

* Ó se realizar o escaneado da biblioteca dende o diálogo Insertar Pistas xa
  non se causa que NVDA non anuncie o escaneado de estado ou reproduza tons
  de erro se NVDA se configurou para anunciar o progreso do escaneado da
  biblioteca ou a conta de escaneado.
* Traducións actualizadas.

## Cambios para 5.3

* Agora está dispoñible a corrección para o Codificador SAM (non reproduce a
  seguinte pista se unha pista se está a reproducir e cando o codificador se
  conecta) para os usuarios do codificador SPL.
* NVDA xa non reproduce erros ou non fai nada cando SPL Assistant, F1
  (diálogo de axuda do Assistant) estea premedo.

## Cambios para 5.2

* NVDA xa non permitirá que se abran os diálogos opcións e alarma. Amosarase
  unha advertencia pedíndoche pechar antes o diálogo aberto con
  anterioridade.
* Cando se monitoriza un ou máis codificadores, premendo SPL Controller, E
  agora anunciará a conta de codificador, o identificador do codificador e a
  cadea de etiqueta(s) se as hai.
* NVDA soporta todas as ordes conectar/desconectar (Control+F9/Control+F10)
  en codificadores SAM.
* NVDA xa non reproducirá a seguinte pista se un codificador se conecta
  mentres Studio estea a reproducir unha pista e Studio dicía que se
  reproduzan pistas cando un codificador estéa conectado.
* Traducións actualizadas.

## Cambios para 5.1

* Agora é posible revisar columnas individuais na Ferramenta de Pista a
  través de Dial de Pista (tecla de conmutación non asignada). Ten en conta
  que Studio debe estar activo antes de usar este modo.
* Engadida unha caixa de verificación no diálogo de opcións do complemento
  do Studio para conmutar o anunciado do nome do cart actualmente en
  reprodución.
* Ó activar ou desactivar o micrófono a través do SPL Controller xa non
  causa que se reproduzan tons de erro ou que o son se conmute a non
  reproducir.
* Se unha orden persoalizada está asignada a unha orde de capa do SPL
  Assistant e esta orde se preme directamente despois de entrar no SPL
  Assistant, NVDA agora sairá rápìdamente do SPL Assistant.

## Cambios para 5.0

* Engadiuse un diálogo de opcións adicado para o complemento do SPL,
  accesible dende o menú Preferencias do NVDA ou premendo Control+NVDA+0
  dende a ventá do SPL.
* Engadida a capacidade para restablecer todas as opcións ás predeterminadas
  a través do diálogo de configuración.
* Se algunhas das opcións teñen erros, só as opcións afectadas se
  restablecerán ás predeterminadas de fábrica.
* Engadido un modo táctil SPL dedicado e ordes táctiles para realizar varias
  ordes do Studio.
* Os cambios para a capa SPL Assistant inclúe o engadido da orden capa de
  Axuda (F1) e a eliminación das ordes para conmutar a conta de oubintes
  (Shift+I) e o anunciamento do tempo programado (Shift+S). Podes configurar
  estas opcións no diálogo de opcións do complemento.
* Renomeado "Conmutar anunciado" por "Anunciado de estado" xa que os pitidos
  utilízanse para anunciar outra información de estado como o completado do
  escaneado de biblioteca.
* A opción de anunciado do estado agora retense a través das
  sesións. Anteriormente tiñas que configurar esta opción manualmente cando
  o Studio arrancaba.
* Agora podes usar a característica Dial de Pista para revisar columnas
  nunha entrada de pista no visualizador de lista de reprodución principal
  do Studio (para conmutar esta característica, preme a orde que asignaches
  para esta característica).
* Agora podes asignar ordes persoalizadas para escoitar a información de
  temperatura ou para anunciar o título para a seguinte pista se se
  programou.
* Engadida unha caixa de verificación nos diálogos fin de pista e
  introdución de canción para habilitar ou deshabilitar estas alarmas (marca
  para habilitar). Estas taméhn poden "configurarse" dende as opcións do
  complemento.
* Solucionouse un problema polo que ó premer ordes do diálogo alarma ou de
  Procurador de pistas track mentres outro diálogo de alarma ou de procura
  está aberto podía causar que aparecera outra instancia do mesmo
  diálogo. NVDA despregará unha mensaxe preguntándoche para pechar o diálogo
  anteriormente aberto primeirro.
* Cambios e correccións do explorador de Cart, incluindo a exploración
  incorecta de bancos de carts cando o usuario non está enfocando sobre o
  visualizador de lista de reprodución. O esplorador de Cart ahora
  verificará asegurarse de que estás no visualizador da lista de reprodución 
* Engadida a capacidade para usar a orde de capa do SPL Controller para
  chamar o SPL Assistant (experimental; consulta a guía do complemento sobre
  como habilitar esto).
* No codificador de windows, a orde de anunciado da hora e da data do NVDA
  (NVDA+F12 por omisión) anunciará a hora incluíndo segundos.
* Agora Podes monitorizar codificadores individuais para estado de conexión
  e para outras mensaxes premendo Control+F11 mentres o codificador que
  desexas monitorizar estea enfocado (funciona mellor cando se usan
  codificadores SAM).
* Engadida unha orde no SPL Controller para informar do estado  dos
  codificadores a seren monitorizados (E).
* Xa está dispoñible unha solución para correxir un fallo onde NVDA
  anunciaba etiquetas de cadea para os codificadores equivocados, sobor de
  todo despois de borrar un codificador (para realiñar as etiquetas de
  cadea, preme Control+F12, logo selecciona a posición do codificador que
  eliminaches).

## Cambios para 4.4/3.9

* A función Library scan agora funciona no Studio 5.10 (require a deradeira
  compilación do Studio 5.10).

## Cambios para 4.3/3.8

* Cando se cambia a outra parte do Studio como o diálogo insertar pistas
  mentres cart explorer está activo, NVDA xa non anunciará mesaxes do cart
  cando as teclas do cart se premen (por exemplo, localizar unha pista dende
  o diálogo insert tracks).
* Novas teclas do SPL Assistant, incluíndo o conmutado do anunciado da hora
  programada e reconto de ouvintes (Shift+S e Shift+I, respectivamente, non
  se gardan a través de sesións).
* Ó saír do Studio mentras se abren varios diálogos de alarma , NVDA
  detectará que se saíu do Studio e non gardará os valores de alarma recén
  modificados .
* Traducións actualizadas.

## Cambios para 4.2/3.7

* NVDA xa non esquecerá de reter as etiquetas novas e cambiadas do
  codificador cando un usuario peche a sesión ou reinicie o computador.
* Cando a configuración do complemento se corrompe ó se iniciar o NVDA, éste
  restaurará a configuración predeterminada e amosará unha mensaxe para
  informar ó usuario deste feito.
* No complemento 3.7, o problema co foco visto ó eliminar pistas no Studio
  4.33 correxiuse (a mesma corrección está dispoñible para os usuarios do
  Studio 5.0x no complemento 4.1).

## Cambios para 4.1

* No Studio 5.0x, eliminando unha pista dende o visualizador principal da
  lista de reprodución xa non causará que NVDA anuncie a pista de abaixo en
  lugar da nova enfocada (máis notable se a segunda a última pista fora
  eliminada, no caso que NVDA dixo "descoñecido").
* Corexidos varios problemas co escaneado da biblioteca en Studio 5.10,
  incluíndo o anunciado do número total de elementos na biblioteca mentras
  se tabula polo diálogo insert tracks e dicindo "O escaneado está en
  progreso" cando se tenta monitorizar os escaneados da biblioteca a través
  do SPL Assistant.
* Cando se utiliza unha pantalla braille co Studio 5.10 e se está marcada
  unha pista, premendo ESPAZO para marcar unha pista máis abaixo xa non
  causa que o braille non reflicta o novo estado marcado.

## Cambios para 4.0/3.6

A versión 4.0 soporta SPL Studio 5.00 e posteriores, con 3.x deseñado para
proporcionar algunhas características novas dende 4.0 para usuarios que
utilicen versións anteriores de Studio.

* Novas teclas para SPL Assistant, incluíndo tempo programado para a pista
  (S), duración restante para a lista de reprodución (D) e temperatura (W se
  se configurou). ademáis, para o Studio 5.x, engadiuse modificación de
  lista de reprodución (Y) e ton de pista (Shift+P).
* Novas ordes SPL Controller, incluíndo o progreso dos escaneados da
  biblioteca (Shift+R) e a habilitación do micrófono sen fade (N). Tamén,
  premendo F1 desprégase un diálogo amosando as ordes dispoñibles.
* Cando se habilita ou deshabilita o micrófono a través de SPL Controller,
  reproduciranse uns pitidos para indicar o estado activado/desactivado.
* Opcións como tempo de remate de pista gárdanse nun ficheiro de
  configuración dedicado no teu cartafol de configuración do usuario e
  presérvanse durante as actualizacións do complemento (versión 4.0 e
  posteriores).
* Engadida unha orde (Alt+NVDA+2) para fixar o tempo da alarma da intro da
  canción entre 1 e 9 segundos.
* Nos diálogos de alarma de intro e de remate de pista, podes utilizar
  flechas arriba e abaixo para cambiar as opcións de alarma. Se se introduce
  un valor erróneo, o valor da alarma fíxase ó máximo valor.
* Engadida unha orde (Control+NVDA+4) para fixar un tempo no que NVDA
  reproducirá unha canción cando o micrófono se activara por un intre.
* Engadida unha característica para anunciar o tempo en horas, minutos e
  segundos (orde non asignada).
* Agora é posible seguir os escaneados da biblioteca dende o diálogo Insert
  Tracks ou dende calquera sitio, unha orden dedicada (Alt+NVDA+R) para
  conmutar o anunciamento das opcións do escaneado da biblioteca.
* Soporte para Track Tool, incluíndo a reprodución dun pitido se se unha
  pista ten unha intro definida e ordes para anunciar información sobre unha
  pista como a duración e a posición na cola.
* Soporte para o codificador StationPlaylist (Studio 5.00 e posteiores),
  proporcionando o mesmo nível de soporte que o atopado no codificador SAM.
* Nas ventás do codificador, NVDA xa non reproduce tons de erro cando NVDA
  dixo de cambiar a Studio ó conectarse a un servidor de streaming mentras a
  ventá do Studio está minimizada.
* Os erros xa non se escoitan despois de eliminar un stream cunha etiqueta
  stream fixada neles.
* Agora é posible monitorizar a introdución e o remate da pista a través do
  braille utilizando as opcións do temporizador braille (Control+Shift+X).
* Correxido un problema onde se tenta cambiar á ventá do Studio dende
  calquera programa despois de que todas as ventás fosen minimizadas
  causando  que apareza otra cosa.
* ó utilizar Studio 5.01 e posteiores, NVDA xa non anunciará certa
  información de estado como o tempo programado múltiples veces.

## Cambios para 3.5

* Cando NVDA se inicie ou reinicie mentras a ventá principal da lista de
  reprodución do Studio 5.10 estea enfocada, NVDA xa non reproducirá tons de
  erro e/ou non anunciará a pista seguinte ou a anterior cando se navegue
  polas pistas.
* Correxido un problema cando se tenta obter o tempo restante e o tempo
  transcorrido para unah pista nas compilacións máis recentes do Studio
  5.10.
* Traducións actualizadas.

## Cambios para 3.4

* No explorador de cart, os carts involucrados ca tecla control (como
  Ctrl+F1) agora manéxanse correctamente.
* Traducións actualizadas.

## Cambios para 3.3

* Ó se conectar a un servidor de streaming utilizando o codificador SAM, xa
  non se necesita estar na ventá do codificador ate que a conexión se
  estableza.
* Correxido un problema onde as ordes do codificador (por exemplo, stream
  labeler) xa non funcionaría ó se cambiar á ventá do SAM dende  outros
  programas.

## Cambios para 3.2

* Engadida unha orde no SPL Controller para informar do tempo restante para
  a pista actualmente en reprodución (R).
* Na ventá do codificador SAM, correxiuse a mesaxe do modo axuda de entrada
  para Shift+F11
* No explorador de cart, se Studio Standard se está a usar, NVDA alertarache
  que un número de filas de ordes non están dispoñibles para asignacións de
  cart.
* No Studio 5.10, o buscador de pista xa non reproduce tons de erro ó buscar
  polas pistas.
* Traducións novas e actualizadas.

## Cambios para 3.1

* Na ventá do SAM Encoder, engadiuse unha orde (Shift+F11) para dicirlle ó
  Studio que reproduza a primeira pista cando estea conectado.
* Correxidos numerosos erros cando se conecta a un servidor no Encoder SAM ,
  incluíndo a incapacidade para levar a cabo as ordes do NVDA , NVDA non
  anuncia cando a conexión foi establecida e da tons de erro en lugar do
  pitido de conexión que se está a reproducir cando se conecta .

## Cambios para  3.0

* Engadido explorador de Cart para deprender as asignacións de cart (ate 96
  carts se poden asignar).
* Engadidas novas ordes, incluíndo tempo de emisora (NVDA+Shift+F12) e
  reconto de oubintes (i) e título da seguinte pista (n) no SPL Assistant.
* Conmutar mesaxes como automation agora amósase en braille
  independentemente da opción conmutar anunciado.
* Cando a ventá do StationPlaylist se minimiza á bandexa do sistema (área de
  notiricacións), NVDA anunciará este feito ó tratar de cambiar a SPL dende
  outros programas.
* Os tons de erro xa non se escoitan cando conmutar anunciado está posto en
  pitidos e as mesaxes de estado que non sexan on/off se anuncian (exemplo:
  reproducindo carts).
* Os tons de erro xa non se escoitan cando se tenta obter información como
  tempo restante mentres outra ventá do Studio que a lista de pistas (como o
  diálogo Opcións) estea enfocada. Se a información necesaria non se atopa,
  NVDA anunciará este feito.
* Agora é posible buscar unha pista polo nome do artista. Con anterioridade
  podías buscar polo título da pista.
* Soporte para o codificador SAM, incluíndo a capacidade para etiquetar o
  codificador e unha orden conmutar para cambiar a Studio cando o
  codificador seleccionado estea  conectado.
* A axuda do complemento está dispoñible dende o Administrador de
  complementos.

## Cambios para 2.1

* Correxido un fallo onde o usuario era incapaz de obter a información de
  estado como estado de automatización cando SPL 5.x foi lanzado antes de
  que NVDA estivera en execución.

## Cambios para 2.0

* Elimináronse Algunhas teclas de acceso globais e específicas da aplicación
  para que poidas asignar un comando personalizado a partir do diálogo
  Xestos de Entrada (a versión 2.0 do complemento require NVDA 2013.3 ou
  posterior).
* Engadidas máis ordes do asistente do SPL tales coma o estado do modo cart
  edit.
* Agora podes cambiar ó SPL Studio mesmo con todas as ventás minimizadas
  (pode non funcionar nalgúns casos).
* Extendido o rango da alarma de remate da pista a 59 segundos.
* Agora podes buscar unha pista dunha lista de reprodución (Control+NVDA+F
  para atopar, NVDA+F3 ou NVDA+Shift+F3 para atopar cara adiante ou cara
  atrás, respectivamente).
* anúncianse  nomes correctos das caixas de combinación polo NVDA(por
  exemplo Do diálogo Opcións e pantallas iniciais de configuración do SPL).
* Correxido un fallo onde NVDA anunciaba información incorrecta cando
  tentaba obter o tempo restante para unha pista no SPL Studio 5.

## Cambios para 1.2

* Cando o Station Playlist 4.x está instalado en certos computadores co
  Windows 8/8.1, é posible novamente escoitar os tempos transcorridos e
  restantes para unha pista.
* Traducións actualizadas.

## Cambios para 1.1

* Engade unha orde (Control+NvDA+2) para establecer unha alarma de remate da
  pista.
* Correxido un erro no que os nomes de campos para certos campos de edición
  non se anunciaban (particularmente campos de edición no diálogo de
  opcións).
* Engadidas varias traduccións.


## Cambios para 1.0

* Versión inicial.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=spl

[2]: http://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: http://spl.nvda-kr.org/files/get.php?file=spl-lts16

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide
