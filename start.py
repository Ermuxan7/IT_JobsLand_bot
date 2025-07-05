import asyncio
from fastapi import FastAPI
from web.main import app as fastapi_app
from bot.main import bot, dp

async def start_bot():
    from aiogram import Dispatcher
    await dp.start_polling(bot)

def create_app():
    app = fastapi_app
    return app

# Asynchronous run (FastAPI + Bot)
if __name__ == "__main__":
    import uvicorn

    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())
    
    uvicorn.run("start:create_app", host="0.0.0.0", port=8001, reload=False)
