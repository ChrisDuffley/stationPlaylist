# StationPlaylist #

* Auteurs: Geoff Shang, Joseph Lee et d'autres contributeurs.
* Télécharger [version stable][1]
* Télécharger [la version de développement][2]
* NVDA compatibility: 2019.3 to 2020.1

This add-on package provides improved usage of StationPlaylist Studio and
other StationPlaylist apps, as well as providing utilities to control Studio
from anywhere. Supported apps include Studio, Creator, Track Tool, VT
Recorder, and Streamer, as well as SAM, SPL, and AltaCast encoders.

For more information about the add-on, read the [add-on guide][4]. For
developers seeking to know how to build the add-on, see
buildInstructions.txt located at the root of the add-on source code
repository.

NOTES IMPORTANTES :

* This add-on requires StationPlaylist suite 5.20 or later.
* Si vous utilisez Windows 8 ou ultérieur, pour une meilleure expérience,
  désactiver le Mode d'atténuation audio.
* Starting from 2018, [changelogs for old add-on releases][5] will be found
  on GitHub. This add-on readme will list changes from version 18.09 (2018
  onwards).
* Certaines fonctionnalités de l'extension ne fonctionneront pas dans
  certaines conditions, notamment l'exécution de NVDA en mode sécurisé.
* En raison de limitations techniques, vous ne pouvez pas installer ou
  utiliser cette extension sur la version Windows Store de NVDA.
* Les fonctionnalités marquées comme "expérimental" servent à tester quelque
  chose avant une publication plus vaste, elles ne seront donc pas activées
  dans les versions stables.
* While Studio is running, you can save, reload saved settings, or reset
  add-on settings to defaults by pressing Control+NVDA+C, Control+NVDA+R
  once, or Control+NVDA+R three times, respectively. This is also applicable
  to encoder settings - you can save and reset (not reload) encoder settings
  if using encoders.

## Raccourcis clavier

La plupart d'entre eux fonctionneront dans Studio uniquement sauf indication
contraire.

* Alt+Maj+T depuis la fenêtre de Studio : annonce le temps écoulé pour la
  piste en cours de lecture.
* Contrôle+Alt+T (glissement à deux doigts vers le bas en mode tactile SPL)
  depuis la fenêtre de Studio : annoncer le temps restant pour la piste en
  cours de lecture.
* NVDA+Maj+F12 (glissement à deux doigts vers le haut en mode tactile SPL)
  depuis la fenêtre de Studio: annonce le temps de diffusion tel que 5
  minutes en haut de l'heure. Appuyez deux fois sur cette commande pour
  annoncer les minutes et les secondes jusqu'au début de l'heure.
* Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens
  alarms category in Studio add-on configuration dialog.
* Alt+NVDA+1 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces scheduled time for the loaded playlist.
* Alt+NVDA+2 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces total playlist duration.
* Alt+NVDA+3 depuis la fenêtre de Studio : Basculer l'explorateur de chariot
  pour apprendre les assignations de chariot.
* Alt+NVDA+3 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces when the selected track is scheduled to play.
* Alt+NVDA+4 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces rotation and category associated with the loaded playlist.
* Control+NVDA+f from Studio window: Opens a dialog to find a track based on
  artist or song name. Press NVDA+F3 to find forward or NVDA+Shift+F3 to
  find backward.
* Alt+NVDA+R depuis la fenêtre de Studio : parcourt les paramètres d'annonce
  du balayage dans la bibliothèque.
* Contrôle+Maj+X depuis la fenêtre de Studio : Parcourt les paramètres du
  minuteur braille.
* Control+Alt+left/right arrow (while focused on a track in Studio, Creator,
  Remote VT, and Track Tool): Announce previous/next track column.
* Control+Alt+Home/End (while focused on a track in Studio, Creator, Remote
  VT, and Track Tool): Announce first/last track column.
* Control+Alt+up/down arrow (while focused on a track in Studio only): Move
  to previous or next track and announce specific columns.
* Control+NVDA+1 through 0 (while focused on a track in Studio, Creator
  (including Playlist Editor), Remote VT, and Track Tool): Announce column
  content for a specified column (first ten columns by default). Pressing
  this command twice will display column information on a browse mode
  window.
