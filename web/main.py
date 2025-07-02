from fastapi import FastAPI
from web.routes import find_worker, send_resume, order_project

app = FastAPI()

app.include_router(find_worker.router)
app.include_router(send_resume.router)
app.include_router(order_project.router)