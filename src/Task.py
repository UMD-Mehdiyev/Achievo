import customtkinter as ct

class Task():
    def __init__(self, value: str) -> None:
        self.value = value
        self.complete = False
    
class TaskEntry(Task):
    def __init__(self, master, value: str) -> None:
        super().__init__(value)
        self.components = []
        self.checkbox = ct.CTkCheckBox(master, text='', width=1, corner_radius=100)
        self.task_entry = ct.CTkEntry(master, height=10, placeholder_text=value)
        self.components.extend([self.checkbox, self.task_entry])

    def align(self, factor: int, x_paddding: int, y_padding: int) -> None:
        self.checkbox.grid(row=factor, column=0, padx=x_paddding, pady=y_padding, sticky="nsew")
        self.task_entry.grid(row=factor, column=1, padx=x_paddding, pady=y_padding, sticky="nsew")
    
    def toggle_completion(self) -> bool:
        self.complete = not self.complete
        return self.complete

    def add_command(self, cmd=None) -> None:
        self.checkbox.configure(command=cmd)

    def get_components(self) -> list:
        return self.components
