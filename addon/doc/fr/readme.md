# StationPlaylist #

* Auteurs: Geoff Shang, Joseph Lee et d'autres contributeurs.
* Télécharger [version stable][1]
* Compatibilité NVDA: 2020.4 et ultérieurs.

Cette extension améliore l'utilisation de Station Playlist Studio, mais elle
fournit aussi des utilitaires pour contrôler le Studio où que vous soyez.

Pour plus d'informations sur l'extension, veuillez lire le [guidede
l'extension][2].

NOTES IMPORTANTES :

* Cette extension nécessite  StationPlaylist Studio 5.30 ou version
  ultérieure.
* Si vous utilisez Windows 8 ou ultérieur, pour une meilleure expérience,
  désactiver le Mode d'atténuation audio.
* À partir de 2018, [les journaux des modifications pour les anciennes
  versions d'extensions][3] seront disponibles sur GitHub. Ce fichier readme
  d'extension répertoriera les modifications apportées à partir de la
  version 20.09 (2020).À partir de 2018, [les journaux des changements des
  anciennes versions de l'extension][5] seront trouvés sur GitHub. Ce
  fichier readme ajoutera les changements depuis la version 7.0 (à partir de
  2016).
* Pendant que Studio est en cours d'exécution, vous pouvez sauvegarder,
  recharger les paramètres sauvegardés, ou rétablir les paramètres par
  défaut de l'extension en pressant Contrôle+NVDA+C, Contrôle+NVDA+R une
  fois, ou Contrôle+NVDA+R trois fois, respectivement. Cela s'applique aussi
  aux paramètres d'encodage - vous pouvez sauver et réinitialiser (pas
  recharger) les paramètres d'encodage si vous utilisez des encodeurs.

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
* Alt+NVDA+1 (faire glisser deux doigts vers la droite en mode SPL) à partir
  de la fenêtre Studio : ouvre la catégorie des alarmes dans le dialogue de
  configuration de l'extension de Studio.
* Alt+NVDA+1 à partir de l'éditeur de liste de lecture du créateur et de
  l'éditeur de liste de lecture à distance VT : annonce l'heure programmée
  pour la liste de lecture chargée.
* Alt+NVDA+2 à partir de l'éditeur de liste de lecture de Creator et de
  l'éditeur de liste de lecture Remote VT : annonce la durée totale de la
  liste de lecture.
* Alt+NVDA+3 depuis la fenêtre de Studio : Basculer l'explorateur de panier
  pour apprendre les assignations de panier.
* Alt+NVDA+3 à partir de l'éditeur de liste de lecture de Creator et de
  l'éditeur de liste de lecture Remote VT : annonce quand la lecture de la
  piste sélectionnée est programmée.
* Alt+NVDA+4 de Creator's Playlist Editor et Remote VT playlist editor :
  annonce la rotation et la catégorie associées à la playlist chargée.
* Contrôle+NVDA+f depuis la fenêtre de Studio : Ouvre un dialogue pour
  chercher une piste en se basant sur l'artiste ou le nom de la
  chanson. Appuyez  sur NVDA+F3 pour chercher vers l'avant ou appuyez sur
  NVDA+Maj+F3 pour rechercher vers l'arrière.
* Alt+NVDA+R depuis la fenêtre de Studio : parcourt les paramètres d'annonce
  du balayage dans la bibliothèque.
* Contrôle+Maj+X depuis la fenêtre de Studio : Parcourt les paramètres du
  minuteur braille.
* Contrôle+Alt+flèche gauche/droite (Si une piste est en focus dans Studio,
  Creator, et l'Outil de piste): Annoncer colonne de piste
  précédente/suivante.
* Control+Alt+Début/Fin (si une piste est en focus dans Studio, Creator,
  Remote VT et Track Tool) : accédez à la première/dernière colonne de
  piste.
* Contrôle+Alt+flèche haut/bas (si une piste est en focus  dans Studio,
  Creator, Remote VT, ou Track Tool): aller à la piste précédente ou
  suivante et annoncer des colonnes spécifiques
* Contrôle+NVDA+1 à 0 (si une piste est en focus dans Studio, Creator (y
  compris Playlist Editor), Remote VT et Track Tool) : annonce le contenu de
  la colonne pour une colonne spécifiée (les dix premières colonnes par
  défaut). Appuyez deux fois sur cette commande pour afficher les
  informations de la colonne dans une fenêtre en mode navigation.
* Contrôle+NVDA+- (trait d'union si une piste est en focus dans Studio,
  Creator, Remote VT et Track Tool) : affiche les données de toutes les
  colonnes d'une piste dans une fenêtre en mode navigation.
* NVDA+V si une piste est en focus (visualiseur de playlist de Studio
  uniquement) : bascule l'annonce de la colonne de piste entre l'ordre de
  l'écran et l'ordre personnalisé.
* Alt+NVDA+C si une piste est en focus (Studio uniquement): annonce les
  commentaires de piste le cas échéant.
* Alt+NVDA+0 depuis la fenêtre de Studio : Ouvre le dialogue de
  configuration de l'extension Studio.
* Alt+NVDA+P à partir de la fenêtre Studio : ouvre le dialogue des profils
  de diffusion Studio.
* Alt+NVDA+F1: Ouvre le dialogue de bienvenue.

## Commandes non assignées

Les commandes suivantes ne sont pas assignées par défaut; Si vous souhaitez
les assigner, utilisez le dialogu des Gestes de Commande pour ajouter des
commandes personnalisées. Pour ce faire, depuis la fenêtre de Studio, ouvrez
le menu NVDA, Préférences, puis Gestes de commande. Développez la catégorie
StationPlaylist, puis localisez les commandes non assignées dans la liste et
sélectionnez "Ajouter" puis tapez le geste que vous désirez utiliser.

* Basculement vers la fenêtre SPL Studio depuis n'importe quel programme.
* Couche Contrôleur SPL.
* Annonçant le statut de Studio, comme la lecture de pistes à partir
  d'autres programmes.
* Annonce de l'état de connexion de l'encodeur à partir de n'importe quel
  programme.
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

## Commandes supplémentaires lors de l'utilisation des encodeurs

Les commandes suivantes sont disponibles lorsque vous utilisez des
encodeurs:

* F9 : Connecte l'encodeur sélectionné.
* F10 (encodeur SAM uniquement) : Déconnectez l'encodeur sélectionné.
* Contrôle+F9 : Connecte tous les encodeurs.
* Contrôle+F10 (encodeur SAM uniquement) : Déconnecter tous les encodeurs.
* F11 : Détermine si NVDA bascule vers la fenêtre Studio pour l'encodeur
  sélectionné  si connecté.
* Maj+F11: Détermine si Studio lit la première piste sélectionnée lorsque
  l'encodeur est connecté à un serveur de streaming.
* Contrôle+F11 : Active ou désactive le contrôle en arrière-plan de
  l'encodeur sélectionné.
* Contrôle+F12 : Ouvre un dialogue pour sélectionner l'encodeur que vous
  avez supprimé (afin de réaligner les étiquettes de flux et les paramètres
  de l'encodeur).
* Alt+NVDA+0 et F12 : Ouvre le dialogue paramètres  de l'encodeur pour
  configurer des options telles que l'étiquette de flux.

De plus, les commandes pour visualiser la colonne sont disponibles, y
compris :

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

Les commandes disponibles sont :

* A : Automatisation.
* C (Maj+C dans la disposition de JAWS et Window-Eyes) : Titre pour la piste
  en cours de lecture.
* C (disposition JAWS) : Bascule l'explorateur de panier (visionneuse de
  playlist uniquement).
* D (R dans la disposition de JAWS) : Durée restante pour la playlist (si un
  message d’erreur est donné, se déplacer vers la visionneuse de playlist et
  puis tapez cette commande).
* E : Statut de métadonnées en streaming.
* Maj+1 jusqu'à maj+4, maj+0 : Statut de Métadonnées individuelles en
  streaming URLs (0 est pour l'encodeur DSP).
* F : Recherche de piste (visionneuse de playlist uniquement).
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
* Maj+F1 : Ouvre le guide de l'utilisateur en ligne.

## Contrôleur SPL

Le contrôleur SPL est un ensemble de commandes couches que vous pouvez
utiliser pour contrôler SPL Studio de n'importe où. Appuyez sur la commandes
couche Contrôleur SPL, et NVDA dira, "Contrôleur SPL." Appuyez sur une autre
commande pour contrôler divers paramètres Studio comme activer/désactiver un
microphone ou lire la piste suivante.

Les commandes disponibles pour le Contrôleur SPL sont:

* P : lire la prochaine piste sélectionnée.
* U : mettre en pause ou reprendre la lecture.
* S : Arrête la piste avec un fondu sortant.
* T : Arrêt immédiat.
* M : Activer le microphone.
* Maj+M : Désactiver le microphone.
* A : Activer l'automatisation.
* Maj+A : Désactiver l'automatisation.
* L : Active l'entrée ligne.
* Maj+l : Désactive l'entrée ligne.
* R :  Temps restant pour la piste en cours de lecture.
* Maj+R : Contrôle de la progression du balayage de la bibliothèque en
  cours.
* C : annoncer le titre et la durée de la piste en cours de lecture.
* Maj+C :  annoncer le titre et la durée de la prochaine piste, le cas
  échéant.
* E : Statut de la connexion de l'encodeur.
* I : Nombre d'auditeurs.
* Q : diverses informations sur l'état de Studio, y compris si une piste est
  en cours de lecture, le microphone est activé et d'autres.
* Appuyez sur les touches de panier (F1, Contrôle+1, par exemple) pour lire
  les paniers assignés à partir de n'importe où.
* H : Aide de couche.

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

Pour apprendre les affectations de panier, à partir de SPL Studio, appuyez
sur Alt+NVDA+3. Appuyer une fois sur la commande panier vous indiquera quel
jingle est affecté à la commande. Appuyez deux fois sur la commande panier
pour jouer le jingle. Appuyez sur Alt+NVDA+3 pour quitter l'explorateur de
panier. Consultez le guide des modules complémentaires pour plus
d'informations sur l'explorateur de panier.

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

You can ask NVDA to announce track columns found in Studio's playlist viewer
in the order it appears on screen or using a custom order and/or exclude
certain columns. Press NVDA+V to toggle this behavior while focused on a
track in Studio's playlist viewer. To customize column inclusion and order,
from column announcement settings panel in add-on settings, uncheck
"Announce columns in the order shown on screen" and then customize included
columns and/or column order.

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

## Dialogue profils de diffusion

Vous pouvez sauvegarder les paramètres pour des émissions spécifiques dans
des profils de diffusion. Ces profils peuvent être gérés  via le dialogue
des profils de diffusion de SPL which can be accessible en pressant
Alt+NVDA+P depuis la fenêtre Studio.

## Mode tactile SPL

Si vous utilisez Studio sur un ordinateur possédant un écran tactile
fonctionnant sous Windows 8 ou version ultérieure et NVDA 2012.3 ou version
ultérieure installé, vous pouvez exécuter certaines commandes Studio depuis
un écran tactile. Tout d'abord utiliser une tape à trois doigts pour
basculer en mode SPL, puis utilisez les commandes tactile énumérées
ci-dessus pour exécuter des commandes.

## Version 21.08

* In SAM encoders, NVDA will no longer play a tone if the selected encoder
  becomes idle as this tone is really meant to help when debugging the
  add-on.

## Version 21.06

* NVDA ne se figera plus ou ne jouera plus de tonalités d'erreur en essayant
  d'ouvrir divers dialogues d'extension tels que le dialogue des paramètres
  d'encodeur. Il s'agit d'un correctif critique requis pour prendre en
  charge NVDA 2021.1.
* NVDA ne semblera plus figé ou jouer des tonalités d'erreur en essayant
  d'annoncer le temps complet (heures, minutes, secondes) depuis Studio
  (commande non assignée). Cela affecte NVDA 2021.1 ou une version
  ultérieure.

## Version 21.04/20.09.7-LTS

* 21.04 : NVDA 2020.4 ou ultérieur est requis.
* Dans les encodeurs, NVDA n'échoue plus à annoncer l'information de date et
  heure lors de l'utilisation de la commande de date/heure (NVDA+F12). Cela
  affecte NVDA 2021.1 ou ultérieurs.

## Version 21.03/20.09.6-LTS

* La version minimum de Windows requise est maintenant liée aux versions de
  NVDA.
* Suppression de la commande d'e-mail de commentaires
  (Alt+NVDA+Tiret). Veuillez envoyer vos commentaires aux développeurs de
  l'extension en utilisant les informations de contact fournies par le
  gestionnaire d'extensions.
* 21.03 : Certaines parties du code source de l'extension incluent
  maintenant des annotations de type.
* 21.03 : le code de l'extension a été rendu plus robuste à l'aide de Mypy
  (unvérificateur de types statiques pour Python). en particulier,
  correction de plusieurs bogues anciens tels que l'impossibilité pour NVDA
  de rétablir les paramètres par défauts dans certaines circonstances et la
  tentative de sauvegarder les paramètres d'encodage quand ils ne sont pas
  chargés. Certains problèmes importants ont également été corrigés dans la
  version 20.09.6-LTS.
* Correction de nombreux bogues dans le dialogue de bienvenue de l'extension
  (Alt+NVDA+F1 depuis la fenêtre de Studio), incluant l'affichage de
  multiples dialogues de bienvenue et NVDA semblant ne rien faire ou
  émettant des signaux d'erreur quand le dialogue de bienvenue reste ouvert
  après fermeture de Studio.
* Correction de nombreux bogues dans le dialogue de commentaires de piste
  (Alt+NVDA+C trois fois depuis une piste dans Studio), incluant une
  tonalité d'erreur quand on essaie de sauvegarder des commentaires et
  plusieurs dialogues de commentaires de piste apparaissant si Alt+NVDA+C
  est pressé de nombreuses fois. Si le dialogue de commentaires de piste est
  encore affiché après fermeture de Studio, les commentaires ne seront pas
  sauvegardés.
* Diverses commandes de colonnes telles que l'explorateur de colonnes
  (Contrôle + NVDA + numéro de ligne) dans les pistes Studio et les annonces
  d'état des encodeurs ne donnent plus de résultats erronés lorsque NVDA est
  redémarré alors que le focus est sur les pistes ou les encodeurs. Cela
  affecte NVDA 2020.4 ou une version ultérieure.
* Correction de nombreux problèmes avec les instantanés de playlist (SPL
  Assistant, F8), y compris l'impossibilité d'obtenir des données
  d'instantané et de signaler les mauvaises pistes comme les pistes les plus
  courtes ou les plus longues.
* NVDA n'annoncera plus "0 éléments dans la bibliothèque" lorsque Studio se
  ferme au milieu d'une analyse de bibliothèque.
* NVDA n'échouera plus à enregistrer les modifications apportées aux
  paramètres de l'encodeur après que des erreurs soient rencontrées lors du
  chargement des paramètres de l'encodeur et que les paramètres sont ensuite
  réinitialisés aux valeurs par défaut.

## Version 21.01/20.09.5-LTS

La version 21.01 supporte SPL Studio 5.30 et ultérieurs.

* 21.01 : NVDA 2020.3 ou ultérieur est requis.
* 21.01 : le paramètre d'inclusion de l'en-tête de colonne a été supprimé
  des paramètres de l'extension . Le paramètre d'en-tête de colonne de
  tableau de NVDA contrôlera les annonces d'en-tête de colonne dans la suite
  SPL et les encodeurs.
* Ajout d'une commande pour basculer entre écran et inclusion de colonne
  personnalisée et réglage de l'ordre (NVDA+V). Notez que cette commande
  n'est disponible que lorsqu'une piste est focalisée dans la visionneuse de
  playlist de Studio.
* L'aide de l'assistant SPL et du contrôleur sera présentée sous forme de
  document en mode navigation au lieu d'une boîte de dialogue.
* NVDA n'arrêtera plus d'annoncer la progression de l'analyse de la
  bibliothèque s'il est configuré pour annoncer la progression de l'analyse
  lors de l'utilisation d'un afficheur braille.

## Version 20.11.1/20.09.4-LTS

* Premier support de StationPlaylist Studio 5.50.
* Améliorations apportées à la présentation de divers dialogue ajoutées
  grâce aux fonctionnalités NVDA 2020.3.

## Version 20.11/20.09.3-LTS

* 20.11 : NVDA 2020.1 ou ultérieur est requis.
* 20.11: Plus de problèmes de style de code ont été résolus ainsi que des
  bogues potentiels avec Flake8.
* Correction de divers problèmes avec le dialogue de bienvenue de
  l'extension (Alt+NVDA+F1 à partir de Studio), y compris une mauvaise
  commande affichée pour les commentaires du module complémentaire
  (Alt+NVDA+Tiret).
* 20.11 : Le format de présentation des colonnes pour les éléments de piste
  et d'encodeur dans la suite StationPlaylist (y compris l'encodeur SAM) est
  désormais basé sur le format d'élément de liste SysListView32.
* 20.11 : NVDA annoncera désormais les informations de colonne pour les
  pistes dans toute la suite SPL, quel que soit le paramètre « description
  de l'objet du rapport » dans le panneau des paramètres de présentation des
  objets de NVDA. Pour une meilleure expérience, laissez ce paramètre
  activé.
* 20.11 : Dans la visionneuse de playlist de Studio, l'ordre des colonnes
  personnalisé et le paramètre d'inclusion affecteront la présentation des
  colonnes de piste lors de l'utilisation de la navigation par objet pour se
  déplacer entre les pistes, y compris l'annonce de l'objet du navigateur
  actuel.
* Si l'annonce de la colonne verticale est définie sur une autre que «
  quelle que soit la colonne que j'examine », NVDA n'annoncera plus les
  données de colonne erronées après avoir modifié la position de la colonne
  à l'écran via la souris.
* présentation améliorée des transcriptions des listes de lecture (Assistant
  SPL, Maj+F8) lors de l'affichage de la transcription au format de tableau
  ou de liste HTML.
* 20.11 : Dans les encodeurs, les étiquettes des encodeurs seront annoncées
  lors de l'exécution de commandes de navigation par objet comme lors de
  l'appui sur les touches fléchées haut ou bas pour se déplacer entre les
  encodeurs.
* Dans les encodeurs, en plus de Alt+NVDA+0, l'appui sur F12 ouvrira
  également le dialogue des paramètres d'encodeur pour l'encodeur
  sélectionné.

## Version 20.10/20.09.2-LTS

* En raison de modifications apportées au format du fichier des paramètres
  de l'encodeur, l'installation d'une ancienne version de cette extension
  après l'installation de cette version entraînera un comportement
  imprévisible.
* Il n'est plus nécessaire de redémarrer NVDA avec le mode de journalisation
  de débogage pour lire les messages de débogage depuis la visionneuse de
  journal. Vous pouvez afficher les messages de débogage si le niveau de
  journalisation est défini sur "déboguer" à partir du panneau des
  paramètres généraux de NVDA.
* Dans la visionneuse de playlist de Studio, NVDA n'inclura pas les en-têtes
  de colonne si ce paramètre est désactivé dans les paramètres de
  l'extension et si l'ordre des colonnes personnalisé ou les paramètres
  d'inclusion ne sont pas définis.
* 20.10 : le paramètre d'inclusion de l'en-tête de colonne des paramètres de
  l'extension est obsolète et sera supprimé dans une future version. À
  l'avenir, le paramètre d'en-tête de colonne de table de NVDA contrôlera
  les annonces d'en-tête de colonne dans la suite SPL et les encodeurs.
* Lorsque SPL Studio est minimisé dans la barre d'état système (zone de
  notification), NVDA annoncera ce fait lorsqu'il essaiera de basculer vers
  Studio à partir d'autres programmes soit via une commande dédiée, soit à
  la suite d'une connexion d'encodeur.

## Version 20.09-LTS

La version 20.09.x est la dernière série de versions à prendre en charge
Studio 5.20 et basée sur d'anciennes technologies, les futures versions
prenant en charge Studio 5.30 et les fonctionnalités NVDA plus
récentes. Certaines nouvelles fonctionnalités seront rétroportées vers
20.09.x si nécessaire.

* En raison de changements dans NVDA, le commutateur de ligne de commande
  --spl-configvolatile n'est plus disponible pour rendre les paramètres de
  l'extension en lecture seule. Vous pouvez émuler cela en décochant la case
  "Enregistrer la configuration en quittant NVDA" dans le panneau des
  paramètres généraux de NVDA.
* Suppression du paramètre des fonctionnalités pilotes de la catégorie
  Paramètres avancés sous les paramètres de l'extension (Alt+NVDA+0),
  utilisé pour permettre aux utilisateurs de versions de développement de
  tester le code de pointe.
* Les commandes de navigation dans les colonnes de Studio sont désormais
  disponibles dans les listes de pistes trouvées dans les demandes d'écoute,
  les pistes d'insertion et d'autres écrans.
* Diverses commandes de navigation dans les colonnes se comporteront comme
  les commandes de navigation dans les tables de NVDA. En plus de simplifier
  ces commandes, cela apporte des avantages tels que la facilité
  d'utilisation par les utilisateurs malvoyants.
* Les commandes de navigation verticale dans les colonnes (Ctrl+Alt+flèche
  haut/bas) sont désormais disponibles pour Creator, l'éditeur de liste de
  lecture, Remote VT et Track Tool.
* La commande d'exploration de colonnes de pistes (Control+NVDA+tiret) est
  maintenant disponible dans l'éditeur de création de playlist et dans VT à
  distance.
* La commande de visualisation des colonnes de piste respectera l'ordre des
  colonnes à l'écran.
* Dans l'encodeur SAM, amélioration de la réactivité de NVDA à l'appui de
  Contrôle+F9 ou Contrôle+F10 pour connecter ou déconnecter tous les
  encodeurs, respectivement. Cela peut provoquer une verbosité accrue à
  l'annonce des informations sur l'encodeur sélectionné.
* Dans les encodeurs SPL et AltaCast, l'appui sur F9 connectera maintenant
  l'encodeur sélectionné.

## Anciennes versions

S'il vous plaît voir le lien changelog pour les notes de version  pour les
anciennes versions de l'extension.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[3]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
