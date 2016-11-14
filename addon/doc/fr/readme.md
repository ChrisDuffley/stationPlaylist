# StationPlaylist Studio #

* Auteurs: Geoff Shang, Joseph Lee et d'autres contributeurs.
* Télécharger [version stable][1]
* Télécharger [la version de développement][2]
* Télécharger [version prise en charge à long terme][3] - module
  complémentaire 15.x pour les utilisateurs de Studio 5.0x

Ce module complémentaire améliore l'utilisation de Station Playlist Studio,
mais il fournit aussi des utilitaires pour contrôler le Studio où que vous
soyez.

Pour plus d’informations sur le module complémentaire, lisez le [guide du
module complémentaire][4]. Pour les développeurs cherchant à savoir comment
construire le module complémentaire, voir buildInstructions.txt situé à la
racine du code source du module complémentaire du référentiel.

IMPORTANT : Ce module complémentaire nécessite NVDA 2015.3 ou plus récent et
StationPlaylist Studio 5.00 ou version ultérieure. Si vous avez installé
NVDA 2016.1 ou version ultérieure sur Windows 8 et supérieur désactiver le
Mode d'atténuation audio. En outre,le module complémentaire 8.0/16.10
nécessite Studio 5.10 et ultérieure, et pour les diffusions utilisant Studio
5.0x, une version prise en charge à long terme (7.x) est disponible.

## Raccourcis clavier

* Alt+Maj+T depuis la fenêtre de Studio : annonce le temps écoulé pour la
  piste en cours de lecture.
* Contrôle+Alt+T (glissement à deux doigts vers le bas en mode tactile SPL)
  depuis la fenêtre de Studio : annoncer le temps restant pour la piste en
  cours de lecture.
* NVDA+Maj+F12 (glissement à deux doigts vers le haut en mode tactile SPL)
  depuis la fenêtre de Studio: annonce le temps de diffusion par exemple 5
  minutes à la fin de l'heure.
* Alt+NVDA+1 (glissement à deux doigts vers la droite en mode SPL) depuis la
  fenêtre de Studio: Ouvre la boîte de dialogue  paramètre fin de piste.
* Alt+NVDA+2 (glissement à deux doigts vers la gauche en mode tactile SPL)
  depuis la fenêtre de Studio: Ouvre la boîte de dialogue  paramètre alarme
  chanson intro.
* Alt+NVDA+3 depuis la fenêtre de Studio : Basculer l'explorateur de chariot
  pour apprendre les assignations de chariot.
* Alt+NVDA+4 depuis la fenêtre de Studio : Ouvre le dialogue alarme
  microphone.
* Contrôle+NVDA+f depuis la fenêtre de Studio : Ouvre un dialogue pour
  chercher une piste en se basant sur l'artiste ou le nom de la
  chanson. Appuyez  sur NVDA+F3 pour chercher vers l'avant ou appuyez sur
  NVDA+Maj+F3 pour rechercher vers l'arrière.
* Alt+NVDA+R depuis la fenêtre de Studio : parcourt les paramètres d'annonce
  du balayage dans la bibliothèque.
* Contrôle+Maj+X depuis la fenêtre de Studio : Parcourt les paramètres du
  minuteur braille.
* Contrôle+Alt+flèche droite/gauche (alors que  a été mis en focus sur une
  piste) : Annoncer colonne de piste suivante/précédente.
* Contrôle+NVDA+1 jusqu'à 0 (6 pour Studio 5.0x) : Annoncer le contenu de la
  colonne pour une colonne spécifiée.
* Alt+NVDA+C alors que  a été mis en focus sur une piste : annonce les
  commentaires de piste le cas échéant.
* Alt+NVDA+0 depuis la fenêtre de Studio : Ouvre le dialogue de
  configuration du module complémentaire Studio.
* Contrôle+NVDA+- (tiret) depuis la fenêtre de Studio : Envoyez vos
  commentaires au développeur du module complémentaire en utilisant le
  client de messagerie par défaut.
* Alt+NVDA+F1: Ouvre le dialogue de bienvenue.

## Commandes non assignées

Les commandes suivantes ne sont pas assignées par défaut ; si vous souhaitez
en assigner une, utilisez le dialogue Gestes de commandes pour ajouter des
commandes personnalisées.

* Basculement vers la fenêtre SPL Studio depuis n'importe quel programme.
* Couche Contrôleur SPL.
* Couche Assistant SPL depuis SPL Studio.
* Annoncer le temps y compris les secondes depuis SPL Studio.
* Basculement du cadran de piste entre activé ou désactivé (fonctionne
  correctement quand une piste a le focus ; pour assigner une commande pour
  cela, se déplacer sur une piste en Studio, puis ouvrez le dialogue Gestes
  de Commandes de NVDA.).
* Annonce de la température.
* Annonce du titre de la piste suivante si planifié.
* Annonçant le titre de la piste en cours de lecture.
* Marquage de piste en cours pour le début de l'analyse de durée de piste.
* Effectuer des analyses de durée de piste.
* Recherche de texte dans des colonnes spécifiques.
* Trouver des piste avec une durée qui se situe dans un intervalle donné via
  la recherche de l'intervalle de temps.
* Activer ou désactiver les métadonnées en streaming rapidement.

## Commandes supplémentaires lors de l'utilisation des encodeurs de Sam ou SPL

Les commandes suivantes sont disponibles lorsque vous utilisez les encodeurs
de Sam ou de SPL :

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
* Contrôle+NVDA+3 depuis l'Encodeur SPL : Paramètres de l'encodeur.
* Contrôle+NVDA+4 depuis l'Encodeur SAM : Statut de la connexion de
  l'encodeur.
* Contrôle+NVDA+4 depuis l'Encodeur SPL : Statut de la connexion ou du taux
  de transfert.
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
* C (disposition JAWS et Window-Eyes) : Bascule l'explorateur de chariot
  (visionneuse de playlist uniquement).
* D (R dans la disposition de JAWS) : Durée restante pour la playlist (si un
  message d’erreur est donné, se déplacer vers la visionneuse de playlist et
  puis tapez cette commande).
* E (G dans la disposition de Window-Eyes) : Statut de métadonnées en
  streaming.
