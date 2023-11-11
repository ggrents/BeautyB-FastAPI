from sqlalchemy import select, Insert, Update
from sqlalchemy.ext.asyncio import AsyncSession

from administration.entities.models.area import Area
from administration.entities.models.master import Master
from administration.entities.schemas.master import MasterCreateUpdate


async def get_masters(db: AsyncSession):
    query = select(Master)
    result = await db.execute(query)
    return result.scalars().all()


async def get_master_by_id(db: AsyncSession, master_id: int):
    result = await db.get(Master, master_id)
    return result


async def get_masters_by_area(db: AsyncSession, area_id: int):
    query = select(Master).join(Area, Master.area).where(area_id=area_id)
    result = await db.execute(query)
    return result.scalars().all()


async def delete_master(db: AsyncSession, master: Master):
    await db.delete(master)
    await db.commit()


async def add_master(db: AsyncSession, master: MasterCreateUpdate):
    query = Insert(Master).values(**master)
    await db.execute(query)


async def update_master(db: AsyncSession, master: MasterCreateUpdate):
    query = Update(Master).values(**master)
    await db.execute(query)
