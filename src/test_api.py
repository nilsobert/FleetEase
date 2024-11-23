from api.api import *

api = API()

scenario = api.create_and_initialize_scenario(100,20)
customers = api.get_customers_for_scenario(scenario)
vehicles = api.get_all_vehicles_for_scenario(scenario)

print(scenario)
print(customers)
print(vehicles)