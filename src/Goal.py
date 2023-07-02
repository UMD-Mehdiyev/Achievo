import customtkinter as ct

class Goal():
    def __init__(self, value: str) -> None:
        self.value = value
        self.complete = False 

class GoalEntry():
    def __init__(self, master, goal: Goal) -> list:
        self.goal = goal
        self.components = []
        self.checkbox = ct.CTkCheckBox(master, text='', width=1, corner_radius=100)
        self.value_entry = ct.CTkEntry(master, height=10, placeholder_text=goal.value)
        self.delete_button = ct.CTkButton(master, width=50, height=10, text="❌", font=(100, 0))
        self.components.extend([self.checkbox, self.value_entry, self.delete_button])

    def align(self, factor: int, x_padding: int, y_padding: int) -> None:
        self.checkbox.grid(row=factor, column=0, padx=x_padding, pady=y_padding, sticky="nsew")
        self.value_entry.grid(row=factor, column=1, padx=x_padding, pady=y_padding, sticky="nsew")
        self.delete_button.grid(row=factor, column=2, padx=x_padding, pady=y_padding, sticky="nsew")

    def add_command(self, command) -> None:
        self.delete_button.configure(command=command)

    def get_components(self) -> list:
        return self.components

