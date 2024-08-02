# StationPlaylist #

* Авторы: Christopher Duffley <nvda@chrisduffley.com> (прежде Joseph Lee
  <joseph.lee22590@gmail.com>, первоначально автор Geoff Shang и другие
  участники)
* Загрузить [стабильную версию][1]
* Совместимость с NVDA: 2023.3.3 и выше

Этот пакет дополнения обеспечивает улучшенное использование StationPlaylist
Studio и других приложений StationPlaylist, а также предоставляет утилиты
для управления Studio из любого места. Поддерживаемые приложения включают
Studio, Creator, Track Tool, VT Recorder и Streamer, а также кодеры SAM, SPL
и AltaCast.

Для получения подробной информации о дополнении прочтите [руководство по
дополнению][2].

ВАЖНЫЕ ПРИМЕЧАНИЯ:

* Для этого дополнения требуется StationPlaylist suite версии 5.40 или выше.
* Некоторые дополнительные функции будут отключены или ограничены, если NVDA
  запущена в защищённом режиме, например, на экране входа в систему.
* Для лучшего восприятия отключите режим приглушения аудио.
* Начиная с 2018 года, [списки изменений для старых версий дополнений][3]
  будут доступны на GitHub. В readme этого дополнения будут перечислены
  изменения, начиная с версии 23.02 (2023) и далее.
* Во время работы Studio вы можете сохранить, перезагрузить сохранённые
  настройки или сбросить настройки дополнения до значений по умолчанию,
  нажав Control+NVDA+C, Control+NVDA+R один раз или Control+NVDA+R три раза
  соответственно. Это также применимо к настройкам энкодера - вы можете
  сохранять и сбрасывать (не перезагружать) настройки энкодера, если
  используете энкодеры.
* Многие команды будут выводить речь, когда NVDA находится в режиме речи по
  требованию (NVDA 2024.1 и выше).

## Сочетания клавиш

Большинство из них будут работать только в Studio, если не указано
иное. Если не указано иное, эти команды поддерживают режим речи по
требованию.

* Alt+Shift+T из окна Studio: объявляет прошедшее время текущей
  воспроизводимой дорожки.
* Control+Alt+T (пролистать двумя пальцами вниз в сенсорном режиме SPL) из
  окна Studio: объявить оставшееся время воспроизводимой в данный момент
  дорожки.
* NVDA+Shift+F12 (two finger flick up in SPL touch mode) from Studio window:
  announces broadcaster time such as 5 minutes to top of the hour. Pressing
  this command twice will announce minutes and seconds till top of the hour.
* Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens
  alarms category in Studio add-on configuration dialog (does not support
  speak on demand).
* Alt+NVDA+1 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces scheduled time for the loaded playlist.
* Alt+NVDA+2 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces total playlist duration.
* Alt+NVDA+3 from Studio window: Toggles cart explorer to learn cart
  assignments (does not support speak on demand).
* Alt+NVDA+3 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces when the selected track is scheduled to play.
* Alt+NVDA+4 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces rotation and category associated with the loaded playlist.
* Control+NVDA+f из окна Studio: Открывает диалог поиска дорожки по
  исполнителю или названию песни. Нажмите NVDA+F3, чтобы перейти вперёд, или
  NVDA+Shift+F3, чтобы перейти назад (не поддерживается речь по требованию).
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
* Control+NVDA+1 through 0 (while focused on a track in Studio, Creator
  (including Playlist Editor), Remote VT, and Track Tool): Announce column
  content for a specified column (first ten columns by default). Pressing
  this command twice will display column information on a browse mode
  window.
* Control+NVDA+- (hyphen while focused on a track in Studio, Creator, Remote
  VT, and Track Tool): display data for all columns in a track on a browse
  mode window (does not support speak on demand).
