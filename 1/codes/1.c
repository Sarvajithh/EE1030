

#include <stdio.h>

// Function to calculate the values of a, b, and c
void calculate_values(float *a, float *b, float *c) {
    // Solving the equations to find a, b, c
    *a = -2.0;
    *b = -18.0 / 3.0;
    *c = -8.0;
}

int main() {
    float a, b, c;

    // Call the function to calculate the values
    calculate_values(&a, &b, &c);

    // Print the results


    return 0;
}
