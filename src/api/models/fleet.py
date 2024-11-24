from dataclasses import dataclass
from typing import List
from uuid import UUID
from .vehicle import Vehicle
from .customer import Customer
from .routePlan import RoutePlan
from .coordinate import Coordinate
from .scenario import Scenario

@dataclass
class Fleet:
    consumption_per_100_km: float
    velocity_in_km_per_hour: float
    total_time_traveled: int
    total_distance_finished_rides: float
    scenario: Scenario

    @scenario.setter
    def scenario(self, value):
        self.scenario = value
