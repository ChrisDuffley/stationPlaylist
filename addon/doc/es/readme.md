# StationPlaylist #

* Autores: Geoff Shang, Joseph Lee y otros colaboradores
* Descargar [Versión estable][1]
* Descargar [versión de desarrollo][2]
* Compatibilidad con NVDA: de 2019.1 a 2019.2

Este paquete de complementos proporciona una utilización mejorada de Station
Playlist Studio y otras aplicaciones de StationPlaylist, así como utilidades
para controlar Studio desde cualquier lugar. Entre las aplicaciones
soportadas se encuentran Studio, Creator, la herramienta de pista, VT
Recorder y Streamer, así como los codificadores SAM, SPL y AltaCast.

Para más información acerca del complemento, lee la [guía del
complemento][4]. Para los desarrolladores que busquen cómo compilar el
complemento, consulta buildInstructions.txt localizado en la raíz del
repositorio del código fuente del complemento.

NOTAS IMPORTANTES:

* Este complemento requiere de NVDA 2019.1 o posterior y StationPlaylist
  Suite 5.20 o posterior.
* Si utilizas Windows 8 o posterior, para una mejor experiencia, deshabilita
  el modo atenuación de audio.
* A partir de 2018, los [registros de cambios para versiones antiguas][5] se
  encontrarán en GitHub. Este léeme del complemento listará cambios desde la
  versión 8.0/16.10 (2016 en adelante).
* Ciertas características del complemento no funcionarán bajo algunas
  condiciones, incluyendo la ejecución de NVDA en modo seguro.
* Debido a limitaciones técnicas, no puedes instalar ni utilizar este
  complemento en la versión de Windows Store de NVDA.
* Las funciones marcadas como "experimentales" están pensadas para ser
  probadas antes de una liberación más amplia, por lo que no estarán
  habilitadas en las versiones estables.

## Teclas de atajo

La mayoría de estos funcionará sólo en Studio a menos que se indique lo
contrario.

* Alt+Shift+T desde la ventana de Studio: anuncia el tiempo transcurrido
  para la pista actual en reproducción.
* Control+Alt+T (deslizar  con dos dedos hacia abajo en modo táctil para
  SPL) desde la ventana de Studio: anuncia el tiempo restante para la pista
  que se esté reproduciendo.
* NVDA+Shift+F12 (deslizar  con dos dedos hacia arriba en modo táctil para
  SPL) desde la ventana Studio: anuncia el tiempo de emisión tal como 5
  minutos para el principio de la hora. Pulsando esta orden dos veces
  anunciará los minutos y segundos hasta la hora.
* Alt+NVDA+1 (deslizar dos dedos a la derecha en modo SPL) desde la ventana
  de Studio: abre el diálogo de opciones de fin de pista.
* Alt+NVDA+2 (deslizar  con dos dedos hacia a la izquierda en modo táctil
  para SPL) desde la ventana Studio: Abre el diálogo de configuración de
  alarma de intro de la canción.
* Alt+NVDA+3 desde la ventana Studio: activa o desactiva el explorador de
  cart para aprender las asignaciones de cart.
* Alt+NVDA+4 desde la ventana Studio: Abre el diálogo alarma del micrófono.
* Control+NVDA+f desde la ventana de Studio: Abre un diálogo para encontrar
  una pista sobre la base del artista o del nombre de la canción. Pulsa
  NVDA+F3 para buscar hacia adelante o NVDA+Shift+F3 para buscar hacia
  atrás.
* Alt+NVDA+R desde la ventana de Studio: Pasos de las opciones de anunciado
  del escaneado de biblioteca.
* Control+Shift+X desde la ventana de Studio: Pasos de las opciones del
  temporizador braille.
* Control+Alt+flecha derecha o izquierda (mientras se enfoca una pista en
  Studio, Creator, o Track Tool): anuncia la columna de la pista siguiente o
  anterior.
* Control+Alt+flecha abajo/arriba (mientras se enfoque una pista sólo en
  Studio): Mueven a la pista siguiente o anterior y anuncian columnas
  específicas (no disponible en el complemento 15.x).
* Control+NVDA+1 a 0 (mientras se enfoque una pista en Studio, Creator o
  Track Tool): Anuncia el contenido de la columna especificada. Pulsando
  este atajo dos veces mostrará la información de la columna en una ventana
  para modo navegación.
* Control+NVDA+- (guión, en Studio): mostrar datos de todas las columnas de
  una pista en una ventana para modo navegación.
* Alt+NVDA+C mientras se enfoca una pista (sólo Studio): anuncia los
  comentarios de pista si los hay.
* Alt+NVDA+0 desde la ventana Studio: abre el diálogo de configuración del
  complemento para Studio.
* Alt+NVDA+- (guión) desde la ventana de Studio: envía retroalimentación al
  desarrollador del complemento utilizando el cliente de correo
  predeterminado.
* Alt+NVDA+F1: abre el diálogo de bienvenida.

## Órdenes sin asignar

Las siguientes órdenes no se asignaron de manera predeterminada; si deseas
asignnarlas, utiliza el diálogo Gestos de Entrada para añadir órdenes
personalizadas.

* Cambia a la ventana SPL Studio desde cualquier programa.
* SPL Controller layer.
* Anunciar el estado de Studio tal como reproducción de pista desde otros
  programas.
* Anunciar el estado del codificador desde otros programas.
* Capa SPL Assistant desde SPL Studio.
* Anuncia el tiempo incluyendo segundos desde SPL Studio.
* Anuncia la temperatura.
* Anuncia el título de la siguiente pista si se programó.
* Annuncia el título de la pista actualmente en reproducción.
* Marcando pista actual para comenzar el análisisx de tiempo de pista.
* Realizando análisis de tiempo de pista.
* Tomar instantáneas de la lista de reproducción.
* Encontrar texto en columnas específicas.
* Encontrar pista con duración que caiga dentro de un rango dado a través de
  buscador de rango de tiempo.
* Habilitar o deshabilitar cíclicamente metadatos del streaming.

## Órdenes adicionales al utilizar los codificadores

Las siguientes órdenes  están disponibles al utilizar los codificadores:

* F9: conecta a un servidor de streaming.
* F10: (Sólo SAM encoder): Desconecta de un servidor de streaming.
* Control+F9/Control+F10 (sólo codificador SAM): Conecta o desconecta todos
  los codificadores.
* F11: Activa o desactiva si NVDA cambiará a la ventana Studio para el
  codificador seleccionador si está conectado.
* Shift+F11: conmuta si Studio reproducirá la primera pista seleccionada
  cuando el codificador esté conectado a un servidor de streaming.
* Control+F11: Conmuta el monitoreo de fondo del codificador seleccionado.
* F12: Abre un diálogo para introducir etiquetas personalizadas para el
  codificador o el stream seleccionado.
* Control+F12: abre un diálogo para seleccionar el codificador que has
  eliminado (para realinear las etiquetas de cadena y las opciones del
  codificador).
* Alt+NVDA+0: abre el diálogo opciones del codificador para configurar
  opciones tales como etiqueta de cadena.

Además, las órdenes de revisión de columna están disponibles, incluyendo:

* Control+NVDA+1: posición del codificador.
* Control+NVDA+2: etiqueta de cadena.
* Control+NVDA+3 desde el codificador SAM: formato del codificador.
* Control+NVDA+3 desde los codificadores SPL y AltaCast: Opciones del
  codificador.
