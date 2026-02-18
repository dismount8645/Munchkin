### ⚙️ Munchkin Steampunk: The Digital Logic Blueprint

Below is the complete logic for the game. All **Variables** are bolded to show how they interact within the "game engine."

---

### **1. The Variable Registry**
| Variable Name | Example Value | Description |
| :--- | :--- | :--- |
| **Level** | `5` | Your rank (1–10). Used to win. |
| **Combat Strength** | `14` | Total battle power (**Level** + Item bonuses + **Cogs**). |
| **Monster Level** | `12` | The power of the enemy you are fighting. |
| **Monster Enhancers**| `+5` | Cards like "Ancient" that buff the monster. |
| **Cogs** | `3` | Gear icons on items. Adds +1 power per icon if you are a Mechanic. |
| **Hand Size** | `4` | Number of cards in your hand (Limit is 5). |
| **Gold Value** | `1200` | The price on cards. 1000 = +1 **Level**. |
| **Equipment Slots** | `Headgear` | Tracks if you are already wearing an item on a body part. |
| **Big Item Count** | `1` | Tracks "Big" items. (Limit is usually 1). |
| **Die Roll** | `4` | Random 1–6 result used to escape. |
| **Escape Bonus** | `+1` | Modifiers from items (like Footgear) to help you run. |
| **Victory Levels** | `1` | How many levels a monster is worth (usually 1, sometimes 2). |
| **Treasure Count** | `2` | How many cards you draw after winning a fight. |
| **Life Status** | `Alive` | Tracks if you have suffered "Death." |

---

### **2. The Game Logic Tree**

**[START OF TURN]**
* **PHASE 1: Kick Open the Door**
    * Draw 1 card face-up.
    * **IF** card is a Curse:
        * Execute penalty. Update **Level**, **Hand Size**, or **Equipment Slots**.
    * **IF** card is a Monster:
        * Calculate **Combat Strength** (**Level** + Item bonuses).
        * **IF Class** == Mechanic: Add **Cogs** to **Combat Strength**.
        * **COMPARE**: **Combat Strength** vs (**Monster Level** + **Monster Enhancers**).
        * **IF Combat Strength** > Monster Power:
            * **Level** += **Victory Levels**.
            * **Hand Size** += **Treasure Count**. (Go to Phase 4).
        * **IF Combat Strength** <= Monster Power:
            * **IF** help is offered: Add helper's **Combat Strength**. Re-calculate.
            * **IF** still losing: Run Away. Roll **Die Roll**.
            * **IF (Die Roll + Escape Bonus)** < 5: 
                * Apply **Bad Stuff**. (If Death, set **Life Status** to Dead).

* **PHASE 2: The Empty Room**
    * **IF** no Monster was faced in Phase 1:
        * **Choice A (Look for Trouble)**: Play a monster from your hand. Follow Phase 1 combat logic.
        * **Choice B (Loot the Room)**: Draw 1 Door card face-down. **Hand Size** +1.

* **PHASE 3: Management (Anytime)**
    * **IF Gold Value** on discarded items >= 1000:
        * **Level** + 1 (Cannot exceed **Level** 9).
    * **IF Big Item Count** > 1:
        * Force discard until **Big Item Count** == 1.
    * **IF Equipment Slots** are open:
        * Move items from hand to table to increase **Combat Strength** and **Cogs**.

* **PHASE 4: Charity (End of Turn)**
    * **IF Hand Size** > 5:
        * **IF** you are the lowest **Level**: Discard extras.
        * **ELSE**: Give extra cards to the player with the lowest **Level**.

---

### **3. The Final Check**
* **IF Level** == 10:
    * **IF** the 10th level came from a Monster Kill: **GAME OVER - YOU WIN.**
    * **ELSE**: Your **Level** stays at 9.