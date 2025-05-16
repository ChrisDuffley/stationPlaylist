# StationPlaylist #

* Auteurs : Christopher Duffley <nvda@chrisduffley.com> (anciennement Joseph
  Lee <Joseph.lee22590@gmail.com>, à l'origine par Geoff Shang et d'autres
  contributeurs)

Cette extension améliore l'utilisation de Station Playlist Studio, mais elle
fournit aussi des utilitaires pour contrôler le Studio où que vous soyez.

Pour plus d'informations sur l'extension, veuillez lire le [guide de
l'extension][1].

NOTES IMPORTANTES :

* Cette extension nécessite StationPlaylist suite 5.50 ou version
  ultérieure.
* Certaines fonctionnalités de l'extension seront désactivées ou limitées si
  NVDA s'exécute en mode sécurisé, comme dans l'écran de connexion.
* Pour une meilleure expérience, désactiver le Mode d'atténuation audio.
* À partir de 2018, les [changelogs des anciennes versions de
  l'extension][2] seront disponibles sur GitHub. Ce fichier readme de
  l'extension listera les modifications apportées à partir de la version
  23.02 (2023).
* Pendant que Studio est en cours d'exécution, vous pouvez sauvegarder,
  recharger les paramètres sauvegardés, ou rétablir les paramètres par
  défaut de l'extension en pressant Contrôle+NVDA+C, Contrôle+NVDA+R une
  fois, ou Contrôle+NVDA+R trois fois, respectivement. Cela s'applique aussi
  aux paramètres d'encodage - vous pouvez sauver et réinitialiser (pas
  recharger) les paramètres d'encodage si vous utilisez des encodeurs.
* De nombreuses commandes fourniront une sortie vocale lorsque NVDA est en
  mode parole à la demande (NVDA 2024.1 et versions ultérieures).

## Raccourcis clavier

La plupart d'entre eux fonctionneront dans Studio uniquement sauf indication
contraire. Sauf indication contraire, ces commandes prennent en charge le
mode parole à la demande.

* Alt+Maj+T depuis la fenêtre de Studio : annonce le temps écoulé pour la
  piste en cours de lecture.
* Contrôle+Alt+T (glissement à deux doigts vers le bas en mode tactile SPL)
  depuis la fenêtre de Studio : annoncer le temps restant pour la piste en
  cours de lecture.
* NVDA+Maj+F12 (glissement à deux doigts vers le haut en mode tactile SPL)
  depuis la fenêtre de Studio: annonce le temps de diffusion tel que 5
  minutes en haut de l'heure. Appuyez deux fois sur cette commande pour
  annoncer les minutes et les secondes jusqu'au début de l'heure.
* Alt+NVDA+1 (faire glisser deux doigts vers la droite en mode SPL) à partir
  de la fenêtre Studio : ouvre la catégorie des alarmes dans le dialogue de
  configuration de l'extension de Studio (ne prend pas en charge la parole à
  la demande).
* Alt+NVDA+1 à partir de l'éditeur de liste de lecture du créateur et de
  l'éditeur de liste de lecture à distance VT : annonce l'heure programmée
  pour la liste de lecture chargée.
* Alt+NVDA+2 à partir de l'éditeur de liste de lecture de Creator et de
  l'éditeur de liste de lecture Remote VT : annonce la durée totale de la
  liste de lecture.
* Alt+NVDA+3 depuis la fenêtre de Studio : Basculer l'explorateur de panier
  pour apprendre les assignations de panier (ne prend pas en charge la
  parole à la demande).
* Alt+NVDA+3 à partir de l'éditeur de liste de lecture de Creator et de
  l'éditeur de liste de lecture Remote VT : annonce quand la lecture de la
  piste sélectionnée est programmée.
* Alt+NVDA+4 de Creator's Playlist Editor et Remote VT playlist editor :
  annonce la rotation et la catégorie associées à la playlist chargée.
