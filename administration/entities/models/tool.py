from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from administration.database import Base


class Tool(Base):
    __tablename__ = "tools"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(64))

    master_id: Mapped[int] = mapped_column(ForeignKey("masters.id"))
    master = relationship("Master", back_populates="tools")
