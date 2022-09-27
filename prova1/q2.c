#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double k1 = 50800.0; 
double k2 = 57.0;
double m = 90.0;
double g = 9.81;
double h = 0.75;

double f(double x){
    return (2*k2*pow(x, 5/2))/5 + 0.5 * k1 * pow(x, 2) - m*g*x - m*g*h;
}

double df(double x){
    return -g * m + k1 * x + k2 * pow(x, 3/2);
}

void bisection(double(*f)(double), double a, double b, int n) {
	double fa = f(a);
	double fb = f(b);
	if (fa * fb >= 0) {
		printf("Intervalo invalido.\n");
		return;
	} else {
		for (int i = 0; i < n; i++) {
			double m = 0.5 * (a + b);
			double fm = f(m);
			if (fm == 0) {
				printf("Raiz encontrada. r = %.17lf\n", m);
				return;
			}
			if (i + 1 == n) {
        		printf("%.17lf,", m);
      		}
			if (fa * fm < 0) {
				b = m;
			} else {
				a = m;
				fa = fm;
			}
		}
	}
}

void newton(double (*f) (double), double (*df) (double), double x0, int n) {
	for (int i = 0; i < n; i++) {
		double dfx0 = df(x0);

		if (dfx0 == 0) {
			break;
		}
		double xi = x0 - f(x0) / dfx0;
		if (i + 1 == n) {
     		printf("%.17lf,", xi);
    	}
		x0 = xi;
	}
}

void secant(double (*f)(double), double x0, double x1, int n) {
	for (int i = 0; i < n; i++) {
		double fx0 = f(x0);
		double fx1 = f(x1);
		if (fx0 == fx1) {
			break;
		}
		double x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0);
		if (i + 1 == n) {
			printf("%.17lf,", x2);
		}
		x0 = x1;
		x1 = x2;
	}
}

void falsePosition(double (*f)(double), double a, double b, int n) {
	for (int i = 0; i < n; i++) {
		double fa = f(a);
		double fb = f(b);
		if (fa * fb >= 0) {
			return;
		}
		double x = (a * fb - b * fa) / (fb - fa);

		if (i + 1 == n) {
		  printf("%.17lf,", x);
		}

		double fx = f(x);

    if (fx == 0) {
      printf("A raiz procurada e: x = %.17lf, e foi encontrada na %d iteracao",x, i+1);
      return;
    } else {
  		if (fa * fx < 0) {
  			b = x;
  			fb = fx;
  		} else {
  			a = x;
  			fa = fx;
  		}
    }
	}
}

void fixedPoint(double (*f)(double), double x0, int n) {
	for (int i = 0; i < n; i++) {
		x0 = f(x0);
		if (i + 1 == n) {
			printf("%.17lf,", x0);
		}
	}
}

int main(){
    // // metodo bisection
    // double a = 26.26;
    // double b = 200.88;
    // // int n = 12;
    // double tol = 0.000000000000000001;

    // bisection(f, a, b, 12, tol);

    // // metodo newton
    // double x0 = 21.48;
    // // int n = 5;

    // newton(f, df, x0, 5);

    // // metodo secante
    // double x00 = 22.73;
    // double x1 = 39.15;
    // // int n = 10;

    // secant(f, x00, x1, 5);

    // //metodo posiçao falsa
    // double aa = 26.67;
    // double bb = 205.58;
    // // int n = 11;

    // falsePosition(f, aa, bb, 11);

    int iterationsBissection[] = {1, 4, 7 ,10};
	int iterationsNewton[] = {1, 3, 6};
    int iterationsSecant[] = {1, 2, 5, 8};
	int iterationsFalsePosition[] = {2, 5, 7, 11};

    // Método da Bisseção
	for(int i = 0; i < sizeof(iterationsBissection) / sizeof(iterationsBissection[0]); i++) {
		bisection(f, 0.0, 1.4, iterationsBissection[i]);
	}
	printf("\n");

	// Método de Newton
	for(int i = 0; i < sizeof(iterationsNewton) / sizeof(iterationsNewton[0]); i++) {
		newton(f, df, 1.09, iterationsNewton[i]);
	}
	printf("\n");

    // Método da Secante
	for(int i = 0; i < sizeof(iterationsSecant) / sizeof(iterationsSecant[0]); i++) {
		secant(f, 0.99, 2.0, iterationsSecant[i]);
	}
	printf("\n");

	// Método da Posição Falsa
	for(int i = 0; i < sizeof(iterationsFalsePosition) / sizeof(iterationsFalsePosition[0]); i++) {
		falsePosition(f, 0.0, 1.34, iterationsFalsePosition[i]);
	}
	printf("\n");

    return 0; 
}
