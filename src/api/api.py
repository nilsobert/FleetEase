import httpx
import asyncio
from models.scenario import Scenario
from models.customer import Customer
from models.vehicle import Vehicle

class API:

    def __init__(self) -> None:
        self.basic_api = _BasicAPI()
        self.scenario_runner = _ScenarioRunnerAPI()

    async def get_customer(self, customer_id):
        return Customer.from_json(await self.basic_api.get_customer(customer_id))

    async def get_customers_for_scenario(self, scenario):
        json_data = await self.basic_api.get_customers_for_scenario(scenario.id)
        customers = [Customer.from_json(customer_data) for customer_data in json_data]
        return customers

    async def get_scenario_metadata(self, scenario):
        pass

    async def create_and_initialize_scenario(self, num_of_customers, num_of_vehicles):
        response = await self.basic_api.create_scenario(num_of_customers, num_of_vehicles)
        return Scenario.from_json(await self.scenario_runner.initialize_scenario(response))
    
    async def get_all_scenarios(self):
        json_data = await self.basic_api.get_all_scenarios()
        scenarios = [Scenario.from_json(scenario_data) for scenario_data in json_data]
        return scenarios

    async def delete_scenario(self, scenario):
        await self.basic_api.delete_scenario(scenario)

    async def get_scenario(self, scenario_id):
        return Scenario.from_json(await self.basic_api.get_scenario(scenario_id))

    async def update_scenario(self, scenario):
        pass

    async def launch_scenario(self, scenario):
        pass

    async def get_vehicle(self, vehicle_id):
        return Vehicle.from_json(await self.basic_api.get_vehicle(vehicle_id))

    async def get_all_vehicles_for_scenario(self, scenario):
        json_data = await self.basic_api.get_all_vehicles_for_scenario(scenario)
        vehicles = [Vehicle.from_json(vehicle_data) for vehicle_data in json_data]
        return vehicles

class _BasicAPI:
    base_url = 'http://159.65.113.122:8080'
    
    def __init__(self) -> None:
        self.request_handler = _RequestHandler()

    async def get_customer(self, customer_id):
        endpoint = f'customers/{customer_id}'
        url = f"{self.base_url}/{endpoint}"
        return await self.request_handler.get(url)

    async def get_customers_for_scenario(self, scenario_id):
        endpoint = f"scenarios/{scenario_id}/customers"
        url = f"{self.base_url}/{endpoint}"
        return await self.request_handler.get(url)

    async def get_scenario_metadata(self, scenario_id):
        endpoint = f"scenarios/{scenario_id}/metadata"
        url = f"{self.base_url}/{endpoint}"
        return await self.request_handler.get(url)

    async def create_scenario(self, num_of_customers, num_of_vehicles):
        endpoint = 'scenario/create'
        url = f"{self.base_url}/{endpoint}"
        params = {
            "numberOfVehicles": num_of_vehicles,
            "numberOfCustomers": num_of_customers
        }
        print(f"URL: {url}, Params: {params}")
        return await self.request_handler.post(url, params=params)

    async def get_all_scenarios(self):
        endpoint = 'scenarios'
        url = f"{self.base_url}/{endpoint}"
        return await self.request_handler.get(url)

    async def delete_scenario(self, scenario_id):
        endpoint = f"scenario/{scenario_id}"
        url = f"{self.base_url}/{endpoint}"
        return await self.request_handler.delete(url)

    async def get_scenario(self, scenario_id):
        endpoint = f"scenarios/{scenario_id}"
        url = f"{self.base_url}/{endpoint}"
        return await self.request_handler.get(url)

    async def get_all_vehicles_for_scenario(self, scenario_id):
        endpoint = f"scenarios/{scenario_id}/vehicles"
        url = f"{self.base_url}/{endpoint}"
        return await self.request_handler.get(url)

    async def get_vehicle(self, vehicle_id):
        endpoint = f"vehicles/{vehicle_id}"
        url = f"{self.base_url}/{endpoint}"
        return await self.request_handler.get(url)

class _ScenarioRunnerAPI:
    base_url = 'http://159.65.113.122:8090'

    def __init__(self) -> None:
        self.request_handler = _RequestHandler()

    async def get_scenario(self, scenario_id):
        endpoint = f"Scenarios/get_scenarios/{scenario_id}"
        url = f"{self.base_url}/{endpoint}"
        return await self.request_handler.get(url)

    async def initialize_scenario(self, body):
        endpoint = f"Scenarios/initialize_scenario"
        url = f"{self.base_url}/{endpoint}"
        return await self.request_handler.post(url, data=body)

    async def update_scenario(self, scenario_id, vehicle_id, customer_id):
        endpoint = f"/Scenarios/update_scenario/{scenario_id}"
        url = f"{self.base_url}/{endpoint}"
        payload = {
            "vehicles": [
                {
                    "id": vehicle_id,
                    "customerId": customer_id
                }
            ]
        }
        return await self.request_handler.put(url, data=payload)

    async def launch_scenario(self, scenario_id, speed):
        endpoint = f"/Runner/launch_scenario/{scenario_id}"
        url = f"{self.base_url}/{endpoint}"
        params = {
            "speed": speed
        }
        return await self.request_handler.post(url, params=params)

    
class _RequestHandler:
    def __init__(self, headers=None):
        self.headers = headers or {"Content-Type": "application/json"}

    async def get(self, url, params=None):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, params=params, headers=self.headers)
                response.raise_for_status()
                return response.json()
        except httpx.RequestError as e:
            print(f"GET request failed: {e}")
            return None

    async def post(self, url, data=None, params=None):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(url, json=data, headers=self.headers, params=params)
                response.raise_for_status()
                return response.json()
        except httpx.RequestError as e:
            print(f"POST request failed: {e}")
            return None

    async def put(self, url, data=None):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.put(url, json=data, headers=self.headers)
                response.raise_for_status()
                return response.json()
        except httpx.RequestError as e:
            print(f"PUT request failed: {e}")
            return None
        
    async def delete(self, url, data=None):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.delete(url, json=data, headers=self.headers)
                response.raise_for_status()
                return response.json()
        except httpx.RequestError as e:
            print(f"DELETE request failed: {e}")
            return None


async def main():
    api = API()
    x = await api.create_and_initialize_scenario(12, 23)
    await api.get_customers_for_scenario(x) #"b5eedd63-db55-4a1e-8c4e-a4d2cc489e17"
    #await api.get_customer("af0fa386-88cf-4e4f-ad22-ffc8726585f1")

if __name__ == "__main__":
    asyncio.run(main())