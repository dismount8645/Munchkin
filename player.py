from deck import Deck
# ============================
# PLAYER CLASS
# ============================
class Player:
    """
    Represents a player in the game, tracking their identity, class, level, 
    and accumulated strength bonuses.
    """
    def __init__(self, name, gender, player_class, level, gold, gear):
        self.name = name
        self.level = level
        self.gender = gender
        self.player_class = player_class
        self.gold = gold
        self.gear = gear