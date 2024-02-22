import TicTacToe as TTT
import sys

def main():
    game = TTT.TicTacToe()

    copyGame = TTT.TicTacToe(board=game.get_board())

    game.display_board()
    game.start_game()

    print(game.get_game_status())

    current_player = game.get_current_player()

    game.make_move(1,current_player)

    game.display_board()

    game.unmake_move(1,current_player)

    game.display_board()

    print(sys.maxsize)

if __name__ == '__main__':
    main()