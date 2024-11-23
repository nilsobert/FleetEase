import httpx
import asyncio
import json
from models.scenario import Scenario

class API:

    def __init__(self) -> None:
        self.basic_api = _BasicAPI()
        self.scenario_runner = _ScenarioRunnerAPI()

    async def get_customer(self, customer):
        return await self.basic_api.get_customer(customer.id)

    async def get_customer_for_scenario(self, scenario):
        pass

    async def get_scenario_metadata(self, scenario):
        pass

    async def create_and_initialize_scenario(self, scenario):
        response = await self.basic_api.create_scenario(23, 34)
        print(Scenario.from_json(json.loads(await self.scenario_runner.initialize_scenario(response))))

    async def get_all_scenarios(self):
        pass

    async def delete_scenario(self, scenario):
        pass

    async def get_scenario(self, scenario):
        pass

    async def update_scenario(self, scenario):
        pass

    async def launch_scenario(self, scenario):
        pass

    async def get_vehicle(self, vehicle):
        pass

    async def get_all_vehicles_for_scenario(self, scenario):
        pass

class _BasicAPI:
    base_url = 'http://159.65.113.122:8080'
    
    def __init__(self) -> None:
        self.request_handler = _RequestHandler()

    async def get_customer(self, customer_id):
        endpoint = 'customers'
        url = f"{self.base_url}/{endpoint}"
        params = {
            "customerId": customer_id,
        }
        return await self.request_handler.get(url, params=params)

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
                return response.json()  # Return parsed JSON
        except httpx.RequestError as e:
            print(f"GET request failed: {e}")
            return None

    async def post(self, url, data=None, params=None):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(url, json=data, headers=self.headers, params=params)
                response.raise_for_status()
                return response.json()  # Return parsed JSON
        except httpx.RequestError as e:
            print(f"POST request failed: {e}")
            return None

    async def put(self, url, data=None):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.put(url, json=data, headers=self.headers)
                response.raise_for_status()
                return response.json()  # Return parsed JSON
        except httpx.RequestError as e:
            print(f"PUT request failed: {e}")
            return None
        
    async def delete(self, url, data=None):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.delete(url, json=data, headers=self.headers)
                response.raise_for_status()
                return response.json()  # Return parsed JSON
        except httpx.RequestError as e:
            print(f"DELETE request failed: {e}")
            return None

# Running the code
async def main():
    api = API()
    await api.create_and_initialize_scenario(342)

# Run the async function using asyncio
asyncio.run(main())