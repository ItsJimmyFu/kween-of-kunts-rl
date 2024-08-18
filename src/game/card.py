import functools

class Card:
    ordering = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
    
    #Declare a new Card with rank and suit value
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"({self.rank} : {self.suit})"
    
    def __repr__(self) -> str:
        return str(self)
    
    def __hash__(self):
        return hash((self.suit, self.rank))

    def __le__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        
        if(self.rank == 'Joker'):
            self_val = '2'
        else:
            self_val = self.rank
        if(other.rank == 'Joker'):
            other_val = '2'
        else:
            other_val = other.rank

        self_idx = self.ordering.index(self_val)
        other_idx = self.ordering.index(other_val)
        return (self_idx<=other_idx)
    
    def __eq__(self, other):
      if isinstance(other, Card):
         return self.rank == other.rank and self.suit == other.suit
      return False
