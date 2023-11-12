from sqlalchemy import select, Insert, Update
from sqlalchemy.ext.asyncio import AsyncSession
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
    query = Insert(Client).values(first_name=client.first_name,
                                  last_name=client.last_name,
                                  gender=client.gender,
                                  phone=client.phone,
                                  address=client.address)
    await db.execute(query)
    await db.commit()


async def update_client(client_id: int, db: AsyncSession, client: ClientCreateUpdate):
    _client = await get_client_by_id(client_id)
    query = Update(Client).values(first_name=_client.first_name if not client.first_name else client.first_name,
                                  last_name=_client.last_name if not client.last_name else client.last_name,
                                  gender=_client.gender if not client.gender else client.gender,
                                  phone=_client.phone if not client.phone else client.phone,
                                  address=_client.address if not client.address else client.address
                                  )
    await db.execute(query)
    await db.commit()
