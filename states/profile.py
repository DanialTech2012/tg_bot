from aiogram.fsm.state import StatesGroup, State


class UserDeopsitState(StatesGroup):
    INPUT_AMOUNT = State()
    APPLY_DEOPSIT = State()
