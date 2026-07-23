from app.services.llm import llm

def skill_gap_agent(state):

    prompt = f"""
Compare the resume and job description.

Return ONLY the missing skills.

Example:

- AWS
- Kubernetes
- Terraform
- LangGraph

No explanation.
"""

    response = llm.invoke(prompt)

    state["missing_skills"] = response.content.strip()

    return state