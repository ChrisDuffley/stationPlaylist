# StationPlaylist Studio #

* Autores: Geoff Shang, Joseph Lee e outros colaboradores
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]
* Descargar [versión de soporte estendido][3] - para usuarios do Studio
  5.10/5.11
* Compatibilidade con NVDA: da 2018.4 á 2019.1

Este paquete de complementos proporciona unhha utilización mellorada do
Station Playlist Studio, así como utilidades para controlar o Studio dende
calquera lugar.

Para máis información acerca do complemento, le a [guía do
complemento][4]. Para os desenvolvedores que queran saber cómo compilar o
complemento, consulta buildInstructions.txt localizado na raíz do
repositorio do código fonte.

NOTAS IMPORTANTES:

* Este complemento require do NVDA 2018.4 ou posterior e do StationPlaylist
  Studio 5.11 ou posterior.
* Se usas o Windows 8 ou posterior, para unha mellor experiencia,
  deshabilita o modo atenuación de audio.
* A partires de 2018, os [rexistros de cambios para versións vellas][5]
  atoparanse en GitHub. Este readme do complemento listará cambios dende a
  versión 7.0 (2016 en diante).
* Certas características do complemento (especialmente a actualización) non
  funcionarán baixo algunhas condicións, incluindo a execución do NVDA en
  modo seguro.
* Debido a limitacións técnicas, non podes instalar nin usar este
  complemento na versión de Windows Store do NVDA.
* A característica de actualización que vén con este complemento xa non
  existirá no 2019. Utiliza Add-on Updater para actualizar este complemento.

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
* Control+Alt+frechas dereita e esquerda (mentres se enfoca nunha pista no
  Studio, Creator ou TrackTool): anuncia a columna da pista seguinte ou
  anterior.
* Control+Alt+frecha abaixo/arriba (mentres se enfoque unha pista só en
  Studio): Moven á pista seguinte ou anterior e anuncian columnas
  específicas (non dispoñible no complemento 15.x).
* Control+NVDA+1 a 0 (cun track enfocado en Studio, Creator e Track Tool):
  Anunciar contido da columna para unha columna especificada. Premer este
  atallo dúas veces amosará a información de columna nunha xanela de modo
  exploración.
* Control+NVDA+- (guión, en Studio): Mostrar datos de todas as columnas
  dunha pista nunha xanela de modo exploración.
* Alt+NVDA+C mentres se enfoca unha pista (só Studio): anuncia os
  comentarios da pista se os hai.
* Alt+NVDA+0 dende a ventá do Studio: Abre o diálogo de configuración do
  complemento.
* Alt+NVDA+- (guión) dende a ventá Studio: envía retroalimentación ao
  desenvolvedor do complemento usando o cliente predeterminado de correo.
* Alt+NVDA+F1: abre o diálogo de benvida.

## Ordes non asignadas

As seguintes ordes non son asignadas por defecto; se desexas asignalas, usa
o diálogo Xestos de Entrada para engadir ordes persoalizadas.

* Cambia á ventá SPL Studio dende calquera programa.
* Capa SPL Controller.
* Anunciar o estado do Studio como a reproducción de pista dende outros
  programas.
* capa SPL Assistant desde SPL Studio.
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
* Control+Shift+U: procurar actualizacións do complemento (eliminarase en
  2019).
* W: Clima e temperatura se se configurou.
* Y: Estado da lista de reprodución modificada.
* 1 ata 0 (6 para Studio 5.0x): anuncia contidos de columna para una columna
  especificada.
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
* Preme E pàra obter contas e etiquetas de codificadores a ser
  monitorizados.
* Preme I para obter o reconto de oíntes.
* Preme Q para obter información de estado variada acerca do Studio
  incluindo se unha pista se está a reproducir, se o micrófono está aceso e
  outra.
* Preme as teclas de cart (F1, Control+1, por exemplo) para reproducir carts
  asignados dende calquer lado.
