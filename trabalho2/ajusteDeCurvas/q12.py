from methods import *
from math import *

x = [0.1569, 0.2712, 0.3484, 0.5171, 0.7617, 0.8386, 1.1008, 1.3112, 1.4697, 1.5579, 1.7469, 1.9917]
y = [5.3309, 6.0126, 7.0135, 10.1174, 13.582, 16.7982, 21.1714, 32.6962, 42.5707, 47.0796, 65.4897, 96.6652]
values = [0.579, 0.9591, 1.3225]

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
	return a * exp(b*x) 

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