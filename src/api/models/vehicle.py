from dataclasses import dataclass
from uuid import UUID
from .coordinate import Coordinate

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

    @property
    def position(self):
        return Coordinate(self.coordX, self.coordY)

    def __repr__(self):
        return (
            f"Vehicle(\n"
            f"    activeTime={self.activeTime},\n"
            f"    coordX={self.coordX},\n"
            f"    coordY={self.coordY},\n"
            f"    customerId={self.customerId},\n"
            f"    distanceTravelled={self.distanceTravelled},\n"
            f"    id={self.id},\n"
            f"    isAvailable={self.isAvailable},\n"
            f"    numberOfTrips={self.numberOfTrips},\n"
            f"    remainingTravelTime={self.remainingTravelTime},\n"
            f"    vehicleSpeed={self.vehicleSpeed}\n"
            f")"
        )

    @staticmethod
    def from_json(data: dict) -> "Vehicle":
        return Vehicle(
            activeTime=data["activeTime"],
            coordX=data["coordX"],
            coordY=data["coordY"],
            customerId=UUID(data["customerId"]) if data["customerId"] else None,
            distanceTravelled=data["distanceTravelled"],
            id=UUID(data["id"]),
            isAvailable=data["isAvailable"],
            numberOfTrips=data["numberOfTrips"],
            remainingTravelTime=data["remainingTravelTime"],
            vehicleSpeed=data["vehicleSpeed"],
        )
