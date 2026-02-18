# -----------------------------
# Player Class
# -----------------------------
class Player:
    def __init__(self, name, gender, player_class):
        self.name = name
        self.level = 1
        self.cp = 0
        self.gender = gender
        self.player_class = player_class


# -----------------------------
# Game Session Class
# -----------------------------
class GameSession:
    def __init__(self):
        self.players = []
        self.startgame = False

    def add_player(self, player):
        self.players.append(player)

    def start_game(self):
        self.startgame = True


# -----------------------------
# Selection Menus (Dropdown-like)
# -----------------------------
def choose_gender():
    options = ["Male", "Female", "Other"]
    print("Choose gender:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    choice = int(input("Enter number: "))
    return options[choice - 1]



def choose_class():
    classes = ["Explorer", "Officer", "Mechanic", "Tycoon"]
    print("Choose class:")
    for i, c in enumerate(classes, start=1):
        print(f"{i}. {c}")
    choice = int(input("Enter number: "))
    return classes[choice - 1]


# -----------------------------
# Scoreboard Display
# -----------------------------
def display_scoreboard(session):
    if not session.startgame:
        print("Game has not started yet.")
        return

    print("\n=== MUNCHKIN SCOREBOARD ===")
    print(f"{'Name':<12}{'Lvl':<5}{'CP':<5}{'Gender':<10}{'Class':<10}")
    print("-" * 60)

    for p in session.players:
        print(f"{p.name:<12}{p.level:<5}{p.cp:<5}{p.gender:<10}{p.player_class:<10}")


# -----------------------------
# Main Program Flow
# -----------------------------
session = GameSession()

start_game = input("Start game? (y/n): ").lower() == "y"

if start_game:
    session.start_game()

    num_players = int(input("How many players? "))

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

