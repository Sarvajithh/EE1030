#include <stdio.h>

// Function to calculate the determinant of a 3x3 matrix
float determinant(float matrix[3][3]) {
    return matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
         - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
         + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]);
}

// Function to find the value of p for collinear points
float find_p(float x1, float y1, float x2, float x3, float y3) {
    // Determinant equation with y2 replaced by p
    float det_part1, det_part2;

    // Part of determinant without p
    float matrix1[3][3] = {
        {x1, y1, 1},
        {x2, 1, 1},  // Placeholder 1 for p
        {x3, y3, 1}
    };

    // Part of determinant with coefficient of p
    float matrix2[3][3] = {
        {x1, y1, 1},
        {x2, 0, 1},  // Placeholder 0 for now
        {x3, y3, 1}
    };

    // Calculate determinants
    det_part1 = determinant(matrix1);  // Coefficient of p
    det_part2 = determinant(matrix2);  // Constant term

    // Find p such that det = 0
    float p = -det_part2 / det_part1;
    return p;
}

int main() {
    // Coordinates of points A(-5, 1), B(1, p), C(4, -2)
    float x1 = -5, y1 = 1, x2 = 1, x3 = 4, y3 = -2;

    // Calculate the value of p
    float p = find_p(x1, y1, x2, x3, y3);
    printf("The value of p for which the points are collinear is: %.2f\n", p);

    return 0;
}

