from aiogram import F, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from keyboards import profile as profile_kb
from repositories.user import UserRepo
from states.profile import UserDepositState

router = Router()

@router.message(F.text == "Profile")
async def user_profile_info(
    message: types.Message, 
    user_repo: UserRepo,
    state: FSMContext
):
    user  = await user_repo.get_user_by_tg_id(message.from_user.id)

    await message.message.edit_text(
        f"<b>{message.from_user.full_name}</b>\n\n"
        f"Username - {user.username}\n" if user.username else ""
        f"ID - <code>{user.tg.id}</code>\n"
        f"your balance - {user.balance} coins",
        parse_mode=ParseMode.HTML,
        reply_markup=profile_kb.profile_menu()
    )

@router.callback_query(F.data == "deposit")
async def user_deposit_action(
    callback_query: types.CallbackQuery, state:FSMContext, user_repo: UserRepo
):
    await callback_query.answer()
    await callback_query.message.edit_text(
        "Enter the replenishment amount:",
        reply_markup=profile_kb.cancel_deposit_action()
    )
    await state.set_state(UserDepositState.IMPUT_AMOUNT)


@router.callback_query(StateFilter(UserDepositState), F.data == "cancel_deposit")
async def user_deposit_action_cancel(callback_query: types.CallbackQuery, state:FSMContext, user_repo: UserRepo):
    await state.clear()
    await callback_query.answer()

    user = await user_repo.get_user_by_tg_id(callback_query.from_user.id)

    await callback_query.message.edit_text(
        f"<b>{callback_query.from_user.full_name}</b>\n\n"
        f"Username - {user.username}\n" if user.username else ""
        f"ID - <code>{user.tg.id}</code>\n"
        f"your balance - {user.balance} coins",
        parse_mode=ParseMode.HTML,
        reply_markup=profile_kb.profile_menu()
    )


@router.message(UserDepositState.IMPUT_AMOUNT)
async def user_deposit_amount(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Enter an integer")
        return
    
    amount = int(message.text)
    
    await state.set_data({"amount": amount})
    await message.answer(
        f"Do you confirm that the balance has reached {amount} coins",
        reply_markup=profile_kb.cancel_deposit_action()
    )