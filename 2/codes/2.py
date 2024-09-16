import ctypes
import matplotlib.pyplot as plt

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
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Add a grid
plt.grid(True)

# Show the plot with a legend
plt.legend()
plt.show()

