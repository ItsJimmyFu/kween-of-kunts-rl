from .card import Card
from .player import Player
import random

class Deck:
    RANKS = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    #Create a new deck of cards
    def __init__(self,joker):
        self.cards = []

        #Add all number and face cards
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.cards.append(Card(rank,suit))
        
        #Add the joker cards
        if(joker):
            self.cards.append(Card("Joker", "Red"))
            self.cards.append(Card("Joker", "Black"))

    #Shuffle the deck
    def shuffle(self):
        random.shuffle(self.cards)

    #Create the players by splitting the deck
    def splitHands(self,players):
        hands = []

        for n in range(players):
            hands.append(Player(set([self.cards[idx] for idx in range(n,len(self.cards),players)])))
        return hands
    
    def __str__(self):
        cards = ', '.join(("(" + str(card)+")") for card in self.cards)
        return cards