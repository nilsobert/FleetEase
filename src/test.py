import numpy as np
from scipy.optimize import linear_sum_assignment

# Assume Coordinate class is already defined as before

class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def as_tuple(self):
        return self.lat, self.lon

    def __repr__(self):
        return f"Coordinate(lat={self.lat}, lon={self.lon})"

# Haversine distance function
def haversine(coord1, coord2):
    lat1, lon1 = coord1.as_tuple()
    lat2, lon2 = coord2.as_tuple()
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    R = 6371.0  # Earth radius in km
    return R * c  # Distance in km

# Customer class implementation
class Customer:
    def __init__(self, initial_position: Coordinate, destination: Coordinate):
        self.initial_position = initial_position  # Starting position of the customer
        self.destination = destination  # Destination position of the customer
        self.state = 'waiting'  # Initial state of the customer (could be 'waiting' or 'travelling')

    def __repr__(self):
        return f"Customer(initial_position={self.initial_position}, destination={self.destination})"

    def get_starting_position(self):
        return self.initial_position.as_tuple()

    def get_destination(self):
        return self.destination.as_tuple()

# Greedy Assignment function (using Hungarian algorithm)
def greedy_assignment(cars, customers):
    dist_matrix = np.zeros((len(cars), len(customers)))
    for i, car in enumerate(cars):
        for j, customer in enumerate(customers):
            dist_matrix[i, j] = haversine(car, customer.initial_position)  # Use car and customer directly

    row_ind, col_ind = linear_sum_assignment(dist_matrix)
    
    return row_ind, col_ind, dist_matrix[row_ind, col_ind]

# Perturbation function to modify current assignments
def perturb_assignment(cars, customers):
    row_ind, col_ind, _ = greedy_assignment(cars, customers)
    i, j = np.random.choice(len(row_ind), size=2, replace=False)
    col_ind[i], col_ind[j] = col_ind[j], col_ind[i]  # Swap two customer assignments
    
    return row_ind, col_ind

# HALNS Implementation
def halns(cars, customers, max_iter=100):
    # Initial assignment using a greedy algorithm
    row_ind, col_ind, costs = greedy_assignment(cars, customers)
    best_assignment = (row_ind, col_ind)
    best_cost = np.sum(costs)
    
    for _ in range(max_iter):
        print(best_cost)
        # Apply a perturbation
        new_row_ind, new_col_ind = perturb_assignment(cars, customers)
        new_costs = np.array([haversine(cars[i], customers[j].initial_position) for i, j in zip(new_row_ind, new_col_ind)])
        new_total_cost = np.sum(new_costs)
        print(new_total_cost)
        
        # If the new solution is better, accept it
        if new_total_cost < best_cost:
            best_cost = new_total_cost
            best_assignment = (new_row_ind, new_col_ind)

    return best_assignment, best_cost

import random

# Function to generate a random coordinate (lat, lon)
def generate_random_coordinate():
    lat = random.uniform(-90.0, 90.0)  # Random latitude between -90 and 90
    lon = random.uniform(-180.0, 180.0)  # Random longitude between -180 and 180
    return Coordinate(lat, lon)

# Generate random cars and customers
def generate_random_cars_and_customers(num_cars, num_customers):
    cars = [generate_random_coordinate() for _ in range(num_cars)]
    customers = [
        Customer(generate_random_coordinate(), generate_random_coordinate())  # Random start and destination for each customer
        for _ in range(num_customers)
    ]
    return cars, customers

# Example usage with random generation
num_cars = 50
num_customers = 100
cars, customers = generate_random_cars_and_customers(num_cars, num_customers)

best_assignment, best_cost = halns(cars, customers, max_iter=100)
print("Best Assignment:", best_assignment)
print("Best Cost:", best_cost)

