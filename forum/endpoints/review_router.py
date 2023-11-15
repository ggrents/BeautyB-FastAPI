from typing import Annotated
import httpx
from fastapi import APIRouter, Path, Body
from forum.data_access import users, reviews
from forum.entities.models.review import Review


review_router = APIRouter(prefix="/reviews", tags=["Reviews"])


@review_router.post("", response_model=Review)
async def add_review(review: Annotated[Review, Body()]):
    _review = await reviews.add_review(review)
    url = "http://127.0.0.1:8000/feedbacks"
    payload = {
        "estimation": _review.rating,
        "record_id": _review.record_id
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)

    return _review


@review_router.get("", response_model=list[Review])
async def list_reviews():
    return await reviews.list_reviews()


@review_router.get("/{review_id}", response_model=Review)
async def get_review_by_id(review_id: Annotated[str, Path()]):
    _review = await reviews.get_review_by_id(review_id)
    return _review


@review_router.put("/{review_id}", response_model=Review)
async def update_review(review_id: Annotated[str, Path()], review: Review):
    return await reviews.update_review(review_id, dict(review))


@review_router.delete("/{review_id}", response_model=Review)
async def delete_review(review_id: Annotated[str, Path()]):
    return await reviews.delete_review(review_id)
