from backend.state import shared_state, Intervention
from datetime import date

class InterventionAgent:
    def suggest_intervention(self):
        deviations = [m.title for m in shared_state.milestones if not m.completed]
        suggestions = []
        for d in deviations:
            suggestion = f"Consider reviewing milestone: {d}"
            new_intervention = Intervention(date=str(date.today()), suggestion=suggestion)
            shared_state.interventions.append(new_intervention)
            suggestions.append(new_intervention)
        return suggestions
