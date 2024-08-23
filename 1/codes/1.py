import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read the values from the C program output (substitute for actual file reading if needed)
a = 1.0  # substitute with actual value
b = -4.0 # substitute with actual value
c = 2.0  # substitute with actual value

# Points calculated
P = [2*a, 2, 6]
Q = [-4, 3*b, -10]
R = [8, 14, 2*c]

# Points in 3D space
x_values = [P[0], Q[0], R[0], P[0]]
y_values = [P[1], Q[1], R[1], P[1]]
z_values = [P[2], Q[2], R[2], P[2]]

# Plot the triangle
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x_values, y_values, z_values, label='Triangle PQR')
ax.scatter([0], [0], [0], color='red', s=100, label='Centroid (0,0,0)')
ax.scatter([P[0], Q[0], R[0]], [P[1], Q[1], R[1]], [P[2], Q[2], R[2]], color='blue')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend()

plt.show()

