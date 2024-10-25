from aiogram.fsm.state import StatesGroup, State

class MainMenuSG(StatesGroup):
    menu = State()

class RegistrationSG(StatesGroup):
    first_name_input = State()
    last_name_input = State()

class ScoreSG(StatesGroup):
    enter_name = State()
    enter_scores = State()
    show_scores = State()