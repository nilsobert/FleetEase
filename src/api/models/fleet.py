import json
from dataclasses import dataclass, field, asdict
from typing import List, Optional
from uuid import UUID
from .vehicle import Vehicle
from .customer import Customer
from .routePlan import RoutePlan
from .coordinate import Coordinate
from .scenario import Scenario
import fleetStatistics

@dataclass
class Fleet:
    consumption_per_100_km: float
    velocity_in_km_per_hour: float
    total_time_traveled: int
    total_distance_finished_rides: float
    _scenario: Optional[Scenario] = field(default=None, init=False)  # Private field for property storage

    @property
    def scenario(self) -> Optional[Scenario]:
        return self._scenario

    @scenario.setter
    def scenario(self, value: Optional[Scenario]):
        (self.consumption_per_100_km, self.total_time_traveled, self.total_time_traveled, self.total_distance_finished_rides) = fleetStatistics.trigger_calculation(value)
        self._scenario = value

    def to_json(self) -> str:
        fleet_dict = asdict(self)
        if self._scenario:
            fleet_dict['_scenario'] = self._scenario.to_json()
        return json.dumps(fleet_dict, indent=4)