* Control+NVDA+4 desde el codificador SAM: estado de conexión del
  codificador.
* Control+NVDA+4 desde el codificador SPL o AltaCast: velocidad de
  transferencia o estado de la conexión.
* Control+NVDA+5 desde el codificador SAM: descripción del Estado de la
  conexión.

## Capa de SPL Assistant

Este conjunto de capas de órdenes te permite obtener varios estados enSPL
Studio, tales como si se está escuchando una canción, duración total de
todas las pistas para la hora y así sucesivamente. desde la ventana SPL
Studio, pulsa la orden de capa SPL Assistant,  luego pulsa una de las teclas
de la siguiente lista (una o más órdenes son exclusivas para el visualizador
de lista de reproducción). También puedes configurar NVDA para emular
órdenes de otros lectores de pantalla.

Las órdenes disponibles son:

* A: Automatización.
* C (Shift+C en distribuciones JAWS y Window-Eyes): Título para la pista
  actualmente en reproducción.
* C (distribuciones JAWS y Window-Eyes): conmuta el explorador de cart
  (visualizador de lista de reproducción sólo).
* D (R en distribución JAWS): duración restante para la lista de
  reproducción (si se da un mensaje de error, se mueve al visualizador de
  lista de reproducción y entonces emite esta orden).
* E(G en distribución Window-Eyes): estado de metadatos del streaming.
* Shift+1 hasta Shift+4, Shift+0: estado para los metadatos individuales de
  la URL del streaming (0 es para el codificador DSP).
* E (distribución Window-Eyes): tiempo transcurrido para la pista
  actualmente en reproducción.
* F: busca pista (visualizador de lista de reproducción sólo).
* H: Duración de la música para el actual espacio de tiempo.
* Shift+H: duración restante de la pista o del slot horario.
* I (L en distribuciones JAWS y Window-eyes): cuenta de oyentes.
* K: se mueve a la pista marcada (sólo visualizador de lista de
  reproducción).
* Control+K: pone la pista actual como la pista marcada (sólo visualizador
  de lista de reproducción).
* L (Shift+L en las distribuciones JAWS y Window-Eyes): línea auxiliar.
* M: Micrófono.
* N: Título para la siguiente pista programada.
* P: Estado de reproducción (reproduciendo o detenido).
* Shift+P: Tono de la pista actual.
* R (Shift+E en disbribuciones JAWS y Window_eyes): Grabar en archivo
  habilitado/deshabilitado.
* Shift+R: Monitor de escaneado de biblioteca en progreso.
* S: Comienzo de pistas (programado).
* Shift+S: tiempo hasta el que se reproducirá la pista seleccionada
  (comienzos de pistas).
* T: modo editar/insertar Cart activado/desactivado.
* U: Studio al día.
* W: clima y temperatura si se configuró.
* Y: Estado modificado de lista de reproducción.
* 1 hasta 0 (6 para Studio 5.0x): anuncia el contenido de la columna para
  una columna específica.
* F8: toma instantáneas de la lista de reproducción (número de pistas, pista
  más larga, etc.).
* Shift+F8: Solicita transcripciones de la lista de reproducción en varios
  formatos.
* F9: Marca la pista actual como inicio del análisis de lista de
  reproducción (sólo visualizador de lista de reproducción).
* F10: realiza el análisis de tiempo de la pista (sólo visualizador de lista
  de reproducción).
* F12: cambia entre el perfil actual y uno predefinido.
* F1: Ayuda de la capa.
* Shift+F1: abre la guía del usuario en línea.

## SPL Controller

El SPL Controller es un conjunto de comandos de capas que puedes utilizar
para el control del SPL Studio desde cualquier lugar. Pulsa la orden de capa
del SPL Controller, y NVDA dirá, "SPL Controller." Pulsa otra orden para
controlar varias opciones del Studio tales como micrófono
activado/desactivado o reproducir la siguiente pista.

Las órdenes disponibles para el SPL Controller son:

* Pulsa P para reproducir la siguiente pista seleccionada.
* Pulsa U para pausar o no pausar la reproducción.
* Pulsa S para detener la pista con desvanecimiento, o para detener la pista
  instantáneamente, pulsa T.
* Pulsa M o Shift+M para activar o desactivar el micrófono, respectivamente,
  o pulsa N para habilitar el micrófono sin fade.
* Pulsa A para permitir la automatización oShift+A para desactivarla.
* Pulsa L para permitir la entrada de línea auxiliar o shift+L para
  desactivarla.
* Pulsa R para escuchar el tiempo restante para la pista actual en
  reproducción.
* Pulsa Shift+R para obtener un informe sobre el progreso del escaneado de
  la biblioteca.
* Pulsa C para permitir a NVDA anunciar el nombre y la duración de la pista
  actualmente en reproducción.
* Pulsa Shift+C para permitir a NVDA anunciar el nombre y la duración de la
  pista actualmente en reproducción si la hay.
* Pulsa E para obtener una cuenta y etiquetas de los codificadores que están
  siendo monitorizados.
* Pulsa I para obtener el recuento de oyentes.
* Pulsa Q para obtener información de estado variada acerca de Studio
  incluyendo si una pista se está reproduciendo, si el micrófono está
  encendido y otra.
* Pulsa las teclas de cart (F1, Control+1, por ejemplo) para reproducir
  carts asignados desde cualquier lugar.
* Pulsa H para mostrar un diálogo de ayuda que liste  las órdenes
  disponibles.

## Alarmas de pista

Por defecto, NVDA reproducirá un pitido si quedan cinco segundos a la
izquierda de la pista (outro) y/o intro. Para configurar este valor así como
para habilitarlos o deshabilitarlos, pulsa Alt+NVDA+1 o Alt+NVDA+2 para
abrir los diálogos fin de la pista y canción ramp, respectivamente. Además,
utiliza las opciones del diálogo del complemento Studio para configurar si
escucharás un pitido, un mensaje o ambos cuando se enciendan las alarmas.

## Alarma de micrófono

Puedes pedir a NVDA reproducir una canción cuando el micrófono haya sido
activado un rato. Pulsa Alt+NVDA+4 para configurar el tiempo de alarma en
segundos (0 la deshabilita).

## Track Finder

Si deseas encontrar rápidamente una canción por un artista o por el nombre
de la canción, desde la lista de pistas, pulsa Control+NVDA+F. Teclea el
nombre del artista o el nombre de la canción. NVDA te colocará en la canción
si la encontró o mostrará un error si no pudo encontrar la canción que estás
buscando. Para encontrar una canción o artista introducidos anteriormente,
pulsa NVDA+Shift+F3 para buscarla hacia adelante o atrás.

Nota: Track Finder es sensible a las mayúsculas.

## Explorador Cart

Dependiendo de la edición, SPL Studio permite hasta 96 carts para asignar
para la reproducción. NVDA te permite escuchar que cart, o jingle se asignó
a estas órdenes.

Para aprender las asignaciones de los cart, desde SPL Studio, pulsa
Alt+NVDA+3. Pulsando la  orden del cart una vez te dirá que  jingle se
asigna a  la orden. Pulsando la orden del cart dos veces reproducirá el
jingle. Pulsa Alt+NVDA+3 para salir del explorador de cart. Mira la guía del
complemento para más información sobre el explorador de carts.

## Análisis de tiempo de la pista

