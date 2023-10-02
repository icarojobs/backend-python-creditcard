import sys

sys.path.append('..')

from fastapi import FastAPI
from app.routes.v1.api import user_router
from app.routes.v1.api import credit_card_router

app = FastAPI(title="MaisTODOS CreditCard API")


@app.get("/")
def index():
    return {"ping": "pong!"}


app.include_router(user_router)
app.include_router(credit_card_router)
