from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from administration.database import Base


class Feedback(Base):
    __tablename__ = "feedbacks"
    id: Mapped[int] = mapped_column(primary_key=True)
    estimation: Mapped[int] = mapped_column()
    comment: Mapped[str] = mapped_column(String(300))
    record_id: Mapped[int] = mapped_column(ForeignKey("records.id"))

    record = relationship("Record", back_populates="feedback")
