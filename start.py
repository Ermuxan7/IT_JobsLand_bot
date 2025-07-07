# start.py

import asyncio
import os
import uvicorn
from web.main import app as fastapi_app
from bot.main import bot, dp

async def start_bot():
    print("✅ Starting polling...")
    await dp.start_polling(bot)

async def start_api():
    port = int(os.environ.get("PORT", 8080))
    config = uvicorn.Config(app=fastapi_app, host="0.0.0.0", port=port)
    server = uvicorn.Server(config)
    await server.serve()

# 💡 BU MUHIM! Railway 'start:app' ni mana shu funksiya sifatida kutmoqda:
async def app():
    await asyncio.gather(
        start_api(),
        start_bot()
    )