Para obtener ancho para reproducir las pistas seleccionadas, marca la pista
actual para iniciar el análisis de tiempo de la pista (SPL Assistant, F9),
entonces pulsa SPL Assistant, F10 cuando se llegue a la selección final.

## Explorador de Columnas

Pulsando Control+NVDA+1 hasta 0 o SPL Assistant, 1 hasta 0, puedes obtener
contenidos de columnas especificadas. Por omisión, hay artista, título,
duración, intro, categoría, Nombre de fichero, año, álbum, género y tiempo
programado. Puedes configurar qué columnas se explorarán a través del
diálogo Explorador de columnas que se encuentra en el diálogo de opciones
del complemento.

## Instantáneas de lista de reproducción

Puedes pulsar SPL Assistant, F8 mientras se enfoque sobre una lista de
reproducción en Studio para obtener varias estadísticas acerca de una lista
de reproducción, incluyendo el número de pistas en la lista, la pista más
larga, lista de artistas y así. Después de asignar una orden personalizada
para esta característica, pulsar dos veces la orden personalizada hará que
NVDA presente la información de la instantánea de la lista de reproducción
como una página web tal que puedas utilizar el modo exploración para navegar
(pulsa escape para cerrar).

## Transcripciones de lista de reproducción

Pulsando en SPL Assistant, Shift+F8 presentará un cuadro de diálogo para
permitirte solicitar transcripciones de lista de reproducción en varios
formatos, incluyendo en un formato de texto plano, y tabla HTML o una lista.

## Diálogo de configuración

Desde la ventana de studio, puedes pulsar Alt+NVDA+0 para abrir el diálogo
de configuración del complemento. Alternativamente, ve al menú Preferencias
de NVDA y selecciona el elemento Opciones de SPL Studio. Este diálogo
también se utiliza para administrar los perfiles de transmisión.

## Modo táctil de SPL

Si estás utilizando Studio en un ordenador con pantalla táctil ejecutando
Windows 8 o posterior y tienes NVDA 2012.3 o posterior instalado, puedes
realizar algunas órdenes de Studio desde la pantalla táctil. Primero utiliza
un toque con tres dedos para cambiar a modo SPL, entonces utiliza las
órdenes táctiles listadas arriba para llevar a cabo tareas.

## Versión 19.10/18.09.12-LTS

* Acortado el mensaje de anuncio de versión de Studio cuando este se inicia.
* Se anunciará información de versión de Creator al iniciarlo.
* 19.10: se puede asignar una orden personalizada para la orden de estado
  del codificador desde el controlador SPL (E) de tal forma que se pueda
  usar desde cualquier parte.
* Soporte inicial para el codificador AltaCast (Plugin para Winamp, Studio
  debe reconocerlo). Las órdenes son las mismas que las del codificador SPL.

## Versión 19.08.1

* En los codificadores SAM, NVDA ya no parecerá hacer nada o reproducir
  tonos de error si una entrada del codificador se elimina mientras se
  monitoriza en segundo plano.

## Versión 19.08/18.09.11-LTS

* 19.08: se requiere NVDA 2019.1 o posterior.
* 19.08: NVDA ya no parecerá hacer nada ni reproducirá tonos de error al
  reiniciarlo mientras el diálogo de opciones del complemento de Studio esté
  abierto.
* NVDA recordará los ajustes específicos del perfil al cambiar entre paneles
  de opciones, incluso tras renombrar el perfil de emisión seleccionado
  actualmente desde las opciones del complemento.
* NVDA ya no se olvidará de respetar los cambios de los perfiles basados en
  tiempo cuando se pulse el botón Aceptar para cerrar las opciones del
  complemento. Este fallo ha estado presente desde que se migró a las
  opciones en varias páginas en 2018.

## Versión 19.07/18.09.10-LTS

* Se ha renombrado el complemento de "StationPlaylist Studio" a
  "StationPlaylist" para describir mejor las aplicaciones y características
  que soporta este complemento.
* Mejoras internas de seguridad.
* Si los ajustes de la alarma del micrófono o el flujo de metadatos se
  modifican desde las opciones del complemento, NVDA ya no fallará al
  aplicar las opciones cambiadas. Esto resuelve un problema por el que la
  alarma del micrófono no se iniciaba o detenía adecuadamente después de
  cambiar los ajustes mediante las opciones del complemento.

## Versión 19.06/18.09.9-LTS

La versión 19.06 soporta Studio 5.20 y posteriores.

* Soporte inicial para StationPlaylist Streamer.
* Mientras se ejecutan diversas aplicaciones de Studio como la herramienta
  de pista o el propio Studio, si se inicia una segunda instancia de la
  aplicación y luego se cierra, NVDA ya no hará que los procedimientos de
  configuración del complemento de Studio causen errores y dejen de
  funcionar correctamente.
* Se han añadido etiquetas para diversas opciones del diálogo de
  configuración del codificador de SPL.

## Versión 19.04.1

* Corregidos varios problemas con los anuncios de columna rediseñados y los
  paneles de transcripción de lista de reproducción en los ajustes del
  complemento, incluyendo cambios en el orden de columnas personalizado y su
  inclusión que no se reflejaban al guardar y / o alternar entre paneles.

## Versión 19.04/18.09.8-LTS

* Varios comandos globales como acceder a SPL Controller y saltar a la
  ventana de Studio se desactivarán si NVDA se está ejecutando en modo
  seguro o como aplicación de la Windows Store.
* 19.04: en los paneles de anuncio de columnas y transcripción de listas de
  reproducción (configuración del complemento), los controles de inclusión /
  orden personalizado serán visibles directamente en vez de tener que pulsar
  un botón para abrir un diálogo y configurar estos ajustes.
* En Creator, NVDA ya no reproducirá tonos de error o parecerá no hacer nada
  al enfocar ciertas listas.

## Versión 19.03/18.09.7-LTS

* Al pulsar ctrl+NVDA+r para recargar los ajustes guardados también hará que
  se recarguen los ajustes del complemento de Studio, y al pulsar esta orden
  tres veces los ajustes del complemento de Studio se restablecerán a
  valores de fábrica junto con los de NVDA.
* Se ha renombrado el panel "Opciones avanzadas" del diálogo de
  configuración del complemento de Studio a "Avanzado".
* Experimental en 19.03: en los paneles de anuncio de columnas y
  transcripción de listas de reproducción (configuración del complemento),
  los controles de inclusión / orden personalizado serán visibles
  directamente en vez de tener que pulsar un botón para abrir un diálogo y
  configurar estos ajustes.

## Versión 19.02

* Se ha eliminado la función de comprobación de actualizaciones incorporada
  en el complemento, incluyendo la orden para buscar actualizaciones en el
  asistente de SPL (ctrl+shift+u) y las opciones de búsqueda de
  actualizaciones del complemento en los ajustes. Ahora es Add-on Updater el
  encargado de buscar actualizaciones.
* NVDA ya no parecerá no hacer nada o no reproducirá tonos de error cuando
  se configure un intervalo de activación del micrófono, usado para recordar
  a los locutores que el micrófono está activo emitiendo pitidos periódicos.
* Cuando se restablecen los ajustes del complemento desde el diálogo de
  configuración / panel de restablecimiento, NVDA preguntará una vez más si
  se encuentra activo un perfil de cambio instantáneo o un perfil basado en
  tiempo.
