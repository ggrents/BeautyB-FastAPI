from pydantic import BaseModel


class ServiceCreateUpdate(BaseModel):
    title: str
    price: float
    area_id: int


class AreaGet(BaseModel):
    id: int
    title: str


class GetService(BaseModel):
    title: str
    price: float
    area_id:int

