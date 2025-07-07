import asyncio
import os
import uvicorn
from web.main import app as fastapi_app
from bot.main import bot, dp

async def start_bot():
    try:
        print("✅ Starting polling...")
        await dp.start_polling(bot)
    except Exception as e:
        print(f"❌ Polling failed: {e}")

async def start_api():
    port = int(os.environ.get("PORT", 8080))
    config = uvicorn.Config(app=fastapi_app, host="0.0.0.0", port=port)
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    await asyncio.gather(
        start_bot(),
        start_api()
    )

if __name__ == "__main__":
    asyncio.run(main())
