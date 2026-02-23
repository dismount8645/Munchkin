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