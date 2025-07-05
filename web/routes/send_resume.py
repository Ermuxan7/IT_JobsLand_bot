from fastapi import APIRouter, Form
from web.utils.telegram import send_to_admin

router = APIRouter()

@router.post("/send-resume/")
async def send_resume(
    full_name: str = Form(...),
    profession: str = Form(...),
    age: int = Form(...),
    address: str = Form(...),
    skills: str = Form(...),
    experience: str = Form(...),
    salary: str = Form(...),
    goal: str = Form(...),
    contacts: str = Form(...),
    portfolio: str = Form(None),
):
    message = (
        f"📄 *Rezyume!*\n"
        f"👤 Ati: {full_name}\n"
        f"🎂 Jasi: {age}\n"
        f"📋 Skills: {skills}\n"
        f"📈 Tajiriybe: {experience}\n"
        f"📞 Baylanisiw: {contacts}"
        f"🌐 Portfolio: {portfolio or 'Korsetilmegen'}"
    )

    result = await send_to_admin(message)
    return {"response": result}