* Preme H para amosar un diálogo de axuda que liste as ordes dispoñibles.

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

Premendo Control+NVDA+1 ata 0 ou SPL Assistant, 1 ata 0, podes obter
contidos das columnas especificadas. Por omisión, estas son  artista,
título, duración, intro, categoría e nome de ficheiro, ano, álbume, xénero e
tempo programado). Podes configurar que columnas se explorarán a través do
diálogo explorador de columnas atopado no diálogo opcións do complemento.

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

## Modo Táctil do SPL

Se estás a usar o Studio nunha computadora con pantalla tactil executando
Windows 8 ou posterior e tes NVDA 2012.3 ou posterior instalado, podes
realizar algunhas ordes do Studio dende a pantalla tactil. Primeiro usa un
toque con tgres dedos para cambiar a modo SPL, logo usa as ordes tactiles
listadas arriba para realizar ordes.

## Version 19.01.1

* NVDA will no longer announce "monitoring library scan" after closing
  Studio in some situations.

## Versión 19.01/18.09.6-LTS

* Requírese do NVDA 2018.4 ou posterior.
* Máis trocos internos para facer o complemento compatible con Python 3.
* 19.01: algunhas traducións de mensaxes deste complemento asemellaranse a
  mensaxes do NVDA:
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
* Agora, en codificadores SAM, podes comandos de navegación por táboas
  (Control+Alt+teclas de frecha) para consultar certa información de estado
  do codificador.

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
  Cancelar

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
* Ao saltar entre paneis de axustes, NVDA lembrará as preferencias
  específicas do perfil (alarmas, anuncios de columnas, axustes da
  retransmisión de metadatos).
* Engadido o formato CSV (valores separados por comas) aos formatos de
  transcricións de listas de reprodución.
* Ao pulsar Control+NVDA+C para gardar a configuración do NVDA agora
  gardaranse tamén os axustes do complemento Station Playlist (require NVDA
  2018.3).

## Versión 18.08.2

* NVDA non verificará as actualizacións do complemento Studio se o
  complemento Add-on UPdater (proba de concepto) está instalado. En
  consecuencia, as opcións do complemento non incluirán as configuracións
  relacionadas coa actualización do complemento se este fose o caso. Se se
  utiliza Add-on Updater os usuarios deberían empregar as características
  fornecidas por este complemento para verificar as actualizacións do
  complemento Studio.

## Versión 18.08.1

* Arranxado un problema de WX4 visto ao saír de Studio.
* NVDA anunciará unha mensaxe axeitada cando o texto de modificación da
  lista de reprodución non estea presente, visto comunmente tras cargar unha
  lista de reprodución non modificada ou ao iniciarse Studio.
* NVDA xa non parecerá non facer nada ou non reproducirá un ton de erro ao
  tentar obter o estado de transmisión de metadatos vía Asistente SPL (E).

## Versión 18.08

* O diálogo de opcións do complemento está agora baseado na interface de
  opcións multicategoría do NVDA 2018.2. En consecuencia, esta versión
  require NVDA 2018.2 ou posterior. A antiga interface de opcións do
  complemento está desaconsellada e eliminarase e será eliminada máis
  adiante no 2018.
* Engadida unha nova sección (botón/panel) nas opcións do complemento para
  configurar as opcións das transcripcións de listaxe de reprodución, usado
  para configurar a inclusión e órden de columnas para esta característica e
  outros axustes.
* Ao crear unha nova transcrición de lista de reprodución baseada en táboa e
  se a ordeación persoalizada de columnas e/ou a eliminación de columnas
  está en efecto, NVDA utilizará a ordeación persoalizada de presentación de
  columnas especificado nas opcións do complemento e/ou non incluirá
  información das columnas eliminadas.
