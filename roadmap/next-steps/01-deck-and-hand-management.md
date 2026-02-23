# Task 01: Card Deck & Hand Management

The goal is to move from static card lists to a dynamic deck system and allow players to hold cards.

## Part A: The Deck System
**Target File:** `game_modules/deck.py` (New File)

- [x] Define a `Card` base class with properties: `name`, `type` (Door/Treasure), `description`.
- [x] Define `DoorCard(Card)` and `TreasureCard(Card)` subclasses.
- [x] Create a `Deck` class that:
    - [x] Takes a list of card objects.
    - [x] Methods: `shuffle()`, `draw_card()`, `discard_card(card)`.
    - [ ] Handles "Reshuffling" if the deck runs out (moving discard pile back to deck).

## Part B: Player Hand Management
**Target File:** `game_modules/player.py`

- [x] Add a `self.hand = []` attribute to the `Player` class `__init__`.
- [x] Implement a `draw_card(deck)` method in `Player` that appends a card from the deck to the hand.
- [x] Implement a `discard_card(index)` method.
- [ ] (Optional) Add a check for `len(self.hand) > 5` for future Charity phase logic.

## Part C: Integration
**Target File:** `game_modules/game_session.py`

- [ ] Initialize two `Deck` objects at the start: `door_deck` and `treasure_deck`.
- [ ] Populate them with data from `card_index.py`.
