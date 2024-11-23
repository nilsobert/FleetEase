from dataclasses import dataclass
from typing import List
from uuid import UUID
from models.vehicle import Vehicle
from models.customer import Customer
@dataclass
class Scenario:
    customers: List[Customer]
    endTime: str
    id: UUID
    startTime: str
    status: str
    vehicles: List[Vehicle]

    @staticmethod
    def from_json(data: dict) -> "Scenario":
        return Scenario(
            customers=[Customer(**{
                **customer, 
                "id": UUID(customer["id"])
            }) for customer in data["customers"]],
            endTime=data["endTime"],
            id=UUID(data["id"]),
            startTime=data["startTime"],
            status=data["status"],
            vehicles=[Vehicle(**{
                **vehicle,
                "id": UUID(vehicle["id"]),
                "customerId": UUID(vehicle["customerId"])
            }) for vehicle in data["vehicles"]]
        )