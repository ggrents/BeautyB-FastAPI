import os
import shutil
from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile, File, Body
from sqlalchemy import select, Insert
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from administration.database import get_async_session
from catalogue.entities.models.image import Image
from catalogue.entities.models.video import Video
from catalogue.entities.schemas.image import GetFile, AddFile

file_router = APIRouter(prefix='/upload', tags=["Files"])


@file_router.get("/images", response_model=list[GetFile])
async def list_images(db: AsyncSession = Depends(get_async_session)):
    query = select(Image)
    result = await db.execute(query)
    return result.scalars().all()


@file_router.get("/images/{area_id}", response_model=list[GetFile])
async def list_images_by_area(area_id: int, db: AsyncSession = Depends(get_async_session)):
    query = select(Image).where(Image.area_id == area_id)
    result = await db.execute(query)
    return result.scalars().all()


@file_router.get("/videos", response_model=list[GetFile])
async def list_images(db: AsyncSession = Depends(get_async_session)):
    query = select(Video)
    result = await db.execute(query)
    return result.scalars().all()


@file_router.get("/videos/{area_id}", response_model=list[GetFile])
async def list_videods_by_area(area_id: int, db: AsyncSession = Depends(get_async_session)):
    query = select(Video).where(Video.area_id == area_id)
    result = await db.execute(query)
    return result.scalars().all()


@file_router.post("/images")
async def upload_image(area_id: int, file: UploadFile = File(...), db: AsyncSession = Depends(get_async_session)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        return {"error": "Only JPEG and PNG image files are allowed"}

    with open(f"catalogue/images/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    query = Insert(Image).values(title=file.filename, area_id=area_id)
    await db.execute(query)
    await db.commit()

    return JSONResponse(content="File was uploaded successfully!", status_code=200)


@file_router.post("/videos")
async def upload_video(area_id: int, file: UploadFile = File(...), db: AsyncSession = Depends(get_async_session)):
    if file.content_type not in ["video/mp4"]:
        return {"error": "Only MP4 files are allowed"}

    with open(f"catalogue/videos/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    query = Insert(Video).values(title=file.filename, area_id=area_id)
    await db.execute(query)
    await db.commit()
    return JSONResponse(content="File was uploaded successfully!", status_code=200)
