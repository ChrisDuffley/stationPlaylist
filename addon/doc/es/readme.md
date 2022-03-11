# StationPlaylist #

* Autores: Geoff Shang, Joseph Lee y otros colaboradores
* Descargar [Versión estable][1]
* Compatibilidad con NVDA: de 2021.3 en adelante

Este paquete de complementos proporciona una utilización mejorada de Station
Playlist Studio y otras aplicaciones de StationPlaylist, así como utilidades
para controlar Studio desde cualquier lugar. Entre las aplicaciones
soportadas se encuentran Studio, Creator, la herramienta de pista, VT
Recorder y Streamer, así como los codificadores SAM, SPL y AltaCast.

Para más información sobre este complemento, lee su [guía][2].

NOTAS IMPORTANTES:

* Este complemento requiere StationPlaylist Suite 5.30 o posterior.
* Si utilizas Windows 8 o posterior, para una mejor experiencia, deshabilita
  el modo atenuación de audio.
* A partir de 2018, los [registros de cambios para versiones antiguas][3] se
  encontrarán en GitHub. Este léeme del complemento listará cambios desde la
  versión 21.10 (2021) en adelante.
* Cuando Studio está en ejecución, se pueden guardar, restablecer o poner
  los valores de fábrica del complemento pulsando control+NVDA+c,
  control+NVDA+r una vez o control+NVDA+r tres veces, respectivamente. Esto
  también se aplica a los ajustes del codificador - se pueden guardar y
  restablecer (pero no recargar) los ajustes del codificador si se usan los
  codificadores.

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
* Alt+NVDA+1 (deslizamiento hacia la derecha con dos dedos en el modo SPL)
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
  Studio, Creator, Remote VT o Track Tool): se mueve a la siguiente o
  anterior columna de la pista.
* Control+Alt+inicio o fin (mientras se enfoca una pista en Studio, Creator,
  Remote VT o Track Tool): se mueve a la primera o última columna de la
  pista.
* Control+Alt+flecha abajo/arriba (mientras se enfoque una pista en Studio,
  Creator, Remote VT o la herramienta de pista): se mueve a la pista
  siguiente o anterior y anuncia columnas específicas.
* Control+NVDA+1 a 0 (mientras se enfoque una pista en Studio, Creator
  (incluyendo su editor de listas de reproducción), Remote VT o Track Tool):
  Anuncia el contenido de la columna especificada (primeras diez columnas
  por defecto). Pulsando este atajo dos veces mostrará la información de la
  columna en una ventana para modo navegación.
* Control+NVDA+- (guión cuando una pista tiene el foco en Studio, Creator,
  Remote VT o herramienta de pista): mostrar datos de todas las columnas de
  una pista en una ventana en modo exploración.
* NVDA+v cuando una pista tenga el foco (sólo en el visualizador de listas
  de reproducción de Studio): conmuta el anuncio de columnas de pista entre
  orden en pantalla y orden personalizado.
* Alt+NVDA+C mientras se enfoca una pista (sólo en el visor de listas de
  reproducción de Studio): anuncia los comentarios de pista si los hay.
* Alt+NVDA+0 desde la ventana Studio: abre el diálogo de configuración del
  complemento para Studio.
* Alt+NVDA+p desde la ventana de Studio: abre el diálogo de perfiles de
  emisión de Studio.
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

* F9: conecta el codificador seleccionado.
* F10 (sólo codificador SAM): Desconecta el codificador seleccionado.
* Control+f9: conecta todos los codificadores.
* Control+F10 (sólo codificador SAM): Desconecta todos los codificadores.
* F11: Activa o desactiva si NVDA cambiará a la ventana Studio para el
  codificador seleccionador si está conectado.
* Shift+F11: conmuta si Studio reproducirá la primera pista seleccionada
  cuando el codificador esté conectado a un servidor de streaming.
* Control+F11: Conmuta el monitoreo de fondo del codificador seleccionado.
* Control+F12: abre un diálogo para seleccionar el codificador que has
  eliminado (para realinear las etiquetas del codificador y las opciones del
  codificador).
* Alt+NVDA+0 y f12: abre el diálogo opciones del codificador para configurar
  ajustes tales como su etiqueta.

