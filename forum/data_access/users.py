from bson import ObjectId
from fastapi import HTTPException

from forum.database import db
from forum.entities.models.user import User

collection = db["users"]


async def add_user(user: User):
    await db["users"].insert_one(dict(user))
    return user


async def list_users():
    users_cursor = db["users"].find()
    users = await users_cursor.to_list(length=1000)
    return users


async def get_user_by_id(user_id: str):
    user = await db["users"].find_one({"_id": ObjectId(user_id)})
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


async def update_user(user_id: str, updated_fields: dict):
    fields_to_update = {k: v for k, v in updated_fields.items() if v is not None}

    await db["users"].update_one({"_id": ObjectId(user_id)}, {"$set": fields_to_update})

    updated_user = await db["users"].find_one({"_id": ObjectId(user_id)})

    if updated_user:
        return updated_user

    raise HTTPException(status_code=404, detail="User not found")


async def delete_user(user_id: str):
    user = await db["users"].find_one({"_id": ObjectId(user_id)})
    if user:
        await db["users"].delete_one({"_id": ObjectId(user_id)})
        return user
    raise HTTPException(status_code=404, detail="User not found")
