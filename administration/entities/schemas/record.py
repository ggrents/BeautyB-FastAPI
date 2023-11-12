from datetime import datetime

from pydantic import BaseModel


class MasterGet(BaseModel):
    first_name: str
    last_name: str
    gender: bool
    address: str
    phone: str
    salary: float
    area_id: int


class ClientGet(BaseModel):
    first_name: str
    last_name: str
    gender: bool
    address: str
    phone: str


class ServiceGet(BaseModel):
    title: str
    price: float
    area_id: int


class SpotGet(BaseModel):
    timestamp: datetime
    master_id: int
    service_id : int


class RecordCreateUpdate(BaseModel):
    client_id: int
    spot_id: int


class GetRecord(BaseModel):
    client: ClientGet
    spot: SpotGet
