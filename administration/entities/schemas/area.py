from typing import List

from pydantic import BaseModel


class GetAreaScheme(BaseModel):
    id: int
    title: str

class AreaGet(BaseModel):
    id:int
    title:str