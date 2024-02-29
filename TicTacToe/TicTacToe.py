import numpy as np
import copy



class TicTacToe:
    """
    Class to simulate a game of tic tac toe with 2 players

    Author: Avery Moates
    Date: 2/28/2024
    """

    #Private variables
    __board = None
    __row_size = 3
    __col_size = 3
    __player_one = 1
    __player_two = -1
    __playable = False
    __current_player = 0

    def __init__(self) -> None:
        """Constructor
        """
        self.__board = np.zeros([self.__row_size,self.__col_size])

    #------------------------------------------------------------------------------------
    #Setter Functions
    #------------------------------------------------------------------------------------
        
    def set_board_to(self, board: np.ndarray) -> bool:
        """Function to override the current board to another board

        Args:
            board (np.ndarray): 3X3 numpy ndarray with 0,1,-1

        Returns:
            bool: True if the operations was successful
        """
        if board.shape != (self.__row_size,self.__col_size):
            print('Wrong board dimensions')
            return False
        #There is no check to see if the elements are 0,1, or -1
        else:
            self.__board = copy.deepcopy(board)
            return True
        
    def set_current_player_to(self, player: int) -> bool:
        """Function to set the current player

        Args:
            player (int): value of 0, 1, or -1

        Returns:
            bool: True if the operation was successful
        """
        if player in [self.__player_one, self.__player_two]:
            self.__current_player = player
            return True
        else:
            print('{0} is a wrong value for player'.format(player))
            return False
        
    def set_game_to_playable(self, choose_random_player = True) -> None:
        """Function to make the game playable

        Args:
            choose_random_player (bool, optional): _description_. Defaults to True.
        """
        self.__playable = True

        if choose_random_player == True and self.__current_player == 0:
            self.__current_player = np.random.choice([self.__player_one, self.__player_two], 1)

        elif choose_random_player == False and self.__current_player == 0:
            self.__current_player = self.__player_one

    #------------------------------------------------------------------------------------
    #Helper Functions
    #------------------------------------------------------------------------------------
    
    def is_empty(self, placement: int) -> bool:
        """Function to check if a placement value is playable

        Args:
            placement (int): 0-8 int value

        Returns:
            bool: True if the placement value is playable
        """
        if placement < 0 or placement >= 9:
            print('Placement value of [{0}]'.format(placement))
            return False
        
        else:
            col = int(placement % self.__col_size)
            row = int((placement-col)/self.__row_size)
            if self.__board[row,col] == 0:
                return True
            else:
                return False

    def change_player(self) -> bool:
        """Function to change player

        Returns:
            bool: _description_
        """
        if self.__current_player == 0:
            print('Game has not started.')
            return False
        
        if self.__current_player == self.__player_one:
            self.__current_player = self.__player_two
            return True
        elif self.__current_player == self.__player_two:
            self.__current_player = self.__player_one
            return True
        

    #------------------------------------------------------------------------------------
    #Game Functions
    #------------------------------------------------------------------------------------
            
    def make_move(self, placement: int, player: int) -> bool:
        """Function to make a move for a certain player with a given placement value. To make a move, it has to be that player's turn and the placement value be 0-8

        Args:
            placement (int): 0-8 int value
            player (int): 0, 1, or -1

        Returns:
            bool: True if the operation was successful
        """
        if self.__playable == False:
            print('Game has not started')
            return False
        elif placement < 0 or placement >= 9:
            print('Placement value of [{0}] is not allowed player {1}'.format(placement,player))
            return False
        elif player not in [self.__player_one, self.__player_two]:
            print('{0} is a wrong value for player'.format(player))
            return False
        elif player != self.__current_player:
            print('Player {0} can not make a move yet'.format(player))
            return False

        col = int(placement % self.__col_size)
        row = int((placement-col)/self.__row_size)
        
        if self.is_empty(placement):
            self.__board[row,col] = player
            
            if self.__current_player == self.__player_one:
                self.__current_player = self.__player_two
            elif self.__current_player == self.__player_two:
                self.__current_player = self.__player_one
            
            return True
        
    def unmake_move(self, placement: int, player: int) -> bool:
        """Function to unmake a certain move for a player given a placement value

        Args:
            placement (int): 0-8
            player (int): 0, 1, -1. The player value can not be the current player

        Returns:
            bool: True if the operation was successful
        """
        if placement < 0 or placement >= 9:
            print('Placement value of [{0}] is not allowed player {1}'.format(placement,player))
            return False
        elif player not in [self.__player_one, self.__player_two]:
            print('{0} is a wrong value for player'.format(player))
            return False
        elif player == self.__current_player:
            print('Player {0} can not unmake a move yet'.format(player))
            return False

        col = int(placement % self.__col_size)
        row = int((placement-col)/self.__row_size)
        
        if self.__board[row,col] == player:
            if player == self.__player_one and self.__current_player == self.__player_two:
                self.__board[row,col] = 0
                self.__current_player = player
                self.__playable = True
                
            elif player == self.__player_two and self.__current_player == self.__player_one:
                self.__board[row,col] = 0
                self.__current_player = player
                self.__playable = True
                
            else:
                print('Something went wrong')
                return False
            
            return True
        
        else:
            print('Can not unmake that move. Please try again')
            return False

    def check_game(self) -> int:
        """Function to see if there is a winner. 

        Returns:
            int: 0 for playable game, 1 for player one winning, -1 for player two winning, 2 for a tied game
        """
        #check all rows
        for i in range(self.__row_size):
            if (self.__board[i,:] == self.__player_one).all() or (self.__board[i,:] == self.__player_two).all():
                self.__playable = False
                return self.__board[i,0]
        
        #check all columns
        for i in range(self.__col_size):
            if (self.__board[:,i] == self.__player_one).all() or (self.__board[:,i]== self.__player_two).all():
                self.__playable = False
                return self.__board[0,i]
            
        #check all diagonals
        diagonal_one = np.array([self.__board[0,0], self.__board[1,1], self.__board[2,2]])
        diagonal_two = np.array([self.__board[0,2], self.__board[1,1], self.__board[2,0]])

        if (diagonal_one == self.__player_one).all() or (diagonal_one == self.__player_two).all():
            self.__playable = False
            return self.__board[1,1]
        elif (diagonal_two == self.__player_one).all() or (diagonal_two == self.__player_two).all():
            self.__playable = False
            return self.__board[1,1]
        
        #check if there is a zero
        if 0 in self.__board:
            self.__playable = True
            return 0
        
        #If non of the other checks happen, then it must be a tie    
        self.__playable = False  
        return 2
        
    #------------------------------------------------------------------------------------
    #Display Functions
    #------------------------------------------------------------------------------------
     
    def print_board(self) -> None:
        """Print the board in a nice format
        """
        for row in range(self.__row_size):
            line = ''

            for col in range(self.__col_size):
                if self.__board[row,col] == 0:
                    line = line + '[-]'
                elif self.__board[row,col] == self.__player_one:
                    line = line + '[X]'
                elif self.__board[row,col] == self.__player_two:
                    line = line + '[O]'
            
            print(line)
        print('')

    #------------------------------------------------------------------------------------
    #Getter Functions
    #------------------------------------------------------------------------------------
    
    def get_possible_moves(self) -> np.ndarray:
        """Function to get all the possible placement value

        Returns:
            np.ndarray: _description_
        """
        possible_moves = np.array([])
        move_index = 0

        for row in range(self.__row_size):
            for col in range(self.__col_size):
                if self.__board[row,col] == 0:
                    action_value = row*self.__row_size + col
                    
                    if possible_moves.size > move_index:
                        possible_moves[move_index] = action_value
                        move_index = move_index + 1
                        
                    else:
                        possible_moves = np.insert(possible_moves, move_index, action_value)
                        move_index = move_index + 1
                        
        return possible_moves
    
    def get_state_space(self) -> int:
        """Function to give a certain board configuration a unique int value

        Returns:
            int: unique int vlaue for board configuration
        """
        state_value = 0
        
        for row in range(self.__row_size):
            for col in range(self.__col_size):
                placement_value = row*3 + col
                if self.__board[row,col] == 0:
                    state_value = (0b1 << placement_value) | state_value
                    
                elif self.__board[row,col] == self.__player_two:
                    state_value = (0b1 << placement_value + 9) | state_value
                    
        return state_value
    
    def get_current_player(self) -> int:
        return self.__current_player
    
    def get_player_one(self) -> int:
        return self.__player_one
    
    def get_player_two(self) -> int:
        return self.__player_two
    
    def get_board(self) -> np.ndarray:
        return copy.deepcopy(self.__board)
    
    def is_game_playable(self) -> bool:
        return self.__playable


        

