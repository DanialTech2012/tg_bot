from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class CategoryCBData(CallbackData, prefix="category"):
    category: str


class BookCBData(CallbackData, prefix="book"):
    id: int
    category: str


def genarate_catalog_kb(catalog):
    Keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    
    for category_cb, category in catalog.items():
        Keyboard.inline_keyboard.append(
            [
                InlineKeyboardButton(
                    text=category["text"],
                    callback_data=CategoryCBData(category=category_cb).pack()
                )
            ]
        )

    return Keyboard 

def generate_books_kb(books, category):
    Keyboard = InlineKeyboardMarkup(inline_keyboard=[])

    for book in books:
        Keyboard.inline_keyboard.append(
            [
                InlineKeyboardButton(
                    text=book["name"].format(book["id"]),
                    callback_data=BookCBData(id=book["id"], category=category).pack()
                )
            ]
        )

    Keyboard.inline_keyboard.append(
        [
            InlineKeyboardButton(text="<< Back", callback_data="catalog")
        ]
    )

    return Keyboard


def back_to_category_books(category):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="<< Back", 
                    callback_data=CategoryCBData(category=category).pack()
                )
            ]
        ]
    )