* Control+NVDA+- (hyphen while focused on a track in Studio, Creator, and
  Track Tool): display data for all columns in a track on a browse mode
  window.
* Alt+NVDA+C alors que  a été mis en focus sur une piste (Studio
  uniquement): annonce les commentaires de piste le cas échéant.
* Alt+NVDA+0 depuis la fenêtre de Studio : Ouvre le dialogue de
  configuration de l'extension Studio.
* Alt+NVDA+P from Studio window: Opens the Studio broadcast profiles dialog.
* Alt+NVDA+- (tiret) depuis la fenêtre de Studio : Envoyez vos commentaires
  au développeur de l'extension en utilisant le client de messagerie par
  défaut.
* Alt+NVDA+F1: Ouvre le dialogue de bienvenue.

## Commandes non assignées

The following commands are not assigned by default; if you wish to assign
them, use Input Gestures dialog to add custom commands. To do so, from
Studio window, open NVDA menu, Preferences, then Input Gestures. Expand
StationPlaylist category, then locate unassigned commands from the list
below and select "Add", then type the gesutre you wish to use.

* Basculement vers la fenêtre SPL Studio depuis n'importe quel programme.
* Couche Contrôleur SPL.
* Annonçant le statut de Studio, comme la lecture de pistes à partir
  d'autres programmes.
* Announcing encoder connection status from any program.
* Couche Assistant SPL depuis SPL Studio.
* Annoncer le temps y compris les secondes depuis SPL Studio.
* Annonce de la température.
* Annonce du titre de la piste suivante si planifié.
* Annonçant le titre de la piste en cours de lecture.
* Marquage de piste en cours pour le début de l'analyse de durée de piste.
* Effectuer des analyses de durée de piste.
* Prendre des instantanés de playlist
* Recherche de texte dans des colonnes spécifiques.
* Trouver des piste avec une durée qui se situe dans un intervalle donné via
  la recherche de l'intervalle de temps.
* Activer ou désactiver les métadonnées en streaming rapidement.

## Additional commands when using encoders

The following commands are available when using encoders:

* F9 : Se connecter à un serveur de streaming.
* F10 (Encodeur SAM uniquement) : Se déconnecter d'un serveur de streaming.
* Contrôle+F9/Contrôle+F10 (encodeur SAM uniquement) : Connecter ou
  déconnecter tous les encodeurs, respectivement.
* F11 : Détermine si NVDA bascule vers la fenêtre Studio pour l'encodeur
  sélectionné  si connecté.
* Maj+F11: Détermine si Studio lit la première piste sélectionnée lorsque
  l'encodeur est connecté à un serveur de streaming.
* Contrôle+F11 : Active ou désactive le contrôle en arrière-plan de
  l'encodeur sélectionné.
* F12 :: Ouvre un dialogue de saisie d'une étiquette personnalisée pour le
  flux ou l'encodeur sélectionné.
