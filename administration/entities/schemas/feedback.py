from pydantic import BaseModel, Field

from administration.entities.schemas.record import GetRecord


class FeedbackCreateUpdate(BaseModel):
    estimation: int = Field(gt=0, lt=6)
    comment: str
    record_id: int


class GetFeedback(BaseModel):
    estimation: int = Field(gt=0, lt=6)
    comment: str
    record_id: int
