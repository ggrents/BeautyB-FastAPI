from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from administration.database import Base


class Record(Base):
    __tablename__ = "records"
    id: Mapped[int] = mapped_column(primary_key=True)

    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    spot_id: Mapped[int] = mapped_column(ForeignKey("spots.id"))

    client: Mapped["Client"] = relationship(back_populates="records")
    spot: Mapped["Spot"] = relationship(back_populates="record")
    feedback: Mapped["Feedback"] = relationship(back_populates="record")
