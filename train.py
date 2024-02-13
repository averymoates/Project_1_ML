import TicTacToe as TTT

def main():
    game = TTT.TicTacToe()

    game.display_board()
    game.start_game()

    print(game.get_game_status())

    while game.get_game_status() == True:
        game.play_turn()


if __name__ == '__main__':
    main()