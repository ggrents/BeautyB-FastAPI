from typing import List, Optional
from sqlalchemy import ForeignKey, String, Boolean
from sqlalchemy.orm import mapped_column, Mapped, relationship

from administration.database import Base


class Client(Base):
    __tablename__ = "clients"
    id: Mapped[int] = mapped_column(primary_key=True)

    first_name: Mapped[str] = mapped_column(String(64), index=True)
    last_name: Mapped[str] = mapped_column(String(64), index=True)
    gender: Mapped[bool] = mapped_column(Boolean, nullable=False)
    address: Mapped[str] = mapped_column(String(64), index=True)
    phone: Mapped[str] = mapped_column(String(64), index=True)
    image_path: Mapped[Optional[str]] = mapped_column(String(140))

    records: Mapped[List["Record"]] = relationship(back_populates="client")
