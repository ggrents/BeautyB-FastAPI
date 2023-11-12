from datetime import datetime

from pydantic import BaseModel

from administration.entities.schemas.master import GetMaster
from administration.entities.schemas.service import GetService


class SpotCreateUpdate(BaseModel):
    timestamp: datetime
    master_id: int
    service_id: int


class GetSpot(BaseModel):
    timestamp: datetime
    master_id: int
    service_id: int
