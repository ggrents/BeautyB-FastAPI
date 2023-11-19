from pydantic import BaseModel, Field


class FeedbackCreateUpdate(BaseModel):
    estimation: int = Field(gt=0, lt=6)
    record_id: int


class GetFeedback(BaseModel):
    estimation: int = Field(gt=0, lt=6)
    record_id: int
