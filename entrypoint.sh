#!/bin/bash

set -e

echo "Démarrage du script entrypoint.sh..."

echo "Attente de la base de données PostgreSQL..."
until nc -z -v -w30 db 5432; do
  echo "En attente de la base de données PostgreSQL..."
  sleep 1
done
echo "Base de données PostgreSQL prête !"

echo "Exécution des migrations..."
python manage.py migrate

echo "Chargement des modèles..."
python manage.py loaddata dhcp_config.json

echo "Collecte des fichiers statiques..."
python manage.py collectstatic --noinput

echo "Démarrage du serveur Django avec Gunicorn..."
exec gunicorn --bind 0.0.0.0:8000 webZtp.wsgi:application --workers 3 --timeout 120