* Contrôle+F12 : Ouvre un dialogue pour sélectionner l'encodeur que vous
  avez supprimé (afin de réaligner les étiquettes de flux et les paramètres
  de l'encodeur).
* Alt+NVDA+0 : Ouvre la boîte de dialogue paramètres  de l'encodeur pour
  configurer des options telles que l'étiquette de flux.

De plus, les commandes pour visualiser la colonne sont disponibles, y
compris :

* Contrôle+NVDA+1 : Position de l'encodeur.
* Contrôle+NVDA+2 : étiquette de flux.
* Contrôle+NVDA+3 depuis l'Encodeur SAM : Format de l'Encodeur.
* Control+NVDA+3 from SPL and AltaCast Encoder: Encoder settings.
* Control+NVDA+4 from SAM Encoder: Encoder connection status.
* Control+NVDA+4 from SPL and AltaCast Encoder: Transfer rate or connection
  status.
* Contrôle+NVDA+5 depuis l'Encodeur SAM : Description du statut de la
  connexion.

## Couche Assistant SPL

This layer command set allows you to obtain various status on SPL Studio,
such as whether a track is playing, total duration of all tracks for the
hour and so on. From any SPL Studio window, press the SPL Assistant layer
command, then press one of the keys from the list below (one or more
commands are exclusive to playlist viewer). You can also configure NVDA to
emulate commands from other screen readers.

Les commandes disponibles sont :

* A : Automatisation.
* C (Shift+C in JAWS layout): Title for the currently playing track.
* C (JAWS layout): Toggle cart explorer (playlist viewer only).
* D (R dans la disposition de JAWS) : Durée restante pour la playlist (si un
  message d’erreur est donné, se déplacer vers la visionneuse de playlist et
  puis tapez cette commande).
* E: Metadata streaming status.
* Maj+1 jusqu'à maj+4, maj+0 : Statut de Métadonnées individuelles en
  streaming URLs (0 est pour l'encodeur DSP).
* F : Recherche de piste (visionneuse de playlist uniquement).
* H : Durée de la musique pour la tranche horaire en cours.
* Maj+H : Durée des pistes restantes pour la tranche horaire.
* I (L in JAWS layout): Listener count.
* K : Se déplacer à la piste marquée (visionneuse de playlist uniquement).
* Contrôle+K : Définir la piste en cours comme le marqueur de position de
  piste (visionneuse de playlist uniquement).
* L (Shift+L in JAWS layout): Line in.
* M : Microphone.
* N : Titre pour la piste suivante planifié.
* P : Statut (en cours de lecture ou arrêté).
* Maj+P : Hauteur de la piste actuelle.
* R (Shift+E in JAWS layout): Record to file enabled/disabled.
* Maj+R : Contrôle du balayage de la bibliothèque en cours.
* S : Piste débute (planifié).
* Maj+S : Durée jusqu'à la piste sélectionnée qui va être jouer (piste
  débute dans).
* T : Mode édition/insertion chariot activé/désactivé.
* U: temps de fonctionnement Studio.
* W: Météo et température si configurée.
* Y: Statut de la modification de la playlist.
* F8 : Prendre des instantanés de playlist (nombre de pistes, piste la plus
  longue, etc.).
* Maj+F8 : Demander des transcriptions de playlist dans de nombreux formats.
* F9 : Marquer la piste en cours pour le début de l'analyse de playlist
  (visionneuse de playlist uniquement).
* F10 : Effectuer une analyse de durée de piste (visionneuse de playlist
  uniquement).
* F12 : basculer entre un profil en cours et un profil prédéfini.
* F1: Aide couche.
* Maj+F1 : Ouvre le guide de l'utilisateur en ligne.

## Contrôleur SPL

Le contrôleur SPL est un ensemble de commandes couches que vous pouvez
utiliser pour contrôler SPL Studio de n'importe où. Appuyez sur la commandes
couche Contrôleur SPL, et NVDA dira, "Contrôleur SPL." Appuyez sur une autre
commande pour contrôler divers paramètres Studio comme activer/désactiver un
microphone ou lire la piste suivante.

Les commandes disponibles pour le Contrôleur SPL sont:

* Appuyez sur P pour lire la suivante piste sélectionnée.
* Appuyez sur U pour mettre en pause ou pour reprendre la lecture.
* Appuyer sur S pour arrêter la piste avec fondu enchaîné, ou pour arrêter
  la piste instantanément, appuyez sur T.
* Appuyer sur M ou Maj+M pour activer ou désactiver le microphone,
  respectivement, ou appuyez sur N pour activer le microphone sans fondu.
* Appuyer sur A pour activer l'automatisation ou Maj+A pour désactiver
  celle-ci.
* Appuyer sur L pour activer l'entrée ligne ou Maj+L pour désactiver
  celle-ci.
* Appuyez sur R pour entendre le temps restant pour la piste en cours de
  lecture.
* Appuyez sur Maj+R pour obtenir un rapport sur  l'avancement du balayage de
  la bibliothèque.
* Appuyez sur C pour laisser NVDA annoncer le nom et la durée de la piste en
  cours de lecture.
* Appuyez sur Maj+C pour laisser NVDA annoncer le nom et la durée de la
  prochaine piste, le cas échéant.
* Press E to hear which encoders are connected.
* Appuyez sur I pour obtenir le nombre d'auditeurs.
* Appuyer sur Q pour obtenir diverses informations du statut de Studio, y
  compris si une piste est en cours de lecture, le microphone est activé et
  d'autres.
* Appuyez sur les touches de chariot (F1, Contrôle+1, par exemple) pour lire
  les chariots assignés à partir de n'importe où.
* Appuyez sur H pour afficher un dialogue d'aide répertoriant les commandes
  disponibles.

## Track and microphone alarms

By default, NVDA will play a beep if five seconds are left in the track
(outro) and/or intro, as well as to hear a beep if microphone has been
active for a while. To configure track and microphone alarms, press
Alt+NVDA+1 to open alarms settings in Studio add-on settings screen. You can
also use this screen to configure if you'll hear a beep, a message or both
when alarms are turned on.

## Chercheur de piste

Si vous souhaitez trouver rapidement une chanson par artiste ou par nom de
chanson, depuis la liste de piste, appuyez sur Contrôle+NVDA+F. Tapez le nom
de l'artiste ou le nom de la chanson. NVDA va vous placer soit à la chanson
Si cell-ci est trouvé ou il affichera une erreur si elle ne trouve pas la
chanson que vous recherchez. Pour trouver une chanson ou un artiste
précédemment entrée, appuyez sur NVDA+F3 ou NVDA+Maj+F3 Pour trouver en
avant ou en arrière.

Remarque: le Chercheur de piste est sensible à la casse.

## Explorateur de Chariot

Selon l'édition, SPL Studio permet d'assigné jusq'à 96 chariots pendant la
lecture. NVDA vous permet d'entendre quel chariot ou jingle est assigné à
ces commandes.

To learn cart assignments, from SPL Studio, press Alt+NVDA+3. Pressing the
cart command once will tell you which jingle is assigned to the
command. Pressing the cart command twice will play the jingle. Press
Alt+NVDA+3 to exit cart explorer. See the add-on guide for more information
on cart explorer.

## Analyse de durée de piste

Pour obtenir la longueur pour jouer les pistes sélectionnés, marquer la
piste en cours pour le début de l'analyse de durée de piste (Assistant SPL,
F9), puis appuyer sur Assistant SPL, F10 lorsque vous atteignez la fin de la
sélection.

