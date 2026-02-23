from deck import Deck
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
        self.hand = []

    def combat_strength(self):
        """Calculates the total combat strength (Base Level + Extra Strength/Gear)."""
        return self.level + self.strength

    def draw_card(self, deck): 
        """Draws a card from the deck and adds it to the player's hand."""
        self.hand.append(deck.draw_card()) # Appends the hand list with the drawn card

    def discard_card(self, card): # This will discard a card from the deck
        self.hand.remove(card) # Removes the card from the hand list