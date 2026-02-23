# ============================
# MAIN PROGRAM
# ============================
from game_modules.game_session import GameSession
from game_modules.selection_menus import choose_gender, choose_class
from game_modules.player import Player
from game_modules.scoreboard import display_scoreboard
from game_modules.card_index import card_index

# Initialize a new game session to manage players and state
session = GameSession()

# Prompt the user to decide whether to start a new game
start_game = input("Start game? (y/n): ").lower() == "y"

if start_game:
    session.start_game()

    # Ask for the number of players participating in this session
    num_players_str = input("How many players? ")
    if num_players_str.isdigit():
        num_players = int(num_players_str)
    else:
        num_players = 0

    # Loop to set up each player's profile (name, gender, class)
    for i in range(num_players):
        print(f"\n--- Player {i + 1} setup ---")
        name = input("Enter player name: ")
        gender = choose_gender()
        pclass = choose_class()

        # Create the Player object and add it to the active session
        new_player = Player(name, gender, pclass)
        session.add_player(new_player)

    # Show the initial scoreboard with all registered players
    display_scoreboard(session)
else:
    print("Game not started.")