* Ao utilizar comandos de navegación por columnas en elementos de pista
  (ctrl+alt+inicio/fin/frecha esquerda/frecha dereita) en Studio, Creator e
  Track Tool, NVDA non anunciará datos de columna incorrectos despois de
  cambiar a posición de columna vía rato.
* Melloras significativas á resposta do NVDA ao utilizar comandos de
  navegación de columnas en Creator e Track tool. En particular, en Creator
  NVDA responderá mellor ao usar comandos de navegación de columnas.
* O NVDA xa non reproducirá tons de erro ou xa non parecerá non facer nada
  ao tentar engadir comentarios a pistas en Studio ou ao saír do NVDA
  mentres se use Studio, causado por un problema de compatibilidade con
  WxPython 4.

## Versión 18.07

* Engadida unha pantalla multicategoría experimental de opcións do
  complemento, accesible activando unha opción no diálogo de opcións do
  complemento/avanzado (debes reiniciar o NVDA tras configurar este axuste
  para que se mostre o novo diálogo). Isto é para usuarios de NVDA 2018.2, e
  non todos os axustes do complemento se poden configurar dende esta
  pantalla.
* NVDA xa non reproducirá tons de erro ou non fará nada ao renomear un
  perfil de transmisión dende os axustes do complemento, causado por un
  problema de compatibilidade co WxPython 4.
* Ao reiniciar NVDA y/o Studio despois de facer cambios nos axustes dun
  perfil de emisión que non sexa o perfil normal, NVDA xa non volverá ás
  opcións por defecto.
* Agora é posible obter transcricións de lista de reprodución para a hora
  actual. Selecciona "hora actual" na lista de rango de listaxe de
  reprodución no diálogo de transcricións de lista de reprodución (asistente
  SPL, shift+F8).
* Engadida unha opción no diálogo de Transcricións de Listas de Reprodución
  para gardar as transcricións nun arquivo (todos os formatos) ou copiala ao
  portapapeis (só nos formatos texto e táboa Markdown) ademais de velas na
  pantalla. Cando se gardan as transcricións, almacénanse no cartafol de
  documentos do usuario baixo o subcartafol "nvdasplPlaylistTranscripts".
* Xa non se inclúe a columna Estado ao crear transcricións de listas de
  reprodución nos formatos táboa HTML e Markdown.
* Cando se estea a enfocar unha pista en Creator e Track Tool, ao pulsar
  Control+NVDA+fila numérica dúas veces amosará a información da columna
  nunha xanela de modo exploración.
* Engadida Control+Alt+Inicio/Fin en Creator e TrackTool para mover o
  navegador de Columnas á primeira ou á última columna no Visualizador de
  Lista de Reprodución.

## Versión 18.06.1

* Arranxa varios problemas de compatibilidade con WxPython 4, incluíndo a
  imposibilidade de abrir os diálogos do buscador de pistas
  (Control+NVDA+F), de procura de columnas e de buscador de rangos de tempo
  en Studio e o diálogo de etiquetado de transmisións (f12) dende a ventá de
  codificadores.
* Se ocorre un erro inesperado ao abrir un diálogo de procura dende studio
  NVDA presentará mensaxes máis axeitadas no canto de dicir que outro
  diálogo de busca xa estaba aberto.
* Na ventá de codificadores, NVDA xa non reproducirá tons de erro nin
  aparentará non facer nada ao tentar abrir o diálogo de axustes do
  codificador (Control+NVDA+0).

## Versión 18.06

* Engadido botón "Aplicar" nas preferencias do complemento para aplicar a
  configuración sobre o perfil actualmente seleccionado e/ou activo sen
  pechar o diálogo primeiro. Esta característica está dispoñible para os
  usuarios de NVDA 2018.2.
* Resolto un erro polo que NVDA aplicaba os cambios nos axustes do
  Explorador de Columnas aínda que se premese "Cancelar" dende o diálogo de
  preferencias do complemento.
