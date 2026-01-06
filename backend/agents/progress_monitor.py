from backend.state import shared_state, ProgressLog
from datetime import date

class ProgressMonitor:
    def log_progress(self, action: str, status: str):
        new_log = ProgressLog(
            date=str(date.today()),
            action=action,
            status=status
        )
        shared_state.progress_logs.append(new_log)
        # Check if any milestones are completed
        completed_milestones = []
        for m in shared_state.milestones:
            if not m.completed and action.lower() in m.title.lower():
                m.completed = True
                completed_milestones.append(m.title)
        return {"new_log": new_log, "completed_milestones": completed_milestones}

    def check_deviation(self):
        # Simple deviation: any milestone not completed by today
        deviations = []
        for m in shared_state.milestones:
            if not m.completed:
                deviations.append(m.title)
        return deviations
