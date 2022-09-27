#include <stdio.h>
#include <math.h>
#define L 4
#define C 4

void jacobi(double A[L][C], double B[L], double chute[L], int n){
    for(int k=0;k<n;k++){
        printf("%d = ", k + 1);
        for(int i=0;i<L;i++){
            double bi=B[i];
            for(int j=0;j<C;j++){
                if(j!=i) bi-=A[i][j]*chute[j];
            }
            bi/=A[i][i];
            printf("%.10f, ", bi);
            chute[i]=bi;
        }
        printf("\n");
    }
}


// INSERIR O TAMANHO DA MATRIZ EM DEFINE
//***************************************************************************

int main(){
    double A[L][C] = {
        {-9.39, -2.27, 1.64, -3.8},
        {2.09, 5.75, -1.88, -0.1},
        {-4.3, -0.91, -8.1, -1.21},
        {-1.91, -2.46, -3.25, 9.31}
    };
    double B[L]={2.65, 0.94, 4.69, 1.82}; // result

    double chute[L]= {0.51, -1.91, -4.85, 1.99}; //x0
    int n = 28;

    jacobi(A, B, chute, n);

    return 0;
}
