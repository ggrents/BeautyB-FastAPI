from typing import Annotated
from fastapi import APIRouter, Path, Body

from forum.data_access import users, reviews, comments
from forum.entities.models.comment import Comment


comment_router = APIRouter(prefix="/comments", tags=["Comments"])


@comment_router.post("", response_model=Comment)
async def add_comment(comment: Annotated[Comment, Body()]):
    _comm = await comments.add_comment(comment)
    return _comm


@comment_router.get("", response_model=list[Comment])
async def list_comments():
    return await comments.list_comments()


@comment_router.get("/{comment_id}", response_model=Comment)
async def get_comment_by_id(comment_id: Annotated[str, Path()]):
    _comm = await comments.get_comment_by_id(comment_id)
    return _comm


@comment_router.delete("/{comment_id}", response_model=Comment)
async def delete_comment(comment_id: Annotated[str, Path()]):
    return await comments.delete_comment(comment_id)
