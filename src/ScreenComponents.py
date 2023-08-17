from Goal import Goal, GoalEntry
import customtkinter as ctk
import Utilities


class HelpWindow(ctk.CTkToplevel):
    """ Top level window to show information on the application. """
    def __init__(self, *args, **kwargs) -> None:
        """ Create a new help window. """
        super().__init__(*args, **kwargs)

        self.title("Achievo Info")
        self.wm_resizable(False, False) # disable resizing 
        self.configure(fg_color="#011627")

        # get preferred dimensions and window screen dimensions
        window_height, window_width = 300, 400
        x_coordinate, y_coordinate = Utilities.center_screen(window_height, window_width, self.winfo_screenheight(), self.winfo_screenwidth())
        # set coordinates
        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        # create the help message for the user
        self.help_label = ctk.CTkLabel(self, text="Type your goal in the textbox on the left side.\n" +
                                            "Then press enter to get it on the list itself.")
        self.help_label.pack(padx=20, pady=100)


class ScrollableGoalEntryFrame(ctk.CTkScrollableFrame):
    """ Custom scrollable frame that will contain the list of goal entries. """ 
    def __init__(self, master, goals: list[Goal], progress_bar, progress_counter, command=None, **kwargs) -> None:
        """ Create a new scrollable entry frame. 
        
        Arguments:
            master is the root of the main application frame
            goals are a list of existing goals that were previously saved
            bar is the progress bar component  
            counter is a label component that holds the progress percentage 
        """
        super().__init__(master, **kwargs)
        self.command = command
        self.goals = goals
        self.progress_bar = progress_bar
        self.progress_counter = progress_counter

        # configure the grid of the screen (1 row and 2 columns)
        self.grid_rowconfigure(0, weight=1) 
        self.grid_columnconfigure(0, weight=3) # first column has 3x weight
        self.grid_columnconfigure(1, weight=1)

        self.entries = []
        
        # if there are any goals already (that were previously saved), then 
        # load them into the list first and update the progress 
        for curr_goal in self.goals:
            self.create_entry(curr_goal)
        self.update_progress()


        def show_data() -> None:
            """ Command for the data button press.

            When the data button is pressed, this command will open its respective window.
            """
            if self.data_window is None or not self.data_window.winfo_exists():
                self.data_window = DataWindow(self)  
            else:
                self.data_window.focus()  # if window exists just focus on it

    def update_progress(self) -> None:
        """ Update the progress bar and counter.

        This will properly update the progress bar and counter based on the 
        ratio of completed goals against total goals.
        """
        if len(self.goals) > 0:
            completed_goals = sum(1 for goal in self.goals if goal.complete)
            val = completed_goals / len(self.goals)
            self.progress_bar.set(val)
            self.progress_counter.configure(text=f"{round(val * 100)}% Complete!")
        else:
            self.progress_bar.set(0)
            self.progress_counter.configure(text="0% Complete!")


    def create_goal(self, new_goal: str) -> bool:
        """ Create a new goal (no duplicates allowed).
        
        Arguments:
            new_goal is the direct text value that the goal will have

        Returns:
            True if the goal was created and False if it already exists
        """
        # based on a given string, create a goal for it
        for curr_goal in self.goals:
            if curr_goal.value == new_goal:
                return False
            
        goal = Goal(new_goal)
        goal.value = Utilities.validate(goal.value, 25) # clean the goal text at 25 intervals
        self.goals.append(goal)
        self.create_entry(goal)
        self.update_progress()
        return True


    def create_entry(self, goal: Goal) -> None:
        """ Create a new entry within the scrollable frame for the given goal.
        
        Arguments:
            goal is the Goal object that this entry is based on
        """


        def check_goal() -> None:
            """ Command for checking the checkbox.

            When the goal gets checked/unchecked, this command will properly update
            the goal's status and correctly update the progress bar. 
            """
            if goal.complete:
                goal.complete = False
            else:
                goal.complete = True
            self.update_progress()


        def delete_goal() -> None:
            """ Command for the delete goal button press.

            When the goal's delete button is pressed, this command will completely remove the 
            current goal entry and update the progress bar.
            """
            self.goals.remove(goal)
            self.entries.remove(goal_components.components)
            for component in goal_components.components:
                component.destroy()
            self.update_progress()


        # based on a given goal, create an entry for it
        goal_components = GoalEntry(self, goal)

        if goal.complete:
            goal_components.checkbox.select()

        goal_components.add_command(check_goal, delete_goal)
        goal_components.align(len(self.entries)) 
        self.entries.append(goal_components.components)
