from fastapi import APIRouter, Form, HTTPException
from web.utils.telegram import send_to_admin
from web.utils.verify_init_data import verify_init_data
from web.schemas.sendResume import SendResume

router = APIRouter()

@router.post("/")
async def send_resume(
    payload: SendResume
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
            f"📄 *Rezyume!*\n"
            f"👤 Ati: {payload.full_name}\n"
            f"🎂 Jasi: {payload.age}\n"
            f"💼 Lawazim: {payload.profession}\n"
            f"📍 Manzil: {payload.address}\n"
            f"📋 Skills: {payload.skills}\n"
            f"📈 Tajiriybe: {payload.experience}\n"
            f"💰 Ayliq: {payload.salary}\n"
            f"🎯 Maqset: {payload.goal}\n"
            f"📞 Baylanisiw: {payload.contacts}\n"
            f"🌐 Portfolio: {payload.portfolio or 'Korsetilmegen'}"
        )

        form_data = {
            "user_id": user_id,
            "full_name": payload.full_name,
            "age": payload.age,
            "profession": payload.profession,
            "address": payload.address,
            "skills": payload.skills,
            "experience": payload.experience,
            "salary": payload.salary,
            "goal": payload.goal,
            "contacts": payload.contacts,
            "portfolio": payload.portfolio,
            "status": "pending"
        }

        result = await send_to_admin(message, form_data, "resume")
        return {"res": result}

    except Exception as e:
        print("❌ send_resume ERROR:", e)
        raise HTTPException(status_code=500, detail="Server error")
