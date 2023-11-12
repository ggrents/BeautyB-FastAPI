from http.client import OK
from typing import Annotated

from fastapi import APIRouter, Depends, Path, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from administration.data_access import areas
from administration.database import get_async_session


areas_router = APIRouter(prefix="/areas",tags=["Areas"])


@areas_router.get("")
async def list_areas(db: AsyncSession = Depends(get_async_session)):
    return await areas.get_areas(db)


@areas_router.get("/{area_id}")
async def get_area_by_id(area_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    area = await areas.get_area_by_id(db, area_id)
    if not area:
        raise HTTPException(status_code=404, detail="Area not found")
    return area


@areas_router.delete("/{area_id}")
async def del_area(area_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    area = await areas.get_area_by_id(db, area_id)
    if not area:
        raise HTTPException(status_code=404, detail="Area not found")
    await areas.delete_area(db, area)
    return OK
