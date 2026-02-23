# ============================
# MAIN PROGRAM
# ============================
from game_modules.game_session import GameSession
from game_modules.selection_menus import choose_gender, choose_class
from game_modules.player import Player
from game_modules.scoreboard import display_scoreboard
from game_modules.card_index import card_index

session = GameSession()

start_game = input("Start game? (y/n): ").lower() == "y"

if start_game:
    session.start_game()

    num_players_str = input("How many players? ")
    if num_players_str.isdigit():
        num_players = int(num_players_str)
    else:
        num_players = 0

    for i in range(num_players):
        print(f"\n--- Player {i + 1} setup ---")
        name = input("Enter player name: ")
        gender = choose_gender()
        pclass = choose_class()

        new_player = Player(name, gender, pclass)
        session.add_player(new_player)

    display_scoreboard(session)

    # Example combat test:
    if session.players:
        print("\nTesting combat with Ada Loveless...")
        # Pass the actual card_index dictionary
        session.fight_monster(session.players[0].name, "Ada Loveless", card_index)

else:
    print("Game not started.")

