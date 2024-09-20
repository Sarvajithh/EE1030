#include <stdio.h>
void vertices(float Bx, float By, float a, float altitude); 
int main(){
	float Bx,By,a,altitude,Ax,Ay;
	vertices(0,0,5.5,5.3);
}



void vertices(float Bx, float By, float a, float altitude) {
    Bx = 0, By = 0; 
    float Cx = a, Cy = 0;  
    
    float Lx = (Bx + Cx) / 2;
    float Ly = 0;      
    float AL = altitude;    
    float Ax = Lx;
    float Ay = AL;         
    printf("Coordinates of A: (%.2f, %.2f)\n", Ax, Ay);

 
}
