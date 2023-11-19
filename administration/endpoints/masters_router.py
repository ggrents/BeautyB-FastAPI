from http.client import OK
from typing import Annotated

from fastapi import APIRouter, Depends, Path, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession

from administration.data_access import masters
from administration.database import get_async_session
from administration.entities.schemas.master import MasterCreateUpdate, GetMaster

master_router = APIRouter(prefix="/masters", tags=["Masters"])


@master_router.get("", response_model=list[GetMaster])
async def list_masters(db: AsyncSession = Depends(get_async_session)):
    return await masters.get_masters(db)


@master_router.get("/{master_id}", response_model=GetMaster)
async def get_master_by_id(master_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    master = await masters.get_master_by_id(db, master_id)
    if not master:
        raise HTTPException(status_code=404, detail="Master not found")
    return master


@master_router.get("/area/{area_id}", response_model=list[GetMaster])
async def get_master_by_area(area_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    master = await masters.get_masters_by_area(db, area_id)
    if not master:
        raise HTTPException(status_code=404, detail="Master not found")
    return master


@master_router.post("", response_model=GetMaster)
async def add_master(master: Annotated[MasterCreateUpdate, Body()],
                     db: AsyncSession = Depends(get_async_session)):
    await masters.add_master(db, master)
    return master


@master_router.patch("/{master_id}", response_model=GetMaster)
async def update_master(master_id: Annotated[int, Path()], master: Annotated[MasterCreateUpdate, Body()],
                        db: AsyncSession = Depends(get_async_session)):
    _master = await masters.get_master_by_id(db, master_id)
    await masters.update_master(master_id, db, master)
    return master


@master_router.delete("/{master_id}")
async def delete_master(master_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    master = await masters.get_master_by_id(db, master_id)
    if not master:
        raise HTTPException(status_code=404, detail="Service not found")
    await masters.delete_master(db, master)
    return OK
