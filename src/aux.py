from dataclasses import dataclass
from datetime import datetime
from typing import Any

class Coordinate:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Vehicle:
    def __init__(self, position:Coordinate, charge:int=100, state="idle", ident:str="def_veh"):
        self.id = ident
        self.position = position  
        self.charge = charge  
        self.state = state  # "transporting", "idle", or "preparing"

    def __repr__(self):
        return f"Vehicle(position={self.position}, charge={self.charge}, state='{self.state}', ident={self.ident})"


class Passenger:
    def __init__(self, initial_position:Coordinate, destination:Coordinate, state="waiting", ident:str="def_pass"):
        self.id = ident
        self.initial_position = initial_position 
        self.destination = destination 
        self.state = state  # "waiting" or "travelling"

    def __repr__(self):
        return f"Passenger(initial_position={self.initial_position}, destination={self.destination}, state='{self.state}', ident={self.ident})"


class Job:
    def __init__(self, request_time:datetime, passenger:Passenger, vehicle:Vehicle, state:str="preparing", pickup_time:datetime|None=None, completion_time:datetime|None=None) -> None:
        self.request_time: datetime = request_time
        self.state: str = state # preparing | transporting | complete
        self.pickup_time: datetime | None = pickup_time
        self.passenger: Passenger = passenger
        self.vehicle: Vehicle = vehicle
        self.completion_time: datetime = completion_time
    
    def complete(self, time:datetime=datetime.now()):
        self.state = "complete"
        self.completion_time = time
    


@dataclass
class ApplicationState:
    cars: list[Vehicle]
    persons: list[Passenger]
    jobs: list[Job]
