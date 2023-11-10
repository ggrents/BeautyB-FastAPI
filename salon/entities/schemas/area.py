from typing import List

from pydantic import BaseModel

from salon.entities.schemas.master import GetMaster
from salon.entities.schemas.service import GetService


class GetArea(BaseModel):
    id: int
    title: str
    masters: List[GetMaster]
    services: List[GetService]

