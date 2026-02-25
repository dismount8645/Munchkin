# Initialize a new game session to manage players and state
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
else:
    print("Game not started.")

