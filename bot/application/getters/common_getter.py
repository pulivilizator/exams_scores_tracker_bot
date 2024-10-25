from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from dishka.integrations.aiogram_dialog import inject
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


@inject
async def common_getter(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        **kwargs
):
    return {
        'previous_button': i18n.previous_button(),
        'next_button': i18n.next_button(),
        'skip_button': i18n.skip_button(),
    }