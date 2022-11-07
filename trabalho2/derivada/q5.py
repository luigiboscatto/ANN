from methods import *

def f(x):
    return math.sqrt(math.cos(x**2) + x)

k = 2 # ordem da derivada
n = 8 # número de pontos

x0 = 3.6413
x = [3.4529, 3.4856, 3.5723, 3.583, 3.6673, 3.758, 3.7948, 3.8302]

y = [f(xi) for xi in x]

coeffs = coeffs_dif_fin(x0, x, k)
aprox = dif_fin(coeffs, y)

print('Coefs:')
for i in coeffs:
    print(i,',')
print('Aproximacao:')
print(f'{aprox}')