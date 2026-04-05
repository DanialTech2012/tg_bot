from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def profile_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Top up your balance", 
                callback_data="deposit"
            )
        ]
    ])


def cancel_deposit_action():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Cancel", 
                callback_data="cancel_deposit"
            )
        ]
    ])


def apply_deposit_action():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Yes", 
                callback_data="apply_deposit"
            ),
            InlineKeyboardButton(
                text="No", 
                callback_data="cancel_deposit"
            )
        ]
    ])
