from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class CategoryCBData(CallbackData, prefix="category"):
    category: str


class BookCBData(CallbackData, prefix="book"):
    id: int
    category_id: int


def genarate_catalog_kb(categories):
    Keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    
    for category in categories:
        Keyboard.inline_keyboard.append(
            [
                InlineKeyboardButton(
                    text=category.name,
                    callback_data=CategoryCBData(category_id=category.id).pack()
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