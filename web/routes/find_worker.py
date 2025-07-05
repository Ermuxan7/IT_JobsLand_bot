from fastapi import APIRouter, Form
from web.utils.telegram import send_to_admin
from web.utils.verify_init_data import verify_init_data

router = APIRouter()

@router.post("/find-worker/")
async def find_worker(
    company: str = Form(...),
    position: str = Form(...),
    address: str = Form(...),
    requirements: str = Form(...),
    working_time: str = Form(...),
    additional: str = Form(...),
    salary: str = Form(...),
    contacts: str = Form(...),
    init_data: str = Form(...),
):

    user_data = verify_init_data(init_data)
    if not user_data:
        return {"error": "Invalid init_data"}

    user_id = int(user_data["user_id"])

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
        "position": position,
        "company": company,
        "address": address,
        "requirements": requirements,
        "working_time": working_time,
        "salary": salary,
        "contacts": contacts,
        "additional": additional,
        "status": "pending"
    }

    result = await send_to_admin(message, form_data, "vacancy")
    return {"res": result}