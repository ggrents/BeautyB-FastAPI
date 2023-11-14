from bson import ObjectId
from pydantic import BaseModel
from datetime import datetime


class Comment(BaseModel):
    user_id: ObjectId
    review_id: ObjectId
    comment_text: str
    comment_time : datetime

