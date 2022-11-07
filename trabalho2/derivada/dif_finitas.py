from methods import *

def f(x):
    return math.exp(math.cos(x)**2) + math.exp(-x**2) + math.log(x)

k = 1 # ordem da derivada
n = 3 # número de pontos

x0 = 7.3736
x = [7.2424, 7.3204, 7.5254]

y = [f(xi) for xi in x]

coeffs = coeffs_dif_fin(x0, x, k)
aprox = dif_fin(coeffs, y)

print('Coefs:')
for i in coeffs:
    print(i,',')
print('Aproximacao:')
print(f'{aprox}')