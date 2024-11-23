from api.models.customer import Customer
from api.models.vehicle import Vehicle
from api.models.scenario import Scenario
from api.api import API
from scipy.optimize import linear_sum_assignment
import asyncio
import numpy as np
import time

from aux import zero_pad, get_distance_matrix

def basic_initial_assignement(scenario, vehicles, customers, api):
    # Get the current positions of the vehicles
    unserved_customers = customers[:]
    vehicle_positions = [vehicle.position for vehicle in vehicles]
    customer_positions = [customer.position for customer in unserved_customers]
    
    free_vehicles = vehicles[:]
    
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
    buys_vehicles = []
    served_customers = []
    for customer_idx, vehicle_idx in mapping:
        asyncio.run(api.update_scenario(scenario=scenario, customer=customers[customer_idx], vehicle=vehicles[vehicle_idx]))
        buys_vehicles.append(vehicles[vehicle_idx])
        served_customers.append(customers[customer_idx])
        free_vehicles[vehicle_idx] = None
        unserved_customers[customer_idx] = None
    free_vehicles = list(filter(lambda a: a != None, free_vehicles))
    unserved_customers = list(filter(lambda a: a != None, unserved_customers))
    return scenario, free_vehicles, buys_vehicles, unserved_customers, served_customers

def basic_procedual_assignement(scenario, vehicles, customers, api):
    return basic_initial_assignement(scenario, vehicles, customers, api)


def basic_loop(self):
    while self.unserved_customers:
        time.sleep(1)
        updated_scenario = asyncio.run(self.api.get_runner_scenario(self.scenario))
        self.unpack_scenario()
        if self.free_vehicles:
            _, _free_vehicles, _buys_vehicles, _unserved_customers, _served_customers = basic_procedual_assignement(self.scenario, self.vehicles, self.customers, self.api)
            self.free_vehicles = _free_vehicles
            self.busy_vehicles += _buys_vehicles
            self.unserved_customers = _unserved_customers
            self.served_customers += _served_customers

