from http.client import OK
from typing import Annotated

from fastapi import APIRouter, Depends, Path, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession

from administration.data_access import services, spots, records, feedbacks
from administration.database import get_async_session
from administration.entities.schemas.feedback import GetFeedback, FeedbackCreateUpdate

feedback_router = APIRouter(prefix="/feedbacks", tags=["Feedbacks"])


@feedback_router.get("", response_model=list[GetFeedback])
async def list_feedbacks(db: AsyncSession = Depends(get_async_session)):
    return await feedbacks.get_feedbacks(db)


@feedback_router.get("/{feedback_id}", response_model=GetFeedback)
async def get_feedback_by_id(feedback_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    rec = await feedbacks.get_feedback_by_id(db, feedback_id)
    if not rec:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return rec


@feedback_router.get("/client/{client_id}", response_model=list[GetFeedback])
async def get_feedbacks_by_client(client_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    rec = await feedbacks.get_feedbacks_by_client(db, client_id)
    if not rec:
        raise HTTPException(status_code=404, detail="Feedbacks not found")
    return rec


@feedback_router.get("/client/{client_id}", response_model=list[GetFeedback])
async def get_feedbacks_by_client(client_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    rec = await feedbacks.get_feedbacks_by_client(db, client_id)
    if not rec:
        raise HTTPException(status_code=404, detail="Feedbacks not found")
    return rec


@feedback_router.get("/master/{master_id}", response_model=list[GetFeedback])
async def get_feedbacks_by_master(master_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    rec = await feedbacks.get_feedbacks_by_master(db, master_id)
    if not rec:
        raise HTTPException(status_code=404, detail="Feedbacks not found")
    return rec


@feedback_router.post("")
async def add_record(feedback: Annotated[FeedbackCreateUpdate, Body()],
                     db: AsyncSession = Depends(get_async_session)):
    await feedbacks.add_feedback(db, feedback)
    return feedback


@feedback_router.delete("/{feedback_id}")
async def delete_record(feedback_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    feedback = await feedbacks.get_feedback_by_id(db, feedback_id)
    if not feedback:
        raise HTTPException(status_code=404, detail="feedback not found")
    await spots.delete_spot(db, feedback)
    return OK
