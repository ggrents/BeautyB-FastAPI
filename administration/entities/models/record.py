from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from administration.database import Base
from administration.entities.models.client import Client
from administration.entities.models.feedback import Feedback
#from administration.entities.models.spot import Spot


class Record(Base):
    __tablename__ = "records"
    id: Mapped[int] = mapped_column(primary_key=True)

    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    spot_id: Mapped[int] = mapped_column(ForeignKey("spots.id"))

    client= relationship(Client, back_populates="records")
    #spot = relationship("Spot", back_populates="record")
    feedback = relationship(Feedback, back_populates="record")
