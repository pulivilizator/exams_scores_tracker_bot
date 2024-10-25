from aiogram import Router

from .dialogs import menu_dialog, registration_dialog
from .handlers.commands_handler import router as commands_router


def get_routers() -> list[Router]:
    return [
        commands_router,
        menu_dialog,
        registration_dialog,
    ]