* Tras restablecer los ajustes del complemento de Studio, NVDA desactivará
  el temporizador de la alarma del micrófono y el anuncio del estado de los
  metadatos del flujo, al igual que ocurre al cambiar entre perfiles de
  emisión.

## Versión 19.01.1

* NVDA ya no anunciará "Monitorizando escaneo de biblioteca" tras cerrar
  Studio en algunas situaciones.

## Versión 19.01/18.09.6-LTS

* Se requiere de NVDA 2018.4 o posterior.
* Más cambios en el código para hacer al complemento compatible con Python
  3.
* 19.01: algunas traducciones de mensajes de este complemento se parecerán a
  los mensajes de NVDA.
* 19.01: la característica buscar actualizaciones para este complemento no
  está  más. Se presentará un mensaje de error cuando se intente utilizar
  SPL Assistant, Control+Shift+U para buscar actualizaciones. Para
  actualizaciones futuras, por favor utiliza el complemento Add-on Updater.
* Ligeras mejoras de rendimiento al utilizar NVDA con aplicaciones distintas
  de Studio mientras la grabadora de pistas de voz esté activa. NVDA seguirá
  mostrando problemas de rendimiento cuando se utilice el propio Studio con
  la grabadora de voz activa.
* En los codificadores, si hay un cuadro de diálogo de configuración del
  codificador abierto (Alt+NVDA+0), NVDA presentará un mensaje de error si
  se intenta abrir otro cuadro de diálogo de configuración del codificador.

## Versión 18.12

* Cambios internos para hacer al complemento compatible con versiones
  futuras de NVDA.
* Corregidas muchas instancias de mensajes del complemento que se
  verbalizaban en inglés a pesar de que el complemento estaba traducido a
  otros idiomas.
* Si se usa el asistente de SPL para buscar actualizaciones del complemento
  (asistente de SPL, ctrl+shift+u), NVDA no instalará nuevas versiones del
  complemento si estas necesitan una versión más reciente de NVDA.
* Algunas órdenes del asistente de SPL ahora necesitarán que el visor de
  lista de reproducción esté visible y contenga una lista de reproducción, y
  en algunos casos, que una pista tenga el foco. Entre las órdenes afectadas
  se incluyen duración restante (D), instantáneas de lista de reproducción
  (f8), y transcripción de listas de reproducción (shift+f8).
* La orden de la duración restante de lista de reproducción (asistente de
  SPL, D) ahora necesitará que el foco esté en una pista en el visor de
  lista de reproducción.
* En los codificadores SAM, ahora puedes usar órdenes de navegación por
  tablas (ctrl+alt+flechas) para revisar diversa información de estado del
  codificador.

## Versión 18.11/18.09.5-LTS

Nota: la versión 18.11.1 sustituye a la 18.11 para proporcionar un soporte
más sólido en Studio 5.31.

* Soporte inicial para StationPlaylist Studio 5.31.
* Ahora puedes obtener instantáneas de la lista de reproducción (asistente
  de SPL, f8) y transcripciones (asistente de SPL, shift+f8) mientras hay
  una lista de reproducción cargada pero la primera pista no está enfocada.
* NVDA ya no parecerá hacer nada o reproducir tonos de error al intentar
  anunciar el estado del flujo de metadatos cuando Studio se inicia si se
  configura para que lo haga.
* Si se ha configurado para anunciar el estado del flujo de metadatos al
  inicio, el anuncio de estado de los metadatos de flujo ya no interrumpirá
  anuncios sobre cambios en la barra de estado y viceversa.

## Versión 18.10.2/18.09.4-LTS

* Solucionado un problema que impedía cerrar la pantalla de opciones del
  complemento si se pulsaba el botón Aplicar y seguidamente se pulsaban los
  botones Aceptar o Cancelar.

## Versión 18.10.1/18.09.3-LTS

* Se han resuelto varios problemas relacionados con la función de anuncio de
  conexión del codificador, incluido que no se anunciaran mensajes de
  estado, fallos al reproducir la primera pista, o no cambiar a la ventana
  de Studio al estar conectado. Estos fallos son causados por WXPython 4
  (NVDA 2018.3 y posterior).

## Versión 18.10

* Se requiere NVDA 2018.3 o posterior.
* Cambios internos para hacer al complemento más compatible con Python 3.

## Versión 18.09.1-LTS

* Al obtener transcripciones de lista de reproducción en formato de tabla
  HTML, las cabeceras de columna ya no se renderizan como una cadena con una
  lista Python.

## Versión 18.09-LTS

La versión 18.09.x es la última que se basa en antiguas tecnologías y da
soporte a Studio 5.10. La versión 18.10 y posteriores darán soporte a Studio
5.11 / 5.20 y nuevas funciones. Algunas nuevas funciones se llevarán a la
18.09.x si es necesario.

* Se recomienda utilizar NVDA 2018.3 o posterior debido a la introducción de
  WXPython 4.
* La pantalla de opciones del complemento está totalmente basada en la
  interfaz multipágina derivada de NVDA 2018.2 y posterior.
* Los anillos de prueba lento y rápido se han combinado en un único canal de
  "desarrollo", ofreciendo una opción a los usuarios de versiones de
  desarrollo para probar las funciones piloto marcando la nueva casilla de
  funciones piloto en el panel de configuración avanzada del
  complemento. Los usuarios del anillo de pruebas rápido continuarán
  probando las funciones piloto.
* Se ha eliminado la posibilidad de seleccionar un canal de actualización
  diferente desde las opciones del complemento. Los usuarios que deseen
  cambiar a otro canal de actualizaciones deberían visitar el sitio web de
  complementos de la comunidad (addons.nvda-project.org), seleccionar
  StationPlaylist Studio y descargar la versión apropiada.
* Las casillas de verificación de inclusión de columnas para la
  verbalización de columnas y transcripciones de listas de reproducción, así
  como las casillas de flujo de metadatos, se han convertido a controles de
  lista verificables.
* Al cambiar entre paneles de opciones, NVDA recordará las opciones actuales
  de los ajustes específicos del perfil (alarmas, anuncios de columna,
  opciones de flujo de metadatos).
* Añadido el formato CSV (valores separados por comas) como formato de
  transcripciones de listas de reproducción.
* Al pulsar NVDA+control+c para guardar la configuración de NVDA, también se
  guardará la configuración del complemento de Studio (requiere NVDA
  2018.3).

## Versión 18.08.2

* NVDA ya no buscará actualizaciones del complemento de Studio si el
  complemento Add-on Updater (prueba de concepto) está instalado. Como
  consecuencia, las opciones del complemento ya no incluirán ajustes
  relacionados con la actualización del complemento si este es el caso. Si
  se utiliza Add-on updater, los usuarios deberían emplear las funciones de
  este complemento para buscar actualizaciones del complemento de Studio.

## Versión 18.08.1

* Ya solucionado otro error de compatibilidad con WXPython 4 reproducible
  cuando se sale de Studio.
* NVDA anunciará con un mensaje pertinente cuando el texto de modificación
  de lista de reproducción no esté presente, común cuando se carga una lista
  sin modificar o cuando arranca Studio.
* NVDA ya no parecerá no hacer nada o reproducirá un tono de error al
  intentar obtener el estado de transmisión vía Asistente SPL (E).

## Versión 18.08

