from sqlalchemy import select, Insert, Update
from sqlalchemy.ext.asyncio import AsyncSession

from administration.entities.models.client import Client
from administration.entities.models.record import Record
from administration.entities.models.feedback import Feedback
from administration.entities.schemas.feedback import FeedbackCreateUpdate
from administration.entities.schemas.record import RecordCreateUpdate


async def get_feedbacks(db: AsyncSession):
    query = select(Feedback)
    result = await db.execute(query)
    return result.scalars().all()


async def get_feedback_by_id(db: AsyncSession, feedback_id: int):
    result = await db.get(Feedback, feedback_id)
    return result


async def get_feedback_by_record(db: AsyncSession, record_id: int):
    query = select(Feedback).where(record_id=record_id)
    result = await db.execute(query)
    return result.scalars().all()


async def get_feedbacks_by_client(db: AsyncSession, client_id: int):
    query = (select(Feedback).join(Record, Feedback.record_id == Record.id).join
             (Client, Record.client_id == Client.id).where(Client.id == client_id))
    result = await db.execute(query)
    return result.scalars().all()


async def delete_feedback(db: AsyncSession, feedback: Feedback):
    await db.delete(feedback)
    await db.commit()


async def add_feedback(db: AsyncSession, feedback: Feedback):
    query = Insert(Feedback).values(**feedback)
    await db.execute(query)


async def update_feedback(db: AsyncSession, feedback: Feedback):
    query = Update(Feedback).values(**feedback)
    await db.execute(query)
