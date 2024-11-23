from uuid import UUID
from dataclasses import dataclass

@dataclass
class Customer:
    awaitingService: bool
    coordX: int
    coordY: int
    destinationX: int
    destinationY: int
    id: UUID

    def __repr__(self):
        return f"Customer(initial_position={self.initial_position}, destination={self.destination}, state='{self.state}', ident={self.ident})"