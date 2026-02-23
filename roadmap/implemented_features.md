# Current State vs. Game Plan

This document compares the current implemented capabilities of the Munchkin game engine to the logic blueprint defined in `master.md`.

## 1. The Variable Registry

| Variable Name | Status | Notes |
| :--- | :--- | :--- |
| **Level** | 🟩 Implemented | Tracked in `Player` class and displayed on scoreboard. |
| **Combat Strength** | 🟨 Partial | Tracked as `Level + Strength`, but dynamic item calculation is missing. |
| **Monster Level** | 🟩 Implemented | Defined in `card_index` and fetched in `combat_system`. |
| **Monster Enhancers** | 🟥 Missing | No card support or combat interaction for enhancers yet. |
| **Cogs** | 🟥 Missing | Not tracked or evaluated for Mechanic class. |
| **Hand Size** | 🟥 Missing | Players do not have an inventory or hand implemented. |
| **Gold Value** | 🟨 Partial | Items have value defined in cards, but selling mechanic is missing. |
| **Equipment Slots** | 🟨 Partial | Card index has slots defined, but equipping logic does not exist in `Player`. |
| **Big Item Count** | 🟥 Missing | Not tracked. |
| **Die Roll** | 🟥 Missing | Not implemented. |
| **Escape Bonus** | 🟥 Missing | Not calculated or verified. |
| **Victory Levels** | 🟥 Missing | Leveling up post-combat is not automated. |
| **Treasure Count** | 🟥 Missing | Drawing treasures post-combat is missing. |
| **Life Status** | 🟥 Missing | Players cannot die or lose gear. |

---

## 2. The Game Logic Tree

### **[START OF TURN]**
- **PHASE 1: Kick Open the Door**
  - **Status:** 🟨 Partial
  - You can manually initiate a fight using `GameSession.fight_monster`. The combat system calculates `Combat Strength` vs `Monster Level`. However, drawing cards (`Door` deck), facing curses, helper dynamics, and "Run Away/Die Roll" functions are entirely missing.
- **PHASE 2: The Empty Room**
  - **Status:** 🟥 Missing
  - No options implemented for "Look for trouble" or "Loot the room". There is no card drawing logic.
- **PHASE 3: Management (Anytime)**
  - **Status:** 🟥 Missing
  - You cannot sell items for levels, drop large items, or formally equip items to body slots from a hand state.
- **PHASE 4: Charity (End of Turn)**
  - **Status:** 🟥 Missing
  - Card counts are not tracked, meaning charity redistribution has not been added.

---

## 3. The Final Check
- **Status:** 🟥 Missing
- There is no automated win-condition checking logic for Level 10 (nor if the last level must come from a monster kill).

## Summary
The current architecture establishes a sturdy foundation for character records (Name, Gender, Class), a comprehensive dictionary of available cards, and basic math for 1-v-1 monster combat. The next crucial step is developing hand/inventory management, turns, and phase transitions.
