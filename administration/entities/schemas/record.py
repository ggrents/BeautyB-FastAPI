from pydantic import BaseModel


class RecordCreateUpdate(BaseModel):
    client_id: int
    spot_id: int


class GetRecord(BaseModel):
    client_id: int
    spot_id: int