# TP - Pratiques proactives de sécurité Web (DevSecOps)

Ce dépôt contient les travaux réalisés dans le cadre du TP sur les pratiques proactives de sécurité web. L'objectif principal est d'intégrer des outils de sécurité de manière continue et automatisée directement dans le cycle de développement logiciel, en s'appuyant sur une culture DevSecOps.

## 🛠️ Outils et technologies

* **Langage** : Python avec le micro-framework Flask
* **CI/CD** : GitHub Actions pour l'automatisation des workflows
* **Analyse de Code Statique (SAST)** : CodeQL pour scanner le code source à la recherche de vulnérabilités
* **Analyse des Dépendances** : Dependabot pour la gestion des bibliothèques vulnérables

## 🚀 Démarche du projet

Le projet a été mis en place en suivant une démarche d'intégration continue de la sécurité :

1.  **Initialisation du projet** : Une application web simple a été créée et poussée sur ce dépôt GitHub.
2.  **Configuration du pipeline CI/CD** : Un premier workflow GitHub Actions a été mis en place pour s'exécuter à chaque `push` sur le dépôt.
3.  **Intégration de la sécurité** :
    * **CodeQL** a été ajouté au pipeline pour analyser le code. Une **vulnérabilité d'injection de commande** a été volontairement introduite dans le code pour démontrer la capacité de détection de l'outil.
    * **Dependabot** a été activé sur le dépôt. Une **dépendance volontairement obsolète et vulnérable** a été utilisée pour montrer comment Dependabot génère des alertes et propose des correctifs.

Les résultats de ces analyses sont visibles dans l'onglet **"Security"** de ce dépôt.

## 🧠 Quiz de sensibilisation à la sécurité

Pour renforcer la compréhension des vulnérabilités web de manière ludique, un quiz interactif a été préparé.

➡️ **Participer au quiz via Google Forms :** [https://forms.gle/Vp1XYBLtrMJKvAbN6](https://forms.gle/Vp1XYBLtrMJKvAbN6)

## 🚩 CTF (Capture The Flag) - Bientôt disponible

Une plateforme de CTF est en cours de développement afin de s'exercer à l'exploitation de failles de sécurité courantes dans un environnement contrôlé.

Les challenges prévus sont :
* Injection SQL simple
* Upload de fichier malveillant
* Exécution de commande shell via une vulnérabilité

## ✍️ Auteur

* Sylvain BOURGEOIS
