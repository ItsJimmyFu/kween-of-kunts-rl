import sys
from game.deck import Deck


def main():

    deck = Deck()
    print(deck)

if __name__ == "__main__":
    sys.path.append('..')
    main()