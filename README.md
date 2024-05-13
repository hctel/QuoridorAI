# QuoridorAI - Projet Informatique ECAM 2024
Ce repo GitHub contient l'entièreté du code du client de résolution pour le jeu Quoridor. Celui ci a été créé dans le cadre du projet informatique 2024 de l'[ECAM](https://www.ecam.be/).

## Fonctionnement
Le fichier Main.py contient la classe principale du programme. C'est dans celle-ci que l'interface entre le réseau et l'algorithme de résolution est faite.

L'algorithme de résolution fait une recherche du meilleur coups à l'aide d'une function heuristic prenant en compte la distance Dijkstra du joueur et de l'adversaire, la distance direct (Manhattan) vers la ligne d'arrivée du joueur et de l'adversaire, le nombre de murs restant dans la main du joueur et de l'adversaire.

A chaque fois qu'un coup est demandé, l'algorithme de résolution génère une liste de tous les coups légaux parmi tous les coups possibles (4 déplacements + 8\*7\*2=112 murs).
Puis il parcourt cette liste de coups en leur attribuant un score en fonction de différents paramètres et leurs pondérations. Le coups ayant obtenu le meilleur score est sélectionné et envoyé en réseau au gestionnaire de partie (GP).

### Classe Network
Cette classe gère la connection réseau avec le gestionnaire de partie (GP). Elle se comporte en tant que client pour l'inscription de notre client auprès du GP, puis en tant que serveur pour répondre entre autres aux requètes de ping et de coup. 

### Fichier Trainer.py
Ce fichier nous a permis de déterminer les meilleures pondérations à utiliser dans notre algorithme, en utilisant une forme de génétique algorithmique. Il crée n instances de notre IA avec, au départ, des poids au hasard. Ensuite, nous fournissons en paramètre les poids ayant obtenu le meilleur score sur un pool, et recréons n instances avec de petites altérations sur les poids fournis.

## Bibliothèques utilisées
time : chronomètre durant le debug et attente pour que les threads fonctionnent correctement\
json : encoder et décoder des objets au format JSON\
random : générateur de nombre aléatoire durant l'entrainement\
hashlib : hashage du plateau de jeu\
socket : gérer tout le fonctionnement réseau\
threading : créer des threads qui fonctionnent en parrallèle\
multiprocessing : créer de réels processus séparés\
copy : pour copier de multiple listes imbriquées\
functools : permet de créer une clé de comparaison pour le tri\



## Membres du groupe
 - [Victor DEUVAERT](https://github.com/22054) (22054)
 - [Hugo de HEPCÉE](https://github.com/hctel) (22167) 
