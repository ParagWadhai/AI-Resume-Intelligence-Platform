from fastapi import APIRouter, UploadFile, File
from uuid import uuid4
import os

from app.services.pdf_parser import extract_text
from app.rag.vector_store import create_vector_store

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_id = str(uuid4())

    filename = f"{file_id}.pdf"

    filepath = os.path.join(UPLOAD_FOLDER, filename)

    with open(filepath, "wb") as f:
        f.write(await file.read())

    text = extract_text(filepath)

    VECTOR_PATH = f"vector_db/{file_id}"

    create_vector_store(
        text,
        VECTOR_PATH
    )

    return {
        "resume_id": file_id,
        "filename": filename,
        "characters": len(text),
        "preview": text[:1000]
    }

@router.post("/upload-jd")
async def upload_jd(file: UploadFile = File(...)):

    file_id = str(uuid4())

    filename = f"{file_id}.pdf"

    filepath = os.path.join(UPLOAD_FOLDER, filename)

    with open(filepath, "wb") as f:
        f.write(await file.read())

    text = extract_text(filepath)

    VECTOR_PATH = f"vector_db/{file_id}"

    create_vector_store(
        text,
        VECTOR_PATH
    )

    return {
        "jd_id": file_id,
        "filename": filename,
        "characters": len(text),
        "preview": text[:1000]
    }