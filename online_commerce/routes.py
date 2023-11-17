import httpx
from fastapi import APIRouter, HTTPException
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="online_commerce/templates")

html_router = APIRouter()


@html_router.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@html_router.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@html_router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@html_router.get("/catalogue", response_class=HTMLResponse)
async def catalogue(request: Request):
    url = "http://127.0.0.1:8003/upload/images"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    cats = response.json()

    return templates.TemplateResponse("catalogue.html", {"request": request, "cats" : cats})


@html_router.get("/masters", response_class=HTMLResponse)
async def masters(request: Request):
    url = "http://127.0.0.1:8000/masters"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    masters_data = response.json()  # Предполагается, что данные в формате JSON

    return templates.TemplateResponse("masters.html", {"request": request, "masters": masters_data})