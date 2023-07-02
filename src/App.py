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

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=4)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.help_window = None

        # get preferred dimensions and window screen dimensions
        window_height, window_width = 600, 800
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

        
        def app_info():
            print("Coming Soon!")
        
        def show_data():
            print("Coming Soon!")

        # create progress counter
        self.progress_counter = ct.CTkLabel(master=self, font=(200, 25))
        self.progress_counter.grid(row=0, column=0, columnspan=2, pady=(20, 0), sticky="nsew")

        # create main progress bar
        self.progress_bar = ct.CTkProgressBar(master=self, width=600)
        self.progress_bar.grid(row=1, column=0, columnspan=2, pady=(20, 0))

        # create text input
        self.textbox = ct.CTkTextbox(master=self, width=300, height=100, corner_radius=15)
        self.textbox.grid(row=2, column=0)
        self.textbox.insert("0.0", "Write Goal Here...")

        # create a help button 
        self.help_button = ct.CTkButton(master=self, text="❓", width=20, height=20, font=(20, 20), command=app_info)
        self.help_button.grid(row=3, column=0, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="sw")

        # create a button for a future data update
        self.data_button = ct.CTkButton(master=self, text="📊", width=20, height=20, font=(20, 20), command=show_data)
        self.data_button.grid(row=3, column=0, columnspan=2,padx=(10, 10), pady=(10, 10), sticky="se")

        # create scrollable frame
        self.scrollable_goal_entry_frame = ScrollableGoalEntryFrame(master=self, goals=goals_data, width=300, height=400, bar=self.progress_bar, counter=self.progress_counter)
        self.scrollable_goal_entry_frame.grid(row=2, column=1, pady=30)

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