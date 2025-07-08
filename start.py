import asyncio
import os
import uvicorn
from web.main import app as fastapi_app
from bot.main import bot, dp
from web.db import database

async def start_bot():
    print("✅ Starting polling...")
    await database.connect()
    try:
        await dp.start_polling(bot)
    finally:
        await database.disconnect()

async def start_api():
    port = int(os.environ.get("PORT", 8080))
    config = uvicorn.Config(app=fastapi_app)
    server = uvicorn.Server(config)
    await server.serve()

async def app():
    await asyncio.gather(
        start_api(),
        start_bot()
    )

if __name__ == "__main__":
    asyncio.run(app())