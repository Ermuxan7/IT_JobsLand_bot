from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from web.routes import find_worker, send_resume, order_project

from web.db import database 

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(request: Request):
    print("Start..")
    await database.connect()
    yield
    await database.disconnect()
    print("End..")


app = FastAPI(lifespan=lifespan)

origins = [
    "https://online-jobs-bot-ui.vercel.app",  
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(find_worker.router, prefix="/find-worker", tags=['Find Worker ushin Api'])
app.include_router(send_resume.router, prefix="/send-resume", tags=['Api for send resume'])
app.include_router(order_project.router, prefix="/order-project", tags=['Api for order project'])

