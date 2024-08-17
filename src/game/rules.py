from .card import Card

#Checks if the move of cards is a legal move
def valid_move(prev_move,new_move):
    #Check if it is the first game move
    if(len(prev_move)==0):
        print(2)
    else:
        print(3)

    return True

#Check if previous move is the trump card
def is_prev_move_trump_card(prev_move):
    if(len(prev_move) == 1 and prev_move[0].suit == 'Spades' and prev_move[0].rank==12):
        return True
    else:
        return False

#Check if new move is the trump card
def is_new_move_trump_card(new_move):
    if(len(new_move) == 1 and new_move[0].suit == 'Spades' and new_move[0].rank==12):
        return True
    else:
        return False

#Check if the move contains the 3 of Clubs card
def is_valid_first_move(new_move):
    for card in new_move:
        if(card.rank==3 and card.suit=='Clubs'):
            return True
    return False

#Check if the new move contains cards of the same rank or joker cards
def is_same_rank(new_move):
    number = None
    for card in new_move:
        if(card.rank == "Joker"):
            continue
        elif(number == None):
            number = card.rank
        elif(number != card.rank):
            return False
    return True

#Check that the new move contains the same number of cards as the previous move
def check_duplicates(prev_move,new_move):
    if(len(prev_move) == len(new_move)):
        return True
    else:
        return False
    
#Check that the new move is a higher value than the previous move
def is_increasing_rank(prev_move,new_move):
    prev_rank = None
    new_rank = None

    #Find the rank of the previous move
    for card in prev_move:
        if(card.rank=='Joker'):
            continue
        else:
            prev_rank = card.rank 
            break
    #If previous move is all Joker cards set value as 2
    if(prev_rank == None):
        prev_rank = 2

    #Find the rank of the next move
    for card in new_move:
        if(card.rank=='Joker'):
            continue
        else:
            new_rank = card.rank 
            break
    #If new move is all Joker cards set value as 2
    if(new_rank == None):
        new_rank = 2
    
    #Check that the previous rank is less than the greater rank
    card_ordering = [3,4,5,6,7,8,9,10,11,12,13]
    prev_idx = card_ordering.index(prev_rank)
    new_idx = card_ordering.index(new_rank)
    
    if(new_idx >= prev_idx):
        return True
    else:
        return False