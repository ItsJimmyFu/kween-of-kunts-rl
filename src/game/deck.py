from .card import Card
from .player import Player
import random

class Deck:
    RANKS = [value for value in range(1,14)]
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    #Create a new deck of cards
    def __init__(self,joker):
        self.deck = []

        #Add all number and face cards
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.deck.append(Card(rank,suit))
        
        #Add the joker cards
        if(joker):
            self.deck.append(Card("Joker", "Red"))
            self.deck.append(Card("Joker", "Black"))

    #Shuffle the deck
    def shuffle(self):
        random.shuffle(self.deck)

    #Create the players by splitting the deck
    def splitHands(self,players):
        players = []

        for n in range(players):
            players.append(Player([self.deck[idx] for idx in range(n,len(self.deck),players)]))
        return players
    
    def __str__(self):
        cards = ', '.join(("(" + str(card)+")") for card in self.deck)
        return cards