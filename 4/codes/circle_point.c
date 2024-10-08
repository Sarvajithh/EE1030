#include <stdio.h>

void sol(int m, int a[m], int b[m], int x[m-1]){
	int p,q;
	p = (a[1]*b[2]-a[2]*b[1])/(a[0]*b[1]-a[1]*b[0]);
	q = (a[2]*b[0] - a[0]*b[2])/(a[0]*b[1] - a[1]*b[0]);
	x[0] = p;
	x[1] = q;
}