## Explorateur de Colonnes

By pressing Control+NVDA+1 through 0, you can obtain contents of specific
columns. By default, these are first ten columns for a track item (in
Studio: artist, title, duration, intro, outro, category, year, album, genre,
mood). For playlist editor in Creator and Remote VT client, column data
depends on column order as shown on screen. In Studio, Creator's main track
list, and Track Tool, column slots are preset regardless of column order on
screen and can be configured from add-on settings dialog under columns
explorer category.

## Instantanés de playlist

Vous pouvez appuyer sur Assistant SPL , F8 étant focalisée sur une playlist
dans Studio pour obtenir diverses statistiques sur une playlist, y compris
le nombre de pistes dans la playlist, la piste la plus longue, les meilleurs
artistes et ainsi de suite.

## Transcriptions de Playlist

En appuyant sur Assistant SPL, Maj+F8 présentera une boîte de dialogue pour
vous permettre de demander des transcriptions de playlist dans de nombreux
formats, y compris dans un format de texte brut, un tableau HTML ou une
liste.

## Boîte de dialogue configuration

Depuis la fenêtre studio, vous pouvez appuyer sur Alt+NVDA+0 pour ouvrir la
boîte de dialogue configuration de l'extension. Sinon, allez dans le menu
préférences de NVDA et sélectionnez l'élément Paramètres SPL Studio. Cette
boîte de dialogue est également utilisé pour gérer les profils de diffusion.

## Broadcast profiles dialog

You can save settings for specific shows into broadcast profiles. These
profiles can be managed via SPL broadcast profiles dialog which can be
accessed by pressing Alt+NVDA+P from Studio window.

## Mode tactile SPL

Si vous utilisez Studio sur un ordinateur possédant un écran tactile
fonctionnant sous Windows 8 ou version ultérieure et NVDA 2012.3 ou version
ultérieure installé, vous pouvez exécuter certaines commandes Studio depuis
un écran tactile. Tout d'abord utiliser une tape à trois doigts pour
basculer en mode SPL, puis utilisez les commandes tactile énumérées
ci-dessus pour exécuter des commandes.

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.
* Fixed many instances of encoders support feature messages spoken in
  English despite translated into other languages.
