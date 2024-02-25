import TicTacToe as ttt
from TicTacToe import TicTacToe
import numpy as np
import csv

"""
Author: Avery Moates
Date: 2/23/2024

Temporal Difference

"""

class TemporalDifference:

    __td_set_up = False

    def __init__(self, max_state_space: int, alpha: float, gamma: float, TD_player: int) -> None:
        self.__max_state_space = max_state_space
        self.__state_values = np.ones(self.__max_state_space)
        self.__rewards = np.zeros(self.__max_state_space)
        self.__alpha = alpha
        self.__gamma = gamma

        #Set which player is which
        self.__td_player_ID = TD_player
        if TD_player == 1:
            self.__opponent_player_ID = 2
        elif TD_player == 2:
            self.__opponent_player_ID = 1

        self.set_rewards(filename='temporal_difference/rewards_file.csv')

    def train_td(self, board, board_size: int) -> int:
        current_state_space = self.board_to_state_space(board,board_size)
        temp_game = ttt.TicTacToe(board,self.__td_player_ID,True)

        #Setting up the policy. I want to give every possible move a eqaul chance
        possible_moves = temp_game.get_possible_actions()
        random_move = np.random.choice(possible_moves,1)

        #Agent making the move then updating the current state value based on current state value, next reward, next state value
        temp_game.make_move(random_move,self.__td_player_ID)

        next_state_space = self.board_to_state_space(temp_game.get_board(), board_size)
        

        current_state_value = self.get_state_value(current_state_space)
        next_state_value = self.get_state_value(next_state_space)
        next_reward = self.get_reward(next_state_space)

        self.__state_values[current_state_space] = current_state_value + self.__alpha*(next_reward + self.__gamma*next_state_value - current_state_value)

        # print('Old current state value: {0}\n New current state value: {1}\n Current state space: {2}\n Next state value: {3}\n Next state space: {4}\n Next reward: {5}'.format(current_state_value, self.__state_values[current_state_space],current_state_space,next_state_value,next_state_space,next_reward))

        return random_move

        

    def TD_make_move(self, board, board_size: int) -> int:
        best_move = -1
        best_state_value = -100_000_000

        for i in range(0,board_size):
            #The current idea is to loop through all the possible actions. Find the best state value, then just return that move.
            game = ttt.TicTacToe(board,self.__td_player_ID,True)

            #find the best move based on the next state value then make that move.
            if game.is_empty(i):
                game.make_move(i,self.__td_player_ID)
                next_state_space = self.board_to_state_space(game.get_board(), board_size)
                game.unmake_move(i,self.__td_player_ID)

                value = self.__state_values[next_state_space]

                if value > best_state_value:
                    best_state_value = value
                    best_move = i

                # print('Move {0} has state value: {1}, and reward: {2}, next state space is: {3}'.format(i,value, self.get_reward(next_state_space), next_state_space))

        # print('TD chose move {0}'.format(best_move))
        return best_move

    #----------------------------------------------------------------------------------
    #Helper set up functions
    #----------------------------------------------------------------------------------

    def print_state_values(self):
        for i in range(0,self.__max_state_space):
            print(self.__state_values[i])
        
    def set_rewards(self,filename='filename.csv') -> bool:
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

            with open('temporal_difference/rewards_file.csv', mode = 'w') as reward_file:
                reward_writer = csv.writer(reward_file,delimiter=',')

                for i in range(0,self.__max_state_space):
                    value = str(self.__rewards[i])
                    reward_writer.writerow([value, ""])

            return True

        #Set the rewards from a file
        else:
            with open(filename) as reward_file:
                reward_reader = csv.reader(reward_file, delimiter=',')
                line_count = 0

                for row in reward_reader:
                    self.__rewards[line_count] = float(row[0])
                    line_count = line_count + 1
            
            return True

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

    def load_state_values(self, filename='filename.csv', line_num=50):

        if filename=='filename.csv':
            print('No filename path was given. Please try again')
            return False

        else:
            with open(filename) as state_value_file:
                state_value_reader = csv.reader(state_value_file, delimiter=',')
                line_count = 0
                offset_counter = 0

                for row in state_value_reader:
                    if offset_counter == line_num:
                        self.__state_values[line_count] = float(row[1])
                        line_count = line_count + 1
                        
                    else:
                        # print(offset_counter)
                        offset_counter = offset_counter + 1
                        
            
            return True

    
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
        return self.__state_values
    
    def get_state_value(self, state_space: int) -> float:
        return self.__state_values[state_space]

    def get_all_rewards(self):
        return self.__rewards
    
    def get_reward(self, state_space: int) -> int:
        return self.__rewards[state_space]
    
    def get_alpha(self) -> float:
        return self.__alpha
    
    def get_gamma(self) -> float:
        return self.__gamma

    def get_max_state_space(self) -> int:
        return self.__max_state_space
        