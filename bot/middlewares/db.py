from aiogram import BaseMiddleware
from typing import Callable, Dict, Any, Awaitable
from sqlalchemy.ext.asyncio import AsyncSession
from bot.database.session import SessionMaker

class DbSessionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any],
    ):
        async with SessionMaker() as session:
            data["session"] = session
            return await handler(event, data)
