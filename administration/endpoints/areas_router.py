from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from administration.data_access.areas import get_areas
from administration.database import get_async_session

areas_router = APIRouter(prefix="/areas")


@areas_router.get("")
async def list_areas(db: AsyncSession = Depends(get_async_session)):
    return await get_areas(db)
