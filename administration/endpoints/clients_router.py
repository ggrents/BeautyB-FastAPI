from http.client import OK
from typing import Annotated
from fastapi import APIRouter, Depends, Path, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession

from administration.data_access import clients
from administration.database import get_async_session

from administration.entities.schemas.client import ClientCreateUpdate, GetClient

client_router = APIRouter(prefix="/clients", tags=["Clients"])


@client_router.get("", response_model=list[GetClient])
async def list_clients(db: AsyncSession = Depends(get_async_session)):
    return await clients.get_clients(db)


@client_router.get("/{client_id}")
async def get_client_by_id(client_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    client = await clients.get_client_by_id(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client


@client_router.post("")
async def add_client(client: Annotated[ClientCreateUpdate, Body()],
                     db: AsyncSession = Depends(get_async_session)):
    await clients.add_client(db, client)
    return client


@client_router.patch("/{client_id}")
async def update_client(client_id: Annotated[int, Path()], client: Annotated[ClientCreateUpdate, Body()],
                        db: AsyncSession = Depends(get_async_session)):
    _serv = await clients.get_client_by_id(db, client_id)
    await clients.update_client(client_id, db, client)
    return client

@client_router.delete("/{client_id}")
async def delete_client(client_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    client = await clients.get_client_by_id(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    await clients.delete_client(db, client)
    return OK
