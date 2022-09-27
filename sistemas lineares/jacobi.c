#include <stdio.h>
#include <stdlib.h>

#define ROWS 3

void jacobi(double A[ROWS][ROWS], double B[ROWS], double chute[ROWS], int n){
    double next[ROWS];
    for(int k = 0; k < n; k++){
        for(int i = 0; i < ROWS; i++){
            double bi = B[i];
            for(int j = 0; j < ROWS; j++){
                if (j != i){
                    bi -= A[i][j] * chute[j];
                }
            }
            bi /= A[i][i];
            printf("x_%d^(%d) = %.10f\t", i + 1, k + 1, bi);
            next[i] = bi;
        }
        printf("\n");
        for(int i = 0; i < ROWS; i++){
            chute[i] = next[i];
        }
    }
} 

int main(){
    double A[ROWS][ROWS] = {{4, 1, -1}, {-1, 3, 1}, {1, -1, 5}};
    double B[ROWS] = {5, 6, 4};

    double chute[ROWS] = {0, 0, 0};
    int n = 10;

    jacobi(A, B, chute, n);

    return 0;
}