* Time-based broadcast profiles feature has been removed.
* Window-Eyes command layout for SPL Assistant has been removed. Window-Eyes
  command layout users will be migrated to NVDA layout.
* As audio ducking feature in NVDA does not impact streaming from Studio
  except for specific hardware setups, audio ducking reminder dialog has
  been removed.
* When errors are found in encoder settings, it is no longer necessary to
  switch to Studio window to let NVDA reset settings to defaults. You must
  now switch to an encoder from encoders window to let NVDA reset encoder
  settings.
* The title of encoder settings dialog for SAM encoders now displays encoder
  format rather than encoder position.

## Version 20.05

* Initial support for Remote VT (voice track) client, including remote
  playlist editor with same commands as Creator's playlist editor.
* Commands used to open separate alarm settings dialogs (Alt+NVDA+1,
  Alt+NVDA+2, Alt+NVDA+4) has been combined into Alt+NvDA+1 and will now
  open alarms settings in SPL add-on settings screen where track outro/intro
  and microphone alarm settings can be found.
* In triggers dialog found in broadcast profiles dialog, removed the user
  interface associated with time-based broadcast profiles feature such as
  profile switch day/time/duration fields.
* Profile switch countdown setting found in broadcast profiles dialog has
  been removed.
* As Window-Eyes is no longer supported by Vispero since 2017, SPL Assistant
  command layout for Window-Eyes is deprecated and will be removed in a
  future add-on release. A warning will be shown at startup urging users to
  change SPL Assistant command layout to NVDA (default) or JAWS.
* When using Columns Explorer slots (Control+NvDA+number row commands) or
  column navigation commands (Control+Alt+home/end/left arrow/right arrow)
  in Creator and Remote VT client, NVDA will no longer announce wrong column
  data after changing column position on screen via mouse.
* In encoders and Streamer, NVDA will no longer appear to do nothing or play
  error tones when exiting NVDA while focused on something other than
  encoders list without moving focus to encoders first.

## Version 20.04

* Time-based broadcast profiles feature is deprecated. A warning message
  will be shown when first starting Studio after installing add-on 20.04 if
  you have defined one or more time-based broadcast profiles.
* Broadcast profiles management has been split from SPL add-on settings
  dialog into its own dialog. You can access broadcast profiles dialog by
  pressing Alt+NVDA+P from Studio window.
* Due to duplication with Control+NVDA+number row commands for Studio
  tracks, columns explorer commands from SPL Assistant (number row) has been
  removed.
* Changed error message shown when trying to open a Studio add-on settings
  dialog (such as metadata streaming dialog) while another settings dialog
  (such as end of track alarm dialog) is active. The new error message is
  same as the message shown when trying to open multiple NVDA settings
  dialogs.
* NVDA will no longer play error tones or appear to do nothing when clicking
  OK button from Columns Explorer dialog after configuring column slots.
* In encoders, you can now save and reset encoder settings (including stream
  labels) by pressing Control+NVDA+C or Control+NVDA+R three times,
  respectively.

## Version 20.03

* Columns Explorer will now announce first ten columns by default (existing
  installations will continue to use old column slots).
* The ability to announce name of the playing track automatically from
  places other than Studio has been removed. This feature, introduced in
  add-on 5.6 as a workaround for Studio 5.1x, is no longer functional. Users
  must now use SPL Controller and/or Assistant layer command to hear title
  of the currently playing track from everywhere (C).
* Due to removal of automatic announcement of playing track title, the
  setting to configure this feature has been removed from add-on
  settings/status announcement category.
* In encoders, NvDA will play connection tone every half a second while an
  encoder is connecting.
* In encoders, NVDA will now announce connection attempt messages until an
  encoder is actually connected. Previously NVDA stopped when an error was
  encountered.
* A new setting has been added to encoder settings to let NvDA announce
  connection messages until the selected encoder is connected. This setting
  is enabled by default.

## Version 20.02

* Initial support for StationPlaylist Creator's Playlist Editor.
* Added Alt+NVDA+number row commands to announce various status information
  in Playlist Editor. These include date and time for the playlist (1),
  total playlist duration (2), when the selected track is scheduled to play
  (3), and rotation and category (4).
* While focused on a track in Creator and Track Tool (except in Creator's
  Playlist Editor), pressing Control+NVDA+Dash will display data for all
  columns on a browse mode window.
