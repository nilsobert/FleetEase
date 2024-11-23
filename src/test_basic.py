import numpy as np
from scipy.optimize import linear_sum_assignment
from typing import Callable
from scipy.spatial.distance import cdist
from api.models import *
import asyncio
import time
from api.api import API
from plotter import Plotter
from algo import Assigner
        

if __name__ == "__main__":
    api = API()
    num_vehicles = 10
    num_customers =35
    scenario, vehicles, customers = asyncio.run(api.create_and_query_scenario(num_of_customers = num_customers, num_of_vehicles = num_vehicles))
    asyncio.run(api.launch_scenario(speed=0.5, scenario=scenario))
    assigner = Assigner(scenario=scenario, vehicles=vehicles, customers=customers, api=api, algorithm="basic")
    assigner.assign()
    #plotter = Plotter(vehicles=vehicles, customers=customers)
    #plotter.animate(10)

