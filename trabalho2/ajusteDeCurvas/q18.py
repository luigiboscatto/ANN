from methods import *
from math import *

x = [0.8869, 1.2563, 1.7913, 2.6136, 3.9353, 4.3358, 5.8853, 6.4916, 7.3596, 7.6824, 8.9005, 9.556]
y = [1.856, 2.3664, 2.4833, 2.471, 2.029, 1.8194, 1.1977, 1.018, 0.7723, 0.678, 0.4362, 0.3711]
values = [1.974, 7.4219, 7.7931]

logxy = list()

#linearização, obtendo ln(y) - ln(x), isso é o que vai entrar no lugar de y no best_poly
for i in range(0, len(x)):
    logxy.append(log(y[i]) - log(x[i]))

matrizA = []
matrizB = []
listPol = []
matrizA, matrizB, listPol = best_poly(x, logxy, 1) 
z, b = listPol

a = exp(z) # a função te retorna um valor z = ln(a), então isola a e obtém a = exp(z)

print('Coefs:\n',f'{a}, {b}', end=',')

def p(x, a, b):
	return a * x * exp(b * x)

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