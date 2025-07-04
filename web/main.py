from fastapi import FastAPI
from web.routes import find_worker, send_resume, order_project
from web.db import database 

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    print("Database connected")

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    print("Database disconnected")

app.include_router(find_worker.router)
app.include_router(send_resume.router)
app.include_router(order_project.router)