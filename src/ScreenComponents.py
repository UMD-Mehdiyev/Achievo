from Task import Task, TaskEntry
from Goal import GoalEntry
import customtkinter as ct
import Utilities


class TaskWindow(ct.CTkToplevel):
    def __init__(self, master, goal: GoalEntry, **kwargs):
        super().__init__(master, **kwargs)

        self.title(goal)
        self.wm_resizable(False, False) # disable resizing 
        # get preferred dimensions and window screen dimensions
        window_height, window_width = 600, 500
        x_coordinate, y_coordinate = Utilities.screen_dim(window_height, window_width, self.winfo_screenheight(), self.winfo_screenwidth())
        # set coordinates
        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        # define a new command for the delete button
        def delete_goal():
            self.destroy()
            # TODO - after bundling the componenets with a proper class strucutre, delete the goal itself here
            
        # create the window's components
        self.label = ct.CTkLabel(self, text=goal.value, font=(100, 0))
        self.progress_bar = ct.CTkProgressBar(self, orientation="horizontal")
        self.scrollable_task_entry_frame = ScrollableTaskEntryFrame(self, goal)
        self.textbox = ct.CTkTextbox(self, width=300, height=100, corner_radius=15)
        self.textbox.insert("0.0", "Task X")
        self.delete_button = ct.CTkButton(self, width=50, height=10, text="❌ Delete Goal ❌", font=(100, 0), command=delete_goal)
        # pack the components into the window
        self.label.pack(padx=20, pady=(20, 0))
        self.progress_bar.pack(padx=20, pady=5)
        self.scrollable_task_entry_frame.pack(padx=20, pady=5)
        self.textbox.pack(padx=20, pady=5)
        self.delete_button.pack(padx=60, pady=5)

        for _, task in enumerate(goal.tasks):
            self.scrollable_task_entry_frame.create_task(task)
            
        # define an event to check for the user pressing enter
        def new_task(event):
            # add the user's task to the list and clear the input
            self.scrollable_task_entry_frame.create_task(self.textbox.get("0.0", "end"))
            goal.add_task(self.textbox.get("0.0", "end"))
            self.textbox.delete("0.0", "end")
        self.bind('<Return>', new_task)


class ScrollableTaskEntryFrame(ct.CTkScrollableFrame):
    def __init__(self, master, goal: GoalEntry, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.parent_goal = goal
        self.entries = []

    def create_task(self, task):
        if isinstance(task, Task):
            task_components = TaskEntry(self, task.value)
            if task.complete:
                task_components.checkbox.select()
        else:
            task_components = TaskEntry(self, task)

        def complete_task() -> None:
            for _, task in enumerate(self.parent_goal.tasks):
                if task.value == task_components.value:
                    task.complete = task_components.toggle_completion()

        task_components.add_command(complete_task)
        task_components.align(len(self.entries) * 2, 0, 10)
        self.entries.append(task_components.get_components())



class ScrollableGoalEntryFrame(ct.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.current_task_window = None
        self.grid_rowconfigure(1, weight=3)
        self.grid_columnconfigure(3, weight=1)
        self.entries = []

    def create_goal(self, goal: str):
        goal_components = GoalEntry(self, goal)
        def open_task_window():
            if self.current_task_window is None or not self.current_task_window.winfo_exists():
                self.current_task_window = TaskWindow(self, goal_components)  # create window if its None or destroyed
                self.current_task_window.focus()
            else:
                self.current_task_window.focus()  # if window exists focus it
        goal_components.add_command(open_task_window)
        goal_components.align(len(self.entries) * 2, 10, 10)
        self.entries.append(goal_components.get_components())
