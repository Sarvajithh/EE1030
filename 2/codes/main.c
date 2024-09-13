#include <stdio.h>

void find_p() {
    // Coordinates of the points
    int x1 = -5, y1 = 1;
    int x2 = 1, y2;
    int x3 = 4, y3 = -2;

    // Calculate the value of p for which the area is zero
    float p = (float)(-5 * (y3 - y1) + 1 * (y1 - y3) + x3 * (y1 - 1)) / (x1 - x2 + x3);

    printf("The value of p for which the points are collinear is: p = %.2f\n", p);
}

int main() {
    find_p();
    return 0;
}

