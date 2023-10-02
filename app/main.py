from fastapi import FastAPI
from routes.v1.api import router

app = FastAPI(title="MaisTODOS CreditCard API")


@app.get("/")
def index():
    return {"ping": "pong!"}


app.include_router(router)