* If NVDA Recognizes a track list item with less than 10 columns, NVDA will
  no longer announce headers for nonexistent columns if Control+NVDA+number
  row for out of range column is pressed.
* In creator, NVDA will no longer announce column information if
  Control+NVDA+number row keys are pressed while focused on places other
  than track list.
* When a track is playing, NVDA will no longer announce "no track is
  playing" if obtaining information about current and next tracks via SPL
  Assistant or SPL Controller.
* If an alarm options dialog (intro, outro, microphone) is open, NVDA will
  no longer appear to do nothing or play error tone if attempting to open a
  second instance of any alarm dialog.
* When trying to switch between active profile and an instant profile via
  SPL Assistant (F12), NVDA will present a message if attempting to do so
  while add-on settings screen is open.
* In encoders, NVDA will no longer forget to apply no connection tone
  setting for encoders when NVDA is restarted.

## Version 20.01

* NVDA 2019.3 or later is required due to extensive use of Python 3.

## Version 19.11.1/18.09.13-LTS

* Initial support for StationPlaylist suite 5.40.
* In Studio, playlist snapshots (SPL Assistant, F8) and various time
  announcement commands such as remaining time (Control+Alt+T) will no
  longer cause NVDA to play error tones or do nothing if using NVDA 2019.3
  or later.
* In Creator's track list items, "Language" column added in Creator 5.31 and
  later is properly recognized.
* In various lists in Creator apart from track list, NVDA will no longer
  announce odd column information if Control+NVDA+number row command is
  pressed.

## Version 19.11

* Encoder status command from SPL Controller (E) will announce connection
  status for the active encoder set instead of encoders being monitored in
  the background.
* NVDA will no longer appear to do nothing or play error tones when it
  starts while an encoder window is focused.

## Version 19.10/18.09.12-LTS

* Shortened the version announcement message for Studio when it starts.
* Version information for Creator will be announced when it starts.
* 19.10: custom command can be assigned for encoder status command from SPL
  Controller (E) so it can be used from everywhere.
* Initial support for AltaCast encoder (Winamp plugin and must be recognized
  by Studio). Commands are same as SPL Encoder.

## Version 19.08.1

* In SAM encoders, NVDA will no longer appear to do nothing or play error
  tones if an encoder entry is deleted while being monitored in the
  background.

## Version 19.08/18.09.11-LTS

* 19.08: NVDA 2019.1 or later is required.
* 19.08: NVDA will no longer appear to do nothing or play error tones when
  restarting it while Studio add-on settings dialog is open.
* NVDA will remember profile-specific setttings when switching between
  settings panels even after renaming the currently selected broadcast
  profile from add-on settings.
* NVDA will no longer forget to honor changes to time-based profiles when OK
  button is pressed to close add-on settings. This bug has been present
  since migrating to multi-page settings in 2018.

## Version 19.07/18.09.10-LTS

* Renamed the add-on from "StationPlaylist Studio" to "StationPlaylist" to
  better describe apps and features supported by this add-on.
* Améliorations de la sécurité interne.
* If microphone alarm or metadata streaming settings are changed from add-on
  settings, NVDA will no longer fail to apply changed settings. This
  resolves an issue where microphone alarm did not start or stop properly
  after changing settings via add-on settings.

## Version 19.06/18.09.9-LTS

Version 19.06 supports SPL Studio 5.20 and later.

* Initial support for StationPlaylist Streamer.
* While running various Studio apps such as Track Tool and Studio, if a
  second instance of the app is started and then exits, NVDA will no longer
  cause Studio add-on configuration routines to produce errors and stop
  working correctly.
* Added labels for various options in SPL Encoder configuration dialog.

## Version 19.04.1

* Fixed several issues with redesigned column announcements and playlist
  transcripts panels in add-on settings, including changes to custom column
  order and inclusion not being reflected when saving and/or switching
  between panels.

## Version 19.04/18.09.8-LTS

* Various global commands such as entering SPL Controller and switching to
  Studio window will be turned off if NVDA is running in secure mode or as a
  Windows Store application.
* 19.04: in column announcements and playlist transcripts panels (add-on
  settings), custom column inclusion/order controls will be visible up front
  instead of having to select a button to open a dialog to configure these
  settings.
