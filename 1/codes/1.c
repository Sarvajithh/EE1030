#include <stdio.h>

int main() {
    // Given points
    int x1 = 2, x2 = -4, x3 = 8;
    int y1 = 2, y2 = 3, y3 = 14;
    int z1 = 6, z2 = -10, z3 = 2;

    // Variables to store a, b, c
    double a, b, c;

    // Calculate the values of a, b, c
    a = (4.0 - x2 - x3) / x1;
    b = (-16.0 - y2 - y3) / y1;
    c = (4.0 - z2 - z3) / z1;

    // Output the points and centroid
    printf("a = %.2f\nb = %.2f\nc = %.2f\n", a, b, c);
    printf("P(%.2f, %d, %d)\n", 2*a, y1, z1);
    printf("Q(%d, %.2f, %d)\n", x2, 3*b, z2);
    printf("R(%d, %d, %.2f)\n", x3, y3, 2*c);
    printf("Centroid: (0, 0, 0)\n");

    return 0;
}

