
# ============================
# GAME SESSION
# ============================
class GameSession:
    def __init__(self):
        self.players = []
        self.startgame = False

    def add_player(self, player):
        self.players.append(player)

    def start_game(self):
        self.startgame = True

    def fight_monster(self, player_name, monster_name, card_index):
        player = next(p for p in self.players if p.name == player_name)
        return combat(player, monster_name, card_index)
