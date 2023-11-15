from typing import List

from pydantic import BaseModel, Field
from datetime import datetime

from forum.entities.models.comment import Comment


class Review(BaseModel):
    user_id: str
    record_id: int
    review_text: str
    rating: int
    visit_date: datetime
    photo_url: str
    comments: List[Comment] = Field(default_factory=list)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "user_id": "65537fad0167a775b19980f6",
                    "record_id": 15,
                    "review_text": "some text about your expirience",
                    "rating": 5,
                    "visit_date" : "2023-11-15T13:56:27.885+00:00",
                    "photo_url" : "some_photo_url.com"

                }
            ]
        }
    }



