#include <stdio.h>

void vertices(float Bx, float By, float a, float altitude) {
    // Coordinates of B and C
   Bx = 0, By = 0;  // B(0, 0)
   float Cx = a, Cy = 0;  // C(5.5, 0)
    
    // Coordinates of L (midpoint of BC)
    float Lx = (Bx + Cx) / 2;
    float Ly = 0;      
    // Altitude AL
    float AL = altitude;      // Coordinates of A
    float Ax = Lx;
    float Ay = AL;         
    printf("Coordinates of A: (%.2f, %.2f)\n", Ax, Ay);

    
}

