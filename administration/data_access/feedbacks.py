from sqlalchemy import select, Insert, Update
from sqlalchemy.ext.asyncio import AsyncSession
from administration.entities.models.master import Master
from administration.entities.models.record import Record
from administration.entities.models.feedback import Feedback
from administration.entities.models.spot import Spot
from administration.entities.schemas.feedback import FeedbackCreateUpdate


async def get_feedbacks(db: AsyncSession):
    query = select(Feedback)
    result = await db.execute(query)
    return result.scalars().all()


async def get_feedback_by_id(db: AsyncSession, feedback_id: int):
    result = await db.get(Feedback, feedback_id)
    return result


async def get_feedbacks_by_master(db: AsyncSession, master_id: int):
    query = select(Feedback).join(Record).join(Spot).join(Master).filter(Master.id == master_id)
    result = await db.execute(query)
    feedbacks = result.scalars().all()
    return feedbacks


async def get_feedbacks_by_client(db: AsyncSession, client_id: int):
    query = select(Feedback).join(Record).filter(Record.client_id == client_id)
    result = await db.execute(query)
    feedbacks = result.scalars().all()
    return feedbacks


async def delete_feedback(db: AsyncSession, feedback: Feedback):
    await db.delete(feedback)
    await db.commit()


async def add_feedback(db: AsyncSession, feedback: FeedbackCreateUpdate):
    query = Insert(Feedback).values(estimation = feedback.estimation, record_id = feedback.record_id, comment = feedback.comment)
    await db.execute(query)
    await db.commit()

# async def update_feedback(db: AsyncSession, feedback: Feedback):
#     query = Update(Feedback).values(**feedback)
#     await db.execute(query)
