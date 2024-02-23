import TicTacToe as TTT
import numpy as np
import sys

from alphabeta import alphabeta

def main():
    game = TTT.TicTacToe(board=np.array([0,1,2,1,0,0,2,0,1]),currentplayer=2,game_started=True)

    print(game.display_board())
    print(game.get_state_space())
    

if __name__ == '__main__':
    main()