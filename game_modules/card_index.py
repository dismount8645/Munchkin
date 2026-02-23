# ============================
# CARD INDEX
# ============================

# Dictionary defining the abilities available for each character class
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

# Dictionary of available monsters, including their base levels and special combat rules
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

# Dictionary defining equippable items, their combat bonuses, slots, restrictions, and gold value
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

# Miscellaneous cards such as curses or one-time use treasures
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

# Master index combining all card categories for easy lookup during gameplay
card_index = {
    "classes": class_cards,
    "monsters": monster_cards,
    "items": item_cards,
    "other": other_cards
}