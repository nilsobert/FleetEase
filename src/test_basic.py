import numpy as np
from scipy.optimize import linear_sum_assignment
from typing import Callable
from scipy.spatial.distance import cdist
from api.models import *
import time
from api import API

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

def assign_customers_to_vehicles_sequential(vehicles, customers):
    """
    Assign vehicles to customers iteratively until all customers are served.
    
    Parameters:
    - vehicles: List of vehicle coordinates
    - customers: List of Customer objects
    
    Returns:
    - assignment_history: A list of tuples (vehicle index, customer index, cost) for all assignments
    """
    # Track which customers have been served
    unserved_customers = customers[:]
    assignment_history = []
    
    while unserved_customers.any():
        # Get the current positions of the vehicles
        vehicle_positions = [vehicle.position for vehicle in vehicles]
        customer_positions = [customer.position for customer in unserved_customers]
        
        # Compute the distance matrix
        dist = zero_pad(get_distance_matrix(customer_positions, vehicle_positions))
        
        # Assign vehicles to customers using Hungarian algorithm
        row_ind, col_ind = linear_sum_assignment(dist)
        mapping = np.column_stack((row_ind, col_ind))
        costs = dist[row_ind, col_ind]
        
        # Filter out zero-cost assignments (due to padding)
        non_zero_mask = costs != 0
        costs = costs[non_zero_mask]
        mapping = mapping[non_zero_mask]
        
        # Record assignments
        for cost, (customer_idx, vehicle_idx) in zip(costs, mapping):
            assignment_history.append((vehicle_idx, customer_idx, cost))
        
        # Update vehicle positions to the destinations of assigned customers
        for customer_idx, vehicle_idx in mapping:
            vehicles[vehicle_idx].coordinate = unserved_customers[customer_idx].destination
        
        # Remove served customers from the list
        unserved_customers = [
            cust for idx, cust in enumerate(unserved_customers) if idx not in mapping[:, 0]
        ]
    
    return assignment_history
        

if __name__ == "__main__":
    num_vehicles = 20
    num_customers =100
    scenario, customers, vehicles = API().create_and_query_scenario(num_customers = num_customers, num_vehicles = num_vehicles)




