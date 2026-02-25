import json
import os

class Player: 
    def __init__(self, name=None, player_class=None, gender=None, level=1, strength=0, gold=0):
        self.name = name
        self.player_class = player_class
        self.gender = gender
        self.level = level
        self.strength = strength
        self.gold = gold

    def change_level(self, amount):
        if self.level + amount >= 1: 
            self.level += amount

    def change_strength(self, amount):
        if self.strength + amount >= 0:
            self.strength += amount

    def change_gold(self, amount):
        if self.gold + amount >= 0:
            self.gold += amount

save_file = ""
players = []

def init(file_path):
    global save_file
    save_file = file_path

def load_players():
    global players
    players = []
    if os.path.exists(save_file):
        with open(save_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            for p_data in data:
                players.append(Player(**p_data))

def save_players():
    with open(save_file, "w", encoding="utf-8") as f:
        json.dump([p.__dict__ for p in players], f, indent=4)

def add_player(name, player_class, gender):
    if not name or not player_class or not gender:
        return False
    player = Player(name=name, player_class=player_class, gender=gender)
    players.append(player)
    save_players()
    return True

def update_player_stat(index, stat, amount):
    if index < 0 or index >= len(players):
        return

    player = players[index]
    if stat == "level":
        player.change_level(amount)
    elif stat == "strength":
        player.change_strength(amount)
    elif stat == "gold":
        player.change_gold(amount)

    save_players()

def get_players():
    return players
