#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX_ITER 1000
#define EPSILON 1e-10


double** allocateMatrix(int n) {
    double** matrix = (double**)malloc(n * sizeof(double*));
    for (int i = 0; i < n; i++) {
        matrix[i] = (double*)malloc(n * sizeof(double));
    }
    return matrix;
}


void freeMatrix(double** matrix, int n) {
    for (int i = 0; i < n; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

void multiplyMatrices(double** A, double** B, double** C, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            C[i][j] = 0;
            for (int k = 0; k < n; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}


void transposeMatrix(double** A, double** B, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            B[j][i] = A[i][j];
        }
    }
}


void qrDecomposition(double** A, double** Q, double** R, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            Q[i][j] = A[i][j];
        }
    }


    for (int j = 0; j < n; j++) {
        R[j][j] = 0;
        for (int i = 0; i < n; i++) {
            R[j][j] += Q[i][j] * Q[i][j];
        }
        R[j][j] = sqrt(R[j][j]);
        
        for (int i = 0; i < n; i++) {
            Q[i][j] /= R[j][j];
        }
        
        for (int k = j + 1; k < n; k++) {
            R[j][k] = 0;
            for (int i = 0; i < n; i++) {
                R[j][k] += Q[i][j] * Q[i][k];
            }
            for (int i = 0; i < n; i++) {
                Q[i][k] -= R[j][k] * Q[i][j];
            }
        }
    }
}

void qrAlgorithm(double** A, int n) {
    double** Q = allocateMatrix(n);
    double** R = allocateMatrix(n);
    double** temp = allocateMatrix(n);

    for (int iter = 0; iter < MAX_ITER; iter++) {
        qrDecomposition(A, Q, R, n);  
        multiplyMatrices(R, Q, temp, n);
        int converged = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j && fabs(A[i][j]) > EPSILON) {
                    converged = 0;
                    break;
                }
            }
            if (!converged) break;
        }

        if (converged) break;

        // Update A with the new values
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A[i][j] = temp[i][j];
            }
        }
    }

    printf("Eigenvalues:\n");
    for (int i = 0; i < n; i++) {
        printf("%lf ", A[i][i]);  // Eigenvalues are on the diagonal
    }
    printf("\n");

    freeMatrix(Q, n);
    freeMatrix(R, n);
    freeMatrix(temp, n);
}

int main() {
    int n;
    printf("Enter the dimension of the matrix: ");
    scanf("%d", &n);

    double** A = allocateMatrix(n);
    printf("Enter the elements of the matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%lf", &A[i][j]);
        }
    }

    qrAlgorithm(A, n);

    freeMatrix(A, n);
    return 0;
}
