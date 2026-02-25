class Card: # This is a generic card class that can be used for both door and treasure cards
    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        self.description = description

class DoorCard(Card): # This is a door card class that inherits from the card class
    def __init__(self, name, description):
        super().__init__(name, "Door", description)

class TreasureCard(Card): # This is a treasure card class that inherits from the card class
    def __init__(self, name, description):
        super().__init__(name, "Treasure", description)


class Deck: # This is a generic deck class that can be used for both door and treasure cards
    def __init__(self, cards):
        self.cards = cards
        self.shuffle()

    def shuffle(self): # This will shuffle the deck
        random.shuffle(self.cards)

    def draw_card(self): # This will draw a card from the deck
        return self.cards.pop()

    def discard_card(self, card): # This will discard a card from the deck
        self.cards.append(card)

    def __len__(self): # This will return the number of cards in the deck
        return len(self.cards)

    def __str__(self): # This will return the number of cards in the deck
        return f"Deck({len(self.cards)} cards)"
