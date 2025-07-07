from pydantic import BaseModel
from fastapi import Form

class SendResume(BaseModel):
    full_name: str = Form(...),
    profession: str = Form(...),
    age: int = Form(...),
    address: str = Form(...),
    skills: str = Form(...),
    experience: str = Form(...),
    salary: str = Form(...),
    goal: str = Form(...),
    contacts: str = Form(...),
    portfolio: str = Form(None),
    init_data: str = Form(...)