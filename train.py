import TicTacToe as TTT
import TemporalDifference as td
import numpy as np
import sys
import csv

from alphabeta import alphabeta

def main():
    game = TTT.TicTacToe(board=np.array([0,1,2,
                                         1,2,0,
                                         2,0,1]),
                         currentplayer=1,
                         game_started=True)

    print(game.display_board())
    print(game.get_state_space())

    TD = td.TemporalDifference(2**18,0.1,0.1,2)

    print(TD.get_reward(game.get_state_space()))
    

if __name__ == '__main__':
    main()