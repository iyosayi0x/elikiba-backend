from fastapi import FastAPI
from app.routes import posts_router

app = FastAPI()


@app.get("/")
def ping():
    return "PONG"


app.include_router(posts_router)