* En Studio, ao premer Control+NVDA+números cando unha pista estea enfocada
  NVDA amosará a información da columna para unha columna específica nunha
  xanela de modo exploración.
* Se está enfocado nunha pista en Studio, ao premer Control+NVDA+Guión
  amosaranse os de todas as columnas nunha ventá de modo exploración.
* No StationPlaylist Creator, mentres unha pista estea enfocada, ao pulsar
  Control+NVDA+números anunciaranse os datos da columna específica.
* Engadido un botón nas opcións do complemento para configurar o Explorador
  de Columnas en SPL Creator.
* Engadido o formato Táboa Markdown aos formatos de transcricións de listas
  de reprodución.
* O comando para o correo electrónico de comentarios ao desenvolvedor
  cambiou de Control+NVDA+Guión a Alt+NVDA+Guión.

## Versión 18.05

* Engadida a posibilidade de tomar capturas parciais da lista de
  reprodución. Pódese facer definindo un rango de análise (asistente SPL, F9
  ao comezo do rango de análise) e movéndose a outro elemento, e executando
  o comando de capturas de lista de reprodución. 
* Engadido un novo comando no asistente SPL para solicitar transcricións da
  lista de reprodución nun número de formatos (shift+F8). Éstes inclúen
  texto plano, unha táboa HTML ou unha listaxe HTML.
* Varias características para análise de listas de reprodución, como a
  análise do tempo de pista e capturas de lista de reprodución están agora
  agrupadas baixo o título "Analizador de lista de reprodución".

## Versión 18.04.1

* O NVDA xa non fallará ao comezar o temporizador de conta atrás para perfís
  de retransmisión baseados en tempo se se está a usar o NVDA co wxPython 4
  toolkit instalado.

## Versión 18.04

* Fixéronse trocos para facer a característica de verificar actualizacións
  máis fiable, especialmente se a verificación automática de actualizacións
  do complemento está activada.
* NVDA reproducirá un ton para indicar o inicio dun escaneo de biblioteca
  cando estea configurado para reproducir pitidos para anuncios diversos.
* NVDA comezará o escaneo da biblioteca en segundo plano cando éste sexa
  invocado dende o diálogo de opcións do Studio ou automáticamente ao
  arranque.
* Tocar dúas veces sobre unha pista nunha pantalla táctil ou realizando o
  comando de acción por defecto agora seleccionará a pista e moverá o foco
  do sistema a ela.
* Resoltos varios erros ao tomar capturas de listas de reprodución
  (asistente SPL, F8) que conteñan só marcas horarias.

## Versión 18.03/15.14-LTS

* Se NVDA está configurado para anunciar o estado de emisión de metadatos
  cando Studio se inicia, NVDA atenderá a esta configuración e xa non
  anunciará o estado de emisión ao alternar dende e cara perfiles de cambio
  instantáneo.
* Se se cambia dende ou cara un perfil de cambio instantáneo e NVDA está
  configurado para anunciar o estado de emisión de metadatos cando isto
  ocorra, non se anunciará a información varias veces cando se alternen
  perfiles rapidamente.
* NVDA lembrará cambiar ao perfil basado en horario (se se definió para un
  evento) aínda que se reinicie NVDA varias veces durante a emisión.
* Se está activo un perfil basado en horario coa duración de perfil
  establecida, NVDA retornará ao perfil orixinal cando o perfil acabe aínda
  que se abra e se peche o diálogo de configuración.
* Se está activo un perfil basado en horario (particularmente durante a
  transmisión), non será posible cambiar os disparadores do perfil de
  emisión mediante o diálogo de configuración do complemento.

## Versión 18.02/15.13-LTS

* 18.02: debido aos cambios internos realizados para soportar pontos de
  extensión e outras características, requírese do NVDA 2017.4.
* A actualización adicional non será posible nalgúns casos. Esto inclúe
  executar o NVDA dende código fonte ou co modo seguro activado. A
  comprobación de modo seguro tamén é aplicable á 15.13-LTS.