* Maj+1 jusqu'à maj+4, maj+0 : Statut de Métadonnées individuelles en
  streaming URLs (0 est pour l'encodeur DSP).
* E (disposition de Window-Eyes) : Temps écoulé pour la piste en cours de
  lecture.
* F : Recherche de piste (visionneuse de playlist uniquement).
* H : Durée de la musique pour la tranche horaire en cours.
* Maj+H : Durée des pistes restantes pour la tranche horaire.
* I (L dans la disposition de JAWS ou Window-Eyes) : Nombre d'auditeurs.
* K : Se déplacer à la piste marquée (visionneuse de playlist uniquement).
* Contrôle+K : Définir la piste en cours comme le marqueur de position de
  piste (visionneuse de playlist uniquement).
* L (Maj+L dans la  disposition de JAWS et Window-Eyes) : Entrée ligne.
* M : Microphone.
* N : Titre pour la piste suivante planifié.
* P : Statut (en cours de lecture ou arrêté).
* Maj+P : Hauteur de la piste actuelle.
* R (Maj+E dans la disposition  de JAWS et Window-Eyes) : Enregistrer dans
  un fichier activé/désactivé.
* Maj+R : Contrôle du balayage de la bibliothèque en cours.
* S : Piste débute dans (planifié).
* Maj+S : Durée jusqu'à la piste sélectionnée qui va être jouer.
* T : Mode édition chariot activé/désactivé.
* U: temps de fonctionnement Studio.
* Contrôle+Maj+U : Rechercher les mises à jour du module complémentaire.
* W: Météo et température si configurée.
* Y: Statut de la modification de la playlist.
* 1 jusqu'à 0 (6 pour Studio 5.0x) : Annoncer le contenu de la colonne pour
  une colonne spécifiée.
* F9 : Marquer la piste en cours pour l'analyse de durée de piste
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
* Appuyez sur E pour obtenir un nombre et des étiquettes pour les encodeurs
  étant contrôlés.
* Appuyez sur I pour obtenir le nombre d'auditeurs.
* Appuyez sur F1 pour afficher une boîte de dialogue d'aide qui répertorie
  les commandes disponibles.

## Alarmes de la piste

Par défaut, NVDA jouera un bip si il y'a cinq secondes restantes dans la
piste (outro) et/ou intro. Pour configurer cette valeur aussi bien quant à
les activer ou désactiver, appuyer sur Alt+NVDA+1 ou Alt+NVDA+2 pour ouvrir
les boîtes de dialogues fin de piste et la montée de la chanson,
respectivement. De plus, Utiliser la boîte de dialogue paramètres du module
complémentaire Studio pour configurer si vous entendrez un bip, un message
ou tous les deux lorsque les alarmes sont basculés sur activé.

## Alarme microphone

Vous pouvez demander à NVDA de lire un son lorsque le microphone est actif
depuis un certain temps. Appuyez sur Alt+NVDA+4 pour configurer l'heure de
l'alarme en secondes (0 désactive celui-ci).

## Chercheur de piste

Si vous souhaitez trouver rapidement une chanson par artiste ou par nom de
chanson, depuis la liste de piste, appuyez sur Contrôle+NVDA+F. Tapez le nom
de l'artiste ou le nom de la chanson. NVDA va vous placer soit à la chanson
Si cell-ci est trouvé ou il affichera une erreur si elle ne trouve pas la
chanson que vous recherchez. Pour trouver une chanson précédemment entrée ou
artiste, appuyez sur NVDA+F3 ou NVDA+Maj+F3 Pour trouver en avant ou en
arrière.

Remarque: le Chercheur de piste est sensible à la casse.

## Explorateur de Chariot

Selon l'édition, SPL Studio permet d'assigné jusq'à 96 chariots pendant la
lecture. NVDA vous permet d'entendre quel chariot ou jingle est assigné à
ces commandes.

Pour apprendre les assignations de chariot, depuis SPL Studio, appuyez sur
Alt+NVDA+3. Appuyant une fois sur la commande chariot il vous dira à quel
jingle est assignée à la commande. Appuyant deux fois sur la commande il
jouera le jingle. appuyez sur Alt+NVDA+3 pour quitter l'explorateur de
chariot. Consultez la documentation du module complémentaire pour plus
d'informations sur l'explorateur de chariot.

## Cadran de Piste

Vous pouvez utiliser les touches fléchées pour visualiser divers
informations sur une piste. Pour activer le Cadran de Piste si une piste a
le focus dans la visionneuse de playlist principale, appuyez sur la commande
que vous avez assignés vous permettant d'alterner le Cadran de Piste. Puis
utilisez les touches fléchées gauche et droite pour visualiser les
informations telles que l'artiste, la durée et ainsi de suite. Sinon appuyer
sur Contrôle+Alt+flèches gauche ou droite pour naviguer entre les colonnes
sans invoquer le Cadran de Piste.

## Analyse de durée de piste

Pour obtenir la longueur pour jouer les pistes sélectionnés, marquer la
piste en cours pour le début de l'analyse de durée de piste (Assistant SPL,
F9), puis appuyer sur Assistant SPL, F10 lorsque vous atteignez la fin de la
sélection.

## Explorateur de Colonnes

En appuyant sur Contrôle+NVDA+1 jusqu'à 0 (6 pour Studio 5.0x) ou Assistant
SPL, 1 jusqu'à 0 (6 pour Studio 5.01 ou version antérieure), vous pouvez
obtenir le contenu des colonnes spécifiques. Par défaut ce sont artiste,
titre, durée, intro, catégorie et nom du fichier (Studio 5.10 ajoute année,
album, genre et heure prévue). Vous pouvez configurer les colonnes qui
seront explorées via le dialogue Explorateur de Colonnes trouvé dans le
dialogue Paramètres module complémentaire.

## Boîte de dialogue configuration

Depuis la fenêtre studio, vous pouvez appuyer sur Alt+NVDA+0 pour ouvrir la
boîte de dialogue configuration du module complémentaire. Sinon, allez dans
le menu préférences de NVDA et sélectionnez l'élément Paramètres SPL
Studio. Cette boîte de dialogue est également utilisé pour gérer les profils
de diffusion.

## Mode tactile SPL

Si vous utilisez Studio sur un ordinateur possédant un écran tactile
fonctionnant sous Windows 8 ou version ultérieure et NVDA 2012.3 ou version
ultérieure installé, vous pouvez exécuter certaines commandes Studio depuis
un écran tactile. Tout d'abord utiliser une tape à trois doigts pour
basculer en mode SPL, puis utilisez les commandes tactile énumérées
ci-dessus pour exécuter des commandes.

## Version 16.11/15.3-LTS

* Premier support de StationPlaylist Studio 5.20, y compris une meilleure
  réactivité lors de l'obtention des informations du statut telles que
  l’automatisation du statut via la couche de l'Assistant SPL.
* Correction des problèmes liés à la recherche de pistes et à l'interaction
  avec celles-ci, y compris l'impossibilité de cocher ou de décocher le
  marqueur de position de piste ou une piste trouvée via le dialogue
  Recherche de l'intervalle de temps.
* L'ordre d'annonce des colonnes ne revient plus à l'ordre par défaut après
  modification.
* 16.11: Si les profils de diffusion ont des erreurs, la boîte de dialogue
  d'erreur ne cessera plus de s'afficher.

## Version 16.10.1/15.2-LTS

* Vous pouvez maintenant interagir avec la piste qui a été trouvé via la
  Recherche de Piste (Contrôle+NVDA+F) tel que la vérification pour la
  lecture.
* Mises à jour des traductions.

## Changements pour la version 8.0/16.10/15.0-LTS

