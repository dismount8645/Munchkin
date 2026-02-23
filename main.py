draw_type = ["curse", "monster"]
players = []


class player:
    def __init__(self, name):
        self.name = name
        self.hand_size = 0
        self.level = 0
        self.strength = 0
        self.gender = None
        self.player_class = None

print("Welcome to the Munchkin game assistant!")

player_count = int(input("How many players are playing? "))

for i in range(player_count):
    players.append(player(input(f"Enter name for player {i+1}: ")))
print(f"Players: {[p.name for p in players]}")


    