from typing import TYPE_CHECKING, List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from salon.database import Base


if TYPE_CHECKING:
    from salon.entities.models.service import Service


class Area(Base):
    __tablename__ = "areas"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(64), index=True)
    services: Mapped[List["Service"]] = relationship(back_populates="area")