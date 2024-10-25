from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Start
from aiogram_dialog.widgets.text import Format

from bot.application.states import MainMenuSG, RegistrationSG
from bot.core.enums import Language
from .getters import main_menu_getter
from ...getters.common_getter import common_getter

dialog = Dialog(
    Window(
        Format('{menu_message}'),
        Start(text=Format('{registration_button}'), state=RegistrationSG.first_name_input, id='start_register'),
        Button(text=Format('{change_lang_button}'), id=Language.WIDGET_KEY),
        getter=main_menu_getter,
        state=MainMenuSG.menu
    ),
    getter=common_getter
)