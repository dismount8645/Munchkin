# Task 03: Equipment & Inventory Slots

Combat strength should no longer be a static number. It must be derived from the player's Level and equipped gear.

## Slot Management
**Target File:** `game_modules/player.py`

- [ ] Define available slots in `Player.__init__`:
    - `self.slots = {"headgear": None, "armor": None, "footgear": None, "left_hand": None, "right_hand": None}`
- [ ] Implement `equip_item(card)`:
    - [ ] Check if the slot is occupied.
    - [ ] Enforce "Big Item" limit (Limit 1 unless special ability).
    - [ ] Check if item requires 1 hand vs 2 hands.
- [ ] Implement `unequip_item(slot_name)`.

## Dynamic Strength Calculation
**Target File:** `game_modules/player.py`

- [ ] Create a `get_total_strength()` method:
    - [ ] Base = `self.level`.
    - [ ] For each card in `self.slots`: Add card item bonus.
    - [ ] **Class Mechanic Bonus**: If `self.player_class == "Mechanic"`, count **Cogs** on all equipped items and add 1 per Cog.
    - [ ] Return total.
- [ ] Update `game_modules/combat_system.py` to call `player.get_total_strength()` instead of using a static property.
