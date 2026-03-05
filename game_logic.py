# Initialize players list
players = []

class Player: # Defining the player class
    def __init__(self, name=None, player_class=None, gender=None, level=1, gear=0, gold=0): # Declaring the variable values
        self.name = name
        self.player_class = player_class
        self.gender = gender
        self.level = level
        self.gear = gear
        self.gold = gold
        self.strength = self.level + self.gear

    def change_level(self, amount): # Changes the level of the player
        if self.level >= 0 and self.level < 10:
            self.level += amount
        # elif self.level == 10:
            # Check for win

    def update_strength(self):
        self.strength = self.level + self.gear

    def change_gear(self, amount): # Changes the gear of the player
        self.gear += amount

    def change_gold(self, amount): # Changes the gold of the player
        if self.gold + amount >= 0:
            self.gold += amount



def get_players():
    return players


def add_player(name, player_class, gender):
    if not name or not player_class or not gender:
        return False
    player = Player(name=name, player_class=player_class, gender=gender)
    players.append(player)
    return True

def update_player_stat(index, stat, amount):
    if index < 0 or index >= len(players):
        return

    player = players[index]
    if stat == "level":
        player.change_level(amount)
    elif stat == "gear":
        player.change_gear(amount)
    elif stat == "gold":
        player.change_gold(amount)
    player.update_strength()

