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
    query = select(Master).join(Area, Master.area).where(Master.area_id==area_id)
    result = await db.execute(query)
    return result.scalars().all()


async def delete_master(db: AsyncSession, master: Master):
    await db.delete(master)
    await db.commit()


async def add_master(db: AsyncSession, master: MasterCreateUpdate):
    query = Insert(Master).values(first_name=master.first_name, last_name=master.last_name,
                                  gender=master.gender, phone=master.phone, salary=master.salary,
                                  address=master.address,
                                  area_id=master.area_id)
    await db.execute(query)
    await db.commit()


async def update_master(master_id: int, db: AsyncSession, master: MasterCreateUpdate):
    _master = await get_master_by_id(db,master_id)
    query = Update(Master).values(first_name=_master.first_name if not master.first_name else master.first_name,
                                  last_name=_master.last_name if not master.last_name else master.last_name,
                                  gender=_master.gender if not master.gender else master.gender,
                                  phone=_master.phone if not master.phone else master.phone,
                                  salary=_master.salary if not master.salary else master.salary,
                                  address=_master.address if not master.address else master.address,
                                  area_id=_master.area_id if not master.area_id else master.area_id
                                  )
    await db.execute(query)
    await db.commit()
