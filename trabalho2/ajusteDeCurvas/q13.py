from methods import *
from math import *

x = [0.0357, 0.0965, 0.151, 0.1669, 0.2438, 0.3185, 0.3547, 0.433, 0.4736, 0.5407, 0.5572, 0.6432, 0.6701, 0.7518, 0.8063, 0.8744, 0.93, 0.992, 1.0465, 1.0657, 1.1651, 1.1684, 1.2332, 1.2904, 1.3577, 1.4043, 1.455, 1.5095, 1.6042, 1.6123, 1.6989, 1.7495, 1.8022, 1.8798, 1.9145, 1.9649]
y = [4.649, 4.5228, 5.6932, 3.9013, 7.0706, 5.3295, 10.2222, 8.8373, 10.9833, 9.0448, 10.0766, 9.0518, 10.1621, 12.9259, 13.8639, 14.3563, 15.5521, 17.1085, 17.8681, 18.1979, 20.9045, 20.7635, 22.7329, 24.9382, 26.7618, 28.3345, 33.3488, 33.3165, 37.0568, 36.1848, 42.2715, 41.8396, 48.1886, 49.3838, 53.9771, 58.6927]
values = [0.1189, 0.2753, 1.3541, 1.3614, 1.8476]

#linearização, transformando y em ln(y)
for i in range(0, len(y)):
    y[i] = log(y[i])

matrizA = []
matrizB = []
listPol = []
matrizA, matrizB, listPol = best_poly(x, y, 1)
z, b = listPol

a = exp(z) # a função te retorna um valor z = ln(a), então isola a e obtém a = exp(z)
print('Coefs:\n',f'{a}, {b}', end=',')

def p(x, a, b):
	return a * pow(2, b * x) 

print('Coefs:\n',f'{a}, {b}', end=',')

def p(x, a, b):
	return a * exp(b*x)

print()
print('Values:')
for value in values:
    print(f' {(p(value, a, b))}', end=", ")
print("")
print("\n\nPARA INSERIR\n")
print(f'{a}, {b}', end=', ')
for value in values:
    print(f'{(p(value, a, b))}', end=", ")
print("")