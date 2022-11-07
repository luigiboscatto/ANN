from methods import *
from math import *

x = [1.8177, 4.0636, 4.5658, 6.9782, 8.5569, 8.9509, 11.23, 12.2802, 13.7248, 16.5298, 17.0854, 18.8101]
y = [0.8296, 1.4092, 1.4627, 1.8153, 2.01, 1.9609, 2.1174, 2.1607, 2.2469, 2.3643, 2.3551, 2.4042]
values = [6.9528, 10.5924, 17.5916]

#linearização, transformando y em 1/y e x em 1/x
for i in range(0, len(y)):
    y[i] = 1/y[i]

for i in range(0, len(x)):
    x[i] = 1/x[i]

matrizA = []
matrizB = []
listPol = []
matrizA, matrizB, listPol = best_poly(x, y, 1)
z, w = listPol

a = 1/z # a função te retorna um valor z = ln(a), então isola a e obtém a = exp(z)
b = a * w
print('Coefs:\n',f'{a}, {b}', end=', ')

def p(x, a, b):
	return a * (x/(x+b))

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