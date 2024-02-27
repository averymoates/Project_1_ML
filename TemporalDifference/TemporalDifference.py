import TicTacToe.TicTacToe as ttt
from TicTacToe.TicTacToe import TicTacToe
import numpy as np
import csv

"""
Author: Avery Moates
Date: 2/23/2024

Temporal Difference

"""

class TemporalDifference:

    #Private variables
    __max_state_space = 0
    __state_values = None
    __rewards = None
    __actions = None
    __alpha = 0
    __gamma = 0
    __td_player_ID = 0
    __opponent_player_ID = 0

    def __init__(self, max_state_space: int, alpha: float, gamma: float, TD_player: int) -> None:
        self.__max_state_space = max_state_space
        self.__state_values = np.zeros(self.__max_state_space)
        self.__rewards = np.zeros(self.__max_state_space)
        self.__actions = np.zeros([self.__max_state_space, 9],np.float64)
        self.__alpha = alpha
        self.__gamma = gamma

        #Set which player is which
        self.__td_player_ID = TD_player
        if TD_player == 1:
            self.__opponent_player_ID = 2
        elif TD_player == 2:
            self.__opponent_player_ID = 1

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
    def state_space_to_board(self, state_space: int, board_size: int) -> np.ndarray:
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
                        offset_counter = offset_counter + 1
                        
            
            return True
        
    def load_rewards(self,filename='filename.csv') -> bool:
        #Calculate the rewards iteratively
        if filename == 'filename.csv':
            self.set_rewards_iteratively(9)

            with open('TemporalDifference/TD_Load_data/rewards_file.csv', mode = 'w') as reward_file:
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

    def load_policy(self, filename='filename.csv') -> bool:
        if filename=='filename.csv':
            self.set_actions_iteratively()
            
            with open('TemporalDifference/TD_Load_data/policy_file.csv', mode = 'w') as policy_file:
                policy_writer = csv.writer(policy_file,delimiter=',')

                for i in range(0,self.__max_state_space):
                    value = self.__actions[i]
                    value = [str(value[0]), str(value[1]), str(value[2]), str(value[3]), str(value[4]), str(value[5]), str(value[6]), str(value[7]), str(value[8])]
                    policy_writer.writerow(value)
                        

            return True
        
        #Set the policy from a file
        else:
            with open(filename) as policy_file:
                policy_reader = csv.reader(policy_file, delimiter=',')
                line_count = 0

                for row in policy_reader:
                    for i in range(0,9):
                        self.__actions[line_count,i] = float(row[i])
                        
                    line_count = line_count + 1
            
            return True
            

    def set_rewards_iteratively(self, board_size: int):
        for i in range(0, self.__max_state_space):
            board = self.state_space_to_board(i, board_size)
            reward = self.calc_reward_from_board(board)
            self.__rewards[i] = reward
            # self.__state_values[i] = reward

    def calc_reward_from_board(self, board) -> float:
        #If the TD player wins give a reward
        if board[0] == self.__td_player_ID and board[1] == self.__td_player_ID and board[2] == self.__td_player_ID:
            return 1.0
        elif board[3] == self.__td_player_ID and board[4] == self.__td_player_ID and board[5] == self.__td_player_ID:
            return 1.0
        elif board[6] == self.__td_player_ID and board[7] == self.__td_player_ID and board[8] == self.__td_player_ID:
            return 1.0
        elif board[0] == self.__td_player_ID and board[3] == self.__td_player_ID and board[6] == self.__td_player_ID:
            return 1.0
        elif board[1] == self.__td_player_ID and board[4] == self.__td_player_ID and board[7] == self.__td_player_ID:
            return 1.0
        elif board[2] == self.__td_player_ID and board[5] == self.__td_player_ID and board[8] == self.__td_player_ID:
            return 1.0
        elif board[0] == self.__td_player_ID and board[4] == self.__td_player_ID and board[8] == self.__td_player_ID:
            return 1.0
        elif board[2] == self.__td_player_ID and board[4] == self.__td_player_ID and board[6] == self.__td_player_ID:
            return 1.0

        #If the opponent player is about to win, give a bad reward
        if board[0] == self.__opponent_player_ID and board[1] == self.__opponent_player_ID and board[2] == 0:
            return -10.0
        elif board[0] == 0 and board[1] == self.__opponent_player_ID and board[2] == self.__opponent_player_ID:
            return -10.0
        elif board[0] == self.__opponent_player_ID and board[1] == 0 and board[2] == self.__opponent_player_ID:
            return -10.0

        elif board[3] == self.__opponent_player_ID and board[4] == self.__opponent_player_ID and board[5] == 0:
            return -10.0
        elif board[3] == 0 and board[4] == self.__opponent_player_ID and board[5] == self.__opponent_player_ID:
            return -10.0
        elif board[3] == self.__opponent_player_ID and board[4] == 0 and board[5] == self.__opponent_player_ID:
            return -10.0

        elif board[6] == self.__opponent_player_ID and board[7] == self.__opponent_player_ID and board[8] == 0:
            return -10.0
        elif board[6] == 0 and board[7] == self.__opponent_player_ID and board[8] == self.__opponent_player_ID:
            return -10.0
        elif board[6] == self.__opponent_player_ID and board[7] == 0 and board[8] == self.__opponent_player_ID:
            return -10.0

        elif board[0] == self.__opponent_player_ID and board[3] == self.__opponent_player_ID and board[6] == 0:
            return -10.0
        elif board[0] == 0 and board[3] == self.__opponent_player_ID and board[6] == self.__opponent_player_ID:
            return -10.0
        elif board[0] == self.__opponent_player_ID and board[3] == 0 and board[6] == self.__opponent_player_ID:
            return -10.0

        elif board[1] == self.__opponent_player_ID and board[4] == self.__opponent_player_ID and board[7] == 0:
            return -10.0
        elif board[1] == 0 and board[4] == self.__opponent_player_ID and board[7] == self.__opponent_player_ID:
            return -10.0
        elif board[1] == self.__opponent_player_ID and board[4] == 0 and board[7] == self.__opponent_player_ID:
            return -10.0

        elif board[2] == self.__opponent_player_ID and board[5] == self.__opponent_player_ID and board[8] == 0:
            return -10.0
        elif board[2] == 0 and board[5] == self.__opponent_player_ID and board[8] == self.__opponent_player_ID:
            return -10.0
        elif board[2] == self.__opponent_player_ID and board[5] == 0 and board[8] == self.__opponent_player_ID:
            return -10.0

        elif board[0] == self.__opponent_player_ID and board[4] == self.__opponent_player_ID and board[8] == 0:
            return -10.0
        elif board[0] == 0 and board[4] == self.__opponent_player_ID and board[8] == self.__opponent_player_ID:
            return -10.0
        elif board[0] == self.__opponent_player_ID and board[4] == 0 and board[8] == self.__opponent_player_ID:
            return -10.0

        elif board[2] == self.__opponent_player_ID and board[4] == self.__opponent_player_ID and board[6] == 0:
            return -1.0
        elif board[2] == 0 and board[4] == self.__opponent_player_ID and board[6] == self.__opponent_player_ID:
            return -10.0
        elif board[2] == self.__opponent_player_ID and board[4] == 0 and board[6] == self.__opponent_player_ID:
            return -10.0

        # If it is non of the above and the game can still continue, then return a reward of -1
        for i in range(0, 9):
            if board[i] == 0:
                return -1.0
           
        # If the game tied, then return a 0 because this is a ok outcome 
        return 0.0

    def set_actions_iteratively(self) -> bool:
        temp_game = ttt.TicTacToe()
        for i in range(0,self.__max_state_space):
            temp_game.set_board_to(self.state_space_to_board(i,9))
            possible_actions = temp_game.get_possible_actions()
            action_size = possible_actions.size
            for action in possible_actions:
                self.__actions[i,int(action)] = 1/action_size
            
    #----------------------------------------------------------------------------------
    #getter functions
    #----------------------------------------------------------------------------------
    
    def get_all_state_values(self) -> np.ndarray:
        return self.__state_values
    
    def get_state_value(self, state_space: int) -> float:
        return self.__state_values[state_space]

    def get_all_rewards(self) -> np.ndarray:
        return self.__rewards
    
    def get_reward(self, state_space: int) -> int:
        return self.__rewards[state_space]
    
    def get_all_actions(self) -> np.ndarray:
        return self.__actions
    
    def get_alpha(self) -> float:
        return self.__alpha
    
    def get_gamma(self) -> float:
        return self.__gamma

    def get_max_state_space(self) -> int:
        return self.__max_state_space
    
    
    #-----------------------------------------------------------------------------------
    #Debug functions
    #-----------------------------------------------------------------------------------
    
    def print_state_values(self):
        for i in range(0,self.__max_state_space):
            print(self.__state_values[i])
            
    def print_reward_values(self):
        for i in range(0,self.__max_state_space):
            print(self.__rewards[i])
            
    def print_policy_values(self):
        for i in range(0,self.__max_state_space):
            print(self.__actions[i])
        