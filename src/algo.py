from api.models import *
import numpy as np
from scipy.optimize import linear_sum_assignment
from typing import Callable
from scipy.spatial.distance import cdist
from api.models.vehicle import Vehicle
from api.models.customer import Customer
from api.models.scenario import Scenario
import time
from api.api import API
from basic import basic_initial_assignement, basic_loop

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
    def __init__(self, scenario: Scenario, vehicles:list[Vehicle], customers:list[Customer], api:API, algorithm:str="basic") -> None:
        self.api = api
        self.scenario = scenario
        self.algorithm: str = algorithm
        self.assign: Callable = self.get_function()
        self.vehicles: list[Vehicle] = vehicles
        self.customers: list[Customer] = customers
        self.free_vehicles = []
        self.busy_vehicles = []
        self.unserved_customers = []
        self.served_customers = []
    
    def get_function(self) -> Callable:
        match self.algorithm:
            case "basic":
                return self.basic
    
    def unpack_scenario(self, new_scenario):
        self.scenario = new_scenario
        self.free_vehicles = [v for v in self.scenario.vehicles if v.isAvailable]

    
    def basic(self):
        print("Initial assignement:")
        _, self.free_vehicles, self.buys_vehicles, self.unserved_customers, self.served_customers = basic_initial_assignement(self.scenario, self.vehicles, self.customers, self.api)
        print(f"    {len(self.free_vehicles)} free vehicles")
        print(f"    {len(self.buys_vehicles)} busy vehicles")
        print(f"    {len(self.unserved_customers)} unserved customers")
        print(f"    {len(self.served_customers)} served customers")
        basic_loop(self)
        

if __name__ == "__main__":
    pass