* Se hai erros durante a comprobación das actualizacións, estos
  rexistraranse e o NVDA aconsellarate que leas o rexistro do NVDA para
  obter máis detalles.
* Nas opcións do complemento, non se amosarán varios axustes de
  actualización na seción de parámetros avanzados, coma o intervalo de
  actualización, se non se admite a actualización de complementos.
* O NVDA xa non semellará conxelarse ou non facer nada ao se cambiar a un
  perfil de cambio instantáneo ou a un perfil baseado no tempo e o NVDA está
  configurado para anunciar o estado da transmisión de metadatos.

## Versión 18.01/15.12-LTS

* Ao se usar a distribución JAWS para SPL Assistant, a orde buscar
  actualizacións (Control+Shift+U) agora funciona correctamente.
* Ao se cambiar as opcións de alarma de micrófono a través do diálogo alarma
  (Alt+NVDA+4), cambios como habilitar alarma e cambios ao intervalo de
  alarma de micrófono aplícanse cando se peche o diálogo.

## Versión 17.12

* Requírese do indows 7 Service Pack 1 ouposterior.
* Melloráronse varias características do complemento con pontos de
  extensión. Esto permite que as características alarma do micrófono e
  streaming de metadatos respondan a cambios en perfís de
  retransmisión. Esto require do NVDA 2017.4.
* Cando se saia do Studio, varios diálogos do complemento coma Opcións de
  complemento, diálogos de alarma e outros pecharanse automáticamente. Esto
  require do NVDA 2017.4.
* Engadida unha orde ao SPL Controller para informar do nome da pista actual
  en reprodución dende calquera sitio (c).
* Agora poedes premer as teclas de cart (F1, por exemplo) despois de
  introducir SPl Controller layer para reproducir carts asignados dende
  calquera lado.
* Debido a cambios introducidos en wxPython 4 GUI toolkit, o diálogo
  Eliminar etiqueta de stream agora é unha caixa combinada en lugar de un
  campo de entrada numérica.

## Versión 17.11.2

Esta é a derradeira versión que soporta o Windows XP, Vista e 7 sen o
Service Pack 1. A seguinte versión estable para estas versións de Windows
serán unha versión 15.x LTS.

* Se se usan versións de Windows anteriores ao Windows 7 Service Pack 1, non
  podes cambiarf ás canles de desenvolvedores.

## Versión 17.11.1/15.11-LTS

* O NVDA xa non reproducirá tons de erro ou xa non parecerá non facer nada
  ao se usar Control+Alt+teclas de frecha esquerda ou dereita para navegar
  por columnas en Track Tool 5.20 cunha pista cargada. Debido a este cambio,
  ao se usar o Studio 5.20, requírese da compilación 48 ou posterior.

## Versión 17.11/15.10-LTS

* Soporte inicial para StationPlaylist Studio 5.30.
* Se a alarma de micrófono e/ou o temporizador de intervalos están acesos e
  se se sae do Studio mentres o micrófono está aceso, o NVDA xa non
  reproducirá os tons de alarma de micrófono dende ningún sitio.
* Ao se borrar os perfís de retransmisión e ocorre outro perfil para seren
  un perfil de cambio instantáneo, a bandeira de cambio instantáneo non se
  debería borrar do perfil de cambio.
* Se borrando un perfil activo que non é un cambio instantáneo ou un perfil
  baseado en tempo, o NVDA pedirá confirmación unha vez máis antes de
  proceder.
* O NVDA aplicará as configuracións correctas para as opcións de alarma de
  micrófono cando os perfís de cambio a través do diálogo opcións do
  complemento.
* Agora podes premer SPL Controller, H para obter axuda para o SPL
  Controller layer.

## Versión 17.10

