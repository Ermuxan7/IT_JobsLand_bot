from fastapi import APIRouter, Form
from web.utils.telegram import send_to_admin

router = APIRouter()

@router.post("/find-worker/")
async def find_worker(
    user_id: int = Form(...),
    company: str = Form(...),
    position: str = Form(...),
    address: str = Form(...),
    requirements: str = Form(...),
    working_time: str = Form(...),
    additional: str = Form(...),
    salary: str = Form(...),
    contacts: str = Form(...),
):
    message = (
        f"   📢 *Vakansiya!*\n"
        f"🏢 Kompaniya: {company}\n"
        f"💼 Lawazim: {position}\n"
        f"📋 Talaplar: {requirements}\n"
        f"📍 Manzil: {address}\n"
        f"⏱ Jumis waqti: {working_time}\n"
        f"📋 Talaplar: {requirements}\n"
        f"💰 Ayliq: {salary}\n"
        f"📞 Baylanisiw: {contacts}"
        f"📝 Qosimsha: {additional}"
    )

    form_data = {
        "user_id": user_id,
        "job_title": position,
        "company": company,
        "address": address,
        "requirements": requirements,
        "working_time": working_time,
        "salary": salary,
        "contacts": contacts,
        "additional": additional,
        "status": "pending"
    }

    result = await send_to_admin(message, form_data)
    return {"res": result}