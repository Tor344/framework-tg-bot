import asyncio

from aiogram import Bot, Dispatcher
import config.settings as set
from bot.apps.user_click.handlers import router as user_click_router
from bot.apps.start.handlers import router as start_router
from bot.apps.user.handlers import router as user_router
from bot.apps.admin.handlers import router as admin_router

from config.logging_admin import loger
from bot.database.repository import db


bot = Bot(token=set.API_TOKEN)
dp = Dispatcher()

dp.include_router(user_click_router)
dp.include_router(user_router)
dp.include_router(admin_router)
dp.include_router(start_router)


async def main():
    try:
        await db.connect()
        loger.info("Бот запущен")
        await dp.start_polling(bot)
    except Exception as e:
        # ВАЖНО: Добавьте вывод ошибки, чтобы узнать причину
        loger.error(f"Ошибка при запуске: {e}")
        # Или просто: print(f"ОШИБКА: {e}")
    finally:
        await db.close()



if __name__ == "__main__":
    asyncio.run(main())