from fastapi import APIRouter, Form
from web.utils.telegram import send_to_admin

router = APIRouter()

@router.post("/order-project/")
async def order_project(
    user_id: int = Form(...),
    specialist: str = Form(...),
    task: str = Form(...),
    additional: str = Form(...),
    budget: str = Form(...),
    contacts: str = Form(...),
):
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