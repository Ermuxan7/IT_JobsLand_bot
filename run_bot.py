import asyncio
from bot.main import bot, dp
from web.db import database

async def main():
    await database.connect()
    try:
        print("🤖 Bot is running...")
        await dp.start_polling(bot)
    finally:
        await database.disconnect()
        print("📴 Bot stopped.")

if __name__ == "__main__":
    asyncio.run(main())
