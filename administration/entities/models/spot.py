from datetime import datetime
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from administration.database import Base


class Spot(Base):
    __tablename__ = "spots"
    id: Mapped[int] = mapped_column(primary_key=True)
    timestamp: Mapped[datetime] = mapped_column()
    master_id: Mapped[int] = mapped_column(ForeignKey("masters.id"))
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"))

    master: Mapped["Master"] = relationship(back_populates="spots")
    service: Mapped["Service"] = relationship(back_populates="spots")
    records: Mapped[List["Record"]] = relationship(back_populates="spot")