* Se se usan versións de Windows anteriores ao Windows 7 Service Pack 1, non
  podes cambiarf á canle de actualizacións Test Drive Fast. Unha versión
  futura deste complemento moverá ao usuario de versións vellas de Windows a
  unha canle de soporte dedicada.
* Varias configuracións xerais coma pitidos de anunciado de estado,
  notificación de comezo e de fin da listaxe de reprodución e outras  agora
  colócanse no novo diálogo opcións xerais do complemento (accesible dende
  un botón novo nas opcións do complemento).
* Agora é posible facer as opcións do complemento de só lectura, usar só o
  perfil normal, ou non cargar opcións dende disco cando Studio
  arranque. Estas contrólanse por novos parámetros de ordes de liña
  específicos para este complemento.
* Ao se executar o NVDA dende o diálogo Executar (Windows+R), agora podes
  pasar uns parámetros adicionais de liña de ordes para cambiar como
  funciona o complemento. Estos inclúen "--spl-configvolatile" (opcións de
  só lectura), "--spl-configinmemory" (Non cargar opcións dende disco), e
  "--spl-normalprofileonly" (usar só o perfil normal).
* Se se sae do Studio (non do NVDA) mentres un perfil de cambio instantáneo
  está activo, o NVDA xa non dará un anunciado enganoso ao cambiar a un
  perfil de cambio instantáneo cando se use o Studio de novo.

## Versión 17.09.1

* Como o resultado do anunciado de NV Access en que o NVDA 2017.3 será a
  derradeira versión que soporte versións de Windows anteriores ao windows 7
  Service Pack 1, o complemento Studio presentará unha mensaxe lembrándote
  acerca de esto se se executan versións vellas de Windows. O final do
  soporte para versións vellas de Windows deste complemento programouse para
  abril do 2018.
* O NVDA xa non amosa diálogos de inicio e/ou anuncia a versión do Studio se
  se iniciou coa bandeira mínimo axustada a (nvda -rm). a única excepción é
  o diálogo que lembra a versión vella de Windows.

## Versión 17.09

* Se un usuario entra no diálogo opcións avanzadas en opciones do
  complemento mentres a canle de actualizacións e o intervalo se configurou
  a Unidade Rápida de Probas e/ou cero días, o NVDA xa non presentará a
  mensaxe de aviso de canle e/ou de intervalo ao saír deste diálogo.
* As ordes de lista de reproducción restante e análise de tempo de pista
  agora requerirán que se cargue unha lista de reprodución, e pola contra
  amosarase unha mensaxe de erro máis precisa.

## Versión 17.08.1

* NVDA xa non fallará causando que o Studio reproduza a primeira pista cando
  estea conectado un codificador.

## Versión 17.08

* Cambios para actualizar as etiquetas de canles: try build agora é Test
  Drive Fast, development channel é Test Drive Slow. As compilacións
  verdadeiras "try" reservaranse para as compilacións reais try que requiran
  que os usuarios instalen manualmente unha versión test.
* O intervalo de actualización agora pode configurarse a 0 (cero) días. Esto
  permite ao complemento procurar actualizacións cando o NVDA e/ou o SPL
  Studio arranquen. Requerirase dunha confirmación para cambiar o intervalo
  de actualización a cero días.
* O NVDA xa non fallará ao procurar actualizacións do complemento se o
  intervalo de actualización se configura a 25 días ou máis.
* Na configuración do complemento, engadiuse unha Caixa de verificación para
  permitir ao NVDA reproducir un son cando un escoitante solicite
  entrar. Para usar esto compretamente, a ventá de peticións debe
  despregarse cando chegue a petición.
* Ao premer dúas veces a orde tempo de transmisión (NVDA+Shift+F12) agora
  causará que o NVDA anuncie os minutos e segundos restantes na hora actual.
* Agora é posible usar Buscador de Pista (Control+NVDA+F) para procurar
  nomes de pistas que procuraras antes selecionando un termo de busca dende
  un historial de termos.
