# StationPlaylist #

* Autores: Geoff Shang, Joseph Lee y otros colaboradores
* Descargar [Versión estable][1]
* Descargar [versión de desarrollo][2]
* Compatibilidad con NVDA: de 2019.3 a 2020.1

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

* Este complemento requiere StationPlaylist Suite 5.20 o posterior.
* Si utilizas Windows 8 o posterior, para una mejor experiencia, deshabilita
  el modo atenuación de audio.
* A partir de 2018, los [registros de cambios para versiones antiguas][5] se
  encontrarán en GitHub. Este léeme del complemento listará cambios desde la
  versión 18.09 (2018 en adelante).
* Ciertas características del complemento no funcionarán bajo algunas
  condiciones, incluyendo la ejecución de NVDA en modo seguro.
* Debido a limitaciones técnicas, no puedes instalar ni utilizar este
  complemento en la versión de Windows Store de NVDA.
* Las funciones marcadas como "experimentales" están pensadas para ser
  probadas antes de una liberación más amplia, por lo que no estarán
  habilitadas en las versiones estables.
* Cuando Studio está en ejecución, se pueden guardar, restablecer o poner
  los valores de fábrica del complemento pulsando control+NVDA+c,
  control+NVDA+r una vez o control+NVDA+r tres veces, respectivamente. Esto
  también se aplica a los ajustes del codificador - se pueden guardar y
  restablecer (pero no recargar) los ajustes del codificador si se usan los
  codificadores.
* La función de perfiles basados en tiempo ha quedado obsoleta y se
  eliminará en una versión futura.

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
* Alt+NVDA+1 (deslizamiento hacia la izquierda con dos dedos en el modo SPL)
  desde la ventana de Studio: abre la categoría Alarmas en el diálogo de
  configuración del complemento de Studio.
* Alt+NVDA+1 desde la ventana del editor de listas de reproducción de
  Creator o de Remote VT: anuncia la hora programada de la lista de
  reproducción cargada.
* Alt+NVDA+2 desde la ventana del editor de listas de reproducción de
  Creator y de Remote VT: anuncia la duración total de la lista de
  reproducción.
* Alt+NVDA+3 desde la ventana Studio: activa o desactiva el explorador de
  cart para aprender las asignaciones de cart.
* Alt+NVDA+3 desde la ventana del editor de listas de reproducción de
  Creator y de Remote VT: indica para cuándo se ha programado la
  reproducción de la pista seleccionada.
* Alt+NVDA+4 desde la ventana del editor de listas de reproducción de
  Creator y de Remote VT: anuncia la rotación y categoría asociadas con la
  lista de reproducción cargada.
* Control+NVDA+f desde la ventana de Studio: Abre un diálogo para encontrar
  una pista sobre la base del artista o del nombre de la canción. Pulsa
  NVDA+F3 para buscar hacia adelante o NVDA+Shift+F3 para buscar hacia
  atrás.
* Alt+NVDA+R desde la ventana de Studio: Pasos de las opciones de anunciado
  del escaneado de biblioteca.
* Control+Shift+X desde la ventana de Studio: Pasos de las opciones del
  temporizador braille.
* Control+Alt+flecha derecha o izquierda (mientras se enfoca una pista en
  Studio, Creator, Remote VT o Track Tool): anuncia la columna de la pista
  siguiente o anterior.
* Control+Alt+inicio o fin (mientras se enfoca una pista en Studio, Creator,
  Remote VT o Track Tool): anuncia la primera o última columna de la pista.
* Control+Alt+flecha abajo/arriba (mientras se enfoque una pista sólo en
  Studio): se mueve a la pista siguiente o anterior y anuncia columnas
  específicas.
* Control+NVDA+1 a 0 (mientras se enfoque una pista en Studio, Creator
  (incluyendo su editor de listas de reproducción), Remote VT o Track Tool):
  Anuncia el contenido de la columna especificada (primeras diez columnas
  por defecto). Pulsando este atajo dos veces mostrará la información de la
  columna en una ventana para modo navegación.
