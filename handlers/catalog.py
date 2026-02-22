from aiogram import F, Router, types

from keyboards.catalog import BookCBData, CategoryCBData, genarate_catalog_kb, generate_books_kb
from repositories.categories import CategoryRepo

router = Router()




@router.callback_query(F.data == "catalog")
@router.message(F.text == "Catalog")
async def catalog(update: types.Message | types.CallbackQuery, category_repo: CategoryRepo):
    categories = await category_repo.get_list()
    
    if isinstance(update, types.Message):
        await update.answer(
            "Our catalog:",
            reply_markup=generate_books_kb(categories)
        )
    else:
        await update.message.edit_text(
            "Our catalog:",
            reply_markup=generate_books_kb(categories)
        )


@router.callback_query(CategoryCBData.filter())
async def category_info(callback: types.CallbackQuery, callback_data: CategoryCBData, category_repo: CategoryRepo):
    category = await category_repo.get_by_id(callback_data.category_id)

    await callback.message.edit_text(
        text=category.description,
        reply_markup=generate_books_kb(
            category["books"], 
            callback_data.category
        )
    )

@router.callback_query(BookCBData.filter())
async def book_info(callback: types.CallbackQuery, callback_data: BookCBData):
    book_id = callback_data.id
    category = CATALOG.get(callback_data.category)

    book = None

    for bk in category["books"]:
        if bk["id"] == book_id:
            book = bk
            break

    if  not book:
        return await callback.answer("Didn't find the book")
    
    await callback.message.edit_text(
        f"Name - {book["name"].format(book["id"])}\n"
        f"Description - {book["description"].format(book["id"])}\n"
        f"Price - {book["price"].format(book["id"])}\n\n"
        "Want to buy?",
        reply_markup=BookCBData
    )