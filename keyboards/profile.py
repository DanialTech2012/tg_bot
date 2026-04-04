from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def profile_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Top up your balance", 
                callbeck_data="deposit"
            )
        ]
    ])


def cancel_deposit_action():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Cancel", 
                callbeck_data="cancel_deposit"
            )
        ]
    ])


def apply_deposit_action():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Yes", 
                callbeck_data="apply_deposit"
            ),
            InlineKeyboardButton(
                text="No", 
                callbeck_data="cancel_deposit"
            )
        ]
    ])