La version 8.0 (également connu sous le nom de 16.10) prend en charge la
version SPL Studio 5.10 et ultérieure, avec la 15.0-LTS (anciennement la
7.x) conçu pour fournir de nouvelles fonctionnalités depuis la 8.0 pour les
utilisateurs des versions antérieures de Studio. À moins que dans le cas
contraire les rubriques ci-dessous s’appliquent à les deux, 8.0 et 7.x. Un
dialogue d'avertissement apparaît la première fois que vous utilisez le
module complémentaire 8.0 avec Studio 5.0x installé, vous demandant
d’utiliser la version  7.x LTS.

* Le Schéma de la version a changé pour refléter la version year.month au
  lieu de major.minor. Au cours de la période de transition (jusqu'au
  mi-2017), la version 8.0 est synonyme de la version 16.10, avec la 7.x LTS
  étant désigné la 15.0 en raison des changements incompatibles.
* Le code source du module complémentaire est désormais hébergé sur GitHub
  (référentiel  localisé à https://github.com/josephsl/stationPlaylist).
* Ajouter un dialogue de Bienvenue qui se lance au démarrage de Studio après
  l’installation du module complémentaire. Une commande (NVDA+AltF1) a été
  ajoutée pour rouvrir ce dialogue une fois rejeté.
* Changements de diverses commandes du module complémentaire, y compris la
  suppression du basculement des annonces des statut (Contrôle+NVDA+1),
  réassigné Alarme de fin de piste à Alt+NVDA+1, basculement  de
  l'Explorateur de Chariot  est maintenant Alt+NVDA+3, le dialogue alarme
  microphone est Alt+NVDA+4 et le dialogue Paramètres du module
  complémentaire/encodeur est Alt+NVDA+0. Cela a été fait pour permettre
  d'être Assigner  à Contrôle+NVDA+rangée de numéro à l'Explorateur de
  Colonnes.
* 8.0: Relâché la restriction de l'Explorateur de colonnes à la place dans
  la  7.x donc les  chiffres 1 jusq'à 6 peuvent être configurés pour
  annoncer les colonnes dans Studio 5.1x.
* 8.0: La commande  pour le basculement du Cadran de piste et  les paramètre
  correspondant dans les paramètres du module complémentaire sont obsolètes
  et seront supprimées dans la 9.0. Cette commande restent disponible dans
  le module complémentaire 7.x.
* Ajouté Contrôle+Alt+début/fin pour déplacer le Navigateur de Colonne à la
  première ou la dernière colonne dans la Visionneuse de playlist.
* Vous pouvez maintenant ajouter, afficher, modifier ou supprimer les
  commentaires (notes) de la piste. Appuyer sur Alt+NVDA+C depuis une piste
  dans la visionneuse de playlist pour entendre les commentaires si défini,
  appuyez deux fois pour copier le commentaire dans le presse-papiers  ou
  trois fois pour ouvrir un dialogue pour modifier les commentaires.
* Ajoutée la possibilité d'annoncer si un commentaire de piste existe,ainsi
  que d’un paramètre dans les paramètres du module complémentaire pour
  contrôler comment cela devrait être fait.
* Ajouter un nouveau paramètre dans le dialogue paramètres du module
  complémentaire pour permettre a NVDA de vous notifier si vous avez atteint
  le haut ou le bas de la visionneuse de playlist.
* Lors de la réinitialisation des paramètres du module complémentaire, vous
  pouvez maintenant spécifier quel type de restauration vous souhaitez
  avoir. Par défaut, les paramètres du module complémentaire seront
  réinitialisés, avec des cases à cocher pour la réinitialisation des
  changement de profil immédiat, pofil basé sur l'heure, paramètres de
  l’encodeur et les commandes pour effacer la piste ajouté pour
  réinitialiser la boîte de dialogue Paramètres.
* Dans l'Outil de piste, vous pouvez obtenir des informations sur l'album et
  le code du CD en appuyant sur Contrôle+NVDA+9 et Contrôle+NVDA+0,
  respectivement.
* Amélioration des performances lors de l’obtention des informations de
  colonne pour la première fois dans l'Outil de Piste.
* 8.0: Ajouté un dialogue dans les paramètres du module complémentaire pour
  configurer les tranches de l'Explorateur de Colonnes pour l'Outil de
  Piste.
* Vous pouvez maintenant configurer l'intervalle alarme microphone depuis le
  dialogue Alarme microphone (Alt+NVDA+4).

## Version 7.5/16.09

* NVDA n'affichera plus la fenêtre de la boîte de dialogue de la progression
  de la mise à jour si le canal de mise à jour du module complémentaire
  vient de changer.
* NVDA honorera le canal de mise à jour sélectionnée lors du téléchargement
  des mises à jour.
* Mises à jour des traductions.

## Version 7.4/16.08

Version 7.4 est également connu comme 16.08 selon le numéro de version
year.month pour les publications stable.

* Il est possible de sélectionner le canal de mise à jour du module
  complémentaire depuis les paramètres du module complémentaire/Options
  avancées pour être supprimé plus tard en 2017. Pour 7.4, les canaux
  disponibles sont bêta, stable et long-terme.
* Ajouté un paramètre dans les paramètres du module complémentaire/Options
  avancées pour configurer l'intervalle de recherche de mise à jour entre 1
  et 30 jours (par défaut est 7 ou recherches hebdomadaire).
* La commande pour le Contrôleur SPL et la commande pour la mise en focus de
  Studio ne sera pas disponibles à partir des écrans sécurisés.
* Nouvelles et mises à jour des traductions et l'ajout de documentation
  localisé en plusieurs langues.

## Changements pour la version 7.3

* Amélioration des performances légère quand on regarde les informations
  telles que l’automatisation via certaines commandes de l'Assistant SPL.
* Mises à jour des traductions.

## Changements pour la version 7.2

* En raison de la suppression du format de l'ancien style de configuration
  interne, il est obligatoire d'installer le module complémentaire 7.2. Une
  fois installé, vous ne pouvez pas revenir à une version antérieure du
  module complémentaire.
* Ajout d'une commande dans le Contrôleur SPL pour annoncer le nombre
  d'auditeurs (I).
* Vous pouvez maintenant ouvrir le dialogue Paramètres module complémentaire
  SPL et le dialogue Paramètres de l'encodeur en appuyant sur
  Alt+NVDA+0. Vous pouvez toujours utiliser Contrôle+NVDA+0 pour ouvrir ces
  boîtes de dialogue (pour être supprimé dans le module complémentaire 8.0).
* Dans l'Outil de Piste, vous pouvez utiliser Contrôle+Alt+les touches
  flèche gauche ou flèche droite pour naviguer entre les colonnes.
* Contenu de diverses boîtes de dialogue de Studio comme la boîte de
  dialogue À propos dans Studio 5.1x sont maintenant annoncées.
* Dans l'Encodeur SPL NVDA fera arrêter la tonalité de connexion si la
  connexion automatique est activée, et puis désactivée depuis le menu
  contextuel alors que l’encodeur sélectionné se connecte.
* Mises à jour des traductions.

## Changements pour la version 7.1

* Correction des erreurs rencontrés lors de la mise à niveau depuis le
  module complémentaire 5.5 et en dessous de la 7.0.
* Lorsque vous répondez "non" lors de la réinitialisation des paramètres du
  module complémentaire, vous retourné à la boîte de dialogue Paramètres
  module complémentaire et NVDA se souviendra du paramètre changement de
  profil immédiat.
* NVDA vous demandera de reconfigurer les étiquettes de flux et d’autres
  options de l'encodeur si le fichier de configuration de l'encodeur est
  endommagé.

## Changements pour la version 7.0

* Ajouté la fonction Rechercher une mise à jour du module
  complémentaire. Cela peut se faire manuellement (Assistant SPL,
  Contrôle+Maj+U) ou automatiquement (configurable depuis la boîte de
  dialogue Options avancées dans la boîte de dialogue paramètres du module
  complémentaire).
* Il n'est plus nécessaire de rester dans la fenêtre de la visionneuse de
  playlist afin d'invoquer la plupart des commandes couche Assistant SPL ou
  obtenir des annonces de temps tels que le temps restant pour la piste et
  le temps de diffusion.
* Changements des commandes Assistant SPL, y compris Durée de la playlist
  (D), réassignation de durée de sélection de l'heure de Maj+H à Maj+S et
  Maj+H maintenant utilisé pour annoncer la Durée des pistes restantes pour
  la tranche horaire courante, la commande Statut de Métadonnées en
  streaming réassignée (1 jusqu'à 4, 0 est maintenant Maj+1 jusqu'à Maj+4,
  Maj+0).
* Il est maintenant possible d'invoquer Recherche de piste via l'Assistant
  SPL (F).
* Assistant SPL, chiffres 1 jusqu'à 0 (6 pour Studio 5.01 ou version
  antérieure) peut être utilisé pour annoncer les informations d'une colonne
  spécifique. Ces tranches de colonne peuvent être modifiés sous l'élément
  Explorateur de Colonnes dans la boîte de dialogue Paramètres module
  complémentaire.
