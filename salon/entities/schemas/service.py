from pydantic import BaseModel

from salon.entities.schemas.area import GetArea


class ServiceCreateUpdate(BaseModel):
    title: str
    price: float
    area_id: int


class GetService(BaseModel):
    title: str
    price: float
    area: GetArea
