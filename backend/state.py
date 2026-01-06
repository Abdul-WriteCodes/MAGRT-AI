from typing import List, Dict
from pydantic import BaseModel

class Milestone(BaseModel):
    title: str
    due_date: str
    completed: bool = False

class ProgressLog(BaseModel):
    date: str
    action: str
    status: str

class Intervention(BaseModel):
    date: str
    suggestion: str

class Reflection(BaseModel):
    date: str
    summary: str

class SharedState(BaseModel):
    user_goal: str = ""
    milestones: List[Milestone] = []
    progress_logs: List[ProgressLog] = []
    interventions: List[Intervention] = []
    reflections: List[Reflection] = []

# Initialize shared state
shared_state = SharedState()
