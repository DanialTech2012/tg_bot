from aiogram import F, Router, types
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from keyboards import profile as profile_kb
from repositories.user import UserRepo
from states.profile import UserDeopsitState

router = Router()

@round.message(F.text == "profile")
async def user_profile_info(
    message: types.Message, 
    user_repo: UserRepo,
    state: FSMContext
):
    user = await user_repo.get_user_by_tg_id(message.from_user.id)

    await message.answer(
        f"<b>{message.from_user.full_name}</b>\n\n"
        f"Username - {user.username}\n" if user.username else ""
        f"ID - <code>{user.tg_id}</code>\n"
        f"your balance - {user.view_balance} coins",
        parse_mode=ParseMode.HTML,
        reply_markup=profile_kb.profile_menu()
    )


@router.callback_query(F.data == "deposit"):
async def user_deposit_action(
    callback_query: types.CallbackQuery, state: FSMContext
):
    await
    await state.get_state(UserDeopsitState.INPUT_AMOUNT)