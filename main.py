from fastapi import FastAPI
from sqlalchemy import true

app = FastAPI()

@app.get("/")
def index():
    return {"status": true, "message": "MaisTODOS Card API v1.0.0-alpha"}