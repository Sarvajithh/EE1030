import ctypes


# Load the C shared library
lib = ctypes.CDLL('./libfind_p.so')  # Use .dll for Windows

# Define the C function prototype in Python
lib.find_p.restype = ctypes.c_float
lib.find_p.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]

# Call the C function to get the value of p
x1, y1 = -5, 1
x2 = 1
x3, y3 = 4, -2
p = lib.find_p(x1, y1, x2, x3, y3)
print(f"The value of p for which the points are collinear is: {p:.2f}")

import numpy as np
import matplotlib.pyplot as plt

# Function to find the value of 'p' for which points A, B, and C are collinear
def find_p(x1, y1, x2, x3, y3):
    # We use the fact that the determinant of the following matrix should be zero
    # | x1 y1 1 |
    # | x2  p  1 |
    # | x3 y3 1 |
    
    # Create the matrix (in terms of p)
    matrix = np.array([
        [x1, y1, 1],
        [x2, 0,  1],  # We'll solve for p, so placeholder 0 for now
        [x3, y3, 1]
    ])
    
    # Solve for p by equating the determinant to zero
    def determinant(p):
        matrix[1, 1] = p  # Replace 0 with p in matrix
        return np.linalg.det(matrix)
    
    # We now need to find the value of p such that det(matrix) = 0
    # Since the matrix determinant is a linear equation in terms of p, we solve it directly:
    det_1 = np.linalg.det(np.array([
        [x1, y1, 1],
        [x2, 1,  1],
        [x3, y3, 1]
    ]))
    
    det_2 = np.linalg.det(np.array([
        [x1, y1, 1],
        [x2, 0,  1],
        [x3, y3, 1]
    ]))
    
    # Solve for p such that determinant = 0
    p = 2*-det_2 / det_1
    return p

# Coordinates for points A and C
x1, y1 = -5, 1
x2 = 1
x3, y3 = 4, -2

# Find the value of p for which the points are collinear
p = find_p(x1, y1, x2, x3, y3)
print(f"The value of p for which the points are collinear is: {p:.2f}")

# Points: A(-5, 1), B(1, p), C(4, -2)
A = (x1, y1)
B = (x2, p)
C = (x3, y3)

# Extracting x and y coordinates for plotting
x_coords = [A[0], B[0], C[0]]
y_coords = [A[1], B[1], C[1]]

# Plotting the points
plt.scatter(x_coords, y_coords, color='red', label='Points')

# Labeling the points
plt.text(A[0], A[1], f"A{A}", fontsize=12, ha='right')
plt.text(B[0], B[1], f"B(1, {p:.2f})", fontsize=12, ha='right')
plt.text(C[0], C[1], f"C{C}", fontsize=12, ha='right')

# Plotting lines connecting the points
plt.plot(x_coords, y_coords, color='blue', label='Collinear Line')

# Set plot labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Collinear Points A, B, and C')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Add a grid
plt.grid(True)

# Show the plot with a legend
plt.legend()
plt.show()

