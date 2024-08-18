class Player:

    def __init__(self,cards):
        self.cards = cards
        self.playing = True
        self.placement = 0

    def __str__(self):
        cards = ', '.join(("(" + str(card)+")") for card in sorted(list(self.cards)))
        return cards