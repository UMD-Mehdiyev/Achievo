import customtkinter as ct
from Task import Task

class Goal():
    def __init__(self, value: str) -> None:
        self.value = value
        self.complete = False
        self.progress = 0
        self.tasks = []

    def add_task(self, task: str) -> None:
        new_task = Task(task)
        self.tasks.append(new_task)

    def remove_task(self, task: str) -> None:
        for _, t in enumerate(self.tasks):
            if t.value == task:
                self.tasks.remove(t)
                return


class GoalEntry(Goal):
    def __init__(self, master, value: str) -> list:
        super().__init__(value)
        self.components = []
        self.checkbox = ct.CTkCheckBox(master, text='', width=1, corner_radius=100)
        self.goal_entry = ct.CTkEntry(master, height=10, placeholder_text=value)
        self.open_button = ct.CTkButton(master, width=50, height=10, text="📖", font=(100, 0))
        self.delete_button = ct.CTkButton(master, width=50, height=10, text="❌", font=(100, 0))
        self.progress_bar = ct.CTkProgressBar(master, orientation="horizontal")
        self.progress_bar.set(self.update_progress() if len(self.tasks) != 0 else 0)
        self.components.extend([self.checkbox, self.goal_entry, self.open_button, self.delete_button, self.progress_bar])

    def align(self, factor: int, x_padding: int, y_padding: int) -> None:
        self.checkbox.grid(row=factor, column=0, padx=x_padding, pady=y_padding, sticky="nsew")
        self.goal_entry.grid(row=factor, column=1, padx=x_padding, pady=y_padding, sticky="nsew")
        self.open_button.grid(row=factor, column=2, padx=x_padding, pady=y_padding, sticky="nsew")
        self.delete_button.grid(row=factor, column=3, padx=x_padding, pady=y_padding, sticky="nsew")
        self.progress_bar.grid(row=factor + 1, column=0, columnspan=4, padx=x_padding, sticky="nsew")
    
    def update_progress(self) -> float:
        complete_tasks = len([task for task in self.tasks if task.complete])
        self.progress = (complete_tasks / len(self.tasks)) if len(self.tasks) != 0 else 0
        self.progress_bar.set(self.progress)
        return self.progress

    def add_command(self, open_cmd, delete_cmd) -> None:
        self.open_button.configure(command=open_cmd)
        self.delete_button.configure(command=delete_cmd)

    def get_components(self) -> list:
        return self.components

