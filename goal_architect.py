from ..state import shared_state, Milestone

class GoalArchitect:
    def generate_milestones(self, goal: str):
        # Dummy milestones for MVP
        milestones = [
            Milestone(title="Break down goal", due_date="2026-01-15"),
            Milestone(title="First milestone achieved", due_date="2026-02-15"),
            Milestone(title="Second milestone achieved", due_date="2026-03-15"),
        ]
        shared_state.user_goal = goal
        shared_state.milestones = milestones
        return milestones