Además, las órdenes de revisión de columna están disponibles, incluyendo:

* Control+NVDA+1: posición del codificador.
* Control+NVDA+2: etiqueta de codificador.
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
* C (Shift+C en la distribución de JAWS): Título para la pista actualmente
  en reproducción.
* C (distribución de JAWS): conmuta el explorador de cart (visualizador de
  lista de reproducción sólo).
* D (R en distribución JAWS): duración restante para la lista de
  reproducción (si se da un mensaje de error, se mueve al visualizador de
  lista de reproducción y entonces emite esta orden).
* E: estado de metadatos del streaming.
* Shift+1 hasta Shift+4, Shift+0: estado para los metadatos individuales de
  la URL del streaming (0 es para el codificador DSP).
* F: busca pista (visualizador de lista de reproducción sólo).
* H: Duración de la música para el actual espacio de tiempo.
* Shift+H: duración restante de la pista o del slot horario.
* I (L en la distribución de JAWS): recuento de oyentes.
* K: se mueve a la pista marcada (sólo visualizador de lista de
  reproducción).
* Control+K: pone la pista actual como la pista marcada (sólo visualizador
  de lista de reproducción).
* L (Shift+L en la distribución de JAWS): línea auxiliar.
* M: Micrófono.
* N: Título para la siguiente pista programada.
* P: Estado de reproducción (reproduciendo o detenido).
* Shift+P: Tono de la pista actual.
* R (Shift+E en la disbribución de JAWS): Grabar en archivo
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

## SPL Controller

El SPL Controller es un conjunto de comandos de capas que puedes utilizar
para el control del SPL Studio desde cualquier lugar. Pulsa la orden de capa
del SPL Controller, y NVDA dirá, "SPL Controller." Pulsa otra orden para
controlar varias opciones del Studio tales como micrófono
activado/desactivado o reproducir la siguiente pista.

Las órdenes disponibles para el SPL Controller son:

* P: reproducir la siguiente pista seleccionada.
* U: pausar o reanudar la reproducción.
* S: detener la pista con desvanecimiento.
* T: parada instantánea.
* M: Activar micrófono.
* Shift+M: Desactivar micrófono.
* A: Activar automatización.
* Shift+A: Desactivar automatización.
* L: activar entrada de línea.
* Shift+L: desactivar línea de entrada.
* R: tiempo restante de la pista actual en reproducción.
* Shift+R: progreso del análisis de la biblioteca.
* C: título y duración de la pista actualmente en reproducción.
* Shift+C: título y duración de la siguiente pista, si la hay.
* E: Estado de conexión del codificador.
* I: recuento de oyentes.
* Q: información de estado de Studio, que incluye si una pista se está
  reproduciendo, el micrófono está encendido y demás.
* Teclas de cart (F1, Control+1, por ejemplo): reproducir carts asignados
  desde cualquier lugar.
* H: Ayuda de la capa.

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

## Anuncio de columnas de pista

Puedes pedir a NVDA que anuncie las columnas de pista del visualizador de
listas de reproducción de Studio en el orden en que aparecen en pantalla o
utilizar un orden personalizado y excluir ciertas columnas. Pulsa NVDA+v
para conmutar este comportamiento mientras el foco esté en una pista en el
visualizador de listas de reproducción de Studio. Para personalizar el orden
y la inclusión de las columnas, desde el panel de opciones de anuncio de
columna en las opciones del complemento, desmarca "Anunciar columnas en el
orden mostrado en pantalla" y personaliza las columnas incluidas y su orden.

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

## Versión 22.01

* Si se pasan argumentos de línea de órdenes del complemento al iniciar
  NVDA, como "--spl-configinmemory", NVDA ya no añadirá el parámetro
  específico cada vez que se carguen NVDA o Studio. Reinicia NVDA para
  restaurar la funcionalidad normal (sin argumentos de la línea de órdenes).

## Versión 21.11

* Soporte inicial para StationPlaylist Suite 6.0.

## Versión 21.10

* Se requiere NVDA 2021.2 o posterior a causa de cambios en NVDA que afectan
  a este complemento.

## Versiones antiguas

Por favor consulta el enlace changelog para notas de la versión para
versiones antiguas del complemento.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[3]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
