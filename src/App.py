import customtkinter
from random import uniform


class ScrollableGoalEntryFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.entry_list = []

        self.grid_rowconfigure(1, weight=3)
        self.grid_columnconfigure(3, weight=1)

    def add_item(self, item):
        checkbox = customtkinter.CTkCheckBox(self, text='', width=1, corner_radius=100)
        label_button = customtkinter.CTkEntry(self, height=10, placeholder_text=item)
        open_button = customtkinter.CTkButton(self, width=50, height=10, text="📖", font=(100, 0))
        progress_bar = customtkinter.CTkProgressBar(self, orientation="horizontal")
        progress_bar.set(uniform(0, 1))

        checkbox.grid(row=len(self.entry_list) * 2, column=0, pady=20, padx=10, sticky="nsew")
        label_button.grid(row=len(self.entry_list) * 2, column=1, pady=20, padx=10, sticky="nsew")
        open_button.grid(row=len(self.entry_list) * 2, column=2, pady=20, padx=10, sticky="nsew")
        progress_bar.grid(row=len(self.entry_list) * 2 + 1, column=0, columnspan=3, padx=10, sticky="nsew")

        self.entry_list.extend([checkbox, label_button, open_button, progress_bar])

# main class to bundle app components together
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # set gui properties
        self.title("Achievo")
        self.geometry("700x600")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # create scrollable frame
        self.scrollable_goal_entry_frame = ScrollableGoalEntryFrame(master=self, width=300, height=500)
        self.scrollable_goal_entry_frame.grid(row=0, column=0)
        [self.scrollable_goal_entry_frame.add_item(f"Goal {i}") for i in range(10)]

