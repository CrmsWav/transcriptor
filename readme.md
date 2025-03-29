# Fiston - Transcription Service

Ce projet met en place un service Flask pour transcrire des fichiers audio en texte grâce à Whisper.

## Structure
- **app.py** : API Flask
- **requirements.txt** : Dépendances Python
- **Procfile** : Commande de démarrage

## Installation
1. Cloner le dépôt :  
   `git clone https://github.com/<votre-utilisateur>/<votre-depot>.git`
2. Installer les dépendances :  
   `pip install -r requirements.txt`

## Utilisation
1. Lancer l’application :  
   `python app.py`
2. Envoyer un fichier audio en POST à `/transcribe` :
   - Exemple avec `curl` :  
     `curl -X POST -F "file=@/chemin/vers/audio.ogg" http://localhost:5000/transcribe`

## Déploiement
- Sur une plateforme PaaS (Railway, Heroku, etc.), la variable d’environnement `PORT` est utilisée.  
- Le fichier **Procfile** indique la commande à exécuter : `web: python app.py`