* Control+NVDA+- (guión cuando una pista tiene el foco en Studio, Creator y
  Track Tool): mostrar datos de todas las columnas de una pista en una
  ventana para modo navegación.
* Alt+NVDA+C mientras se enfoca una pista (sólo Studio): anuncia los
  comentarios de pista si los hay.
* Alt+NVDA+0 desde la ventana Studio: abre el diálogo de configuración del
  complemento para Studio.
* Alt+NVDA+p desde la ventana de Studio: abre el diálogo de perfiles de
  emisión de Studio.
* Alt+NVDA+- (guión) desde la ventana de Studio: envía retroalimentación al
  desarrollador del complemento utilizando el cliente de correo
  predeterminado.
* Alt+NVDA+F1: abre el diálogo de bienvenida.

## Órdenes sin asignar

Las siguientes órdenes se encuentran por defecto sin asignar; si deseas
asignarlas, usa el diálogo Gestos de entrada para añadir órdenes
personalizadas. Para hacerlo, desde la ventana de Studio, abre el menú NVDA,
Preferencias, Gestos de entrada. Expande la categoría StationPlaylist y
busca las órdenes sin asignar de la siguiente lista, elige "Añadir" y teclea
la orden que quieres usar.

* Cambia a la ventana SPL Studio desde cualquier programa.
* SPL Controller layer.
* Anunciar el estado de Studio tal como reproducción de pista desde otros
  programas.
* Anunciar el estado de conexión del codificador desde cualquier programa.
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
* Pulsa E para escuchar qué codificadores están conectados.
* Pulsa I para obtener el recuento de oyentes.
* Pulsa Q para obtener información de estado variada acerca de Studio
  incluyendo si una pista se está reproduciendo, si el micrófono está
  encendido y otra.
* Pulsa las teclas de cart (F1, Control+1, por ejemplo) para reproducir
  carts asignados desde cualquier lugar.
* Pulsa H para mostrar un diálogo de ayuda que liste  las órdenes
  disponibles.

## Alarmas de pista y micrófono

Por defecto, NVDA reproducirá un pitido si quedan cinco segundos para que
acabe la pista (outro) y/o intro, así como un pitido si el micrófono ha
estado activado durante un rato. Para configurar las alarmas de pista y
micrófono, pulsa NVDA+alt+1 para abrir las opciones de las alarmas en la
pantalla de opciones del complemento de Studio. También puedes utilizar esta
pantalla para configurar si se oye un pitido, un mensaje o ambos cuando se
encienden las alarmas.

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

Pulsando Control+NVDA+1 hasta 0, puedes obtener contenidos de columnas
específicas. Por defecto, estas son las diez primeras columnas de un
elemento de pista (en Studio: artista, título, duración, intro, outro,
categoría, año, álbum, género, mood). En el editor de listas de reproducción
de Creator y del cliente Remote VT, los datos de las columnas dependen del
orden de las mismas según se muestren en pantalla. En Studio, la lista
principal de pistas de Creator y la herramienta de pista, los slots de
columna están predefinidos sin importar el orden de las columnas en pantalla
y se pueden configurar desde el diálogo de opciones del complemento, bajo la
categoría Explorador de columnas.

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

## El diálogo de perfiles de emisión

Se pueden guardar configuraciones específicas para programas concretos en
perfiles de emisión. Estos perfiles se pueden gestionar desde el diálogo de
perfiles de emisión de SPL, al que se puede acceder pulsando alt+NVDA+p
desde la ventana de Studio.

## Modo táctil de SPL

Si estás utilizando Studio en un ordenador con pantalla táctil ejecutando
Windows 8 o posterior y tienes NVDA 2012.3 o posterior instalado, puedes
realizar algunas órdenes de Studio desde la pantalla táctil. Primero utiliza
un toque con tres dedos para cambiar a modo SPL, entonces utiliza las
órdenes táctiles listadas arriba para llevar a cabo tareas.

## Versión 20.05

