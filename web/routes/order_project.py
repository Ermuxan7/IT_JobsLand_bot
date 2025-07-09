from fastapi import APIRouter, Form, HTTPException
from web.utils.telegram import send_to_admin
from web.utils.verify_init_data import verify_init_data
from web.schemas.orderProject import OrderProject

router = APIRouter()

@router.post("/")
async def order_project(
    payload: OrderProject
):  
    try:
        user_data = verify_init_data(payload.init_data)
        
        user_id = user_data["user"]["id"]
        print(f"Paydalaniwshi id: {user_id}")
        
        message = (
            f"🛠 *Proyekt buyirtpa!*\n"
            f"👤 Buyirtpashi: {payload.specialist}\n"
            f"📌 Proyekt-turi: {payload.task}\n"
            f"📝 Proekt haqqinda: {payload.additional}\n"
            f"💰 Budjet: {payload.budget}\n"
            f"📞 Baylanisiw: {payload.contacts}"
        )

        form_data = {
            "user_id": user_id,
            "specialist": payload.specialist,
            "task": payload.task,
            "additional": payload.additional,
            "budget": payload.budget,
            "contacts": payload.contacts,
            "status": "pending"
        }

        result = await send_to_admin(message, form_data, "project")
        return {"res": result}

    except Exception as e:
        print("❌ order_project ERROR:", e)
        raise HTTPException(status_code=500, detail="Server error")
