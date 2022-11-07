from methods import *
from math import *

x = [0.2414, 0.4782, 0.6235, 0.9801, 1.0901, 1.5233, 1.6459, 1.9383, 2.1531, 2.2719, 2.634, 2.8609, 3.0605, 3.3231, 3.5551, 3.7167, 4.081, 4.3435, 4.3774, 4.806, 5.0369, 5.2413, 5.4687, 5.7311, 5.8496, 6.0881, 6.3694, 6.5867, 6.7306, 6.9813, 7.2333, 7.5603, 7.8515, 7.9871, 8.1737, 8.5521, 8.7438, 8.9414, 9.1383, 9.5284, 9.6737, 9.9058]
y = [0.7579, 1.3687, 1.662, 2.2118, 2.3178, 2.6569, 2.7182, 2.7925, 2.8311, 2.8301, 2.7882, 2.7662, 2.642, 2.7318, 2.4771, 2.3791, 2.2155, 2.2713, 2.104, 1.8879, 1.7853, 1.6768, 1.6102, 1.4784, 1.5348, 1.3225, 1.2223, 1.1322, 1.1055, 1.0167, 0.9286, 0.8514, 0.824, 0.7436, 0.6869, 0.5974, 0.5989, 0.5564, 0.5176, 0.45, 0.4164, 0.3746]
values = [4.6784, 4.8164, 7.2775, 8.6656, 9.6118]

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