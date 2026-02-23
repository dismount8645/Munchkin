# ============================
# PLAYER CLASS
# ============================
class Player:
    """
    Represents a player in the game, tracking their identity, class, level, 
    and accumulated strength bonuses.
    """
    def __init__(self, name, gender, player_class):
        self.name = name
        self.level = 1
        self.strength = 0
        self.gender = gender
        self.player_class = player_class

    def combat_strength(self):
        """Calculates the total combat strength (Base Level + Extra Strength/Gear)."""
        return self.level + self.strength