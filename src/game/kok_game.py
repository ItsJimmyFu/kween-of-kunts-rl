from game.deck import Deck
from game.card import Card

class Game:
    def __init__(self, n, joker=True):
        #Initialise the deck and shuffle into 4 hands
        deck = Deck(joker)
        deck.shuffle()
        self.players = deck.splitHands(n)
        for idx in range(n):
            if(Card(3,"Clubs") in self.players[idx].cards):
                self.turn = idx
                break
        self.prev_move = []