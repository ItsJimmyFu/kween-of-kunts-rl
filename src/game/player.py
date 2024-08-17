class Player:

    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        cards = ', '.join(("(" + str(card)+")") for card in self.cards)
        return cards