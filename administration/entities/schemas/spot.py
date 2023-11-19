from datetime import datetime

from pydantic import BaseModel


class SpotCreateUpdate(BaseModel):
    timestamp: datetime
    master_id: int
    service_id: int


class GetSpot(BaseModel):
    timestamp: datetime
    master_id: int
    service_id: int
