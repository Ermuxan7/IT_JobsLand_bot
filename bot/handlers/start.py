from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_command(msg: Message):
    await msg.answer("Assalawma aleykum!")