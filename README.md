<p align="center">
    <img src="image/image2.png" align="center" width="30%">
</p>
<p align="center"><h1 align="center">WEB-ZTP</h1></p>
<p align="center">
    <em><code>❯ Fait par : Chadi, Nassim, Ilyes, Lucas</code></em>
</p>

# Projet ZTP - Zero Touch Provisioning

## Description

Ce projet vise à développer une plateforme complète de gestion et de configuration automatisée des équipements réseau via le concept de **Zero Touch Provisioning (ZTP)**. L’objectif est d’automatiser la configuration des appareils à la première connexion (Day 0) grâce à un serveur DHCP intégré, des templates de configuration, et une interface web moderne et responsive.

La plateforme permet aussi le monitoring en temps réel des équipements, la gestion avancée des utilisateurs, ainsi que le déploiement facile via Docker.

---

## Installation

### Prérequis

- Docker et Docker Compose installés
- Python 3.x
- PostgreSQL

### Lancement rapide

1. Cloner le dépôt :  
   ```bash
   git clone https://github.com/Chadi-Mangle/web-ztp.git
   ```
2. Lancer le projet :
   ```bash
   docker-compose up -d build

---

## Architecture

```bash
ztp-project/
├── core/                       # App principale Django (gestion utilisateurs, dashboard)
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── ...
├── device/                     # App pour gestion des appareils et templates
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   └── ...
├── dhcp_server/                # App serveur DHCP intégré
│   ├── config/                 # Config spécifiques DHCP
│   ├── scripts/                # Scripts de gestion DHCP
│   ├── views.py
│   └── ...
├── monitoring/                 # App monitoring et logs
│   ├── templates/
│   ├── views.py
│   └── ...
├── user/                      # Gestion avancée utilisateurs (rôles, 2FA, LDAP)
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   └── ...
├── static/                    # Fichiers statiques globaux
├── templates/                 # Templates globaux
├── migrations/                # Migrations globales (si besoin)
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
├── README.md
└── roadmap.png                # Image de la roadmap

```

## Fonctionnalités principales

- **Gestion des utilisateurs**
  - Authentification (connexion, inscription, déconnexion)
  - Gestion du profil utilisateur (modification mot de passe, informations personnelles)

- **Dashboard & navigation**
  - Tableau de bord central avec statistiques (équipements, templates, appareils configurés)
  - Navigation dynamique avec Unpoly
  - Interface responsive et moderne

- **Gestion des appareils (Devices)**
  - Ajout, modification, suppression
  - Association de templates aux appareils
  - Visualisation de l’état des appareils (configuré / non configuré)
  - Variables spécifiques par appareil via template

- **Gestion des templates**
  - Création, modification, suppression
  - Association à plusieurs appareils
  - Visualisation des templates existants

- **Serveur DHCP intégré**
  - Serveur DHCP sur-mesure intégré
  - Interface web de configuration DHCP
  - Attribution automatique d’IP aux appareils

- **Zero Touch Provisioning (ZTP)**
  - Automatisation de la configuration des appareils à la première connexion
  - Chargement et application automatique des configurations via DHCP

- **Monitoring & logs**
  - Suivi en temps réel de l’état des appareils
  - Visualisation des logs (ajout, suppression, erreurs, etc.)

- **Aide & documentation**
  - Page d’aide intégrée
  - Lien vers documentation externe (GitHub Pages)

- **Pages d’erreur personnalisées** (403, 404, 429, 500)

- **Déploiement & maintenance**
  - Dockerisation complète (Dockerfile, docker-compose)
  - Scripts d’initialisation (migrations, fixtures, superuser)

---

## Roadmap (actuelle & future)

La roadmap détaille les fonctionnalités déjà mises en place ainsi que celles prévues pour les évolutions futures. 

<p align="center">
    <img src="image/image.png" align="center" width="80%">
</p>
<p align="center">
    <img src="image/image1.png" align="center" width="80%">
</p>

