from datetime import datetime

from sqlalchemy import BigInteger, String, Boolean, DateTime, func, Enum as SQLAlchemyEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.core.enums import LanguageList
from .base import Base
from .mixins import TimestampMixin


class User(TimestampMixin, Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=True)
    last_name: Mapped[str] = mapped_column(String, nullable=True)
    name_is_setted: Mapped[bool] = mapped_column(Boolean, default=False)
    language: Mapped[str] = mapped_column(SQLAlchemyEnum(LanguageList), nullable=False, default=LanguageList.RU)

    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    scores: Mapped[list['Score']] = relationship(back_populates='user')