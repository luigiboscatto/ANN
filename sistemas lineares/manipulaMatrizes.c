#include <stdio.h>
#include <math.h>

#define ROW 4
#define COL 4

void imprimeMatriz(double matriz[ROW][COL]){
    for(int row = 0; row < ROW; row++){
        for(int col = 0; col < COL; col++){
            printf("%.16f, ", matriz[row][col]);
        }
        printf("\n");
    }
}

void trocaLinha(double matriz[ROW][COL], int r1, int r2){
        for(int k=0;k<COL;k++){
        double temp = matriz[r1][k];
        matriz[r1][k] = matriz[r2][k];
        matriz[r2][k] = temp;
    }
}

void operacaoEmLinha(double matriz[ROW][COL], int row, double num){
    for(int i = 0; i < COL; i++){
        matriz[row][i] *= num; 
    }
}

void operacaoEmDuasLinhas(double matriz[ROW][COL], int target, int r2, double num){
    for(int i = 0; i < COL; i++){
        matriz[target][i] = (num*matriz[r2][i]) + matriz[target][i];
    }
}

void operacoes(double matriz[ROW][COL]){
    // minhas operaçoes
    operacaoEmDuasLinhas(matriz, 1, 0, (2.0/3.0));

    operacaoEmDuasLinhas(matriz, 2, 0, -(1.0/3.0));

    operacaoEmDuasLinhas(matriz, 3, 0, (2.0/3.0));

    operacaoEmDuasLinhas(matriz, 2, 1, -4.0);

    operacaoEmDuasLinhas(matriz, 3, 1, -(32.0/5.0));

    operacaoEmDuasLinhas(matriz, 3, 2, -(183.0/145.0));

    imprimeMatriz(matriz);
}

int main(){
    double matriz[ROW][COL] = {
		{3, 4, -2, 4}, 
        {-2, -1, 7, 4}, 
        {1, 8, -7, -1},
        {-2, 8, 1, -1}
    };

    printf("Matriz Original:\n");
    imprimeMatriz(matriz);
    printf("\nResultado:\n");
    operacoes(matriz);
    return 0;
}