* Corrigé les nombreuses erreurs signalées par les utilisateurs lors de
  l'installation du module complémentaire 7.0 pour la première fois lorsque
  aucune version antérieure de ce module complémentaire a été installé.
* Améliorations apportées au Cadran de Piste, y compris la meilleure
  réactivité lors d’un déplacement dans les colonnes et le suivi de comment
  les colonnes sont présentées à l'écran.
* Ajoutée la possibilité d'appuyer sur Contrôle+Alt+touches flèche gauche ou
  flèche droite pour se déplacer entre les colonnes de piste.
* Il est maintenant possible d'utiliser une commande différente   pour la
  disposition du lecteur d'écran pour les commandes Assistant SPL. Aller
  dans la boîte de dialogue Options avancées depuis Paramètres module
  complémentaire pour configurer cette option entre les dispositions NVDA,
  JAWS et Window-Eyes. Voir les commandes Assistant SPL ci-dessus pour plus
  de détails.
* NVDA peut être configuré pour basculer vers un profil de diffusion
  spécifique à un jour et à une heure spécifier. Utiliser la nouvelle boîte
  de dialogue Déclencheurs dans Paramètres module complémentaire pour
  configurer cela.
* NVDA annoncera le nom du profil lors du basculement vers via le changement
  immédiat (Assistant SPL, F12) ou comme un résultat du profil basé sur
  l'heure lequel devient actif.
* Déplacé la bascule du changement immédiat(maintenant une case à cocher)
  vers la nouvelle boîte de dialogue Déclencheurs.
* Entrées dans la liste déroulante des profils dans la boîte de dialogue
  Paramètres module complémentaire maintenant s'affiche le drapeaux du
  profil par exemple actif, que ce soit un changement de profil immédiat et
  ainsi de suite.
* Si un problème sérieux avec le fichier lors de la lecture du profil de
  diffusion on été trouvés, NVDA présentera une boîte de dialogue d'erreur
  et va réinitialiser les paramètres par défaut au lieu de ne rien faire ou
  donnera une tonalité d'erreur.
