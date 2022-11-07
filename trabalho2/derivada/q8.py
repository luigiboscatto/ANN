from methods import *

def f(x):
    return x**2 * math.exp(-x) * math.cos(x) + 1

k = 5 # ordem da derivada
n = 15 # número de pontos

x0 = 2.6558
x = [2.4279, 2.4667, 2.479, 2.5129, 2.5674, 2.6027, 2.6218, 2.6663, 2.6808, 2.7204, 2.7705, 2.7819, 2.8237, 2.8583, 2.8981]

y = [f(xi) for xi in x]

coeffs = coeffs_dif_fin(x0, x, k)
aprox = dif_fin(coeffs, y)

print('Coefs:')
for i in coeffs:
    print(i,',')
print('Aproximacao:')
print(f'{aprox}')