class Scenario:
    def __init__(self, json_data) -> None:
        self.vehicles: list[Vehicle] = []
        self.passengers: list[Passenger] = []
        scenario = json.loads(json_data).get("scenario")
        vehicles = scenario.get("vehicles")
        passengers = scenario.get("customers")