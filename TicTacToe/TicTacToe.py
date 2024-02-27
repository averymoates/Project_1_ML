import numpy as np
from random import randint
import copy

"""
Author: Avery Moates
Date: 2/23/2024

Simple tic tac toe game

"""

class TicTacToe:

    #Private variables
    __board_size = 9
    __player_one = 1
    __player_two = 2
    __game_started = False
    __current_player = -1

    def __init__(self, board = np.array([0,0,0,0,0,0,0,0,0]), current_player=-1, game_started=False):
        """Constructor function

        Args:
            board (int[9], optional): _description_. Defaults to np.array([0,0,0,0,0,0,0,0,0]).
            currentplayer (int, optional): _description_. Defaults to -1.
            game_started (bool, optional): _description_. Defaults to False.
        """
        self.__board = board
        self.__current_player = current_player
        self.__game_started = game_started

    def make_move(self,placement: int, player: int) -> bool:
        """Function to make a move for a certain player

        Args:
            placement (int): Index value
            player (int): Player

        Returns:
            bool: True if the the move was legal. False if the move was illegal
        """
        if self.__game_started == False:
            print('Tic Tac Toe has not started')
            return False

        # Return false if the placement is not 0,1,2,3,4,5,6,7,8
        if (placement < 0) or (placement >= 9):
            print('Wrong placement value {0} player {1}'.format(placement, player))
            return False
        
        if player != self.__current_player:
            print('Wrong player')
            return False

        # Return true if the placement is legal
        if self.check_move(placement):
            self.__board[placement] = player
            if player==1:
                self.__current_player = 2

            elif player==2:
                self.__current_player = 1

            return True
        
        # Return false if the placement is not legal
        return False

    def unmake_move(self,placement: int, player: int) -> bool:
        """Function to unmake a move for a certain player. NOTE: you can only unmake a move for the player that just make a move. Be carefull using this function

        Args:
            placement (int): Index value
            player (int): Player

        Returns:
            bool: True if the action was legal. False if the action was illegal
        """
        if placement<0 or placement>=9:
            print('Wrong placement value')
            return False
        
        if self.__current_player == player:
            print('Current player can not numake move')
            return False
        
        if self.__board[placement] == player:
            
            if player == 1 and self.__current_player == 2:
                self.__board[placement] = 0
                self.__current_player = player
                self.__game_started = True

            elif player == 2 and self.__current_player == 1:
                self.__board[placement] = 0
                self.__current_player = player
                self.__game_started = True

            else:
                print('Something went wrong')
                return False
            
            return True
        
        else:
            print('Can not unmake that move.')
            return False

    def check_move(self,placement: int) -> bool:
        """Function to check if a move is legal or not

        Args:
            placement (int): Index value

        Returns:
            bool: True if the action was legal. False if the action was illegal
        """
        # Return true if the placement is empty
        if self.__board[placement] == 0:
            return True
        
        # Return false if the placement is not empty
        return False
    
    #To check if a placement is empty
    def is_empty(self, placement: int) -> bool:
        """To check if a index value is empty or a value of 0

        Args:
            placement (int): Index value

        Returns:
            bool: True if the value in placement index is 0, false if not
        """
        if placement<0 and placement>=9:
            print("Wrong placement value")
            return False
        
        if self.__board[placement] == 0:
            return True
        else:
            return False

    def check_board(self) -> int:
        """Function to check if there is a winner to Tic Tac Toe.

        Returns:
            int: 1 - player one wins, 2 - player two wins, 3 - tie, 0 - can still play
        """
        # Player one wins
        if self.__board[0] == self.__player_one and self.__board[1] == self.__player_one and self.__board[2] == self.__player_one:
            self.__game_started = False
            return self.__player_one
        elif self.__board[3] == self.__player_one and self.__board[4] == self.__player_one and self.__board[5] == self.__player_one:
            self.__game_started = False
            return self.__player_one
        elif self.__board[6] == self.__player_one and self.__board[7] == self.__player_one and self.__board[8] == self.__player_one:
            self.__game_started = False
            return self.__player_one
        elif self.__board[0] == self.__player_one and self.__board[3] == self.__player_one and self.__board[6] == self.__player_one:
            self.__game_started = False
            return self.__player_one
        elif self.__board[1] == self.__player_one and self.__board[4] == self.__player_one and self.__board[7] == self.__player_one:
            self.__game_started = False
            return self.__player_one
        elif self.__board[2] == self.__player_one and self.__board[5] == self.__player_one and self.__board[8] == self.__player_one:
            self.__game_started = False
            return self.__player_one
        elif self.__board[0] == self.__player_one and self.__board[4] == self.__player_one and self.__board[8] == self.__player_one:
            self.__game_started = False
            return self.__player_one
        elif self.__board[2] == self.__player_one and self.__board[4] == self.__player_one and self.__board[6] == self.__player_one:
            self.__game_started = False
            return self.__player_one
        
        # Player two wins
        if self.__board[0] == self.__player_two and self.__board[1] == self.__player_two and self.__board[2] == self.__player_two:
            self.__game_started = False
            return self.__player_two
        elif self.__board[3] == self.__player_two and self.__board[4] == self.__player_two and self.__board[5] == self.__player_two:
            self.__game_started = False
            return self.__player_two
        elif self.__board[6] == self.__player_two and self.__board[7] == self.__player_two and self.__board[8] == self.__player_two:
            self.__game_started = False
            return self.__player_two
        elif self.__board[0] == self.__player_two and self.__board[3] == self.__player_two and self.__board[6] == self.__player_two:
            self.__game_started = False
            return self.__player_two
        elif self.__board[1] == self.__player_two and self.__board[4] == self.__player_two and self.__board[7] == self.__player_two:
            self.__game_started = False
            return self.__player_two
        elif self.__board[2] == self.__player_two and self.__board[5] == self.__player_two and self.__board[8] == self.__player_two:
            self.__game_started = False
            return self.__player_two
        elif self.__board[0] == self.__player_two and self.__board[4] == self.__player_two and self.__board[8] == self.__player_two:
            self.__game_started = False
            return self.__player_two
        elif self.__board[2] == self.__player_two and self.__board[4] == self.__player_two and self.__board[6] == self.__player_two:
            self.__game_started = False
            return self.__player_two
        
        # Tied game
        if 0 not in self.__board:
            self.__game_started = False
            return 3
        
        # Still empty slots
        return 0

    def display_board(self) -> None:
        """Void function to display the int[9] array in a 3 by 3 matrix
        """
        if self.__board.size != 9:
            print("Wrong __board size")

        else:
            print(self.__board[0:3])
            print(self.__board[3:6])
            print(self.__board[6:9]) 
            print('')  

    def get_current_player(self) -> int:
        return self.__current_player

    def get_board(self) -> np.ndarray:
        """A deep copy function of the int[9] array

        Returns:
            int[9]: Deep copy of the int[9] array
        """
        return copy.deepcopy(self.__board)

    def start_game(self,display=False) -> None:
        """Function to start the game

        Args:
            display (bool, optional): Prints out who the first player is. Defaults to False.
        """
        self.__game_started = True
        self.__current_player = randint(1,2)
        if display == True:
            print('Player {0} is first'.format(self.__current_player))

    def set_board_to(self, board: np.ndarray) -> None:
        """Function to set the Tic Tac Toe to a certain board configuration

        Args:
            board (np.ndarray): board array
        """
        self.__board = copy.deepcopy(board)
        
    def set_first_player(self,first_player: int) -> bool:
        """Function to set the first player

        Args:
            first_player (int): Player ID that you want to go first

        Returns:
            bool: True if it was successful
        """
        if first_player != 1 or first_player != 2:
            print('Wrong player ID values')
            self.__current_player = -1
            return False

        else:
            self.__current_player = first_player
            return True
    
    def get_game_status(self) -> bool:
        """Function to see if the game is going or not

        Returns:
            bool: True if the game is on, False if the game is not on
        """
        return self.__game_started

    def cal_state_space(self) -> int:
        """Function to calculate the state space using 18 bits. Bits 0-8 describes the placement of zeros. Bits 17-9 describes the placement of the players

           Example:
           [0 1 2]
           [1 0 0]   => 0b001000100_010110001 == 34993
           [2 0 1]

        Returns:
            int: value that will represent the board placement
        """
        temp_value = 0

        for i in range(0,self.__board_size):
            if self.__board[i] == 0:
                temp_value = (0b1 << i) | temp_value

            elif self.__board[i] == 2:
                temp_value = (0b1 << i + 9) | temp_value

        return temp_value

    # def get_state_space(self) -> int:
    #     """Function to get the value of the state space

    #     Returns:
    #         int: self.__state_value
    #     """
    #     self.cal_state_space()
    #     return self.__state_value

    def get_possible_actions(self) -> np.ndarray:
        """Function to get all the possible placement values

        Returns:
            np.ndarray: array of all the possible placement values
        """
        move = np.array([])
        move_index = 0
        
        for i in range(0, self.__board_size):
            if self.__board[i] == 0:
                if move.size > move_index:
                    move[move_index] = i
                    move_index = move_index + 1

                else:
                    move = np.insert(move,move_index,i)
                    move_index = move_index + 1

        return move