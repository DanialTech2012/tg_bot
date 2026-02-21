from aiogram import F, Router, types

from keyboards.catalog import BookCBData, CategoryCBData, genarate_catalog_kb, generate_books_kb

router = Router()


CATALOG = {
    "Romans": 
    {"text": "Romans", 
     "description":"Book romans",
     "books" : [ {
         "id" : 1,
         "name" : "Книга {}",
         "description" : "Описание книги {}",
         "price" : 100
     },
     {
         "id" : 2,
         "name" : "Книга {}",
         "description" : "Описание книги {}",
         "price" : 200
     }
     ]},
    "Fantasy": {"text": "Fantasy", "description":"Book fantasy"},
    "Horror": {"text": "Horror", "description":"Book horror "},
    "Detectives": {"text": "Detectives", "description":"Book detectives"},
    "Documentaries": {"text": "Documentaries", "description":"Book documentaries"},
}


@router.callback_query(F.data == "catalog")
@router.message(F.text == "Catalog")
async def catalog(update: types.Message | types.CallbackQuery):
    
    if isinstance(update, types.Message):
        await update.answer(
            "Our catalog:",
            reply_markup=generate_books_kb(CATALOG)
        )
    else:
        await update.message.edit_text(
            "Our catalog:",
            reply_markup=generate_books_kb(CATALOG)
        )


@router.callback_query(CategoryCBData.filter())
async def category_info(callback: types.CallbackQuery, callback_data: CategoryCBData):
    category = CATALOG.get(callback_data.category)

    await callback.message.edit_text(
        text=category["description"],
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