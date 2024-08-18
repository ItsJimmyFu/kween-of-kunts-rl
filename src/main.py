import sys
from game.deck import Deck


def main():

    #Initialise the deck and shuffle into 4 hands
    deck = Deck(joker=True)
    deck.shuffle()
    hands = deck.splitHands(4)
    print(hands)
    

if __name__ == "__main__":
    sys.path.append('..')
    main()