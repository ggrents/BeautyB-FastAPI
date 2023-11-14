from typing import Annotated

from fastapi import APIRouter, Path, Body

from forum.data_access import users
from forum.entities.models.user import User

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.post("", response_model=User)
async def register(user: Annotated[User, Body()]):
    return await users.add_user(user)


@user_router.get("", response_model=list[User])
async def list_users():
    return await users.list_users()


@user_router.get("/{user_id}", response_model=User)
async def get_user_by_id(user_id: Annotated[str, Path()]):
    user = await users.get_user_by_id(user_id)
    return user


@user_router.put("/{user_id}", response_model=User)
async def update_user(user_id: Annotated[str, Path()], user: User):
    return await users.update_user(user_id, dict(user))


@user_router.delete("/{user_id}", response_model=User)
async def delete_user(user_id: Annotated[str, Path()]):
    return await users.delete_user(user_id)
