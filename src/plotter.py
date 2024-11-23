from typing import Any
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from api.models.coordinate import Coordinate

class Plotter:
    def __init__(self, vehicles, customers) -> None:
        self.vehicles = vehicles
        self.customers = customers
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.time_step = 0
        self.completed_customers =[]

    def update_frame(self, frame):
        self.ax.clear()  # Clear the previous frame

        # Plot customers with their destinations
        

        for customer in self.customers:
            pointx, pointy = customer.position.as_tuple()
            pointx_d, pointy_d = customer.destination.as_tuple()

            linex = [pointx, pointx_d]
            liney = [pointy, pointy_d]
            if not customer in self.completed_customers:
                self.ax.plot(linex, liney, color='grey', linewidth=2)
                self.ax.scatter([pointx], [pointy], c="green", s=50)
            self.ax.scatter([pointx_d], [pointy_d], c="blue", s=50)

        # Plot vehicles and their trips
        for vehicle in self.vehicles:
            if not vehicle.routePlan.trips:
                pointx, pointy = vehicle.routePlan.initial_Coords.as_tuple()
            elif len(vehicle.routePlan.trips) <= frame:
                pointx, pointy = vehicle.position.as_tuple()

            if len(vehicle.routePlan.trips) > frame:
                pointx, pointy = vehicle.routePlan.trips[frame].start.as_tuple()
                pointx_d, pointy_d = vehicle.routePlan.trips[frame].destination.as_tuple()
                if vehicle.routePlan.trips[frame].customer:
                    if vehicle.routePlan.trips[frame].customer in self.completed_customers:
                        print("öasldfjöalksdjfölkasdjfölkasdjf")
                    self.completed_customers.append(vehicle.routePlan.trips[frame].customer)
                linex = [pointx, pointx_d]
                liney = [pointy, pointy_d]
                self.ax.plot(linex, liney, color='red', linewidth=2)

            self.ax.scatter([pointx], [pointy], c="red", s=50)

        # Update the title with the time step
        self.ax.set_title(f"Step: {frame}")
        self.ax.set_ylim(11.48, 11.65)
        self.ax.set_xlim(48.1, 48.18)
        self.ax.legend(["Customer-Destination", "Vehicle Route"], loc="upper left")
        print(len(self.customers), len(self.completed_customers))

    def animate(self, frames):
        # Total number of frames in the animation
        total_frames = frames

        # Create the animation
        animation = FuncAnimation(
            self.fig,
            self.update_frame,
            frames=total_frames,
            interval=2000,  # Interval between frames in ms
            repeat=False
        )

        plt.show()
