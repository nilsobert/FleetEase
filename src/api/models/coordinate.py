class Coordinate:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def as_tuple(self):
        return (self.x, self.y)