* Contrôle+NVDA+F depuis la fenêtre de Studio : Ouvre un dialogue pour
  chercher une piste en se basant sur l'artiste ou le nom de la
  chanson. Appuyez  sur NVDA+F3 pour chercher vers l'avant ou appuyez sur
  NVDA+Maj+F3 pour rechercher vers l'arrière (ne prend pas en charge la
  parole à la demande).
* Maj+NVDA+R depuis la fenêtre de Studio : parcourt les paramètres d'annonce
  du balayage dans la bibliothèque (ne prend pas en charge la parole à la
  demande).
* Contrôle+Maj+X depuis la fenêtre de Studio : Parcourt les paramètres du
  minuteur braille (ne prend pas en charge la parole à la demande).
* Contrôle+Alt+flèche gauche/droite (Si une piste est en focus dans Studio,
  Creator, et l'Outil de piste): Annoncer colonne de piste
  précédente/suivante (ne prend pas en charge la parole à la demande).
* Contrôle+Alt+flèche haut/bas (si une piste est en focus  dans Studio,
  Creator, Remote VT, ou Track Tool): aller à la piste précédente ou
  suivante et annoncer des colonnes spécifiques (ne prend pas en charge la
  parole à la demande).
* Contrôle+NVDA+1 à 0 (si une piste est en focus dans Studio, Creator (y
  compris Playlist Editor), Remote VT et Track Tool) : annonce le contenu de
  la colonne pour une colonne spécifiée (les dix premières colonnes par
  défaut). Appuyez deux fois sur cette commande pour afficher les
  informations de la colonne dans une fenêtre en mode navigation.
* Contrôle+NVDA+- (trait d'union si une piste est en focus dans Studio,
  Creator, Remote VT et Track Tool) : affiche les données de toutes les
  colonnes d'une piste dans une fenêtre en mode navigation (ne prend pas en
  charge la parole à la demande).
* NVDA+V si une piste est en focus (visualiseur de playlist de Studio
  uniquement) : bascule l'annonce de la colonne de piste entre l'ordre de
  l'écran et l'ordre personnalisé (ne prend pas en charge la parole à la
  demande).
* Alt+NVDA+C si une piste est en focus (Studio uniquement): annonce les
  commentaires de piste le cas échéant.
* Alt+NVDA+0 depuis la fenêtre de Studio : Ouvre le dialogue de
  configuration de l'extension Studio (ne prend pas en charge la parole à la
  demande).
* Alt+NVDA+P à partir de la fenêtre Studio : ouvre le dialogue des profils
  de diffusion Studio (ne prend pas en charge la parole à la demande).
* Alt+NVDA+F1: Ouvre le dialogue de bienvenue (ne prend pas en charge la
  parole à la demande).

## Commandes non assignées

Les commandes suivantes ne sont pas assignées par défaut; Si vous souhaitez
les assigner, utilisez le dialogu des Gestes de Commande pour ajouter des
commandes personnalisées. Pour ce faire, depuis la fenêtre de Studio, ouvrez
le menu NVDA, Préférences, puis Gestes de commande. Développez la catégorie
StationPlaylist, puis localisez les commandes non assignées dans la liste et
sélectionnez "Ajouter" puis tapez le geste que vous désirez utiliser.

Important : certaines de ces commandes ne fonctionneront pas si NVDA
s'exécute en mode sécurisé, par exemple à partir de l'écran de
connexion. Toutes les commandes ne prennent pas en charge la parole à la
demande.

* Basculement vers la fenêtre SPL Studio depuis n'importe quel programme
  (indisponible en mode sécurisé, ne prend pas en charge la parole à la
  demande).
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
* Recherche de texte dans des colonnes spécifiques (ne prend pas en charge
  la parole à la demande).
* Trouver des piste avec une durée qui se situe dans un intervalle donné via
  la recherche de l'intervalle de temps (ne prend pas en charge la parole à
  la demande).
