from api.api import API
import asyncio

api = API()

scenario = asyncio.run(api.create_and_initialize_scenario(100,20))
print(scenario)

customers = asyncio.run(api.get_customers_for_scenario(scenario))
vehicles = asyncio.run(api.get_all_vehicles_for_scenario(scenario))


print(customers)
print(vehicles)
