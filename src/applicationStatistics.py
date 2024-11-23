from tqdm import tqdm
from time import sleep
import psutil

def demoLiveUsage():
    """
    Displays live CPU and RAM usage using progress bars. (Only for demo)
    """
    with tqdm(total=100, desc='cpu%', position=1) as cpubar, tqdm(total=100, desc='ram%', position=0) as rambar:
        while True:
            rambar.n=psutil.virtual_memory().percent
            cpubar.n=psutil.cpu_percent()
            rambar.refresh()
            cpubar.refresh()
            sleep(0.5)

def get_cpu_usage():
    return psutil.cpu_percent()

def get_ram_usage():
    return psutil.virtual_memory().percent

def getApplicationStatistics(length:int):
    """
    Calculates and returns the average CPU and RAM usage over a specified period.

    Args:
        length (int): The duration in seconds over which to calculate the statistics.

    Returns:
        dict: A dictionary containing the average RAM and CPU usage percentages.
    """
    total_ram = 0
    total_cpu = 0
    time = 0
    running = True
    while running:
        total_ram += get_ram_usage()
        total_cpu += get_cpu_usage()
        time += 1
        if time == length:
            running = False
        sleep(1)
    print(f"Average RAM usage: {round(total_ram/time, 1)}%")
    print(f"Average CPU usage: {round(total_cpu/time, 1)}%")
    return {"Average RAM usage": round(total_ram/time, 1), "Average CPU usage": round(total_cpu/time, 1)}


def get_cpu_usage():
    # Get the current process
    process = psutil.Process()
    # Get the CPU usage as a percentage
    cpu_usage = process.cpu_percent(interval=1)  # The interval defines the time span for sampling
    return cpu_usage



class System:
    def __init__(self) -> None:
        self.number_of_points = 50
        self.cpu = []
        self.ram = []
        self.process = psutil.Process()
        self.interval = 0.3
        self.stop = False
    
    def measure(self):
        while not self.stop:
            self.cpu.append(self.process.cpu_percent(interval=0.2))
            self.ram.append(self.process.memory_percent())
            self.cpu = self.cpu[-min(len(self.cpu), self.number_of_points):]
            self.ram = self.ram[-min(len(self.ram), self.number_of_points):]
            sleep(self.interval)
            print(self.cpu)
            print(self.ram)

if __name__ == "__main__":
    system = System()
    system.measure()
            
