from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.kbd import Cancel, Back
from aiogram_dialog.widgets.text import Format

from bot.application.states import RegistrationSG
from .getters import registration_getter
from .handlers import name_filter, save_first_name, incorrect_name_input, finish_registration
from ...getters.common_getter import common_getter

dialog = Dialog(
    Window(
        Format('{first_name_input_message}'),
        TextInput(
            id='first_name_input',
            type_factory=name_filter,
            on_success=save_first_name,
            on_error=incorrect_name_input
        ),
        MessageInput(
            content_types=ContentType.ANY,
            func=incorrect_name_input
        ),
        Cancel(text=Format('{previous_button}')),
        state=RegistrationSG.first_name_input,
        getter=registration_getter,
    ),
    Window(
        Format('{last_name_input_message}'),
        TextInput(
            id='last_name_input',
            type_factory=name_filter,
            on_success=finish_registration,
            on_error=incorrect_name_input
        ),
        MessageInput(
            content_types=ContentType.ANY,
            func=incorrect_name_input
        ),
        Back(Format('{previous_button}')),
        state=RegistrationSG.last_name_input,
        getter = registration_getter,
    ),
    getter=common_getter
)