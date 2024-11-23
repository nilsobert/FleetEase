import matplotlib.pyplot as plt

# Example data
points_x = [1, 2, 3, 4, 5]
points_y = [2, 3, 5, 7, 11]
point_colors = ['red', 'blue', 'green', 'orange', 'purple']
point_sizes = [50, 100, 150, 200, 250]

line_x = [1, 2]
line_y = [1, 4]

# Create a figure and axis
plt.figure(figsize=(8, 6))

# Plot points with different colors and sizes
plt.scatter(points_x, points_y, c=point_colors, s=point_sizes, label="Points")

# Plot a line
plt.plot(line_x, line_y, color='black', linewidth=2, label="Line")

# Add labels, title, and legend
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Points and Line")
plt.legend()

# Show the plot
plt.show()
