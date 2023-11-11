from typing import List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from administration.database import Base
from administration.entities.models.master import Master


class Tool(Base):
    __tablename__ = "tools"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(64))

    master_id: Mapped[int] = mapped_column(ForeignKey("tools.id"))
    master = relationship(Master, back_populates="tools")
