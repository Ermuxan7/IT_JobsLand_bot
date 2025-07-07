from fastapi import APIRouter, Form, HTTPException
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
    init_data: str = Form(...)
):
    try:
        user_data = verify_init_data(init_data)
        if not user_data:
            return {"res": "error", "reason": "invalid init_data"}
        
        user_id = int(user_data.get("user_id", 0))

        message = (
            f"   📢 *Vakansiya!*\n"
            f"🏢 Kompaniya: {company}\n"
            f"💼 Lawazim: {position}\n"
            f"📋 Talaplar: {requirements}\n"
            f"📍 Manzil: {address}\n"
            f"⏱ Jumis waqti: {working_time}\n"
            f"💰 Ayliq: {salary}\n"
            f"📞 Baylanisiw: {contacts}\n"
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

    except Exception as e:
        print("❌ Qatelik find_worker'da:", e)
        raise HTTPException(status_code=500, detail="Ishki server qatesi")
