from fastapi import APIRouter, Form
from web.utils.telegram import send_to_admin

router = APIRouter()

@router.post("/order-project/")
async def order_project(
    client_name: str = Form(...),
    project_type: str = Form(...),
    description: str = Form(...),
    budget: str = Form(...),
    contact: str = Form(...),
):
    message = (
        f"🛠 *Proyekt buyirtpa!*\n"
        f"👤 Buyirtpashi: {client_name}\n"
        f"📌 Proyekt-turi: {project_type}\n"
        f"📝 Proekt haqqinda: {description}\n"
        f"💰 Budjet: {budget}\n"
        f"📞 Baylanisiw: {contact}"
    )

    result = await send_to_admin(message)
    return {"response": result}