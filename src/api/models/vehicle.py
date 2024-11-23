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
        return f"Vehicle(activeTime={self.activeTime}, coordX={self.coordX}, coordY='{self.coordY}', customerId={self.customerId}, distanceTravelled={self.distanceTravelled}, id={self.id}, isAvailable={self.isAvailable}, numberOfTrips={self.numberOfTrips}, remainingTravelTime={self.remainingTravelTime}, vehicleSpeed={self.vehicleSpeed})"  