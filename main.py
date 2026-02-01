import asyncio
import sys
import logging

from aiogram import Bot, Dispatcher


from bot.apps.start.handlers import router as start_router
from bot.database.session import engine, Base
import bot.database.models
from bot.middlewares.db import DbSessionMiddleware

import config.settings as set

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout  # Рекомендуется для aiogram/Docker
)

logger = logging.getLogger(__name__)

bot = Bot(token=set.BOT_TOKEN)

dp = Dispatcher()

dp.update.middleware(DbSessionMiddleware())

dp.include_router(start_router)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def main():
    try:
        await init_db()
        logger.info("Бот запущен")
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Ошибка при запуске: {e}")


if __name__ == "__main__":
    asyncio.run(main())