from fastapi import APIRouter, Form, HTTPException
from web.utils.telegram import send_to_admin
from web.utils.verify_init_data import verify_init_data
from web.schemas.findWorker import FindWorkerForm

router = APIRouter()

@router.post("/")
async def find_worker(
    payload: FindWorkerForm,
):
    try:
        user_data = verify_init_data(payload.init_data)
        if not user_data:
            return {"res": "error", "reason": "invalid init_data"}
        
        user_id_str = user_data.get("user_id")
        if not user_id_str:
            return {"res": "error", "reason": "missing user.id"}
        
        user_id = int(user_id_str)

        message = (
            f"   📢 *Vakansiya!*\n"
            f"🏢 Kompaniya: {payload.company}\n"
            f"💼 Lawazim: {payload.position}\n"
            f"📋 Talaplar: {payload.requirements}\n"
            f"📍 Manzil: {payload.address}\n"
            f"⏱ Jumis waqti: {payload.working_time}\n"
            f"💰 Ayliq: {payload.salary}\n"
            f"📞 Baylanisiw: {payload.contacts}\n"
            f"📝 Qosimsha: {payload.additional}"
        )

        form_data = {
            "user_id": user_id,
            "position": payload.position,
            "company": payload.company,
            "address": payload.address,
            "requirements": payload.requirements,
            "working_time": payload.working_time,
            "salary": payload.salary,
            "contacts": payload.contacts,
            "additional": payload.additional,
            "status": "pending"
        }

        result = await send_to_admin(message, form_data, "vacancy")
        return {"res": result}

    except Exception as e:
        print("❌ Qatelik find_worker'da:", e)
        raise HTTPException(status_code=500, detail=f"Ishki server qatesi")
