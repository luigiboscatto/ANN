#include <stdio.h>
#include <math.h>

void newton(double (*f)(double), double (*df)(double), double x0, int n){
    int iterations[] = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195};
    int j = 0;

    for(int i = 0; i < n; i++){
        double dfx0 = df(x0);
        if(fabs(dfx0) == 0){
            break;
        }
        double xi = x0 - f(x0) / dfx0;
        
        // if(i == 0 || i == 24 || i == 49 || i == 99 || i == 149 || i == 199 || i == 249 ||
        //     i == 299 || i == 349 || i == 399 || i == 449 || i == 499 || i == 549 || i == 599 ||
        //      i == 649 || i == 699){
        //     //printf("x_%d = %.7f\n", i + 1, xi);
        //     printf("%.7f, ", xi);
        // }

        if(i + 1 == iterations[j]){
            // printf("x_%d = %.7f\n", i + 1, xi);
            printf("%.7f, ", xi);
            j++;
        }

        x0 = xi;
    }
}

int main(){
    double f(double x){
        return  x * (x - 1) * (x - 2) + 0.42;
    }

    double df(double x){
        return 3 * (x * x) - 6 * x + 2;
    }

    double x0 = 2.90894103;
    int n = 200;

    newton(f, df, x0, n);
}