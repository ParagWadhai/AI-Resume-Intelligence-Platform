from app.services.llm import llm

def interview_agent(state):

    prompt = f"""
You are an AI Technical Interviewer.

Resume:
{state['resume_summary']}

Job Description:
{state['jd_summary']}

Generate exactly 10 technical interview questions.

Rules:
- Number the questions from 1 to 10.
- No answers.
- No explanations.
- Questions should test the candidate based on the resume and the job description.
"""

    response = llm.invoke(prompt)

    state["interview_questions"] = response.content.strip()

    return state