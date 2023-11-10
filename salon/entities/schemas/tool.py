from pydantic import BaseModel

from salon.entities.schemas.master import GetMaster


class ToolCreateUpdate(BaseModel):
    title: str
    master_id: int


class GetTool(BaseModel):
    title: str
    master: GetMaster
