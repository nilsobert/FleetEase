from dataclasses import dataclass
from uuid import UUID
from .coordinate import Coordinate
from .routePlan import RoutePlan

@dataclass
class Vehicle:
    activeTime: int
    coordX: int
    coordY: int
    customerId: UUID
    distanceTravelled: int
    id: UUID
    isAvailable: bool
    numberOfTrips: int
    remainingTravelTime: int
    vehicleSpeed: int
    routePlan: RoutePlan

    @property
    def position(self):
        return self.routePlan.last_position()

    def __repr__(self):
        return (
            f"Vehicle(activeTime={self.activeTime}, coordX={self.coordX}, coordY={self.coordY}, "
            f"customerId={self.customerId}, distanceTravelled={self.distanceTravelled}, id={self.id}, "
            f"isAvailable={self.isAvailable}, numberOfTrips={self.numberOfTrips}, "
            f"remainingTravelTime={self.remainingTravelTime}, vehicleSpeed={self.vehicleSpeed})"
        )

    @staticmethod
    def from_json(data: dict) -> "Vehicle":
        return Vehicle(
            activeTime=data["activeTime"],
            coordX=data["coordX"],
            coordY=data["coordY"],
            customerId=UUID(data["customerId"]) if data["customerId"] else None,  # Handle None for optional fields
            distanceTravelled=data["distanceTravelled"],
            id=UUID(data["id"]),
            isAvailable=data["isAvailable"],
            numberOfTrips=data["numberOfTrips"],
            remainingTravelTime=data["remainingTravelTime"],
            vehicleSpeed=data["vehicleSpeed"],
            routePlan = RoutePlan(trips=[], initial_Coords=Coordinate(data["coordX"], data["coordY"]))
        )
