import asyncio
from aiogram import Bot, Dispatcher
from bot.config import BOT_TOKEN
from bot.handlers import start, callbacks
from web.db import database

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(callbacks.router)

async def main():
    await database.connect()
    try:
        await dp.start_polling(bot)
    finally:
        await database.disconnect()

# if __name__ == "__main__":
#     asyncio.run(main())