from typing import List
from api.models.coordinate import Coordinate
from api.models.customer import Customer
from dataclasses import dataclass
from aux import haversine_scalar

@dataclass
class Trip:
    start: Coordinate
    destination: Coordinate
    customer: Customer | None
    start_time: float
    end_time: float | None

    def __str__(self) -> str:
        return f"{str(self.start)} -> {str(self.destination)}, Time:{round(float(self.end_time)-float(self.start_time),3)}, Customer:{self.customer != None}"

    def complete(self):
        if not self.end_time:
            self.end_time = self.start_time + self.distance()
    
    def distance(self):
        return haversine_scalar(self.start, self.destination)
    

@dataclass
class RoutePlan:
    initial_Coords: Coordinate
    trips: list[Trip]

    def __str__(self) -> str:
        out = str(self.initial_Coords) + "\n"
        for trip in self.trips:
            out += f"    ---> {str(trip)}\n"
        return out

    def complete(self):
        for trip in self.trips:
            trip.complete()
    
    def complete_last(self):
        self.trips[-1].complete()
    
    def last_position(self):
        if self.trips:
            return self.trips[-1].destination
        else:
            return self.initial_Coords
    
    def last_time(self):
        if self.trips:
            return self.trips[-1].end_time
        else:
            return 0
    
    def add_customer(self, customer):
        self.trips.append(Trip(start=self.last_position(), destination=customer.position, start_time=self.last_time(), end_time=None, customer=None))
        self.complete_last()
        self.trips.append(Trip(start=self.last_position(), destination=customer.destination, start_time=self.last_time(), end_time=None, customer=customer))
        self.complete_last()


