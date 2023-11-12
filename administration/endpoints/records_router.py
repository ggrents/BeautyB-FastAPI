from http.client import OK
from typing import Annotated

from fastapi import APIRouter, Depends, Path, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession

from administration.data_access import services, spots, records
from administration.database import get_async_session
from administration.entities.schemas.record import GetRecord, RecordCreateUpdate


record_router = APIRouter(prefix="/records", tags=["Records"])


@record_router.get("", response_model=list[GetRecord])
async def list_records(db: AsyncSession = Depends(get_async_session)):
    return await records.get_records(db)


@record_router.get("/{record_id}", response_model=GetRecord)
async def get_record_by_id(record_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    rec = await records.get_record_by_id(db, record_id)
    if not rec:
        raise HTTPException(status_code=404, detail="Record not found")
    return rec


@record_router.get("/client/{client_id}", response_model=list[GetRecord])
async def get_record_by_client(client_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    rec = await records.get_records_by_client(db, client_id)
    if not rec:
        raise HTTPException(status_code=404, detail="Records not found")
    return rec


@record_router.post("", response_model=GetRecord)
async def add_record(record: Annotated[RecordCreateUpdate, Body()],
                     db: AsyncSession = Depends(get_async_session)):
    await records.add_record(db, record)
    return record


@record_router.patch("/{record_id}")
async def update_record(record_id: Annotated[int, Path()], record: Annotated[RecordCreateUpdate, Body()],
                        db: AsyncSession = Depends(get_async_session)):
    await records.update_record(record_id, db, record)
    return record


@record_router.delete("/{record_id}")
async def delete_record(record_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    record = await records.get_record_by_id(db, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Service not found")
    await spots.delete_spot(db, record)
    return OK
