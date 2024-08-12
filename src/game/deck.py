from .card import Card

class Deck:

    #Create a new deck of cards
    def __init__(self):
        self.deck = []
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        for suit in suits:
            for rank in range(1,14):
                self.deck.append(Card(rank,suit))
        self.deck.append(Card("Joker", "Red"))
        self.deck.append(Card("Joker", "Black"))

    def __str__(self):
        cards = ', '.join(("(" + str(card)+")") for card in self.deck)
        return cards