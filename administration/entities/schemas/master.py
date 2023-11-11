import decimal
from typing import List

from pydantic import BaseModel

from administration.entities.schemas.area import GetArea
from administration.entities.schemas.service import GetService
from administration.entities.schemas.tool import GetTool


class MasterCreateUpdate(BaseModel):
    first_name: str
    last_name: str
    gender: bool
    address: str
    phone: str
    image_path: str
    salary: decimal.Decimal
    area_id: int


class GetMaster(BaseModel):
    first_name: str
    last_name: str
    gender: bool
    address: str
    phone: str
    salary: decimal.Decimal
    area: GetArea
    services: List[GetService]
    tools: List[GetTool]
