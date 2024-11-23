from uuid import UUID
from dataclasses import dataclass
from .coordinate import Coordinate

@dataclass
class Customer:
    awaitingService: bool
    coordX: int
    coordY: int
    destinationX: int
    destinationY: int
    id: UUID

    @property
    def position(self):
        return Coordinate(self.coordX, self.coordY)

    def __repr__(self):
        return f"Customer(coordX={self.coordX}, coordY={self.coordY}, destinationX={self.destinationX}, destinationY={self.destinationX} awaitingService='{self.awaitingService}', id={self.id})"
    
    @staticmethod
    def from_json(data: dict) -> "Customer":
        return Customer(
            awaitingService=data["awaitingService"],
            coordX=data["coordX"],
            coordY=data["coordY"],
            destinationX=data["destinationX"],
            destinationY=data["destinationY"],
            id=UUID(data["id"]),
        )