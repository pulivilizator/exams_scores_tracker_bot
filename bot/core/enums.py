from enum import StrEnum


class BaseKeys(StrEnum):
    WIDGET_KEY: str
    REDIS_KEY: str

class UserKeys(StrEnum):
    USER_KEY = 'user:{}'

class LanguageList(StrEnum):
    RU = 'ru'
    EN = 'en'

class Language(BaseKeys):
    DEFAULT = LanguageList.RU

    WIDGET_KEY = 'language'
    REDIS_KEY = 'language'

class RegistrationKeys(StrEnum):
    FIRST_NAME = 'first_name'
    LAST_NAME = 'last_name'

    NAME_IS_SETTED = 'name_is_setted'

class ScoreKeys(StrEnum):
    NAME = 'exam_name'
    QUANTITY = 'scores_quantity'

