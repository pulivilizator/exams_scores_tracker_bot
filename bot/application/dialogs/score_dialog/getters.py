from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject
from fluentogram import TranslatorRunner

from bot.core import dto
from bot.services.score_service import ScoreService

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner


@inject
async def enter_score_getter(dialog_manager: DialogManager,
                              i18n: TranslatorRunner,
                              **kwargs):
    return {
        'enter_score_name': i18n.score.enter.name(),
        'enter_score_scores': i18n.score.enter.scores(),
    }
@inject
async def show_score_getter(dialog_manager: DialogManager,
                            i18n: TranslatorRunner,
                            score_service: FromDishka[ScoreService],
                            **kwargs):
    exams: list[dto.Score] = await score_service.list(user_id=dialog_manager.event.from_user.id)

    return {
        'show_score': i18n.score.show.message(),
        'exams': ((exam.score_id, f'❌ {exam.exam_name} - {exam.quantity}') for exam in exams)
    }
