import TicTacToe.TicTacToe as ttt
import TicTacToe.alphabeta as ab
import QLearning.QLearning as ql

import numpy as np

def main():
    alpha = 0.1
    gamma = 0.2
    
    game = ttt.TicTacToe()
    game.set_game_to_playable()
    
    player_one = ab.alphabeta()
    player_two = ql.QLearning(alpha,gamma,2**18,9)
    player_two.load_q_values('QLearning/QL_results/vs_AB/State_value_500.csv')
    
    game.print_board()
    
    current_player = game.get_current_player()
    
    while game.is_game_playable():
        if current_player == game.get_player_one():
            placement = player_one.alphabeta_make_move(game.get_board(),10,game.get_player_one())
            game.make_move(placement,game.get_player_one())
            
        elif current_player == game.get_player_two():
            current_state = game.get_state_space()
            possible_actions = np.array([int(i) for i in game.get_possible_moves()])
            placement = player_two.get_argmax_q(current_state,possible_actions)
            print('QL placement value: {0}'.format(placement))
            game.make_move(placement,game.get_player_two())
            
        game.print_board()
        game.check_game()
        current_player = game.get_current_player()
        
if __name__ == '__main__':
    main()