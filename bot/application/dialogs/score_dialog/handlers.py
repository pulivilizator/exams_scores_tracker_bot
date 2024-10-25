from typing import TYPE_CHECKING

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject
from fluentogram import TranslatorRunner

from bot.application.states import ScoreSG
from bot.core import dto
from bot.core.enums import ScoreKeys
from bot.core.exceptions.dialog_errors import ScoreQuantityInputError
from bot.services.score_service import ScoreService

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner

async def save_score_name(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str
):
    dialog_manager.dialog_data.update({ScoreKeys.NAME: text})
    await dialog_manager.next()

@inject
async def save_exam_score(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str,
        score_service: FromDishka[ScoreService]
):
    i18n = dialog_manager.middleware_data.get('i18n')
    name = dialog_manager.dialog_data.get(ScoreKeys.NAME)
    quantity = int(text)

    exam_score = dto.CreateScore(exam_name=name, quantity=quantity, user_id=message.from_user.id)
    await score_service.create(exam_score)
    await message.answer(text=i18n.score.done())
    await dialog_manager.switch_to(state=ScoreSG.enter_name)


async def incorrect_score_input(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        err: ScoreQuantityInputError | None = None
):
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    msg = i18n.score.quantity.err_message()
    if err:
        await message.answer(i18n.score.quantity.err_message())
        return
    await message.answer(i18n.common.text_error())

def score_quantity(text: str):
    try:
        quantity = int(text)
        if 0 <= quantity <= 100:
            return text
        raise ValueError()
    except ValueError:
        raise ScoreQuantityInputError

@inject
async def delete_score(
        callback: CallbackQuery,
        widget: Button,
        dialog_manager: DialogManager,
        widget_id: str,
        score_service: FromDishka[ScoreService]
):
    await score_service.delete(widget_id)