from dataclasses import dataclass
from typing import List
from uuid import UUID
from .vehicle import Vehicle
from .customer import Customer

@dataclass
class Scenario:
    id: str
    startTime: str
    endTime: str
    status: str
    customers: List[Customer]
    vehicles: List[Vehicle]

    def __repr__(self):
        return f"Scenario(id={self.id}, startTime={self.startTime}, endTime={self.endTime}, status={self.status} customers='{self.customers}', vehicles={self.vehicles})"

    @staticmethod
    def from_json(data: dict) -> "Scenario":
        scenario_data = data.get("scenario", {})
        return Scenario(
            id=scenario_data["id"],
            startTime=scenario_data["startTime"],
            endTime=scenario_data["endTime"],
            status=scenario_data["status"],
            customers=[
                Customer(**customer) for customer in scenario_data.get("customers", [])
            ],
            vehicles=[
                Vehicle(**vehicle) for vehicle in scenario_data.get("vehicles", [])
            ],
        )