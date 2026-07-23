from langgraph.graph import StateGraph, END

from app.graph.state import GraphState

from app.agents.resume_agent import resume_agent
from app.agents.jd_agent import jd_agent
from app.agents.ats_agent import ats_agent
from app.agents.skill_gap_agent import skill_gap_agent
from app.agents.improvement_agent import improvement_agent
from app.agents.interview_agent import interview_agent

builder = StateGraph(GraphState)

builder.add_node("resume", resume_agent)
builder.add_node("jd", jd_agent)
builder.add_node("ats", ats_agent)
builder.add_node("skill", skill_gap_agent)
builder.add_node("improvement", improvement_agent)
builder.add_node("interview", interview_agent)

builder.set_entry_point("resume")

builder.add_edge("resume", "jd")
builder.add_edge("jd", "ats")
builder.add_edge("ats", "skill")
builder.add_edge("skill", "improvement")
builder.add_edge("improvement", "interview")
builder.add_edge("interview", END)

graph = builder.compile()