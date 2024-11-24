from api.models.customer import Customer
from api.models.vehicle import Vehicle
from api.models.scenario import Scenario
from api.api import API
from scipy.optimize import linear_sum_assignment
import asyncio
import numpy as np
import time

from aux import zero_pad, get_distance_matrix

def random_initial_assignement(scenario, vehicles, customers, api):
    # Get the current positions of the vehicles
    unserved_customers = customers[:]
    vehicle_positions = [vehicle.position for vehicle in vehicles]
    customer_positions = [customer.position for customer in unserved_customers]
    
    free_vehicles = vehicles[:]
    
    buys_vehicles = []
    served_customers = []
    num_ass = min(len(free_vehicles), len(unserved_customers))
    cars = np.arange(0,num_ass)
    persons = np.random.choice(len(unserved_customers), num_ass)
    mapping = np.column_stack((persons, cars))
    for customer_idx, vehicle_idx in mapping:
        asyncio.run(api.update_scenario(scenario=scenario, customer=customers[customer_idx], vehicle=vehicles[vehicle_idx]))
        buys_vehicles.append(vehicles[vehicle_idx])
        served_customers.append(customers[customer_idx])
        free_vehicles[vehicle_idx] = None
        unserved_customers[customer_idx] = None
    free_vehicles = list(filter(lambda a: a != None, free_vehicles))
    unserved_customers = list(filter(lambda a: a != None, unserved_customers))
    return scenario, free_vehicles, buys_vehicles, unserved_customers, served_customers

def random_procedual_assignement(scenario, vehicles, customers, api):
    return random_initial_assignement(scenario, vehicles, customers, api)


def random_loop(self, synchronizer, data_lock):
    while self.unserved_customers:
        time.sleep(2)
        #print(".")
        updated_scenario = asyncio.run(self.api.get_runner_scenario(self.scenario))
        self.unpack_scenario(updated_scenario)
        if self.free_vehicles:
            _, _free_vehicles, _buys_vehicles, _unserved_customers, _served_customers = random_procedual_assignement(self.scenario, self.free_vehicles, self.unserved_customers, self.api)
            self.free_vehicles = _free_vehicles
            self.busy_vehicles += _buys_vehicles
            self.unserved_customers = _unserved_customers
            self.served_customers += _served_customers
            with data_lock:
                synchronizer.fleet.scenario = self.scenario

