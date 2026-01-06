from fastapi import FastAPI
from pydantic import BaseModel
from backend.agents.goal_architect import GoalArchitect
from backend.agents.progress_monitor import ProgressMonitor
from backend.agents.intervention_agent import InterventionAgent
from backend.agents.reflection_agent import ReflectionAgent
from backend.state import shared_state

app = FastAPI()

# Initialize agents
goal_agent = GoalArchitect()
progress_agent = ProgressMonitor()
intervention_agent = InterventionAgent()
reflection_agent = ReflectionAgent()

class GoalRequest(BaseModel):
    goal: str

class ProgressRequest(BaseModel):
    action: str
    status: str

@app.post("/set_goal")
def set_goal(request: GoalRequest):
    milestones = goal_agent.generate_milestones(request.goal)
    return {"message": "Goal set successfully!", "milestones": milestones}

@app.post("/log_progress")
def log_progress(request: ProgressRequest):
    result = progress_agent.log_progress(request.action, request.status)
    return result

@app.get("/interventions")
def get_interventions():
    suggestions = intervention_agent.suggest_intervention()
    return {"interventions": suggestions}

@app.get("/reflection")
def get_reflection():
    reflection = reflection_agent.summarize()
    return {"reflection": reflection}

@app.get("/state")
def get_state():
    return shared_state.dict()
