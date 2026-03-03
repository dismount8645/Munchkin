import tkinter as tk
import game_logic as logic
import UI

# Defining some constants
PLACEHOLDER_TEXT = "Pick one"
AVAILABLE_CLASSES = ["Officer", "Mechanic", "Wizard", "Warrior", "Rogue"]
AVAILABLE_GENDERS = ["Male", "Female"]

def main(): # Main function
    # 1. Initialize the main window
    root = tk.Tk()
    root.title("Munchkin Scoreboard")

    # 2. Setup the user interface
    UI.setup_ui(root, PLACEHOLDER_TEXT, AVAILABLE_CLASSES, AVAILABLE_GENDERS)

    # 3. Start the application
    root.mainloop()

if __name__ == "__main__": # Will only run if this file is run as the main program
    main()
