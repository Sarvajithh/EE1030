import matplotlib.pyplot as plt
import numpy as np

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 4))

# Define the beam line
beam_x = [0, 6]
beam_y = [0, 0]
ax.plot(beam_x, beam_y, 'k')  # Beam line

# Define the triangular shape for the force
triangle_x = [1, 3, 5]
triangle_y = [0, 2, 0]
ax.plot(triangle_x, triangle_y, 'k')  # Triangle for distributed load

# Add compression arrow
ax.arrow(1, -0.5, 0, 0.4, head_width=0.2, head_length=0.2, fc='k', ec='k')
ax.text(0.6, -0.8, 'compression', fontsize=10, verticalalignment='center')

# Add tension arrow
ax.arrow(4, 2, 0, -0.8, head_width=0.2, head_length=0.2, fc='k', ec='k')
ax.text(4.1, 1.2, 'tension', fontsize=10, verticalalignment='center')

# Indicate ILD region with text
ax.text(2.5, -0.3, 'ILD', fontsize=12, verticalalignment='center')

# Hide axes
ax.axis('off')

# Set axis limits for better visualization
ax.set_xlim(0, 6)
ax.set_ylim(-1.5, 3)

# Display the plot
plt.show()


