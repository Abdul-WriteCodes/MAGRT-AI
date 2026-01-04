from fastapi import FastAPI
from pydantic import BaseModel
from agents.goal_architect import GoalArchitect
from state import shared_state

app = FastAPI()
goal_agent = GoalArchitect()

class GoalRequest(BaseModel):
    goal: str

@app.post("/set_goal")
def set_goal(request: GoalRequest):
    milestones = goal_agent.generate_milestones(request.goal)
    return {"message": "Goal set successfully!", "milestones": milestones}

@app.get("/state")
def get_state():
    return shared_state.dict()
