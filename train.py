import TicTacToe as TTT
import TemporalDifference as td
import numpy as np
import sys
import csv

from alphabeta import alphabeta

def main():
    

    Player_one = alphabeta()
    Player_two = td.TemporalDifference(2**18, 0.1, 0.1, 2)

    counter = 0

    while counter != 500:
        game = TTT.TicTacToe(board=np.array([0,0,0,0,0,0,0,0,0]),current_player=-1,game_started=False)
        game.start_game()
        current_player = game.get_current_player()
        # print('Starting board: \n')
        # game.display_board()

        while(game.get_game_status()):
            if current_player == 1:
                placement = Player_one.alphabeta_make_move(game.get_board(),10,1)
                game.make_move(placement,1)
                current_player = game.get_current_player()

            elif current_player == 2:
                placement = Player_two.TD_make_move(game.get_board(), 9)
                game.make_move(placement,2)
                current_player = game.get_current_player()

            game.check_board()

        print('Winner is: {0}'.format(game.check_board()))
        # game.display_board()
        counter = counter + 1

    # Player_two.print_state_values()
    
    

if __name__ == '__main__':
    main()