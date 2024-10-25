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

    fullname: dto.UserFullName = await user_cache.hget_all(user_id=user.id, response_model=dto.UserFullName)
    first_name = fullname.first_name or ''
    last_name = f' {fullname.last_name}' or ''

    return {
        'menu_message': i18n.menu_message(first_name=first_name, last_name=last_name),
        'enter_scores_button': i18n.scores.enter.button(),
        'list_scores_button': i18n.scores.list.button(),
        'change_lang_button': change_lang_button,
        'registration_button': registration_button
    }