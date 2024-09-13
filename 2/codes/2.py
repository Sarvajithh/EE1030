from sympy import symbols, Eq, solve

# Define the variable p
p = symbols('p')

# Coordinates of the points A(-5, 1), B(1, p), and C(4, -2)
x1, y1 = -5, 1
x2, y2 = 1, p
x3, y3 = 4, -2

# Define the equation for collinearity (area of triangle = 0)
area_eq = Eq(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2), 0)

# Solve the equation for p
solution = solve(area_eq, p)

# Print the solution
print(f"The value of p for which the points are collinear is: p = {solution}")
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

# Define the variable p
p = symbols('p')

# Coordinates of the points A(-5, 1), B(1, p), and C(4, -2)
x1, y1 = -5, 1
x2 = 1
y3 = -2
x3 = 4

# Collinearity condition equation (area of the triangle = 0)
area_eq = Eq(x1 * (p - y3) + x2 * (y3 - y1) + x3 * (y1 - p), 0)

# Solve for p
solution = solve(area_eq, p)
p_value = float(solution[0])  # Convert symbolic result to float

print(f"The value of p for which the points are collinear is: p = {p_value}")

# Define the points with the calculated p
A = np.array([-5, 1])
B = np.array([1, p_value])
C = np.array([4, -2])

# Create the plot
plt.figure(figsize=(6, 6))

# Plot points A, B, C
plt.scatter(*A, color='red', label='A(-5, 1)')
plt.scatter(*B, color='green', label=f'B(1, {p_value:.2f})')
plt.scatter(*C, color='blue', label='C(4, -2)')

# Plot lines between the points to show collinearity
plt.plot([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='black', linestyle='-', linewidth=1)

# Label axes
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlabel('X')
plt.ylabel('Y')

# Set equal scaling for better visualization
plt.gca().set_aspect('equal', adjustable='box')

# Add grid, title, and legend
plt.grid(True)
plt.title("Collinear Points A, B, and C")
plt.legend()

# Show the plot
plt.show()

