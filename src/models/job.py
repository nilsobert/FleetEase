from datetime import datetime
from .customer import *
from .vehicle import *

class Job:
    def __init__(self, request_time:datetime, customer:Customer, vehicle:Vehicle, state:str="preparing", pickup_time:datetime|None=None, completion_time:datetime|None=None) -> None:
        self.request_time: datetime = request_time
        self.state: str = state # preparing | transporting | complete
        self.pickup_time: datetime | None = pickup_time
        self.customer: Customer = customer
        self.vehicle: Vehicle = vehicle
        self.completion_time: datetime = completion_time
    
    def complete(self, time:datetime=datetime.now()):
        self.state = "complete"
        self.completion_time = time