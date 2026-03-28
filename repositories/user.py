from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.user import User

class UserRepo:
    def __init__(self,session: AsyncSession):
        self.__session = session

    async def get_user_by_tg_id(self, tg_id: int):
        statement = select(User).where(User.tg_id == tg_id)

        return await self.__session.scalar(statement)

    async def create_or_update_user(self, tg_id: int, fullname: str, username: str):
        user = await self.get_user_by_tg_id(tg_id)

        if not user:
            await self.get_user_(tg_id, fullname, username)
        else:
            user.fullname = fullname
            user.username = username

        await self.__session.commit()
        async def get_user(self, tg_id: int, fullname: str, username: str):
            user = User(tg_id = tg_id, username = username, fullname = fullname)
            self.__session.add(user)