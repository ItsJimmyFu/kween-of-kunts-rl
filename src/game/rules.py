from .card import Card

#Checks if the move of cards is a legal move
def valid_move(prev_move,new_move,start=False):
    if(len(prev_move)==0):
        if(start):
            #If first move of the game
            if(valid_first_move(new_move) and same_rank(new_move)):
                return True
            else:
                return False
        else:
            #If first move of the round
            if(same_rank(new_move)):
                return True
            else:
                return False
    else:
        if(prev_move_trump_card(prev_move)):
            return False
        elif(new_move_trump_card(new_move)):
            return True
        elif(not same_number_of_cards(prev_move,new_move)):
            return False
        elif(not same_rank(new_move)):
            return False
        elif(not increasing_rank(prev_move,new_move)):
            return False
    return True

#Check if previous move is the trump card
def prev_move_trump_card(prev_move):
    if((len(prev_move) == 1) and (prev_move[0].suit == 'Spades') and (prev_move[0].rank=='Q')):
        return True
    else:
        return False

#Check if new move is the trump card
def new_move_trump_card(new_move):
    if(len(new_move) == 1 and new_move[0].suit == 'Spades' and new_move[0].rank=='Q'):
        return True
    else:
        return False

#Check if the move contains the 3 of Clubs card
def valid_first_move(new_move):
    for card in new_move:
        if(card.rank=='3' and card.suit=='Clubs'):
            return True
    return False

#Check if the new move contains cards of the same rank or joker cards
def same_rank(new_move):
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
def same_number_of_cards(prev_move,new_move):
    if(len(prev_move) == len(new_move)):
        return True
    else:
        return False
    
#Check that the new move is a higher value than the previous move
def increasing_rank(prev_move,new_move):

    #Find the card of the previous move
    for prev_card in prev_move:
        if(prev_card.rank !='Joker'):
            break
    
    #Find the card of the new move
    for new_card in new_move:
        if(new_card.rank !='Joker'):
            break

    #Check if previous move rank is less than new move rank
    if(prev_card <= new_card):
        return True
    else:
        return False
    