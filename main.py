import tkinter as tk
import game_logic as logic
import UI

PLACEHOLDER_TEXT = "Vælg en"
AVAILABLE_CLASSES = ["Officer", "Mechanic", "Wizard", "Warrior", "Rogue"]
AVAILABLE_GENDERS = ["Male", "Female"]
SAVE_FILE = "players_save.json"

def main():
    # 1. Initialize data layer and load save file
    logic.init(SAVE_FILE)
    logic.load_players()

    # 2. Initialize the main window
    root = tk.Tk()
    root.title("Munchkin Scoreboard")

    # 3. Setup the user interface
    UI.setup_ui(root, PLACEHOLDER_TEXT, AVAILABLE_CLASSES, AVAILABLE_GENDERS)

    # 4. Start the application
    root.mainloop()

if __name__ == "__main__":
    main()
