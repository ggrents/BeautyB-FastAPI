import decimal
from pydantic import BaseModel


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
    id: int
    first_name: str
    last_name: str
    gender: bool
    image_path: str
    address: str
    phone: str
    salary: float
    area_id: int
