# ============================
# PLAYER CLASS
# ============================
class Player:
    def __init__(self, name, gender, player_class):
        self.name = name
        self.level = 1
        self.strength = 0
        self.gender = gender
        self.player_class = player_class

    def combat_strength(self):
        return self.level + self.strength