* El diálogo de opciones del complemento se basa ahora en la interfaz de
  opciones multicategoría de NVDA 2018.2. En consecuencia, esta versión
  requiere NVDA 2018.2 o posterior. La interfaz antigua de opciones del
  complemento está desaprobada y se eliminará más adelante en 2018.
* Añadida una nueva sección (botón/panel) en las opciones del complemento
  para configurar las opciones de las transcripciones de lista de
  reproducción, usado para configurar la inclusión y orden de columnas para
  esta característica y otros ajustes.
* Al crear una transcripción de lista de reproducción basada en tabla y si
  el orden de columnas personalizado y/o la eliminación de columnas está
  configurada, NVDA usará el orden personalizado de presentación de columnas
  especificado en las opciones del complemento y/o no incluirá la
  información de columnas eliminadas.
* Al usar comandos de navegación por columnas en elementos de pista
  (ctrl+alt+inicio/fin/flecha izquierda/flecha derecha) en Studio, Creator y
  Track Tool, NVDA no anunciará datos de columna incorrectos después de
  cambiar la posición de columna vía ratón.
* Mejoras significativas en la respuesta de NVDA al usar atajos de
  navegación por columnas en Creator y Track Tool. En particular, usando
  Creator, NVDA responderá mejor al utilizar atajos de navegación por
  columnas.
* NVDA ya no reproducirá tonos de error o parecerá no hacer nada al intentar
  añadir comentarios a pistas en Studio o al salir de NVDA mientras Studio
  esté en uso, causado por un problema de compatibilidad con WXPython 4.

## Versión 18.07

* Añadida una pantalla multicategoría experimental de opciones del
  complemento, accesible activando una opción en el diálogo de opciones del
  complemento/avanzado (debes reiniciar NVDA tras configurar este ajuste
  para que se muestre el nuevo diálogo). Esto es para usuarios de NVDA
  2018.2, y no todos los ajustes del complemento se pueden configurar desde
  esta pantalla.
* NVDA ya no reproducirá tonos de error o parecerá no hacer nada al intentar
  renombrar un perfil de difusión desde los ajustes del complemento, causado
  por un problema de compatibilidad con WXPython 4.
* Al reiniciar NVDA y/o Studio después de hacer cambios en los ajustes de un
  perfil de emisión que no sea el perfil normal, NVDA ya no volverá a las
  opciones por defecto.
* Ahora es posible obtener transcripciones de lista de reproducción para la
  hora actual. Selecciona "hora actual" en el desplegable de rango de lista
  de reproducción en el diálogo de transcripciones de lista de reproducción
  (Asistente SPL, shift+f8).
* Añadida una opción en el diálogo de transcripciones de lista de
  reproducción para guardar las transcripciones en un archivo (todos los
  formatos) o copiadas al portapapeles (solo formatos texto y tabla
  Markdown) además de la de verlas en la pantalla. Cuando se guardan las
  transcripciones, lo hacen en la carpeta de documentos del usuario bajo la
  subcarpeta "nvdasplPlaylistTranscripts".
* La columna Estado ya no se incluye al crear listas en formatos HTML y
  tabla Markdown.
* Cuando  esté enfocada una pista en Creator o Track tool, pulsar
  control+NVDA+fila numérica dos veces presentará la información de columna
  en una ventana navegable.
* En Creator y Track Tool, añadidos los atajos Control+Alt+Inicio/Fin para
  mover el navegador de Columna a la primera o última columna para la pista
  enfocada.

## Versión 18.06.1

* Solucionados varios problemas de compatibilidad con WXPython 4, incluyendo
  la imposibilidad de abrir el buscador de pistas (control+NVDA+F), el
  buscador de columnas o el buscador de rango de tiempo en Studio y el
  diálogo etiquetador de streams (f12) desde la ventana de codificadores.
* Si al abrir un diálogo de buscar en Studio ocurre un error inesperado,
  NVDA presentará mensajes más apropiados en lugar de decir que otra ventana
  buscar está abierta.
* En la ventana de codificadores, NVDA ya no reproducirá tonos de error o
  parecerá no hacer nada al intentar abrir el diálogo de ajustes del
  codificador (alt+NVDA+0).

## Versión 18.06

* En los ajustes del complemento, añadido botón "Aplicar" de manera que la
  configuración se aplique al perfil actualmente seleccionado y/o activo sin
  cerrar la ventana primero. Esta característica está disponible para los
  usuarios de NVDA 2018.2.
* Resuelto un fallo por el que NVDA aplicaba los cambios en los ajustes del
  explorador de columnas a pesar de pulsar el botón cancelar en el diálogo
  de opciones del complemento.
* En Studio, al pulsar control+NVDA+fila numérica dos veces mientras una
  pista esté enfocada, NVDA mostrará la información de columna para una
  columna  específica en una ventana de modo exploración.
* Mientras una pista esté enfocada en Studio, pulsar control+NVDA+guión
  mostrará los datos para todas las columnas en una ventana de modo
  exploración.
* En StationPlaylist Creator, mientras una pista esté enfocada, pulsar
  control+NVDA+fila numérica anunciará los datos para una columna
  específica.
* Añadido un botón en los ajustes del complemento Studio para configurar el
  explorador de columnas en SPL Creator.
* Añadido el formato tabla markdown como formato de transcripciones de
  listas de reproducción.
* El comando de email para comentarios al desarrollador ha cambiado de
  control+NVDA+guión a alt+NVDA+guión.

## Versión 18.05

* Añadido soporte para capturas parciales de la lista de reproducción. Esto
  se puede hacer definiendo rango de análisis (asistente SPL, F9 al inicio
  del rango de análisis) y moviéndose a otro elemento, y pulsando el comando
  de Capturas de lista de reproducción.
* Añadido un nuevo comando en el asistente SPL para solicitar
  transcripciones de la lista de reproducción en un número de formatos
  (shift+F8). Éstos incluyen texto plano, tabla HTML y lista HTML.
* Varias características de análisis de lista de reproducción, como el
  análisis de tiempo de pista y capturas de lista de reproducción están
  ahora agrupadas bajo el título "Analizador de lista de reproducción".

## Versión 18.04.1

* NVDA ya no fallará al comenzar el temporizador de cuenta atrás para
  perfiles de retransmisión basados en tiempo si se está utilizando NVDA con
  el wxPython 4 toolkit instalado.

## Versión 18.04

* Se han realizado cambios para hacer la característica de verificar
  actualizaciones más fiable, especialmente si la verificación automática de
  actualizaciones del complemento está activada.
* NVDA reproducirá un tono para indicar el comienzo del escaneo de
  biblioteca cuando esté configurado para reproducir pitidos para anuncios
  diversos.
* NVDA comenzará a escanear la biblioteca en segundo plano si el escaneo se
  invoca desde el diálogo de opciones de Studio o automáticamente al
  arrancar.
* Tocar dos veces sobre una pista en la pantalla táctil o realizando el
  comando de acción por defecto seleccionará la pista y moverá el foco del
  sistema a ella.
* Se han resuelto varios errores cuando se toman capturas de listas de
  reproducción (asistente SPL, F8) que solo tienen marcadores horarios.

## Versión 18.03/15.14-LTS

* Si NVDA está configurado para anunciar el estado de emisión de metadatos
  cuando Studio se inicia, NVDA atenderá a esta configuración y ya no
  anunciará el estado de emisión al alternar desde y a perfiles de cambio
  instantáneo.
