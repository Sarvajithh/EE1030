#include <stdio.h>
void find_p(int x1,int y1, int x2, int x3, int y3) {
    float p = (float)(y3*(x2-x1)+y1*(x3-x2))/(x3-x1);
    printf("The value of p for which the points are collinear is: p = %.2f\n", p);
}


