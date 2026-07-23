from fastapi import APIRouter
from pydantic import BaseModel

from app.graph.workflow import graph
from app.rag.retriever import retrieve

router = APIRouter()

# class AnalyzeRequest(BaseModel):

#     resume: str
#     jd: str

class AnalyzeRequest(BaseModel):
    resume_id: str
    jd_id: str

@router.post("/analyze")
async def analyze(data: AnalyzeRequest):

    # Resume Retrieval
    resume_docs = retrieve(
        "Extract all candidate skills, experience, education and projects",
        f"vector_db/{data.resume_id}"
    )

    resume_text = "\n".join(
        [doc.page_content for doc in resume_docs]
    )

    # JD Retrieval
    jd_docs = retrieve(
        "Extract required skills, responsibilities and qualifications",
        f"vector_db/{data.jd_id}"
    )

    jd_text = "\n".join(
        [doc.page_content for doc in jd_docs]
    )

    result = graph.invoke(
        {
            "resume": resume_text,
            "jd": jd_text
        }
    )

    return {
        "ATS Score": result["ats_score"],
        "Missing Skills": result["missing_skills"],
        "Resume Improvements": result["improvements"],
        "Interview Questions": result["interview_questions"]
    }

# @router.post("/analyze")

# async def analyze(data: AnalyzeRequest):

#     result = graph.invoke(
#         {
#             "resume": data.resume,
#             "jd": data.jd
#         }
#     )

#     return result