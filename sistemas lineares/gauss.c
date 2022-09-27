#include <stdio.h>
#define NUMROWS 3
#define NUMCOLS 4

void gauss(double E[NUMROWS][NUMCOLS]);
void reverse_substitution(double E[NUMROWS][NUMCOLS]);
void printMatrix(double m[NUMROWS][NUMCOLS]);

int main()
{
    double E[NUMROWS][NUMCOLS];
     FILE *fr = fopen("matriz.txt", "r+");
    for (int i = 0; i < NUMROWS; i += 1)
    {
        for (int j = 0; j < NUMCOLS; j += 1)
        {
            fscanf(fr, "%lf, ", &E[i][j]);
        }
    }
    gauss(E);
    return 0;
}
void printMatrix(double m[NUMROWS][NUMCOLS])
{
    printf("\n");
    for (int i = 0; i < NUMROWS; i += 1)
    {
        for (int j = 0; j < NUMCOLS; j += 1)
        {
            printf("%.8f, ", m[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void reverse_substitution(double E[NUMROWS][NUMCOLS])
{
    double answer[NUMROWS];

    for (int i = 0; i < NUMROWS; i++)
    {
        int d = NUMROWS - 1 - i;
        double b = E[d][NUMCOLS - 1];
        for (int j = d + 1; j < NUMCOLS - 1; j++)
        {
            b -= E[d][j] * answer[j];
        }
        double xd = b / E[d][d];
        answer[d] = xd;
        printf("X_%d = %.16f\n", d, xd);
    }
}
void gauss(double E[NUMROWS][NUMCOLS])
{
    for (int j = 0; j < NUMCOLS - 1; j += 1)
    {
        for (int i = j; i < NUMROWS; i += 1)
        {
            if (E[i][j] != 0)
            {
                if (i != j)
                {
                    for (int k = 0; k < NUMCOLS; k += 1)
                    {
                        double temp = E[i][k];
                        E[i][k] = E[j][k];
                        E[j][k] = temp;
                    }
                    printf("L%d <-> L%d\n", j + 1, i + 1);
                }

                for (int k = j + 1; k < NUMROWS; k += 1)
                {
                    double m = -E[k][j] / E[j][j];
                    printf("L%d -> %.4f*L%d + L%d\n", k + 1, m, k + 1, j + 1);
                    for (int p = j; p < NUMCOLS; p += 1)
                    {
                        E[k][p] += m * E[j][p];
                    }
                }
                printMatrix(E);
                break;
            }
        }
    }
    reverse_substitution(E);
}