* Si se cambia desde o a un perfil de cambio instantáneo y NVDA está
  configurado para anunciar el estado de emisión de metadatos cuando esto
  ocurra, no se anunciará la información varias veces cuando se alternen
  perfiles rápidamente.
* NVDA recordará cambiar al perfil basado en horario (si se definió para un
  evento) aunque se reinicie NVDA varias veces durante la emisión.
* Si está activo un perfil basado en horario con la duración de perfil
  establecida, NVDA volverá al perfil original cuando el perfil acabe aunque
  se abra y se cierre el diálogo de configuración.
* Si está activo un perfil basado en horario (particularmente durante la
  transmisión), no será posible cambiar los disparadores del perfil de
  emisión mediante el diálogo de configuración del complemento.

## Versión 18.02/15.13-LTS

* 18.02: debido a los cambios internos realizados para soportar puntos de
  extensión y otras características, se requiere de NVDA 2017.4.
* La actualización adicional no será posible en algunos casos. Esto incluye
  ejecutar NVDA desde código fuente o con el modo seguro activado. La
  comprobación de modo seguro también es aplicable a 15.13-LTS.
* Si se producen errores durante la comprobación de las actualizaciones,
  éstos se registrarán y NVDA te aconsejará que leas el registro de NVDA
  para obtener más detalles.
* En las opciones del complemento, no se mostrarán varios ajustes de
  actualización en la sección de parámetros avanzados, como el intervalo de
  actualización, si no se admite la actualización de complementos.
* NVDA ya no parecerá congelarse o no hacer nada al cambiar a un perfil de
  cambio instantáneo o a un perfil basado en el tiempo y NVDA está
  configurado para anunciar el estado de la transmisión de metadatos.

## Versión 18.01/15.12-LTS

* Al utilizar la distribución de JAWS para SPL Assistant, la orden buscar
  actualizaciones (Control+Shift+U) ahora funciona correctamente.
* Al cambiar las opciones de alarma de micrófono a través del diálogo alarma
  (Alt+NVDA+4), cambios tales como habilitar alarma y cambios al intervalo
  de alarma de micrófono se aplican cuando se cierre el diálogo.

## Versión 17.12

* Se requiere Windows 7 Service Pack 1 o posterior.
* Se mejoraron varias características del complemento con puntos de
  extensión. Esto permite que las características alarma del micrófono y
  streaming de metadatos respondan a cambios en perfiles de
  retransmisión. Esto requiere NVDA 2017.4.
* Cuando se salga de Studio, varios diálogos del complemento tales como
  Opciones de complemento, diálogos de alarma y otros se cerrarán
  automáticamente. Esto requiere NVDA 2017.4.
* Añadida una orden a SPL Controller para informar del nombre de la pista
  actual en reproducción desde cualquier sitio (c).
* Ahora puedes pulsar las teclas de cart (F1, por ejemplo) después de
  introducir SPl Controller layer para reproducir carts asignados desde
  cualquier lugar.
* Debido a cambios introducidos en wxPython 4 GUI toolkit, el diálogo
  Eliminar etiqueta de stream ahora es un cuadro combinado en lugar de un
  campo de entrada numérica.

## Versión 17.11.2

Esta es la última versión que soporta Windows XP, Vista y 7 sin el Service
Pack 1. La siguiente versión estable para estas versiones de Windows serán
una versión 15.x LTS.

* Si se utilizan versiones de Windows anteriores a Windows 7 Service Pack 1,
  no puedes cambiarte a los canales de desarrollo.

## Versión 17.11.1/15.11-LTS

* NVDA ya no reproducirá tonos de error o ya no parecerá no hacer nada al
  utilizar Control+Alt+teclas de flecha izquierda o derecha para navegar por
  columnas en Track Tool 5.20 con una pista cargada. Debido a este cambio,
  al utilizar Studio 5.20, se requiere de la compilación 48 o posterior.

## Versión 17.11/15.10-LTS

* Soporte inicial para StationPlaylist Studio 5.30.
* Si la alarma de micrófono y/o el temporizador de intervalos están
  activados y si se sale de Studio mientras el micrófono está encendido,
  NVDA ya no reproducirá los tonos de alarma de micrófono desde ningún
  sitio.
* Al eliminar los perfiles de retransmisión y ocurre otro perfil para ser un
  perfil de cambio instantáneo, la bandera de cambio instantáneo no se
  debería borrar del perfil de cambio.
* Si eliminando un perfil activo que no es un cambio instantáneo o un perfil
  basado en tiempo, NVDA pedirá confirmación una vez más antes de proceder.
* NVDA aplicará las configuraciones correctas para las opciones de alarma de
  micrófono cuando los perfiles de cambio a través del diálogo opciones del
  complemento.
* Ahora puedes pulsar SPL Controller, H para obtener ayuda para el SPL
  Controller layer.

## Versión 17.10

* Si se utilizan versiones de Windows anteriores a Windows 7 Service Pack 1,
  no puedes cambiarf al canal de actualizaciones Test Drive Fast. Una
  versión futura de este complemento moverá al usuario de versiones antiguas
  de Windows a un canal de soporte dedicado.
* Varias configuraciones generales tales como pitidos de anunciado de
  estado, notificación de inicio y de fin de la lista de reproducción y
  otras  ahora se colocan en el nuevo diálogo opciones generales del
  complemento (accesible desde un botón nuevo en las opciones del
  complemento).
* Ahora es posible hacer las opciones del complemento de sólo lectura,
  utilizar sólo el perfil normal, o no cargar opciones desde disco cuando
  Studio arranque. Estas se controlan por nuevos parámetros de órdenes de
  línea específicos para este complemento.
* Al ejecutar NVDA desde el diálogo Ejecutar (Windows+R), ahora puedes pasar
  unos parámetros adicionales de línea de órdenes para cambiar cómo funciona
  el complemento. Estos incluyen "--spl-configvolatile" (opciones de sólo
  lectura), "--spl-configinmemory" (No cargar opciones desde disco), y
  "--spl-normalprofileonly" (utilizar sólo el perfil normal).
* Si se sale de Studio (no de NVDA) mientras un perfil de cambio instantáneo
  está activo, NVDA ya no dará un anuncio engañoso al cambiar a un perfil de
  cambio instantáneo cuando se utilice Studio de nuevo.

## Versión 17.09.1

* Como resultado del anuncio de NV Access en que NVDA 2017.3 será la última
  versión que soporte versiones de Windows anteriores a windows 7 Service
  Pack 1, el complemento Studio presentará un mensaje recordatorio acerca de
  esto si se ejecutan versiones antiguas de Windows. El fin del soporte para
  versiones antiguas de Windows de este complemento se programó para abril
  de 2018.
* NVDA ya no muestra diálogos de inicio y/o anuncia la versión de Studio si
  se inició con la bandera mínimo ajustada a (nvda -rm). la única excepción
  es el diálogo recordatorio de versión antigua de Windows.

## Versión 17.09

* Si un usuario entra en el diálogo opciones avanzadas en opciones del
  complemento mientras el canal de actualizaciones y el intervalo se
  configuró a Unidad Rápida de Pruebas y/o cero días, NVDA ya no presentará
  el mensaje de aviso de canal y/o de intervalo al salir de este diálogo.
