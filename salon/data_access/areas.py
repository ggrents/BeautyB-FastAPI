from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from salon.entities.models.area import Area


async def get_areas(db: AsyncSession):
    query = select(Area)
    result = await db.execute(query)
    return result.scalars().all()


async def get_area_by_id(db: AsyncSession, area_id: int):
    result = await db.get(Area, area_id)
    return result


async def delete_area(db: AsyncSession, area: Area) -> None:
    await db.delete(area)
    await db.commit()
