from TicTacToe import TicTacToe
import sys
import numpy as np

"""
Author: Avery Moates
Date: 2/23/2024

Alpha beta prunning algorithm for tic tac toe

player == 1

"""

class alphabeta:

    def __init__(self):
        """Constructor
        """
        self.__game = TicTacToe()
        self.__max_depth = 3

    def alphabeta_make_move(self, board, depth: int, player: int) -> int:
        """Function to make a decision on a value of 0-8 using the Alpha-beta algorithm

        Args:
            board (int[9] array): Array to describe the placement of a Tic Tac Toe game
            depth (int): The max depth you want the Alpha-Beta algorithm to calculate 
            player (int): Who the max player is in Tic Tac Toe

        Returns:
            int: int value between 0-8 
        """
        self.__max_depth = depth
        #Setting everything up so that alpha beta works
        game = TicTacToe(board=board,current_player=player,game_started=True)
        maxPlayer = game.get_current_player()

        #Error if the max player is not the current player
        if maxPlayer != player:
            print('Something went wrong')
            return -1
        
        #Set the min player
        minPlayer = 0
        if maxPlayer == 1:
            minPlayer = 2

        elif maxPlayer == 2:
            minPlayer = 1

        alpha = -100_000_000_000
        beta = 100_000_000_000

        return self.init_alphabeta(game,alpha,beta,maxPlayer,minPlayer)
    
    def init_alphabeta(self, TTTgame: TicTacToe, alpha: int, beta: int, maxPlayer: int, minPlayer: int) -> int:
        """The start of the Alpha-Beta algorithm

        Args:
            TTTgame (TicTacToe): _description_
            alpha (int): _description_
            beta (int): _description_
            maxPlayer (int): _description_
            minPlayer (int): _description_

        Returns:
            int: _description_
        """
        value = -100_000_000_000
        best_move = -1

        #Loop through each node for Max player
        for i in range(0,9):
            if TTTgame.is_empty(i):
                TTTgame.make_move(i,maxPlayer)
                score = self.alphabeta(TTTgame,1,alpha,beta,False,maxPlayer,minPlayer)
                TTTgame.unmake_move(i,maxPlayer)

                if score > value:
                    value = score
                    best_move = i

                if score > alpha:
                    alpha = score

                #Prune branch if it can
                if alpha > beta:
                    return best_move
                
        return best_move
    
    def alphabeta(self, TTTgame: TicTacToe, depth: int, alpha: int, beta: int, isMax: bool, maxPlayer: int, minPlayer: int) -> int:
        """Recursive function of the alpha-beta algorithm

        Args:
            TTTgame (TicTacToe): _description_
            depth (int): _description_
            alpha (int): _description_
            beta (int): _description_
            isMax (bool): _description_
            maxPlayer (int): _description_
            minPlayer (int): _description_

        Returns:
            int: _description_
        """
        if TTTgame.check_board() != 0 or depth > self.__max_depth:
            return self.evaluate_game(TTTgame,maxPlayer,minPlayer)
        
        if isMax == True:
            max_value = -100_000_000_000
            for i in range(0,9):
                if TTTgame.is_empty(i):
                    TTTgame.make_move(i,maxPlayer)
                    score = self.alphabeta(TTTgame,depth+1,alpha,beta,False,maxPlayer,minPlayer)
                    TTTgame.unmake_move(i,maxPlayer)

                    max_value = max([max_value,score])
                    alpha = max([alpha, score])

                    if(alpha >= beta):
                        return max_value
                    
            return max_value
        
        elif isMax == False:
            min_value = 100_000_000_000
            for i in range(0,9):
                if TTTgame.is_empty(i):
                    TTTgame.make_move(i,minPlayer)
                    score = self.alphabeta(TTTgame,depth+1,alpha,beta,True,maxPlayer,minPlayer)
                    TTTgame.unmake_move(i,minPlayer)

                    min_value = min([min_value,score])
                    beta = min([beta, score])

                    if(alpha >= beta):
                        return min_value
                    
            return min_value

    def evaluate_game(self, TTTgame: TicTacToe, maxPlayer: int, minPlayer: int) -> int:
        """Function to calculate the score of the board. 0 if the board has no winner, a 1 for max player winning and additional 1 for each empty space, and a -1 for min player winning and additional -1 for each empty space

        Args:
            TTTgame (TicTacToe): _description_
            maxPlayer (int): _description_
            minPlayer (int): _description_

        Returns:
            int: _description_
        """
        winner = TTTgame.check_board()

        if winner == maxPlayer:
            score = 1
            for i in range(0,9):
                if TTTgame.is_empty(i):
                    score = score + 1

            return score
            
        elif winner == minPlayer:
            score = -1
            for i in range(0,9):
                if TTTgame.is_empty(i):
                    score = score - 1
            
            return score
        
        else:
            return 0

