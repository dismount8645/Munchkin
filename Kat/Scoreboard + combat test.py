# ============================
# PLAYER CLASS
# ============================
class Player:
    def __init__(self, name, gender, player_class):
        self.name = name
        self.level = 1
        self.cp = 0
        self.gender = gender
        self.player_class = player_class

    def combat_strength(self):
        return self.level + self.cp


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


# ============================
# CARD INDEX
# ============================

class_cards = {
    "Explorer": {
        "abilities": [
            "Nose for loot",
            "Resourcefulness"
        ]
    },
    "Officer": {
        "abilities": [
            "Voice of Command",
            "Tactical skill"
        ]
    },
    "Mechanic": {
        "abilities": [
            "High Gear",
            "Nuts! I'm Bolting!"
        ]
    },
    "Tycoon": {
        "abilities": [
            "Robber Baron",
            "Them What Has, Gets"
        ]
    }
}

monster_cards = {
    "Babbage Cabbage": {
        "level": 1,
        "special_rules": "Only your Level counts",
        "bad_stuff": "Help next player with no reward"
    },
    "Ada Loveless": {
        "level": 4,
        "special_rules": "+4 against males",
        "bad_stuff": "Cannot help anyone until you win a combat"
    },
    "Robot Queen Victoria": {
        "level": 20,
        "special_rules": "+4 against officers",
        "bad_stuff": "Lose a level and your Class(es)"
    }
}

item_cards = {
    "Martini-Henry Rifle": {
        "slot": "2 Hands",
        "bonus": 5,
        "usable_by": "Tycoon only",
        "value": 700
    },
    "Vacuum Pressure Pulsator": {
        "slot": "1 Hand",
        "bonus": 2,
        "usable_by": "Not usable by Tycoon",
        "value": 100
    },
    "Pith Helmet": {
        "slot": "Headgear",
        "bonus": 3,
        "usable_by": "Explorer only",
        "value": 400
    },
    "Brass Hat": {
        "slot": "Headgear",
        "bonus": 4,
        "usable_by": "Officer only",
        "value": 600
    },
    "Whalebone Corset": {
        "slot": "Armor",
        "bonus": 3,
        "usable_by": "Females only",
        "value": 500
    },
    "Pea Coat": {
        "slot": "Armor",
        "bonus": 2,
        "usable_by": "Anyone",
        "value": 400
    },
    "Electrospats": {
        "slot": "Footgear",
        "bonus": 1,
        "usable_by": "Anyone",
        "value": 300
    },
    "Spring Heels": {
        "slot": "Footgear",
        "bonus": 1,
        "usable_by": "Anyone",
        "value": 300
    },
    "Mustache": {
        "slot": "Other",
        "bonus": 2,
        "usable_by": "Males only",
        "value": 0
    }
}

other_cards = {
    "Curse – Stripped Gear": {
        "type": "Curse",
        "effect": "Lose your armor"
    },
    "Rage Against the Machine": {
        "type": "Treasure",
        "effect": "Go up a level"
    }
}

card_index = {
    "classes": class_cards,
    "monsters": monster_cards,
    "items": item_cards,
    "other": other_cards
}


# ============================
# COMBAT SYSTEM
# ============================
def combat(player, monster_name, card_index):
    monster = card_index["monsters"][monster_name]
    monster_level = monster["level"]

    # --- SPECIAL RULES ---
    if monster_name == "Ada Loveless" and player.gender.lower() == "male":
        monster_level += 4

    if monster_name == "Robot Queen Victoria" and player.player_class.lower() == "officer":
        monster_level += 4

    player_strength = player.combat_strength()

    print(f"\nCombat: {player.name} VS {monster_name}")
    print(f"Player strength: {player_strength}")
    print(f"Monster strength: {monster_level}")

    if player_strength >= monster_level:
        print("You win the combat!")
        return True
    else:
        print("You lose the combat!")
        return False


# ============================
# SCOREBOARD
# ============================
def display_scoreboard(session):
    if not session.startgame:
        print("Game has not started yet.")
        return

    print("\n=== MUNCHKIN SCOREBOARD ===")
    print(f"{'Name':<12}{'Lvl':<5}{'CP':<5}{'Gender':<10}{'Class':<10}")
    print("-" * 60)

    for p in session.players:
        print(f"{p.name:<12}{p.level:<5}{p.cp:<5}{p.gender:<10}{p.player_class:<10}")


# ============================
# SELECTION MENUS
# ============================
def choose_gender():
    options = ["Male", "Female", "Other"]
    print("Choose gender:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    return options[int(input("Enter number: ")) - 1]


def choose_class():
    classes = ["Explorer", "Officer", "Mechanic", "Tycoon"]
    print("Choose class:")
    for i, c in enumerate(classes, start=1):
        print(f"{i}. {c}")
    return classes[int(input("Enter number: ")) - 1]


# ============================
# MAIN PROGRAM
# ============================
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

    # Example combat test:
    print("\nTesting combat with Ada Loveless...")
    session.fight_monster(session.players[0].name, "Ada Loveless", card_index)

else:
    print("Game not started.")
