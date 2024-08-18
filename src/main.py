import sys
from game.kok_game import Game
from game.card import Card


def main():
    game = Game(4)
    while(game.over == False):
        game.display_player_hand()
        move = input("Input Move:")
        move = game.parse_move(move)
        
        if(len(move)==0):
            print("Invalid Input")
            continue
        if (not game.make_move(move)):
            print("Invalid Move")
            continue
        else:
            game.next_turn()

    print("Game Over")
    for idx in range(len(game.players)):
        print("Player:", idx ,"-", game.players[idx].placement)

if __name__ == "__main__":
    sys.path.append('..')
    main()