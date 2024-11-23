from aux import *
import numpy as np
from scipy.optimize import linear_sum_assignment
from typing import Callable
from scipy.spatial.distance import cdist

def zero_pad(matrix):
    m = matrix.reshape((matrix.shape[0], -1))
    padded = 0 * np.ones(2 * [max(m.shape)], dtype=m.dtype)
    padded[0:m.shape[0], 0:m.shape[1]] = m
    return padded

def haversine_vector(coords1: np.ndarray, coords2: np.ndarray) -> np.ndarray:
    lat1, lon1 = np.radians(coords1[:, 0]), np.radians(coords1[:, 1])
    lat2, lon2 = np.radians(coords2[:, 0]), np.radians(coords2[:, 1])

    dlat = lat2[:, np.newaxis] - lat1
    dlon = lon2[:, np.newaxis] - lon1

    a = (
        np.sin(dlat / 2)**2
        + np.cos(lat1) * np.cos(lat2)[:, np.newaxis] * np.sin(dlon / 2)**2
    )
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    
    R = 6371.0
    return R * c  # [km]

def get_distance_matrix(v1, v2):
    v1_array = np.array([coord.as_tuple() for coord in v1])
    v2_array = np.array([coord.as_tuple() for coord in v2])
    
    distance_matrix = cdist(v1_array, v2_array, metric=lambda u, v: haversine_vector(np.array([u]), np.array([v]))[0])
    return distance_matrix

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
        
        return linear_sum_assignment()

if __name__ == "__main__":
    coordsx = np.array([Coordinate(52.5200, 13.4050), Coordinate(40.7128, -74.0060), Coordinate(34.0522, -118.2437)])
    coordsy = np.array([Coordinate(48.8566, 2.3522), Coordinate(55.7558, 37.6173)])
    dist = zero_pad(get_distance_matrix(coordsx, coordsy))
    