* Les paramètres seront sauvegardés sur le disque si et seulement si vous
  modifiez les paramètres. Ceci prolonge la vie des SSD (solid state drives(
  en empêchant les arrêts inutiles sur le disque si aucun paramètres n’ont
  été modifiés.
* Dans le dialogue paramètres du module complémentaire les contrôles
  utilisés pour basculer l'annonce de l'heure prévue, le nombre d'auditeurs,
  le nom du chariot et le nom de la piste a été déplacé vers un dialogue
  Annonces des statut (sélectionnez  le bouton annonce de statut pour ouvrir
  cette boîte de dialogue).
* Ajouter un nouveau paramètre dans le dialogue paramètres du module
  complémentaire pour permettre a NVDA de jouer un bip pour les différentes
  catégories de piste lors du déplacement entre les pistes dans la
  visionneuse de playlist.
* Tentative lors de l'ouverture de l'option de configuration de métadonnées
  dans le dialogue de paramètres du module complémentaire alors que le
  dialogue rapide de métadonnées en streaming est ouvert ne provoquera plus
  que NVDA ne puisse rien faire ou de jouer une tonalité d’erreur. NVDA va
  maintenant vous demander de fermer le dialogue de métadonnées en streaming
  avant que vous puissiez ouvrir les paramètres du module complémentaire.
* En annonçant le temps comme le temps restant pour la piste en cours de
  lecture, les heures sont également annoncées. Par conséquent, le réglage
  pour l'annonce des heures est activé par défaut.
* Appuyant sur le Contrôleur SPL, R permet maintenant a NVDA d’annoncer le
  temps restant en heures, minutes et secondes (minutes et secondes s’il
  s’agit d’un tel cas).
* Dans les encodeurs, en appuyant sur contrôle + NVDA + 0 se présentera le
  dialogue Paramètres de l'encodeur permettant de configurer différentes
  options telles que l'étiquette de flux, en plaçant le focus à Studio
  lorsqu'il est connecté et ainsi de suite.
* Dans les encodeurs, il est maintenant possible de désactiver la tonalité
  de progression de connexion (configurable à partir  de la boîte  de
  dialogue paramètres de l'encodeur).

## Changements pour la version 6.4

* Correction d'un problème majeur lors du retour au basculement d'un profil
  à partir d'un changement de profil immédiat et d'un changement de profil
  immédiat devenue active à nouveau, vu après la suppression d'un profil qui
  a été positionné juste avant le profil précédemment actif. Lorsque vous
  essayez de supprimer un profil, une boîte de dialogue d'avertissement
  s'affichera si un changement de profil immédiat est actif.

## Changements pour la version 6.3

* Améliorations de la sécurité interne.
* Lorsque le module complémentaire 6.3 ou version ultérieure est tout
  d'abord lancé sur un ordinateur fonctionnant sous Windows 8 ou supérieur
  avec NVDA 2016.1 ou installé par la suite, un dialogue d'alerte
  s'affichera vous demandant pour désactiver le Mode d'atténuation audio
  (NVDA+Maj+D). Sélectionnez la case à cocher pour supprimer cette boîte de
  dialogue à l'avenir.
* Ajouté une commande pour envoyer des rapports de bugs, des suggestions de
  fonctionnalité et autres commentaires aux développeurs du module
  complémentaire (Contrôle+NVDA+tiret (trait d'union, "-")).
* Mises à jour des traductions.

## Changements pour la version 6.2

* Correction d'un problème avec la commande reste de la playlist (Assistant
  SPL, D (R si le mode de compatibilité est activé)) lorsque la durée de
  l'heure actuelle a été annoncée par opposition à la playlist entière (le
  comportement de cette commande peut être configuré à partir des Paramètres
  Avancés dans la boîte de dialogue Paramètres du module complémentaire).
* NVDA peut maintenant annoncer le nom de la piste en cours de lecture tout
  en utilisant un autre programme (configurable depuis les paramètres du
  module complémentaire).
* Le paramètre utilisé pour laisser la commande Contrôleur SPL pour appeler
  l'Assistant SPL est maintenant honoré (auparavant elle a été activée en
  permanence).
* Dans les encodeurs SAM, les commandes Contrôle+F9 et Contrôle+F10
  fonctionne maintenant correctement.
* Dans les encodeurs, lorsqu'un encodeur est mis en focus tout d'abord et si
  cet encodeur est configuré pour contrôler en arrière-plan, NVDA va
  maintenant démarrer le contrôle en arrière-plan automatiquement.

## Changements pour la version 6.1

* L'ordre des colonnes annoncer et inclusion, ainsi que les paramètres de
  métadonnées en streaming sont maintenant des paramètres spécifiques au
  profil.
* Lors du changement de profils, les flux de métadonnées correct seront
  activées.
* Lors de l'ouverture de la boîte de dialogue paramètres rapide de
  métadonnées en streaming (commande non assignée), les paramètres modifiés
  sont maintenant appliqués au profil actif.
* Lors du démarrage de Studio, changé la façon dont les erreurs s'affichent
  si le seul profil corrompu est le profil normal.
* Lorsque vous modifiez certains paramètres à l'aide de raccourcis clavier
  tels que  les annonces de statut, corrigé un problème où les paramètres
  modifiés ne sont pas conservées lors du basculement vers et depuis un
  changement de profil  immédiat.
* Lorsque vous utilisez une commande Assistant SPL avec un geste
  personnalisé défini (tel que  la commande piste suivante), il n'est plus
  nécessaire de rester dans la visionneuse de playlist de Studio pour
  utiliser ces commandes (ils peuvent être effectuées depuis les autres
  fenêtres de Studio).

## Changements pour la version 6.0

* Nouvelles commandes de l'Assistant SPL, y compris annonçant le titre de la
  piste en cours de lecture (C), annonçant le statut des métadonnées en
  streaming (E, 1 jusqu'à 4 et 0) et l'ouverture du guide de l'utilisateur
  en ligne (Maj+F1).
* La possibilité de mmettre en bloc les paramètres favoris comme les profils
  de diffusion à utiliser lors d'une présentation et de basculer à un profil
  prédéfini. Consultez le guide du module complémentaire pour plus de
  détails sur les profils de diffusion.
* Ajouté un nouveau paramètre dans les paramètres du module complémentaire
  pour contrôler la verbosité du message (certains messages seront
  raccourcies lorsque la verbosité avancée est sélectionnée).
* Ajouté un nouveau paramètre dans les paramètres du module complémentaire
  pour laisser à NVDA annoncer les heures, minutes et secondes pour les
  commandes de durée de piste ou playlist  (caractéristiques affectée y
  compris annonçant le temps écoulé et restant de la piste en cours de
  lecture, l'analyse de durée de piste et d'autres).
* Vous pouvez maintenant demander à NVDA d'indiquer la longueur totale d'un
  intervalle des pistes  via la fonctionnalité d'analyse de durée de
  piste. Appuyer sur AssistantSPL, F9 pour marquer la piste en cours comme
  marqueur de début, se déplacer à la fin de l'intervalle de piste et
  appuyez sur Assistant SPL, F10. Ces commandes peuvent être réassignées
  donc on n'a pas à invoquer la couche Assistant SPL pour effectuer
  l'analyse de durée de piste.
* Ajouté une boîte de dialogue Recherche de colonne (commande non assignée)
  pour rechercher du texte dans des colonnes spécifiques tels que l'artiste
  ou une partie du nom du fichier.
* Ajouté la boîte de dialogue Recherche de l'intervalle de temps (commande
  non assignée) pour trouver une piste avec une durée qui se situe dans un
  intervalle spécifié, utile si je souhaite trouver une piste pour remplir
  une tranche horaire.
* Ajouté la possibilité de réorganiser l'annonce de la piste en colonne et
  pour supprimer l'annonce d'une  colonnes spécifiques si "utiliser l'ordre
  affichés sur l'écran" est non coché depuis la boîte de dialogue paramètres
  du module complémentaire. Utiliser la boîte de dialogue "Gérer les
  annonces de colonne" pour réorganiser les colonnes.
* Ajouté une boîte de dialogue (commande non assignée) pour basculer
  rapidement entre activer/désactiver des métadonnées en streaming.
* Ajouté un paramètre dans les paramètres du module complémentaire pour
  configurer lorsque le statut des métadonnées en streaming devraient être
  annoncée et pour activer des métadonnées en streaming.
* Ajouté la possibilité de marquer une piste comme un marqueur de position
  afin d'y revenir plus tard (Assistant SPL, Contrôle+K pour définir,
  Assistant SPL, K pour ce déplacer à la piste marquée).
* Amélioration des performances lorsque vous rechercher le texte sur la
  piste suivante ou précédente contenant le texte recherché.
* Ajouté un paramètre dans les paramètres du module complémentaire pour
  configurer la notification d'alarme (bip, message ou tous les deux).
* Il est maintenant possible de configurer l'alarme du microphone entre 0
  désactivé) et deux heures (7200 secondes) et d'utiliser les touches flèche
  haut et bas pour configurer ce paramètre.
* Ajouté un paramètre dans les paramètres du module complémentaire pour
  permettre une notification du microphone actif afin de le recevoir
  périodiquement.
* Vous pouvez maintenant utiliser la commande à bascule pour le Cadran de
  Piste en Studio pour  basculer le Cadran de Piste dans l'Outil de Piste
  sous réserve que vous n'assignez une commande pour basculer le Cadran de
  Piste dans l'Outil de Piste.
* Ajouté la possibilité d'utiliser la commande Couche Contrôleur SPL pour
  appeler la Couche de l'Assistant SPL (configurable depuis la boîte de
  dialogue paramètres avancé trouvé dans la boîte de dialogue paramètres du
  module complémentaire).
