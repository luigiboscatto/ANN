from methods import *
from math import *

x = [0.5219, 0.8792, 0.9966, 1.1789, 1.4553, 1.7, 1.9403, 2.144, 2.3647, 2.4744, 2.6279, 2.8653]
y = [1.2286, 0.4335, 0.781, 2.5634, 4.312, 7.1011, 11.3381, 15.3168, 20.7444, 24.2791, 29.2422, 40.1543]
values = [0.8529, 0.9546, 1.810]

#linearização, transformando y em ln(y) e x em ln(x)
for i in range(0, len(y)):
    y[i] = log(y[i])

for i in range(0, len(x)):
    x[i] = log(x[i])

matrizA = []
matrizB = []
listPol = []
matrizA, matrizB, listPol = best_poly(x, y, 1) 
z, b = listPol

a = exp(z) # a função te retorna um valor z = ln(a), então isola a e obtém a = exp(z)

print('Coefs:\n',f'{a}, {b}', end=',')

def p(x, a, b):
	return a * pow(x, b)

print()
print('Values:\n')
for value in values:
    print(f'{(p(value, a, b))}', end=", ")
print("")

print("\n\nPARA INSERIR\n")
print(f'{a}, {b}', end=', ')
for value in values:
    print(f'{(p(value, a, b))}', end=", ")
print("")