from typing import TYPE_CHECKING, List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from salon.database import Base

if TYPE_CHECKING:
    from salon.entities.models.area import Area


class Service(Base):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(64), index=True)
    price: Mapped[float] = mapped_column()
    area_id: Mapped[int] = mapped_column(ForeignKey("areas.id"))

    area: Mapped["Area"] = relationship(back_populates="services")
    records: Mapped[List["Record"]] = relationship(back_populates="service")