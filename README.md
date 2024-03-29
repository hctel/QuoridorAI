# QuoridorAI - Projet Informatique ECAM 2024
Ce repo GitHub contient l'entièreté du code du client de résolution pour le jeu Quoridor. Celui ci a été créé dans le cadre du projet informatique 2024 de l'[ECAM](https://www.ecam.be/).

## Fonctionnement
Le fichier Main.py contient la classe principale du programme. C'est dans celle-ci que l'interface entre le réseau et l'algorithme de résolution est faite.

### Classe Network
Cette classe gère la connection réseau avec le gestionnaire de partie (GP). Elle se comporte en tant que client pour l'inscription de notre client auprès du GP, puis en tant que serveur pour répondre entre autres aux requètes de ping et de coup.