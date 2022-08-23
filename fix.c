#include <stdio.h>
#include <math.h>

void fixed_point(double(*f)(double), double x0, int n){
    for(int i = 0; i < n; i++){
        double x1 = f(x0);
        printf("x_%d = %.7f\n", i + 1, x1);
        x0 = x1;
    }
}

double f(double x){
    return cos(x);
}

int main(){
    int n = 100;
    double x0 = -0.5;

    fixed_point(f, x0, n);
}
