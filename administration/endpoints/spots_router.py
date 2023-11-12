from http.client import OK
from typing import Annotated

from fastapi import APIRouter, Depends, Path, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession

from administration.data_access import services, spots
from administration.database import get_async_session
from administration.entities.schemas.spot import SpotCreateUpdate, GetSpot

spot_router = APIRouter(prefix="/spots", tags=["Spots"])


@spot_router.get("", response_model=list[GetSpot])
async def list_spots(db: AsyncSession = Depends(get_async_session)):
    return await spots.get_spots(db)


@spot_router.get("/{spot_id}", response_model=GetSpot)
async def get_spot_by_id(spot_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    spot = await spots.get_spot_by_id(db, spot_id)
    if not spot:
        raise HTTPException(status_code=404, detail="Spot not found")
    return spot


@spot_router.get("/master/{master_id}", response_model=list[GetSpot])
async def get_spot_by_master(master_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    spot = await spots.get_spots_by_master(db, master_id)
    if not spot:
        raise HTTPException(status_code=404, detail="Spots not found")
    return spot


@spot_router.get("/today/all", response_model=list[GetSpot])
async def get_spot_todays(db: AsyncSession = Depends(get_async_session)):
    spot = await spots.get_todays_spots(db)
    if not spot:
        raise HTTPException(status_code=404, detail="Spots not found")
    return spot


@spot_router.get("/today/master/{master_id}", response_model=list[GetSpot])
async def get_spot_by_master_todays(master_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    spot = await spots.get_todays_spots_by_master(db, master_id)
    if not spot:
        raise HTTPException(status_code=404, detail="Spots not found")
    return spot


@spot_router.get("/today/service/{service_id}", response_model=list[GetSpot])
async def get_spot_by_master_todays(service_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    spot = await spots.get_todays_spots_by_service(db, service_id)
    if not spot:
        raise HTTPException(status_code=404, detail="Spots not found")
    return spot


@spot_router.post("", response_model=GetSpot)
async def add_spot(spot: Annotated[SpotCreateUpdate, Body()],
                   db: AsyncSession = Depends(get_async_session)):
    await spots.add_spot(db, spot)
    return spot


@spot_router.patch("/{spot_id}", response_model=GetSpot)
async def update_spot(spot_id: Annotated[int, Path()], spot: Annotated[SpotCreateUpdate, Body()],
                      db: AsyncSession = Depends(get_async_session)):
    _serv = await spots.get_spot_by_id(db, spot_id)
    return await spots.update_spot(spot_id, db, spot)


@spot_router.delete("/{spot_id}")
async def delete_spot(spot_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    spot = await spots.get_spot_by_id(db, spot_id)
    if not spot:
        raise HTTPException(status_code=404, detail="Service not found")
    await spots.delete_spot(db, spot)
    return OK
