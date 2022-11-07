from methods import *

def f(x):
    return math.cos(math.exp(-x**2)) + math.sin(x**2 / 2)

k = 1 # ordem da derivada
n = 9 # número de pontos

x0 = -2.435
x = [-2.6575, -2.6171, -2.524, -2.4688, -2.4118, -2.3529, -2.3387, -2.2536, -2.1907]

y = [f(xi) for xi in x]

coeffs = coeffs_dif_fin(x0, x, k)
aprox = dif_fin(coeffs, y)

print('Coefs:')
for i in coeffs:
    print(i,',')
print('Aproximacao:')
print(f'{aprox}')