import matplotlib.pyplot as plt
import numpy as np

# Create a new figure and axes for the plot
fig, ax = plt.subplots()

# Set the limits of the plane
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Make the aspect ratio equal so the plane is not stretched
ax.set_aspect('equal', adjustable='box')

# Add a grid to create the "plane" effect
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add x and y axes passing through the origin
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Remove ticks for a cleaner visual
ax.set_xticks(np.arange(-10, 10.1, 1))
ax.set_yticks(np.arange(-10, 10.1, 1))
ax.set_xticklabels([])
ax.set_yticklabels([])

# Add labels for the axes
ax.set_xlabel('X-axis', loc='right')
ax.set_ylabel('Y-axis', loc='top')

# Display the plane
plt.title("Open 2D Plane")
plt.show()
