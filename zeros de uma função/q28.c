#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double f(double x){
    return (9.81 * 81.39)/x - exp(-(x/81.39) * 7.08) * (9.81 * 81.39)/x - 44.55;
}

double df(double x){
    return (exp(-0.0869886 * x) * (69.4548 * x - 798.436 * exp(0.0869886 * x) + 798.436))/(x * x);
}

void bisection(double(*f)(double), double a, double b, int n, double tol){
    int iterations[] = {2, 4, 8, 12};
    int j = 0;
    
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

            if(i + 1 == iterations[j]){
                printf("%.7f, ", m);
                j++;
            }

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

void newton(double (*f)(double), double (*df)(double), double x0, int n){
    int iterations[] = {1, 3, 5};
    int j = 0;

    for(int i = 0; i < n; i++){
        double dfx0 = df(x0);
        if(fabs(dfx0) == 0){
            break;
        }
        double xi = x0 - f(x0) / dfx0;

        if(i + 1 == iterations[j]){
            printf("%.7f, ", xi);
            j++;
        }

        x0 = xi;
    }
}

void secant(double (*f)(double), double x0, double x1, int n){
    int iterations[] = {1, 2, 5};
    int j = 0;
    
    for(int i = 0; i < n; i++){
        double fx0 = f(x0);
        double fx1 = f(x1);

        if(fx0 == fx1){
            break;
        }

        double x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0);
        if(i + 1 == iterations[j]){
            printf("%.7f, ", x2);
            j++;
        }
        
        // printf("x_%d = %.7f\n", i + 2, x2);

        x0 = x1;
        x1 = x2;
    }
}

void falsePosition(double (*f)(double), double a, double b, int n){
    int iterations[] = {2, 4, 7, 11};
    int j = 0;
    
    for(int i = 0; i < n; i++){
        double fa = f(a);
        double fb = f(b);

        if(fa * fb >= 0){
            printf("O teorema de Bolzano nao sabe dizer se existe raiz para f nesse intervalo,");
            break;
        }

        double x1 = (a * fb - b * fa) / (fb - fa);

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

int main(){
    // metodo bisection
    double a = 0.36;
    double b = 58.37;
    // int n = 12;
    double tol = 0.000000000000000001;

    bisection(f, a, b, 12, tol);

    // metodo newton
    double x0 = 1.61;
    // int n = 5;

    newton(f, df, x0, 5);

    // metodo secante
    double x00 = 1.29;
    double x1 = 15.83;
    // int n = 10;

    secant(f, x00, x1, 5);

    //metodo posiçao falsa
    double aa = 1.6;
    double bb = 54.65;
    // int n = 11;

    falsePosition(f, aa, bb, 11);

    return 0; 
}