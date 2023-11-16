from fastapi import FastAPI

from catalogue.endpoints.file_router import file_router

app = FastAPI(title="Catalogue")
app.include_router(file_router)