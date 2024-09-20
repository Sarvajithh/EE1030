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
a = 5.5
altitude = 5.3

# Create variables to store Ax and Ay (output from C function)
Ax = ctypes.c_float()
Ay = ctypes.c_float()

# Call the C function to calculate the coordinates of A
lib.vertices(Bx, By, a, altitude, ctypes.byref(Ax), ctypes.byref(Ay))

# Coordinates of the vertices
A = (2.75, 5.3)
B = (0, 0)
C = (5.5, 0)

# Extracting x and y coordinates for plotting
x_coords = [A[0], B[0], C[0], A[0]]  # Closing the triangle by returning to A
y_coords = [A[1], B[1], C[1], A[1]]

# Plotting the triangle
plt.figure(figsize=(6, 6))
plt.plot(x_coords, y_coords, marker='o', color='b', linestyle='-', label='Triangle ABC')
plt.fill(x_coords, y_coords, 'b', alpha=0.2)  # Fill the triangle for better visualization

# Annotate the points
plt.text(A[0], A[1], f'A{A}', fontsize=12, ha='center', color='black')
plt.text(B[0], B[1], f'B{B}', fontsize=12, ha='right', color='black')
plt.text(C[0], C[1], f'C{C}', fontsize=12, ha='left', color='black')

# Set the plot limits and labels
plt.xlim(-1, 7)
plt.ylim(-1, 7)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Triangle ABC')

# Show the plot
plt.legend()
plt.show()

