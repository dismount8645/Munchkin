# ============================
# COMBAT SYSTEM
# ============================
def combat(player, monster_name, card_index):
    """
    Handles a combat encounter between a player and a specified monster.
    Retrieves the monster's stats, applies any special rules based on the player's 
    attributes (gender, class), and compares final combat strengths.
    """
    monster = card_index["monsters"][monster_name]
    monster_level = monster["level"]

    # --- SPECIAL RULES ---
    if monster_name == "Ada Loveless" and player.gender.lower() == "male":
        monster_level += 4

    if monster_name == "Robot Queen Victoria" and player.player_class.lower() == "officer":
        monster_level += 4

    # Calculate the player's total combat strength (level + bonuses)
    player_strength = player.combat_strength()

    print(f"\nCombat: {player.name} VS {monster_name}")
    print(f"Player strength: {player_strength}")
    print(f"Monster strength: {monster_level}")

    # Determine the outcome of the combat encounter
    if player_strength >= monster_level:
        print("You win the combat!")
        return True
    else:
        print("You lose the combat!")
        return False