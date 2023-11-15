from motor.motor_asyncio import AsyncIOMotorClient
from forum.settings import MongoURL

client = AsyncIOMotorClient(MongoURL)
db = client["forum"]
