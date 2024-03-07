import csv
import numpy as np

class QLearning():
    __alpha = 0
    __gamma = 0

    __q_values = None
    __max_states = 0
    __max_actions = 0

    __inital_state_action_value = 0

    def __init__(self, alpha: float, gamma: float, max_states: int, max_actions: int):
        self.__alpha = alpha
        self.__gamma = gamma
        self.__max_states = max_states
        self.__max_actions = max_actions
        self.__q_values = self.__inital_state_action_value*np.ones((self.__max_states,self.__max_actions))

    def qlearn(self,current_state: int, action: int, next_state: int, reward: float) -> None:
        max_q = np.max(self.__q_values[next_state])
        q = self.__q_values[current_state][action]
        self.__q_values[current_state][action] = q + self.__alpha*(reward + self.__gamma*max_q - q)

    #------------------------------------------------------------------------------------
    #Saving Functions
    #------------------------------------------------------------------------------------
        
    def save_q_values(self, file_path: str) -> None:

        with open(file_path, mode='w') as file:
            file_writer = csv.writer(file,delimiter=',')
            
            for i in range(self.__max_states):
                value = self.__q_values[i]
                file_writer.writerow(value)

    #------------------------------------------------------------------------------------
    #Loading Functions
    #------------------------------------------------------------------------------------
                
    def load_q_values(self, file_path: str) -> None:
        with open(file_path) as file:
            file_reader = csv.reader(file, delimiter=',')
            
            i = 0
            for row in file_reader:
                if row == []:
                    continue
                self.__q_values[i] = [float(value) for value in row]
                i+=1

    #------------------------------------------------------------------------------------
    #getter Functions
    #------------------------------------------------------------------------------------ 
    
    def get_q_value(self, state: int, action: int) -> float:
        return self.__q_values[state][action]
    
    def get_q_values(self) -> np.ndarray:
        return self.__q_values
    
    def get_argmax_q(self, state: int, possible_actions: np.ndarray) -> int:
        
        values = self.__q_values[state]
        
        max = np.argmax(values[possible_actions])
        
        return possible_actions[max]
