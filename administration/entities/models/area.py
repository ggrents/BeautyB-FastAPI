from typing import TYPE_CHECKING, List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from administration.database import Base
from administration.entities.models.service import Service
from administration.entities.models.master import Master


class Area(Base):
    __tablename__ = "areas"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(64), index=True)
    services = relationship(Service, back_populates="area")
    masters = relationship(Master, back_populates="area")
