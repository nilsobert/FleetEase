from models import *
import numpy as np
from scipy.optimize import linear_sum_assignment
from typing import Callable
from scipy.spatial.distance import cdist
import time

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
    def __init__(self, vehicles:list[Vehicle], customers:list[Customer], algorithm:str="basic") -> None:
        self.algorithm: str = algorithm
        self.assign: Callable = self.get_function()
        self.vehicles: list[Vehicle] = vehicles
        self.customers: list[Customer] = customers
    
    def get_function(self) -> Callable:
        match self.algorithm:
            case "basic":
                return self.basic
    
    def basic(self):
        coordsx, coordsy = [customer.coordinate for customer in self.customers], [vehicle.coordinate for vehicle in self.vehicles]
        dist = zero_pad(get_distance_matrix(coordsx, coordsy))
        row_ind, col_ind = linear_sum_assignment(dist)
        mapping = np.column_stack((row_ind, col_ind))
        costs = dist[row_ind, col_ind]

        non_zero_mask = costs != 0
        costs = costs[non_zero_mask]
        mapping = mapping[non_zero_mask]

        for cost, (customer, vehicle) in zip(costs, mapping):
            print(cost, customer, vehicle)
        

if __name__ == "__main__":
    coordsx = np.zeros((200), dtype=object)
    coordsy = np.zeros((50), dtype=object)
    for n in range(200):
        coordsx[n] = Coordinate(np.random.random()*100, np.random.random()*100)
    for n in range(50):
        coordsy[n] = Coordinate(np.random.random()*100, np.random.random()*100)
    dist = zero_pad(get_distance_matrix(coordsx, coordsy))
    row_ind, col_ind = linear_sum_assignment(dist)
    mapping = np.column_stack((row_ind, col_ind))
    costs = dist[row_ind, col_ind]

    non_zero_mask = costs != 0
    costs = costs[non_zero_mask]
    mapping = mapping[non_zero_mask]

    for cost, (customer, vehicle) in zip(costs, mapping):
            print(cost, customer, vehicle)