* Soporte inicial para el cliente VT (pistas de voz) remoto, incluyendo las
  mismas órdenes para el editor remoto de listas de reproducción que las del
  editor de listas de reproducción de Creator.
* Las órdenes para abrir diálogos de opciones de alarma separados
  (Alt+NVDA+1, Alt+NVDA+2, Alt+NVDA+4) se han combinado en Alt+NVDA+1, y
  ahora abrirán los ajustes de la alarma en la pantalla de opciones del
  complemento de SPL, donde se pueden encontrar las opciones de alarma del
  micrófono y de la introducción y la conclusión.
* En el diálogo de disparadores que hay dentro del diálogo de perfiles de
  emisión, se ha eliminado la interfaz de usuario asociada a la función de
  perfiles de emisión basados en tiempo, como los campos de cambio de perfil
  en día, hora o duración.
* La opción de cuenta atrás de cambio de perfil que se encontraba en el
  diálogo de perfiles de emisión se ha eliminado.
* Ya que Window Eyes no está soportado por Vispero desde 2017, la
  disposición de órdenes del asistente de SPL para Window Eyes está obsoleta
  y se eliminará en una versión futura del complemento. Se mostrará un aviso
  al inicio urgiendo a los usuarios a que cambien la disposición de órdenes
  del asistente de SPL a NVDA (por defecto) o JAWS.
* Al usar slots en el explorador de columnas (órdenes control+NVDA+fila
  numérica) u órdenes de navegación por columnas (Control+alt+inicio / fin /
  flecha izquierda / flecha derecha) en Creator o el cliente Remote VT, NVDA
  ya no anunciará los datos de columna incorrectos tras cambiar la posición
  de columna en pantalla mediante el ratón.
* En los codificadores y Streamer, NVDA ya no parecerá hacer nada o
  reproducir tonos de error al salir de NVDA mientras el foco está en algo
  distinto a la lista de codificadores sin mover el foco a los codificadores
  primero.

## Versión 20.04

* La función de perfiles de emisión basados en tiempo está obsoleta. Se
  mostrará un mensaje con una advertencia cuando se inicie Studio por
  primera vez tras instalar el complemento 20.04 si se encuentran definidos
  uno o varios perfiles de emisión basados en tiempo.
* La gestión de perfiles de emisión se ha separado en un diálogo
  independiente al diálogo de opciones del complemento. Se puede acceder al
  diálogo de perfiles de emisión pulsando alt+NVDA+p desde la ventana de
  Studio.
* A causa de la duplicidad con las órdenes control+NVDA+números de la fila
  numérica en las pistas de Studio, las órdenes del explorador de columnas
  del asistente de SPL (fila numérica) se han eliminado.
* Se ha cambiado el mensaje de error que se muestra al intentar abrir un
  diálogo de opciones del complemento de Studio (tal como el diálogo de
  metadatos del flujo) mientras otro diálogo de opciones (como el diálogo de
  alarma de fin de pista) está activo. El nuevo mensaje de error es el mismo
  que el que se muestra al intentar abrir varios diálogos de opciones de
  NVDA.
* NVDA ya no reproducirá tonos de error ni se quedará sin hacer nada al
  pulsar el botón Aceptar en el diálogo del explorador de columnas después
  de configurar los slots de columna.
* En los codificadores, ahora se puede guardar o restablecer la
  configuración del codificador (incluyendo etiquetas de flujo) pulsando
  control+NVDA+c o control+NVDA+r tres veces, respectivamente.

## Versión 20.03

* El explorador de columnas ahora anunciará por defecto las diez primeras
  columnas (las instalaciones existentes continuarán usando los viejos slots
  de columna).
* Se ha eliminado la capacidad de anunciar automáticamente el nombre de la
  pista en reproducción desde lugares ajenos a Studio. Esta función,
  introducida en el complemento 5.6 como un parche para Studio 5.1x, ya no
  es útil. Los usuarios ahora deben recurrir a la orden del controlador de
  SPL y / o la capa del asistente para oír el título de la pista que se esté
  reproduciendo actualmente desde cualquier parte (C).
