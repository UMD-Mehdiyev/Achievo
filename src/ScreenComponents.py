from Goal import Goal, GoalEntry
import customtkinter as ct
import Utilities


class HelpWindow(ct.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Achievo Info")
        self.wm_resizable(False, False) # disable resizing 

        # get preferred dimensions and window screen dimensions
        window_height, window_width = 300, 400
        x_coordinate, y_coordinate = Utilities.screen_dim(window_height, window_width, self.winfo_screenheight(), self.winfo_screenwidth())
        # set coordinates
        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        self.label = ct.CTkLabel(self, text="<information about app and how to use goes here>")
        self.label.pack(padx=20, pady=100)

class ScrollableGoalEntryFrame(ct.CTkScrollableFrame):
    def __init__(self, master, goals: list[Goal], bar, counter, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.goals = goals
        self.progress_bar = bar
        self.progress_counter = counter

        self.grid_rowconfigure(0, weight=3)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)

        self.entries = []

        for curr_goal in self.goals:
            self.create_entry(curr_goal)
        
        self.update_progress()

    def update_progress(self) -> None:
        if len(self.goals) > 0:
            completed_goals = len([x for x in self.goals if x.complete])
            val = completed_goals / len(self.goals)
            self.progress_bar.set(val)
            self.progress_counter.configure(text=f"{round(val * 100)}% Complete!")
        else:
            self.progress_bar.set(0)
            self.progress_counter.configure(text="0% Complete!")


    def create_goal(self, new_goal: str) -> bool:
        # based on a given string, create a goal for it
        for curr_goal in self.goals:
            if curr_goal.value == new_goal:
                return False
            
        goal = Goal(new_goal)
        self.goals.append(goal)
        self.create_entry(goal)
        self.update_progress()
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
            self.update_progress()

        def delete_goal():
            self.goals.remove(goal)
            self.entries.remove(goal_components.components)
            for component in goal_components.components:
                component.destroy()
            self.update_progress()


        goal_components.add_command(complete_goal, delete_goal)
        goal_components.align(len(self.entries))
        self.entries.append(goal_components.components)
