from typing import TYPE_CHECKING, List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from administration.database import Base
from administration.entities.models.spot import Spot

#from administration.entities.models.area import Area


class Service(Base):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(64), index=True)
    price: Mapped[float] = mapped_column()
    area_id: Mapped[int] = mapped_column(ForeignKey("areas.id"))

    area= relationship("Area", back_populates="services")
    spots = relationship(Spot, back_populates="service")