* Activer ou désactiver les métadonnées en streaming rapidement (ne prend
  pas en charge la parole à la demande).

## Commandes supplémentaires lors de l'utilisation des encodeurs

Les commandes suivantes sont disponibles lors de l'utilisation des
encodeurs, et celles utilisées pour basculer les options de comportement
lors de la connexion tandis que le focus est mis sur Studio, la lecture de
la première piste et le basculement de la surveillance en arrière-plan
peuvent être assignées via le dialogue Gestes de commandes dans le menu
NVDA, Préférences, Gestes de commandes, dans la catégorie
StationPlaylist. Ces commandes ne prennent pas en charge la parole à la
demande.

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
  avez supprimé (afin de réaligner les étiquettes et les paramètres de
  l'encodeur).
* Alt+NVDA+0 ou F12 : Ouvre le dialogue paramètres  de l'encodeur pour
  configurer des options telles que l'étiquette de l'encodeur.

De plus, les commandes pour visualiser la colonne sont disponibles, y
compris (prend en charge la parole à la demande) :

* Contrôle+NVDA+1 : Position de l'encodeur.
* Contrôle+NVDA+2 : étiquette de l'encodeur.
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

Les commandes disponibles sont (la plupart des commandes prennent en charge
la parole à la demande) :

* A : Automatisation.
* C (Maj+C dans la disposition de JAWS) : Titre pour la piste en cours de
  lecture.
* C (disposition JAWS) : Bascule l'explorateur de panier (visionneuse de
  playlist uniquement, ne prend pas en charge la parole à la demande).
* D (R dans la disposition de JAWS) : Durée restante pour la playlist (si un
  message d’erreur est donné, se déplacer vers la visionneuse de playlist et
  puis tapez cette commande).
* Contrôle+D (Studio 6.10 et versions ultérieures) : touches de contrôle
  activées/désactivées.
* E : Statut de métadonnées en streaming.
* Maj+1 jusqu'à maj+4, maj+0 : Statut de Métadonnées individuelles en
  streaming URLs (0 est pour l'encodeur DSP).
* F : Recherche de piste (visionneuse de playlist uniquement, ne prend pas
  en charge la parole à la demande).
* H : Durée de la musique pour la tranche horaire en cours.
* Maj+H : Durée des pistes restantes pour la tranche horaire.
* I (L dans la disposition de JAWS) : Nombre d'auditeurs.
* K : Se déplacer à la piste marquée (visionneuse de playlist uniquement).
* Contrôle+K : Définir la piste en cours comme le marqueur de position de
  piste (visionneuse de playlist uniquement).
* L (Maj+L dans la  disposition de JAWS) : Entrée ligne.
* M : Microphone.
* N : Titre pour la piste suivante planifié.
* O : Playlist en heure / heure passée.
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

Les commandes disponibles pour le Contrôleur SPL sont (certaines commandes
prennent en charge la parole à la demande) :

* P : lire la prochaine piste sélectionnée.
* U : mettre en pause ou reprendre la lecture.
* S : Arrête la piste avec un fondu sortant.
* T : Arrêt immédiat.
* M : Activer le microphone.
* Maj+M : Désactiver le microphone.
* N: Turn microphone on without fade.
* A : Activer l'automatisation.
* Maj+A : Désactiver l'automatisation.
* L : Active l'entrée ligne.
* Maj+L : Désactive l'entrée ligne.
* R :  Temps restant pour la piste en cours de lecture.
* Maj+R : Contrôle de la progression du balayage de la bibliothèque en
  cours.
* C : Le titre et la durée de la piste en cours de lecture (prend en charge
  la parole à la demande).
* Maj+C : Le titre et la durée de la prochaine piste, le cas échéant (prend
  en charge la parole à la demande).
* E : Statut de la connexion de l'encodeur (prend en charge la parole à la
  demande).
