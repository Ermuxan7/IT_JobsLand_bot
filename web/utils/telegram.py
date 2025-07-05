import requests, uuid
from datetime import datetime
from web.db import database, vacancies
from bot.config import BOT_TOKEN, CHANNEL_ID, ADMIN_ID


async def send_to_admin(message: str, form_data: dict):
    vacancy_id = uuid.uuid4()

    if not database.is_connected:
        await database.connect()

    await database.execute(vacancies.insert().values(
        id = vacancy_id,
        user_id = form_data["user_id"],
        job_title = form_data["job_title"],
        company = form_data["company"],
        address = form_data["address"],
        requirements = form_data["requirements"],
        working_time = form_data["working_time"],
        salary = form_data["salary"],
        contacts = form_data["contacts"],
        additional = form_data["additional"],
        status = "pending",
        created_at = datetime.utcnow(),
        updated_at = datetime.utcnow(),
    ))

    inline_keyboard = {
        "inline_keyboard": [[
                {"text": "✅ Tastiyiqlaw", "callback_data": f'approve::{str(vacancy_id)}'},
                {"text": "❌ Biykar etiw", "callback_data": f'reject::{vacancy_id}'},
            ]]
    }

    payload = {
        "chat_id": ADMIN_ID,
        "text": f"📥 Jan'a vakansiya keldi.\n\n`{message}`",
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