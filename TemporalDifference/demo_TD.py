import TicTacToe.TicTacToe as TTT
import numpy as np
import TemporalDifference.TemporalDifference as td
import sys

from TicTacToe.alphabeta import alphabeta

'''
Note for future:

I need to redo the rewards. I need to set the reward to a -10 if the opponent is about to win. 
Since this is 1 turn TD, it need to be able to see two steps ahead like alpha beta can
'''

def main():
    alpha = 0.01
    gamma = 0.05

    game = TTT.TicTacToe()
    game.set_first_player(1)
    game.start_game()

    Player_two = td.TemporalDifference(2**18, alpha, gamma, 2)
    Player_two.load_state_values(filename='temporal_difference_data_2/gamma_0_05_alpha_0_01/ver_1.csv',line_num=50)
    # Player_two.print_state_values()
    print(Player_two.get_state_value(510))
    game.display_board()

    current_player = game.get_current_player()

    while(game.get_game_status()):
        if current_player == 1:
            print('Player 1, enter your move:')
            placement = int(input())
            game.make_move(placement,1)
            current_player = game.get_current_player()
            game.display_board()

        elif current_player == 2:
            placement = Player_two.TD_make_move(game.get_board(), 9)
            game.make_move(placement,2)
            current_player = game.get_current_player()
            game.display_board()

        game.check_board()

if __name__ == '__main__':
    main()