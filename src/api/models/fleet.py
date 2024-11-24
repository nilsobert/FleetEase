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
    total_active_time: float
    energy_consumed_total: float
    total_distance_travelled: float
    vehicles_states: list[dict]
    num_waiting: int
    num_arrived: int
    _scenario: Optional[Scenario] = field(default=None, init=False)  # Private field for property storage

    @property
    def scenario(self) -> Optional[Scenario]:
        return self._scenario

    @scenario.setter
    def scenario(self, value: Optional[Scenario]):
        self.total_active_time, self.total_distance_travelled, self.vehicles_states, self.num_served, self.num_waiting = fleetStatistics.trigger_calculation(value)
        kwhpkm = 18.5
        self.energy_consumed_total = kwhpkm*self.total_distance_travelled
        self._scenario = value

    def to_json(self) -> str:
        fleet_dict = asdict(self)
        if self._scenario:
            fleet_dict['_scenario'] = self._scenario.to_json()
        return json.dumps(fleet_dict, indent=4)
