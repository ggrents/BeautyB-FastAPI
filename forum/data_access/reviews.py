from bson import ObjectId
from fastapi import HTTPException

from forum.database import db
from forum.entities.models.review import Review


collection = db["reviews"]


async def add_review(review: Review):
    await collection.insert_one(dict(review))
    return review


async def list_reviews():
    reviews_cursor = collection.find()
    reviews = await reviews_cursor.to_list(length=1000)
    return reviews


async def get_review_by_id(review_id: str):
    _review = await collection.find_one({"_id": ObjectId(review_id)})
    if _review:
        return _review
    raise HTTPException(status_code=404, detail="Review not found")


async def update_review(review_id: str, updated_fields: dict):
    fields_to_update = {k: v for k, v in updated_fields.items() if v is not None}

    await collection.update_one({"_id": ObjectId(review_id)}, {"$set": fields_to_update})

    updated_review = await collection.find_one({"_id": ObjectId(review_id)})

    if updated_review:
        return updated_review

    raise HTTPException(status_code=404, detail="Review not found")


async def delete_review(review_id: str):
    _review = await collection.find_one({"_id": ObjectId(review_id)})
    if _review:
        await collection.delete_one({"_id": ObjectId(review_id)})
        return _review
    raise HTTPException(status_code=404, detail="Review not found")
