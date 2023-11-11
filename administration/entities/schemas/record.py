from pydantic import BaseModel

from administration.entities.schemas.client import GetClient
from administration.entities.schemas.spot import GetSpot


class RecordCreateUpdate(BaseModel):
    client_id: int
    spot_id: int


class GetRecord(BaseModel):
    client: GetClient
    spot: GetSpot
