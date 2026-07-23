from app.services.llm import llm

def ats_agent(state):

    prompt = f"""
You are an ATS evaluator.

Compare the resume and job description.

Resume:
{state['resume_summary']}

Job Description:
{state['jd_summary']}

Return ONLY in this format:

ATS Score: <number>/100

Do not explain your reasoning.
Do not write paragraphs.
"""

    response = llm.invoke(prompt)

    state["ats_score"] = response.content.strip()

    return state