* Las órdenes de lista de reproducción restante y análisis de tiempo de
  pista ahora requerirán que se cargue una lista de reproducción, y de lo
  contrario se mostrará un mensaje de error más preciso.

## Versión 17.08.1

* NVDA ya no fallará causando que Studio reproduzca la primera pista cuando
  esté conectado un codificador.

## Versión 17.08

* Cambios para actualizar las etiquetas de canales: try build ahora es Test
  Drive Fast, development channel es Test Drive Slow. Las compilaciones
  verdaderas "try" se reservarán para las compilaciones reales try que
  requieran que los usuarios instalen manualmente una versión test.
* El intervalo de actualización ahora puede configurarse a 0 (cero)
  días. Esto permite al complemento buscar actualizaciones cuando NVDA y/o
  SPL Studio arranquen. Se requerirá de una confirmación para cambiar el
  intervalo de actualización a cero días.
* NVDA ya no fallará al buscar actualizaciones del complemento si el
  intervalo de actualización se configura a 25 días o más.
* En la configuración del complemento, se añadió una casilla de verificación
  para permitir a NVDA reproducir un sonido cuando un oyente solicite
  entrar. Para utilizar esto completamente, la ventana de peticiones debe
  desplegarse cuando llegue la petición.
* Al pulsar dos veces la orden tiempo de transmisión (NVDA+Shift+F12) ahora
  causará que NVDA anuncie los minutos y segundos restantes en la hora
  actual.
* Ahora es posible utilizar Buscador de Pista (Control+NVDA+F) para buscar
  nombres de pistas que hayas buscado antes seleccionando un término de
  búsqueda desde un historial de términos.
* Al anunciar el título de la pista actual o siguiente a través del SPL
  Assistant, ahora es posible incluir información acerca de qué reproductor
  interno de Studio reproducirá la pista (ej.: player 1).
* Añadida una opción en la configuración del complemento en anuncios de
  estado para incluir información del reproductor al anunciar el título de
  la pista actual y siguiente .
* Corregido un problema en la cola temporal y otros diálogos donde NVDA no
  anunciaría los nuevos valores al manipular temporizadores.
* NVDA puede suprimir el anunciado de encabezados de columna tales como
  Artista y Categoría cuando se revisan pistas en el visualizador de listas
  de reproducción. Esta es una opción específica del perfil de transmisión.
* Añadida una casilla de verificación en el diálogo de opciones del
  complemento para suprimir el anunciado  de los encabezados de columna al
  revisar pistas en el visualizador de listas de reproducción.
* Añadida una orden a SPL Controller para informar del nombre y la duración
  de la pista actual en reproducción desde cualquier sitio (c).
* Al obtener información de estado a través de SPL Controller (Q) mientras
  se utiliza Studio 5.1x, la información tal como estado del micrófono, modo
  edición del cart y otra también se anunciará además de reproducción y
  automatización.

## Versión 17.06

* Ahora puedes realizar la orden Buscador de Pista (Control+NVDA+F) mientras
  se carga una lista de reproducción pero la primera pista no se enfoca.
* NVDA ya no reproducirá tonos de error o no hará nada al buscar una pista
  hacia adelante desde la última pista o hacia atrás desde la primera,
  respectivamente.
* Pulsar NVDA+Subrimir del teclado numérico (NVDA+Suprimir en la
  distribución portátil) ahora anunciará la posición de la pista seguida del
  número de elementos en una lista de reproducción.

## Versión 17.05.1

* NVDA ya no fallará al guardar cambios para opciones de alarma desde varios
  diálogos de alarma (por ejemplo, Alt+NVDA+1 para alarma de fin de pista).

## Versión 17.05/15.7-LTS

* El intervalo de actualización ahora puede configurarse a 180 días. Para
  instalaciones predeterminadas, el intervalo de actualización se buscará
  cada 30 días.
* Corregido un fallo donde NVDA podrá reproducir tonos de error si Studio
  sale mientras está activo un perfil basado en tiempo.

## Versión 17.04

* Añadido el soporte básico de depuración del complemento registrando
  información variada mientras el complemento está activo con NVDA
  configurado para registrar la depuración (se requiere de NVDA 2017.1 y
  superior). Para utilizar esto, antes de instalar NVDA 2017.1, desde el
  diálogo Salir de NVDA, elige la opción "reiniciar con el registro de
  depuración habilitado".
* Mejoras para la presentación de varios diálogos del complemento gracias a
  las características del NVDA 2016.4.
* NVDA descargará actualizaciones para el complemento en segundo plano si
  respondiste "sí" cuando se te preguntó para actualizar el
  complemento. Consecuentemente, ya no se te mostrarán las notificaciones de
  descarga del fichero desde los navegadores web.
* NVDA ya no parecerá colgarse al buscar una actualización al iniciarse
  debido a que cambie el canal de actualizaciones del complemento.
* Añadida la capacidad de pulsar Control+Alt+flecha arriba o abajo para
  moverse entre pistas (en especial, columnas de pista) verticalmente sólo
  según se mueve a la fila siguiente o anterior en una tabla.
* Añadida una casilla de verificación en el diálogo opciones del complemento
  para configurar qué columna debería anunciarse al moverse por las columnas
  verticalmente.
* Movidos los controles fin de pista, alarmas de intro y de micrófono desde
  las opciones del complemento al nuevo Centro de Alarmas.
* En el Centro de alarmas, los campos de edición de fin de pista e intro de
  pista siempre se muestran independientemente del estado de las casillas de
  verificación de notificación de alarma.
* Añadida una orden en el SPL Assistant para obtener instantáneas de listas
  de reproducción tales como número de pista, pista más larga, artistas
  principales y así (F8). también puedes añadir una orden personalizada para
  esta característica.
* Pulsando el gesto personalizado para instantáneas de lista de reproducción
  una vez permitirá a NVDA verbalizar y mostrar en braile una breve
  información instantánea. Pulsando la orden dos veces hará que NVDA abra
  una página web conteniendo una información más completa de la instantánea
  de la lista de reproducción. Pulsa escape para cerrar esta página web.
* Eliminado el Dial de Pista (versión mejorada de teclas de flechas de
  NVDA), reemplazado por las órdenes de navegación Explorador de Columnas y
  navegador de columnas/tablas ). Esto afecta a Studio y a Track Tool.
* Después de cerrar el diálogo Insertar Pistas mientras esté en progreso un
  escaneado de biblioteca, ya no se requiere pulsar SPL Assistant, Shift+R
  para monitorizar el progreso del escaneo.
* Mejorada la precisión de la detección y anunciado del completado de los
  escaneados de la biblioteca en Studio 5.10 y posterior. Esto corrige un
  problema donde el monitoreo de escaneado de la biblioteca finalizará
  prematuramente cuando hay más pistas a escanear, necesitando reiniciar el
  monitoreo de escaneado de la biblioteca.
* Mejorado el anunciado del estado del escaneo de biblioteca a través del
  SPL Controller (Shift+R) anunciando la cuenta de escaneo si el escaneado
  está ocurriendo.
* En la demo de Studio, cuando aparece la ventana de registro al iniciar
  Studio, las órdenes como tiempo restante para una pista ya no causará que
  NVDA no haga nada, reproduzca tonos de error, o dé información errónea. Se
  anunciará un mensaje de error en su lugar. Órdenes tales como estas
  requerirán que la ventana principal de Studio esté presente.
