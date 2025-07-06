import asyncio
import uvicorn
from web.main import app as fastapi_app
from bot.main import bot, dp
from aiogram import Dispatcher

async def start_bot():
    await dp.start_polling(bot)

async def main():
    # Parallel ishga tushurish (FastAPI va Bot)
    bot_task = asyncio.create_task(start_bot())
    
    config = uvicorn.Config(app=fastapi_app, host="0.0.0.0", port=8001)
    server = uvicorn.Server(config)

    api_task = asyncio.create_task(server.serve())
    
    await asyncio.gather(bot_task, api_task)

if __name__ == "__main__":
    asyncio.run(main())
