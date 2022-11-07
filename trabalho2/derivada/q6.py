from methods import *

def f(x):
    return math.sin(x)**4 - 4*math.sin(x)**2 + math.cos(x**2) + math.exp(-x**2) + 5

k = 3 # ordem da derivada
n = 8 # número de pontos

x0 = 2.5951
x = [2.389, 2.4587, 2.5285, 2.5701, 2.6973, 2.7401, 2.8036]

y = [f(xi) for xi in x]

coeffs = coeffs_dif_fin(x0, x, k)
aprox = dif_fin(coeffs, y)

print('Coefs:')
for i in coeffs:
    print(i,',')
print('Aproximacao:')
print(f'{aprox}')