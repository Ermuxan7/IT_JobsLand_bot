from fastapi import APIRouter, Form
from web.utils.telegram import send_to_admin
from web.utils.verify_init_data import verify_init_data

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
    init_data: str = Form(...)
):
    user_data = verify_init_data(init_data)
    if not user_data:
        return {"error": "Invalid init_data"}

    user_id = int(user_data["user_id"])

    message = (
        f"📄 *Rezyume!*\n"
        f"👤 Ati: {full_name}\n"
        f"🎂 Jasi: {age}\n"
        f"💼 Lawazim: {profession}\n"
        f"📍 Manzil: {address}\n"
        f"📋 Skills: {skills}\n"
        f"📈 Tajiriybe: {experience}\n"
        f"💰 Ayliq: {salary}\n"
        f"🎯 Maqset: {goal}\n"
        f"📞 Baylanisiw: {contacts}"
        f"🌐 Portfolio: {portfolio or 'Korsetilmegen'}"
    )

    form_data = {
        "user_id": user_id,
        "full_name": full_name,
        "age": age,
        "profession": profession,
        "address": address,
        "skills": skills,
        "experience": experience,
        "salary": salary,
        "goal": goal,
        "contacts": contacts,
        "portfolio": portfolio,
        "status": "pending"
    }

    result = await send_to_admin(message, form_data, "resume")
    return {"response": result}