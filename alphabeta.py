from TicTacToe import TicTacToe
import sys
import numpy as np


class alphabeta:

    #Constructor function
    def __init__(self):
        self.game = TicTacToe()
        self.max_depth = 3

    #Function to return a value of 0-8
    def alphabeta_make_move(self, board, depth, player: int) -> int:
        self.max_depth = depth
        #Setting everything up so that alpha beta works
        game = TicTacToe(board=board,currentplayer=player,game_started=True)
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
        if TTTgame.check_board() != 0 or depth > self.max_depth:
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

