import asyncio
from aiogram import Bot, Dispatcher, Router
from config import API_TOKEN, BOT_PROPERTIES
from handlers import start, register, balance, topup
from database.models import init_db

bot = Bot(token=API_TOKEN, default=BOT_PROPERTIES)
dp = Dispatcher()
router = Router()

router.include_routers(
    start.router,
    register.router,
    balance.router,
    topup.router
)

dp.include_router(router)

async def main():
    init_db()
    print("✅ Бот запущено")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
