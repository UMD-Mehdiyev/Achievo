from Goal import Goal, GoalEntry
import customtkinter as ct


class ScrollableGoalEntryFrame(ct.CTkScrollableFrame):
    def __init__(self, master, goals: list[Goal], command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.goals = goals
        self.current_task_window = None

        self.grid_rowconfigure(0, weight=3)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)

        self.entries = []

        for curr_goal in self.goals:
            self.create_entry(curr_goal)


    def create_goal(self, new_goal: str) -> bool:
        # based on a given string, create a goal for it
        for curr_goal in self.goals:
            if curr_goal.value == new_goal:
                return False
            
        goal = Goal(new_goal)
        self.goals.append(goal)
        self.create_entry(goal)
        return True

    def create_entry(self, goal: Goal):
        # based on a given goal, create an entry for it
        goal_components = GoalEntry(self, goal)

        if goal.complete:
            goal_components.checkbox.select()
            
        def complete_goal():
            if goal.complete:
                goal.complete = False
            else:
                goal.complete = True
            
        def delete_goal():
            self.goals.remove(goal)
            self.entries.remove(goal_components.components)
            for component in goal_components.components:
                component.destroy()

        goal_components.add_command(complete_goal, delete_goal)
        goal_components.align(len(self.entries))
        self.entries.append(goal_components.components)
