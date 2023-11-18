import uuid
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    pass

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    pass
