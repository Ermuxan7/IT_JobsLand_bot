from pydantic import BaseModel
from fastapi import Form

class OrderProject(BaseModel):
    specialist: str
    task: str
    additional: str 
    budget: str 
    contacts: str 
    init_data: str