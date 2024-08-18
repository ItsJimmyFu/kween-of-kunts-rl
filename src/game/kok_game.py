from game.deck import Deck
from game.card import Card
from game.rules import valid_move

class Game:
    def __init__(self, n, joker=True):
        #Initialise the deck
        self.deck = Deck(joker)

        #Shuffle and split into n hands to initialise the players
        self.deck.shuffle()
        self.players = self.deck.splitHands(n)

        #Find the player who plays first
        for idx in range(n):
            if(Card('3',"Clubs") in self.players[idx].cards):
                self.turn = idx
                break

        #Initialise game state variables
        self.prev_move = []
        self.start = True
        self.over = False
        self.current_placement=1

    def next_turn(self):
        turn = self.turn
        next_turn = None
        playing_count = 0
        while(True):
            turn = (turn+1)%len(self.players)
            #Check if player is still playing in the round and has not won
            if(self.players[turn].playing and self.players[turn].placement==0):
                #Set the next turn of a player that is not passing
                if(next_turn == None):
                    next_turn = turn
                playing_count += 1

            #End loop when back to the player who made the previous move
            if(turn == self.turn):
                break

        #Reset the round if there is only one player left
        if(playing_count == 1):
            self.prev_move = []

            #Check if player who has won the round has also finished the game,
            if(self.players[self.turn].placement > 0):
                #Set the next turn to the next player still in the game
                turn = self.turn
                next_turn = None
                player_count = 0
                while(True):
                    turn = (turn+1)%len(self.players)
                    if(self.players[turn].placement==0):
                        if(next_turn == None):
                            next_turn = turn
                        player_count+= 1
                    #If there is no more players end the game
                    if(turn == self.turn):
                        break
                #End the game if only one player left
                if(player_count == 1):
                    self.players[next_turn].placement = self.current_placement
                    self.over = True
                    return

            #Add all players still in the game back to the new round
            for player in self.players:
                if(player.placement == 0):
                    player.playing=True
        
        self.turn = next_turn
        return

    def make_move(self,move):
        #Check if player is passing this turn
        if(type(move)==str and move == 'Pass'):
            self.players[self.turn].playing = False
            return True

        #Check if the player can make the move based on their hand
        if(not move.issubset(self.players[self.turn].cards)):
            return False
    
        #Check the validity of the move based on the previous move
        if(not valid_move(list(self.prev_move),list(move),self.start)):
                return False
        
        #Set start state as false
        if(self.start):
            self.start=False
       
        self.prev_move = move
        self.players[self.turn].cards = self.players[self.turn].cards-move
        
        #Check if the player has won
        if(len(self.players[self.turn].cards)==0):
            self.players[self.turn].placement = self.current_placement
            self.current_placement += 1

        return True
    
    #Display the hand of the current player's turn
    def display_player_hand(self):
        print("Player", self.turn, ":", self.players[self.turn])
        print("Previous Move: ", self.prev_move)
        return self.players[self.turn].cards
    
    #Take the user inputted string of moves and convert into a list of cards
    #Format of Rank Suit
    #Or Pass
    def parse_move(self,move):
        cards = set()
        words = move.split()

        #Check if Passing
        if(words[0] == 'Pass'):
            return 'Pass'
        
        for idx in range(0,len(words)-1,2):
            rank = words[idx]
            suit = words[idx+1]
            card = Card(rank,suit)
            #Check if valid card in the deck
            if(card not in self.deck.cards):
                return {}
            
            cards.add(card)
        return cards
