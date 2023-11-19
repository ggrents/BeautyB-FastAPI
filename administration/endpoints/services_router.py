from http.client import OK
from typing import Annotated

from fastapi import APIRouter, Depends, Path, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession

from administration.data_access import services
from administration.database import get_async_session
from administration.entities.schemas.service import ServiceCreateUpdate, GetService

service_router = APIRouter(prefix="/services", tags=["Services"])


@service_router.get("", response_model=list[GetService])
async def list_services(db: AsyncSession = Depends(get_async_session)):
    return await services.get_services(db)


@service_router.get("/{service_id}", response_model=GetService)
async def get_service_by_id(service_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    service = await services.get_service_by_id(db, service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service


@service_router.get("/area/{area_id}", response_model=list[GetService])
async def get_service_by_area(area_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    service = await services.get_services_by_area(db, area_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service


@service_router.post("")
async def create_service(service: Annotated[ServiceCreateUpdate, Body()],
                         db: AsyncSession = Depends(get_async_session)):
    await services.add_service(db, service)
    return service


@service_router.patch("/{service_id}")
async def update_service(service_id: Annotated[int, Path()], service: Annotated[ServiceCreateUpdate, Body()],
                         db: AsyncSession = Depends(get_async_session)):
    _serv = await services.get_service_by_id(db, service_id)
    return await services.update_service(service_id, db, service)


@service_router.delete("/{service_id}")
async def delete_service(service_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    service = await services.get_service_by_id(db, service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    await services.delete_service(db, service)
    return OK
