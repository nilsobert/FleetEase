from dataclasses import dataclass
from typing import List
from uuid import UUID
from .vehicle import Vehicle
from .customer import Customer
from .routePlan import RoutePlan
from .coordinate import Coordinate

@dataclass
class Scenario:
    id: UUID
    startTime: str
    endTime: str
    status: str
    customers: List[Customer]
    vehicles: List[Vehicle]

    def __repr__(self):
        return (f"Scenario(\n"
            f"    id={self.id},\n"
            f"    startTime={self.startTime},\n"
            f"    endTime={self.endTime},\n"
            f"    status={self.status},\n"
            f"    customers={self.customers},\n"
            f"    vehicles={self.vehicles}\n"
            f")")

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
                Vehicle(routePlan=RoutePlan(trips=[], initial_Coords=Coordinate(vehicle["coordX"], vehicle["coordY"])), **vehicle) for vehicle in scenario_data.get("vehicles", [])
            ],
        )
    
    @staticmethod
    def from_json_plain(data: dict) -> "Scenario":
        return Scenario(
            id=data["id"],
            startTime=data["startTime"],
            endTime=data["endTime"],
            status=data["status"],
            customers=[
                Customer(**customer) for customer in data.get("customers", [])
            ],
            vehicles=[
                Vehicle(**vehicle) for vehicle in data.get("vehicles", [])
            ],
        )