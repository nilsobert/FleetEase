from coordinate import *

class Customer:
    def __init__(self, initial_position:Coordinate, destination:Coordinate, state="waiting", ident:str="def_pass"):
        self.id = ident
        self.initial_position = initial_position 
        self.destination = destination 
        self.state = state  # "waiting" or "travelling"

    def __repr__(self):
        return f"Customer(initial_position={self.initial_position}, destination={self.destination}, state='{self.state}', ident={self.ident})"