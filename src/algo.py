from aux import *
import numpy as np
from scipy.optimize import linear_sum_assignment
from typing import Callable

def zero_pad(matrix):
    m = matrix.reshape((matrix.shape[0], -1))
    padded = 0 * np.ones(2 * [max(m.shape)], dtype=m.dtype)
    padded[0:m.shape[0], 0:m.shape[1]] = m
    return padded

def get_distance_matrix(v1, v2):
    pass


class Assigner:
    def __init__(self, vehicles:list[Vehicle], passengers:list[Passenger], algorithm:str="basic") -> None:
        self.algorithm:str = algorithm
        self.assign: Callable = self.get_function()
        self.vehicles: list[Vehicle] = vehicles
        self.passengers: list[Passenger] = passengers
    
    def get_function(self) -> Callable:
        match self.algorithm:
            case "basic":
                return self.basic
    
    def basic():
        pass

if __name__ == "__main__":
    r2=np.random.rand(3,5)
    print(zero_pad(r2))