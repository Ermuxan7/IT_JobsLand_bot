
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from bot.config import BOT_TOKEN
from bot.handlers import start, callbacks
from web.db import database

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(callbacks.router)


# if __name__ == "__main__":
#     asyncio.run(main())