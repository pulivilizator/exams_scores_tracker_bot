from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.kbd import Cancel, Back, ScrollingGroup, Select
from aiogram_dialog.widgets.text import Format

from .getters import enter_score_getter, show_score_getter
from bot.application.getters.common_getter import common_getter
from bot.application.states import ScoreSG
from .handlers import save_score_name, incorrect_score_input, score_quantity, save_exam_score, delete_score

dialog = Dialog(
    Window(
        Format('{enter_score_name}'),
        TextInput(
            id='enter_score_name',
            on_success=save_score_name,
        ),
        MessageInput(
            content_types=ContentType.ANY,
            func=incorrect_score_input
        ),
        Cancel(Format('{previous_button}')),
        state=ScoreSG.enter_name,
        getter=enter_score_getter
    ),
    Window(
        Format('{enter_score_scores}'),
        TextInput(
            id='enter_score_scores',
            type_factory=score_quantity,
            on_success=save_exam_score,
            on_error=incorrect_score_input
        ),
        MessageInput(
            content_types=ContentType.ANY,
            func=incorrect_score_input
        ),
        Back(Format('{previous_button}')),
        state=ScoreSG.enter_scores,
        getter=enter_score_getter
    ),

    Window(
        Format('{show_score}'),
        ScrollingGroup(
            Select(text=Format('{item[1]}'),
                   id='item',
                   item_id_getter=lambda x: x[0],
                   items='exams',
                   on_click=delete_score),
            id='exams',
            width=1,
            height=5,
            hide_on_single_page=True,

        ),
        Cancel(Format('{previous_button}')),
        state=ScoreSG.show_scores,
        getter=show_score_getter
    ),
    getter=common_getter
)