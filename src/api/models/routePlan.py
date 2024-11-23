from typing import List
from api.models.coordinate import Coordinate
from api.models.customer import Customer
from dataclasses import dataclass
from aux import haversine_scalar

@dataclass
class Trip:
    start: Coordinate
    destination: Coordinate
    Customer: Customer | None
    start_time: float
    end_time: float | None

    def complete(self):
        if not self.end_time:
            self.end_time = self.start_time
    
    def distance(self):
        return haversine_scalar(self.start, self.destination)
    

@dataclass
class RoutePlan:
    initial_Coords: Coordinate
    trips: list[Trip]

    def complete(self):
        for trip in self.trips:
            trip.complete()
    
    def complete_last(self):
        self.trips[-1].complete()
    
    def last_position(self):
        if self.trips:
            return self.trips[-1].destination
        else:
            self.initial_Coords
    
    def last_time(self):
        if self.trips:
            return self.trips[-1].end_time
    
    def add_customer(self, customer):
        self.trips.append(Trip(start=self.last_position, destination=customer.position, start_time=self.last_time, end_time=None, customer=None))
        self.complete_last()
        self.trips.append(Trip(tart=self.last_position, destination=customer.destination, start_time=self.last_time, end_time=None, customer=customer))
        self.complete_last()


