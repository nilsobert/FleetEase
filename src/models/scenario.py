from .vehicle import *
from .customer import *
import json

class Scenario:
    def __init__(self, json_data) -> None:
        self.vehicles: list[Vehicle] = []
        self.passengers: list[Customer] = []
        scenario = json.loads(json_data).get("scenario")
        vehicles = scenario.get("vehicles")
        passengers = scenario.get("customers")