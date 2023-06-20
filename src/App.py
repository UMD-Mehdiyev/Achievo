import customtkinter as ct
from random import uniform


class TaskWindow(ct.CTkToplevel):
    def __init__(self, master, goal: str, progress = float, **kwargs):
        super().__init__(master, **kwargs)
        self.title(goal)

        self.wm_resizable(False, False) # disable resizing 

        # get preferred dimensions and window screen dimensions 
        window_height = 600
        window_width = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # calculate center of screen
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        # set coordinates
        self.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

        # create label for goal
        self.label = ct.CTkLabel(self, text=goal, font=(100, 0))
        self.label.pack(padx=20, pady=(20, 0))
        
        # create goal's progress bar
        self.progress_bar = ct.CTkProgressBar(self, orientation="horizontal")
        self.progress_bar.set(progress)
        self.progress_bar.pack(padx=20, pady=5)

        # create scrollable frame for list of tasks
        self.scrollable_task_entry_frame = ScrollableTaskEntryFrame(master=self, width=300, height=300)
        self.scrollable_task_entry_frame.pack(padx=20, pady=5)

        # create text input
        self.textbox = ct.CTkTextbox(master=self, width=300, height=100, corner_radius=15)
        self.textbox.pack(padx=20, pady=5)
        self.textbox.insert("0.0", "Task X")
    

        # define an event to check for the user pressing enter
        def new_task(event):
            # add the user's task to the list and clear the input
            self.scrollable_task_entry_frame.add_task(self.textbox.get("0.0", "end"))
            self.textbox.delete("0.0", "end")
        self.bind('<Return>', new_task)



class ScrollableTaskEntryFrame(ct.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.task_list = []
    
    def add_task(self, task: str):
        """Each entry consists of a checkbox and an entry label. The checkbox is there for 
        once the user has completed the task, and the entry label is there in case the 
        user wants to adjust their task."""
        checkbox = ct.CTkCheckBox(self, text='', width=1, corner_radius=100)
        task_entry = ct.CTkEntry(self, height=10, placeholder_text=task)
        checkbox.grid(row=len(self.task_list) * 2, column=0, pady=20, padx=10, sticky="nsew")
        task_entry.grid(row=len(self.task_list) * 2, column=1, pady=20, padx=10, sticky="nsew")
        self.task_list.extend([checkbox, task_entry])
    

class ScrollableGoalEntryFrame(ct.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.goal_list = []

        self.current_task_window = None

        self.grid_rowconfigure(1, weight=3)
        self.grid_columnconfigure(3, weight=1)

    def add_goal(self, goal: str):
        """
        Each entry consists of a checkbox, an entry label, an open button and a progress
        bar beneath the first 3 widgets. The checkbox is there for once the user has 
        completed the goal, the entry label is there in case the user wants to adjust
        their goal, and the open button is there to open a new interface where the user
        can set tasks to build up to the goal, and finally the progress bar is there to
        show how close the user is to finishing the goal, based on completion of tasks. 
        """
        progress = uniform(0, 1)

        def open_task_window():
            if self.current_task_window is None or not self.current_task_window.winfo_exists():
                self.current_task_window = TaskWindow(self, goal, progress)  # create window if its None or destroyed
            else:
                self.current_task_window.focus()  # if window exists focus it

        checkbox = ct.CTkCheckBox(self, text='', width=1, corner_radius=100)
        goal_entry = ct.CTkEntry(self, height=10, placeholder_text=goal)
        open_button = ct.CTkButton(self, width=50, height=10, text="📖", font=(100, 0), command=open_task_window)
        progress_bar = ct.CTkProgressBar(self, orientation="horizontal")
        progress_bar.set(progress)

        checkbox.grid(row=len(self.goal_list) * 2, column=0, pady=20, padx=10, sticky="nsew")
        goal_entry.grid(row=len(self.goal_list) * 2, column=1, pady=20, padx=10, sticky="nsew")
        open_button.grid(row=len(self.goal_list) * 2, column=2, pady=20, padx=10, sticky="nsew")
        progress_bar.grid(row=len(self.goal_list) * 2 + 1, column=0, columnspan=3, padx=10, sticky="nsew")

        self.goal_list.extend([checkbox, goal_entry, open_button, progress_bar])

# main class to bundle app components together
class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("Achievo")
        self.wm_resizable(False, False) # disable resizing 

        # get preferred dimensions and window screen dimensions 
        window_height = 600
        window_width = 700
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # calculate center of screen
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        # set coordinates
        self.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

        # create scrollable frame
        self.scrollable_goal_entry_frame = ScrollableGoalEntryFrame(master=self, width=300, height=400)
        self.scrollable_goal_entry_frame.grid(padx=200, pady=20, sticky="nsew")

        # create text input
        self.textbox = ct.CTkTextbox(master=self, width=300, height=100, corner_radius=15)
        self.textbox.grid(padx=200, pady=20, sticky="nsew")
        self.textbox.insert("0.0", "Goal X")

        # define an event to check for the user pressing enter
        def new_goal(event):
            # add the user's goal to the list and clear the input
            self.scrollable_goal_entry_frame.add_goal(self.textbox.get("0.0", "end"))
            self.textbox.delete("0.0", "end")
        self.bind('<Return>', new_goal)
