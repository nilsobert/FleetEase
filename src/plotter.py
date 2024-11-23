from typing import Any
import matplotlib.pyplot as plt
from api.models.coordinate import Coordinate

class Plotter:
    def __init__(self, vehicles, customers) -> None:
        self.vehicles = vehicles
        self.customers = customers
    
    def to_euklidean(coord):
        x, y = coord.as_tuple()
        return x,y
    
    def plot_customers(self):

        # Create a figure and axis
        plt.figure(figsize=(8, 6))

        # Plot points with different colors and sizes
        for customer in self.customers:
            pointx, pointy = customer.position.as_tuple()
            pointx, pointy = [pointx], [pointy]
            
            pointx_d, pointy_d = customer.destination.as_tuple()
            pointx_d, pointy_d = [pointx_d], [pointy_d]
            
            linex = [pointx, pointx_d]
            liney = [pointy, pointy_d]

            plt.plot(linex, liney, color='grey', linewidth=2)
            plt.scatter(pointx, pointy, c="green", s=50)
            plt.scatter(pointx_d, pointy_d, c="blue", s=50)
        
        for vehicle in self.vehicles:
            pointx, pointy = vehicle.routePlan.initial_Coords.as_tuple()
            pointx, pointy = [pointx], [pointy]

            pointx_d, pointy_d = vehicle.routePlan.trips[0].destination.as_tuple()
            pointx_d, pointy_d = [pointx_d], [pointy_d]

            linex = [pointx, pointx_d]
            liney = [pointy, pointy_d]
            print(linex, liney)
            plt.plot(linex, liney, color='red', linewidth=2)
            plt.scatter(pointx, pointy, c="red", s=50)
            


        plt.title("Scatter Points and Line")
        plt.legend()

        # Show the plot
        plt.show()
