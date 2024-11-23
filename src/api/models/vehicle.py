from dataclasses import dataclass
from uuid import UUID

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

    def __repr__(self):
        return f"Vehicle(position={self.position}, charge={self.charge}, state='{self.state}', ident={self.ident})"