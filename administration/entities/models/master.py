import decimal
from typing import List, Optional

from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from administration.database import Base


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

    area =  relationship("Area", back_populates="masters")
    tools = relationship("Tool", back_populates="master")
    spots = relationship("Spot", back_populates="master")
