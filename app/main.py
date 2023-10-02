from fastapi import FastAPI

app = FastAPI(title="MaisTODOS CreditCard API")


@app.get("/")
def index():
    return {"ping": "pong!"}
