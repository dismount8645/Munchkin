from game_modules.combat_system import combat
from game_modules.deck import Deck
from game_modules.card_index import card_index    

# Initialization of game objects

door_deck = Deck(card_index.door_cards)
treasure_deck = Deck(card_index.treasure_cards)


# ============================
# GAME SESSION
# ============================
class GameSession:
    """
    Manages the overall game state, including the list of players and whether 
    the game sequence has started.
    """
    def __init__(self):
        self.players = []
        self.startgame = False

    def add_player(self, player):
        """Adds a newly created Player instance to the session."""
        self.players.append(player)

    def start_game(self):
        """Flags the game session as active/started."""
        self.startgame = True

    def fight_monster(self, player_name, monster_name, card_index):
        """
        Helper method to initiate a combat by finding the correct player object 
        by name and calling the combat system.
        """
        player = next(p for p in self.players if p.name == player_name)
        return combat(player, monster_name, card_index)
