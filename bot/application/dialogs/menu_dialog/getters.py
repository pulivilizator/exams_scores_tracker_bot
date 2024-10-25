from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from dishka.integrations.aiogram import FromDishka
from dishka.integrations.aiogram_dialog import inject
from fluentogram import TranslatorRunner

from bot.core import dto
from bot.core.enums import LanguageList, RegistrationKeys
from bot.repository.implementations.user_cache_repository import UserCacheRepository

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner

@inject
async def main_menu_getter(dialog_manager: DialogManager,
                           i18n: TranslatorRunner,
                           user_cache: FromDishka[UserCacheRepository],
                           **kwargs):
    user = dialog_manager.event.from_user
    name_is_setted = await user_cache.hget(user_id=user.id, key=RegistrationKeys.NAME_IS_SETTED)
    current_lang: dto.UserLanguage = await user_cache.hget_all(user_id=user.id, response_model=dto.UserLanguage)
    change_lang_button = i18n.lang.russian()
    if current_lang.language == LanguageList.RU:
        change_lang_button = i18n.lang.english()

    registration_button = i18n.registration.button()
    if name_is_setted:
        registration_button = i18n.update_data.button()

    return {
        'menu_message': i18n.menu_message(),
        'change_lang_button': change_lang_button,
        'registration_button': registration_button
    }