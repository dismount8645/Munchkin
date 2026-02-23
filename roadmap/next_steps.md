# Next Steps

Based on the implemented features, here are the most immediate priorities for the next development sprint. Our goal is to bridge the gap between our current foundation and the full game logic defined in `master.md`.

## Immediate Priorities

### 1. Card Deck & Hand Management
This is the foundational component needed to handle game progression.
- Create `Deck` mechanisms for both Door and Treasure cards.
- Implement card shuffling and drawing functions.
- Update the `Player` class to include a `hand` list.
- Enforce the hand size limit of 5.

### 2. Phase 1: Kick Open the Door
The beginning of every player's turn involves interacting with the Door deck.
- Force players to draw a Door card at the start of their turn.
- Ensure curses execute directly upon drawing.
- **Run Away Mechanic:** Introduce a dice roll (1-6) generator for fleeing from battles that cannot be won, accounting for escape modifiers.

### 3. Equipment & Inventory Slots (Phase 3 Prep)
Right now, `Combat Strength` is a static property. It must become dynamic.
- Allow players to "equip" items from their hand to their active slots (Headgear, Armor, Footgear, 1 Hand, 2 Hands).
- Automatically recalculate the player's total combat strength whenever an item is equipped or removed.
- Enforce the "1 Big Item" limit rule on the equipped gear.

### 4. Turn Processing & Charity (Phases 2 & 4)
- **Phase 2 (The Empty Room):** If a monster was not fought, allow the user to either "Look for Trouble" (play a monster from hand) or "Loot the Room" (draw a standard Door card face down).
- **Phase 4 (Charity):** Build out the mechanism that ends a turn. Demand that any player with more than 5 cards either gifts them to the lowest-level player or discards them.

## Future Ambitions
- Resolving the Level 10 win condition reliably.
- Introducing cooperative combat ("Help") against tough monsters.
- Expanding on Monster Enhancers and Class-specific rules (like the Mechanic's "Cog" counting).
