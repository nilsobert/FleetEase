from flask import Flask, request, jsonify
import threading
import time
from algo import Assigner
from api.api import API
import asyncio
from synchronizer import Synchronizer

# Shared data and lock
global synchronizer
synchronizer = Synchronizer()
data_lock = threading.Lock()


def init_api():
    api = API()
    num_vehicles = 30
    num_customers = 70
    scenario, vehicles, customers = asyncio.run(api.create_and_query_scenario(num_of_customers = num_customers, num_of_vehicles = num_vehicles))
    asyncio.run(api.launch_scenario(speed=0.1, scenario=scenario))
    return scenario, vehicles, customers, api

    

def test_run():
    scenario, vehicles, customers, api = init_api()
    algorithm = "basic"

    assigner = Assigner(scenario=scenario, vehicles=vehicles, customers=customers, api=api, algorithm=algorithm, debug=False)
    assigner.assign(synchronizer, data_lock)

if __name__ == "__main__":
   
