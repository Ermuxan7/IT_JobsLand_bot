import requests, uuid
from datetime import datetime
from web.db import database, vacancies, resumes, projects
from bot.config import BOT_TOKEN, CHANNEL_ID, ADMIN_ID


async def send_to_admin(message: str, form_data: dict, form_type: str):
    item_id = uuid.uuid4()

    if not database.is_connected:
        await database.connect()

    if form_type == "vacancy":
        await database.execute(vacancies.insert().values(
            id = item_id,
            user_id = form_data["user_id"],
            position = form_data["position"],
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
    elif form_type == "resume":
        await database.execute(resumes.insert().values(
            id = item_id,
            user_id = form_data["user_id"],
            full_name = form_data["full_name"],
            age = form_data["age"],
            address = form_data["address"],
            profession = form_data["profession"],
            skills = form_data["skills"],
            experience = form_data["experience"],
            salary = form_data["salary"],
            goal = form_data["goal"],
            contacts = form_data["contacts"],
            portfolio = form_data["portfolio"],
            status = "pending",
            created_at = datetime.utcnow(),
            updated_at = datetime.utcnow(),
        ))
    elif form_type == "project":
        await database.execute(projects.insert().values(
            id = item_id,
            user_id = form_data["user_id"],
            specialist = form_data["specialist"],
            task = form_data["task"],
            additional = form_data["additional"],
            budget = form_data["budget"],
            contacts = form_data["contacts"],
            status = "pending",
            created_at = datetime.utcnow(),
            updated_at = datetime.utcnow(),
        ))
    else: 
        raise ValueError("Qate forma turi!")

    inline_keyboard = {
        "inline_keyboard": [[
                {"text": "✅ Tastiyiqlaw", "callback_data": f'approve_{form_type}_{item_id}'},
                {"text": "❌ Biykar etiw", "callback_data": f'reject_{form_type}_{item_id}'},
            ]]
    }

    payload = {
        "chat_id": ADMIN_ID,
        "text": f"📥 Jan'a {form_type} keldi.\n\n{message}",
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