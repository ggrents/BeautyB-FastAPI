from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from forum.database import db
from forum.endpoints.user_router import user_router
from forum.entities.models.user import User
from forum.settings import MongoURL

app = FastAPI(title="Microservice")


app.include_router(user_router)