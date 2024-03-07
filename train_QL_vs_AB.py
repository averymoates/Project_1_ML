import TicTacToe.TicTacToe as TTT
import TicTacToe.alphabeta as ab
import QLearning.QLearning as ql
import numpy as np
from tqdm import tqdm

from TicTacToe.alphabeta import alphabeta

alpha = 0.1
gamma = 0.2
epsilon = 0.1

#Player one is alpha beta
opponent = ab.alphabeta()

#Player two will be the TD agent
agent = ql.QLearning(alpha,gamma,2**18,9)

def main():
    trials = [1,5,10,50,100,500,1000,5000,10_000]
    
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
            action = -1

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
                    possible_actions = np.array([int(i) for i in game.get_possible_moves()])
                    action = choose_action(current_state_space,possible_actions)
                    game.make_move(action,game.get_player_two())

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
                    agent.qlearn(current_state_space,action,next_state_space,reward)

                    current_updated = False
                    next_updated = False     
                
        agent.save_q_values('QLearning/QL_results/vs_AB/State_value_{0}.csv'.format(episodes))


def choose_action(current_state: int, possible_action: np.ndarray) -> int:
    global epsilon
    a = -1
    if np.random.rand() < epsilon:
        a = np.random.choice(possible_action,1)
    else:
        a = agent.get_argmax_q(current_state,possible_action)

    if np.random.rand() < 0.001:
        epsilon -= 0.0005
    
    if epsilon < 0:
        epsilon = 0

    if type(a) == np.ndarray:
        a = int(a[0])
        
    return a

if __name__ == '__main__':
    main()