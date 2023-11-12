from pydantic import BaseModel

from administration.entities.schemas.area import GetAreaScheme


class ServiceCreateUpdate(BaseModel):
    title: str
    price: float
    area_id: int


class GetService(BaseModel):
    title: str
    price: float
    #area_id: int
    area: GetAreaScheme