* NVDA+V while focused on a track (Studio's playlist viewer only): toggles
  track column announcement between screen order and custom order (does not
  support speak on demand).
* Alt+NVDA+C while focused on a track (Studio's playlist viewer only):
  announces track comments if any.
* Alt+NVDA+0 из окна studio: Открывает диалог настройки дополнения Studio
  (не поддерживает речь по требованию).
* Alt+NVDA+P from Studio window: Opens the Studio broadcast profiles dialog
  (does not support speak on demand).
* Alt+NVDA+F1: Открыть диалог приветствия (не поддерживает речь по
  требованию).

## Неназначенные команды

Следующие команды по умолчанию не назначены; если вы хотите их назначить,
используйте диалог жестов ввода для добавления пользовательских команд. Для
этого в окне Studio откройте меню NVDA, Параметры, затем жесты
ввода. Разверните категорию StationPlaylist, затем найдите неназначенные
команды в списке ниже и выберите "Добавить", затем введите жест, который вы
хотите использовать.

Важно: некоторые из этих команд не будут работать, если NVDA запущен в
безопасном режиме, например, с экрана входа в систему. Не все команды
поддерживают режим речи по требованию.

* Переключение в окно SPL Studio из любой программы (недоступно в безопасном
  режиме, не поддерживает речь по требованию).
* Уровень панели управления SPL (недоступен в безопасном режиме).
* Объявление состояния студии, например, о воспроизведении дорожек из других
  программ (недоступно в безопасном режиме).
* Оповещение о состоянии подключения кодировщика из любой программы
  (недоступно в безопасном режиме).
* Уровень Помощника SPL для SPL Studio.
* Объявлять время в SPL Studio, включая секунды.
* Объявляет температуру.
* Объявлять название следующей дорожки, если она запланирована.
* Объявлять название проигрываемой в данный момент дорожки.
* Marking current track for start of track time analysis.
* Performing track time analysis.
* Take playlist snapshots.
* Поиск текста в определённых столбцах (не поддерживает речь по требованию).
* Искать дорожки с длительностью заданного диапазона с помощью функции
  поиска по времени (не поддерживает речь по требованию).
* Быстрое включение или отключение потоковой передачи метаданных (не
  поддерживает речь по требованию).

## Дополнительные команды при использовании кодировщиков

При использовании кодировщиков доступны следующие команды, а те, которые
используются для переключения параметров поведения при подключении, таких
как фокус на Studio, воспроизведение первой дорожки и переключение фонового
мониторинга, могут быть назначены в диалоге жестов ввода в меню NVDA,
Параметры, жесты ввода, в категории StationPlaylist. Эти команды не
поддерживают речь по требованию.

* F9: подключить выбранный кодировщик.
* F10 (только кодировщик SAM): Отключить выбранный кодировщик.
* Control+F9: Подключить все кодировщики.
* Control+F10 (только кодировщик SAM): Отключить все кодировщики.
* Control+Shift+F11: Toggles whether NVDA will switch to Studio window for
  the selected encoder if connected.
* Shift+F11: Toggles whether Studio will play the first selected track when
  encoder is connected to a streaming server.
* Control+F11: Toggles background monitoring of the selected encoder.
* Control+F12: opens a dialog to select the encoder you have deleted (to
  realign encoder labels and settings).
* Alt+NVDA+0 or F12: Opens encoder settings dialog to configure options such
  as encoder label.

Кроме того, доступны команды просмотра столбцов, в том числе (поддержка речи
по требованию):

* Control+NVDA+1: Положение кодировщика.
* Control+NVDA+2: метка кодировщика.
* Control+NVDA+3 от SAM-кодировщика: Формат кодировщика.
* Control+NVDA+3 from SPL and AltaCast Encoder: Encoder settings.
* Control+NVDA+4 from SAM Encoder: Encoder connection status.
* Control+NVDA+4 from SPL and AltaCast Encoder: Transfer rate or connection
  status.
* Control+NVDA+5 from SAM Encoder: Connection status description.

## Уровень Помощника SPL

Набор команд этого уровня позволяет вам получать различные состояния в SPL
Studio, такие как, воспроизводится ли дорожка, общая продолжительность всех
дорожек в течение часа и так далее. В любом окне SPL Studio нажмите команду
уровня помощника SPL, затем нажмите одну из клавиш из списка ниже (одна или
несколько команд доступны только для просмотра списков воспроизведения). Вы
также можете настроить NVDA на эмуляцию команд из других программ для чтения
с экрана.

Доступны следующие команды (большинство команд поддерживают речь по
требованию):

* A: Автоматизация.
* C (Shift+C в раскладке JAWS): Название проигрываемой в данный момент
  дорожки.
* C (JAWS layout): Toggle cart explorer (playlist viewer only, does not
  support speak on demand).
* D (R in JAWS layout): Remaining duration for the playlist (if an error
  message is given, move to playlist viewer and then issue this command).
* E: Metadata streaming status.
* Shift+1 through Shift+4, Shift+0: Status for individual metadata streaming
  URL's (0 is for DSP encoder).
* F: Find track (playlist viewer only, does not support speak on demand).
* H: Duration of music for the current hour slot.
* Shift+H: Remaining track duration for the hour slot.
* I (L в раскладке JAWS): Количество слушателей.
* K: Move to the marked track (playlist viewer only).
* Control+K: Set the current track as the place marker track (playlist
  viewer only).
* L (Shift+L в раскладке JAWS): Линейный вход.
* M: Микрофон.
* N: Название следующей запланированной дорожки.
* P: Состояние воспроизведения (играет или остановлено).
* Shift+P: Высота текущей дорожки.
* R (Shift+E в раскладке JAWS): Запись в файл включена/отключена.
* Shift+R: Monitor library scan in progress.
* S: Track starts (scheduled).
* Shift+S: Time until selected track will play (track starts in).
* T: Cart edit/insert mode on/off.
* U: Время работы Studio.
* W: Погода и температура, если настроено.
* Y: Playlist modified status.
* F8: Take playlist snapshots (number of tracks, longest track, etc.).
* Shift+F8: Request playlist transcripts in numerous formats.
* F9: Mark current track for start of playlist analysis (playlist viewer
  only).
* F10: Perform track time analysis (playlist viewer only).
* F12: Switch between current and a predefined profile.
* F1: Справка по уровню.

## Панель управления SPL

Панель управления SPL - это набор многоуровневых команд, которые вы можете
использовать для управления SPL Studio в любом месте. Нажмите команду уровня
панели управления SPL, и NVDA выдаст сообщение "Панель управления
SPL". Нажмите другую команду для управления различными студийными
настройками, такими как включение/ выключение микрофона или воспроизведение
следующего трека.

Важно: команды уровня панели управления SPL отключены, если NVDA запущен в
защищенном режиме.

Доступны следующие команды панели управления SPL (некоторые команды
поддерживают речь по требованию):

* P: Воспроизвести следующую выбранную дорожку.
* U: Приостановить или возобновить воспроизведение.
* S: Остановить дорожку с затуханием.
* T: Мгновенная остановка.
* M: Включить микрофон.
* Shift+M: Выключить микрофон.
* A: Включить автоматику.
* Shift+A: Отключить автоматику.
* L: Turn on line-in input.
* Shift+L: Turn off line-in input.
* R: Remaining time for the currently playing track.
* Shift+R: Library scan progress.
* C: Title and duration of the currently playing track (supports speak on
  demand).
* Shift+C: Title and duration of the upcoming track if any (supports speak
  on demand).
* E: Encoder connection status (supports speak on demand).
* I: Количество слушателей (поддерживает речь по требованию).
* Q: Информация о состоянии студии, например, воспроизводится ли дорожка,
  включен ли микрофон и другие данные (поддерживается речь по требованию).
* Cart keys (F1, Control+1, for example): Play assigned carts from anywhere.
* H: Справка по уровню.

## Сигнализация дорожки и микрофона

По умолчанию NVDA воспроизводит звуковой сигнал, если до конца дорожки
(окончание) и/или вступления осталось пять секунд, а также если микрофон был
активен в течение некоторого времени. Чтобы настроить звуковые сигналы
дорожки и микрофона, нажмите Alt+NVDA+1, чтобы открыть настройки звуковых
сигналов на экране настроек дополнения Studio. Вы также можете использовать
этот экран для настройки того, будет ли слышен звуковой сигнал, сообщение
или и то, и другое вместе при включении звуковых сигналов.

## Поисковик Дорожек

Если вы хотите быстро найти песню по исполнителю или по названию песни в
списке композиций, нажмите Control+NVDA+F. Введите или выберите имя
исполнителя или название песни. NVDA либо направит вас к нужной песне, если
она будет найдена, либо выдаст сообщение об ошибке, если не удастся найти
нужную песню. Чтобы найти ранее введенную песню или исполнителя, нажмите
NVDA+F3 или NVDA+Shift+F3, чтобы перейти вперед или назад.

Примечание: Функция поиска дорожек чувствительна к регистру.

## Cart Explorer

Depending on edition, SPL Studio allows up to 96 carts to be assigned for
playback. NVDA allows you to hear which cart, or jingle is assigned to these
commands.

To learn cart assignments, from SPL Studio, press Alt+NVDA+3. Pressing the
cart command once will tell you which jingle is assigned to the
command. Pressing the cart command twice will play the jingle. Press
Alt+NVDA+3 to exit cart explorer. See the add-on guide for more information
on cart explorer.

## Track time analysis

To obtain length to play selected tracks, mark current track for start of
track time analysis (SPL Assistant, F9), then press SPL Assistant, F10 when
reaching end of selection.

## Columns Explorer

By pressing Control+NVDA+1 through 0, you can obtain contents of specific
columns. By default, these are first ten columns for a track item (in
Studio: artist, title, duration, intro, outro, category, year, album, genre,
mood). For playlist editor in Creator and Remote VT client, column data
depends on column order as shown on screen. In Studio, Creator's main track
list, and Track Tool, column slots are preset regardless of column order on
screen and can be configured from add-on settings dialog under columns
explorer category.

## Track column announcement

You can ask NVDA to announce track columns found in Studio's playlist viewer
in the order it appears on screen or using a custom order and/or exclude
certain columns. Press NVDA+V to toggle this behavior while focused on a
track in Studio's playlist viewer. To customize column inclusion and order,
from column announcement settings panel in add-on settings, uncheck
"Announce columns in the order shown on screen" and then customize included
columns and/or column order.

## Playlist snapshots

You can press SPL Assistant, F8 while focused on a playlist in Studio to
obtain various statistics about a playlist, including number of tracks in
the playlist, longest track, top artists and so on. After assigning a custom
command for this feature, pressing the custom command twice will cause NVDA
to present playlist snapshot information as a webpage so you can use browse
mode to navigate (press escape to close).

## Playlist Transcripts

Pressing SPL Assistant, Shift+F8 will present a dialog to let you request
playlist transcripts in numerous formats, including in a plain text format,
an HTML table or a list.

## Диалог настройки

В окне studio вы можете нажать Alt+NVDA+0, чтобы открыть диалог настройки
дополнения. В качестве альтернативы, перейдите в меню параметров NVDA и
выберите пункт Настройки SPL Studio. Не все настройки доступны, если NVDA
запущен в безопасном режиме.

## Broadcast profiles dialog

You can save settings for specific shows into broadcast profiles. These
profiles can be managed via SPL broadcast profiles dialog which can be
accessed by pressing Alt+NVDA+P from Studio window.

## Сенсорный режим SPL

Если вы используете Studio на компьютере с сенсорным экраном и установленной
NVDA, вы можете выполнять некоторые команды Studio с сенсорного
экрана. Сначала коснитесь тремя пальцами, чтобы переключиться в режим SPL,
затем используйте сенсорные команды, перечисленные выше, для выполнения
команд.

## Версия 24.03

* Совместимо с NVDA 2024.1.
* Требуется NVDA 2023.3.3 или выше.
* Поддержка пакета StationPlaylist suite 6.10.
* Большинство команд поддерживают речь по требованию (NVDA 2024.1), поэтому
  объявления можно озвучивать в этом режиме.

## Версия 24.01

* Команды диалога настроек кодировщика для использования с кодировщиками SPL
  и SAM теперь доступны для назначения, что означает, что вы можете изменить
  их по умолчанию в категории StationPlaylist в меню NVDA > Настройки >
  Жесты ввода. Команды, которые нельзя назначить, - это команды подключения
  и отключения. Кроме того, чтобы предотвратить конфликты команд и упростить
  использование этой команды на удалённых серверах, жест по умолчанию для
  переключения в Studio после подключения теперь Control+Shift+F11 (ранее
  просто F11). Всё это, конечно, по-прежнему можно переключать в диалоге
  настроек кодировщика (NVDA+Alt+0 или F12).

## Версия 23.05

* Чтобы отразить смену сопровождающего, манифест был обновлён и указан как
  таковой.

## Версия 23.02

* Требуется NVDA 2022.4 или выше.
* Требуется Windows 10 21H2 (обновление от ноября 2021 года/сборка 19044)
  или выше.
* В программе просмотра плейлистов Studio NVDA не будет объявлять заголовки
  столбцов, такие как исполнитель и название, если для параметра заголовки
  таблиц установлено значение "строки и столбцы" или "столбцы" на панели
  настроек форматирования документов NVDA.

## Старые выпуски

Пожалуйста, ознакомьтесь с [списком изменений][3] для получения информации о
старых выпусках дополнения.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=stationPlaylist

[2]: https://github.com/chrisDuffley/stationplaylist/wiki/SPLAddonGuide

[3]: https://github.com/ChrisDuffley/stationplaylist/wiki/splchangelog
