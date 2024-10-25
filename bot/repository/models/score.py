from uuid import UUID

from sqlalchemy import Uuid, text, SmallInteger, String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import TimestampMixin

class Score(TimestampMixin, Base):
    __tablename__ = 'scores'

    score_id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, server_default=text('gen_random_uuid()'))
    number_scores: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    exam_name: Mapped[str] = mapped_column(String, nullable=False)

    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('users.user_id', ondelete='CASCADE'))
    user: Mapped['User'] = relationship(back_populates='scores')