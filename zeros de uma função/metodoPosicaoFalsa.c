#include <stdio.h>
#include <math.h>

void secant(double (*f)(double), double a, double b, int n){
    int iterations[] = {1 , 25, 50, 100, 200, 400, 800, 1600, 3200, 4800, 6400, 8000, 10000};
    int j = 0;
    
    for(int i = 0; i < n; i++){
        double fa = f(a);
        double fb = f(b);

        if(fa * fb >= 0){
            printf("O teorema de Bolzano nao sabe dizer se existe raiz para f nesse intervalo,");
            break;
        }

        double x1 = (a * fb - b * fa) / (fb - fa);
        // printf("x_%d = %.7f\n", i + 1, x1);

         if(i + 1 == iterations[j]){
            // printf("x_%d = %.7f\n", i + 1, xi);
            printf("%.7f, ", x1);
            j++;
        }

        double fx1 = f(x1);
        if(fa * fx1 < 0){
            b = x1;
            fb = fx1;
        } else {
            a = x1;
            fa = fx1;
        }
    }
}

double f(double x){
    return exp(5 * x) - 2;
}

int main(){
    double a = -0.9597485;
    double b = 1.923124;
    int n = 10000;

    secant(f, a, b, n);
}