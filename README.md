# air-paradis-NLP-flask

Ce dépôt contient une application Flask pour l'analyse des sentiments sur Twitter. L'application utilise un modèle de traitement du langage naturel (NLP) pour prédire le sentiment (positif ou négatif) d'un tweet donné. ✨🐦

## Prérequis

Avant de pouvoir exécuter l'application, assurez-vous d'avoir les éléments suivants installés :

- Python (version 3.7 ou supérieure) 🐍
- Les packages Python répertoriés dans le fichier `requirements.txt` 📦

## Installation

1. Clonez ce dépôt GitHub sur votre machine locale :
```bash
git clone https://github.com/votre-utilisateur/air-paradis-NLP-flask.git
```
   
2. Accédez au répertoire du projet :
  ```bash
  cd air-paradis-NLP-flask
  ```

3. Installez les dépendances requises en exécutant la commande suivante :
  ```bash
  pip install -r requirements.txt
  ```

## Utilisation

1. Assurez-vous d'être toujours dans le répertoire du projet.

2. Lancez l'application en exécutant la commande suivante :
  ```bash
  python app.py
  ```

3. Accédez à l'application dans votre navigateur en ouvrant l'URL suivante : http://localhost:5000 🌐🚀

4. Saisissez votre tweet dans le champ de texte et cliquez sur le bouton "Prédire" pour obtenir le sentiment prédit. 💭🔮

## Fonctionnement de l'application
- L'application utilise le modèle entraîné GLOVE_LSTM_traite pour prédire le sentiment d'un tweet donné.
- Le fichier model.py contient les fonctions nécessaires pour charger le modèle et effectuer des prédictions.
- Le fichier app.py est responsable de la gestion des requêtes HTTP et de l'affichage des résultats sur la page web.

## Remarques
- Assurez-vous d'avoir une connexion Internet active pour que l'application puisse fonctionner correctement. 🌐
- Si vous souhaitez déployer cette application sur un serveur de production, vous pouvez utiliser Gunicorn en exécutant la commande suivante :
  ```bash
  gunicorn app:app
  ```

Assurez-vous d'avoir configuré correctement Gunicorn pour votre environnement de déploiement. 🚀🔧
