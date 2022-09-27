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
            printf("%.10f,\t", bi);
            chute[i]=bi;
        }
        printf("\n");
    }
}


// INSERIR O TAMANHO DA MATRIZ EM DEFINE
//***************************************************************************

int main(){
    double A[L][C] = {
        {-10.79, 3.23, -4.14, 2.3},
        {-1.96, 10.55, 4.16, -3.3},
        {2.09, 3.89, -8.83, 1.73},
        {4.69, 0.46, 2.44, -8.71}
    };
    double B[L]={-4.63, 1.39, 2.71, -1.15}; // result

    double chute[L]= {2.37, -3.87, 2.54, -2.88}; //x0
    int n = 25;

    jacobi(A, B, chute, n);

    return 0;
}
