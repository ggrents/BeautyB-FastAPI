from pydantic import BaseModel, Field
from datetime import datetime


class Comment(BaseModel):
    user_id: str
    review_id: str
    comment_text: str
    comment_time :  datetime = Field(default_factory=datetime.now, exclude=True)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "user_id": "string",
                    "review_id": "string",
                    "comment_text": "string"

                }
            ]
        }
    }




