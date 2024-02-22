import numpy as np
from random import randint
import copy

class TicTacToe:

    BOARD_SIZE = 3

    board = 0

    PLAYER_ONE = 1
    PLAYER_TWO = 2

    game_started = False

    current_player = -1

    state_value = 0b111111111000000000

    def __init__(self, board = np.array([0,0,0,0,0,0,0,0,0]), currentplayer=-1, game_started=False):
        self.board = board
        self.current_player = currentplayer
        self.game_started = game_started

    def make_move(self,placement,player):
        if self.game_started == False:
            print('Tic Tac Toe has not started')
            return False

        # Return false if the placement is not 0,1,2,3,4,5,6,7,8
        if placement <0 or placement >= 9:
            print('Wrong placement value')
            return False
        
        if player != self.current_player:
            print('Wrong player')
            return False

        # Return true if the placement is legal
        if self.check_move(placement):
            self.board[placement] = player
            if player==1:
                self.current_player = 2

            elif player==2:
                self.current_player = 1

            return True
        
        # Return false if the placement is not legal
        return False

    def unmake_move(self,placement,player):
        if placement<0 or placement>=9:
            print('Wrong placement value')
            return False
        
        if self.current_player == player:
            print('Current player can not numake move')
            return False
        
        if self.board[placement] == player:
            
            if player == 1 and self.current_player == 2:
                self.board[placement] = 0
                self.current_player = player

            elif player == 2 and self.current_player == 1:
                self.board[placement] = 0
                self.current_player = player

            else:
                print('Something went wrong')
                return False
            
            return True
        
        else:
            print('Can not unmake that move.')
            return False

    def check_move(self,placement):
        # Return true if the placement is empty
        if self.board[placement] == 0:
            return True
        
        # Return false if the placement is not empty
        return False
    
    #To check if a placement is empty
    def is_empty(self, placement):
        if placement<0 and placement>=9:
            print("Wrong placement value")
            return False
        
        if self.board[placement] == 0:
            return True
        else:
            return False

        

    # 1 - player one wins, 2 - player two wins, 3 - tie, 0 - can still play
    def check_board(self):
        # Player one wins
        if self.board[0] == self.PLAYER_ONE and self.board[1] == self.PLAYER_ONE and self.board[2] == self.PLAYER_ONE:
            self.game_started = False
            return self.PLAYER_ONE
        elif self.board[3] == self.PLAYER_ONE and self.board[4] == self.PLAYER_ONE and self.board[5] == self.PLAYER_ONE:
            self.game_started = False
            return self.PLAYER_ONE
        elif self.board[6] == self.PLAYER_ONE and self.board[7] == self.PLAYER_ONE and self.board[8] == self.PLAYER_ONE:
            self.game_started = False
            return self.PLAYER_ONE
        elif self.board[0] == self.PLAYER_ONE and self.board[3] == self.PLAYER_ONE and self.board[6] == self.PLAYER_ONE:
            self.game_started = False
            return self.PLAYER_ONE
        elif self.board[1] == self.PLAYER_ONE and self.board[4] == self.PLAYER_ONE and self.board[7] == self.PLAYER_ONE:
            self.game_started = False
            return self.PLAYER_ONE
        elif self.board[2] == self.PLAYER_ONE and self.board[5] == self.PLAYER_ONE and self.board[8] == self.PLAYER_ONE:
            self.game_started = False
            return self.PLAYER_ONE
        elif self.board[0] == self.PLAYER_ONE and self.board[4] == self.PLAYER_ONE and self.board[8] == self.PLAYER_ONE:
            self.game_started = False
            return self.PLAYER_ONE
        elif self.board[2] == self.PLAYER_ONE and self.board[4] == self.PLAYER_ONE and self.board[6] == self.PLAYER_ONE:
            self.game_started = False
            return self.PLAYER_ONE
        
        # Player two wins
        if self.board[0] == self.PLAYER_TWO and self.board[1] == self.PLAYER_TWO and self.board[2] == self.PLAYER_TWO:
            self.game_started = False
            return self.PLAYER_TWO
        elif self.board[3] == self.PLAYER_TWO and self.board[4] == self.PLAYER_TWO and self.board[5] == self.PLAYER_TWO:
            self.game_started = False
            return self.PLAYER_TWO
        elif self.board[6] == self.PLAYER_TWO and self.board[7] == self.PLAYER_TWO and self.board[8] == self.PLAYER_TWO:
            self.game_started = False
            return self.PLAYER_TWO
        elif self.board[0] == self.PLAYER_TWO and self.board[3] == self.PLAYER_TWO and self.board[6] == self.PLAYER_TWO:
            self.game_started = False
            return self.PLAYER_TWO
        elif self.board[1] == self.PLAYER_TWO and self.board[4] == self.PLAYER_TWO and self.board[7] == self.PLAYER_TWO:
            self.game_started = False
            return self.PLAYER_TWO
        elif self.board[2] == self.PLAYER_TWO and self.board[5] == self.PLAYER_TWO and self.board[8] == self.PLAYER_TWO:
            self.game_started = False
            return self.PLAYER_TWO
        elif self.board[0] == self.PLAYER_TWO and self.board[4] == self.PLAYER_TWO and self.board[8] == self.PLAYER_TWO:
            self.game_started = False
            return self.PLAYER_TWO
        elif self.board[2] == self.PLAYER_TWO and self.board[4] == self.PLAYER_TWO and self.board[6] == self.PLAYER_TWO:
            self.game_started = False
            return self.PLAYER_TWO
        
        # Tied game
        if 0 not in self.board:
            self.game_started = False
            return 3
        
        # Still empty slots
        return 0

    def display_board(self):
        if self.board.size != 9:
            print("Wrong board size")

        else:
            print(self.board[0:3])
            print(self.board[3:6])
            print(self.board[6:9]) 
            print('')  

    def get_current_player(self):
        return self.current_player

    # def player_one_turn(self,placement):
    #     if self.current_player != 1:
    #         print("Wrong player.")
    #         return False
        
    #     if self.make_move(placement,self.PLAYER_ONE):
    #         self.display_board()
    #         self.current_player = 2
    #         return True

    #     else:
    #         print("Please try again player {0}".format(self.PLAYER_ONE))
    #         return False

        
    # def player_two_turn(self,placement):
    #     if self.current_player != 2:
    #         print("Wrong player.")
    #         return False
        
    #     if self.make_move(placement,self.PLAYER_TWO):
    #         self.display_board()
    #         self.current_player = 1
    #         return True

    #     else:
    #         print("Please try again player {0}".format(self.PLAYER_TWO))
    #         return False

    def get_board(self):
        return copy.deepcopy(self.board)

    def start_game(self,display=False):
        self.game_started = True
        self.current_player = randint(1,2)
        if display == True:
            print('Player {0} is first'.format(self.current_player))

    def get_game_status(self):
        return self.game_started

    # def play_turn(self, move=-1):
    #     print('Player {0}, please type in your move'.format(self.current_player))

    #     placement_value = input()

    #     while True:
    #         if placement_value.isdigit() == False:
    #             print('Wrong value for placement. Please try again player {0}'.format(self.current_player))
    #             placement_value = input()
    #             continue

    #         else:
    #             placement_value = int(placement_value)

    #         if isinstance(placement_value, int):
    #             if self.current_player == self.PLAYER_ONE:
    #                 if self.player_one_turn(placement_value):
    #                     break
    #                 else:
    #                     placement_value = input()

    #             elif self.current_player == self.PLAYER_TWO:
    #                 if self.player_two_turn(placement_value):
    #                     break
    #                 else:
    #                     placement_value = input()

    #         else:
    #             print('Wrong value for placement. Please try again player {0}'.format(self.current_player))
    #             placement_value = input()

    #     game_status = self.check_board()

    #     if game_status == 1 or game_status == 2:
    #         print('Player {0} has won!'.format(game_status))

    #     elif game_status == 3:
    #         print('Game ended in a tie')

    def cal_state_space(self):
        temp_value = 0

        for i in range(0,self.BOARD_SIZE*self.BOARD_SIZE):
            if self.board[i] == 0:
                temp_value = (0b1 << i) | temp_value

            elif self.board[i] == 2:
                temp_value = (0b1 << i + 9) | temp_value

        self.state_value = temp_value

    def get_state_space(self):
        return self.state_value
    
    def get_action_used(self):
        return False
        #Need to work on this function