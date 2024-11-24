from dataclasses import dataclass, field
from typing import List
from uuid import UUID
from .vehicle import Vehicle
from .customer import Customer
from .routePlan import RoutePlan
from .coordinate import Coordinate
from .scenario import Scenario

from typing import Optional

@dataclass
class Fleet:
    consumption_per_100_km: float
    velocity_in_km_per_hour: float
    total_time_traveled: int
    total_distance_finished_rides: float
    _scenario: Optional[Scenario] = field(default=None, init=False)  # Private field for property storage

    @property
    def scenario(self) -> Optional[Scenario]:
        """Getter for the scenario."""
        return self._scenario

    @scenario.setter
    def scenario(self, value: Optional[Scenario]):
        """Setter for the scenario with custom logic (if needed)."""
        print("setting fleet")
        self._scenario = value