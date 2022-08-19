#include <stdio.h>

void bisection(double(*f)(double), double a, double b, int n, double tol){
    double fa = f(a);
    double fb = f(b);
    if(fa * fb >= 0){
        printf("Você não pode usar esse intervalo");
        return;
    } else {
        for(int i = 0; i < n; i++){
            double m = 0.5 * (a + b);
            double fm = f(m);

            if(fm == 0){
                printf("Você encontrou uma raiz r = %.16f", m);
                return;
            }
            printf("x_%d = %.16f\n", i + 1, m);
            if(fabs(fm) < tol){
                printf("atingiu a tolerancia => x_%d = %.16f\n", i + 1, m);
                return;
            }
            if(fa * fm < 0){
                b = m;
            } else {
                a = m;
                fa = fm;
            }
        }
    }
}

int main(){
    double f(double x){
        return x * x - 3;
    }
    double a = 1;
    double b = 2;
    int n = 100;
    double tol = 0.0001;

    bisection(f, a, b, n, tol);
}
