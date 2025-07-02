from fastapi import APIRouter, Form
from web.utils.telegram import send_telegram_message

router = APIRouter()

@router.post("/send-resume/")
async def send_resume(
    full_name: str = Form(...),
    age: str = Form(...),
    skills: str = Form(...),
    experience: str = Form(...),
    contact: str = Form(...),
    portfolio: str = Form(None),
):
    message = (
        f"📄 *Rezyume!*\n"
        f"👤 Ati: {full_name}\n"
        f"🎂 Jasi: {age}\n"
        f"📋 Skills: {skills}\n"
        f"📈 Tajiriybe: {experience}\n"
        f"📞 Baylanisiw: {contact}"
        f"🌐 Portfolio: {portfolio or 'Korsetilmegen'}"
    )

    result = send_telegram_message(message)
    return {"response": result}