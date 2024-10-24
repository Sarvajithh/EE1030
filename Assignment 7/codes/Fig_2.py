import matplotlib.pyplot as plt
import numpy as np

# Create a figure and set of subplots with specified height ratios
fig, ax = plt.subplots(2, 1, figsize=(10, 6), gridspec_kw={'height_ratios': [2, 1]})

# Truss structure points
points = {
    'R': (0, 0), 'P': (2, 2), 'S': (4, 0), 'Q': (6, 2), 'C': (8, 0)
}

# Define truss members as pairs of points
members = [
    ('R', 'P'), ('P', 'Q'), ('Q', 'C'),  # Top chord
    ('R', 'S'), ('S', 'C'),              # Bottom chord
    ('R', 'Q'), ('P', 'S'), ('S', 'Q')   # Diagonals
]

# Plot the truss members
for start, end in members:
    x_vals = [points[start][0], points[end][0]]
    y_vals = [points[start][1], points[end][1]]
    ax[0].plot(x_vals, y_vals, 'k', linewidth=1.5)

# Label the points
for point, coord in points.items():
    ax[0].text(coord[0], coord[1] + 0.1, point, fontsize=12, ha='center')

# Add supports
ax[0].plot(points['R'][0], points['R'][1], 'k^', markersize=10)  # Pinned support at R
ax[0].plot(points['C'][0], points['C'][1], 'ko', markersize=6)   # Roller support at C

# Set limits and remove axes for the truss plot
ax[0].set_xlim(-1, 9)
ax[0].set_ylim(-1, 3)
ax[0].axis('off')

# ILD: Define the influence line data
x_ild = [0, 2, 4, 8]
y_ild = [-0.5, 1, 0.3, 0]

# Plot the ILD line
ax[1].plot(x_ild, y_ild, 'k', linewidth=1.5)

# Add the straight line connecting the start and end points of the ILD
ax[1].plot([0, 8], [-0.5, 0], 'k', linewidth=1.5)  # Solid line for reference

# Annotate ILD with arrows for compression and tension
ax[1].annotate('compression', xy=(0, -0.5), xytext=(-0.5, -0.7),
               arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10)
ax[1].annotate('tension', xy=(4, 1), xytext=(5, 1.2),
               arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=10)

# Set limits and remove axes for ILD plot
ax[1].set_xlim(-1, 9)
ax[1].set_ylim(-1, 1.5)
ax[1].axis('off')

# Show the plot
plt.tight_layout()
plt.show()

