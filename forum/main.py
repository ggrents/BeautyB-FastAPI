from fastapi import FastAPI

from forum.endpoints.comment_router import comment_router
from forum.endpoints.review_router import review_router
from forum.endpoints.user_router import user_router

app = FastAPI(title="Forum")


app.include_router(user_router)
app.include_router(review_router)
app.include_router(comment_router)

