from pydantic import BaseModel
from fastapi import Form

class FindWorkerForm(BaseModel):
    company: str = Form(...)
    position: str = Form(...)
    address: str = Form(...)
    requirements: str = Form(...)
    working_time: str = Form(...)
    additional: str = Form(...)
    salary: str = Form(...)
    contacts: str = Form(...)
    init_data: str = Form(...)