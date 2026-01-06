from ..state import shared_state, Reflection
from datetime import date

class ReflectionAgent:
    def summarize(self):
        summary_text = f"Goal: {shared_state.user_goal}\n"
        completed = [m.title for m in shared_state.milestones if m.completed]
        pending = [m.title for m in shared_state.milestones if not m.completed]
        summary_text += f"Completed milestones: {completed}\n"
        summary_text += f"Pending milestones: {pending}\n"
        summary_text += f"Progress logs: {[log.action for log in shared_state.progress_logs]}"
        new_reflection = Reflection(date=str(date.today()), summary=summary_text)
        shared_state.reflections.append(new_reflection)
        return new_reflection
