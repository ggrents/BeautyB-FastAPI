from typing import Annotated

import httpx
from fastapi import APIRouter, HTTPException, Path, Form
from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse
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

    return templates.TemplateResponse("catalogue.html", {"request": request, "cats": cats})


@html_router.get("/masters", response_class=HTMLResponse)
async def masters(request: Request):
    url = "http://127.0.0.1:8000/masters"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    masters_data = response.json()

    return templates.TemplateResponse("masters.html", {"request": request, "masters": masters_data})


@html_router.get("/areas", response_class=HTMLResponse)
async def areas(request: Request):
    url = "http://127.0.0.1:8000/areas"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    areas_data = response.json()

    return templates.TemplateResponse("areas.html", {"request": request, "areas": areas_data})


@html_router.get("/services/{id}", response_class=HTMLResponse)
async def services(request: Request, id: Annotated[int, Path()]):
    url = f"http://127.0.0.1:8000/services/area/{id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    services_data = response.json()

    return templates.TemplateResponse("services.html", {"request": request, "services": services_data})


@html_router.post("/register")
async def register(request: Request, email: str = Form(...), password: str = Form(...)):
    print(email, password)
    return RedirectResponse(url="/login", status_code=303)

@html_router.post("/login")
async def login(request: Request, email: str = Form(...), password: str = Form(...)):
    return RedirectResponse(url="/", status_code=303)