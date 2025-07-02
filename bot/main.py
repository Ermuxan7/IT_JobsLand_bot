import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from config import BOT_TOKEN
from handlers import start

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start.router)

@dp.message(F.text == "/get_chat_id")
async def get_chat_id(msg: Message):
    await msg.answer(f"Chat ID: `{msg.chat.id}`", parse_mode="Markdown")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())