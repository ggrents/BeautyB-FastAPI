from pydantic import BaseModel


class ToolCreateUpdate(BaseModel):
    title: str
    master_id: int


class GetTool(BaseModel):
    title: str
    master_id: int
