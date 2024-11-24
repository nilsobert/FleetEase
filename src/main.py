from flask import Flask, request, jsonify
import threading
import time
from algo import Assigner
from api.api import API
import asyncio
from server import app, synchronizer, data_lock
from systemStatistics import System


def init_api():
    api = API()
    num_vehicles = 30
    num_customers = 70
    scenario, vehicles, customers = asyncio.run(api.create_and_query_scenario(num_of_customers = num_customers, num_of_vehicles = num_vehicles))
    asyncio.run(api.launch_scenario(speed=0.1, scenario=scenario))
    return scenario, vehicles, customers, api

# Worker thread function
def assignement_worker(scenario, vehicles, customers, api, algorithm="basic"):
    global synchronizer
    assigner = Assigner(scenario=scenario, vehicles=vehicles, customers=customers, api=api, algorithm=algorithm, debug=False)
    assigner.assign(synchronizer, data_lock)

# Worker thread function
def system_worker():
    global synchronizer
    system = System()
    system.measure(synchronizer, data_lock)



if __name__ == "__main__":
    print("\033[32mInitializing api...\033[0m")
    scenario, vehicles, customers, api = init_api()
    print("\033[34mInitializing assignment threat...\033[0m")
    assigner_thread = threading.Thread(target=assignement_worker, args=(scenario, vehicles, customers, api))
    assigner_thread.start()
    print("\033[36mInitializing system threat...\033[0m")
    system_thread = threading.Thread(target=system_worker, args=())
    system_thread.start()

    
    # Start the Flask server
    app.run(debug=False)
