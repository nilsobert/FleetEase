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
    
    @property
    def destination(self):
        return Coordinate(self.destinationX, self.destinationY)

    def __repr__(self):
        return (f"Customer(\n"
            f"    coordX={self.coordX},\n"
            f"    coordY={self.coordY},\n"
            f"    destinationX={self.destinationX},\n"
            f"    destinationY={self.destinationY},\n"
            f"    awaitingService={self.awaitingService},\n"
            f"    id={self.id}\n"
            f")")

    
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