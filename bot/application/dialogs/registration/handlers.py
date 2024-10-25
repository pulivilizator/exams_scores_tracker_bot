from typing import TYPE_CHECKING

from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject
from fluentogram import TranslatorRunner

from bot.core import dto
from bot.core.enums import RegistrationKeys
from bot.core.exceptions.dialog_errors import NameInputError
from bot.repository.implementations.user_cache_repository import UserCacheRepository
from bot.services.user_service import UserService

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner

def name_filter(text: str):
    if len(text.split(' ')) == 1 and len(text) > 1 and all(i.isalpha() or i == '-' for i in text):
        return text
    raise NameInputError()

async def save_first_name(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str
):
    dialog_manager.dialog_data.update({RegistrationKeys.FIRST_NAME: text})
    await dialog_manager.next()

async def incorrect_name_input(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str,
        err: NameInputError | None = None
):
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    await message.answer(i18n.name.err.message())

@inject
async def finish_registration(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str,
        user_service: FromDishka[UserService],
        cache: FromDishka[UserCacheRepository]
):
    first_name = dialog_manager.dialog_data.get(RegistrationKeys.FIRST_NAME)
    last_name = text

    register_user = dto.RegisterUser(
        first_name=first_name, last_name=last_name
    )
    await cache.hset(user_id=message.from_user.id, model_data=register_user)
    await user_service.update(lookup_value=message.from_user.id, update_data=register_user)
    await dialog_manager.done()