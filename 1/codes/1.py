from ctypes import *

# Load the shared object file
centroid = CDLL('./1.so')

# Prepare the arguments for the C function
a = c_float()
b = c_float()
c = c_float()

# Call the C function
centroid.calculate_values(byref(a), byref(b), byref(c))

# Print the results
print("The values of a, b, and c are: a = {:.2f}, b = {:.2f}, c = {:.2f}".format(a.value, b.value, c.value))
import numpy as np
import matplotlib.pyplot as plt

# Solve the equations for a, b, c
# From the equations derived above
# 1. 2a - 4 + 8 = 0
# 2. 4 + 3b + 14 = 0
# 3. 6 + 10 + 2c = 0

# Calculate the values
a = (4 - 8) / 2
b = -(4 + 14) / 3
c = -(10 + 6) / 2

# Triangle vertices
P = np.array([2*a, 2, 6])
Q = np.array([-4, 3*b, -10])
R = np.array([8, 14, 2*c])

# Print the values of a, b, c
print(f"a = {a}, b = {b}, c = {c}")

# Plot the triangle
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(*P, color='r', label='P')
ax.scatter(*Q, color='g', label='Q')
ax.scatter(*R, color='b', label='R')

# Draw the triangle
ax.plot([P[0], Q[0]], [P[1], Q[1]], [P[2], Q[2]], color='k')
ax.plot([Q[0], R[0]], [Q[1], R[1]], [Q[2], R[2]], color='k')
ax.plot([R[0], P[0]], [R[1], P[1]], [R[2], P[2]], color='k')

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Triangle PQR')
ax.legend()

plt.show()

