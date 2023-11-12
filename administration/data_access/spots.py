from sqlalchemy import func, select, Insert, Update, and_
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
    query = select(Spot).where(Spot.master_id == master_id).join(Master, Spot.master_id == Master.id)
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
        (Spot.service_id == service_id) & (func.DATE(Spot.timestamp) == today)
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
    query = Insert(Spot).values(timestamp=spot.timestamp, master_id=spot.master_id, service_id=spot.service_id)
    await db.execute(query)
    await db.commit()


async def update_spot(spot_id: int, db: AsyncSession, spot: SpotCreateUpdate):
    _spot = await get_spot_by_id(db, spot_id)
    query = Update(Spot).values(timestamp=_spot.timestamp if not spot.timestamp else spot.timestamp,
                                master_id=_spot.master_id if not spot.master_id else spot.master_id,
                                service_id=_spot.service_id if not spot.service_id else spot.service_id)

    await db.execute(query)
    await db.commit()
    return _spot