* Ao se anunciar o título da pista actual ou seguinte a través do SPL
  Assistant, agora é posible incluir información acerca de que reproductor
  interno do Studio reproducirá a pista (ex.: player 1).
* Engadida unha opción na configuración do complemento en anuncios de estado
  para incluir información do reproductor ao se anunciar o título da pista
  actual e seguinte .
* Arranxado un problema na cola temporal e outros diálogos onde o NVDA non
  anunciaría os novos valores ao se manipular temporizadores.
* NVDA pode suprimir o anunciado de cabeceiras de columna como Artista e
  Categoría cando se revisan pistas no visualizador de listas de
  reprodución. Esta é unha opción específica do perfil de transmisión.
* Engadida unha Caixa de verificación no diálogo de opcióne do complemento
  para suprimir o anunciado  das cabeceiras de columna ao revisar pistas no
  visualizador de listas de reprodución.
* Engadida unha orde ao SPL Controller para informar do nome e da duración
  da pista actual en reprodución dende calquera sitio (c).
* Ao obter información de estado a través do SPL Controller (Q) mentres se
  usa o Studio 5.1x, a información coma o estado do micrófono, modo edición
  do cart e outra tamén se anunciará ademáis da reproducción e
  automatización.

## Versión 17.06

* Agora podes realizar a orde Buscador de Pista (Control+NVDA+F) mentres se
  carga unha lista de reproducción pero a primeira pista non se enfoca.
* NVDA xa non reproducirá tons de erro ou non fará nada ao procurar unha
  pista cara adiante dende a última pista ou cara atrás dende a primeira,
  respectivamente.
* Premer NVDA+Subrimir do teclado numérico (NVDA+Suprimir na distribución
  portátil) agora anunciará a posición da pista seguida do número de
  elementos nunha lista de reprodución.

## Versión 17.05.1

* NVDA xa non fallará ao gardar cambios para opcións de alarma dende varios
  diálogos de alarma (por exemplo, Alt+NVDA+1 para alarma de remate da
  pista).

## Versión 17.05/15.7-LTS

* O intervalo de actualización agora pode configurarse a 180 días. Para
  instalacións predeterminadas, o intervalo de actualización procurarase
  cada 30 días.
* Correxido un fallo onde o NVDA poderá reproducir tons de erro se o Studio
  sae mentres está activo un perfil baseado en tempo.

## Versión 17.04

* Engadido o soporte básico de depuración do complemento rexistrando
  información variada mentres o complemento está activo co NVDA configurado
  para rexistrar a depuración (requírese do NVDA 2017.1 e superior). Para
  usar esto, antes de instalar o NVDA 2017.1, dende o diálogo Saír do NVDA,
  escolle a opción "reiniciar co rexistro de depuración habilitado".
* Melloras para a presentación de varios diálogos do complemento gracias ás
  características do NVDA 2016.4.
* NVDA descargará actualizacións para o complemento de fondo se respondiches
  "si" cando se che preguntou para actualizar o
  complemento. Consecuentemente, xa non se che amosarán as notificacións de
  descarga do ficheiro dende os navegadores web.
* NVDA xa non parecerá colgarse ao procurar unha actualización ao iniciarse
  debido a que cambie a canle de actualizacións do complemento.
* Engadida a capacidade de premer Control+Alt+frecha arriba ou abaixo para
  moverse entre pistas (en especial, columnas de pista) verticalmente só
  según se move á fila seguinte ou anterior nunha táboa.
* Engadida unha Caixa de verificación no diálogo opcións do complemento para
  configurar que columna debería anunciarse ao se mover polas columnas
  verticalmente.
* Movidos os controis fin de pista, alarmas de intro e de micrófono dende as
  opcións do complemento ao novo Centro de Alarmas.
* No Centro de alarmas, os campos de edición de fin de pista e intro de
  pista sempre se amosan independientemente do estado das caixas de
  verificación de notificación de alarma.
