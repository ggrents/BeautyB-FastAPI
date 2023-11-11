from sqlalchemy import select, Insert, Update
from sqlalchemy.ext.asyncio import AsyncSession

from administration.entities.models.service import Service
from administration.entities.schemas.service import ServiceCreateUpdate


async def get_services(db: AsyncSession):
    query = select(Service)
    result = await db.execute(query)
    return result.scalars().all()


async def get_service_by_id(db: AsyncSession, service_id: int):
    result = await db.get(Service, service_id)
    return result


async def get_services_by_area(db: AsyncSession, area_id: int):
    query = select(Service).where(area_id=area_id)
    result = await db.execute(query)
    return result.scalars().all()


async def delete_service(db: AsyncSession, service: Service):
    await db.delete(service)
    await db.commit()


async def add_service(db: AsyncSession, service: ServiceCreateUpdate):
    query = Insert(Service).values(**service)
    await db.execute(query)


async def update_service(db: AsyncSession, service: ServiceCreateUpdate):
    query = Update(Service).values(**service)
    await db.execute(query)