* Debido a la eliminación de la indicación automática del título de la pista
  en reproducción, el ajuste para configurar esta función también se ha
  eliminado de la categoría Ajustes / Indicación de estado del complemento.
* En los codificadores, NVDA reproducirá un tono de conexión cada medio
  segundo mientras el codificador se esté conectando.
* En los codificadores, NVDA verbalizará los mensajes de intento de conexión
  hasta que un codificador se conecte realmente. Antes, NVDA se detenía
  cuando se producía un error.
* Se ha añadido una nueva opción en los ajustes del codificador para
  permitir que NVDA anuncie los mensajes de conexión hasta que el
  codificador seleccionado se conecte. Esta opción viene activada por
  defecto.

## Versión 20.02

* Soporte inicial para el editor de listas de reproducción de
  StationPlaylist creator.
* Se han añadido las órdenes alt+NVDA+fila numérica para anunciar diversa
  información de estado en el editor de listas de reproducción. Esto incluye
  fecha y hora de la lista de reproducción (1), duración total de la lista
  de reproducción (2), para cuándo se ha programado la reproducción de la
  pista seleccionada (3), y rotación y categoría (4).
* Mientras una pista esté enfocada en Creator y Track Tool (exceptuando el
  editor de listas de reproducción de Creator), pulsar control+NVDA+guión
  mostrará los datos para todas las columnas en una ventana de modo
  exploración.
* Si NVDA reconoce un elemento de lista de pista con menos de 10 columnas,
  ya no anunciará encabezados de columnas inexistentes si se pulsa
  control+NVDA+fila numérica con columnas fuera de rango.
* En Creator, NVDA ya no anunciará información de columna si se pulsan las
  teclas control+NVDA+fila numérica mientras el foco se encuentre en lugares
  distintos a la lista de pistas.
* Cuando se esté reproduciendo una pista, NVDA ya no anunciará "No hay pista
  en reproducción" si se obtiene información sobre las pistas actual y
  siguiente mediante el asistente o el controlador de SPL.
* Si hay abierto un diálogo de opciones de alarma (introducción, salida o
  micrófono), NVDA ya no parecerá hacer nada ni reproducirá tonos de error
  si se intenta abrir una segunda instancia de cualquier diálogo de alarma.
* Al intentar alternar entre el perfil activo y un perfil instantáneo
  mediante el asistente de SPL (f12), NVDA presentará un mensaje si se
  pretende hacer con el diálogo de opciones del complemento abierto.
* En los codificadores, NVDA ya no olvidará aplicar el ajuste del tono que
  indica que no hay conexión al reiniciarlo.

## Versión 20.01

* Se requiere NVDA 2019.3 o posterior debido al uso extenso de Python 3.

## Versión 19.11.1/18.09.13-LTS

* Soporte inicial para StationPlaylist Suite 5.40.
* En Studio, las instantáneas de lista de reproducción (asistente de SPL,
  f8) y diversas órdenes de anuncio de tiempo, como la de tiempo restante
  (control+alt+T) ya no causarán que NVDA reproduzca tonos de error o
  parezca no hacer nada si se usa NVDA 2019.3 o posterior.
* En los elementos de lista de pistas de Creator, se reconoce adecuadamente
  la etiqueta "Language" añadida en la versión 5.31 y posteriores.
* En diversas listas de Creator aparte de la lista de pistas, NVDA ya no
  anunciará información de columnas defectuosa si se pulsa la orden
  control+NVDA+fila numérica.

## Versión 19.11

* La orden de estado del codificador del controlador de SPL (E) anunciará el
  estado de conexión del codificador activo configurado en vez de los
  codificadores monitorizados en segundo plano.
* NVDA ya no parecerá no hacer nada o reproducir tonos de error cuando se
  inicie mientras una ventana del codificador tenga el foco.

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

## Versiones antiguas

Por favor consulta el enlace changelog para notas de la versión para
versiones antiguas del complemento.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