* Engadida unha orde no SPL Assistant para obter instantáneas das listaxes
  de reprodución coma o número de pista, pista máis longa, artistas
  principais e así (F8). tamén podes engadir unha orde persoalizada para
  esta característica.
* Premendo o xesto persoalizado para instantáneas de listaxe de reprodución
  unha vez permitirá ao NVDA falar e amosar en braille unha información
  curta  instantánea. Premendo a orde dúas veces fará que o NVDA abra unha
  páxina web contendo unha información máis compreta da instantánea da
  listaxe de reprodución. Preme escape para pechar esta páxina web.
* Borrado o Dial de Pista (versión mellorada de teclas de frechas do NVDA),
  reemplazado polas ordes de navegación Explorador de Columnas e navegador
  de columnas/táboas). Esto afecta ao Studio e ao Track Tool.
* Despois de pechar o diálogo Insertar Pistas mentres estea en progreso un
  escaneado da biblioteca, xa non se require premer SPL Assistant, Shift+R
  para monitorizar o progreso do escaneo.
* Mellorada a precisión da detección e anunciado do compretado dos
  escaneados da biblioteca no Studio 5.10 e posterior. Esto corrixe un
  problema onde o monitoreo do escaneado da biblioteca rematará
  prematuramente cando hai máis pistas a escanear, necesitando reiniciar o
  monitoreo do escaneado da biblioteca.
* Mellorado o anunciado do estado do escaneo da biblioteca a través do SPL
  Controller (Shift+R) anunciando a conta de escaneo se o escaneado está a
  ocorrir.
* Na demo do Studio, cando aparece a ventá de rexistro ao se iniciar o
  Studio, as ordes coma tempo restante para unha pista xa non causará que o
  NVDA non faga nada, reproduza tons de erro, ou dé información
  errónea. Anunciarase unha mensaxe de erro no seu lugar. Ordes coma estas
  requerirán que a ventá principal do Studio estea presente.
* Soporte inicial para StationPlaylist Creator.
* Engadida unha nova orde no SPL Controller layer para anunciar o estado do
  Studio como a reprodución da pista e o estado do micrófono (Q).

## Versión 17.03

* NVDA xa non parecerá non facer nada ou non reproducirá un ton de erro ao
  cambiar a un perfil de transmisión baseado en tempo.
* Traducións actualizadas.

## Versión 17.01/15.5-LTS

Nota: 17.01.1/15.5A-LTS reemplaza a 17.01 debido aos cambios da localización
dos ficheiros novos do complemento.

* 17.01.1/15.5A-LTS: cambiouse de onde se descargan as actualizacións para
  as versións de soporte a longo prazo. É obrigatoria a instalación desta
  versión.
* Mellorada a resposta e a fiabilidade ao se usar o complemento para cambiar
  ao Studio, ou usando o foco para ordes do Studio dende outros programas ou
  cando un codificador está conectado e se lle pide ao NVDA que cambie ao
  Studio cando esto ocurra. Se o Studio se minimiza, a ventá do Studio
  amosarase como non dispoñible. Se é así, restaura a ventá do Studio dende
  a bandexa do sistema.
* Se se editan carts mentres o explorador de Cart está activado, xa non é
  necesario reintroducir o explorador de Cart para ver as asignacións de
  cart actualizadas cando o modo Edición de Cart se
  desactive. Consecuentemente, a mensaxe reintroducir explorador de Cart xa
  non se anuncia.
* No complemento 15.5-LTS,  correxiuse a presentación da interfaz do usuario
  para o diálogo de opcións do complemento SPL.

## Versión 16.12.1

* Correxida a presentación da interfaz do usuario para o diálogo de opcións
  do complemento SPL.
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

## Versións vellas

Por favor consulta a liga changelog para notas da versión para versións
vellas do complemento.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: https://addons.nvda-project.org/files/get.php?file=spl-lts18

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
