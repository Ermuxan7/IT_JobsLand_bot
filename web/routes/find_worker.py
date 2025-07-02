from fastapi import APIRouter, Form
from web.utils.telegram import send_telegram_message

router = APIRouter()

@router.post("/find-worker/")
async def find_worker(
    company: str = Form(...),
    position: str = Form(...),
    requirements: str = Form(...),
    salary: str = Form(...),
    contact: str = Form(...),
):
    message = (
        f"📢 *Vakansiya!*\n"
        f"🏢 Kompaniya: {company}\n"
        f"💼 Lawazim: {position}\n"
        f"📋 Talaplar: {requirements}\n"
        f"💰 Ayliq: {salary}\n"
        f"📞 Baylanisiw: {contact}"
    )

    result = send_telegram_message(message)
    return {"response": result}