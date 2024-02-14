import TicTacToe as TTT

def main():
    game = TTT.TicTacToe()

    copyGame = TTT.TicTacToe(board=game.get_board())

    game.display_board()
    game.start_game()

    print(game.get_game_status())

    while game.get_game_status() == True:
        game.play_turn()
        game.cal_state_space()
        print(game.get_state_space())

    print("Copied board:")
    print(copyGame.display_board())


if __name__ == '__main__':
    main()