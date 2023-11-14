from bson import ObjectId
from pydantic import BaseModel
from datetime import datetime


class Review(BaseModel):
    user_id: ObjectId
    record_id: int
    review_text: str
    rating: int
    visit_date: datetime
    photo_url: str 
