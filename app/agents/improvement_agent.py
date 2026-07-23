from app.services.llm import llm

def improvement_agent(state):

#     prompt = f"""
# Suggest resume improvements.

# Missing Skills:
# {state['missing_skills']}
# """
    prompt = f"""
Based on these missing skills:

{state['missing_skills']}

Give ONLY 5 resume improvement suggestions.

Example:

- Add AWS deployment project
- Mention Docker
- Add LangGraph project
- Quantify achievements
- Mention cloud deployment

No explanation.
"""

    response = llm.invoke(prompt)

    state["improvements"] = response.content

    return state