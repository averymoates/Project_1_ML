import TicTacToe.TicTacToe as TTT
import TicTacToe.alphabeta as ab
import TemporalDifference.TemporalDifference as td
import numpy as np
from tqdm import tqdm

from TicTacToe.alphabeta import alphabeta

def main():
    trials = [1,5,10,50,100,500]
    alpha = 0.1
    gamma = 0.2

    #Player one is alpha beta
    opponent = ab.alphabeta()

    #Player two will be the TD agent
    agent = td.TemporalDifference(alpha,gamma,0.5)

    for episodes in tqdm(trials):
        
        for game in tqdm(range(episodes)):
            game = TTT.TicTacToe()
            game.set_game_to_playable()

            current_player = game.get_current_player()
            current_state_space = None
            current_updated = False
            next_state_space = None
            next_updated = False
            reward = None

            while game.is_game_playable():
                
                if current_player == game.get_player_one():
                    placement = opponent.alphabeta_make_move(game.get_board(),10,game.get_player_one())
                    game.make_move(placement,game.get_player_one())
                    next_state_space = game.get_state_space()
                    if current_updated:
                        next_updated = True
                    

                elif current_player == game.get_player_two():
                    current_state_space = game.get_state_space()
                    current_updated = True
                    possible_actions = game.get_possible_moves()
                    placement = np.random.choice(possible_actions,1)
                    game.make_move(placement,game.get_player_two())

                game_status = game.check_game()
                current_player = game.get_current_player()

                if current_updated and next_updated:
                    reward = -1
                    if game_status == game.get_player_one():
                        reward = -5
                    elif game_status == game.get_player_two():
                        reward = 5
                    elif game_status == 2:
                        reward = 0

                    agent.temporal_difference(current_state_space,next_state_space,reward)
                    current_updated = False
                    next_updated = False
                    

                
                
        agent.save_state_values('TemporalDifference/TD_results/vs_AB/State_value_{0}.csv'.format(episodes))
        agent.save_rewards('TemporalDifference/TD_results/vs_AB/Rewards_{0}.csv'.format(episodes))


if __name__ == '__main__':
    main()