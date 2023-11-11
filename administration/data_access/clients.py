from sqlalchemy import select, Insert, Update
from sqlalchemy.ext.asyncio import AsyncSession

from administration.entities.models.master import Master
from administration.entities.models.client import Client
from administration.entities.schemas.client import ClientCreateUpdate


async def get_clients(db: AsyncSession):
    query = select(Client)
    result = await db.execute(query)
    return result.scalars().all()


async def get_client_by_id(db: AsyncSession, client_id: int):
    result = await db.get(Client, client_id)
    return result


async def delete_client(db: AsyncSession, client: Client):
    await db.delete(client)
    await db.commit()


async def add_client(db: AsyncSession, client: ClientCreateUpdate):
    query = Insert(Master).values(**client)
    await db.execute(query)


async def update_client(db: AsyncSession, client: ClientCreateUpdate):
    query = Update(Client).values(**client)
    await db.execute(query)
