from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class CategoryCBData(CallbackData, prefix="category"):
    category_id: int


class BookCBData(CallbackData, prefix="book"):
    id: int


class BuyBookCBData(CallbackData, prefix="buy-book"):
    id: int


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

def generate_books_kb(books):
    Keyboard = InlineKeyboardMarkup(inline_keyboard=[])

    for book in books:
        Keyboard.inline_keyboard.append(
            [
                InlineKeyboardButton(
                    text=book.name.format(book.id),
                    callback_data=BookCBData(id=book.id).pack()
                )
            ]
        )

    Keyboard.inline_keyboard.append(
        [
            InlineKeyboardButton(text="<< Back", callback_data="catalog")
        ]
    )

    return Keyboard


def back_to_category_books(book_id, category_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Buy",
                    callback_data=BuyBookCBData(id=book_id).pack()
                )
            ],
            [
                InlineKeyboardButton(
                    text="<< Back", 
                    callback_data=CategoryCBData(category_id=category_id).pack()
                )
            ]
        ]
    )