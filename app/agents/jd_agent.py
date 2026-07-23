from app.services.llm import llm

def jd_agent(state):

    prompt = f"""
Summarize this job description.

JD:
{state['jd']}
"""

    response = llm.invoke(prompt)

    state["jd_summary"] = response.content

    return state