* Ajouté la possibilité pour NVDA d'utiliser certaines commandes de
  l'Assistant SPL utilisés par les autres lecteurs d'écran. Pour ce faire,
  allez dans les paramètres du module complémentaire, sélectionnez
  Paramètres Avancés et cochez la case à cocher mode compatibilité lecteur
  écran.
* Dans les encodeurs, les paramètres tels que la mise en focus de Studio
  lorsqu'il est connecté sont maintenant rappeler.
* Il est maintenant possible d'afficher plusieurs colonnes depuis la fenêtre
  de l'encodeur (tels que le statut de la connexion de l'encodeur) via
  Contrôle+NVDA+chiffre de la commande ; consulter les commandes de
  l'encodeur ci-dessus.
* Correction d'un bug rare où lors du basculement à Studio ou lors de la
  fermeture d'une boîte de dialogue NVDA ((y compris les boîtes de dialogue
  du module complémentaire Studio) d'empêché les commandes de piste (comme
  le basculement du Cadran de Piste) de fonctionner comme prévu.

## Changements pour la version 5.6

* Dans Studio 5.10 et versions ultérieures, NVDA n'annonce plus "non
  sélectionné" lorsque joue la  piste sélectionnée.
* Suite à un problème avec Studio lui-même, NVDA maintenant annoncera le nom
  de la piste en cours de lecture automatiquement. Une option pour
  activer/désactiver ce comportement a été ajoutée dans la boîte de dialogue
  paramètres du module complémentaire Studio.

## Changements pour la version 5.5

* Jouer après la configuration de la connexion se souviendra lors du
  déplacement en dehors de la fenêtre de l'encodeur.

## Changements pour la version 5.4

* En exécutant le balayage de la bibliothèque depuis la boîte de dialogue
  Insérer des pistes n'entraîne plus à NVDA de ne pas annoncer le statut du
  balayage ou jouer des tonalités d'erreur si NVDA est configuré pour
  annoncer l'avancement du balayage de la bibliothèque ou le nombre de
  balayages.
* Mises à jour des traductions.

## Changements pour la version 5.3

* La correction du bogue faisant que l'Encodeur SAM (ne lisait pas la piste
  suivante si une piste est en cours de lecture et lorsque l'encodeur se
  connecte), est maintenant disponible pour les utilisateurs de l'encodeur
  SPL.
* NVDA n'affiche plus d'erreurs et ne manque plus de réagir quand, dans
  l'assistant de SPL, F1, (Dialogue de l'aide de l'assistant) est actionnée.

## Changements pour la version 5.2

* NVDA ne permettra plus à ces deux boîtes de dialogue paramètres et alarme
  d'être ouverte. Un avertissement apparaît vous demandant de fermer la
  boîte de dialogue ouverte préalablement avant d'ouvrir une autre boîte de
  dialogue.
* Lors du contrôle d'un ou plusieurs encodeurs en appuyant sur le Contrôleur
  SPL, E annoncera maintenant le nombre d'encodeur, l'ID de l'encodeur et
  l'étiquette(s) de flux dans le cas échéant.
* NVDA supporte toutes les commandes connecter/déconnecter
  (Contrôle+F9/Contrôle+F10) dans les encodeurs SAM.
* NVDA ne  lira plus la piste suivante si un encodeur se connecte alors que
  Studio est entrain de lire une piste et Studio on lui dit de lire les
  pistes lorsqu'un encodeur est connecté.
* Mises à jour des traductions.

## Changements pour la version 5.1

* Il est maintenant possible de visualiser les colonnes individuelles dans
  l'Outil de piste via le Cadran  de piste (touche de basculement non
  assigné). Note ce Studio doit être activée avant d'utiliser ce mode.
* Ajouté une case à cocher   dans la boîte de dialogue paramètres du module
  complémentaire Studio pour basculer entre activer/désactiver l'annonce du
  nom du chariot en cours de lecture.
* Le basculement du microphone entre  activer/désactiver via le contrôleur
  SPL n'entraîne plus de tonalités d'erreur afin d'être lu ou basculer entre
  activer/désactiver le son pour ne pas être lu.
* Si une commande personnalisée est assignée pour une commande couche
  Assistant SPL et cette commande est appuyée correctement après d'avoir
  entré dans l'Assistant SPL, NVDA maintenant, va rapidement quitter
  l'Assistant SPL.

## Changements pour la version 5.0

* Une boîte de dialogue de configuration dédié pour le module complémentaire
  SPL a été ajoutée, accessible depuis le menu préférences de NVDA ou en
  appuyant sur Contrôle+NVDA+0 depuis la fenêtre SPL.
* Ajouté la possibilité de réinitialiser tous les paramètres aux valeurs par
  défaut via la boîte de dialogue configuration.
* Si certains des paramètres ont des erreurs, seul les paramètres concernés
  seront réinitialisés aux valeurs par défaut.
* Ajouté un Mode écran tactile dédié à SPL et des commandes tactile pour
  exécuter diverses commandes Studio.
* Changements de couche Assistant SPL incluent l'ajout de la commande aide
  couche (F1) et suppression des commandes pour alterner entre
  activer/désactiver nombre d'auditeurs (Maj+I) et anonce du temps planifier
  (Maj+S). Vous pouvez configurer ces paramètres dans la boîte de dialogue
  paramètres du module complémentaire.
* Renommé "bascule  entre activé/désactivé l'annonce" à "l'annonce de
  statut" comme les bips sont utilisés pour annoncer les autres informations
  de statut comme l'exécution du balayage de la bibliothèque.
* Le paramètre pour l'annonce de statut est maintenant conservé dans les
  sessions. Auparavant, vous deviez configurer ce paramètre manuellement au
  démarrage de Studio.
* Vous pouvez maintenant utiliser la fonction Cadran de piste pour
  visualiser les colonnes dans une entrée de piste dans la visionneuse de
  playlist principale du Studio (pour basculer entre activer/désactiver
  cette fonction, appuyez sur la commande que vous avez assigné pour cette
  fonctionnalité).
* Vous pouvez maintenant assigner des commandes personnalisées pour écouter
  les informations de température ou pour annoncer le titre de la piste à
  venir si planifié.
* Ajouté une case à cocher dans la boîte de dialogue fin de piste et allarme
  chanson intro pour activer ou désactiver ces alarmes (cocher pour
  activer). Ceux-ci peuvent également être "configurée" depuis les
  paramètres du module complémentaire.
* Correction d'un problème où en appuyant sur la boîte de dialogue alarme ou
  sur les commandes  du chercheur de piste alors qu'une autre alarme ou la
  boîte de dialogue trouver est ouverte entraînerait qu'une autre instance
  de la même boîte de dialogue apparaisse. NVDA affichera un message vous
  demandant tout d'abord de fermer la boîte de dialogue préalablement
  ouverte.
