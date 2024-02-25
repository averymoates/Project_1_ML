import TicTacToe as TTT
import TemporalDifference as td
import numpy as np
import sys
import csv

from alphabeta import alphabeta

def main():
    alpha = 0.01
    gamma = 0.01

    Player_one = alphabeta()
    Player_two = td.TemporalDifference(2**18, alpha, gamma, 2)

    train_counter = 0

    #Trainning
    while train_counter != 500:
        game = TTT.TicTacToe(board=np.array([0,0,0,0,0,0,0,0,0]),current_player=1,game_started=True)
        # game.start_game()
        current_player = game.get_current_player()

        #Complete one game of training
        while(game.get_game_status()):
            if current_player == 1:
                placement = Player_one.alphabeta_make_move(game.get_board(),10,1)
                game.make_move(placement,1)
                current_player = game.get_current_player()

            elif current_player == 2:
                placement = Player_two.train_td(game.get_board(), 9)
                game.make_move(placement,2)
                current_player = game.get_current_player()

            game.check_board()

        #After a multiple of 10 training sessions, play 50 games to see how it has done
        if train_counter%10 == 0:
            game_counter = 0
            total_games = 0
            player_one_wins = 0
            player_two_wins = 0
            game_ties = 0
            
            while game_counter != 50:
                game = TTT.TicTacToe(board=np.array([0,0,0,0,0,0,0,0,0]),current_player=-1,game_started=False)
                game.start_game()
                current_player = game.get_current_player()

                while(game.get_game_status()):
                    if current_player == 1:
                        placement = Player_one.alphabeta_make_move(game.get_board(),10,1)
                        game.make_move(placement,1)
                        current_player = game.get_current_player()

                    elif current_player == 2:
                        placement = Player_two.TD_make_move(game.get_board(), 9)
                        game.make_move(placement,2)
                        current_player = game.get_current_player()

                    game.check_board()

                game_counter = game_counter + 1
                total_games = total_games + 1
                winner = game.check_board()
                if winner == 1:
                    player_one_wins = player_one_wins + 1
                
                elif winner == 2:
                    player_two_wins = player_two_wins + 1

                elif winner == 3:
                    game_ties = game_ties + 1

            print('{0},{1},{2}'.format(player_one_wins/total_games, player_two_wins/total_games, game_ties/total_games))


        train_counter = train_counter + 1

if __name__ == '__main__':
    main()