* In Creator, NVDA will no longer play error tones or appear to do nothing
  when focused on certain lists.

## Version 19.03/18.09.7-LTS

* L'appui sur Contrôle+NVDA+R pour recharger les paramètres sauvegardés
  rechargera maintenant aussi les paramètres de l'extension Studio, et un
  triple appui sur cette commande réinitialisera également les paramètres
  par défaut de l'extension Studio ainsi que les paramètres NVDA.
* Le dialogue de paramètres de l'extension Studio "Options avancées" a été
  renommé en "Avancé".
* 19.03 experimental: in column announcements and playlist transcripts
  panels (add-on settings), custom column inclusion/order controls will be
  visible up front instead of having to select a button to open a dialog to
  configure these settings.

## Version 19.02

* Suppression de la fonctionnalité de vérification de mise à jour autonome
  de l'extension y compris la commande de vérification de mise à jour à
  partir de l'Assistant SPL (Contrôle+Maj+U) et les options de vérification
  de mise à jour à partir des paramètres de l'extension. La vérification de
  mise à jour de l'extension est maintenant effectuée par Add-on Updater.
* NVDA ne semble plus rien faire ou ne lit plus une tonalité d'erreur
  lorsque l'intervalle d'activation du microphone est défini, il est utilisé
  pour se souvenir lors de la diffusion que le microphone est actif avec des
  bips périodiques.
* Lors de la réinitialisation des paramètres de l'extension à partir du
  dialogue Paramètres extension / panneau réinitialisation, NVDA demandra à
  nouveau si un changement de profil immédiat ou un profil basé sur l'heure
  est actif.
* After resetting Studio add-on settings, NVDA will turn off microphone
  alarm timer and announce metadata streaming status, similar to after
  switching between broadcast profiles.

## Version 19.01.1

* NVDA n'annoncera plus "Contrôle du balayage de la bibliothèque en cours"
  après la fermeture de Studio dans certaines situations.

## Version 19.01/18.09.6-LTS

* NVDA 2018.4 ou ultérieur est requis.
* Davantage de changements de code pour rendre l'extension compatible avec
  Python 3.
* 19.01: certaines traductions de message de cette extension ressembleront à
  des messages NVDA.
* 19.01: la fonctionnalité Rechercher les mises à jour de l'extension n'est
  plus disponible. Un message d'erreur apparaît lorsque vous essayez
  d'utiliser l'Assistant SPL, Contrôle+Maj+U pour rechercher des mises à
  jour. Pour les futures mises à jour, veuillez utiliser l'extension Add-on
  Updater.
* Légères améliorations des performances lors de l'utilisation de NVDA avec
  des applications autres que Studio lorsque Voice Track Recorder est
  actif. NVDA continuera d'afficher des problèmes de performances lors de
  l'utilisation de Studio lui-même avec Voice Track Recorder actif.
* Dans les encodeurs, si un dialogue Paramètres de l'encodeur est ouvert
  (Alt+NVDA+0), NVDA affichera un message d'erreur si vous essayez d'ouvrir
  un eautre dialogue Paramètres de l'encodeur.

## Version 18.12

* Changements internes afin de rendre l'extension compatible avec les
  futures versions de NVDA.
* Correction de nombreuses occurrences de messages de l'extension annoncés
  en anglais malgré leur traduction dans d'autres langues.
* Si vous utilisez l'Assistant SPL pour rechercher des mises à jour de
  l'extension (Assistant SPL, Contrôle+Maj+U), NVDA n'installe pas de
  nouvelles versions de l'extension si elles nécessitent une version plus
  récente de NVDA.
* Certaines commandes de l'assistant SPL exigent désormais que la
  visionneuse de playlist soit visible et complété par une playlist. Dans
  certains cas, une piste est focalisée. Les commandes concernées incluent
  la durée restante (D), les instantanés de playlist (F8) et les
  transcriptions de Playlist (Maj + F8).
* La commande pour la durée restante de la playlist (Assistant SPL, D) exige
  désormais qu'une piste depuis la visionneuse de playlist soit focalisée.
* Dans les encodeurs de SAM, vous pouvez désormais utiliser les commandes de
  navigation dans les tableaux (Contrôle+Alt+touches fléchées) pour examiner
  diverses informations sur l'état de l'encodeur.

