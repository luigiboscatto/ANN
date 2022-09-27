#include <stdio.h>

#define numRows 3
#define numCols 3


//so funciona para sistemas nxn
void seidel(double E[numRows][numCols],double chute[numRows],int n ){
    for(int i =0 ; i<n; i++) {
        for(int j =0;j<numRows;j++) {
            double bj = E[j][numCols-1];
            double soma = 0;
            for(int k=0;k<numCols-1;k++) {
                if(k!=j) {
                    soma += E[j][k] * chute[k];
                }
            }
            double xj = (bj - soma ) / E[j][j];
            chute[j] = xj;
            printf("X_%d^(%d) = %.16f\t",j+1,i+1,xj);
        }
        printf("\n");
    }
}

int main() {
    double E[numRows][numCols] = {
        {-5.99, 2.26, 1.99},
        {4.66, -8.16, 1.76},
        {3.61, -2.63, -7.98}
    };

    double chute[numRows] = {0,0,0};
    int n = 10;

    seidel(E,chute,n);

    return 0;
}
