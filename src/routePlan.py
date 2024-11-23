from typing import List
from api.models.coordinate import Coordinate
from api.models.customer import Customer


class routePlan:
    waypoints: List[Coordinate]
    customers: List[Customer]
    timepoints: List[float]