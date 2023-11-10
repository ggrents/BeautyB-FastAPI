import decimal
from typing import List, Optional

from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from salon.database import Base


class Master(Base):
    __tablename__ = "masters"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(64), index=True)
    last_name: Mapped[str] = mapped_column(String(64), index=True)
    gender: Mapped[bool] = mapped_column(Boolean, nullable=False)
    address: Mapped[str] = mapped_column(String(64), index=True)
    phone: Mapped[str] = mapped_column(String(64), index=True)
    image_path: Mapped[Optional[str]] = mapped_column(String(140))
    salary: Mapped[decimal.Decimal] = mapped_column()
    area_id : Mapped[int] = mapped_column(ForeignKey("areas.id"))

    service: Mapped["Area"] = relationship(back_populates="masters")
    tools: Mapped[List["Tool"]] = relationship(back_populates="master")
    records: Mapped[List["Record"]] = relationship(back_populates="master")
