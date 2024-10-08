from src.game.deck import Deck
from src.game.card import Card


def test_deck_init():
    deck = Deck(joker=True)
    assert(len(deck.cards) == len(set(deck.cards)))
    assert(len(deck.cards) == 54)

    deck = Deck(joker=False)
    assert(len(deck.cards) == len(set(deck.cards)))
    assert(len(deck.cards) == 52)

def test_card_comparison():
    assert(Card('3','Diamond') == Card('3','Diamond'))
    assert(not Card('3','Diamond') == Card('3','Spades'))
    assert(Card('3','Diamond') <= Card('5','Spades'))
    assert(not (Card('5','Diamond') <= Card('3','Spades')))

def test_split_hands():
    deck = Deck(joker=True)

    for n in range(1,len(deck.cards)):
        hands = deck.splitHands(n)
        combined_deck = []
        for hand in hands:
            combined_deck.extend(hand.cards)
        
        assert(len(combined_deck) == len(set(combined_deck)))
        assert(len(combined_deck) == 54)
