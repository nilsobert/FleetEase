from api.models.fleet import Fleet



class Synchronizer:
    def __init__(self) -> None:
        self.fleet = Fleet(0, 0, 0, 0,0,0)
        self.system = {}
    def reset(self):
        self.fleet = Fleet(0, 0, 0, 0,0,0)
        self.system = {}
    