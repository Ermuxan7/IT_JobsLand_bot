from pydantic import BaseModel
from fastapi import Form

class OrderProject(BaseModel):
    specialist: str = Form(...),
    task: str = Form(...),
    additional: str = Form(...),
    budget: str = Form(...),
    contacts: str = Form(...),
    init_data: str = Form(...)