from pathlib import Path

from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from online_commerce.auth.auth import auth_backend
from online_commerce.auth.database import User
from online_commerce.auth.manager import get_user_manager
from online_commerce.auth.schemas import UserRead, UserCreate
from online_commerce.config import DESCRIPTION

from online_commerce.routes import html_router, templates

app = FastAPI(title="Beauty B", description=DESCRIPTION)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user(optional=True)

app.include_router(html_router)
static_path = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=static_path), name="static")


@app.get("/", response_class=HTMLResponse)
async def main(request: Request, user: User = Depends(current_user)):
    return templates.TemplateResponse("index.html", {"request": request, "current_user": user})