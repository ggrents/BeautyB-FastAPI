from sqlalchemy import func, select, Insert, Update
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta

from administration.entities.models.master import Master
from administration.entities.models.service import Service
from administration.entities.models.spot import Spot
from administration.entities.schemas.spot import SpotCreateUpdate


async def get_spots(db: AsyncSession):
    query = select(Spot)
    result = await db.execute(query)
    return result.scalars().all()


async def get_spot_by_id(db: AsyncSession, spot_id: int):
    result = await db.get(Spot, spot_id)
    return result


async def get_spots_by_master(db: AsyncSession, master_id: int):
    query = select(Spot).join(Master, Spot.master_id == Master.id).where(master_id=master_id)
    result = await db.execute(query)
    return result.scalars().all()


async def get_spots_by_service(db: AsyncSession, service_id: int):
    query = select(Spot).join(Service, Spot.service_id == Service.id).where(service_id=service_id)
    result = await db.execute(query)
    return result.scalars().all()


async def get_todays_spots(db: AsyncSession):
    today = datetime.now().date()
    query = select(Spot).where(func.DATE(Spot.timestamp) == today)
    result = await db.execute(query)
    return result.scalars().all()


async def get_todays_spots_by_service(db: AsyncSession, service_id: int):
    today = datetime.now().date()
    query = select(Spot).where(
        (Spot.service_id == service_id),
        (func.DATE(Spot.timestamp) == today)
    )
    result = await db.execute(query)
    return result.scalars().all()


async def get_todays_spots_by_master(db: AsyncSession, master_id: int):
    today = datetime.now().date()
    query = select(Spot).where(
        (Spot.master_id == master_id),
        (func.DATE(Spot.timestamp) == today)
    )
    result = await db.execute(query)
    return result.scalars().all()


async def delete_spot(db: AsyncSession, spot: Spot):
    await db.delete(spot)
    await db.commit()


async def add_spot(db: AsyncSession, spot: SpotCreateUpdate):
    query = Insert(Spot).values(**spot)
    await db.execute(query)


async def update_spot(db: AsyncSession, spot: SpotCreateUpdate):
    query = Update(Spot).values(**spot)
    await db.execute(query)
