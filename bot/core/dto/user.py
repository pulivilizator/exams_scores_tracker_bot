from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from bot.core.enums import LanguageList


class IsAdmin(BaseModel):
    is_admin: Optional[bool] = Field(default=False)

class UserFullName(BaseModel):
    first_name: str | None = None
    last_name: str | None = None

class UserBase(IsAdmin, UserFullName):
    user_id: int
    name_is_setted: bool = False
    is_active: Optional[bool] = Field(default=True)

class UserLanguage(BaseModel):
    language: LanguageList = Field(default=LanguageList.RU)

class User(UserBase, UserLanguage):
    created_at: datetime
    updated_at: datetime

class RegisterUser(BaseModel):
    first_name: str
    last_name: str
    name_is_setted: bool = True