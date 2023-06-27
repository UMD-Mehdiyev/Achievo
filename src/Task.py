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
        self.delete_button = ct.CTkButton(master, width=50, height=10, text="❌", font=(100, 0))
        self.components.extend([self.checkbox, self.task_entry, self.delete_button])

    def align(self, factor: int, x_paddding: int, y_padding: int) -> None:
        self.checkbox.grid(row=factor, column=0, padx=x_paddding, pady=y_padding, sticky="nsew")
        self.task_entry.grid(row=factor, column=1, padx=x_paddding, pady=y_padding, sticky="nsew")
        self.delete_button.grid(row=factor, column=2, padx=x_paddding, pady=y_padding, sticky="nsew")
    
    def toggle_completion(self) -> bool:
        self.complete = not self.complete
        return self.complete

    def add_command(self, check_cmd=None, delete_cmd=None) -> None:
        self.checkbox.configure(command=check_cmd)
        self.delete_button.configure(command=delete_cmd)

    def get_components(self) -> list:
        return self.components
