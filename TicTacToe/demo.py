import TicTacToe as TTT
import sys

from alphabeta import alphabeta

def main():
    game = TTT.TicTacToe()

    otherPlayer = alphabeta()

    game.display_board()
    game.start_game()

    # print(game.get_game_status())

    current_player = game.get_current_player()

    # print('Player {0} starts'.format(current_player))

    while(game.get_game_status()):
        if current_player == game.get_player_one():
            placement = otherPlayer.alphabeta_make_move(game.get_board(),10,game.get_player_one())
            game.make_move(placement,game.get_player_one())
            current_player = game.get_current_player()
            game.display_board()

        elif current_player == game.get_player_two():
            # print(game.get_possible_actions())
            print('Player 2, enter your move:')
            placement = int(input())
            game.make_move(placement,game.get_player_two())
            current_player = game.get_current_player()
            game.display_board()

        game.check_board()

if __name__ == '__main__':
    main()