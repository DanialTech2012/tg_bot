from aiogram import Router, types
from aiogram.filters import Command
from sqlalchemy import text

from keyboards.menu import main_menu_kb
from repositories.user import UserRepo

router = Router()

@router.message(Command("start"))
async def start_bot(message: types.Message, user_repo:  UserRepo):
    await user_repo.
    await message.answer(
        f"Hi, {message.from_user.full_name}!n\I am bookstore, select the desired menu below:",
        reply_markup=main_menu_kb()
    )