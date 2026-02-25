# Task 02: Phase 1 - Kick Open the Door

This is the start of every turn. A player encounters a card face-up from the Door deck.

## Phase Logic
**Target File:** `game_modules/game_session.py`

- [ ] Implement `start_turn(player)` function.
- [ ] Logic for **Drawing Face-Up**:
    - [ ] Call `door_deck.draw_card()`.
    - [ ] Print/Show the card name and type to the player.
- [ ] Logic for **Curse Cards**:
    - [ ] `IF card.type == "Curse"`: Execute its effect immediately. (e.g., Level -1, Discard 1 item).
    - [ ] Move card to discard pile.
- [ ] Logic for **Monster Cards**:
    - [ ] `IF card.type == "Monster"`: Trigger `combat_system.start_combat(player, monster)`.

## The Run Away Mechanic
**Target File:** `game_modules/game_session.py` or new `game_modules/utils.py`

- [ ] Implement `roll_die()` function using `random.randint(1, 6)`.
- [ ] In combat failure logic:
    - [ ] Roll die.
    - [ ] Add `player.escape_bonus`.
    - [ ] `IF roll + bonus < 5`: Apply **Bad Stuff** (from monster card data).
    - [ ] `ELSE`: Successfully escaped!
