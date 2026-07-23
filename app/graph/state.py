from typing import TypedDict

class GraphState(TypedDict):
    resume: str
    jd: str

    resume_summary: str
    jd_summary: str

    ats_score: str
    missing_skills: str
    improvements: str
    interview_questions: str