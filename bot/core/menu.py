from aiogram import Bot
from aiogram.types import BotCommand


async def set_menu(bot: Bot):
    menu = [
        BotCommand(command='/start', description='Main menu'),
        BotCommand(command='/register', description='Sign up'),
        BotCommand(command='/enter_scores', description='Add a exam with score'),
        BotCommand(command='/view_scores', description='View a exams with scores'),
    ]

    await bot.set_my_commands(menu)
