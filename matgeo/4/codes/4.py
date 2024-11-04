import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
solution_lib = ctypes.CDLL('./libsolution.so')

# Set the argument types for the 'sol' function
solution_lib.sol.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]

# Define input arrays
m = 3
a = (ctypes.c_int * m)(3, 1, -14)  # int a[3] = {3, 1, -14}
b = (ctypes.c_int * m)(2, 5, -18)  # int b[3] = {2, 5, -18}
x = (ctypes.c_int * (m - 1))()  # int x[2];

# Call the C function
solution_lib.sol(m, a, b, x)

# Retrieve the point from x array
point_x = x[0]
point_y = x[1]

# Print the point
print(f"Point on the circle: ({point_x}, {point_y})")

# Define the center of the circle
center = (1, -2)
# Calculate the radius
radius = np.sqrt((point_x - center[0])**2 + (point_y - center[1])**2)

# Create circle data with more points
theta = np.linspace(0, 2 * np.pi, 1000)  # Increased points for smoother circle
circle_x = center[0] + radius * np.cos(theta)
circle_y = center[1] + radius * np.sin(theta)

# Create line data for 3x + y = 14
x_line1 = np.linspace(center[0] - radius - 2, center[0] + radius + 2, 100)
y_line1 = 14 - 3 * x_line1  # Rearranged: y = 14 - 3x

# Create line data for 2x + 5y = 18
x_line2 = np.linspace(center[0] - radius - 2, center[0] + radius + 2, 100)
y_line2 = (18 - 2 * x_line2) / 5  # Rearranged: y = (18 - 2x) / 5

# Plot the circle and lines
plt.figure(figsize=(8, 8))
plt.plot(circle_x, circle_y, label='Circle', color='blue')
plt.plot(x_line1, y_line1, label='Line: 3x + y = 14', color='orange')
plt.plot(x_line2, y_line2, label='Line: 2x + 5y = 18', color='purple')
plt.scatter(*center, color='red', label='Center (1, -2)')
plt.scatter(point_x, point_y, color='green', label=f'Point ({point_x}, {point_y})')

# Set appropriate limits for better view
plt.xlim(center[0] - radius - 2, center[0] + radius + 2)
plt.ylim(center[1] - radius - 2, center[1] + radius + 2)

plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')  # Ensure the aspect ratio is equal
plt.title('Circle with Center (1, -2), Point from C Code, and Lines')
plt.legend()
plt.show()