* Changements et corrections  dans l'explorateur de chariot, y compris en
  explorant les  banques de chariot incorrect Lorsque l'utilisateur n'a pas
  le focus sur la visionneuse de playlist. L'explorateur de chariot va
  maintenant vérifiez que vous êtes dans la visionneuse de playlist.
* Ajouté la possibilité d'utiliser la commande Couche Contrôleur SPL pour
  appeler Assistant SPL (expérimental ; consulter le guide du module
  complémentaire sur la façon d'activer ceci).
* Dans les fenêtres de l'encodeur, la commande pour annoncer la date et
  l'heure de NVDA (NVDA+F12 par défaut) annoncera l'heure y compris en
  secondes.
* Vous pouvez maintenant contrôler différents encodeurs pour le statut de la
  connexion et pour les autres messages en appuyant sur Contrôle+F11 alors
  que l'encodeur que vous souhaitez contrôler a le focus (fonctionne mieux
  lorsque vous utilisez des encodeurs  SAM).
* Ajout d'une commande dans la couche Contrôleur SPL pour annoncer le statut
  des encodeurs étant contrôlés (E).
* Une solution de contournement est maintenant disponible pour corriger un
  problème où NVDA annonçait les étiquettes de flux pour les encodeurs
  incorrects, surtout après la suppression d'un encodeur (pour réaligner
  les étiquettes de flux, appuyez sur Contrôle+F12, puis sélectionnez la
  position de l'encodeur, que vous avez supprimé).

## Changements pour les versions 4.4/3.9

* La fonction du balayage de la bibliothèque fonctionne désormais dans
  Studio 5.10 (il nécessite la dernière version de Studio 5.10).

## Changements pour les versions 4.3/3.8

* Lors du basculement vers une autre partie du Studio tel que la boîte de
  dialogue insérer des pistes pendant que l'explorateur de chariot est
  active, NVDA n'annoncera plus le messages du chariot lorsque on appuie sur
  les touches chariot (par exemple, lors de la localisation d'une piste
  depuis la boîte de dialogue insérer des pistes).
* Nouvelles touches Assistant SPL, y compris le basculement de l'anonce du
  temps planifier  et le nombre d'auditeurs (Maj+S et Maj+I, respectivement,
  pas enregistré entre les sessions).
* En quittant Studio alors que les différentes boîtes de dialogue des alarme
  sont ouverts, NVDA détectera que Studio a été quitté et ne sauvera pas les
  valeurs des alarme récemment modifiée.
* Mises à jour des traductions.

## Changements pour les versions 4.2/3.7

* NVDA n'oubliera plus de conserver les nouvelles étiquettes et modifiés
  l'encodeur lorsqu'un utilisateur se déconnecte ou redémarre un ordinateur.
* Lorsque la configuration du module complémentaire devient corrompue au
  démarrage de NVDA, NVDA restaurera la configuration par défaut et affiche
  un message pour informer l'utilisateur de ce fait.
* Dans le module complémentaire 3.7, problème de focus vu lors de la
  suppression des pistes dans Studio 4.33 a été corrigée (même correctif est
  disponible pour les utilisateurs de Studio 5.0x dans le module
  complémentaire 4.1).

## Changements pour la version 4.1

* Dans Studio 5.0x, lors de la suppression d'une piste depuis la visionneuse
  de la playlist principale il ne provoque plus que NVDA annonce la piste en
  dessous de la piste récemment focalisée (plus perceptible si la deuxième à
  la dernière piste a été supprimée, auquel cas NVDA dit "inconnu").
* Correction de plusieurs problèmes de balayage de la bibliothèque dans
  Studio 5.10, y compris annonçant le nombre total d'éléments dans la
  bibliothèque lors de la tabulation à travers  de la boîte de dialogue
  Insérer des pistes et la verbalisation "balayage est en cours" lorsque
  vous essayer de contrôler les balayages de la bibliothèque via l'Assistant
  SPL.
* Lorsque vous utilisez un terminal braille avec Studio 5.10 et si une piste
  est coché, en appuyant sur espace pour cocher une piste ci-dessous le
  braille   il ne provoque plus et ne va pas renvoyer l'état récemment
  coché.

## Changements pour les versions 4.0/3.6

Version 4.0 supporte SPL Studio 5.00 et ultérieure , avec la 3.x est conçu
pour fournir de nouvelles fonctionnalités depuis la 4.0 pour les
utilisateurs des versions antérieures de Studio.

* Nouvelles touches Assistant SPL, y compris le temps planifier pour la
  piste (S), durée restante pour la playlist (D) et la température (W si
  configuré). En outre, pour Studio 5.x, ajouté modification playlist (Y) et
  hauteur de la piste (Maj+P).
* Nouvelles commandes Contrôleur SPL, y compris l'avancement  des balayages
  de la bibliothèque (Maj+R) et l'activation du microphone sans fondu
  (N). En outre, en appuyant sur F1 il apparaît une boîte de dialogue des
  commandes disponibles.
* Lors de l'activation ou la désactivation du microphone via le Contrôleur
  SPL, des bips seront joué pour indiquer si le statut est activé/désactivé.
* Les paramètres tels que le temps pour la fin de piste sont enregistrées
  dans un fichier de configuration dédié dans votre répertoire de
  configuration utilisateur et sont conservés au cours d'une mises à niveau
  du module complémentaire (version 4.0 et versions ultérieure).
* Ajout d'une commande (Alt+NVDA+2) pour définir l'heure de l'allarme
  chanson intro entre 1 et 9 secondes.
* Dans les boîtes de dialogue fin de piste et alarme intro, vous pouvez
  utiliser les flèches haut et bas pour changer les paramètres de
  l'alarme. Si vous saisissez une valeur erronée, la valeur pour l'alarme
  est définie à la valeur maximale.
* Ajout d'une commande (Contrôle+NVDA+4) pour définir une heure lorsque NVDA
  jouera un son lorsque le microphone est actif depuis un certain temps.
* Ajouté une fonctionnalité pour annoncer le temps en heures, minutes et
  secondes (commande non assigné).
* Il est maintenant possible de suivre le balayage de la bibliothèque depuis
  la boîte de dialogue Insérer des pistes ou depuis n'importe où et une
  commande dédiée (NVDA+Alt+R) pour activer/désactiver des options pour
  l'annonce du balayage de la bibliothèque.
* Support pour l'Outil de Piste, incluant la lecture d'un bip si une piste
  intro a été définie et les commandes pour annoncer des informations sur
  une piste comme la durée et le repère de position.
* Support pour l'Encodeur StationPlaylist (Studio 5.00 et ultérieure),
  offrant le même niveau de support comme trouvé dans le support pour
  l'Encodeur SAM.
* Dans les fenêtres de l'encodeur, NVDA ne lit plus les tonalités d'erreur
  lorsque NVDA on lui dit de basculer vers Studio dès la connexion à un
  serveur de streaming alors que la fenêtre Studio est minimisé.
