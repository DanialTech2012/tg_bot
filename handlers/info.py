from aiogram import F, Router, types

router = Router()


@router.message(F.text == "About Us")
async def info(message: types.Message):
    await message.answer(
        (
            "I am a book buying bot.\n" \
            "You can look through "
            "my entire catalog and byu the book you like.\n\n"
            "Good reading"
        )
    )
