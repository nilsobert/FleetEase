class Coordinate:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"Coord:({round(self.x,3)} / {round(self.y,3)})"
    
    def as_tuple(self):
        return (self.x, self.y)