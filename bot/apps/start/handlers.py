from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession

from bot.database.repository import UserRepository

router = Router()


@router.message(Command("start"))
async def start(message: Message, session: AsyncSession):
    repo = UserRepository(session)

    user = await repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await repo.create(message.from_user.id)

    await message.answer("Hello World")
