import matplotlib.pyplot as plt
import numpy as np

# Set up the figure and axis
fig, ax = plt.subplots(2, 1, figsize=(8, 6))

# ---------------------- Truss Diagram ---------------------- #
# Coordinates for truss nodes
truss_x = [0, 2, 4, 6, 8, 10, 12]
truss_y = [0, 2, 0, 2, 0, 2, 0]

# Draw truss members
ax[0].plot([0, 2], [0, 2], 'k')  # PR
ax[0].plot([2, 4], [2, 0], 'k')  # PQ
ax[0].plot([4, 6], [0, 2], 'k')  # QS
ax[0].plot([6, 8], [2, 0], 'k')  # ST
ax[0].plot([8, 10], [0, 2], 'k') # RT

ax[0].plot([0, 4], [0, 0], 'k')  # Bottom chord PR -> RS
ax[0].plot([4, 10], [0, 0], 'k') # Bottom chord RS -> T
ax[0].plot([2, 6], [2, 2], 'k')  # Top chord PQ -> QS

# Plot the supports
ax[0].plot(0, 0, marker='^', markersize=10, color='black')   # Left Support
ax[0].plot(10, 0, marker='^', markersize=10, color='black')  # Right Support

# Label points
ax[0].text(0, 0, 'R', fontsize=12, ha='center', va='top')
ax[0].text(2, 2, 'P', fontsize=12, ha='center', va='bottom')
ax[0].text(4, 0, 'S', fontsize=12, ha='center', va='top')
ax[0].text(6, 2, 'Q', fontsize=12, ha='center', va='bottom')
ax[0].text(10, 0, 'T', fontsize=12, ha='center', va='top')

# Formatting
ax[0].set_title('Truss Diagram')
ax[0].set_xlim([-1, 12])
ax[0].set_ylim([-1, 3])
ax[0].axis('off')

# ---------------------- ILD Diagram ---------------------- #
# Influence line diagram data
x_ild = [0, 2, 4, 6, 8, 10]
y_ild = [0, 0.5, 1, 0.5, 0, 0] 

ax[1].plot(x_ild, y_ild, 'k', lw=1.5)

# Mark compression and tension arrows
ax[1].annotate('compression', xy=(1, 0.5), xytext=(-1, -0.5),
               arrowprops=dict(facecolor='black', shrink=0.05),
               fontsize=10)

ax[1].annotate('tension', xy=(7, 0.5), xytext=(8, 1),
               arrowprops=dict(facecolor='black', shrink=0.05),
               fontsize=10)

# Label ILD
ax[1].text(4, 1.1, 'ILD', fontsize=12, ha='center')

# Formatting
ax[1].set_title('Influence Line Diagram')
ax[1].set_xlim([-1, 12])
ax[1].set_ylim([-1, 2])
ax[1].axis('off')

# Show the plot
plt.tight_layout()
plt.show()
