from pydantic import BaseModel
from fastapi import Form

class FindWorkerForm(BaseModel):
    company: str 
    position: str 
    address: str 
    requirements: str 
    working_time: str 
    additional: str 
    salary: str 
    contacts: str 
    init_data: str