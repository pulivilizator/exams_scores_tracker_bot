from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from bot.application.states import MainMenuSG, RegistrationSG, ScoreSG

router = Router()

@router.message(CommandStart())
async def start_process(message: Message,
                        dialog_manager: DialogManager,):
    await dialog_manager.start(state=MainMenuSG.menu, mode=StartMode.RESET_STACK)

@router.message(Command('register'))
async def register_process(message: Message,
                        dialog_manager: DialogManager,):
    await dialog_manager.start(state=RegistrationSG.first_name_input)

@router.message(Command('enter_scores'))
async def register_process(message: Message,
                           dialog_manager: DialogManager):
    await dialog_manager.start(state=ScoreSG.enter_name)

@router.message(Command('view_scores'))
async def register_process(message: Message,
                           dialog_manager: DialogManager):
    await dialog_manager.start(state=ScoreSG.show_scores)

