from typing import List
from pydantic import BaseModel
from administration.entities.schemas.record import GetRecord


class ClientCreateUpdate(BaseModel):
    first_name: str
    last_name: str
    gender: bool
    address: str
    phone: str
    image_path: str


class GetClient(BaseModel):
    first_name: str
    last_name: str
    gender: bool
    address: str
    phone: str
    records: List[GetRecord]
