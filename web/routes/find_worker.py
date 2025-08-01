from fastapi import APIRouter, HTTPException
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
        
        user_id = user_data["user"]["id"]
        print(f"Paydalaniwshi id: {user_id}")

        message = (
            f"   *#vacancy*\n\n"
            f"👨‍💼 *Lawazim*: {payload.position}\n"
            f"🏛 *Mekeme*: {payload.company}\n"
            f"📍 *Mánzil*: {payload.address}\n"
            f"📌 *Talaplar*: {payload.requirements}\n"
            f"⏰ *Jumis waqiti*: {payload.working_time}\n"
            f"💰 *Ayliq*: {payload.salary}\n"
            f"☎️ *Baylanis*: {payload.contacts}\n"
            f"📎 *Qosimsha*: {payload.additional}"
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
