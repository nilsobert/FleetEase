from tqdm import tqdm
from time import sleep
import psutil
import numpy as np


class System:
    def __init__(self) -> None:
        self.number_of_points = 50
        self.cpu = []
        self.ram = []
        self.process = psutil.Process()
        self.interval = 0.2
        self.stop = False
        self._time = list(np.array(list(range(self.number_of_points))[::-1])*-0.5)
        self.time = []
    
    def measure(self):
        while not self.stop:
            self.cpu.append(self.process.cpu_percent(interval=0.3))
            self.ram.append(round(self.process.memory_percent(),3))
            self.cpu = self.cpu[-min(len(self.cpu), self.number_of_points):]
            self.ram = self.ram[-min(len(self.ram), self.number_of_points):]
            self.time = self._time[-min(len(self.ram), self.number_of_points):]
            sleep(self.interval)
            
    
    def json(self):
        return {
            "cpu":self.cpu,
            "ram": self.ram,
            "time": self.time
        }

            

if __name__ == "__main__":
    system = System()
    system.measure()
            
