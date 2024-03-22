# StationPlaylist #

* Auteurs : Christopher Duffley <nvda@chrisduffley.com> (anciennement Joseph
  Lee <Joseph.lee22590@gmail.com>, à l'origine par Geoff Shang et d'autres
  contributeurs)
* Télécharger [version stable][1]
* NVDA compatibility: 2023.3.3 and later

Cette extension améliore l'utilisation de Station Playlist Studio, mais elle
fournit aussi des utilitaires pour contrôler le Studio où que vous soyez.

Pour plus d'informations sur l'extension, veuillez lire le [guide de
l'extension][2].

NOTES IMPORTANTES :

* Cette extension nécessite StationPlaylist suite 5.40 ou version
  ultérieure.
* Certaines fonctionnalités de l'extension seront désactivées ou limitées si
  NVDA s'exécute en mode sécurisé, comme dans l'écran de connexion.
* Pour une meilleure expérience, désactiver le Mode d'atténuation audio.
* À partir de 2018, les [changelogs des anciennes versions de
  l'extension][3] seront disponibles sur GitHub. Ce fichier readme de
  l'extension listera les modifications apportées à partir de la version
  23.02 (2023).
* Pendant que Studio est en cours d'exécution, vous pouvez sauvegarder,
  recharger les paramètres sauvegardés, ou rétablir les paramètres par
  défaut de l'extension en pressant Contrôle+NVDA+C, Contrôle+NVDA+R une
  fois, ou Contrôle+NVDA+R trois fois, respectivement. Cela s'applique aussi
  aux paramètres d'encodage - vous pouvez sauver et réinitialiser (pas
  recharger) les paramètres d'encodage si vous utilisez des encodeurs.
* Many commands will provide speech output while NVDA is in speak on demand
  mode (NVDA 2024.1 and later).

## Raccourcis clavier

Most of these will work in Studio only unless otherwise specified. Unless
noted otherwise, these commands support speak on demand mode.

* Alt+Shift+T from Studio window: announce elapsed time for the currently
  playing track.
* Control+Alt+T (two finger flick down in SPL touch mode) from Studio
  window: announce remaining time for the currently playing track.
* NVDA+Maj+F12 (glissement à deux doigts vers le haut en mode tactile SPL)
  depuis la fenêtre de Studio: annonce le temps de diffusion tel que 5
  minutes en haut de l'heure. Appuyez deux fois sur cette commande pour
  annoncer les minutes et les secondes jusqu'au début de l'heure.
* Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens
  alarms category in Studio add-on configuration dialog (does not support
  speak on demand).
* Alt+NVDA+1 à partir de l'éditeur de liste de lecture du créateur et de
  l'éditeur de liste de lecture à distance VT : annonce l'heure programmée
  pour la liste de lecture chargée.
* Alt+NVDA+2 à partir de l'éditeur de liste de lecture de Creator et de
  l'éditeur de liste de lecture Remote VT : annonce la durée totale de la
  liste de lecture.
* Alt+NVDA+3 from Studio window: Toggles cart explorer to learn cart
  assignments (does not support speak on demand).
* Alt+NVDA+3 à partir de l'éditeur de liste de lecture de Creator et de
  l'éditeur de liste de lecture Remote VT : annonce quand la lecture de la
  piste sélectionnée est programmée.
* Alt+NVDA+4 de Creator's Playlist Editor et Remote VT playlist editor :
  annonce la rotation et la catégorie associées à la playlist chargée.
* Control+NVDA+f from Studio window: Opens a dialog to find a track based on
  artist or song name. Press NVDA+F3 to find forward or NVDA+Shift+F3 to
  find backward (does not support speak on demand).
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
* Contrôle+NVDA+1 à 0 (si une piste est en focus dans Studio, Creator (y
  compris Playlist Editor), Remote VT et Track Tool) : annonce le contenu de
  la colonne pour une colonne spécifiée (les dix premières colonnes par
  défaut). Appuyez deux fois sur cette commande pour afficher les
  informations de la colonne dans une fenêtre en mode navigation.
* Control+NVDA+- (hyphen while focused on a track in Studio, Creator, Remote
  VT, and Track Tool): display data for all columns in a track on a browse
  mode window (does not support speak on demand).
* NVDA+V while focused on a track (Studio's playlist viewer only): toggles
  track column announcement between screen order and custom order (does not
  support speak on demand).
* Alt+NVDA+C si une piste est en focus (Studio uniquement): annonce les
  commentaires de piste le cas échéant.
* Alt+NVDA+0 from Studio window: Opens the Studio add-on configuration
  dialog (does not support speak on demand).
* Alt+NVDA+P from Studio window: Opens the Studio broadcast profiles dialog
  (does not support speak on demand).
* Alt+NVDA+F1: Open welcome dialog (does not support speak on demand).

## Commandes non assignées

Les commandes suivantes ne sont pas assignées par défaut; Si vous souhaitez
les assigner, utilisez le dialogu des Gestes de Commande pour ajouter des
commandes personnalisées. Pour ce faire, depuis la fenêtre de Studio, ouvrez
le menu NVDA, Préférences, puis Gestes de commande. Développez la catégorie
StationPlaylist, puis localisez les commandes non assignées dans la liste et
sélectionnez "Ajouter" puis tapez le geste que vous désirez utiliser.

Important: some of these commands will not work if NVDA is running in secure
mode such as from login screen. Not all commands support speak on demand.

* Switching to SPL Studio window from any program (unavailable in secure
  mode, does not support speak on demand).
* Couche du Contrôleur SPL (indisponible en mode sécurisé).
* Annonçant le statut de Studio, comme la lecture de pistes à partir
  d'autres programmes (indisponible en mode sécurisé).
* Annonce de l'état de connexion de l'encodeur à partir de n'importe quel
  programme (indisponible en mode sécurisé).
* Couche Assistant SPL depuis SPL Studio.
* Annoncer le temps y compris les secondes depuis SPL Studio.
* Annonce de la température.
* Annonce du titre de la piste suivante si planifié.
* Annonçant le titre de la piste en cours de lecture.
* Marquage de piste en cours pour le début de l'analyse de durée de piste.
* Effectuer des analyses de durée de piste.
* Prendre des instantanés de playlist.
* Find text in specific columns (does not support speak on demand).
* Find tracks with duration that falls within a given range via time range
  finder (does not support speak on demand).
* Quickly enable or disable metadata streaming (does not support speak on
  demand).

## Commandes supplémentaires lors de l'utilisation des encodeurs

The following commands are available when using encoders, and the ones used
for toggling options for on-connection behavior such as focusing to Studio,
playing the first track, and toggling of background monitoring can be
assigned through the Input Gestures dialog in NVDA menu, Preferences, Input
Gestures, under the StationPlaylist category. These commands do not support
speak on demand.

* F9 : Connecte l'encodeur sélectionné.
* F10 (encodeur SAM uniquement) : Déconnectez l'encodeur sélectionné.
* Contrôle+F9 : Connecte tous les encodeurs.
* Contrôle+F10 (encodeur SAM uniquement) : Déconnecter tous les encodeurs.
* Ctrl+Maj+F11 : Détermine si NVDA bascule vers la fenêtre Studio pour
  l'encodeur sélectionné  si connecté.
* Maj+F11: Détermine si Studio lit la première piste sélectionnée lorsque
  l'encodeur est connecté à un serveur de streaming.
* Contrôle+F11 : Active ou désactive le contrôle en arrière-plan de
  l'encodeur sélectionné.
* Contrôle+F12 : Ouvre un dialogue pour sélectionner l'encodeur que vous
  avez supprimé (afin de réaligner les étiquettes de flux et les paramètres
  de l'encodeur).
* Alt+NVDA+0 or F12: Opens encoder settings dialog to configure options such
  as encoder label.

In addition, column review commands are available, including (supports speak
on demand):

* Contrôle+NVDA+1 : Position de l'encodeur.
* Contrôle+NVDA+2 : étiquette de flux.
* Contrôle+NVDA+3 depuis l'Encodeur SAM : Format de l'Encodeur.
* Contrôle+NVDA+3 depuis les encodeurs SPL et AltaCast : Paramètres de
  l'encodeur.
* Contrôle+NVDA+4 depuis l'Encodeur SAM : Statut de la connexion de
  l'encodeur.
* Contrôle+NVDA+4 depuis les Encodeurs SPL et AltaCast : Statut de la
  connexion ou du taux de transfert.
* Contrôle+NVDA+5 depuis l'Encodeur SAM : Description du statut de la
  connexion.

## Couche Assistant SPL

Cette couche de commandes vous permet d'obtenir différents statuts sur SPL
Studio, comme si une piste est en cours de lecture, la durée totale de
toutes les pistes pour l'heure et ainsi de suite. De n'importe quelle
fenêtre de SPL Studio appuyez sur la commande couche Assistant SPL, puis
appuyez sur une des touches dans la liste ci-dessous (une ou plusieurs
commandes sont exclusives a la visionneuse de playlist). Vous pouvez
également configurer NVDA pour émuler les commandes des autres lecteurs
d’écran.

The available commands are (most commands support speak on demand):

* A : Automatisation.
* C (Maj+C dans la disposition de JAWS et Window-Eyes) : Titre pour la piste
  en cours de lecture.
* C (JAWS layout): Toggle cart explorer (playlist viewer only, does not
  support speak on demand).
* D (R dans la disposition de JAWS) : Durée restante pour la playlist (si un
  message d’erreur est donné, se déplacer vers la visionneuse de playlist et
  puis tapez cette commande).
* E : Statut de métadonnées en streaming.
* Maj+1 jusqu'à maj+4, maj+0 : Statut de Métadonnées individuelles en
  streaming URLs (0 est pour l'encodeur DSP).
* F: Find track (playlist viewer only, does not support speak on demand).
* H : Durée de la musique pour la tranche horaire en cours.
* Maj+H : Durée des pistes restantes pour la tranche horaire.
* I (L dans la disposition de JAWS) : Nombre d'auditeurs.
* K : Se déplacer à la piste marquée (visionneuse de playlist uniquement).
* Contrôle+K : Définir la piste en cours comme le marqueur de position de
  piste (visionneuse de playlist uniquement).
* L (Maj+L dans la  disposition de JAWS) : Entrée ligne.
* M : Microphone.
* N : Titre pour la piste suivante planifié.
* P : Statut (en cours de lecture ou arrêté).
* Maj+P : Hauteur de la piste actuelle.
* R (Maj+E dans la disposition  de JAWS) : Enregistrer dans un fichier
  activé/désactivé.
* Maj+R : Contrôle du balayage de la bibliothèque en cours.
* S : Piste débute (planifié).
* Maj+S : Durée jusqu'à la piste sélectionnée qui va être jouer (piste
  débute dans).
* T : Mode édition/insertion panier activé/désactivé.
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

## Contrôleur SPL

Le contrôleur SPL est un ensemble de commandes couches que vous pouvez
utiliser pour contrôler SPL Studio de n'importe où. Appuyez sur la commandes
couche Contrôleur SPL, et NVDA dira, "Contrôleur SPL." Appuyez sur une autre
commande pour contrôler divers paramètres Studio comme activer/désactiver un
microphone ou lire la piste suivante.

Important : Les commandes en couche du contrôleur SPL sont désactivées si
NVDA s'exécute en mode sécurisé.

The available SPL Controller commands are (some commands support speak on
demand):

* P : lire la prochaine piste sélectionnée.
* U : mettre en pause ou reprendre la lecture.
* S : Arrête la piste avec un fondu sortant.
* T : Arrêt immédiat.
* M : Activer le microphone.
* Maj+M : Désactiver le microphone.
* A : Activer l'automatisation.
* Maj+A : Désactiver l'automatisation.
* L : Active l'entrée ligne.
* Maj+L : Désactive l'entrée ligne.
* R :  Temps restant pour la piste en cours de lecture.
* Maj+R : Contrôle de la progression du balayage de la bibliothèque en
  cours.
* C: Title and duration of the currently playing track (supports speak on
  demand).
* Shift+C: Title and duration of the upcoming track if any (supports speak
  on demand).
* E: Encoder connection status (supports speak on demand).
* I: Listener count (supports speak on demand).
* Q: Studio status information such as whether a track is playing,
  microphone is on and others (supports speak on demand).
* Appuyez sur les touches de panier (F1, Contrôle+1, par exemple) pour lire
  les paniers assignés à partir de n'importe où.
* H: Aide de couche.

## Alarmes piste et microphone

Par défaut, NVDA émettra un bip s'il reste cinq secondes dans la piste
(outro) et/ou l'intro, ainsi qu'un bip si le microphone est actif depuis un
certain temps. Pour configurer les alarmes de piste et de microphone,
appuyez sur Alt+NVDA+1 pour ouvrir les paramètres des alarmes dans l'écran
des paramètres de l'extension Studio. Vous pouvez également utiliser cet
écran pour configurer si vous entendez un bip, un message ou les deux
lorsque les alarmes sont activées.

## Chercheur de piste

Si vous souhaitez trouver rapidement une chanson par artiste ou par nom de
chanson, depuis la liste de piste, appuyez sur Contrôle+NVDA+F. Tapez le nom
de l'artiste ou le nom de la chanson. NVDA va vous placer soit à la chanson
Si cell-ci est trouvé ou il affichera une erreur si elle ne trouve pas la
chanson que vous recherchez. Pour trouver une chanson ou un artiste
précédemment entrée, appuyez sur NVDA+F3 ou NVDA+Maj+F3 Pour trouver en
avant ou en arrière.

Remarque: le Chercheur de piste est sensible à la casse.

## Explorateur de panier

Selon l'édition, SPL Studio permet d'assigné jusq'à 96 paniers pendant la
lecture. NVDA vous permet d'entendre quel panier ou jingle est assigné à ces
commandes.

Pour apprendre les assignations de panier, à partir de SPL Studio, appuyez
sur Alt+NVDA+3. Appuyer une fois sur la commande panier vous indiquera quel
jingle est affecté à la commande. Appuyez deux fois sur la commande panier
pour jouer le jingle. Appuyez sur Alt+NVDA+3 pour quitter l'explorateur de
panier. Consultez le guide de l'extension pour plus d'informations sur
l'explorateur de panier.

## Analyse de durée de piste

Pour obtenir la longueur pour jouer les pistes sélectionnés, marquer la
piste en cours pour le début de l'analyse de durée de piste (Assistant SPL,
F9), puis appuyer sur Assistant SPL, F10 lorsque vous atteignez la fin de la
sélection.

## Explorateur de Colonnes

En appuyant sur Ctrl+NVDA+1 à 0, vous pouvez obtenir le contenu de colonnes
spécifiques. Par défaut, ce sont les dix premières colonnes d'un élément de
piste (dans Studio : artiste, titre, durée, intro, outro, catégorie, année,
album, genre, ambiance). Pour l'éditeur de liste de lecture dans le client
Creator et Remote VT, les données de colonne dépendent de l'ordre des
colonnes, comme indiqué à l'écran. Dans Studio, la liste des pistes
principale de Creator et l'outil de piste, les emplacements de colonne sont
prédéfinis quel que soit l'ordre des colonnes à l'écran et peuvent être
configurés à partir du dialogue des paramètres de l'extension sous la
catégorie explorateur de colonnes.

## Annonce des colonnes des pistes

Vous pouvez demander à NVDA d'annoncer des colonnes de piste trouvées dans
la visionneuse de playlist de Studio dans l'ordre où il apparaît sur l'écran
ou en utilisant l'ordre personnalisé et / ou exclure certaines
colonnes. Appuyez sur NVDA+V pour basculer ce comportement tandis que le
focus est mis sur une piste dans la visionneuse de playlist de Studio. Pour
l'ordre et l'inclusion des colonnes personnalisées à partir du panneau de
paramètres annonces de colonne dans les paramètres de l'extension, décochez
"Annoncer les colonnes dans l'ordre affichés sur l'écran" puis personnaliser
les colonnes incluses et / ou l'ordre de colonne.

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
préférences de NVDA et sélectionnez l'élément Paramètres SPL Studio. Tous
les paramètres ne sont pas disponibles si NVDA s'exécute en mode sécurisé.

## Dialogue profils de diffusion

Vous pouvez sauvegarder les paramètres pour des émissions spécifiques dans
des profils de diffusion. Ces profils peuvent être gérés  via le dialogue
des profils de diffusion de SPL which can be accessible en pressant
Alt+NVDA+P depuis la fenêtre Studio.

## Mode tactile SPL

Si vous utilisez Studio sur un ordinateur possédant un écran tactile avec
NVDA installé, vous pouvez exécuter certaines commandes Studio depuis un
écran tactile. Tout d'abord utiliser une tape à trois doigts pour basculer
en mode SPL, puis utilisez les commandes tactile énumérées ci-dessus pour
exécuter des commandes.

## Version 24.03

* Compatible with NVDA 2024.1.
* NVDA 2023.3.3 or later is required.
* Support for StationPlaylist suite 6.10.
* Most commands support speak on demand (NVDA 2024.1) so announcements can
  be spoken in this mode.

## Version 24.01

* Les commandes du dialogue Paramètres de l'encodeur à utiliser avec les
  encodeurs SPL et SAM sont désormais assignables, ce qui signifie que vous
  pouvez les modifier par rapport à leurs valeurs par défaut dans la
  catégorie StationPlaylist dans Menu NVDA > Préférences > Gestes de
  commandes. Celles qui ne sont pas attribuables sont les commandes de
  connexion et de déconnexion. De plus, pour éviter les conflits de
  commandes et faciliter l'utilisation de cette commande sur les serveurs
  distants, le geste par défaut pour passer à Studio après la connexion est
  désormais Ctrl+Maj+F11 (auparavant uniquement F11). Tous ces éléments
  peuvent bien sûr toujours être activés à partir du dialogue Paramètres de
  l'encodeur (NVDA+Alt+0 ou F12).

## Version 23.05

* Pour refléter le changement du mainteneur, le manifeste a été mis à jour
  pour indiquer en tant que tel.

## Version 23.02

* NVDA 2022.4 ou ultérieur est requis.
* Windows 10 21H2 (Mise à jour Novembre 2021 / build 19044) ou ultérieure
  est requise.
* Dans la visionneuse de playlist de Studio, NVDA n'annoncera pas les
  en-têtes de colonne tels que l'artiste et le titre si le paramètre
  d'en-têtes des tableaux est défini sur En-têtes "Lignes et colonnes" ou
  "Colonnes" dans le panneau Mise en Forme des Documents dans les Paramètres
  de NVDA.

## Anciennes versions

S'il vous plaît voir le [changelog][3] pour les notes de version  pour les
anciennes versions de l'extension.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=stationPlaylist

[2]: https://github.com/chrisDuffley/stationplaylist/wiki/SPLAddonGuide

[3]: https://github.com/ChrisDuffley/stationplaylist/wiki/splchangelog