## Version 18.11/18.09.5-LTS

Note: 18.11.1 remplace 18.11 afin de mieux prendre en charge Studio 5.31.

* Premier support de StationPlaylist Studio 5.31.
* Vous pouvez maintenant obtenir des instantanés de playlist (Assistant SPL,
  F8) et des transcriptions (Assistant SPL, Maj+F8) alors qu'une playlist
  est chargée mais la première piste n'a pas le focus.
* NVDA ne semblera plus rien faire et ne jouera pas des tonalités d'erreur
  en essayant d'obtenir le statut de diffusion des métadonnées au démarrage
  de Studio s'il est configuré pour le faire.
* S'il est configuré pour annoncer l'état de la diffusion des métadonnées au
  démarrage , , l'annonce de l'état de diffusion des métadonnées et ne sera
  plus coupé les annonces relatives aux modifications de la barre d'état, et
  inversement.

## Version 18.10.2/18.09.4-LTS

* Correction de l'incapacité de fermer l'écran Paramètres de l'extension si
  le bouton Appliquer a été appuyé et que les boutons OK ou Annuler ont
  ensuite été pressés.

## Version 18.10.1/18.09.3-LTS

* Résolution de plusieurs problèmes liés à la fonction de l'annonce de
  connexion de l'encodeur, y compris le fait de ne pas annoncer les statut
  des messages, de ne pas lire la première piste sélectionnée ou de ne pas
  basculer à la fenêtre Studio lorsqu'il est connectée. Ces bugs sont causés
  par wxPython 4 (NVDA 2018.3 ou ultérieur).

## Version 18.10

* NVDA 2018.3 ou ultérieur est requis.
* Changements internes afin de rendre l'extension plus compatible avec
  Python 3.

## Version 18.09.1-LTS

* Lors de l'obtention de transcriptions de playlist au format de tableau
  HTML, les titres de colonnes ne sont plus affichés sous la forme d'une
  chaîne de liste Python.

## Version 18.09-LTS

La version 18.09.x est la dernière série à prendre en charge Studio 5.10 et
elle est basée sur les anciennes technologies, avec la 18.10 et versions
ultérieures prenant en charge Studio 5.11 / 5.20 et des nouvelles
fonctionnalités si nécessaire, certaines nouvelles fonctionnalités seront
redirigées vers la 18.09.x.

* NVDA 2018.3 ou une version ultérieure est recommandée en raison de
  l'introduction de wxPython 4.
* L'écran des paramètres des extensions est désormais entièrement basé sur
  une interface multi-pages dérivée de NVDA 2018.2 et versions ultérieures.
* Test Drive Fast et Slow ont combiné le canal "développement" avec une
  option permettant aux utilisateurs de snapshot  de développement de tester
  les fonctionnalités pilotes en cochant la nouvelle case à cocher
  "Fonctions pilotes" du panneau Paramètres avancés. Les utilisateurs
  d'abord sur Test Drive Fast Ring continuera à tester les fonctionnalités
  du pilote.
* La possibilité de sélectionner un canal différent pour la mise à jour de
  l'extension à partir des paramètres de l'extension a été supprimée. Les
  utilisateurs qui souhaitent basculer vers un canal de version différent
  devraient visiter le site comunautaire des extensions NVDA
  (addons.nvda-project.org), sélectionnez StationPlaylist Studio, puis
  téléchargez la version appropriée.
* Les cases à cocher d'inclusion de colonne pour l'annonce de colonne et les
  transcriptions de playlist, ainsi que les cases à cocher pour les flux de
  métadonnées ont été converties en contrôles de liste vérifiables.
* When switching between settings panels, NVDA will remember current
  settings for profile-specific settings (alarms, column announcements,
  metadata streaming settings).
* Ajout du format CSV (valeurs séparées par des virgules) en tant que format
  de transcriptions de playlist.
* En appuyant sur Ctrl+NVDA+C pour enregistrer les paramètres, vous
  sauvegarderez également les paramètres de l'extension Studio (nécessite
  NVDA 2018.3).

## Anciennes versions

S'il vous plaît voir le lien changelog pour les notes de version  pour les
anciennes versions de l'extension.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
