
from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.upload import router as upload_router
from app.api.rag import router as rag_router
from app.api.analyze import router as analyze_router


app = FastAPI(title="AI Resume Intelligence Platform")

app.include_router(chat_router)
app.include_router(upload_router)
app.include_router(rag_router)
app.include_router(analyze_router)


@app.get("/")
def home():
    return {"status": "running"}