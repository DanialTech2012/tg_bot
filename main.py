import asyncio
from aiogram import Bot, Dispatcher

from handlers._init_ import register_routes
from database.models._init_ import BaseModel 
from middlewares import register_middlewares
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker



TOKEN = "8462182666:AAGMr9ibQUzRPoM3M6foxRn28oN9xS8WWUY"


async def  init_model(engine):
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    engine = create_async_engine(
        url= "sqlite+aiosqlite:///book_shop.db"
    )
    session_maker = async_sessionmaker(engine, expire_on_commit= False)

    register_middlewares(dp,session_maker )
    register_routes(dp)
    
    await init_model(engine)
    await dp.start_polling(bot)


if __name__ =="__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped!")