* Soporte inicial para StationPlaylist Creator.
* Añadida una nueva orden en SPL Controller layer para anunciar el estado de
  Studio como la reproducción de la pista y el estado del micrófono (Q).

## Versión 17.03

* NVDA ya no parecerá no hacer nada o no reproducirá un tono de error al
  cambiar a un perfil de transmisión basado en tiempo.
* Traducciones actualizadas.

## Versión 17.01/15.5-LTS

Nota: 17.01.1/15.5A-LTS reemplaza a 17.01 debido a cambios de la
localización de los ficheros nuevos del complemento.

* 17.01.1/15.5A-LTS: se cambió de dónde se descargan las actualizaciones
  para las versiones de soporte a largo plazo. Es obligatoria la instalación
  de esta versión.
* Mejorada la respuesta y la fiabilidad al utilizar el complemento para
  cambiar a Studio, o utilizando el foco para órdenes de Studio desde otros
  programas o cuando un codificador está conectado y se le pide a NVDA que
  cambie a Studio cuando esto ocurra. Si Studio se minimiza, la ventana de
  Studio se mostrará como no disponible. Si es así, restaura la ventana de
  Studio desde la bandeja del sistema.
* Si se editan carts mientras el explorador de Cart está activado, ya no es
  necesario reintroducir el explorador de Cart para ver las asignaciones de
  cart actualizadas cuando el modo Edición de Cart se
  desactive. Consecuentemente, el mensaje reintroducir explorador de Cart ya
  no se anuncia.
* En el complemento 15.5-LTS, se corrigió la presentación de la interfaz de
  usuario para el diálogo Opciones del complemento SPL.

## Versión 16.12.1

* Corregida la presentación de la interfaz de usuario para el diálogo
  Opciones del complemento SPL.
* Traducciones actualizadas.

## Versión 16.12/15.4-LTS

* Más trabajo sobre el soporte de Studio 5.20, incluyendo el anunciado del
  estado del modo inserción de cart (si está activado) desde el SPL
  Assistant layer (T).
* El conmutado del modo editar/insertar Cart ya no está afectado por la
  verbosidad de los mensajes ni por las opciones de anunciado del tipo de
  estado (Este estado se anunciará siempre a través de voz y/o braille).
* Ya no es posible añadir commentarios a las notas partidas.
* Soporte para Track Tool 5.20, incluyendo corregido un problema donde se
  anunciaba información errónea al utilizar las órdenes del Explorador de
  Columnas para anunciar información de columna.

## Versión 16.11/15.3-LTS

* Soporte inicial para StationPlaylist Studio 5.20, incluyendo la
  sensibilidad mejorada al obtener información de estado tal como estado de
  la automatización a través de SPL Assistant layer.
* Corregidos fallos relativos a la búsqueda de pistas e interactuación con
  ellas, incluyendo la incapacidad para marcar o desmarcar marcadores de
  pista o una pista encontrada a través del diálogo buscador de rango.
* El orden del anunciado de columnas ya no se revertirá al orden
  predeterminado después de cambiarlo.
* 16.11: Si los perfiles de transmisión tienen errores, el diálogo error ya
  no fallará al desplegarse.

## Versión 16.10.1/15.2-LTS

* Ahora puedes interactuar con la pista que se encontró a través del
  Buscador de Pistas (Control+NVDA+F) según la busques para reproducir.
* Traducciones actualizadas.

## Versión 8.0/16.10/15.0-LTS

La versión 8.0 (también conocida como 16.10) soporta SPL Studio 5.10 y
posteriores, con 15.0-LTS (antes 7.x) diseñada para proporcionar algunas
características nuevas de 8.0 para usuarios que utilicen versiones
anteriores de Studio. Al menos que se indique lo contrario, las entradas que
siguen se aplican tanto a 8.0 como a 7.x. Se mostrará un diálogo de
advertencia la primera vez que utilices el complemento 8.0 con Studio 5.0x
instalado, pidiéndote que utilices la versión 15.x LTS.

* El esquema de la versión ha cambiado para reflejar el año/mes de la
  publicación en lugar de mayor.menor. Durante el período de transición
  (hasta mediados de 2017), versión 8.0 es sinónimo de versión 16.10, con
  7.x LTS designándose como 15.0 debido a cambios incompatibles.
* El código fuente del complemento ahora se publica en GitHub (repositorio
  localizado en https://github.com/josephsl/stationPlaylist).
* Añadido un diálogo de bienvenida que se lanza cuando Studio arranca
  después de instalar el complemento. Se ha añadido una orden (Alt+NVDA+F1)
  para reabrir este diálogo una vez cerrado.
* Cambios para varias órdenes del complemento, incluyendo la eliminación de
  el comuntado del anuncio de estado (Control+NVDA+1), reasignada la alarma
  de fin de pista a Alt+NVDA+1, el conmutador de explorador de Cart ahora es
  Alt+NVDA+3, el diálogo de alarma de micrófono es Alt+NVDA+4 y el diálogo
  opciones del complemento/codificador es Alt+NVDA+0. Esto se hizo para
  permitir que Control+NVDA+fila de números se asigne al Explorador de
  Columnas.
* 8.0: relajada la restricción del Explorador de Columnas en lugar del 7.x
  así los números del 1 al 6 pueden configurarse para anunciar columnas en
  Studio 5.1x.
* 8.0: la orden conmutar Dial de pista y la opción correspondiente en las
  opciones del complemento han quedado en desuso y se eliminarán 9.0. Esta
  orden permanecerá disponible en el complemento 7.x.
* Añadido Control+Alt+Inicio/Fin para mover el navegador de Columna a la
  primera o última columna en el visualizador de la lista de reproducción.
* Ahora puedes añadir, ver, cambiar o eliminar comentarios de pista
  (notas). Pulsa Alt+NVDA+C desde una pista en el visualizador de lista de
  reproducción para escuchar los comentarios de pista si se definieron,
  pulsa dos veces para copiar el comentario al portapapeles o tres veces
  para abrir un diálogo para editar los comentarios.
* Añadida la capacidad de notificar si existe un comentario de pista, así
  como una opción en las opciones del complemento para controlar cómo
  debería hacerse.
* Añadido un ajuste en el diálogo opciones del complemento para permitir a
  NVDA notificarte si has alcanzado la parte superior o inferior del
  visualizador de lista de reproducción.
* Al reiniciar las opciones del complemento, ahora puedes especificar lo que
  se reinicia. Por defecto, las opciones del complemento se reiniciarán, con
  cuadros combinados para reiniciar el perfil de cambio instantáneo, perfil
  basado en tiempo, opciones del codificador y borrado de comentarios de
  pista añadidos al diálogo de opciones de reiniciado.
* En la Herramienta Pista, puedes obtener información sobre el álbum y
  código de CD pulsando Control+NVDA+9 y Control+NVDA+0, respectivamente.
* Se realizan mejoras al obtener información de columna por primera vez en
  la Herramienta de Pista.
* 8.0: añadido un diálogo en las opciones del complemento para configurar
  los slots del Explorador de Columnas para la Herramienta de Pista.
* Ahora puedes configurar el intervalo de alarma de micrófono desde el
  diálogo Alarma de micrófono (Alt+NVDA+4).

## Versiones antiguas

Por favor consulta el enlace changelog para notas de la versión para
versiones antiguas del complemento.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: https://addons.nvda-project.org/files/get.php?file=spl-lts18

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
