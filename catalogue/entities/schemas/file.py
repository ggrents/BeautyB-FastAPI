from pydantic import BaseModel


class GetFile(BaseModel):
    id: int
    title: str
    area_id: int


class AddFile(BaseModel):
    title: str
    area_id: int
