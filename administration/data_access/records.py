from sqlalchemy import select, Insert, Update
from sqlalchemy.ext.asyncio import AsyncSession

from administration.entities.models.client import Client
from administration.entities.models.record import Record
from administration.entities.schemas.record import RecordCreateUpdate


async def get_records(db: AsyncSession):
    query = select(Record)
    result = await db.execute(query)
    return result.scalars().all()


async def get_record_by_id(db: AsyncSession, record_id: int):
    result = await db.get(Record, record_id)
    return result


async def get_records_by_client(db: AsyncSession, client_id: int):
    query = select(Record).join(Client, Record.client_id == Client.id).where(client_id=client_id)
    result = await db.execute(query)
    return result.scalars().all()


async def delete_record(db: AsyncSession, record: Record):
    await db.delete(record)
    await db.commit()


async def add_record(db: AsyncSession, record: RecordCreateUpdate):
    query = Insert(Record).values(**record)
    await db.execute(query)


async def update_record(db: AsyncSession, record: RecordCreateUpdate):
    query = Update(Record).values(**record)
    await db.execute(query)
