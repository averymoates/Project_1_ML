import TicTacToe
import numpy as np

"""
Author: Avery Moates
Date: 2/23/2024

Temporal Difference

"""

class TemporalDifference:

    __td_set_up = False

    def __init__(self, max_state_space: int, alpha: float, gamma: float, TD_player: int) -> None:
        self.__max_state_space = max_state_space
        self.__state_values = np.zeros(self.__max_state_space)
        self.__rewards = np.zeros(self.__max_state_space)
        self.__alpha = alpha
        self.__gamma = gamma

        #Set which player is which
        self.__td_player_ID = TD_player
        if TD_player == 1:
            self.__opponent_player_ID = 2
        elif TD_player == 2:
            self.__opponent_player_ID = 1

        self.cal_rewards()

        #I may need to read inital values from a file to set the inital values for the rewards. I do not know though

    def TD_make_move(self, board, board_size: int) -> int:

        for i in range(0,board_size):
            #The current idea is to loop through all the possible actions. Find the best state value, then just return that move.
            pass

    #----------------------------------------------------------------------------------
    #Helper set up functions
    #----------------------------------------------------------------------------------
        
    def cal_rewards(self,filename='filename.csv') -> bool:
        #Calculate the rewards iteratively
        if filename == 'filename.csv':
            for i in range(0,self.__max_state_space):
                board = self.state_space_to_board(i,9)
                game = TicTacToe.TicTacToe(board)

                winner = game.check_board()

                if winner == self.__td_player_ID:
                    self.set_reward(i,10)
                elif winner == self.__opponent_player_ID:
                    self.set_reward(i,-10)
                else:
                    self.set_reward(i,-1)

            #I probably should save the rewards to a file so that I do not have to keep doing this
            return True

        else:
            print('Function not implemented')
            return False


    #Function to set the individual rewards for each state
    def set_reward(self,state_space,reward) -> bool:
        if state_space > self.__max_state_space:
            print('State value is too big')
            return False
        
        self.__rewards[state_space] = reward
        return True
    
    #Convert a Tic Tac Toe board to its state space
    def board_to_state_space(self, board, board_size: int) -> int:
        
        state_value = 0

        for i in range(0,board_size):
            if board[i] == 0:
                state_value = (0b1 << i) | state_value

            elif board[i] == 2:
                state_value = (0b1 << i + 9) | state_value

        return state_value

    #Convert a state space into its Tic Tac Toe board
    def state_space_to_board(self, state_space, board_size: int):
        board = np.zeros(board_size)
        for i in range(0, board_size):
            if (state_space >> i & 0b1) == 1:
                board[i] = 0

            else:
                if (state_space >> i+board_size & 0b1) == 1:
                    board[i] = 2
                else:
                    board[i] = 1

        return board
    
    def evaluate_game(self, TTTgame: TicTacToe, TD_player: int, opponent_player: int) -> int:
        """Function to calculate the score of the board. 0 if the board has no winner, a 1 for max player winning and additional 1 for each empty space, and a -1 for min player winning and additional -1 for each empty space

        Args:
            TTTgame (TicTacToe): _description_
            maxPlayer (int): _description_
            minPlayer (int): _description_

        Returns:
            int: _description_
        """
        winner = TTTgame.check_board()

        if winner == TD_player:
            score = 1
            for i in range(0,9):
                if TTTgame.is_empty(i):
                    score = score + 1

            return score
            
        elif winner == opponent_player:
            score = -1
            for i in range(0,9):
                if TTTgame.is_empty(i):
                    score = score - 1
            
            return score
        
        else:
            return 0


    #----------------------------------------------------------------------------------
    #Debug functions
    #----------------------------------------------------------------------------------
    def get_state_values(self):
        return self.__states
    
    def get_all_rewards(self):
        return self.__rewards
    
    def get_reward(self, state_space: int) -> int:
        return self.__rewards[state_space]
    
    def get_alpha(self) -> float:
        return self.__alpha
    
    def get_gamma(self) -> float:
        return self.__gamma
        