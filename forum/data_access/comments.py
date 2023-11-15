from bson import ObjectId
from fastapi import HTTPException

from forum.database import db
from forum.entities.models.comment import Comment


collection = db["comments"]
collection_users = db["reviews"]


async def add_comment(comm: Comment):
    await collection.insert_one(dict(comm))
    review = await collection_users.find_one({"_id": ObjectId(comm.review_id)})
    review["comments"].append(dict(comm))

    await db["reviews"].update_one({"_id": ObjectId(comm.review_id)}, {"$set": review})
    return comm


async def list_comments():
    comm_cursor = collection.find()
    comments = await comm_cursor.to_list(length=1000)
    return comments


async def get_comment_by_id(comment_id: str):
    _comm = await collection.find_one({"_id": ObjectId(comment_id)})
    if _comm:
        return _comm
    raise HTTPException(status_code=404, detail="Comment not found")


async def delete_comment(comment_id: str):
    _comm = await collection.find_one({"_id": ObjectId(comment_id)})
    if _comm:
        await collection.delete_one({"_id": ObjectId(comment_id)})
        return _comm
    raise HTTPException(status_code=404, detail="Comment not found")
