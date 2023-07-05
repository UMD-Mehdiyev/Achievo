from ScreenComponents import *
import customtkinter as ct
import Utilities
import pickle

class App(ct.CTk):
    """ Main class to bundle app components together. """
    def __init__(self):
        super().__init__()

        self.title("Achievo") 
        self.wm_resizable(False, False) # disable resizing
        self.configure(fg_color="#011627") # background color

        # configure the grid of the screen (3 rows and 2 columns)
        self.grid_rowconfigure(0, weight=1) 
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=4) # the 2nd row will have 4x the weight 
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # these will prevent the user from spam opening new windows
        self.help_window = None
        self.data_window = None

        # get preferred dimensions and window screen dimensions
        window_height, window_width = 600, 800
        x_coordinate, y_coordinate = Utilities.center_screen(window_height, window_width, self.winfo_screenheight(), self.winfo_screenwidth())
        # set coordinates
        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        def app_info():
            """ Command for the help button press.

            When the help button is pressed, this command will open its respective window.
            """
            if self.help_window is None or not self.help_window.winfo_exists():
                self.help_window = HelpWindow(self)  
            else:
                self.help_window.focus()  # if window exists just focus on it
        
        def show_data():
            """ Command for the data button press.

            When the data button is pressed, this command will open its respective window.
            """
            if self.data_window is None or not self.data_window.winfo_exists():
                self.data_window = DataWindow(self)  
            else:
                self.data_window.focus()  # if window exists just focus on it

        def new_goal(event):
            """ Command for enter key event.

            When the enter key is pressed, this command will create a new
            goal and an entry for the goal, it'll also clear the textbox. 
            """
            # add the user's goal to the list and clear the input
            self.scrollable_goal_entry_frame.create_goal(self.textbox.get("0.0", "end").strip())
            self.textbox.delete("0.0", "end")

        def on_closing():
            """ Command for window closing event.

            When the application screen is closed, this command will save all the 
            goals into a file. 
            """
            filename = 'saved_goals.pickle'

            # open the file in binary mode
            with open(filename, 'wb') as file:
                # use pickle to dump the list of goals into the file
                pickle.dump(self.scrollable_goal_entry_frame.goals, file)
            
            # close the screen
            self.destroy()


        try:
        
            filename = 'saved_goals.pickle'

            # open the file in binary mode
            with open(filename, 'rb') as file:
                # use pickle to load the list of goals from the file
                goals_data = pickle.load(file)
        except:
            goals_data = [] # if any type of error occurred, just make the list empty

        
        # create progress counter (number value above the progress bar)
        self.progress_counter = ct.CTkLabel(master=self, font=(200, 25))
        self.progress_counter.grid(row=0, column=0, columnspan=2, pady=(20, 0), sticky="nsew")

        # create main progress bar
        self.progress_bar = ct.CTkProgressBar(master=self, width=600)
        self.progress_bar.grid(row=1, column=0, columnspan=2, pady=(20, 0))

        # create text input
        self.textbox = ct.CTkTextbox(master=self, width=300, height=100, corner_radius=15)
        self.textbox.configure(fg_color="#010E1A")
        self.textbox.grid(row=2, column=0)
        self.textbox.insert("0.0", "Write Goal Here...")
        self.textbox.bind('<Return>', new_goal) # add the command to the text box

        # create a help button 
        self.help_button = ct.CTkButton(master=self, text="❓", width=20, height=20, font=(20, 20), command=app_info)
        self.help_button.grid(row=3, column=0, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="sw")
        self.help_button.configure(fg_color='transparent')

        # create a button for a future data update
        self.data_button = ct.CTkButton(master=self, text="📊", width=20, height=20, font=(20, 20), command=show_data)
        self.data_button.grid(row=3, column=0, columnspan=2,padx=(10, 10), pady=(10, 10), sticky="se")
        self.data_button.configure(fg_color='transparent')

        # create scrollable frame
        self.scrollable_goal_entry_frame = ScrollableGoalEntryFrame(master=self, goals=goals_data, width=300, height=400, bar=self.progress_bar, counter=self.progress_counter)
        self.scrollable_goal_entry_frame.configure(fg_color="#010E1A")
        self.scrollable_goal_entry_frame.grid(row=2, column=1, pady=30)

        # add the on_closing command to be called in the event of the window closing
        self.wm_protocol("WM_DELETE_WINDOW", on_closing)
