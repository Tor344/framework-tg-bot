from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("admin"))
async def admin_panel(message: Message):
    pass