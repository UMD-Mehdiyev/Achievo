from ScreenComponents import *
import customtkinter as ct
import Utilities
import pickle


# main class to bundle app components together
class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("Achievo")
        self.wm_resizable(False, False) # disable resizing 

        # get preferred dimensions and window screen dimensions
        window_height, window_width = 600, 700
        x_coordinate, y_coordinate = Utilities.screen_dim(window_height, window_width, self.winfo_screenheight(), self.winfo_screenwidth())
        # set coordinates
        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        try:
            # get any saved goals
            filename = 'saved_data.pickle'

            # Open the file in binary mode
            with open(filename, 'rb') as file:
                # Use pickle to load the list of goals from the file
                goals_data = pickle.load(file)
                print(goals_data)
        except:
            goals_data = []


        # create scrollable frame
        self.scrollable_goal_entry_frame = ScrollableGoalEntryFrame(master=self, goals=goals_data, width=300, height=300)
        self.scrollable_goal_entry_frame.grid(padx=200, pady=(100, 0))

        # create text input
        self.textbox = ct.CTkTextbox(master=self, width=300, height=100, corner_radius=15)
        self.textbox.grid(padx=200, pady=20, sticky="nsew")
        self.textbox.insert("0.0", "Enter Goal Here")

        # define an event to check for the user pressing enter
        def new_goal(event):
            # add the user's goal to the list and clear the input
            self.scrollable_goal_entry_frame.create_goal(self.textbox.get("0.0", "end").strip())
            self.textbox.delete("0.0", "end")
        self.bind('<Return>', new_goal)


        def on_closing():
  
            # Define the filename/path where you want to save the data
            filename = 'saved_data.pickle'

            # Open the file in binary mode
            with open(filename, 'wb') as file:
                # Use pickle to dump the list of goals into the file
                pickle.dump(self.scrollable_goal_entry_frame.goals, file)
            
            # close the screen
            self.destroy()

        self.wm_protocol("WM_DELETE_WINDOW", on_closing)