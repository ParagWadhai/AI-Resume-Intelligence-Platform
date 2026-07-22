from fastapi import FastAPI
from app.api.chat import router as chat_router

app = FastAPI(
    title="AI Resume Intelligence Platform"
)

app.include_router(chat_router)


@app.get("/")
def home():
    return {
        "status": "running"
    }