import os, requests, uuid
from dotenv import load_dotenv
from web.db import database, vacancies

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
ADMIN_ID = os.getenv("ADMIN_ID")

async def send_to_admin(message: str):
    message_id = uuid.uuid4()

    if not database.is_connected:
        await database.connect()

    await database.execute(vacancies.insert().values(
        id = message_id,
        message = message,
        status = "pending"
    ))

    inline_keyboard = {
        "inline_keyboard": [[
                {"text": "✅ Tastiyiqlaw", "callback_data": f'approve::{str(message_id)}'},
                {"text": "❌ Biykar etiw", "callback_data": f'reject::{message_id}'},
            ]]
    }

    payload = {
        "chat_id": ADMIN_ID,
        "text": f"📥 Jan'a vakansiya keldi.\nID: `{message_id}`",
        "parse_mode": "Markdown",
        "reply_markup": inline_keyboard
    }

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    res = requests.post(url, json=payload)
    return res.json()


async def send_telegram_message(message: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    res = requests.post(url, data=payload, timeout=10)
    return {"status": "success", "response": res.json()}