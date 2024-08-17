class Card:
    
    #Declare a new Card with rank and suit value
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} : {self.suit}"

