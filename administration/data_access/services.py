from sqlalchemy import select, Insert, Update
from sqlalchemy.ext.asyncio import AsyncSession

from administration.entities.models.area import Area
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
    query = select(Service).join(Area, Service.area).where(area_id=area_id)
    result = await db.execute(query)
    return result.scalars().all()


async def delete_service(db: AsyncSession, service: Service):
    await db.delete(service)
    await db.commit()


async def add_service(db: AsyncSession, service: ServiceCreateUpdate):
    query = Insert(Service).values(price=service.price, title=service.title, area_id=service.area_id)
    await db.execute(query)
    await db.commit()


async def update_service(service_id: int, db: AsyncSession, service: ServiceCreateUpdate):
    _service = await get_service_by_id(db, service_id)
    query = Update(Service).values(title=_service.title if not service.title else service.title,
                                   price=_service.price if not service.price else service.price,
                                   area_id=_service.area_id if not service.area_id else service.area_id
                                   )
    await db.execute(query)
    await db.commit()
    return _service
