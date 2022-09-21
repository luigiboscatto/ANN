#include <stdio.h>
#include <math.h>

void fixed_point(double(*f)(double), double x0, int n){
    int iterations[] = {1, 2, 3, 4, 5, 6, 7, 8};
    int j = 0;
    
    for(int i = 0; i < n; i++){
        double x1 = f(x0);
        // printf("x_%d = %.7f\n", i + 1, x1);

        if(i + 1 == iterations[j]){
            // printf("x_%d = %.7f\n", i + 1, xi);
            printf("%.7f, ", x1);
            j++;
        }

        x0 = x1;
    }
}

double f(double x){
    return  ((3 * pow(x, 4) + 2 * pow(x, 2) + 3) / (4 * pow(x, 3) + 4 * x - 1));
}

int main(){
    int n = 100;
    double x0 = 1.40424;

    fixed_point(f, x0, n);
}