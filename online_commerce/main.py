from pathlib import Path

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from online_commerce.config import DESCRIPTION
from online_commerce.routes import html_router

app = FastAPI(title="Beauty B", description=DESCRIPTION)

app.include_router(html_router)
static_path = Path(__file__).parent / "static"


# Добавление маршрута для статических файлов
app.mount("/static", StaticFiles(directory=static_path), name="static")