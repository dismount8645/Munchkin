# Task 04: Turn Processing & Charity (Phases 2 & 4)

Finalizing the turn loop based on whether a fight occurred and enforcing hand size limits.

## Phase 2: The Empty Room
**Target File:** `game_modules/game_session.py`

- [ ] **Condition**: Only runs if NO monster was fought in Phase 1.
- [ ] Offer Choice:
    - [ ] **A: Look for Trouble**: Choose a Monster card from hand to fight. Follow standard combat rules.
    - [ ] **B: Loot the Room**: Draw 1 Door card face-down (added to hand, others don't see it).

## Phase 4: Charity (End of Turn)
**Target File:** `game_modules/game_session.py`

- [ ] **Condition**: `IF len(player.hand) > 5`.
- [ ] Logic:
    - [ ] Find the player(s) with the lowest level.
    - [ ] `IF current_player` is the lowest: They can simply discard extras to the discard pile.
    - [ ] `ELSE`: They must give the extra cards to the lowest-level player(s).
- [ ] Update `Hand Size` variable.

## Turn End
- [ ] Reset any "Until the end of turn" combat bonuses.
- [ ] Move to `next_player()`.
