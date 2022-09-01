#include <stdio.h>
#include <math.h>

void secant(double (*f)(double), double x0, double x1, int n){
    for(int i = 0; i < n; i++){
        double fx0 = f(x0);
        double fx1 = f(x1);

        if(fx0 == fx1){
            break;
        }

        double x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0);
        printf("x_%d = %.7f\n", i + 2, x2);

        x0 = x1;
        x1 = x2;
    }
}

int main(){
    double f(double x){
        return 2 * (x + 1) * (x - 0.5) * (x - 1);
    }

    double x0 = -0.42099;
    double x1 = 0.69742 ;
    int n = 10;

    secant(f, x0, x1, n);
}