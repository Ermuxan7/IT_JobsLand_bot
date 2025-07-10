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
        
        user_id = user_data["user"]["id"]
        print(f"Paydalaniwshi id: {user_id}")
        
        message = (
             f"   *#resume*\n\n"
            f"*Kásibim*: {payload.profession}\n"
            f"*FAA*: {payload.full_name}\n"
            f"*Jasim*: {payload.age}\n"
            f"*Aymaq*: {payload.address}\n"
            f"*Uqiplarim*: {payload.skills}\n"
            f"*Tájiriybe*: {payload.experience}\n"
            f"*Portfolio*: {payload.portfolio or 'Korsetilmegen'}"
            f"*Ayliq kútim*: {payload.salary}\n"
            f"*Maqset*: {payload.goal}\n"
            f"*Baylanis*: {payload.contacts}\n"
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
