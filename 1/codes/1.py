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

from sympy import symbols, Eq, solve

# Define the symbols
a, b, c = symbols('a b c')

# Define the equations
equation1 = Eq(2*a - 4 + 8, 0)
equation2 = Eq(4 + 3*b + 14, 0)
equation3 = Eq(6 + 10 + 2*c, 0)

# Solve the equations
solution = solve((equation1, equation2, equation3), (a, b, c))

# Print the solutions
print(f"Solution: a = {solution[a]}, b = {solution[b]}, c = {solution[c]}")
# Triangle vertices
P = np.array([2*a, 2, 6])
Q = np.array([-4, 3*b, -10])
R = np.array([8, 14, 2*c])
# Coordinates of the centroid
G = [0, 0, 0]

# Plot the triangle
# Plotting the triangle and its centroid
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the triangle vertices
ax.scatter(*P, color='r', label='P(-12, 2, 6)')
ax.scatter(*Q, color='g', label='Q(-4, -18, -14)')
ax.scatter(*R, color='b', label='R(8, 14, -16)')

# Plot the centroid
ax.scatter(*G, color='k', label='G(0, 0, 0)', marker='o')

# Plot the triangle edges
ax.plot([P[0], Q[0]], [P[1], Q[1]], [P[2], Q[2]], color='r')
ax.plot([Q[0], R[0]], [Q[1], R[1]], [Q[2], R[2]], color='g')
ax.plot([R[0], P[0]], [R[1], P[1]], [R[2], P[2]], color='b')

# Plot lines from the centroid to each vertex
ax.plot([G[0], P[0]], [G[1], P[1]], [G[2], P[2]], color='gray', linestyle='dashed')
ax.plot([G[0], Q[0]], [G[1], Q[1]], [G[2], Q[2]], color='gray', linestyle='dashed')
ax.plot([G[0], R[0]], [G[1], R[1]], [G[2], R[2]], color='gray', linestyle='dashed')

# Setting the labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Triangle PQR and Centroid G')
ax.legend()
plt.show()
