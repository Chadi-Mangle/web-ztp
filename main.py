"""Fichier pour lancer le serveur fastapi"""
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from db.database import get_db

from db.models import Client
from db.schema import ClientSchema

app = FastAPI()

@app.post("/client")
async def add_client(client: ClientSchema, db: AsyncSession = Depends(get_db)):
    """Permet d'ajouter un client à la bdd"""
    new_client = Client(mac=str(client.mac), ip=str(client.ip))
    db.add(new_client)
    await db.commit()
    await db.refresh(new_client)
    return new_client

@app.get("/clients")
async def get_clients(db: AsyncSession = Depends(get_db)):
    """Recupère la liste des clients"""
    results = await db.execute(select(Client))
    clients = results.scalars().all()
    return clients
