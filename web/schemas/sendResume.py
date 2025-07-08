from pydantic import BaseModel
from fastapi import Form

class SendResume(BaseModel):
    full_name: str 
    profession: str 
    age: int 
    address: str 
    skills: str 
    experience: str 
    salary: str 
    goal: str 
    contacts: str 
    portfolio: str 
    init_data: str