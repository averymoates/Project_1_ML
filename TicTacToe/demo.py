import TicTacToe as TTT
import sys

from alphabeta import alphabeta

def main():
    game = TTT.TicTacToe()

    otherPlayer = alphabeta()

    game.print_board()
    game.set_game_to_playable()

    # print(game.get_game_status())

    current_player = game.get_current_player()

    # print('Player {0} starts'.format(current_player))

    while(game.is_game_playable()):
        if current_player == game.get_player_one():
            placement = otherPlayer.alphabeta_make_move(game.get_board(),10,game.get_player_one())
            game.make_move(placement,game.get_player_one())
        elif current_player == game.get_player_two():
            print(game.get_possible_moves())
            print('Player 2, enter your move:')
            placement = int(input())
            game.make_move(placement,game.get_player_two())
            
        # print('Winner is {0}'.format(game.check_game()))
        current_player = game.get_current_player()
        game.print_board()
        print('State space is {0}\n'.format(game.get_state_space()))
        game.check_game()

if __name__ == '__main__':
    main()