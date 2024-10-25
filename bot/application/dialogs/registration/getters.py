from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from dishka.integrations.aiogram_dialog import inject
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


@inject
async def registration_getter(dialog_manager: DialogManager,
                              i18n: TranslatorRunner,
                              **kwargs):

    return {
        'first_name_input_message': i18n.first_name_input.message(),
        'last_name_input_message': i18n.last_name_input.message(),
    }