from fastapi import APIRouter, Form
from web.utils.telegram import send_to_admin
from web.utils.verify_init_data import verify_init_data

router = APIRouter()

@router.post("/order-project/")
async def order_project(
    specialist: str = Form(...),
    task: str = Form(...),
    additional: str = Form(...),
    budget: str = Form(...),
    contacts: str = Form(...),
    init_data: str = Form(...),
):  
    
    user_data = verify_init_data(init_data)
    if not user_data:
        return {"error": "Invalid init_data"}

    user_id = int(user_data["user_id"])
    
    message = (
        f"🛠 *Proyekt buyirtpa!*\n"
        f"👤 Buyirtpashi: {specialist}\n"
        f"📌 Proyekt-turi: {task}\n"
        f"📝 Proekt haqqinda: {additional}\n"
        f"💰 Budjet: {budget}\n"
        f"📞 Baylanisiw: {contacts}"
    )

    form_data = {
        "user_id": user_id,
        "specialist": specialist,
        "task": task,
        "additional": additional,
        "budget": budget,
        "contacts": contacts,
        "status": "pending"
    }

    result = await send_to_admin(message, form_data, "project")
    return {"response": result}