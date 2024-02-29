import TicTacToe.TicTacToe as ttt
from TicTacToe.TicTacToe import TicTacToe
import numpy as np
import csv

"""
Author: Avery Moates
Date: 2/23/2024

Temporal Difference

"""

class TemporalDifference:
    
    #Private variables
    __state_values = None
    __rewards = None
    __alpha = 0
    __gamma = 0
    __max_states = 0
    
    def __init__(self, alpha: float, gamma: float) -> None:
        self.__state_values = {}
        self.__rewards = {}
        self.__alpha = alpha
        self.__gamma = gamma
        
        
    def temporal_difference(self, current_state: int, next_state: int, next_reward: float) -> None:
        #Add states to state values
        if current_state not in self.__state_values.keys():
            self.__state_values[current_state] = float(0.0)
            self.__max_states = self.__max_states + 1
            
        if next_state not in self.__state_values.keys():
            self.__state_values[next_state] = float(0.0)
            self.__max_states = self.__max_states + 1
            
        if next_state not in self.__rewards.keys():
            self.__rewards[next_state] = float(next_reward)
            
        self.__state_values[current_state] = self.__state_values[current_state] + self.__alpha*(self.__rewards[next_state] + self.__gamma*(self.__state_values[next_state]) - self.__state_values[current_state])
    
    #------------------------------------------------------------------------------------
    #Saving Functions
    #------------------------------------------------------------------------------------
    
    def save_state_values(self, file_path: str) -> None:
        with open(file_path, mode='w') as file:
            file_writer = csv.writer(file,delimiter=',')
            
            for i in self.__state_values.keys():
                value = [i, self.__state_values[i]]
                file_writer.writerow(value)
                
    def save_rewards(self, file_path: str) -> None:
        with open(file_path, mode='w') as file:
            file_writer = csv.writer(file,delimiter=',')
            
            for i in self.__rewards.keys():
                value = [i, self.__rewards[i]]
                file_writer.writerow(value)
    
    #------------------------------------------------------------------------------------
    #Loading Functions
    #------------------------------------------------------------------------------------
    
    def load_state_values(self, file_path: str) -> None:
        with open(file_path) as file:
            file_reader = csv.reader(file, delimiter=',')
            
            for row in file_reader:
                # print(row)
                self.__state_values[int(row[0])] = int(row[1]) 
                
    def load_rewards(self, file_path: str) -> None:
        with open(file_path) as file:
            file_reader = csv.reader(file, delimiter=',')
            
            for row in file_reader:
                # print(row)
                self.__rewards[int(row[0])] = int(row[1])    
    
    #------------------------------------------------------------------------------------
    #Getter Functions
    #------------------------------------------------------------------------------------
       
    def get_state_values(self) -> dict:
        return self.__state_values
    
    def get_state_value(self, state_space: int) -> float:
        if state_space not in self.__state_values.keys():
            print('State space of [{0}] is not in known state spaces'.format(state_space))
            return -100_000_000
        else:
            return self.__state_values[state_space]
    
    def get_rewards(self) -> dict:
        return self.__rewards
    
    def get_reward(self, state_space: int) -> float:
        if state_space not in self.__state_values.keys():
            print('State space of [{0}] is not in known state spaces'.format(state_space))
            return -100_000_000
        else:
            return self.__rewards[state_space]
    
    def get_max_states(self) -> int:
        return self.__max_states
    