#include <stdio.h>
#include <math.h>

void newton(double (*f)(double), double (*df)(double), double x0, int n){
    for(int i = 0; i < n; i++){
        double dfx0 = df(x0);
        if(fabs(dfx0) == 0){
            break;
        }
        double xi = x0 - f(x0) / dfx0;
        
        if(i == 0 || i == 24 || i == 49 || i == 99 || i == 149 || i == 199 || i == 249 ||
            i == 299 || i == 349 || i == 399 || i == 449 || i == 499 || i == 549 || i == 599 ||
             i == 649 || i == 699){
            //printf("x_%d = %.7f\n", i + 1, xi);
            printf("%.7f, ", xi);
        }
        x0 = xi;
    }
}

int main(){
    double f(double x){
        return  exp(5 * x) - 2;
    }

    double df(double x){
        return 5 * exp(5 * x);
    }

    double x0 = -1.16286014;
    int n = 700;

    newton(f, df, x0, n);
}