from src.game.deck import Deck


def test_deck_init():
    deck = Deck(joker=True)
    assert(len(deck.deck) == len(set(deck.deck)))
    assert(len(deck.deck) == 54)

    deck = Deck(joker=False)
    assert(len(deck.deck) == len(set(deck.deck)))
    assert(len(deck.deck) == 52)

def test_split_hands():
    deck = Deck(joker=True)

    for n in range(1,len(deck.deck)):
        hands = deck.splitHands(n)
        combined_deck = []
        for hand in hands:
            combined_deck.extend(hand.cards)
        
        assert(len(combined_deck) == len(set(combined_deck)))
        assert(len(combined_deck) == 54)
