#include <stdio.h>

// Function to calculate the value of p
float find_p(int x1, int y1, int x2, int x3, int y3) {
    // Calculate the value of p for which the area is zero
    float p = (float)(y3*(x2-x1) + y1*(x3-x2)) / (x3-x1);
    return p;
}

int main(){
    // Test the function
    float p = find_p(-5, 1, 1, 4, -2);
    printf("The value of p for which the points are collinear is: p = %.2f\n", p);
    return 0;
}

