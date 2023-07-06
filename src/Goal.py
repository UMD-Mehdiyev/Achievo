import customtkinter as ctk


class Goal():
    """
    Nothing too fancy, a Goal is simply defined as a value that's complete or incomplete.
    Although using dictionary structure would have also worked fine, this was kept as a 
    class to allow for easier scaling in the future, if ever needed. 
    """
    def __init__(self, value: str) -> None:
        """Create a new goal.

        Arguments:
            value is the goal text 
        """
        self.value = value
        self.complete = False 
    

class GoalEntry():
    """
    A GoalEntry is a single row or record that's stored in the list which sits on the 
    right of the screen. This organization point allows for easier maintenence down the 
    line if scaling were to ever happen. This class also comes with functions to align
    the components, and add commands to the components post-creation.
    """
    def __init__(self, master, goal: Goal) -> None:
        """Create a new GoalEntry.
        
        Arguments:
            master is the root frame in which these components should be placed
            goal is the Goal object that this entry is based on

        Returns:
            a list of components that make up the entry
        """
        self.goal = goal
        self.components = []
        
        self.checkbox = ctk.CTkCheckBox(master, text=goal.value, font=(75, 0), corner_radius=100)
        self.delete_button = ctk.CTkButton(master, width=10, text="❌", fg_color='transparent')
        self.components.extend([self.checkbox, self.delete_button])


    def align(self, row_pos: int) -> None:
        """ Align this entry's components relative to the list where they're stored in.
        
        Arguments:
            row_pos is which row position this entry should be at
        """
        self.checkbox.grid(row=row_pos, column=0, padx=5, pady=5, sticky="W")
        self.delete_button.grid(row=row_pos, column=1, padx=5, pady=5, sticky="E")        


    def add_command(self, check_cmd, delete_cmd) -> None:
        """ Add commands to the two components to allow for functionality after they've been created.

        Arguments:
            check_cmd is the command that should be called when the checkbox is checked
            delete_cmd is the command that should be called when the delete button is pressed
        """
        self.checkbox.configure(command=check_cmd)
        self.delete_button.configure(command=delete_cmd)
