from app.services.llm import llm

def resume_agent(state):

    prompt = f"""
Summarize this resume.

Resume:
{state['resume']}
"""

    response = llm.invoke(prompt)

    state["resume_summary"] = response.content

    return state