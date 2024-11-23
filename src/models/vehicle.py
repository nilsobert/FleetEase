from coordinate import *

class Vehicle:
    def __init__(self, position:Coordinate, charge:int=100, state="idle", ident:str="def_veh"):
        self.id = ident
        self.position = position  
        self.charge = charge  
        self.state = state  # "transporting", "idle", or "preparing"

    def __repr__(self):
        return f"Vehicle(position={self.position}, charge={self.charge}, state='{self.state}', ident={self.ident})"