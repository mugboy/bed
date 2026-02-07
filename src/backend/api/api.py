from fastapi import FastAPI
from fastapi.responses import JSONResponse
from backend.db import DB

app = FastAPI()

@app.get("/api/messages", response_class=JSONResponse)
async def messages():
    db = DB()
    return dict({'hello':'world'})