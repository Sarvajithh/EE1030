import ctypes
import matplotlib.pyplot as plt

# Load the C shared library
lib = ctypes.CDLL('./libtriangle.so')  # Use './libtriangle.dll' for Windows

# Define the C function prototype in Python
lib.vertices.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float,
                         ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)]

# Variables for B, a (BC), and altitude
Bx = 0.0
By = 0.0
a = 5.5  # BC = 5.5 units
altitude = 5.3  # Altitude from A to BC

# Create variables to store Ax and Ay (output from C function)
Ax = ctypes.c_float()
Ay = ctypes.c_float()

# Call the C function to calculate the coordinates of A
lib.vertices(Bx, By, a, altitude, ctypes.byref(Ax), ctypes.byref(Ay))

# Print the coordinates of A
print(f"Coordinates of A: ({Ax.value:.2f}, {Ay.value:.2f})")

# Coordinates for points B, C, and A
B = (Bx, By)
C = (a, 0.0)
A = (Ax.value, Ay.value)

# Extract the x and y coordinates for plotting
x_coords = [B[0], C[0], A[0], B[0]]  # Close the triangle by connecting back to B
y_coords = [B[1], C[1], A[1], B[1]]

# Plot the triangle
plt.figure(figsize=(6, 6))
plt.plot(x_coords, y_coords, marker='o', color='b', linestyle='-', label='Triangle ABC')
plt.fill(x_coords, y_coords, 'b', alpha=0.2)  # Fill the triangle for better visualization

# Annotate the points
plt.text(B[0], B[1], 'B(0,0)', fontsize=12, ha='right')
plt.text(C[0], C[1], f'C({a:.1f},0)', fontsize=12, ha='left')
plt.text(A[0], A[1], f'A({A[0]:.2f},{A[1]:.2f})', fontsize=12, ha='center')

# Set the plot limits and labels
plt.xlim(-1, 7)
plt.ylim(-1, 7)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Isosceles Triangle ABC')

# Show the plot
plt.legend()
plt.show()

