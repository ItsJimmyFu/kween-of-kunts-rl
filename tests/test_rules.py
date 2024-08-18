from src.game.card import Card
from src.game.rules import valid_move

def test_first_moves():
    #Testing first valid move in a game
    assert(valid_move([], [Card(3,'Clubs')], True))
    assert(valid_move([], [Card(3,'Clubs'), Card(3, 'Spades')], True))
    assert(not valid_move([], [Card(3,'Clubs'), Card(2, 'Spades')], True))
    assert(not valid_move([], [Card(4,'Clubs')], True))
    assert(not valid_move([], [Card(3,'Spades')], True))

    #Testing first valid move in a round
    assert(valid_move([],[Card(2,'Clubs'), Card(2,'Spades')]))
    assert(valid_move([],[Card(10,'Diamonds'), Card(10,'Clubs'), Card("Joker","Red")]))
    assert(not valid_move([],[Card(1,'Diamonds'), Card(2,'Diamonds')]))


def test_trump_cards():
    #Previous move trump card
    assert(not valid_move([Card(12,'Spades')],[Card(13,'Spades')]))
    assert(not valid_move([Card(12,'Spades')],[Card('Joker','Red')]))

    #Next move trump card
    assert(valid_move([Card(2,'Diamonds')],[Card(12,'Spades')]))
    assert(valid_move([Card('Joker','Red')],[Card(12,'Spades')]))
    assert(valid_move([Card(2,'Diamonds'),Card(2,'Spades')],[Card(12,'Spades')]))
    assert(valid_move([Card(2,'Diamonds'),Card(2,'Spades')],[Card(12,'Spades')]))

def test_not_same_number_of_cards():
    assert(not valid_move([Card(3,'Diamonds'),Card(3,'Spades')],[Card(3,'Clubs')]))
    assert(not valid_move([Card(11,'Diamonds')],[Card(11,'Spades'), Card(11,'Clubs')]))
    assert(not valid_move([Card('Joker','Red'),Card(3,'Spades')],[Card(3,'Clubs')]))
    assert(not valid_move([Card(11,'Diamonds')],[Card('Joker','Black'), Card(11,'Clubs')]))

def test_not_same_rank():
    assert(not valid_move([Card(8,'Diamonds'),Card(8,'Spades')],[Card(9,'Diamonds'),Card(8,'Spades')]))
    assert(not valid_move([Card(8,'Diamonds'),Card(8,'Spades')],[Card(10,'Diamonds'),Card(11,'Spades')]))
    assert(not valid_move([Card(10,'Diamonds'),Card(10,'Spades'),Card(10,'Clubs')],[Card(11,'Diamonds'),Card(11,'Spades'),Card(12,"Spades")]))

def test_not_increasing_rank():
    assert(not valid_move([Card(4,'Diamonds')],[Card(3,'Spades')]))
    assert(not valid_move([Card(2,'Clubs')],[Card(1,'Hearts')]))
    assert(not valid_move([Card(2,'Clubs'),Card('Joker','Red')],[Card(1,'Hearts'), Card('Joker','Black')]))
    assert(not valid_move([Card(11,'Clubs'),Card(11,'Diamonds'),Card(11,'Hearts')],[Card(6,'Hearts'), Card(6,'Diamonds'), Card(6,'Clubs')]))

def test_valid_moves():
    assert(valid_move([Card(3,'Spades')],[Card(4,'Diamonds')]))
    assert(valid_move([Card(1,'Hearts')],[Card(2,'Clubs')]))
    assert(valid_move([Card(1,'Hearts'), Card('Joker','Black')],[Card(2,'Clubs'),Card('Joker','Red')]))
    assert(valid_move([Card(6,'Hearts'), Card(6,'Diamonds'), Card(6,'Clubs')], [Card(11,'Clubs'),Card(11,'Diamonds'),Card(11,'Hearts')]))
    assert(valid_move([Card(1,'Spades')],[Card('Joker','Red')]))
    assert(valid_move([Card(3,'Diamonds')],[Card(3,'Hearts')]))
    assert(valid_move([Card('Joker','Black')],[Card('Joker','Red')]))
    assert(valid_move([Card(2,'Diamonds'),Card(2,'Spades')],[Card('Joker','Black'),Card('Joker','Red')]))
    assert(valid_move([Card('Joker','Black')],[Card(2,'Diamond')]))

