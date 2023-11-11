from fastapi import FastAPI

from administration.endpoints.areas_router import areas_router

app = FastAPI()

app.include_router(areas_router)