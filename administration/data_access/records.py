from sqlalchemy import select, Insert, Update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from administration.entities.models.client import Client
from administration.entities.models.record import Record
from administration.entities.schemas.record import RecordCreateUpdate


async def get_records(db: AsyncSession):
    query = select(Record).options(
        selectinload(Record.client),
        selectinload(Record.spot),
    )
    result = await db.execute(query)
    return result.scalars().all()


async def get_record_by_id(db: AsyncSession, record_id: int):
    result = await db.get(Record, record_id)
    return result


async def get_records_by_client(db: AsyncSession, client_id: int):
    query = select(Record).join(Client, Record.client_id == Client.id).where(Record.client_id == client_id)
    result = await db.execute(query)
    return result.scalars().all()


async def delete_record(db: AsyncSession, record: Record):
    await db.delete(record)
    await db.commit()


async def add_record(db: AsyncSession, record: RecordCreateUpdate):
    query = Insert(Record).values(client_id=record.client_id, spot_id=record.spot_id)
    await db.execute(query)
    await db.commit()


async def update_record(record_id: int, db: AsyncSession, record: RecordCreateUpdate):
    _record = await get_record_by_id(db, record_id)
    query = Update(Record).values(client_id=_record.client_id if not record.client_id else record.client_id,
                                  spot_id=_record.spot_id if not record.spot_id else record.spot_id)
    await db.execute(query)
    await db.commit()
    return _record
