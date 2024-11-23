import requests

class API:

    def __init__(self) -> None:
        _BasicAPI.__init__(self, )

    def get_customer():
        pass
        

class _BasicAPI:
    base_url = 'http://159.65.113.122:8080'

    def get_customer(id):
        pass

    def get_customers_for_scenario(scenario_id):
        pass

    def get_scenario_metadata(scenario_id):
        pass

    def initialize_scenario(number_vehicles, number_customers):
        pass

    def get_all_scenarios():
        pass

    def delete_scenario(scenario_id):
        pass

    def get_scenario(scenario_id):
        pass

    def get_all_vehicles_for_scenario(scenario_id):
        pass

    def get_vehicle(vehicle_id):
        pass

class _ScenarioRunnerAPI:
    base_url = 'http://159.65.113.122:8090'

    def get_scenario(scenario_id):
        pass

    def initialize_scenario(scenario_id, start_time):
        pass

    def update_scenario(scenario_id):
        pass

    def launch_scenario(scenario_id, speed):
        pass

    
class _RequestHandler:
    def __init__(self, headers=None):
        self.headers = headers or {"Content-Type": "application/json"}

    def get(self, base_url, endpoint, params=None):
        url = f"{base_url}/{endpoint.lstrip('/')}"
        try:
            response = requests.get(url, params=params, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"GET request failed: {e}")
            return None

    def post(self, base_url, endpoint, data=None):
        url = f"{base_url}/{endpoint.lstrip('/')}"
        try:
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"POST request failed: {e}")
            return None

    def put(self, base_url, endpoint, data=None):
        url = f"{base_url}/{endpoint.lstrip('/')}"
        try:
            response = requests.put(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"PUT request failed: {e}")
            return None
        
    def delete(self, base_url, endpoint, data=None):
        url = f"{base_url}/{endpoint.lstrip('/')}"
        try:
            response = requests.delete(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"DELETE request failed: {e}")
            return None