* I : Nombre d'auditeurs (prend en charge la parole à la demande).
* Q : Diverses informations sur l'état de Studio, par exemple si une piste
  est en cours de lecture, le microphone est activé et d'autres (prend en
  charge la parole à la demande).
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

## Version 25.06-LTS

Version 25.06.x est la dernière version des séries à prendre en charge
Studio 5.x avec les versions futures nécessitant Studio 6.x. Certaines
nouvelles fonctionnalités seront recouvertes à la 25.06.x si nécessaire.

* NVDA will no longer forget to transfer broadcast profiles while updating
  the add-on (fixing a regression introduced in 25.05).
* Ajout d'une nouvelle commande dans l'Assistant SPL pour annoncer la
  playlist en heure / heure passée en minutes et secondes (O).
* Dans Studio, la commande de parcourt des paramètres d'annonce du balayage
  dans la bibliothèque est passé d'Alt+NVDA+R à Maj+NVDA+R car l'ancienne
  commande bascule la fonction d'accès à distance dans NVDA 2025.1.
* NVDA ne jouera plus de tonalités d'erreur ou n'apparaîtra pour ne rien
  faire lors de l'exécution des commandes de l'Assistant SPL après le
  redimensionnement de la fenêtre de Studio.
* The user interface for confirmation dialog shown when deleting broadcast
  profiles now resembles NVDA's configuration profile deletion interface.
* NVDA reconnaîtra les changements de colonne de piste introduits dans
  Creator et l'Outil de piste 6.11.
* In columns explorer for Creator, "Date Restriction" column is now
  "Restrictions".
* NVDA ne jouera plus de paniers erronés lorsque vous les jouez via la
  Couche du Contrôleur SPL.

## Version 25.05

* NVDA 2024.1 ou ultérieur est requis en raison de la mise à niveau de
  Python 3.11.
* Restauré la prise en charge limitée pour Windows 8.1.
* Déplacé les documents du wiki de l'extension tels que le changelog de
  l'extension vers le dépôt de code principal.
* Ajout du bouton Fermer aux Instantanés de playlist, Transcriptions de
  Playlist et Assistant SPL et écrans d'Aide du Contrôleur  en Couche (NVDA
  2025.1 et ultérieur).
* NVDA ne fera plus rien ni ne jouera des tonalités d'erreur lors de
  l'annonce des informations Météo et température dans Studio 6.x (Assistant
  SPL, W).

## Version 25.01

* Windows 10 21H2 64 bits (build 19044) ou ultérieure est requise.
* Les liens de téléchargement des versions de l'extension ne sont plus
  inclus dans la documentation de l'extension. Vous pouvez télécharger
  l'extension à partir de l'add-on store de NV Access.
* Changement de l'outil linting qui fait de l'analyse statique de Flake8
  vers Ruff et le reformatage des modules de l'extension pour mieux
  s'aligner sur les normes de codage de NVDA.
* Suppression de la prise en charge de la fonctionnalité de mise à jour
  automatique à partir de l'extension Add-on Updater.
* Dans Studio 6.10 et versions ultérieures, ajout d'une nouvelle commande
  dans Assistant SPL pour annoncer le statut activé/désactivé des touches de
  contrôle (Contrôle+D).

## Version 24.03

* Compatible avec NVDA 2024.1.
* NVDA 2023.3 ou ultérieur est requis.
* Prise en charge de StationPlaylist suite 6.10.
* La plupart des commandes prennent en charge la parole à la demande (NVDA
  2024.1), les annonces peuvent donc être verbalisées dans ce mode.

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

S'il vous plaît voir le [changelog][2] pour les notes de version  pour les
anciennes versions de l'extension.

[1]:
https://github.com/ChrisDuffley/stationPlaylist/blob/main/addonuserguide.md

[2]: https://github.com/ChrisDuffley/stationPlaylist/blob/main/changes.md
