from tqdm import tqdm
from time import sleep
import psutil

def demoLiveUsage():
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

def getStatistics(length:int):
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


if __name__ == "__main__":
   getStatistics(10)