from typing import List
from api.models.coordinate import Coordinate
from api.models.customer import Customer
from dataclasses import dataclass

@dataclass
class Trip:
    start: Coordinate
    destination: Coordinate
    Customer: Customer | None
    start_time: float
    end_time: float | None

    def complete(self):
        if not self.end_time:
            self.end_time = self.start_time + 


@dataclass
class RoutePlan:
    trips: list[Trip]

    def complete(self):
        for trip in self.trips:
            trip.complete()
        

