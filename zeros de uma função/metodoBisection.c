#include <stdio.h>
#include <math.h>

void bisection(double(*f)(double), double a, double b, int n, double tol){
    double fa = f(a);
    double fb = f(b);
    if(fa * fb >= 0){
        printf("Você não pode usar esse intervalo");
        return;
    } else {
        for(int i = 0; i < n; i++){
            double m = (a + b)/2;
            double fm = f(m);

            if(fm == 0){
                printf("Você encontrou uma raiz r = %.7f", m);
                return;
            }

            // if(i == 1 || i == 2 || i == 5 || i == 6 || i == 7 || i == 8 || i == 9 || i == 14 || i == 15 || i == 18 || i == 21 || i == 22 || i == 26 || i == 27 || i == 28 || i == 29 || i == 31 || i == 35 || i == 37 || i == 38){
            //     printf("%.7f ,", m);
            // }

            printf("x_%d = %.7f\n", i + 1, m);

            // if(fabs(fm) < tol){
            //     printf("atingiu a tolerancia => x_%d = %.7f\n", i + 1, m);
            //     return;
            // }

            if(fabs(b - a) < tol){
                printf("atingiu a tolerancia => x_%d = %.7f\n", i + 1, m);
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
        return pow(x, 3) - 7 * (x * x) + 14 * x - 7;
    }
    double a = 0.1687;
    double b = 1.2631;
    int n = 10;
    double tol = 0.000000000000000001;

    bisection(f, a, b, n, tol);
}