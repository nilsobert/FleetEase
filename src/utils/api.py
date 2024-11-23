import requests
from scenario import Scenario


class API:

    def __init__(self) -> None:
        _BasicAPI.__init__(self, )

    def get_customer(customer):
        return _BasicAPI.get_customer(customer.id)

    def get_customer_for_scenario(scenario):
        pass

    def get_scenario_metadata(scenario):
        pass

    def create_and_initialize_scenario(scenario):
        response = _BasicAPI.create_scenario(scenario)
        _ScenarioRunnerAPI.initialize_scenario(response)

    def get_all_scenarios():
        pass

    def delete_scenario(scenario):
        pass

    def get_scenario(scenario):
        pass

    def update_scenario(scenario):
        pass

    def launch_scenario(scenario):
        pass


    def get_vehicle(vehicle):
        pass

    def get_all_vehicles_for_scenario(scenario):
        pass
    

class _BasicAPI:
    base_url = 'http://159.65.113.122:8080'

    def get_customer(self, customer_id):
        endpoint = 'customers'
        url = f"{self.base_url}/{endpoint}"
        params = {
            "customerId": customer_id,
        } 
        return _RequestHandler(url, params=params)

    def get_customers_for_scenario(self, scenario_id):
        endpoint = f"scenarios/{scenario_id}/customers"
        url = f"{self.base_url}/{endpoint}"
        return _RequestHandler.get(url)

    def get_scenario_metadata(self, scenario_id):
        endpoint = f"scenarios/{scenario_id}/metadata"
        url = f"{self.base_url}/{endpoint}"
        return _RequestHandler.get(url)

    def create_scenario(self, num_of_customers, num_of_vehicles):
        endpoint = 'scenario/create'
        url = f"{self.base_url}/{endpoint}"
        params = {
            "numberOfVehicles": num_of_vehicles,
            "numberOfCustomers": num_of_customers
        }
        return _RequestHandler.post(url, params=params)

    def get_all_scenarios(self):
        endpoint = 'scenarios'
        url = f"{self.base_url}/{endpoint}"
        return _RequestHandler.post(url)

    def delete_scenario(self, scenario_id):
        endpoint = f"scenario/{scenario_id}"
        url = f"{self.base_url}/{endpoint}"
        return _RequestHandler.delete(url)

    def get_scenario(self, scenario_id):
        endpoint = f"scenarios/{scenario_id}"
        url = f"{self.base_url}/{endpoint}"
        return _RequestHandler.get(url)

    def get_all_vehicles_for_scenario(self, scenario_id):
        endpoint = f"scenarios/{scenario_id}/vehicles"
        url = f"{self.base_url}/{endpoint}"
        return _RequestHandler.get(url)

    def get_vehicle(self, vehicle_id):
        endpoint = f"vehicles/{vehicle_id}"
        url = f"{self.base_url}/{endpoint}"
        return _RequestHandler.get(url)

class _ScenarioRunnerAPI:
    base_url = 'http://159.65.113.122:8090'

    def get_scenario(self, scenario_id):
        endpoint = f"Scenarios/get_scenarios/{scenario_id}"
        url = f"{self.base_url}/{endpoint}"
        return _RequestHandler.get(url)

    def initialize_scenario(self, body):
        endpoint = f"Scenarios/initialize_scenario"
        url = f"{self.base_url}/{endpoint}"
        return _RequestHandler.post(url)

    def update_scenario(self, scenario_id, vehicle_id, customer_id):
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
        return _RequestHandler.put(url, data=payload)

    def launch_scenario(self, scenario_id, speed):
        endpoint = f"/Runner/launch_scenario/{scenario_id}"
        url = f"{self.base_url}/{endpoint}"
        params = {
            "speed": speed
        }
        return _RequestHandler.post(url, params=params)

    
class _RequestHandler:
    def __init__(self, headers=None):
        self.headers = headers or {"Content-Type": "application/json"}

    def get(self, url, endpoint, params=None):
        try:
            response = requests.get(url, params=params, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"GET request failed: {e}")
            return None

    def post(self, url, data=None, params=None):
        try:
            response = requests.post(url, json=data, headers=self.headers, params=params)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"POST request failed: {e}")
            return None

    def put(self, url, endpoint, data=None):
        try:
            response = requests.put(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"PUT request failed: {e}")
            return None
        
    def delete(self, url, endpoint, data=None):
        try:
            response = requests.delete(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"DELETE request failed: {e}")
            return None