* Les erreurs n'on sont plus entendu après la suppression d'un flux avec
  une étiquette de flux défini sur celui-ci.
* Il est maintenant possible de contrôler l'introduction et fin de piste via
  le braille en utilisant les options du minuteur braille (Contrôle+Maj+X).
* Correction d'un problème où la tentative de basculement vers la fenêtre
  Studio depuis n'importe quel programme, après que toutes les fenêtres ont
  été minimisées causé quelque chose d'autre visiblement.
* Lorsque vous utilisez Studio 5.01 et antérieure, NVDA n'annoncera  pas
  certaines informations du statut telles que le temps planifié plusieurs
  fois.

## Changements pour la version 3.5

* Lorsque NVDA démarre ou redémarre alors que la fenêtre principal de la
  playlist de Studio 5.10 est mis en focus, NVDA ne lira plus les tonalités
  d'erreur et/ou il ne vas pas annoncer les pistes précédentes et suivantes
  lorsque vous utiliser les touches fléché à travers les pistes.
* Correction d'un problème en essayant d'obtenir le temps restant et le
  temps écoulé pour une piste dans les versions ultérieures  de Studio 5.10.
* Mises à jour des traductions.

## Changements pour la version 3.4

* Dans l'explorateur de chariot, les chariots impliquant la touche contrôle
  (par exemple Ctrl+F1) sont maintenant gérées correctement.
* Mises à jour des traductions.

## Changements pour la version 3.3

* Lors de la connexion à un serveur de streaming en utilisant l'encodeur
  SAM, il n'est plus nécessaire de rester dans la fenêtre de l'encodeur,
  jusqu'à ce que la connexion est établie.
* Correction d'un problème où les commandes de l'encodeur (par exemple,
  l'étiqueteuse de flux) pourrait ne plus fonctionner lors du passage à la
  fenêtre SAM provenant d'autres programmes.

## Changements pour la version 3.2

* Ajout d'une commande dans le Contrôleur SPL pour annoncer le temps restant
  pour la piste en cours de lecture (R).
* Dans la fenêtre de l'Encodeur SAM, le message lorsque vous êtes en mode
  aide à la saisie pour la commande Maj+F11 a été corrigée
* Dans l'Explorateur de Chariot, Si Studio Standard est utilisé, NVDA
  avertira que les commandes numéros de ligne ne sont pas disponibles pour
  les assignations de chariot.
* Dans le Studio 5.10, le chercheur de piste ne lit plus les tonalités
  d'erreur lors de la recherche à travers les pistes.
* Traductions nouvelles et mises à jour.

## Changements pour la version 3.1

* Dans la fenêtre de l'Encodeur SAM, ajout d'une commande (Maj+F11) pour
  dire si Studio lit la première piste lorsqu'il est connecté.
* Correction de nombreux bugs lors de la connexion à un serveur dans
  l'Encodeur SAM, dont l'incapacité d'exécuter des commandes NVDA, NVDA
  n'annonçant pas lorsque la connexion a été établie et des tonalités
  d'erreur au lieu de bip de connexion étant lu lorsqu'il est connecté.

## Changements pour la version 3.0

* Ajout Explorateur de Chariot pour apprendre les assignations de chariot
  (jusqu'à 96 chariots peut être assigné).
* Ajout de nouvelles commandes, y compris le Temps de diffusion
  (NVDA+Maj+F12) et le Nombre d'auditeurs (i) et le suivant titre de la
  piste (n) dans l'Assistant SPL.
* Basculer entre activer/désactiver les messages tels que l'automatisation
  sont maintenant affichées en braille quelle que soit le paramètre de
  l'annonce de la bascule.
* Lorsque la fenêtre de StationPlaylist est minimisé dans la barre d'état
  système (zone de notification), NVDA annoncera cette action en essayant de
  basculer vers SPL provenant d'autres programmes.
* Tonalités d'erreur ils ne sont plus entendue lorsque l'annonce de bascule
  est défini pour les bips et le statut des messages autre que la bascule
  entre activer/désactiver sont annoncés (exemple: jouer les chariots).
* Tonalités d'erreur ils ne sont plus entendue lorsque en essayant d'obtenir
  des informations telles que le temps restant tandis que l'autre fenêtre de
  Studio autre que la liste de pistes (par exemple la boîte de dialogue
  Options) est mis en focus. Si l'information n'est pas trouvée, NVDA
  annonce cette action.
* Il est maintenant possible de rechercher une piste par nom
  d'artiste. Auparavant vous pouvez rechercher par titre de la piste.
* Support pour l'Encodeur SAM , y compris la possibilité d'étiqueter
  l'encodeur et une commande de bascule pour commuter au Studio lorsque
  l'encodeur sélectionné est connecté.
* L'aide du module complémentaire est disponible à partir du Gestionnaire de
  modules complémentaires.

## Changements pour la version 2.1

* Correction d'un problème où l'utilisateur était incapable d'obtenir des
  informations du statut telles que le statut de l'automatisation lorsque
  SPL 5.x a été lancée pendant l'exécution de NVDA.

## Changements pour la version 2.0

* Certains raccourcis clavier global  et app spécifiques ont été supprimé
  donc, vous pouvez assigner une commande personnalisée dans la boîte de
  dialogue Gestes de commandes (module complémentaire version 2.0 requiert
  NVDA 2013.3 ou version ultérieure).
* Ajout de plusieurs commandes dans Assistant SPL tels que le statut du mode
  édition chariot.
* Vous pouvez maintenant basculer vers SPL Studio même avec toutes les
  fenêtres minimisées (peut ne pas fonctionner dans certains cas).
* Augmenté Alarme fin de piste limiter à 59 secondes.
* Vous pouvez maintenant rechercher une piste dans une playlist
  (NVDA+Contrôle+F pour trouver, NVDA+F3 ou NVDA+Maj+F3 pour trouver en
  avant ou en arrière, respectivement).
* Les noms exacts des zones de liste déroulante sont maintenant annoncés par
  NVDA (par exemple, boîte de dialogue Options et écrans de configuration
  initiales SPL).
* Correction d'un problème où NVDA annonçait des informations erronées en
  essayant d'obtenir le temps restant pour une piste dans SPL Studio 5.

## Changements pour la version 1.2

* Lorsque Station Playlist 4.x est installé sur certains ordinateurs Windows
  8/8.1, c'est encore possible d'entendre le temps écoulé et restant pour
  une piste.
* Mises à jour des traductions.

## Changements pour la version 1.1

* Ajout d'une commande (contrôle+NVDA+2) pour définir l'heure de l'alarme
  pour la fin de piste.
* Correction d'un bug dans le noms du champ pour certains des champs
  d'édition les quells n'étaient pas annoncé (en particulier les champs
  d'édition dans la boîte de dialogue Options).
* Ajout de différentes traductions.


## Changements pour la version 1.0

* Première version.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=spl

[2]: http://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: http://spl.nvda-kr.org/files/get.php?file=spl-lts16

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide
