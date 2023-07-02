import customtkinter as ct

class Goal():
    def __init__(self, value: str) -> None:
        self.value = value
        self.complete = False 

class GoalEntry():
    def __init__(self, master, goal: Goal) -> list:
        self.goal = goal
        self.components = []

        self.validate()
        
        self.checkbox = ct.CTkCheckBox(master, text=goal.value, font=(75, 0), corner_radius=100)
        self.delete_button = ct.CTkButton(master, width=10, text="❌")

        self.components.extend([self.checkbox, self.delete_button])

    def align(self, row) -> None:
        self.checkbox.grid(row=row, column=0, padx=5, pady=5, sticky="W")
        self.delete_button.grid(row=row, column=1, padx=5, pady=5, sticky="E")

    def validate(self):
        temp = ""
        c = 1
        for i in range(len(self.goal.value)):
            temp += self.goal.value[i]
            if c == 25:
                temp += "\n"
                c = 0
            c += 1
        self.goal.value = temp
        

    def add_command(self, check_cmd, delete_cmd) -> None:
        self.checkbox.configure(command=check_cmd)
        self.delete_button.configure(command=delete_cmd)


