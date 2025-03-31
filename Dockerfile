FROM python:3.9-slim

WORKDIR /app

# Installation des dépendances système
RUN apt-get update && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

# Installation des dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY . .

# Donner les permissions d'exécution au script
RUN chmod +x entrypoint.sh

# Exposition du port pour le serveur web Django
EXPOSE 8000

# Commande de démarrage avec bash explicite
CMD ["/bin/bash", "entrypoint.sh"]