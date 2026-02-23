# ============================
# SCOREBOARD
# ============================
def display_scoreboard(session):
    """
    Prints a formatted, tabular scoreboard displaying all players and their current stats
    (Level, Combat Power, Gender, Class).
    """
    if not session.startgame:
        print("Game has not started yet.")
        return

    print("\n=== MUNCHKIN SCOREBOARD ===")
    print(f"{'Name':<12}{'Lvl':<5}{'CP':<5}{'Gender':<10}{'Class':<10}")
    print("-" * 60)

    for p in session.players:
        print(f"{p.name:<12}{p.level:<5}{p.strength:<5}{p.gender:<10}{p.player_class:<10}")

